"""Isolated S02 motion from approved frame R1. No master or voice edits."""
from pathlib import Path
import json,shutil,hashlib,wave
ROOT=Path(__file__).resolve().parents[1];REF=ROOT/'revisions/S02-design-r1';OUT=ROOT/'revisions/S02-approved-frame-motion-r1'
if OUT.exists():raise SystemExit('Refusing to overwrite pilot revision')
OUT.mkdir();a=OUT/'assets';a.mkdir()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
approval={'scene':'S02','version':'S02-design-r1','scope':'static frame design','user_message':'oke mình duyệt, lên cho mình cái pilot luôn đi','date_local':'2026-10-27','frame_sha256':sha(REF/'frames/frame-00-at-0.5s.png'),'motion_approved':False}
(REF/'APPROVAL.json').write_text(json.dumps(approval,ensure_ascii=False,indent=2),encoding='utf-8')
for src,dest in [(REF/'assets/font.ttf','font.ttf'),(REF/'assets/gsap.min.js','gsap.min.js'),(ROOT/'inputs/audio/seg_02.wav','voice.wav')]:shutil.copy2(src,a/dest)
with wave.open(str(a/'voice.wav'),'rb') as w:n=w.getnframes();sr=w.getframerate();pcm=w.readframes(n)
assert (n,sr)==(92532,24000)
with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:w.setpos(144466);assert w.readframes(n)==pcm
duration=n/sr
art=(REF/'layered-art.svg').read_text(encoding='utf-8').replace('HÀNG TỶ ĐỒNG','H&#192;NG T&#7926; &#272;&#7890;NG')
js=''
for i in range(4,14):
    t=.85+(i-4)*.13
    js+=f"tl.set('#coin-{i}',{{opacity:1}},{t:.3f});tl.fromTo('#coin-{i}',{{x:28,y:-68}},{{x:0,y:0,duration:.27,ease:'power2.in'}},{t:.3f});"
js+="tl.fromTo('#measuring-rule',{y:70},{y:0,duration:.6,ease:'power2.inOut'},1.92);tl.to('#measuring-rule',{opacity:1,duration:.18},1.92);tl.to('#hero',{opacity:1,duration:.18},1.92);"
hidden=','.join('#coin-'+str(i) for i in range(4,14))
html=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{width:100%;height:100%;margin:0;overflow:hidden;background:#FFF0E5}}#root{{width:100%;height:100%;position:relative}}svg{{display:block;width:100%;height:100%}}#hero,#measuring-rule,{hidden}{{opacity:0}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-fps="30" data-duration="{duration:.12f}">{art}<audio id="S02-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="1"></audio></div><script>const tl=gsap.timeline({{paused:true}});{js}window.__timelines=window.__timelines||{{}};window.__timelines.root=tl;</script></body></html>'''
(OUT/'index.html').write_text(html,encoding='utf-8');(OUT/'layered-art.svg').write_text(art,encoding='utf-8')
spec=json.loads((REF/'DIRECTION.json').read_text(encoding='utf-8'));spec.update({'phase':'pilot_pending_user_motion_review','version':'S02-approved-frame-motion-r1','source_voice_sha256':sha(a/'voice.wav'),'approved_frame':approval,'proof_times':[.1,.85,1.5,1.92,2.15,2.52,3.65],'motion_cues':{'coins_add':[.85,2.29],'headline_and_gauge':[1.92,2.52],'resolved_hold':[2.52,duration]},'cue_basis':'Existing whisper_raw word timing: hang7.94, ty8.18, dong8.42global; local offset6.019416667. Approximate ASR; no audio edits.','master_modified':False,'motion_approved':False})
(OUT/'DIRECTION.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'README.md').write_text('''# S02 motion R1
Approved frame S02-design-r1; original voice seg02 copied verbatim,92532samples@24kHz /3.8555s, global[144466,236998). Four coins already stacked; ten added successively0.85–2.29s. No growth/return claim: these coins represent resources allocated to education. At local1.92s (“hàng tỷ đồng”), title reveals and physical unnumbered gauge rises70px to the final pose by2.52s. Cap and ledger stay grounded. Final pose matches approved design. No mascot, no invented school price or currency amount. New pilot only, master/assembly manifest remain unchanged until motion approval. Local editable SVG/font/GSAP/WAV. Voice export must bypass native auto gain by direct AAC mux from original WAV.\n''',encoding='utf-8')
print('S02 pilot source created')
