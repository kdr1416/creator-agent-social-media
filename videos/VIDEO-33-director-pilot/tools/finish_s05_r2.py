"""Verify the logical S05 revision, preserve S09, update the handoff additively."""
import json,subprocess,wave,hashlib
from pathlib import Path
import numpy as np
from PIL import Image,ImageOps,ImageDraw,ImageFont
from prepare import ROOT,digest
from s05_motion_r2 import OUT

def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2) if isinstance(obj,(dict,list)) else obj,encoding='utf-8')
def run(args):return subprocess.run(args,check=True,capture_output=True).stdout

def main():
    d=load(OUT/'DIRECTION.json');video=OUT/'renders/pilot.mp4'
    v=load(ROOT/'production_status.json')
    s09=next(x for x in v['revised_pilot_renders'] if x['scene_id']=='S09')
    assert digest(ROOT/s09['video_path'])==s09['video_sha256'],'S09 was changed'
    probe=json.loads(run(['ffprobe','-v','error','-show_streams','-of','json',str(video)]))
    vs=next(s for s in probe['streams'] if s['codec_type']=='video');aus=next(s for s in probe['streams'] if s['codec_type']=='audio')
    assert (vs['width'],vs['height'],vs['avg_frame_rate'])==(720,1280,'30/1')
    with wave.open(str(OUT/'assets/voice.wav'),'rb') as w:original=w.readframes(w.getnframes())
    with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:
        w.setpos(435629);expected=w.readframes(572581-435629)
    assert original==expected
    decoded=run(['ffmpeg','-v','error','-i',str(video),'-vn','-ac','1','-ar','24000','-f','s16le','-'])
    a=np.frombuffer(original,np.int16).astype(float)/32768;b=np.frombuffer(decoded,np.int16).astype(float)/32768;n=min(len(a),len(b))
    corr=float(np.corrcoef(a[:n],b[:n])[0,1]);rms=float(np.sqrt(np.mean(b*b)))
    assert corr>.98 and rms>.001 and abs(float(vs['duration'])-d['duration'])<.05
    qa=OUT/'qa';qa.mkdir(exist_ok=True)
    sheet=Image.new('RGB',(1080,1340),'#FFF8E9');draw=ImageDraw.Draw(sheet)
    font=ImageFont.truetype(str(ROOT/'assets/fonts/segoe-ui-black.ttf'),22)
    for i,t in enumerate(d['proof_times']):
        f=qa/f'frame-{t:.2f}.png';run(['ffmpeg','-y','-v','error','-ss',str(t),'-i',str(video),'-frames:v','1',str(f)])
        im=Image.open(f).convert('RGB');mobile=im.resize((360,640),Image.Resampling.LANCZOS);mobile.save(qa/f'mobile-{t:.2f}.png')
        sheet.paste(mobile,((i%3)*360,(i//3)*670+30));draw.text(((i%3)*360+10,(i//3)*670+4),f'{t:.2f}s',font=font,fill='#30313B')
        foot=np.array(im)[1080:,:,:];assert int((foot.max(axis=(0,1))-foot.min(axis=(0,1))).max())<12
    sheet.save(OUT/'FRAME_PROOFS.jpg',quality=93)
    last=Image.open(qa/'frame-5.30.png').convert('RGB');last.resize((360,640)).save(OUT/'MOBILE_FINAL.png');ImageOps.grayscale(last).resize((180,320)).save(OUT/'GRAYSCALE.png')
    check=load(OUT/'qa-check.json');assert check['ok'] and not check['browserSkipped']
    report={**d,'scene_id':'S05','revision':'motion-r2','video_path':str(video.relative_to(ROOT)),'video_sha256':digest(video),'video_duration':float(vs['duration']),'audio_duration':float(aus['duration']),'video_frames':int(vs['nb_frames']),'original_pcm_bit_exact':True,'aac_correlation':corr,'decoded_rms':rms,'hyperframes_check_ok':True,'architecture_motion':'No transform/opacity tween on house or balcony. One intact paper leaf rotates in 3D. Character and hand follow projected leaf edge, release before final step.','S09_sha256_unchanged':s09['video_sha256'],'motion_status':'pending_user_review','playback_review':'pending'}
    save(OUT/'verification.json',report)
    v['revised_pilot_renders']=[report if x['scene_id']=='S05' else x for x in v['revised_pilot_renders']]
    v['latest_motion_revision']='revisions/S05-motion-r2';v['latest_motion_revisions']={'S05':'revisions/S05-motion-r2','S09':'revisions/pilots-approved-frames-r1/S09'}
    v['review_entry']='revisions/S05-motion-r2/REVIEW.html';v['next_action']='User reviews S05 motion r2; S05 motion r1 rejected as illogical. S09 r1 unchanged and still awaiting motion approval.'
    v['rejected_motion_revisions']=[{'scene':'S05','revision':'pilots-approved-frames-r1','reason':'User: ảo ảo, phi logic. Affine stretch of facade / gallery removed in r2.'}]
    save(ROOT/'production_status.json',v)
    description='Giữ ngôi nhà và ban công nguyên hình, không scale/skew/morph/fade. Mascot mở một bìa giấy có bản lề ở góc phải; bước ngang theo mép bìa đang quay, buông tay trước khi bước về vị trí kết. Bìa che được mở đi để lộ kiến trúc có sẵn, không biến giấy thành nhà.'
    for file in [ROOT/'scenes/S05/packet.json',ROOT/'STORYBOARD.json']:
        obj=load(file);scene=next(x for x in obj['scenes'] if x['scene_id']=='S05') if file.name=='STORYBOARD.json' else obj
        scene['latest_motion_revision']=report;scene['latest_design_revision']='S05 motion r2 supersedes rejected r1. '+description
        scene['transformation']=description;scene['hf_signature_motion']=description;scene['visual_verb']='mở trang / khám phá'
        scene['timed_beats']=[{'local_seconds':t,'action':action,'alignment':'approximate_directorial_cue_based_on_preserved_ASR'} for t,action in [(0,'Bìa in nét kiến trúc đã có, nhà đứng sẵn phía sau'),(1.65,'Mascot với tay tới tai giấy'),(2.52,'Giữ tai giấy, mở bìa quanh bản lề và bước ngang'),(4.35,'Bất động sản: kiến trúc có sẵn được lộ gần hết, không méo hình'),(4.60,'Buông tay rồi bước cuối'),(4.95,'MALTA hiện phía trên; nhìn ban công và giữ kết')]]
        save(file,obj)
    note='\n\n## S05 motion r2 — sửa tính hợp lý, chờ duyệt\n\nS05 motion r1 bị người dùng phản hồi ảo/phi logic. Bản r2 tại `revisions/S05-motion-r2/renders/pilot.mp4` bỏ mọi co giãn mặt nhà/ban công. '+description+' Voice nguyên lát nguồn. Frame kiến trúc v3 là tham chiếu đã duyệt; pose kết được chỉnh sau nhả tay để đúng hành động, chưa tự coi motion r2 là đã duyệt. S09 r1 giữ nguyên. Trang xem mới: `revisions/S05-motion-r2/REVIEW.html`.\n'
    for name in ['APPROVED_VERSIONS.md','START_HERE.md','DIRECTOR_BRIEF.md','ANTIGRAVITY_PROMPT.md','TECHNICAL_HANDOFF.md','REVIEW_GUIDE.md','scenes/S05/PACKET.md']:
        f=ROOT/name;save(f,f.read_text(encoding='utf-8')+note)
    page='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>S05 r2 · Sửa cơ chế mở giấy</title><style>body{margin:24px;background:#FFF8E9;color:#30313B;font:17px/1.5 Segoe UI,sans-serif}h1{font-size:27px}.grid{display:flex;gap:32px;flex-wrap:wrap}article{max-width:380px}video{display:block;width:360px;max-width:100%;aspect-ratio:9/16;background:#FFF0E5}button{display:block;margin:12px 0;padding:12px 18px;background:#087BC1;color:white;border:0;font-size:17px}output{display:block}a{color:#0870AC}</style></head><body><h1>S05 motion r2 · Mở giấy, không biến dạng ngôi nhà</h1><p>Nhà và ban công giữ nguyên hình. Mascot mở bìa giấy quanh một bản lề rồi buông tay. S09 giữ nguyên bản r1.</p><div class="grid"><article><h2>S05 · motion r2 mới</h2><video id="S05" controls playsinline preload="metadata" poster="MOBILE_FINAL.png" src="renders/pilot.mp4"></video><button onclick="play('S05')">Phát S05 r2</button><output id="out-S05">Chưa phát</output><p><a href="FRAME_PROOFS.jpg">Các mốc động tác</a></p></article><article><h2>S09 · r1 giữ nguyên</h2><video id="S09" controls playsinline preload="metadata" poster="../pilots-approved-frames-r1/S09/qa/frame-7.10.png" src="../pilots-approved-frames-r1/S09/renders/pilot.mp4"></video><button onclick="play('S09')">Phát S09</button><output id="out-S09">Chưa phát</output></article></div><p>Bản chuyển động S05 r2 chờ người dùng duyệt; chưa dựng full.</p><script>function play(id){document.querySelectorAll('video').forEach(v=>v.pause());let v=document.getElementById(id);v.currentTime=0;v.play()}document.querySelectorAll('video').forEach(v=>v.addEventListener('timeupdate',()=>document.getElementById('out-'+v.id).textContent=v.currentTime.toFixed(2)+' / '+v.duration.toFixed(2)+'s'+(v.ended?' · Đã phát hết':' · Đang phát')))</script></body></html>'''
    save(OUT/'REVIEW.html',page)
    for name in ['REVIEW.html','STORYBOARD.html']:
        f=ROOT/name;text=f.read_text(encoding='utf-8');banner='<p><strong>Bản S05 mới nhất: </strong><a href="revisions/S05-motion-r2/REVIEW.html">S05 motion r2 — sửa cơ chế mở giấy; S09 giữ nguyên</a></p>'
        text=text.replace('<body>','<body>'+banner,1) if name=='REVIEW.html' else text.replace('<header>','<header>'+banner,1)
        save(f,text)
    print(json.dumps({'video_duration':float(vs['duration']),'audio_corr':corr,'S09_unchanged':True,'check_ok':check['ok']},indent=2))

if __name__=='__main__':main()
