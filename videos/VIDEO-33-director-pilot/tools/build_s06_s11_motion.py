"""Author isolated S06/S11 pilots from approved review frames, with original PCM."""
from pathlib import Path
import xml.etree.ElementTree as ET
import json, shutil, wave, hashlib

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'revisions/S06-S11-design-r1'
OUT=ROOT/'revisions/S06-S11-motion-r1'
if OUT.exists() and any(OUT.iterdir()):raise SystemExit('Refusing to overwrite motion revision')
OUT.mkdir(parents=True,exist_ok=True)
ET.register_namespace('','http://www.w3.org/2000/svg');NS='{http://www.w3.org/2000/svg}'
def tag(name,attrs=None):return ET.Element(NS+name,attrs or {})
def find(r,id):return next(e for e in r.iter() if e.get('id')==id)
def load(rel):return ET.parse(REF/rel/'layered-art.svg').getroot()
def wrap(r,e,id):
    p=next(p for p in r.iter() if e in list(p));i=list(p).index(e);p.remove(e);g=tag('g',{'id':id});g.append(e);p.insert(i,g);return g
def dump(r):return ET.tostring(r,encoding='unicode')
def limb(prefix,which,x,y,dur,t):
    return f"tl.to('#{prefix}-{which}-path',{{attr:{{d:'M0 0Q{x*.55:.5f} {y*.35:.5f} {x:.5f} {y:.5f}'}},duration:{dur},ease:'power2.inOut'}},{t});tl.to('#{prefix}-{which}-hand',{{attr:{{cx:{x:.5f},cy:{y:.5f}}},duration:{dur},ease:'power2.inOut'}},{t});"
board=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'))
approval=json.loads((REF/'APPROVAL.json').read_text(encoding='utf-8'))
for a in approval['frames']:assert hashlib.sha256((REF/a['file']).read_bytes()).hexdigest()==a['sha256']
records=[]
def write(sid,r,js,cues,proofs,contacts):
    s=next(x for x in board['scenes'] if x['scene_id']==sid);f=OUT/sid;a=f/'assets';a.mkdir(parents=True)
    for source,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(source,a/dest)
    # Concatenate complete original PCM payloads for the merged S11 scene.
    buffers=[];params=None;source_hashes={}
    for rel in s['audio_source']:
        source=ROOT/rel;source_hashes[rel]=hashlib.sha256(source.read_bytes()).hexdigest()
        with wave.open(str(source),'rb') as w:
            pp=(w.getnchannels(),w.getsampwidth(),w.getframerate());assert params is None or params==pp;params=pp;buffers.append(w.readframes(w.getnframes()))
    if len(buffers)==1:shutil.copy2(ROOT/s['audio_source'][0],a/'voice.wav')
    else:
        with wave.open(str(a/'voice.wav'),'wb') as w:w.setnchannels(params[0]);w.setsampwidth(params[1]);w.setframerate(params[2]);w.writeframes(b''.join(buffers))
    n=len(b''.join(buffers))//params[0]//params[1];assert n==s['sample_frames'];duration=n/params[2]
    text=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{margin:0;width:100%;height:100%;overflow:hidden;background:#FFF8E9}}#root{{width:100%;height:100%;position:relative}}svg{{display:block;width:100%;height:100%}}#student-grip{{opacity:0}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="{duration:.12f}" data-fps="30">{dump(r)}<audio id="{sid}-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="1"></audio></div><script>const tl=gsap.timeline({{paused:true}});{js}tl.to({{v:0}},{{v:1,duration:{duration:.12f},ease:'none'}},0);window.__timelines['root']=tl;</script></body></html>'''
    (f/'index.html').write_text(text,encoding='utf-8')
    d={'scene':sid,'duration':duration,'source_start_sample':s['start_sample'],'source_end_sample':s['end_sample'],'sample_frames':n,'sample_rate':params[2],'source_segments':s['source_segments'],'raw_text':s['raw_text'],'corrected_text':s['corrected_text'],'source_audio':s['audio_source'],'source_audio_hashes':source_hashes,'original_voice_sha256':hashlib.sha256((a/'voice.wav').read_bytes()).hexdigest(),'approved_frame_reference':'../../S06-S11-design-r1','cues':cues,'proof_times':proofs,'contact_ranges':contacts,'approval':'motion_pending_user_review','timing_basis':'Scene sample bounds immutable; internal motion cues are directorial and require playback review.'}
    (f/'DIRECTION.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8');records.append(d)

r=load('S06/01-ready')
placement=next(p for p in r.iter() if find(r,'family-actor') in list(p))
wrap(r,placement,'family-travel')
chair=find(r,'invited-chair');wrap(r,chair,'chair-pull')
# A real foot rung supports the child's short climb into the pulled chair.
chair.append(tag('path',{'d':'M-3 238H118','fill':'none','stroke':'#8A73AF','stroke-width':'7','stroke-linecap':'round'}))
legs=next(e for e in find(r,'family-actor').iter() if e.get('d','').startswith('M48 143'))
legs.set('id','family-legs')
shadow=find(r,'family-student-shadow');shadow.set('opacity','0')
near0=((198-32)/1.05-109,(864-810)/1.05-83)
near1=((163-20)/1.05-109,(884-810)/1.05-83)
js="tl.to('#chair-pull',{x:-35,y:20,duration:.85,ease:'power2.inOut'},.55);tl.to('#family-travel',{x:-12,duration:.85,ease:'power2.inOut'},.55);"
js+=limb('family','near',*near1,.85,.55)
# Release chair before stepping in front of the seat; placement stays intact.
js+=limb('family','near',30,12,.20,1.48)
js+="tl.to('#family-travel',{x:42,y:32,scale:1.035,svgOrigin:'32 810',duration:.60,ease:'power1.inOut'},1.70);tl.to('#family-travel',{x:108,y:40,scale:1.0666666667,svgOrigin:'32 810',duration:.60,ease:'power1.inOut'},2.30);"
walk_a='M48 143L32 184L6 194M90 143L106 184L130 194'
walk_b='M48 143L49 184L30 194M90 143L87 184L108 194'
rest='M48 143L41 190L18 194M90 143L98 190L120 194'
for t,d in [(1.78,walk_a),(2.08,walk_b),(2.38,walk_a),(2.68,rest)]:js+=f"tl.to('#family-legs',{{attr:{{d:'{d}'}},duration:.22,ease:'sine.inOut'}},{t});"
# Both the hand and planted foot stay in scene space during the supported rise.
seat_grip_x=(240-140)/1.12-109
js+=limb('family','near',seat_grip_x,(972-850)/1.12-83,.22,2.90)
js+="tl.to('#family-legs',{attr:{d:'M48 143L45 166L35 166M90 143L98 190L120 194'},duration:.23,ease:'power2.inOut'},2.94);"
js+="tl.to('#family-travel',{y:-12,duration:.65,ease:'power2.inOut'},3.20);"
js+=limb('family','near',seat_grip_x,(972-798)/1.12-83,.65,3.20)
js+="tl.to('#family-legs',{attr:{d:'M48 143L45 212.42857L35 212.42857M90 143L98 226L120 226'},duration:.65,ease:'power2.inOut'},3.20);tl.to('#family-legs',{attr:{d:'M48 143L48 226L25 226M90 143L90 226L111 226'},duration:.25,ease:'power1.out'},3.90);"
js+=limb('family','near',33.86,-67.82,.56,4.12)
js+=limb('family','far',-20,30,.35,4.10)
js+="tl.to('#family-eyes',{x:4,y:-4,duration:.3},4.25);"
write('S06',r,js,{'chair_pull':[.55,1.4],'release':[1.48,1.68],'approach_front_of_seat':[1.7,2.9],'hand_and_foot_support':[2.9,3.2],'supported_climb_and_sit':[3.2,4.15],'shared_plan_gesture':[4.12,4.68]},[.1,1.1,1.45,2.15,2.85,3.15,3.50,3.85,4.3,5.5],[[.65,1.45],[2.85,4.15]])

r=load('S11/01-offer')
parent=find(r,'adult-placement')
arms=[e for e in parent if e.get('d','').startswith('M49 108')]
for i,e in enumerate(arms):e.set('id','parent-offer-arm-'+str(i))
hand=next(e for e in parent if e.tag==NS+'circle' and abs(float(e.get('cx',0))-103.846)<.01);hand.set('id','parent-offer-hand')
parent_thumb=next(e for e in r if e.tag==NS+'circle' and e.get('cx')=='330');parent_thumb.set('id','parent-grip')
book=find(r,'notebook');wrap(r,book,'book-insertion')
student_grip=tag('circle',{'id':'student-grip','cx':'410','cy':'730','r':'10','fill':'#FFAC3C','stroke':'#30313B','stroke-width':'3'})
r.append(student_grip)
def local(x,y):return ((x-390)/1.55-25,(y-725)/1.55-72)
js=limb('prepare','far',*local(410,730),.65,2.30)
js+="tl.to('#student-grip',{opacity:1,duration:.06},2.95);"
# Parent retains the book until recipient contact, then releases before insertion.
lx=(310-195)/1.3;ly=(805-570)/1.3
pd=f'M49 108Q{(49+lx)*.5:.5f} {(108+ly)*.5:.5f} {lx:.5f} {ly:.5f}'
for i in range(2):js+=f"tl.to('#parent-offer-arm-{i}',{{attr:{{d:'{pd}'}},duration:.50,ease:'power2.inOut'}},3.23);"
js+=f"tl.to('#parent-offer-hand',{{attr:{{cx:{lx:.5f},cy:{ly:.5f}}},duration:.50,ease:'power2.inOut'}},3.23);tl.to('#parent-grip',{{attr:{{cx:310,cy:805}},duration:.50,ease:'power2.inOut'}},3.23);"
js+="tl.to('#book-insertion',{y:110,duration:1.12,ease:'power2.inOut'},3.84);tl.to('#student-grip',{attr:{cy:840},duration:1.12,ease:'power2.inOut'},3.84);"
js+=limb('prepare','far',*local(410,840),1.12,3.84)
js+=limb('prepare','far',*local(435,840),.35,5.12)
js+="tl.to('#student-grip',{attr:{cx:435},duration:.35,ease:'power2.inOut'},5.12);tl.to('#student-grip',{opacity:0,duration:.14},5.50);tl.to('#prepare-eyes',{x:-3,y:3,duration:.3},4.4);"
write('S11',r,js,{'reach_to_notebook':[2.3,2.95],'shared_grip':[2.95,3.23],'parent_release':[3.23,3.73],'insert_with_held_book':[3.84,4.96],'student_release':[5.12,5.64],'ready_hold':[5.64,6.811833333333]},[.1,2.6,2.98,3.5,3.8,4.2,4.65,5.15,5.6,6.6],[[2.55,3.75],[3.85,5.5]])
(OUT/'pilot_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'production_status.json').write_text(json.dumps({'phase':'authored_pending_visual_checks','motion_approved':False,'master_modified':False,'voice_modified':False,'approved_frame_reference':'../S06-S11-design-r1/APPROVAL.json','pilots':records},ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
