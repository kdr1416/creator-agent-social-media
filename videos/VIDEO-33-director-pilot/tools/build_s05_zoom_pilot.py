"""Isolated S05 restart pilot: shared map camera, grip, release, editorial cut."""
from pathlib import Path
import xml.etree.ElementTree as ET
import json,shutil,hashlib,wave

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'revisions/S05-design-restart-r2'
OUT=ROOT/'revisions/S05-zoom-motion-r1'
if OUT.exists(): raise SystemExit('Refusing to overwrite pilot revision')
OUT.mkdir();a=OUT/'assets';a.mkdir()
NS='{http://www.w3.org/2000/svg}';ET.register_namespace('',NS[1:-1])
def find(r,id):return next(n for n in r.iter() if n.get('id')==id)
def load(p):return ET.parse(REF/p/'layered-art.svg').getroot()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
opening=load('01-hold');contact=load('02-contact');release=load('03-release');house=load('04-house')
geometry=find(opening,'geography');land=find(opening,'land');geometry.remove(land)
cam=ET.Element(NS+'g',{'id':'map-camera','data-layout-allow-overflow':'true'});cam.append(land)
# Background and camera viewport remain fixed; all objects and the gripping hand share one camera.
for node in list(opening):
    if node.tag==NS+'g' and node is not geometry:
        opening.remove(node);cam.append(node)
    elif node.get('id')=='gripping-fingers':
        opening.remove(node);cam.append(node)
geometry.append(cam)
pin=find(opening,'location-pin');parent=next(n for n in opening.iter() if pin in list(n));ix=list(parent).index(pin);parent.remove(pin)
travel=ET.Element(NS+'g',{'id':'pin-travel'});travel.append(pin);parent.insert(ix,travel)
for n in house.iter():
    if n.get('id'):n.set('id','photo-'+n.get('id'))
for src,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js'),(ROOT/'inputs/audio/seg_05.wav','voice.wav'),(REF/'assets/townhouse-crop.jpg','townhouse-crop.jpg')]:shutil.copy2(src,a/dest)
with wave.open(str(a/'voice.wav'),'rb') as w:n=w.getnframes();sr=w.getframerate();pcm=w.readframes(n)
assert (n,sr)==(136952,24000)
with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:w.setpos(435629);assert w.readframes(n)==pcm
duration=n/sr
js="gsap.set('#map-camera',{svgOrigin:'360 740',smoothOrigin:false});tl.fromTo('#map-camera',{scale:.82,x:0,y:-18},{scale:1,x:0,y:0,duration:.8,ease:'power2.inOut'},0);"
def arm_pose(source,t,d):
    global js
    path=find(source,'selector-near-path').get('d');hand=find(source,'selector-near-hand')
    js+=f"tl.to('#selector-near-path',{{attr:{{d:{json.dumps(path)}}},duration:{d},ease:'power2.inOut'}},{t});"
    js+=f"tl.to('#selector-near-hand',{{attr:{{cx:{hand.get('cx')},cy:{hand.get('cy')}}},duration:{d},ease:'power2.inOut'}},{t});"
arm_pose(contact,.9,1.65)
js+="tl.to('#pin-travel',{x:-9,y:-42,duration:1.65,ease:'power2.inOut'},.9);tl.to('#gripping-fingers',{attr:{cx:323,cy:760},duration:1.65,ease:'power2.inOut'},.9);"
js+="tl.to('#selector-eyes',{x:4,y:-2,duration:.3,ease:'power1.inOut'},.95);tl.to('#gripping-fingers',{attr:{cx:308,cy:832},duration:.65,ease:'power2.inOut'},2.7);"
arm_pose(release,2.7,.65)
js+="tl.to('#selector-eyes',{x:2,y:0,duration:.3},3.05);tl.set('#map-shot',{opacity:0},4.35);tl.set('#photo-shot',{opacity:1},4.35);"
art=ET.tostring(opening,encoding='unicode');photo=ET.tostring(house,encoding='unicode')
(OUT/'map-layered.svg').write_text(art,encoding='utf-8');(OUT/'photo-layered.svg').write_text(photo,encoding='utf-8')
(OUT/'index.html').write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{width:100%;height:100%;margin:0;overflow:hidden;background:#FFF8E9}}#root{{position:relative;width:100%;height:100%}}.shot{{position:absolute;inset:0;width:100%;height:100%}}svg{{display:block;width:100%;height:100%}}#photo-shot{{opacity:0}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-fps="30" data-duration="{duration:.12f}"><div id="map-shot" class="shot">{art}</div><div id="photo-shot" class="shot">{photo}</div><audio id="S05-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="1"></audio></div><script>const tl=gsap.timeline({{paused:true}});{js}window.__timelines=window.__timelines||{{}};window.__timelines['root']=tl;</script></body></html>''',encoding='utf-8')
spec=json.loads((REF/'STORYBOARD_SOURCE.json').read_text(encoding='utf-8'))
spec.update({'version':'S05-zoom-motion-r1','duration':duration,'source_start_sample':435629,'source_end_sample':572581,'source_voice_sha256':sha(a/'voice.wav'),'frame_reference':'../S05-design-restart-r2','cues':{'opening_shared_camera_zoom':[0,.8],'reach':[.9,2.55],'contact_hold':[2.55,2.7],'release':[2.7,3.35],'editorial_cut_to_house':4.35},'proof_times':[.05,.4,.8,1.6,2.55,2.85,3.35,4.30,4.40,5.5],'motion_approved':False,'timing_basis':'Original WAV sample bounds immutable; internal cut cue inherited from ASR/director restart storyboard.'})
(OUT/'DIRECTION.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(REF/'CREDITS.json',OUT/'CREDITS.json')
manifest=[{'path':str(f.relative_to(REF)),'sha256':sha(f)} for f in REF.glob('*/frames/frame-00-at-0.5s.png')]
(OUT/'production_status.json').write_text(json.dumps({'phase':'building_pilot','motion_approved':False,'master_modified':False,'voice_modified':False,'source_pcm_bit_exact':True,'reference_frame_manifest':manifest},indent=2),encoding='utf-8')
(OUT/'README.md').write_text('''# S05 zoom motion R1
Source editable index.html, SVG layers, font/runtime/photo and copied original WAV are local. Timeline: zoom 0–0.8s, reach0.9–2.55s, contact hold to2.7s, release2.7–3.35s, hard cut4.35s to original house crop. Keep geography, pin, mascot and grip under one camera wrapper. Camera origin set once before fromTo to avoid SVG-origin drift. Malta label remains fixed from opening; Sicily is absent. Source [435629,572581),24kHz136952 samples untouched. Native MP4 can hold the last image for the remainder of a30fps frame; when assembling master do not accumulate independent scene padding. No master replacement; motion pending user review. Photo crop CC BY-SA4.0: Marika Caruana, source/license in CREDITS.json.\n''',encoding='utf-8')
print('Created isolated S05 zoom pilot source')
