"""Verify delivered pilot streams/audio and create review proofs from encoded MP4s."""
from pathlib import Path
import json, subprocess, hashlib, wave
import numpy as np
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'revisions/S07-S08-motion-r1'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def probe(f):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]))
results=[]
for sid in ['S07','S08']:
    f=P/sid/'renders/pilot.mp4';folder=P/sid;qa=folder/'qa';qa.mkdir(exist_ok=True)
    d=probe(f);v=next(s for s in d['streams'] if s['codec_type']=='video');a=next(s for s in d['streams'] if s['codec_type']=='audio')
    ref=ROOT/f'inputs/audio/seg_{sid[1:]}.wav';assert sha(ref)==sha(folder/'assets/voice.wav')
    with wave.open(str(ref),'rb') as w:n=w.getnframes();sr=w.getframerate();raw=np.frombuffer(w.readframes(n),dtype='<i2').astype(float)/32768
    decoded=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-map','0:a:0','-ar',str(sr),'-ac','1','-f','f32le','-']),dtype='<f4')
    assert len(decoded)>=n
    corr=float(np.corrcoef(raw,decoded[:n])[0,1]);assert corr>.99,(sid,corr)
    assert (v['width'],v['height'],v['r_frame_rate'])==(720,1280,'30/1')
    source=json.loads((folder/'DIRECTION.json').read_text(encoding='utf-8'));times=source['proof_times']
    for i,t in enumerate(times):
        out=qa/f'frame-{i:02d}-{t:.3f}s.png'
        subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(f),'-frames:v','1','-y',str(out)],check=True)
        im=Image.open(out).convert('RGB');im.resize((360,640)).save(qa/f'mobile-{i:02d}.png');im.convert('L').resize((180,320)).save(qa/f'gray-{i:02d}.png')
    # Contact proof at 12fps around semantic gesture, from the actual encoded video.
    begin,end=(1.4,2.5) if sid=='S07' else (.7,1.8)
    dense=qa/'contact-12fps';dense.mkdir(exist_ok=True)
    subprocess.run(['ffmpeg','-v','error','-ss',str(begin),'-t',str(end-begin),'-i',str(f),'-vf','fps=12,scale=180:320','-y',str(dense/'frame-%03d.png')],check=True)
    fs=sorted(dense.glob('frame-*.png'));sheet=Image.new('RGB',(720,((len(fs)+3)//4)*345),'#fff8e9');draw=ImageDraw.Draw(sheet)
    for i,frame in enumerate(fs):
        x=(i%4)*180;y=(i//4)*345;draw.text((x+5,y+4),f'{begin+i/12:.2f}s',fill='#30313B');sheet.paste(Image.open(frame),(x,y+23))
    sheet.save(qa/'CONTACT-12FPS.jpg')
    fs=sorted(qa.glob('frame-*.png'));sheet=Image.new('RGB',(800,((len(fs)+3)//4)*380),'#fff8e9');draw=ImageDraw.Draw(sheet)
    for i,frame in enumerate(fs):
        x=(i%4)*200;y=(i//4)*380;draw.text((x+5,y+5),f'{times[i]:.3f}s',fill='#30313B');sheet.paste(Image.open(frame).resize((190,338)),(x+5,y+25))
    sheet.save(qa/'SEQUENCE.jpg')
    check=json.loads((folder/'qa-check.json').read_text(encoding='utf-8'))
    assert check['ok'] and check['lint']['warningCount']==0
    results.append({'scene':sid,'path':str(f.relative_to(P)),'sha256':sha(f),'source_duration':n/sr,'video_duration':float(v['duration']),'audio_duration':float(a['duration']),'video_frames':int(v['nb_frames']),'audio_codec':a['codec_name'],'audio_sample_rate':a['sample_rate'],'audio_channels':a['channels'],'source_voice_sha256':sha(ref),'voice_copy_bit_exact':True,'decoded_aac_correlation':corr,'decoded_rms':float(np.sqrt(np.mean(decoded[:n]**2))),'hyperframes_check_ok':check['ok'],'lint_warning_count':check['lint']['warningCount'],'proof_times':times,'contact_sampling_fps':12,'motion_approved':False})
    print(sid,'frames',v['nb_frames'],'voice correlation',round(corr,6))
approved=json.loads((ROOT/'revisions/S07-S08-design-r1/APPROVAL.json').read_text(encoding='utf-8'))
for item in approved['frames']:assert sha(ROOT/'revisions/S07-S08-design-r1'/item['file'])==item['sha256']
expected={'master':'6f51c8368997f7e2d3721888c3a3d471c2407e8718248fc9d3bea6e4b2b87c50','clean':'7050ecb46b98b8b6f50fdce327bcd25c2e8879c282e3c1ef9b417839f05a22b4'}
for k,h in expected.items():assert sha(ROOT/f'build/renders/VIDEO-33-{k}.mp4')==h
(P/'qa-verification.json').write_text(json.dumps({'pilots':results,'approved_eight_frame_hashes_unchanged':True,'previous_master_and_clean_unchanged':True,'browser_playback':'pending','full_film_replaced':False},ensure_ascii=False,indent=2),encoding='utf-8')
parts=['<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>S07–S08 · Pilot motion R1</title><style>body{background:#fff8e9;color:#30313b;font:18px/1.6 Segoe UI,sans-serif;margin:28px auto;max-width:1100px;padding:0 22px}h1{font-size:30px;color:#195d8c}.grid{display:flex;flex-wrap:wrap;gap:35px}article{width:360px}video{width:360px;max-width:100%;background:#fff8e9;border-radius:4px}button{font:700 17px Segoe UI,sans-serif;background:#195d8c;color:white;border:0;padding:12px 20px;border-radius:8px;cursor:pointer}a{color:#195d8c}.status{font-weight:700}small{font-size:15px}</style><h1>S07–S08 · Pilot motion R1</h1><p>Dựng theo bộ frame R1 đã duyệt, có voice gốc. Hai pilot chờ bạn duyệt chuyển động; bản master cũ giữ nguyên.</p><div class="grid">']
for r in results:
    sid=r['scene'];parts.append(f'''<article><h2>{sid}</h2><video id="{sid}" controls playsinline preload="metadata" poster="{sid}/qa/frame-00-{r['proof_times'][0]:.3f}s.png"><source src="{sid}/renders/pilot.mp4" type="video/mp4"></video><p><button onclick="document.getElementById('{sid}').currentTime=0;document.getElementById('{sid}').play()">Phát {sid}</button></p><p id="status-{sid}" class="status">Chưa phát</p><small>Voice gốc: {r['source_duration']:.6f}s · Hình: {r['video_duration']:.3f}s<br><a href="{sid}/renders/pilot.mp4">Mở MP4</a> · <a href="{sid}/qa/SEQUENCE.jpg">Frame kiểm tra</a> · <a href="{sid}/index.html">Source editable</a></small></article>''')
parts.append('''</div><p>S07: chạm nút gọi → kết nối → vẫy đáp lại. S08: kéo vali/gặp con → học tập → sinh sống → làm việc. Các shot hoạt động cắt theo word timing ASR có sẵn; voice không đổi.</p><p><a href="QA_REPORT.md">Báo cáo kiểm tra</a> · <a href="../S07-S08-design-r1/REVIEW.html">Frame đã duyệt</a></p><script>for(const sid of ['S07','S08']){const v=document.getElementById(sid),s=document.getElementById('status-'+sid);v.addEventListener('timeupdate',()=>{s.textContent=v.currentTime.toFixed(2)+' / '+v.duration.toFixed(2)+'s';});v.addEventListener('ended',()=>{s.textContent='Đã phát hết '+sid+' · '+v.duration.toFixed(2)+'s';});}</script></html>''')
(P/'REVIEW.html').write_text(''.join(parts),encoding='utf-8')
(P/'QA_REPORT.md').write_text('# S07/S08 motion R1 — kiểm tra\n\nHai MP4 có voice gốc, bản WAV copy khớp SHA256, AAC correlation >0.99, 720×1280 @30fps. HyperFrames check cả hai: không có lỗi/cảnh báo lint, runtime, layout hoặc contrast. Render cục bộ screenshot capture với GPU phần cứng.\n\nĐã tạo frame mở/giữa/cuối, mobile/grayscale và contact sampling 12fps từ MP4. Xem qa-verification.json cho số đo thật. Voice/sample giữ nguyên; hình làm tròn lên frame 30fps nên có đuôi hold tối đa một frame. Browser playback đang chờ kiểm tra. Không coi encode/check là duyệt sáng tạo.\n\nTạo hình/bố cục dựa trên 8 frame R1 đã duyệt; động tác và cue nội cảnh là thực thi mới đang chờ người dùng duyệt. Các khoảng cảnh học/sống/làm ngắn theo voice; mỗi shot có một thao tác nhỏ, không thêm nội dung vào voice. Không thay master, không sản xuất các cảnh khác.\n',encoding='utf-8')
