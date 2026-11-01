"""Isolated ending pilots from approved design; preserve source PCM and master."""
from pathlib import Path
import xml.etree.ElementTree as ET
import math,json,shutil,wave,hashlib

ROOT=Path(__file__).resolve().parents[1];REF=ROOT/'revisions/S13-S14-design-r1';OUT=ROOT/'revisions/S13-S14-motion-r1'
if OUT.exists():raise SystemExit('Refusing to overwrite motion revision')
OUT.mkdir(parents=True);ET.register_namespace('','http://www.w3.org/2000/svg');NS='{http://www.w3.org/2000/svg}'
def tag(n,a=None):return ET.Element(NS+n,a or {})
def find(r,id):return next(e for e in r.iter() if e.get('id')==id)
def load(rel):return ET.parse(REF/rel/'layered-art.svg').getroot()
def wrap(r,e,id):
    p=next(p for p in r.iter() if e in list(p));i=list(p).index(e);p.remove(e);g=tag('g',{'id':id});g.append(e);p.insert(i,g);return g
def dump(r):return ET.tostring(r,encoding='unicode')
def prefix(r,p):
    ids={e.get('id'):p+'-'+e.get('id') for e in r.iter() if e.get('id')}
    for e in r.iter():
        for k,v in list(e.attrib.items()):
            if k=='id':e.set(k,ids[v])
            else:
                for old,new in ids.items():v=v.replace('url(#'+old+')','url(#'+new+')')
                e.set(k,v)
    return r
def limb(p,which,x,y,d,t):
    return f"tl.to('#{p}-{which}-path',{{attr:{{d:'M0 0Q{x*.55:.6f} {y*.35:.6f} {x:.6f} {y:.6f}'}},duration:{d},ease:'power2.inOut'}},{t});tl.to('#{p}-{which}-hand',{{attr:{{cx:{x:.6f},cy:{y:.6f}}},duration:{d},ease:'power2.inOut'}},{t});"
board=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'));approval=json.loads((REF/'APPROVAL.json').read_text(encoding='utf-8'))
for f in approval['reference_frame_manifest']:assert hashlib.sha256((REF/f['file']).read_bytes()).hexdigest()==f['sha256']
records=[]
def write(sid,art,js,cues,proofs,contacts):
    s=next(x for x in board['scenes'] if x['scene_id']==sid);f=OUT/sid;a=f/'assets';a.mkdir(parents=True)
    for src,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(src,a/dest)
    chunks=[];params=None;hashes={}
    for rel in s['audio_source']:
        src=ROOT/rel;hashes[rel]=hashlib.sha256(src.read_bytes()).hexdigest()
        with wave.open(str(src),'rb') as w:
            pp=(w.getnchannels(),w.getsampwidth(),w.getframerate());assert params is None or params==pp;params=pp;chunks.append(w.readframes(w.getnframes()))
    if len(chunks)==1:shutil.copy2(ROOT/s['audio_source'][0],a/'voice.wav')
    else:
        with wave.open(str(a/'voice.wav'),'wb') as w:w.setnchannels(params[0]);w.setsampwidth(params[1]);w.setframerate(params[2]);w.writeframes(b''.join(chunks))
    n=len(b''.join(chunks))//params[0]//params[1];assert n==s['sample_frames'];duration=n/params[2]
    h=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{width:100%;height:100%;margin:0;overflow:hidden;background:#FFF8E9}}#root{{width:100%;height:100%;position:relative}}.shot{{position:absolute;inset:0;width:100%;height:100%}}svg{{display:block;width:100%;height:100%}}#assets-shot,#gate-shot,#assets-possibility,#assets-malta-label{{opacity:0}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="{duration:.12f}" data-fps="30">{art}<audio id="{sid}-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="1"></audio></div><script>const tl=gsap.timeline({{paused:true}});{js}tl.to({{v:0}},{{v:1,duration:{duration:.12f},ease:'none'}},0);window.__timelines['root']=tl;</script></body></html>'''
    (f/'index.html').write_text(h,encoding='utf-8')
    spec={'scene':sid,'duration':duration,'sample_frames':n,'sample_rate':params[2],'source_start_sample':s['start_sample'],'source_end_sample':s['end_sample'],'source_segments':s['source_segments'],'source_audio':s['audio_source'],'source_audio_hashes':hashes,'raw_text':s['raw_text'],'corrected_text':s['corrected_text'],'original_voice_sha256':hashlib.sha256((a/'voice.wav').read_bytes()).hexdigest(),'approved_frame_reference':'../../S13-S14-design-r1/APPROVAL.json','approval':'motion_pending_user_review','cues':cues,'proof_times':proofs,'contact_ranges':contacts,'timing_basis':'Original sample bounds and PCM preserved; internal cue timing based on existing ASR and directorial staging.'}
    (f/'DIRECTION.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8');records.append(spec)

# S13: Approach a campus, cut to existing property, widen one shared camera.
student=load('S13/01-student');actor=find(student,'world-student-actor');place=next(e for e in student.iter() if actor in list(e));wrap(student,place,'student-walk')
legs=next(e for e in actor.iter() if e.get('d','').startswith('M48 143'));legs.set('id','walking-legs');student=prefix(student,'student')
assets=load('S13/03-expand');camera=find(assets,'asset-camera');defs=tag('defs');clip=tag('clipPath',{'id':'camera-clip'});clip.append(tag('rect',{'id':'camera-aperture','x':'0','y':'0','width':'620','height':'1080'}));defs.append(clip);assets.insert(0,defs);viewport=wrap(assets,camera,'camera-viewport');viewport.set('clip-path','url(#camera-clip)');viewport.set('data-layout-allow-overflow','true')
modal=find(assets,'possibility');camera.remove(modal);assets.append(modal)
country=next(e for e in camera if e.tag==NS+'text' and e.text=='MALTA');country.set('id','malta-label');camera.remove(country);assets.append(country);assets=prefix(assets,'assets')
js="gsap.set('#assets-asset-camera',{svgOrigin:'0 0',smoothOrigin:false});tl.fromTo('#assets-asset-camera',{x:94,y:-250,scale:1.4},{x:0,y:0,scale:1,duration:1.03,ease:'power2.inOut'},3.0);"
js+="tl.to('#student-student-walk',{x:18,y:-52,duration:1.12,ease:'power1.inOut'},.55);tl.to('#student-world-student-eyes',{x:5,y:-4,duration:.35},.6);"
rest='M48 143L41 190L18 194M90 143L98 190L120 194';a='M48 143L33 184L8 194M90 143L106 184L130 194';b='M48 143L48 184L30 194M90 143L89 184L108 194'
for t,d in [(.58,a),(.88,b),(1.18,a),(1.48,rest)]:js+=f"tl.to('#student-walking-legs',{{attr:{{d:'{d}'}},duration:.21,ease:'sine.inOut'}},{t});"
js+="tl.set('#student-shot',{opacity:0},2.32);tl.set('#assets-shot',{opacity:1},2.32);tl.to('#assets-camera-aperture',{attr:{width:720},duration:1.03,ease:'power2.inOut'},3.0);tl.to('#assets-possibility',{opacity:1,duration:.22},3.15);tl.to('#assets-malta-label',{opacity:1,duration:.20},3.65);"
write('S13','<div id="student-shot" class="shot">'+dump(student)+'</div><div id="assets-shot" class="shot">'+dump(assets)+'</div>',js,{'campus_approach':[.55,1.67],'cut_to_assets':2.32,'shared_camera_widen':[3.0,4.03],'possibility_label':[3.15,3.37],'malta_label':[3.65,3.85]},[.1,.9,1.65,2.4,2.98,3.3,3.7,4.12,4.42],[[.65,1.7],[3.0,4.1]])

# S14: Show the key, then open one rigid vertical gate about a fixed hinge.
key=load('S14/01-key');wrap(key,find(key,'house-key'),'key-present')
palm=next(e for e in key if e.tag==NS+'circle' and e.get('cx')=='364');palm.set('id','key-palm');key=prefix(key,'key')
gate=load('S14/02-gate');mom=find(gate,'adult-placement');wrap(gate,mom,'mother-travel')
paths=[e for e in mom if e.get('d','').startswith('M49 108')]
for i,e in enumerate(paths):e.set('id','gate-arm-'+str(i))
hand=next(e for e in mom if e.tag==NS+'circle' and float(e.get('cx',0))>50);hand.set('id','gate-grip')
legs=next(e for e in mom if e.get('d','').startswith('M-45 214'));legs.set('id','mother-legs')
shoes=next(e for e in mom if e.get('d','').startswith('M-43 328'));shoes.set('id','mother-shoes');gate=prefix(gate,'gate')
js="tl.to('#key-key-present',{x:16,y:25,duration:.65,ease:'power2.inOut'},.6);tl.to('#key-key-palm',{attr:{cx:380,cy:815},duration:.65,ease:'power2.inOut'},.6);"
js+=limb('key-choice','near',(380-170)/1.5-109,(815-715)/1.5-83,.65,.6)
js+="tl.to('#key-choice-eyes',{x:3,y:-3,duration:.3},.75);tl.to('#key-key-present',{x:0,y:0,duration:.5,ease:'power2.inOut'},2.9);tl.to('#key-key-palm',{attr:{cx:364,cy:790},duration:.5,ease:'power2.inOut'},2.9);"
js+=limb('key-choice','near',(364-170)/1.5-109,(790-715)/1.5-83,.5,2.9)
js+="tl.set('#key-shot',{opacity:0},3.8);tl.set('#gate-shot',{opacity:1},3.8);"
start=4.32;duration=1.5;steps=45;k=24/(130*math.sin(math.radians(120)));samples=[]
for i in range(1,steps+1):
    u=i/steps;e=u*u*(3-2*u);angle=math.radians(120*e);c=math.cos(angle);sn=math.sin(angle)
    def point(d,y):return (570-d*c,y+k*d*sn)
    ex,ey=point(130,700);_,eb=point(130,900);hx,hy=point(105,760)
    mx=hx-105-15*e;localx=(hx-mx)/1.2;localy=(hy-620)/1.2;t=start+(i-1)*duration/steps;dt=duration/steps
    pts=f'{ex:.6f},{ey:.6f} 570,700 570,900 {ex:.6f},{eb:.6f}'
    js+=f"tl.to('#gate-gate-panel',{{attr:{{points:'{pts}'}},duration:{dt:.9f},ease:'none'}},{t:.9f});"
    for index,d in enumerate([103,70,34]):
        xx,yy=point(d,700);_,yb=point(d,900);pd=f'M{xx:.6f} {yy:.6f}L{xx:.6f} {yb:.6f}'
        js+=f"tl.to('#gate-gate-bar-{index}',{{attr:{{d:'{pd}'}},duration:{dt:.9f},ease:'none'}},{t:.9f});"
    js+=f"tl.to('#gate-gate-handle',{{attr:{{cx:{hx:.6f},cy:{hy:.6f}}},duration:{dt:.9f},ease:'none'}},{t:.9f});tl.to('#gate-mother-travel',{{x:{mx-360:.6f},duration:{dt:.9f},ease:'none'}},{t:.9f});"
    pd=f'M49 108Q{(49+localx)*.5:.6f} {(108+localy)*.5:.6f} {localx:.6f} {localy:.6f}'
    for index in range(2):js+=f"tl.to('#gate-gate-arm-{index}',{{attr:{{d:'{pd}'}},duration:{dt:.9f},ease:'none'}},{t:.9f});"
    js+=f"tl.to('#gate-gate-grip',{{attr:{{cx:{localx:.6f},cy:{localy:.6f}}},duration:{dt:.9f},ease:'none'}},{t:.9f});"
    samples.append({'time':start+i*dt,'angle_deg':120*e,'panel_free_edge':[ex,ey,eb],'handle':[hx,hy],'mother_scene_x':mx,'wrist_local':[localx,localy]})
rest='M-45 214L-42 330L-9 331L1 239L14 331H48L43 214Z';step='M-45 214L-48 330L-15 331L1 239L20 331H54L43 214Z'
shoe_rest='M-43 328H-8L-8 346H-65Q-66 336-43 328ZM15 329H48L65 343Q64 350 17 347Z';shoe_step='M-49 328H-14L-14 346H-71Q-72 336-49 328ZM21 329H54L71 343Q70 350 23 347Z'
for t,p,s in [(4.4,step,shoe_step),(4.7,rest,shoe_rest),(5.0,step,shoe_step),(5.3,rest,shoe_rest),(5.52,step,shoe_step),(5.74,rest,shoe_rest)]:js+=f"tl.to('#gate-mother-legs',{{attr:{{d:'{p}'}},duration:.18,ease:'sine.inOut'}},{t});tl.to('#gate-mother-shoes',{{attr:{{d:'{s}'}},duration:.18,ease:'sine.inOut'}},{t});"
js+="tl.to('#gate-choices-student-eyes',{x:5,y:-3,duration:.4},4.35);"
write('S14','<div id="key-shot" class="shot">'+dump(key)+'</div><div id="gate-shot" class="shot">'+dump(gate)+'</div>',js,{'key_present':[.6,1.25],'key_return':[2.9,3.4],'cut_to_choice_paths':3.8,'rigid_gate_open':[4.32,5.82],'final_both_paths_open':[5.82,6.855625],'hinge_scene':[[570,700],[570,900]],'projection':'x=570-d*cos(theta); y=y0+k*d*sin(theta), k=24/(130*sin120deg); vertical lengths invariant','gate_angle_deg':[0,120]},[.1,1.5,3.35,3.9,4.35,4.65,5.05,5.4,5.82,6.65],[[4.32,5.85]])
(OUT/'S14/gate-geometry.json').write_text(json.dumps({'hinge':[[570,700],[570,900]],'width':130,'height':200,'samples':samples},indent=2),encoding='utf-8')
(OUT/'pilot_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8');(OUT/'production_status.json').write_text(json.dumps({'phase':'authored_pending_checks','motion_approved':False,'master_modified':False,'voice_modified':False,'pilots':records},ensure_ascii=False,indent=2),encoding='utf-8');print(OUT)
