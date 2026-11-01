"""Verify final encoded S05 and export mobile, grayscale and grip proofs."""
from pathlib import Path
import json,subprocess,hashlib,wave
import numpy as np
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'revisions/S05-zoom-motion-r1'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
f=P/'renders/pilot.mp4';spec=json.loads((P/'DIRECTION.json').read_text(encoding='utf-8'))
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
with wave.open(str(P/'assets/voice.wav'),'rb') as w:n=w.getnframes();sr=w.getframerate();pcm=w.readframes(n)
with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:w.setpos(435629);assert pcm==w.readframes(n)
assert sha(P/'assets/voice.wav')==sha(ROOT/'inputs/audio/seg_05.wav')==spec['source_voice_sha256']
raw=np.frombuffer(pcm,dtype='<i2').astype(float)/32768
dec=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-map','0:a:0','-ar',str(sr),'-ac','1','-f','f32le','-']),dtype='<f4')
corr=float(np.corrcoef(raw,dec[:n])[0,1]);assert corr>.99
assert (v['width'],v['height'],v['r_frame_rate'])==(720,1280,'30/1')
assert abs(float(v['duration'])-n/sr)<1/30+.001
qa=P/'qa';qa.mkdir(exist_ok=True);times=spec['proof_times']
sheet=Image.new('RGB',(1080,3*680),'#fff8e9');draw=ImageDraw.Draw(sheet)
for i,t in enumerate(times):
    target=qa/f'frame-{i:02d}-{t:.2f}s.png'
    subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(f),'-frames:v','1','-y',str(target)],check=True)
    im=Image.open(target).convert('RGB');im.resize((360,640)).save(qa/f'mobile-{i:02d}.png');im.convert('L').resize((180,320)).save(qa/f'gray-{i:02d}.png')
    if i in [0,1,2,3,4,5,6,8,9]:
        j=[0,1,2,3,4,5,6,8,9].index(i);x=(j%3)*360;y=(j//3)*680;sheet.paste(im.resize((360,640)),(x,y+28));draw.text((x+10,y+7),f'{t:.2f}s',fill='#30313b')
sheet.save(qa/'SEQUENCE.jpg',quality=94)
dense=qa/'contact';dense.mkdir(exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-ss','2.40','-t','1.05','-i',str(f),'-vf','fps=12','-y',str(dense/'frame-%03d.png')],check=True)
fs=sorted(dense.glob('frame-*.png'));sheet=Image.new('RGB',(1000,((len(fs)+3)//4)*270),'#fff8e9');draw=ImageDraw.Draw(sheet)
for i,img in enumerate(fs):
    piece=Image.open(img).crop((245,710,390,860)).resize((225,233));x=(i%4)*250;y=(i//4)*270;sheet.paste(piece,(x+5,y+24));draw.text((x+5,y+4),f'{2.4+i/12:.2f}s',fill='#30313b')
sheet.save(qa/'GRIP-12FPS.jpg',quality=94)
status=json.loads((P/'production_status.json').read_text(encoding='utf-8'));ref=ROOT/'revisions/S05-design-restart-r2'
assert all(sha(ref/e['path'])==e['sha256'] for e in status['reference_frame_manifest'])
old=json.loads((ROOT/'production_status.json').read_text(encoding='utf-8-sig'))
assert all(sha(ROOT/e['video_path'])==e['video_sha256'] for e in old['approved_pilots'])
masters={'build/renders/VIDEO-33-master.mp4':'6f51c8368997f7e2d3721888c3a3d471c2407e8718248fc9d3bea6e4b2b87c50','build/renders/VIDEO-33-clean.mp4':'7050ecb46b98b8b6f50fdce327bcd25c2e8879c282e3c1ef9b417839f05a22b4'}
assert all(sha(ROOT/k)==h for k,h in masters.items())
check=json.loads((P/'qa-check.json').read_text(encoding='utf-8-sig'));assert check['ok'] and check['lint']['warningCount']==0
result={'video':'renders/pilot.mp4','sha256':sha(f),'width':720,'height':1280,'fps':30,'frames':int(v['nb_frames']),'video_duration':float(v['duration']),'source_duration':n/sr,'source_samples':n,'source_pcm_bit_exact':True,'decoded_aac_correlation':corr,'decoded_rms':float(np.sqrt(np.mean(dec[:n]**2))),'qa_check_ok':True,'reference_frames_unchanged':True,'previous_approved_pilots_unchanged':True,'previous_master_and_clean_unchanged':True,'browser_playback':'pending','motion_approved':False}
(P/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
status.update({'phase':'rendered_pending_user_motion_review','video':result,'review_entry':'REVIEW.html'});(P/'production_status.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
(P/'QA_REPORT.md').write_text(f'''# S05 zoom pilot R1 — QA

- 720×1280 @30fps, {v['nb_frames']}frames, hình {v['duration']}s; source voice {n/sr:.12f}s / {n}samples@24kHz.
- Voice WAV nguyên file, PCM đối chiếu đúng source toàn phim [435629,572581); không TTS/retime. AAC decoded correlation {corr:.6f}. Phần hình lẻ cuối làm tròn lên1frame, không cắt voice.
- HyperFrames check: pass; không lint warning. Snapshot zoom đầu/giữa/cuối, contact–release và cut; qa/ trích trực tiếp từ MP4 cuối. Có bản360×640 và grayscale.
- 10pilot đã duyệt trước,4frame R2 và master/clean cũ giữ nguyên hash.
- Browser playback: pending. Motion chờ người dùng duyệt; không thay master.
''',encoding='utf-8')
(P/'REVIEW.html').write_text('''<!doctype html><html lang="vi"><meta charset="utf-8"><title>S05 · Zoom pilot R1</title><style>body{margin:32px auto;padding:0 20px;max-width:1000px;background:#fff8e9;color:#30313b;font:17px system-ui}.layout{display:flex;gap:30px;flex-wrap:wrap}video{display:block;width:360px;max-width:100%;background:#fff8e9}button{font:inherit;padding:12px 22px;margin:16px 0;background:#195d8c;color:white;border:0;border-radius:8px}a{color:#195d8c}.info{max-width:460px}</style><h1>S05 · Zoom pilot R1</h1><p>Zoom mở đầu → đặt ghim Malta → ảnh nhà thật. Voice gốc. Motion chờ bạn duyệt.</p><div class="layout"><section><video id="pilot" controls playsinline preload="auto" poster="qa/frame-02-0.80s.png" src="renders/pilot.mp4" aria-label="Pilot S05 zoom"></video><button id="play">Phát S05</button><p id="status">Chưa phát</p></section><section class="info"><p>0–0,8s: zoom từ toàn quần đảo vào gần đảo chính; Sicily không xuất hiện. Chữ MALTA giữ cố định.</p><p>0,9–2,55s: tay đưa ghim tới vị trí. Sau chạm, tay nhả và thu về.</p><p>4,35s: cắt thẳng sang ảnh mặt tiền nhà thật. Không thay voice hoặc master.</p><p><a href="renders/pilot.mp4">Mở MP4</a> · <a href="qa/SEQUENCE.jpg">Frame kiểm tra</a> · <a href="qa/GRIP-12FPS.jpg">Tay chạm–nhả ghim</a></p><p><a href="index.html">Source editable</a> · <a href="QA_REPORT.md">QA</a> · <a href="../S05-design-restart-r2/REVIEW.html">Frame R2</a></p><p>Ảnh: Marika Caruana — <a href="https://commons.wikimedia.org/wiki/File:Townhouse_in_Zejtun.jpg">Townhouse in Zejtun</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA4.0</a>; đã crop. Bản đồ Natural Earth, public domain.</p></section></div><script>const v=document.getElementById('pilot'),s=document.getElementById('status');document.getElementById('play').onclick=()=>{v.currentTime=0;v.play().catch(e=>s.textContent=e.message)};v.ontimeupdate=()=>s.textContent=v.currentTime.toFixed(2)+' / '+v.duration.toFixed(2)+'s';v.onended=()=>s.textContent='Đã phát hết S05 · '+v.duration.toFixed(2)+'s';v.onerror=()=>s.textContent='Lỗi tải video';</script></html>''',encoding='utf-8')
print(json.dumps(result,indent=2))
