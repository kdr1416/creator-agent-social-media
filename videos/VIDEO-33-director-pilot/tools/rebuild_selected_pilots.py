"""Animate approved S05-v3 / S09-v2 final frames in a new revision folder.

Keep all original pilots, approved stills, PCM and raw transcript untouched.
"""
from pathlib import Path
import json, shutil, wave, hashlib, math
from prepare import ROOT, save, digest
from s05_frame_v3 import scene as approved_s05
from final_frames_v2 import p,r,e,building,token,I

OUT=ROOT/'revisions/pilots-approved-frames-r1'

def wrap(content,id):return f'<g id="{id}">{content}</g>'

def s05():
    art=approved_s05()
    photo_start=p('M65 314L612 294L646 633L90 665Z','#FFFDF5')
    photo_end='<image href="assets/valletta.jpg" x="76" y="307" width="563" height="350" preserveAspectRatio="xMidYMid slice" clip-path="url(#photo)"/>'
    art=art.replace(photo_start,'<g id="r05-photo">'+photo_start).replace(photo_end,photo_end+'</g>')
    art=art.replace('<g filter="url(#soft)">','<g id="r05-architecture" filter="url(#soft)">',1)
    balcony_start=p('M144 554L181 525L389 509L409 532L181 554Z','#83B5A3')
    door_start=p('M149 949V846Q149 792 203 789Q257 784 257 835V938Z','#FCEAC8','#BBA07E',3)
    art=art.replace(balcony_start,'<g id="r05-gallery">'+balcony_start).replace(door_start,'</g>'+door_start)
    tab_start=p('M469 909L483 873L507 884L493 921Z','#FFD183')
    tab_end=p('M481 895L493 901','none','#D3A15D',2)
    art=art.replace(tab_start,'<g id="r05-pull-tab">'+tab_start).replace(tab_end,tab_end+'</g>')
    # The flap only introduces the geographic photograph; it is not an information card.
    flap=wrap(p('M68 315L612 294L646 633L90 665Z','#FFF1D3')+p('M99 373L565 355M105 397L441 385M113 576L579 551','none','#D8C6A7',3),'r05-photo-fold')
    art=art.replace(photo_end+'</g>',photo_end+'</g>'+flap)
    js='''
    // Use handoff ASR word times as approximate cues, while keeping sample timing exact.
    tl.fromTo('#r05-photo-fold',{scaleX:1,svgOrigin:'68 490'},
      {scaleX:.015,duration:1.45,ease:'power2.inOut'},.55);
    tl.to('#r05-photo-fold',{opacity:0,duration:.12},1.97);
    tl.fromTo('#s05v3-far-path',{attr:{d:'M0 0Q-30 12-45 28'}},
      {attr:{d:'M0 0Q-49 4-73 8'},duration:.55,ease:'power2.inOut'},2.30);
    tl.fromTo('#s05v3-far-hand',{attr:{cx:-45,cy:28}},
      {attr:{cx:-73,cy:8},duration:.55,ease:'power2.inOut'},2.30);
    // Contact precedes pull; tab and hand have the same travel/ease over this interval.
    tl.fromTo('#r05-pull-tab',{x:-35,y:15},{x:0,y:0,duration:.9,ease:'power2.inOut'},3.30);
    tl.to('#s05v3-far-path',{attr:{d:'M0 0Q-23 0-39-7'},duration:.9,ease:'power2.inOut'},3.30);
    tl.to('#s05v3-far-hand',{attr:{cx:-39,cy:-7},duration:.9,ease:'power2.inOut'},3.30);
    // Two joined wall planes hinge up from their common paper fold; the timber gallery opens separately.
    tl.fromTo('#r05-architecture',{scaleY:.025,skewX:-28,svgOrigin:'431 940',opacity:0},
      {scaleY:1,skewX:0,opacity:1,duration:.84,ease:'power2.inOut'},3.36);
    // 'bất động sản' begins around local 4.349s in the preserved ASR timing.
    tl.fromTo('#r05-gallery',{scaleX:.035,x:4,svgOrigin:'144 649'},
      {scaleX:1,x:0,duration:.62,ease:'back.out(1.04)'},4.32);
    tl.fromTo('#r05-title',{opacity:0,y:9},{opacity:1,y:0,duration:.22,ease:'power2.out'},4.95);
    '''
    return art,js,'MALTA','#FFF0E5',68,60,162,600,[.15,2.0,3.72,4.62,5.35]

def bezier(a,b,c,d,n=14):
    result=[]
    for i in range(1,n+1):
        t=i/n;u=1-t
        result.append((u*u*u*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t*t*t*d[0],u*u*u*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t*t*t*d[1]))
    return result

def route(start,end,market):
    hub=(214,523)
    points=bezier(start,(start[0]-5,start[1]+35),(209,482),hub,6)
    if market=='a':points+=bezier(hub,(274,509),(305,424),end,16)
    elif market=='b':points+=bezier(hub,(437,485),(352,664),(510,720),16)+bezier((510,720),(529,726),(end[0]-10,end[1]-8),end,5)
    else:points+=bezier(hub,(71,654),(131,815),(220,909),18)+bezier((220,909),(228,921),(end[0]-10,end[1]-8),end,5)
    return points

def s09():
    a=p('M87 431L523 394L660 898L242 1030L66 915Z','#ECD4B4')
    a+=p('M66 915L242 1030L660 898V921L242 1050L66 937Z','#C8A47D')
    a+=p('M105 459L505 425M128 499L517 462M150 542L531 501','none','#E0BF99',2)
    a+=wrap(p('M214 537C437 485 352 664 510 720M214 537C71 654 131 815 220 909','none','#B79D8F',30)+p('M214 537C437 485 352 664 510 720M214 537C71 654 131 815 220 909','none','#FFFCED',20)+p('M214 537C437 485 352 664 510 720M214 537C71 654 131 815 220 909','none','#8EBDD0',3),'r09-rails')
    a+=e(214,534,62,44,'#DAB991')+e(214,523,62,44,'#FFF4DB')
    a+=wrap(p('M202 545L198 502L244 478L253 499L218 526L222 548Z','#A990D5')+e(211,528,9,7,'#FFCD74'),'r09-selector')
    a+=p('M90 468L150 412L269 443L242 493L130 513Z','#FFF3D9')+p('M90 468L130 513V535L91 491Z','#DDBA8E')
    for id,x,y,col in [('a',420,460,'#D9CBEA'),('b',525,751,'#B9DBDF'),('c',235,948,'#C9DFC4')]:
        a+=wrap(e(x,y+12,94,43,col)+e(x,y,94,43,'#FFF9EB'),'r09-platform-'+id)
    a+=wrap(building(350,326,.65,'#E8CCAB'),'r09-building-a')
    a+=wrap(building(468,608,.62,'#EED6B2'),'r09-building-b')
    a+=wrap(building(164,806,.62,'#EFD7B7'),'r09-building-c')
    # Precomputed path samples are seek-safe, offline and always land at the approved positions.
    tokens=[('a1',447,449,'capital',(124,472),'a',2.43,1.06),('a2',493,454,'home',(166,463),'a',2.77,1.04),
            ('b1',555,741,'office',(211,457),'b',3.10,1.45),('b2',596,737,'capital',(144,438),'b',3.48,1.40),
            ('c1',253,941,'home',(184,430),'c',3.81,1.68),('c2',302,934,'capital',(224,425),'c',4.16,1.64)]
    motions=[]
    for id,x,y,typ,start,market,at,dur in tokens:
        a+=wrap(token(x,y,typ),'r09-token-'+id)
        positions=route(start,(x,y),market)
        keys=[{'x':round(px-x,4),'y':round(py-y,4),'duration':dur/len(positions),'ease':'none'} for px,py in positions]
        motions.append(f"tl.fromTo('#r09-token-{id}',{{x:{start[0]-x},y:{start[1]-y}}},{{keyframes:{json.dumps(keys)},ease:'none'}},{at});")
    a+=wrap(p('M363 384Q372 374 383 384Q395 397 406 384M574 621Q585 611 596 621Q608 634 619 621M280 811Q292 801 303 811Q316 824 327 811','none','#B97A4C',3),'r09-local-risks')
    for x,y in [(107,452),(504,418),(638,887),(238,1022)]:a+=e(x,y,4,4,'#D0AE84')
    js='''
    tl.fromTo('#r09-initial-title',{opacity:0,y:6},{opacity:1,y:0,duration:.25},.25);
    tl.fromTo('#r09-selector',{rotation:-55,svgOrigin:'211 528'},
      {rotation:0,duration:.5,ease:'power2.inOut'},2.04);
    tl.fromTo('#r09-rails',{opacity:.28},{opacity:1,duration:.4},2.20);
    tl.to('#r09-initial-title',{opacity:0,y:-5,duration:.2},2.35);
    tl.fromTo('#r09-title',{opacity:0,y:7},{opacity:1,y:0,duration:.25},2.47);
    tl.fromTo('#r09-platform-a,#r09-platform-b,#r09-platform-c',{opacity:.35},{opacity:1,duration:.35},2.30);
    tl.fromTo('#r09-building-a',{scaleY:.02,svgOrigin:'420 460',opacity:0},{scaleY:1,opacity:1,duration:.47,ease:'power2.out'},3.20);
    tl.fromTo('#r09-building-b',{scaleY:.02,svgOrigin:'525 751',opacity:0},{scaleY:1,opacity:1,duration:.47,ease:'power2.out'},4.23);
    tl.fromTo('#r09-building-c',{scaleY:.02,svgOrigin:'235 948',opacity:0},{scaleY:1,opacity:1,duration:.47,ease:'power2.out'},5.16);
    '''+'\n'.join(motions)+'''
    tl.fromTo('#r09-local-risks',{opacity:0},{opacity:1,duration:.25},5.84);
    tl.fromTo('#r09-local-risks',{x:0},{x:3,duration:.14,repeat:3,yoyo:true,ease:'sine.inOut'},6.08);
    '''
    return a,js,'NHIỀU THỊ TRƯỜNG','#F0EAFB',44,50,160,620,[.15,2.55,3.65,4.85,7.1]

def main():
    if OUT.exists():raise RuntimeError('Revision already exists; refuse to overwrite.')
    OUT.mkdir(parents=True)
    approved=json.loads((ROOT/'research/visual-approvals.json').read_text(encoding='utf-8'))
    board=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'))
    before={str(p.relative_to(ROOT)):digest(p) for p in [ROOT/'inputs/source_audio.wav',ROOT/'research/visual-approvals.json',*[ROOT/f'pilots/{s}/renders/pilot.mp4' for s in ('S01','S05','S09')],*[ROOT/x['frame_path'] for x in approved['approved']]]}
    (OUT/'source-before.json').write_text(json.dumps(before,indent=2),encoding='utf-8')
    index=[]
    for sid,fn in [('S05',s05),('S09',s09)]:
        src=next(s for s in board['scenes'] if s['scene_id']==sid)
        folder=OUT/sid;(folder/'assets').mkdir(parents=True);(folder/'renders').mkdir()
        for file,name in [(ROOT/'assets/fonts/segoe-ui-black.ttf','display.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js'),(ROOT/f'pilots/{sid}/assets/voice.wav','voice.wav')]:shutil.copy2(file,folder/'assets'/name)
        if sid=='S05':shutil.copy2(ROOT/'assets/valletta.jpg',folder/'assets/valletta.jpg')
        with wave.open(str(folder/'assets/voice.wav'),'rb') as w:duration=w.getnframes()/w.getframerate()
        assert abs(duration-src['duration'])<1e-9
        art,js,title,bg,size,left,top,width,proof=fn()
        # Character references make transport encoding unambiguous for the compositor.
        title=title.encode('ascii','xmlcharrefreplace').decode()
        comp='selected-'+sid.lower()
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280">{art}</svg>'
        initial='<h1 id="r09-initial-title">M&#7896;T N&#416;I</h1>' if sid=='S09' else ''
        html=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{sid} revised pilot</title><script src="assets/gsap.min.js"></script><style>
        @font-face{{font-family:Display;src:url('assets/display.ttf');font-weight:900;font-display:block}}
        html,body{{width:100%;height:100%;margin:0;overflow:hidden}}
        #{comp}{{position:relative;width:100%;height:100%;background:{bg}}}
        svg{{position:absolute;inset:0;width:720px;height:1280px;overflow:hidden}}
        h1{{position:absolute;left:{left}px;top:{top}px;width:{width}px;text-align:center;margin:0;color:#0870AC;font-family:Display,sans-serif;font-size:{size}px;font-weight:900;line-height:1.3}}
        </style></head><body><div id="{comp}" data-composition-id="{comp}" data-width="720" data-height="1280" data-duration="{duration:.12f}" data-fps="30">{svg}{initial}<h1 id="{'r05' if sid=='S05' else 'r09'}-title">{title}</h1><audio id="{comp}-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="2"></audio></div><script>(()=>{{const tl=gsap.timeline({{paused:true}});{js}window.__timelines['{comp}']=tl;}})();</script></body></html>'''
        (folder/'index.html').write_text(html,encoding='utf-8')
        (folder/'assets/layered-art.svg').write_text(svg,encoding='utf-8')
        (folder/'hyperframes.json').write_text(json.dumps({'authoringSkill':'general-video','media':{'autoProxy':False}}),encoding='utf-8')
        (folder/'package.json').write_text(json.dumps({'private':True,'scripts':{'check':'npx hyperframes@0.8.170 check','preview':'npx hyperframes@0.8.170 preview','render':'npx hyperframes@0.8.170 render --fps 30 --quality delivery --workers 2 --output renders/pilot.mp4'}},indent=2),encoding='utf-8')
        rec={'scene_id':sid,'revision':'approved-frames-motion-r1','based_on_approved_frame':'S05-v3' if sid=='S05' else 'S09-v2','duration':duration,'source_start_sample':src['start_sample'],'source_end_sample':src['end_sample'],'proof_times':proof,'motion_approval':'pending_user_review','final_frame_approval':'previously_approved','timing_evidence':'Original whisper_raw word times used as approximate cue evidence, not independent perceptual listening. S05 bất động sản at 22.50s global ~=4.349s local. S09 nhiều thị trường at 42.24s global ~=2.440s local.','signature':'Photo opens, hand contacts tab, joined facade hinges up; enclosed green balcony opens on bất động sản.' if sid=='S05' else 'Mechanical selector rotates; six differentiated asset tokens travel authored curved channels from tray to three markets; buildings develop at arrival; no profit or guarantee symbols.'}
        (folder/'DIRECTION.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8');index.append(rec)
        print(f'{sid}: {duration:.9f}s source prepared')
    (OUT/'revision.json').write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'README.md').write_text('# Revised pilots · approved frames motion r1\n\nNew motion source from S05 approved final frame v3 and S09 approved final frame v2. The static designs are approved; the rendered motion remains pending user review. Original pilots / approved stills / raw audio untouched. No full film production.\n\nRead each DIRECTION.json for word-cue provenance and proof times. One local paused GSAP timeline, exact original PCM source range, 720×1280 / 30fps. Static signatures are custom semantic props; previous catalog paper-collage primitives do not implement these mechanical interactions.\n',encoding='utf-8')

if __name__=='__main__':main()
