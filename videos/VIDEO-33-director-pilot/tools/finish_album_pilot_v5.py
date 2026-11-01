"""Verify and register only the album-based S05 pilot, retaining prior versions."""
import json,subprocess,wave,hashlib
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageOps
from prepare import ROOT,digest
from s05_album_pilot_v5 import OUT

def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2) if isinstance(v,(dict,list)) else v,encoding='utf-8')
def run(a):return subprocess.run(a,check=True,capture_output=True).stdout

def main():
    d=read(OUT/'DIRECTION.json');video=OUT/'renders/pilot.mp4';status=read(ROOT/'production_status.json')
    old_s09=next(x for x in status['revised_pilot_renders'] if x['scene_id']=='S09')
    assert digest(ROOT/old_s09['video_path'])==old_s09['video_sha256']
    approved=read(ROOT/'research/visual-approvals.json')
    approved_frame=next(x for x in approved['approved'] if x['scene_id']=='S05' and x['version']=='final-frame-v5')
    assert digest(ROOT/approved_frame['frame_path'])==approved_frame['frame_sha256']
    probe=json.loads(run(['ffprobe','-v','error','-show_streams','-of','json',str(video)]))
    vs=next(x for x in probe['streams'] if x['codec_type']=='video');aus=next(x for x in probe['streams'] if x['codec_type']=='audio')
    assert (vs['width'],vs['height'],vs['avg_frame_rate'])==(720,1280,'30/1')
    with wave.open(str(OUT/'assets/voice.wav'),'rb') as w:pcm=w.readframes(w.getnframes())
    with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:w.setpos(d['source_start_sample']);expected=w.readframes(d['source_end_sample']-d['source_start_sample'])
    assert pcm==expected
    decoded=run(['ffmpeg','-v','error','-i',str(video),'-vn','-ac','1','-ar','24000','-f','s16le','-'])
    a=np.frombuffer(pcm,np.int16).astype(float)/32768;b=np.frombuffer(decoded,np.int16).astype(float)/32768;n=min(len(a),len(b))
    corr=float(np.corrcoef(a[:n],b[:n])[0,1]);rms=float(np.sqrt(np.mean(b*b)))
    assert corr>.98 and rms>.001 and abs(float(vs['duration'])-d['duration'])<.05
    qa=OUT/'qa';qa.mkdir(exist_ok=True)
    sheet=Image.new('RGB',(1080,1340),'#FFF3E8');draw=ImageDraw.Draw(sheet);font=ImageFont.truetype(str(ROOT/'assets/fonts/segoe-ui-black.ttf'),22)
    for i,t in enumerate(d['proof_times']):
        f=qa/f'frame-{t:.2f}.png';run(['ffmpeg','-y','-v','error','-ss',str(t),'-i',str(video),'-frames:v','1',str(f)])
        im=Image.open(f).convert('RGB');mobile=im.resize((360,640),Image.Resampling.LANCZOS);mobile.save(qa/f'mobile-{t:.2f}.png')
        sheet.paste(mobile,((i%3)*360,(i//3)*670+30));draw.text(((i%3)*360+10,(i//3)*670+5),f'{t:.2f}s',font=font,fill='#30313B')
        footer=np.array(im)[1080:,:,:];assert int((footer.max(axis=(0,1))-footer.min(axis=(0,1))).max())<12
    sheet.save(OUT/'FRAME_PROOFS.jpg',quality=93)
    final=Image.open(qa/'frame-5.35.png').convert('RGB');final.resize((360,640)).save(OUT/'MOBILE_FINAL.png');ImageOps.grayscale(final).resize((180,320)).save(OUT/'GRAYSCALE.png')
    check=read(OUT/'qa-check.json');assert check['ok'] and not check['browserSkipped']
    assert all(check[x]['errorCount']==0 for x in ['lint','runtime','layout','contrast'])
    # A lossless browser snapshot isolates layout parity from ordinary AAC/H.264 encoding.
    snapshot=Image.open(OUT/'FINAL_CHECK.png').convert('RGB');reference=Image.open(ROOT/approved_frame['frame_path']).convert('RGB')
    lossless_difference=np.abs(np.array(snapshot).astype(float)-np.array(reference).astype(float))
    report={**d,'video_path':str(video.relative_to(ROOT)),'video_sha256':digest(video),'video_duration':float(vs['duration']),'audio_duration':float(aus['duration']),'video_frames':int(vs['nb_frames']),'original_pcm_bit_exact':True,'aac_correlation':corr,'decoded_rms':rms,'hyperframes_check_ok':check['ok'],'findings':{k:check[k]['findings'] for k in ['lint','runtime','layout','contrast']},'approved_static_frame':approved_frame['frame_path'],'lossless_final_frame_mean_pixel_difference':float(lossless_difference.mean()),'S09_sha256_unchanged':old_s09['video_sha256'],'motion_status':'rendered_pending_user_review','browser_playback':'pending'}
    write(OUT/'verification.json',report)
    # Current selection is the approved album still; older architecture approvals are history.
    for x in approved['pending']:
        if x['scene_id']=='S05':x['scope']='rendered_pending_user_review';x['path']=report['video_path']
    write(ROOT/'research/visual-approvals.json',approved)
    status['revised_pilot_renders']=[report if x['scene_id']=='S05' else x for x in status['revised_pilot_renders']]
    status['latest_motion_revision']='revisions/S05-album-pilot-v5-r1'
    status['latest_motion_revisions']={'S05':'revisions/S05-album-pilot-v5-r1','S09':'revisions/pilots-approved-frames-r1/S09'}
    status['review_entry']='revisions/S05-album-pilot-v5-r1/REVIEW.html'
    status['proposed_final_frames']={}
    status['approval_scope']='S05 album final frame v5 approved and pilot rendering authorized. Album motion r1 rendered, awaiting user approval. S09 static v2 approved; S09 motion r1 unchanged. No full-film production.'
    status['next_action']='User reviews the new album-based S05 pilot; use its final-frame-v5 direction rather than superseded house/street/paper-house proposals.'
    write(ROOT/'production_status.json',status)
    description='Mascot ngồi sau bàn, hai tay giữ đúng mép trang album ảnh nhà thật. Cuốn sổ đang mở được hạ phẳng dần để giới thiệu ảnh; ảnh luôn in trên giấy, không trở thành khối nhà. Kết bám frame v5 đã duyệt.'
    for f in [ROOT/'scenes/S05/packet.json',ROOT/'STORYBOARD.json']:
        doc=read(f);s=next(x for x in doc['scenes'] if x['scene_id']=='S05') if f.name=='STORYBOARD.json' else doc
        s['approved_final_frame']=approved_frame;s['latest_motion_revision']=report;s['latest_design_revision']='Album v5 approved; pilot album r1 is the current motion candidate.'
        s['composition']='Một mặt bàn, một album mở có ảnh nhà thật; mascot ngồi phía sau, hai tay giữ mép trang. Không bối cảnh phố vẽ hoặc khối nhà dựng riêng.'
        s['transformation']=description;s['hf_signature_motion']=description;s['visual_verb']='mở / giới thiệu album'
        s['asset_contract'].append({'layer':'album-house-photo-v5','source':'Marika Caruana / Townhouse in Zejtun.jpg / CC BY-SA 4.0','status':'local in revisions/S05-album-pilot-v5-r1/assets/townhouse.jpg; credits beside source'})
        write(f,doc)
    note='\n\n## S05 hiện tại · album v5 / pilot r1\n\nNgười dùng đã duyệt frame album v5 và yêu cầu dựng pilot. MP4 hiện tại: `revisions/S05-album-pilot-v5-r1/renders/pilot.mp4`; source cạnh đó. '+description+' Bản chuyển động đang chờ duyệt; voice giữ nguyên, S09 r1 giữ nguyên. Các hướng nhà giấy/phố trước đây là lịch sử, không dùng để thi công tiếp. CREDITS.md/.json trong revision lưu nguồn ảnh và license.\n'
    for n in ['START_HERE.md','DIRECTOR_BRIEF.md','ANTIGRAVITY_PROMPT.md','TECHNICAL_HANDOFF.md','REVIEW_GUIDE.md','scenes/S05/PACKET.md']:
        f=ROOT/n;write(f,f.read_text(encoding='utf-8')+note)
    write(ROOT/'APPROVED_VERSIONS.md','# Phiên bản hiện tại\n\n## Frame tĩnh đã duyệt\n\n- **S05 final frame v5 — album ảnh nhà thật:** `revisions/S05-final-frame-v5/FINAL_FRAME.png`.\n- **S09 final frame v2 — bàn phân bổ:** `revisions/final-frames-v2/S09/frames/frame-00-at-0.5s.png`.\n\n## Pilot chuyển động chờ duyệt\n\n- **S05 album v5 / motion r1:** `revisions/S05-album-pilot-v5-r1/renders/pilot.mp4`.\n- **S09 motion r1 giữ nguyên:** `revisions/pilots-approved-frames-r1/S09/renders/pilot.mp4`.\n\nCác bản S05 khối nhà giấy, phố vẽ và bìa che nhà trước đây là lịch sử, không phải lựa chọn hiện tại. S01 pilot ban đầu và full film chưa được duyệt. Con số 3,8 tỷ đã được chủ nội dung xác minh riêng.\n')
    page='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>S05 · Pilot album v5 r1</title><style>body{margin:24px;background:#FFF3E8;color:#30313B;font:17px/1.5 Segoe UI,sans-serif}h1{font-size:27px}video{display:block;width:360px;max-width:100%;aspect-ratio:9/16;background:#FFF3E8}button{display:block;margin:12px 0;padding:12px 18px;background:#087BC1;color:white;border:0;font-size:17px}output{display:block}a{color:#0870AC}</style></head><body><h1>S05 · Pilot mới theo frame album v5</h1><p>Voice gốc, album và ảnh nhà thật. Hai tay giữ mép trang; mở sổ về bố cục v5 đã duyệt. Bản chuyển động r1 chờ bạn duyệt.</p><video id="pilot" controls playsinline preload="metadata" poster="MOBILE_FINAL.png" src="renders/pilot.mp4"></video><button onclick="let v=document.getElementById('pilot');v.currentTime=0;v.play()">Phát S05 album v5</button><output id="state">Chưa phát</output><p><a href="FRAME_PROOFS.jpg">Frame mở / giữa / kết</a> · <a href="index.html">Source editable</a> · <a href="CREDITS.md">Nguồn ảnh</a></p><p><a href="../pilots-approved-frames-r1/S09/renders/pilot.mp4">S09 giữ nguyên</a></p><script>const v=document.getElementById('pilot');v.addEventListener('timeupdate',()=>document.getElementById('state').textContent=v.currentTime.toFixed(2)+' / '+v.duration.toFixed(2)+'s'+(v.ended?' · Đã phát hết':' · Đang phát'));</script></body></html>'''
    write(OUT/'REVIEW.html',page)
    f=ROOT/'STORYBOARD.html';s=f.read_text(encoding='utf-8');s=s.replace('S05 FINAL FRAME V5 · ALBUM ẢNH NHÀ THẬT · CHỜ DUYỆT','S05 FINAL FRAME V5 ĐÃ DUYỆT · PILOT ALBUM R1 CHỜ DUYỆT');s=s.replace('<header>','<header><p><a href="revisions/S05-album-pilot-v5-r1/REVIEW.html">Xem pilot S05 mới theo album v5</a></p>',1);write(f,s)
    print(json.dumps({'video_duration':float(vs['duration']),'audio_correlation':corr,'lossless_final_frame_pixel_difference':float(lossless_difference.mean()),'S09_unchanged':True},indent=2))

if __name__=='__main__':main()
