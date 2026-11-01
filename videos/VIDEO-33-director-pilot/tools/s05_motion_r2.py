"""Fix S05 logic: a real hinged paper cover uncovers a rigid illustration.

Architecture and balcony never scale, skew, morph or fade. The mascot follows
the projected free edge of one rigid 3D cover, then releases it before settling.
"""
import math,json,shutil,wave
from pathlib import Path
from prepare import ROOT,digest
from s05_frame_v3 import scene as architecture
from final_frames_v2 import p

OUT=ROOT/'revisions/S05-motion-r2'
PERSPECTIVE=1400
def projected(theta):
    a=math.radians(theta);z=337*math.sin(a);f=PERSPECTIVE/(PERSPECTIVE-z)
    return 431-337*math.cos(a)*f,681+204*f
def easing(t):return 4*t*t*t if t<.5 else 1-((-2*t+2)**3)/2

def main():
    if OUT.exists():raise RuntimeError('Refusing to overwrite an existing revision')
    (OUT/'assets').mkdir(parents=True);(OUT/'renders').mkdir()
    for src,name in [(ROOT/'assets/fonts/segoe-ui-black.ttf','display.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js'),(ROOT/'assets/valletta.jpg','valletta.jpg'),(ROOT/'pilots/S05/assets/voice.wav','voice.wav')]:shutil.copy2(src,OUT/'assets'/name)
    with wave.open(str(OUT/'assets/voice.wav'),'rb') as w:duration=w.getnframes()/w.getframerate()
    a=architecture()
    # Keep the architecture exactly rigid. Only identify the actor and its joints.
    actor_start='<g transform="translate(508 818) scale(1.03)">'
    a=a.replace(actor_start,'<g id="r2-walk">'+actor_start,1)+'</g>'
    a=a.replace('<path d="M48 143L41 190L18 194M90 143L98 190L120 194"','<path id="r2-legs" d="M48 143L41 190L18 194M90 143L98 190L120 194"')
    # The old freestanding pull tab is removed: the only handle belongs to the actual cover.
    a=a.replace(p('M469 909L483 873L507 884L493 921Z','#FFD183'),'')
    a=a.replace(p('M481 895L493 901','none','#D3A15D',2),'')
    cover_svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 337 562" width="337" height="562">
      <path d="M1 2L336 1V560L2 561Z" fill="#FFF2D6" stroke="#30313B" stroke-width="3"/>
      <path d="M321 4V558" stroke="#D5BA91" stroke-width="4"/>
      <path d="M26 112L276 104V447L26 459ZM26 112L276 104L300 122V464L276 447M26 171L276 162M26 350L276 340" fill="none" stroke="#86AAA7" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M53 213L209 204L229 216V305L70 320L53 307ZM70 225L229 216M70 225V320M109 222V315M148 219V311M188 215V307M70 268L229 255" fill="none" stroke="#438A83" stroke-width="2.6"/>
      <path d="M104 451V390Q134 353 162 384V446M25 476L299 459" fill="none" stroke="#86AAA7" stroke-width="2.5"/>
      <path d="M-7 477L13 474L17 494L-5 497Z" fill="#FFD183" stroke="#30313B" stroke-width="2"/>
    </svg>'''
    # Cover projection and actor trajectory are both authored from the same hinge geometry.
    movement=[];hand=[]
    count=48;open_at=2.52;open_duration=2.02
    for i in range(1,count+1):
        t=i/count;theta=90*easing(t);hx,hy=projected(theta)
        body_x=hx+41;end_x=-66.75/1.03;end_y=(hy-892.16)/1.03
        movement.append({'x':round(body_x-508,5),'duration':open_duration/count,'ease':'none'})
        hand.append({'x':round(end_x,5),'y':round(end_y,5),'duration':open_duration/count,'ease':'none'})
    # Joint-path keyframes are separate but use exactly the same samples as the cover.
    armkeys=[];handkeys=[]
    for pos in hand:
        x,y=pos['x'],pos['y'];t=pos['duration']
        armkeys.append({'attr':{'d':f'M0 0Q-38 {y*.45:.5f} {x:.5f} {y:.5f}'},'duration':t,'ease':'none'})
        handkeys.append({'attr':{'cx':x,'cy':y},'duration':t,'ease':'none'})
    js=f'''
      const tl=gsap.timeline({{paused:true}});
      tl.fromTo('#r2-walk',{{x:-373}},{{x:-373,duration:.01}},0);
      tl.fromTo('#s05v3-far-path',{{attr:{{d:'M0 0Q-28 14-43 27'}}}},
        {{attr:{{d:'M0 0Q-38-3-64.80583-6.95146'}},duration:.5,ease:'power2.inOut'}},1.65);
      tl.fromTo('#s05v3-far-hand',{{attr:{{cx:-43,cy:27}}}},
        {{attr:{{cx:-64.80583,cy:-6.95146}},duration:.5,ease:'power2.inOut'}},1.65);
      // A single intact paper leaf rotates on a fixed vertical hinge; the building does not move.
      tl.fromTo('#r2-cover',{{rotationY:0,transformPerspective:1400,transformOrigin:'100% 50%'}},
        {{rotationY:90,duration:{open_duration},ease:'power2.inOut'}},{open_at});
      tl.to('#r2-walk',{{keyframes:{json.dumps(movement)},ease:'none'}},{open_at});
      tl.to('#s05v3-far-path',{{keyframes:{json.dumps(armkeys)},ease:'none'}},{open_at});
      tl.to('#s05v3-far-hand',{{keyframes:{json.dumps(handkeys)},ease:'none'}},{open_at});
      // Side steps have one foot planted and the other lifted; no body bob disrupts the grip.
      const rest='M48 143L41 190L18 194M90 143L98 190L120 194';
      const stepA='M48 143L41 173L20 183M90 143L98 190L120 194';
      const stepB='M48 143L41 190L18 194M90 143L96 173L116 183';
      [2.58,3.12,3.66,4.20].forEach((at,i)=>{{
        tl.to('#r2-legs',{{attr:{{d:i%2?stepB:stepA}},duration:.14,ease:'sine.inOut'}},at);
        tl.to('#r2-legs',{{attr:{{d:rest}},duration:.16,ease:'sine.inOut'}},at+.19);
      }});
      // Release precedes the last step: the hand no longer pretends to pull an unrelated tab.
      tl.to('#s05v3-far-path',{{attr:{{d:'M0 0Q-26 13-43 25'}},duration:.36,ease:'power2.inOut'}},4.60);
      tl.to('#s05v3-far-hand',{{attr:{{cx:-43,cy:25}},duration:.36,ease:'power2.inOut'}},4.60);
      tl.to('#r2-walk',{{x:0,duration:.37,ease:'power2.out'}},4.66);
      tl.fromTo('#r2-title',{{opacity:0,y:7}},{{opacity:1,y:0,duration:.22}},4.95);
      window.__timelines['s05-motion-r2']=tl;
    '''
    page=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>S05 motion r2</title><script src="assets/gsap.min.js"></script><style>
    @font-face{{font-family:Display;src:url('assets/display.ttf');font-weight:900;font-display:block}}
    html,body{{width:100%;height:100%;margin:0;overflow:hidden}}
    #s05-motion-r2{{position:relative;width:100%;height:100%;background:#FFF0E5;overflow:hidden}}
    #world{{position:absolute;inset:0;width:720px;height:1280px}}
    #r2-cover-anchor{{position:absolute;left:94px;top:400px;width:337px;height:562px;pointer-events:none}}
    #r2-cover{{position:absolute;inset:0;transform-style:preserve-3d}}
    #r2-cover svg{{display:block;overflow:visible}}
    #r2-title{{position:absolute;left:60px;top:162px;width:600px;text-align:center;margin:0;color:#0870AC;font:900 68px/1.3 Display,sans-serif}}
    #cover-title{{position:absolute;left:22px;top:32px;width:290px;text-align:center;color:#0870AC;font:900 38px/1.3 Display,sans-serif}}
    </style></head><body><div id="s05-motion-r2" data-composition-id="s05-motion-r2" data-width="720" data-height="1280" data-duration="{duration:.12f}" data-fps="30">
    <svg id="world" xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280">{a}</svg>
    <div id="r2-cover-anchor"><div id="r2-cover">{cover_svg}<div id="cover-title">MALTA</div></div></div>
    <h1 id="r2-title">MALTA</h1>
    <audio id="r2-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="2"></audio></div><script>{js}</script></body></html>'''
    # Put the moving actor above the paper leaf by duplicating only its SVG transport in the foreground.
    # This preserves arm occlusion while the world/architecture remain behind the cover.
    start=a.index('<g id="r2-walk">');actor=a[start:]
    background=a[:start]
    page=page.replace(f'{a}</svg>',f'{background}</svg>',1)
    actor_svg=f'<svg id="r2-foreground" xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280" style="position:absolute;inset:0;pointer-events:none">{actor}</svg>'
    page=page.replace('<h1 id="r2-title">',actor_svg+'<h1 id="r2-title">')
    (OUT/'index.html').write_text(page,encoding='utf-8')
    (OUT/'hyperframes.json').write_text(json.dumps({'authoringSkill':'general-video','media':{'autoProxy':False}}),encoding='utf-8')
    (OUT/'DIRECTION.json').write_text(json.dumps({'scene':'S05','revision':'motion-r2','reason':'User rejected r1 as illogical / rubbery. Building and balcony stay completely rigid; one printed paper leaf opens about its real corner hinge. Actor side-steps while holding the same free edge, releases before settling.','duration':duration,'hinge':[431,681],'cover_size':[337,562],'perspective':1400,'opening_interval':[open_at,open_at+open_duration],'proof_times':[.3,2.15,3.15,3.75,4.35,5.3],'voice_sha256':digest(OUT/'assets/voice.wav'),'S09':'unchanged; use revisions/pilots-approved-frames-r1/S09/renders/pilot.mp4','approval':'pending_user_review'},ensure_ascii=False,indent=2),encoding='utf-8')
    print(OUT)

if __name__=='__main__':main()
