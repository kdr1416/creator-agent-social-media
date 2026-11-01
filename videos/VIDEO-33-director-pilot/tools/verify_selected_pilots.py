"""Verify only the newly rendered S05/S09 revision and stage its review page."""
from pathlib import Path
import json,subprocess,wave,hashlib,re
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageOps
from prepare import ROOT,digest
from rebuild_selected_pilots import OUT

def write(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2) if isinstance(obj,(dict,list)) else obj,encoding='utf-8')

def run(args):return subprocess.run(args,check=True,capture_output=True).stdout

def main():
    revisions=json.loads((OUT/'revision.json').read_text(encoding='utf-8'))
    approvals=json.loads((ROOT/'research/visual-approvals.json').read_text(encoding='utf-8'))
    before=json.loads((OUT/'source-before.json').read_text(encoding='utf-8'))
    assert all(digest(ROOT/k)==v for k,v in before.items()),'Original pilot / approved still / source changed'
    overview=Image.new('RGB',(720,680),'#FFF8E9');draw=ImageDraw.Draw(overview)
    sheet=Image.new('RGB',(1800,1340),'#FFF8E9');sd=ImageDraw.Draw(sheet)
    font=ImageFont.truetype(str(ROOT/'assets/fonts/segoe-ui-black.ttf'),22)
    reports=[]
    for row,item in enumerate(revisions):
        sid=item['scene_id'];folder=OUT/sid;video=folder/'renders/pilot.mp4';voice=folder/'assets/voice.wav'
        probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]))
        vs=next(s for s in probe['streams'] if s['codec_type']=='video');aus=next(s for s in probe['streams'] if s['codec_type']=='audio')
        assert (vs['width'],vs['height'],vs['avg_frame_rate'])==(720,1280,'30/1')
        with wave.open(str(voice),'rb') as w:pcm=w.readframes(w.getnframes());duration=w.getnframes()/w.getframerate()
        with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:
            w.setpos(item['source_start_sample']);expected=w.readframes(item['source_end_sample']-item['source_start_sample'])
        assert pcm==expected
        a=np.frombuffer(pcm,np.int16).astype(np.float64)/32768
        raw=run(['ffmpeg','-v','error','-i',str(video),'-vn','-ac','1','-ar','24000','-f','s16le','-'])
        b=np.frombuffer(raw,np.int16).astype(np.float64)/32768;n=min(len(a),len(b));corr=float(np.corrcoef(a[:n],b[:n])[0,1])
        rms=float(np.sqrt(np.mean(b*b)));vd=float(vs['duration'])
        assert corr>.98 and rms>.001 and abs(vd-duration)<.05
        q=folder/'qa';q.mkdir(exist_ok=True)
        proof=[]
        for col,t in enumerate(item['proof_times']):
            frame=q/f'frame-{t:.2f}.png'
            run(['ffmpeg','-y','-v','error','-ss',str(t),'-i',str(video),'-frames:v','1',str(frame)])
            im=Image.open(frame).convert('RGB');mobile=im.resize((360,640),Image.Resampling.LANCZOS)
            mobile.save(q/f'mobile-{t:.2f}.png');sheet.paste(mobile,(col*360,row*670+30))
            sd.text((col*360+10,row*670+5),f'{sid} · {t:.2f}s',font=font,fill='#30313B')
            footer=np.array(im)[1080:,:,:]
            assert int((footer.max(axis=(0,1))-footer.min(axis=(0,1))).max())<12
            proof.append(str(frame.relative_to(ROOT)))
        last=Image.open(q/f"frame-{item['proof_times'][-1]:.2f}.png").convert('RGB')
        approved=next(x for x in approvals['approved'] if x['scene_id']==sid)
        reference=Image.open(ROOT/approved['frame_path']).convert('RGB')
        difference=np.abs(np.array(last).astype(float)-np.array(reference).astype(float))
        overview.paste(last.resize((360,640)),(row*360,40));draw.text((row*360+12,9),sid+' · motion r1',font=font,fill='#30313B')
        check=json.loads((folder/'qa-check.json').read_text(encoding='utf-8-sig'))
        assert check['ok'] and not check['browserSkipped']
        report={**item,'video_path':str(video.relative_to(ROOT)),'video_sha256':digest(video),'video_frames':int(vs['nb_frames']),'video_duration':vd,'audio_duration':float(aus['duration']),'original_pcm_bit_exact':True,'aac_correlation':corr,'decoded_rms':rms,'hyperframes_check_ok':True,'layout_warnings':check['layout']['findings'],'warning_interpretation':'S09 rotation_pivot_drift is intentional: selector rotates about the visible pin at (211,528), not its bounding-box center. Keep the physical hinge.' if sid=='S09' else None,'final_frame_approved_reference':approved['frame_path'],'final_frame_mean_absolute_pixel_error':float(difference.mean()),'final_frame_pixel_match_fraction':float(np.mean(np.all(difference<3,axis=2))),'frame_proofs':proof,'motion_status':'rendered_pending_user_review'}
        write(q/'verification.json',report);reports.append(report)
    sheet.save(OUT/'FRAME_PROOFS.jpg',quality=93);overview.save(OUT/'PILOTS_OVERVIEW.jpg',quality=94)
    ImageOps.grayscale(overview).resize((360,340)).save(OUT/'GRAYSCALE_THUMBNAIL.png')
    write(OUT/'verification.json',{'pilots':reports,'protected_files_checked':len(before),'protected_files_unchanged':True,'full_film_rendered':False,'browser_playback_review':'pending; separate from frame and audio decoding checks'})
    # This page reviews the new MP4s only. The original review and original files remain available.
    articles=[]
    for r in reports:
        sid=r['scene_id'];time=r['proof_times'][-1]
        articles.append(f'''<article><h2>{sid} · {r['based_on_approved_frame']}</h2><p>Voice gốc {r['duration']:.3f}s · chuyển động r1 chờ duyệt</p><video id="v-{sid}" controls playsinline preload="metadata" poster="{sid}/qa/frame-{time:.2f}.png" src="{sid}/renders/pilot.mp4"></video><button onclick="document.querySelectorAll('video').forEach(v=>v.pause());let v=document.getElementById('v-{sid}');v.currentTime=0;v.play()">Phát {sid} từ đầu</button><output id="out-{sid}">Chưa phát</output><p><a href="{sid}/index.html">Source editable</a> · <a href="{sid}/qa/verification.json">QA</a></p></article>''')
    page='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>S05 + S09 · Pilot sửa r1</title><style>@font-face{font-family:Display;src:url('S05/assets/display.ttf');font-weight:900}body{margin:24px;background:#FFF8E9;color:#30313B;font:17px/1.5 Segoe UI,sans-serif}h1,h2{font-family:Display,sans-serif}h1{font-size:28px}h2{font-size:23px}.grid{display:flex;flex-wrap:wrap;gap:32px}article{max-width:380px}video{display:block;width:360px;max-width:100%;aspect-ratio:9/16;background:#FFF0E5}button{display:block;margin:12px 0;padding:12px 18px;background:#087BC1;border:0;color:white;font-size:17px;cursor:pointer}output{display:block}a{color:#0870AC}</style></head><body><h1>S05 + S09 · Hai pilot chuyển động sửa r1</h1><p>Dựa trên frame S05 v3 và S09 v2 đã duyệt. Voice gốc giữ nguyên. Bản chuyển động mới chờ bạn duyệt; chưa dựng full.</p><div class="grid">'''+''.join(articles)+'''</div><p><a href="../../REVIEW.html">Các pilot ban đầu và mốc hình đã duyệt</a> · <a href="FRAME_PROOFS.jpg">Frame mở / giữa / kết</a></p><script>document.querySelectorAll('video').forEach(v=>v.addEventListener('timeupdate',()=>{let sid=v.id.slice(2);document.getElementById('out-'+sid).textContent=v.currentTime.toFixed(2)+' / '+v.duration.toFixed(2)+'s'+(v.ended?' · Đã phát hết':' · Đang phát');}));</script></body></html>'''
    write(OUT/'REVIEW.html',page)
    print(json.dumps([{'scene':x['scene_id'],'duration':x['video_duration'],'audio_corr':x['aac_correlation'],'final_pixel_error':x['final_frame_mean_absolute_pixel_error'],'match_fraction':x['final_frame_pixel_match_fraction']} for x in reports],ensure_ascii=False,indent=2))

if __name__=='__main__':main()
