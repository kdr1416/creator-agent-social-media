"""Isolated S10/S12 motion pilots from approved static design R1."""
from pathlib import Path
import xml.etree.ElementTree as ET
import json, shutil, hashlib, wave

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'revisions/S10-S12-design-r1'
OUT=ROOT/'revisions/S10-S12-motion-r1'
if OUT.exists():raise SystemExit('Refusing to overwrite motion revision')
OUT.mkdir(parents=True)
ET.register_namespace('','http://www.w3.org/2000/svg');NS='{http://www.w3.org/2000/svg}'
def tag(name,attrs=None):return ET.Element(NS+name,attrs or {})
def find(r,id):return next(e for e in r.iter() if e.get('id')==id)
def load(rel):return ET.parse(REF/rel/'layered-art.svg').getroot()
def wrap(r,e,id):
    p=next(p for p in r.iter() if e in list(p));i=list(p).index(e);p.remove(e);g=tag('g',{'id':id});g.append(e);p.insert(i,g);return g
def prefix(r,p):
    ids={e.get('id'):p+'-'+e.get('id') for e in r.iter() if e.get('id')}
    for e in r.iter():
        for k,v in list(e.attrib.items()):
            if k=='id':e.set(k,ids[v])
            else:
                for old,new in ids.items():v=v.replace('url(#'+old+')','url(#'+new+')')
                e.set(k,v)
    return r
def dump(r):return ET.tostring(r,encoding='unicode')
def limb(p,which,x,y,d,t):
    return f"tl.to('#{p}-{which}-path',{{attr:{{d:'M0 0Q{x*.55:.6f} {y*.35:.6f} {x:.6f} {y:.6f}'}},duration:{d},ease:'power2.inOut'}},{t});tl.to('#{p}-{which}-hand',{{attr:{{cx:{x:.6f},cy:{y:.6f}}},duration:{d},ease:'power2.inOut'}},{t});"
board=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'))
approval=json.loads((REF/'APPROVAL.json').read_text(encoding='utf-8'))
for a in approval['reference_frame_manifest']:assert hashlib.sha256((REF/a['file']).read_bytes()).hexdigest()==a['sha256']
records=[]
def write(sid,art,js,cues,proofs,contacts):
    s=next(x for x in board['scenes'] if x['scene_id']==sid);f=OUT/sid;a=f/'assets';a.mkdir(parents=True)
    for source,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js'),(ROOT/s['audio_source'][0],'voice.wav')]:shutil.copy2(source,a/dest)
    with wave.open(str(a/'voice.wav'),'rb') as w:n=w.getnframes();sr=w.getframerate();assert n==s['sample_frames'];duration=n/sr
    text=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{width:100%;height:100%;margin:0;overflow:hidden;background:#FFF8E9}}#root{{position:relative;width:100%;height:100%}}.shot{{position:absolute;inset:0;width:100%;height:100%}}svg{{display:block;width:100%;height:100%}}#family-shot,#family-headline,#family-condition,#family-labels{{opacity:0}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="{duration:.12f}" data-fps="30">{art}<audio id="{sid}-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="1"></audio></div><script>const tl=gsap.timeline({{paused:true}});{js}tl.to({{v:0}},{{v:1,duration:{duration:.12f},ease:'none'}},0);window.__timelines['root']=tl;</script></body></html>'''
    (f/'index.html').write_text(text,encoding='utf-8')
    d={'scene':sid,'duration':duration,'sample_frames':n,'sample_rate':sr,'source_start_sample':s['start_sample'],'source_end_sample':s['end_sample'],'source_segments':s['source_segments'],'source_audio':s['audio_source'],'raw_text':s['raw_text'],'corrected_text':s['corrected_text'],'source_audio_hashes':{s['audio_source'][0]:hashlib.sha256((a/'voice.wav').read_bytes()).hexdigest()},'original_voice_sha256':hashlib.sha256((a/'voice.wav').read_bytes()).hexdigest(),'cues':cues,'proof_times':proofs,'contact_ranges':contacts,'approval':'motion_pending_user_review','approved_frame_reference':'../../S10-S12-design-r1/APPROVAL.json','timing_basis':'Original sample bounds unchanged. S10 word cues from existing ASR; S12 physical beat timing directed within original slice.'}
    (f/'DIRECTION.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8');records.append(d)

# S10: Editorial cut from the approved price composition to a wider family
# composition. Relatives are already entering that shot; no long sliding parade.
cost=prefix(load('S10/01-cost'),'cost')
family=load('S10/02-arrive')
texts=[e for e in family if e.tag==NS+'text']
texts[0].set('id','headline');texts[1].set('id','condition')
labels=tag('g',{'id':'labels'})
for e in texts[2:]:family.remove(e);labels.append(e)
family.append(labels)
gm=find(family,'oldest-generation');wrap(family,gm,'grandparent-step')
pa=find(family,'parent-generation');wrap(family,pa,'parent-step')
old_arms=[e for e in gm if e.get('d','').startswith('M35 102')]
for i,e in enumerate(old_arms):e.set('id','grandparent-link-arm-'+str(i))
old_hand=next(e for e in gm if e.tag==NS+'circle' and e.get('cx')=='52');old_hand.set('id','grandparent-link-hand')
cane=next(e for e in gm if e.get('d','').startswith('M-69 179'));wrap(family,cane,'cane-lift')
left_arm=[e for e in gm if e.get('d','').startswith('M-42 104')]
for i,e in enumerate(left_arm):e.set('id','cane-arm-'+str(i))
cane_hand=next(e for e in gm if e.tag==NS+'circle' and e.get('cx')=='-51');cane_hand.set('id','cane-hand')
old_legs=next(e for e in gm if e.get('d','').startswith('M-34 279'));old_legs.set('id','grandparent-legs')
old_shoes=next(e for e in gm if e.get('d','').startswith('M-35 318'));old_shoes.set('id','grandparent-shoes')
dad=find(family,'father');dad_legs=next(e for e in dad if e.get('d','').startswith('M-66 194'));dad_legs.set('id','parent-legs')
dad_shoes=next(e for e in dad if e.get('d','').startswith('M-62 359'));dad_shoes.set('id','parent-shoes')
family=prefix(family,'family')
js=limb('cost-generation-child','far',-34,-57,.55,.55)
js+="tl.to('#cost-generation-child-eyes',{x:-3,y:-4,duration:.3},.8);tl.set('#cost-shot',{opacity:0},2.75);tl.set('#family-shot',{opacity:1},2.75);"
js+="tl.to('#family-grandparent-step',{x:28,duration:1.0,ease:'power1.inOut'},2.85);tl.to('#family-parent-step',{x:9.8,duration:1.0,ease:'power1.inOut'},2.85);"
for time,lift in [(2.86,-6),(3.58,0)]:
    js+=f"tl.to('#family-cane-lift',{{y:{lift},duration:.24,ease:'power1.inOut'}},{time});tl.to('#family-cane-hand',{{attr:{{cy:{175+lift}}},duration:.24,ease:'power1.inOut'}},{time});"
    for i in range(2):js+=f"tl.to('#family-cane-arm-{i}',{{attr:{{d:'M-42 104Q-66 136 -51 {175+lift}'}},duration:.24,ease:'power1.inOut'}},{time});"
# Small matched leg/shoe shifts during the short supported steps.
gm_rest='M-34 279V324H-9L-6 278M12 278L15 324H39L36 276'
gm_step='M-34 279V324H-15L-6 278M12 278L21 324H45L36 276'
gs_rest='M-35 318H-9V333H-53Q-52 323-35 318ZM16 318H39L55 330Q52 336 16 333Z'
gs_step='M-41 318H-15V333H-59Q-58 323-41 318ZM22 318H45L61 330Q58 336 22 333Z'
dp_rest='M-66 194L-60 363L-25 363L-10 230L7 363H45L58 194Z'
dp_step='M-66 194L-66 363L-31 363L-10 230L13 363H51L58 194Z'
ds_rest='M-62 359H-24V378H-85Q-87 367-62 359ZM7 359H45L69 374Q71 382 8 379Z'
ds_step='M-68 359H-30V378H-91Q-93 367-68 359ZM13 359H51L75 374Q77 382 14 379Z'
for t,gm_d,gs_d,dp_d,ds_d in [(2.9,gm_step,gs_step,dp_step,ds_step),(3.22,gm_rest,gs_rest,dp_rest,ds_rest),(3.48,gm_step,gs_step,dp_step,ds_step),(3.76,gm_rest,gs_rest,dp_rest,ds_rest)]:
    for id,d in [('grandparent-legs',gm_d),('grandparent-shoes',gs_d),('parent-legs',dp_d),('parent-shoes',ds_d)]:js+=f"tl.to('#family-{id}',{{attr:{{d:'{d}'}},duration:.20,ease:'sine.inOut'}},{t});"
for i in range(2):js+=f"tl.to('#family-grandparent-link-arm-{i}',{{attr:{{d:'M35 102Q56 132 61 185'}},duration:.48,ease:'power2.inOut'}},3.95);"
js+="tl.to('#family-grandparent-link-hand',{attr:{cx:61,cy:185},duration:.48,ease:'power2.inOut'},3.95);tl.to('#family-condition',{opacity:1,duration:.24},4.0);tl.to('#family-labels',{opacity:1,duration:.28},4.48);tl.to('#family-headline',{opacity:1,duration:.24},4.0);"
art='<div id="cost-shot" class="shot">'+dump(cost)+'</div><div id="family-shot" class="shot">'+dump(family)+'</div>'
write('S10',art,js,{'price_read':[0,2.75],'cut_to_wider_family':2.75,'short_supported_steps':[2.85,3.96],'hand_link':[3.95,4.43],'relationship_labels':[4.48,4.76],'four_generation_headline':[4.0,4.24]},[.1,1.6,2.65,2.8,3.3,3.95,4.43,5.39,6.02],[[2.85,4.48]])

# S12: Keep the model in place; local rotor rotates about its scene-space hub.
r=load('S12/01-ready')
find(r,'rotor').insert(0,tag('circle',{'id':'rotor-rig-envelope','cx':'0','cy':'0','r':'150','fill':'none','stroke':'none'}))
eyes=find(r,'experiment-eyes');wrap(r,eyes,'experiment-eye-motion')
def near(x,y):return ((x-110)/1.65-109,(y-680)/1.65-83)
js=limb('experiment','near',*near(385,822),.45,.55)
js+=limb('experiment','near',*near(385,829),.13,1.0)
js+="tl.to('#push-button',{attr:{cy:829},duration:.13,ease:'power2.inOut'},1.0);tl.to('#power-indicator',{fill:'#52A985',duration:.12},1.08);"
js+="tl.fromTo('#rotor',{rotation:0,svgOrigin:'0 0'},{rotation:768,svgOrigin:'0 0',duration:2.401458333333,ease:'power1.in'},1.13);"
js+=limb('experiment','near',*near(385,822),.13,1.47)
js+="tl.to('#push-button',{attr:{cy:822},duration:.13,ease:'power2.inOut'},1.47);"
js+=limb('experiment','near',*near(368,799),.35,1.60)
js+="tl.to('#experiment-eye-motion',{x:2,y:-3,duration:.35},1.50);"
write('S12','<div class="shot">'+dump(r)+'</div>',js,{'reach':[.55,1.0],'press':[1.0,1.13],'power_and_acceleration':[1.08,3.531458333333],'release':[1.47,1.95],'rotor_pivot_scene':[490,505],'rotor_final_angle':768},[.1,.84,1.02,1.13,1.4,1.75,2.2,2.8,3.4],[[.8,1.96],[2.15,3.45]])
(OUT/'pilot_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'production_status.json').write_text(json.dumps({'phase':'authored_pending_visual_checks','motion_approved':False,'master_modified':False,'voice_modified':False,'approved_frame_reference':'../S10-S12-design-r1/APPROVAL.json','pilots':records},ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
