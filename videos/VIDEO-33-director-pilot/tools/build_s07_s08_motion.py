"""Build isolated motion pilots from the approved S07/S08 vector frames."""
from pathlib import Path
import xml.etree.ElementTree as ET
import json, shutil, hashlib, wave

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'revisions/S07-S08-design-r1'
OUT=ROOT/'revisions/S07-S08-motion-r1'
if OUT.exists(): raise SystemExit('Refusing to overwrite motion revision')
OUT.mkdir(parents=True)
ET.register_namespace('', 'http://www.w3.org/2000/svg')
NS='{http://www.w3.org/2000/svg}'
def tag(name, attrs=None):return ET.Element(NS+name,attrs or {})
def find(root, id):return next(x for x in root.iter() if x.get('id')==id)
def wrap(root, element, id):
    parent=next(p for p in root.iter() if element in list(p));i=list(parent).index(element);parent.remove(element);g=tag('g',{'id':id});g.append(element);parent.insert(i,g);return g
def prefix(root,p):
    ids={e.get('id'):p+'-'+e.get('id') for e in root.iter() if e.get('id')}
    for e in root.iter():
        for k,v in list(e.attrib.items()):
            if k=='id':e.set(k,ids[v])
            else:
                for old,new in ids.items():v=v.replace('url(#'+old+')','url(#'+new+')')
                e.set(k,v)
    return root
def load(rel):return ET.parse(REF/rel/'layered-art.svg').getroot()
def dump(root):return ET.tostring(root,encoding='unicode')
def hand_js(prefix,fx,fy,duration,time):
    return f"tl.to('#{prefix}-far-path',{{attr:{{d:'M0 0Q{fx*.55:.4f} {fy*.35:.4f} {fx:.4f} {fy:.4f}'}},duration:{duration},ease:'power2.inOut'}},{time});tl.to('#{prefix}-far-hand',{{attr:{{cx:{fx:.4f},cy:{fy:.4f}}},duration:{duration},ease:'power2.inOut'}},{time});"

approved=json.loads((REF/'APPROVAL.json').read_text(encoding='utf-8'))
for f in approved['frames']:
    assert hashlib.sha256((REF/f['file']).read_bytes()).hexdigest()==f['sha256']
board=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'))
records=[]
def write(sid,arts,js,cues,proofs):
    s=next(x for x in board['scenes'] if x['scene_id']==sid);folder=OUT/sid;assets=folder/'assets';assets.mkdir(parents=True)
    for a,b in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js'),(ROOT/f'inputs/audio/seg_{sid[1:]}.wav','voice.wav')]:shutil.copy2(a,assets/b)
    with wave.open(str(assets/'voice.wav'),'rb') as w:assert w.getnframes()==s['sample_frames'];duration=w.getnframes()/w.getframerate()
    text=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}*{{box-sizing:border-box}}html,body{{width:100%;height:100%;margin:0;overflow:hidden;background:#FFF8E9}}#root{{width:100%;height:100%;position:relative}}.shot{{position:absolute;inset:0;width:100%;height:100%}}.shot svg{{display:block;width:100%;height:100%}}#online-screen,#study-shot,#living-shot,#work-shot{{opacity:0}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="{duration:.12f}" data-fps="30">{arts}<audio id="{sid}-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="1"></audio></div><script>const tl=gsap.timeline({{paused:true}});{js}tl.to({{v:0}},{{v:1,duration:{duration:.12f},ease:'none'}},0);window.__timelines['root']=tl;</script></body></html>'''
    (folder/'index.html').write_text(text,encoding='utf-8')
    (folder/'DIRECTION.json').write_text(json.dumps({'scene':sid,'duration':duration,'source_start_sample':s['start_sample'],'source_end_sample':s['end_sample'],'sample_rate':24000,'raw_text':s['raw_text'],'corrected_text':s['corrected_text'],'original_voice_sha256':hashlib.sha256((assets/'voice.wav').read_bytes()).hexdigest(),'approved_frame_reference':'../../S07-S08-design-r1','timing_basis':'original sample boundaries; existing ASR word cues for internal beats, not independent phonetic alignment','cues':cues,'proof_times':proofs,'approval':'motion_pending_user_review'},ensure_ascii=False,indent=2),encoding='utf-8')
    records.append({'scene':sid,'path':str(folder.relative_to(OUT)),'duration':duration,'proof_times':proofs,'cues':cues})

# S07: Keep all approved screen and mascot geometry. The arm starts in the
# ready pose, touches a precise scene point, releases and waves from its shoulder.
r=load('S07/03-connected')
screen=next(e for e in r if e.get('clip-path')=='url(#screen-mask)')
screen.set('id','online-screen')
ready=load('S07/01-ready')
offline=tag('g',{'id':'offline-screen'})
for e in list(ready):
    if e.get('x')=='89' or (e.tag==NS+'circle' and e.get('cy') in ['510','674']) or (e.tag==NS+'path' and e.get('d','').startswith('M269 639')):
        offline.append(e)
assert len(offline)>=5
r.insert(list(r).index(screen)+1,offline)
portrait=next(e for e in screen if e.get('transform','').startswith('translate(310'))
wavepaths=[e for e in list(portrait) if e.get('d','').startswith('M95 135')]
for i,e in enumerate(wavepaths):e.set('id','parent-wave-'+str(i))
palm=next(e for e in portrait if e.get('d','').startswith('M153 40'));wrap(r,palm,'parent-palm-motion')
button=next(e for e in find(r,'call-controls') if e.get('x')=='411');button.set('id','call-button')
path=find(r,'call-far-path');path.set('d','M0 0Q-15.4 -11.2 -28 -32');h=find(r,'call-far-hand');h.set('cx','-28');h.set('cy','-32')
js="tl.set('#offline-screen',{opacity:1},0);tl.set('#call-button',{fill:'#25836A'},0);"
# Align connection to the family/connection phrase, not the opening Malta phrase.
js+=hand_js('call',-52.5862068966,-55.4482758621,.72,1.05)
js+="tl.to('#call-button',{fill:'#D96D75',duration:.18},1.86);tl.to('#online-screen',{opacity:1,duration:.32},1.92);tl.to('#offline-screen',{opacity:0,duration:.32},1.92);"
js+=hand_js('call',-18,-97,.55,2.30)
for time,end in [(2.9,10),(3.24,0),(3.58,8),(3.9,0)]:
    for i in range(2):js+=f"tl.to('#parent-wave-{i}',{{attr:{{d:'M95 135Q154 151 {157+end} {90+end*.3}L{153+end} {39+end*.3}'}},duration:.27,ease:'sine.inOut'}},{time});"
    js+=f"tl.to('#parent-palm-motion',{{x:{end},y:{end*.3},duration:.27,ease:'sine.inOut'}},{time});"
for t,fx,fy in [(2.95,-10,-94),(3.28,-18,-97),(3.61,-11,-94),(3.94,-18,-97)]:js+=hand_js('call',fx,fy,.26,t)
js+="tl.to('#call-eyes',{x:-3,y:-3,duration:.3},1.98);"
write('S07','<div class="shot">'+dump(r)+'</div>',js,{'reach':[1.05,1.77],'contact':1.77,'connection':[1.92,2.24],'release_and_raise':[2.3,2.85],'greeting':[2.9,4.2]},[.15,1.55,1.77,2.14,2.75,3.2,4.42])

# S08: One large arrival scene followed by three dedicated activity shots.
arr=load('S08/01-arrive')
adult=find(arr,'adult-placement');luggage=find(arr,'suitcase')
travel=tag('g',{'id':'parent-and-luggage-travel'})
for e in [luggage,adult]:arr.remove(e);travel.append(e)
arr.insert(len(arr)-1,travel)
paths=[e for e in adult if e.get('d','').startswith('M49 108')]
for i,e in enumerate(paths):e.set('id','parent-hello-arm-'+str(i))
hello_hand=next(e for e in adult if e.tag==NS+'circle' and e.get('cx')=='91');hello_hand.set('id','parent-hello-hand')
pants=next(e for e in adult if e.get('d','').startswith('M-45 214'));pants.set('id','parent-pants')
shoes=next(e for e in adult if e.get('d','').startswith('M-43 328'));shoes.set('id','parent-shoes')
art={}
for key,root in [('arr',arr),('study',load('S08/03-study')),('living',load('S08/04-living')),('work',load('S08/05-work'))]:
    if key=='study':
        pp=[e for e in root if e.get('d','').startswith(('M355 795','M385 826'))]
        g=tag('g',{'id':'pencil-motion'})
        for e in pp:root.remove(e);g.append(e)
        root.append(g)
        root.append(tag('path',{'id':'writing-mark','d':'M391 833L403.06 838.36','fill':'none','stroke':'#087BC1','stroke-width':'3','stroke-linecap':'round'}))
    if key=='living':
        wrap(root,find(root,'held-book'),'book-motion')
        thumb=next(e for e in root if e.tag==NS+'circle' and e.get('cx')=='423.1');thumb.set('id','book-thumb')
    if key=='work':
        bars=next(e for e in find(root,'work-laptop') if e.get('d','').startswith('M382 756'));bars.set('id','screen-bars')
        root.append(tag('rect',{'id':'typing-key','x':'365','y':'816','width':'25','height':'9','rx':'2','fill':'#A990D5','opacity':'0'}))
    art[key]=prefix(root,key)
start=823751/24000
study=37.28-start;living=37.96-start;work=38.74-start
js="tl.set('#arr-shot',{opacity:1},0);tl.fromTo('#arr-parent-and-luggage-travel',{x:0},{x:35,duration:1.28,ease:'power1.inOut'},.12);"
rest='M-45 214L-42 330L-9 331L1 239L14 331H48L43 214Z'
step='M-45 214L-48 330L-15 331L1 239L20 331H54L43 214Z'
shoe_rest='M-43 328H-8L-8 346H-65Q-66 336-43 328ZM15 329H48L65 343Q64 350 17 347Z'
shoe_step='M-49 328H-14L-14 346H-71Q-72 336-49 328ZM21 329H54L71 343Q70 350 23 347Z'
for t,pd,sd in [(.18,step,shoe_step),(.5,rest,shoe_rest),(.82,step,shoe_step),(1.14,rest,shoe_rest)]:
    js+=f"tl.to('#arr-parent-pants',{{attr:{{d:'{pd}'}},duration:.22,ease:'sine.inOut'}},{t});tl.to('#arr-parent-shoes',{{attr:{{d:'{sd}'}},duration:.22,ease:'sine.inOut'}},{t});"
for i in range(2):js+=f"tl.to('#arr-parent-hello-arm-{i}',{{attr:{{d:'M49 108Q84 124 88 91L91 55'}},duration:.4,ease:'power2.inOut'}},1.45);"
js+="tl.to('#arr-parent-hello-hand',{attr:{cy:55},duration:.4,ease:'power2.inOut'},1.45);"
js+=hand_js('arr-travel',-42,-70,.42,1.58)
js+=hand_js('arr-travel',-36,-67,.23,2.12)+hand_js('arr-travel',-42,-70,.23,2.38)
for prev,nxt,t in [('arr','study',study),('study','living',living),('living','work',work)]:js+=f"tl.set('#{prev}-shot',{{opacity:0}},{t:.8f});tl.set('#{nxt}-shot',{{opacity:1}},{t:.8f});"
js+=f"tl.set('#study-writing-mark',{{strokeDasharray:14,strokeDashoffset:14}},0);tl.to('#study-pencil-motion',{{x:12.06,y:5.36,duration:.30,ease:'power1.inOut'}},{study+.12});tl.to('#study-writing-mark',{{strokeDashoffset:0,duration:.30,ease:'power1.inOut'}},{study+.12});"
js+=f"tl.to('#study-activity-near-path',{{attr:{{d:'M0 0Q23.4 14.7 39 49'}},duration:.30,ease:'power1.inOut'}},{study+.12});tl.to('#study-activity-near-hand',{{attr:{{cx:39,cy:49}},duration:.30,ease:'power1.inOut'}},{study+.12});tl.to('#study-activity-eyes',{{y:3,duration:.18}},{study+.05});"
# Lifted book and hand lower together, then the hand releases while book remains.
js+="tl.set('#living-book-motion',{y:-24},0);tl.set('#living-book-thumb',{y:-24},0);tl.set('#living-home-far-path',{attr:{d:'M0 0Q-20.9 8.9385 -38 25.5385'}},0);tl.set('#living-home-far-hand',{attr:{cx:-38,cy:25.5385}},0);"
js+=f"tl.to(['#living-book-motion','#living-book-thumb'],{{y:0,duration:.32,ease:'power2.out'}},{living+.03});"
js+=hand_js('living-home',-38,44,.32,living+.03)
js+=f"tl.set('#living-book-thumb',{{opacity:0}},{living+.37});"+hand_js('living-home',-23,55,.23,living+.38)
js+=f"tl.to('#work-activity-near-path',{{attr:{{d:'M0 0Q18 16.5 30 55'}},duration:.14,yoyo:true,repeat:3,ease:'sine.inOut'}},{work+.08});tl.to('#work-activity-near-hand',{{attr:{{cx:30,cy:55}},duration:.14,yoyo:true,repeat:3,ease:'sine.inOut'}},{work+.08});tl.to('#work-typing-key',{{opacity:.85,duration:.14,yoyo:true,repeat:3,ease:'sine.inOut'}},{work+.08});tl.fromTo('#work-screen-bars',{{opacity:.4}},{{opacity:1,duration:.35}},{work+.18});"
arts=''.join(f'<div id="{k}-shot" class="shot">{dump(v)}</div>' for k,v in art.items())
write('S08',arts,js,{'arrival_walk':[.12,1.4],'greeting':[1.45,2.61],'study_cut':study,'living_cut':living,'work_cut':work},[.15,.75,1.35,1.85,2.5,study+.35,living+.25,living+.65,work+.40,5.32])
(OUT/'pilot_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'production_status.json').write_text(json.dumps({'phase':'motion_authored_pending_checks_and_render','approved_frames':'../S07-S08-design-r1/APPROVAL.json','motion_approved':False,'master_modified':False,'original_voice_modified':False,'pilots':records},ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
