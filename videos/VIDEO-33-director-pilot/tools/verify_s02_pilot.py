"""Verify final encoded S02 and export mobile, grayscale and grip proofs."""
from pathlib import Path
import json,subprocess,hashlib,wave
import numpy as np
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'revisions/S02-approved-frame-motion-r1'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
f=P/'renders/pilot.mp4';spec=json.loads((P/'DIRECTION.json').read_text(encoding='utf-8'))
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
with wave.open(str(P/'assets/voice.wav'),'rb') as w:n=w.getnframes();sr=w.getframerate();pcm=w.readframes(n)
with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:w.setpos(144466);assert pcm==w.readframes(n)
assert sha(P/'assets/voice.wav')==sha(ROOT/'inputs/audio/seg_02.wav')==spec['source_voice_sha256']
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
    if i in [0,1,2,3,4,5,6]:
        j=[0,1,2,3,4,5,6].index(i);x=(j%3)*360;y=(j//3)*680;sheet.paste(im.resize((360,640)),(x,y+28));draw.text((x+10,y+7),f'{t:.2f}s',fill='#30313b')
sheet.save(qa/'SEQUENCE.jpg',quality=94)
dense=qa/'contact';dense.mkdir(exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-ss','0.85','-t','1.50','-i',str(f),'-vf','fps=12','-y',str(dense/'frame-%03d.png')],check=True)
fs=sorted(dense.glob('frame-*.png'));sheet=Image.new('RGB',(1000,((len(fs)+3)//4)*270),'#fff8e9');draw=ImageDraw.Draw(sheet)
for i,img in enumerate(fs):
    piece=Image.open(img).crop((395,500,595,950)).resize((104,233));x=(i%4)*250;y=(i//4)*270;sheet.paste(piece,(x+5,y+24));draw.text((x+5,y+4),f'{0.85+i/12:.2f}s',fill='#30313b')
sheet.save(qa/'STACK-12FPS.jpg',quality=94)
status={};ref=ROOT/'revisions/S02-design-r1'
assert sha(ref/'frames/frame-00-at-0.5s.png')==spec['approved_frame']['frame_sha256']
old=json.loads((ROOT/'production_status.json').read_text(encoding='utf-8-sig'))
assert all(sha(ROOT/e['video_path'])==e['video_sha256'] for e in old['approved_pilots'])
masters={'build/renders/VIDEO-33-master.mp4':'6f51c8368997f7e2d3721888c3a3d471c2407e8718248fc9d3bea6e4b2b87c50','build/renders/VIDEO-33-clean.mp4':'7050ecb46b98b8b6f50fdce327bcd25c2e8879c282e3c1ef9b417839f05a22b4'}
assert all(sha(ROOT/k)==h for k,h in masters.items())
check=json.loads((P/'qa-check.json').read_text(encoding='utf-8-sig'));assert check['ok'] and check['lint']['warningCount']==0
result={'video':'renders/pilot.mp4','sha256':sha(f),'width':720,'height':1280,'fps':30,'frames':int(v['nb_frames']),'video_duration':float(v['duration']),'source_duration':n/sr,'source_samples':n,'source_pcm_bit_exact':True,'decoded_aac_correlation':corr,'decoded_rms':float(np.sqrt(np.mean(dec[:n]**2))),'qa_check_ok':True,'reference_frame_unchanged':True,'previous_approved_pilots_unchanged':True,'previous_master_and_clean_unchanged':True,'browser_playback':'pending','motion_approved':False}
(P/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
status.update({'phase':'rendered_pending_user_motion_review','video':result,'review_entry':'REVIEW.html'});(P/'production_status.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
(P/'QA_REPORT.md').write_text(f'''# S02 pilot R1 — QA

- 720×1280 @30fps, {v['nb_frames']}frames, hình {v['duration']}s; source voice {n/sr:.12f}s / {n}samples@24kHz.
- Voice WAV nguyên file, PCM đối chiếu đúng source toàn phim [144466,236998); không TTS/retime. AAC decoded correlation {corr:.6f}. Phần hình lẻ cuối làm tròn lên1frame, không cắt voice.
- HyperFrames check: pass; không lint warning. Snapshot đầu/giữa/cuối, các xu tiếp xúc và nhịp thước/chữ; qa/ trích trực tiếp từ MP4 cuối. Có bản360×640 và grayscale.
- Các pilot đã duyệt trước, frame S02 R1 và master/clean cũ giữ nguyên hash.
- Browser playback: pending. Motion chờ người dùng duyệt; không thay master.
''',encoding='utf-8')
print(json.dumps(result,indent=2))
