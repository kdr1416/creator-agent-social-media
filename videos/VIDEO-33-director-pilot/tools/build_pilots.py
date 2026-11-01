"""Rebuild the three editable HyperFrames pilots from authored vector layers.

This utility produces only S01/S05/S09, never the remaining film scenes.
"""
from pathlib import Path
import json, shutil, wave, re, hashlib
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
BOARD=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'))
INK='#30313B'

def mascot(sid,x,y,scale=1.15):
    source=(ROOT/'assets/approved-student-source.js').read_text(encoding='utf-8-sig')
    obj=json.loads(source.split('=',1)[1].strip().rstrip(';').replace('{markup:', '{"markup":',1))
    rig=obj['markup']
    rig=rig.replace('id="c12-',f'id="{sid}-')
    # Give independently animated limb/eye sublayers stable IDs.
    rig=rig.replace(f'<g id="{sid}-arm-far" >',f'<g id="{sid}-arm-far" >')
    rig=rig.replace('<path d="M0 0Q-27-8-43-31"',f'<path id="{sid}-far-path" d="M0 0Q-27-8-43-31"')
    rig=rig.replace('<circle cx="-43" cy="-31"',f'<circle id="{sid}-far-hand" cx="-43" cy="-31"')
    rig=rig.replace('<path d="M0 0Q20 24 38 7"',f'<path id="{sid}-near-path" d="M0 0Q20 24 38 7"')
    rig=rig.replace('<circle cx="38" cy="7"',f'<circle id="{sid}-near-hand" cx="38" cy="7"')
    return f'<g transform="translate({x} {y}) scale({scale})"><g id="{sid}-actor">{rig}</g></g>'

def house(prefix,x,y,s=1,fill='#FFD59B'):
    return f'''<g transform="translate({x} {y}) scale({s})"><g id="{prefix}">
    <path d="M6 105L86 57L176 105V212H6Z" fill="{fill}" stroke="{INK}" stroke-width="3.4" stroke-linejoin="round"/>
    <path d="M-13 107L85 30L195 107L176 122L86 61L5 122Z" fill="#D48DA2" stroke="{INK}" stroke-width="3.4" stroke-linejoin="round"/>
    <path d="M122 60V25H147V79" fill="#E2B6B1" stroke="{INK}" stroke-width="3"/>
    <path d="M73 212V149Q93 132 111 149V212" fill="#087BC1" stroke="{INK}" stroke-width="3"/>
    <path d="M25 132H54V169H25ZM133 132H162V169H133Z" fill="#FFFBEA" stroke="{INK}" stroke-width="2.6"/>
    <path d="M39 133V168M26 150H53M147 133V168M134 150H161" stroke="#C69F8B" stroke-width="2"/>
    <circle cx="101" cy="174" r="3.2" fill="#FFCD71"/>
    <path d="M17 202H63M121 202H164" stroke="#E2AE7C" stroke-width="3" stroke-linecap="round"/>
    </g></g>'''

def person(x,y,s=1,color='#91C9C9'):
    return f'''<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-44" r="16" fill="#FFD5AA" stroke="{INK}" stroke-width="2.3"/><path d="M-23 9V-10Q-22-27 0-27Q22-27 23-10V9Z" fill="{color}" stroke="{INK}" stroke-width="2.3"/><path d="M-7 9V27M8 9V27" stroke="{INK}" stroke-width="3" stroke-linecap="round"/><circle cx="-5" cy="-45" r="1.5" fill="{INK}"/><circle cx="5" cy="-45" r="1.5" fill="{INK}"/><path d="M-5-36Q0-32 5-36" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"/></g>'''

def svg_start(sid):
    return f'''<svg id="{sid}-art" class="art" xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280" aria-label="Editable layered illustration">
    <defs><filter id="{sid}-shadow" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="9" stdDeviation="7" flood-color="#796572" flood-opacity=".13"/></filter></defs>'''

def s01():
    sid='p01'
    art=svg_start(sid)+f'''
    <ellipse cx="346" cy="1003" rx="273" ry="25" fill="#E6D4C2" opacity=".6"/>
    <g id="p01-book" filter="url(#p01-shadow)">
      <path d="M72 780L323 730L603 774L585 921L330 971L73 916Z" fill="#087BC1" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>
      <path d="M85 787L325 744L586 783L570 900L329 950L88 897Z" fill="#E8D8BE" stroke="{INK}" stroke-width="2.7"/>
      <path d="M89 799L324 759L578 797M90 812L326 773L577 810M90 826L326 788L575 824M90 841L327 804L574 837M90 855L327 818L572 851M90 870L329 835L571 866" fill="none" stroke="#BDB5A9" stroke-width="1.8"/>
      <path d="M91 776L325 729L328 893L94 914Z" fill="#FFFEF2" stroke="{INK}" stroke-width="2.8"/>
      <g id="p01-opening-page"><path d="M326 729L587 772L576 916L328 893Z" fill="#FFFDF1" stroke="{INK}" stroke-width="2.8"/><path d="M354 774L542 803M354 791L509 814M354 846L543 869" stroke="#DBD2C3" stroke-width="3" stroke-linecap="round"/><path d="M570 878L576 916L537 910Z" fill="#E8DEC7" stroke="#BFB29E" stroke-width="1.5"/></g>
      <path d="M325 730L328 893" stroke="#C5B096" stroke-width="5"/>
      <path d="M115 792L274 761M115 808L240 783M114 868L281 852M114 884L249 870" stroke="#DBD2C3" stroke-width="3" stroke-linecap="round"/>
      <g id="p01-fold"><path d="M143 786L227 676L332 722L427 654L531 796L330 856Z" fill="#F1E0BA" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/><path d="M143 786L332 722L531 796L330 856Z" fill="#FFF7DB" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/><path d="M227 676L332 722L427 654" fill="none" stroke="#D4B98B" stroke-width="3"/><path d="M330 722V855" stroke="#D4B98B" stroke-width="2.4"/></g>
    </g>
    <g id="p01-base"><path d="M170 652L348 612L496 649L321 701Z" fill="#88C6D7" stroke="{INK}" stroke-width="3.2"/><path d="M170 652V666L321 716L496 663V649L321 701Z" fill="#087BC1" stroke="{INK}" stroke-width="3.2"/></g>
    {house('p01-house',208,383,1.25)}
    <g id="p01-family" filter="url(#p01-shadow)">{person(253,652,.58,'#90C9D3')}{person(306,646,.72,'#B89BD7')}{person(366,644,.73,'#EEA7A4')}</g>
    {mascot(sid,505,788,1.15)}
    </svg>'''
    text='<div id="p01-title-a" class="feature">HỌC TẬP</div><div id="p01-title-b" class="feature long">ĐIỂM TỰA DÀI LÂU</div>'
    js='''
    tl.fromTo('#p01-title-a',{rotation:-3,y:12,opacity:0},{rotation:-2,y:0,opacity:1,duration:.3,ease:'back.out(1.2)'},.12);
    tl.fromTo('#p01-opening-page',{scaleX:.20,svgOrigin:'326 805'},{scaleX:1,duration:1.35,ease:'power2.inOut'},.25);
    tl.fromTo('#p01-far-path',{attr:{d:'M0 0Q-28 10-42 22'}},{attr:{d:'M0 0Q-22-35-2-64'},duration:.7,ease:'power2.inOut'},.8);
    tl.fromTo('#p01-far-hand',{attr:{cx:-42,cy:22}},{attr:{cx:-2,cy:-64},duration:.7,ease:'power2.inOut'},.8);
    tl.fromTo('#p01-fold',{scaleY:.04,y:94,opacity:0,svgOrigin:'330 855'},{scaleY:1,y:0,opacity:1,duration:1.12,ease:'power2.inOut'},2.68);
    tl.fromTo('#p01-base',{y:132,opacity:0},{y:0,opacity:1,duration:1.12,ease:'power2.inOut'},2.68);
    tl.fromTo('#p01-house',{scaleY:.02,svgOrigin:'90 212',opacity:0},{scaleY:1,opacity:1,duration:.85,ease:'back.out(1.05)'},3.02);
    tl.fromTo('#p01-family',{y:12,opacity:0},{y:0,opacity:1,duration:.35,ease:'power2.out'},3.88);
    tl.to('#p01-title-a',{opacity:0,y:-8,duration:.2},3.7);
    tl.fromTo('#p01-title-b',{rotation:-2,y:12,opacity:0},{rotation:-1,y:0,opacity:1,duration:.3,ease:'back.out(1.1)'},3.96);
    tl.to('#p01-eyes',{y:-8,x:-1,duration:.32},3.88);
    tl.to('#p01-near-path',{attr:{d:'M0 0Q30-5 37-29'},duration:.35},4.17);
    tl.to('#p01-near-hand',{attr:{cx:37,cy:-29},duration:.35},4.17);
    '''
    return art,text,js,'#FFF8E9'

def s05():
    sid='p05'
    art=svg_start(sid)+f'''
    <defs><clipPath id="p05-photo-clip"><path d="M104 361L145 356L181 362L224 353L268 359L313 351L358 360L406 352L455 359L497 352L542 359L609 354L616 693L569 699L523 694L479 704L435 698L386 706L343 699L301 707L258 700L214 706L172 701L109 707Z"/></clipPath></defs>
    <ellipse cx="348" cy="1017" rx="277" ry="24" fill="#E7D6C5" opacity=".58"/>
    <g id="p05-map" filter="url(#p05-shadow)">
      <path d="M78 330L352 315L638 336L631 780L350 812L80 779Z" fill="#FFFDF4" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
      <path d="M91 345L351 332L623 351L618 766L350 792L95 766Z" fill="#ECE3D3"/>
      <image id="p05-photo" href="assets/valletta.jpg" x="104" y="325" width="516" height="395" preserveAspectRatio="xMidYMid slice" clip-path="url(#p05-photo-clip)"/>
      <path d="M109 719L329 721M379 719L610 715" stroke="#D8CDBB" stroke-width="2.5"/>
      <path d="M330 340L334 774" stroke="#DFD3BC" stroke-width="2"/>
      <g id="p05-left-fold"><path d="M79 330L351 315L347 811L80 779Z" fill="#F4E8CC" stroke="{INK}" stroke-width="2.7"/><path d="M110 415Q211 392 299 424M118 462Q201 444 298 459M117 653Q213 624 295 654" fill="none" stroke="#CEC3AA" stroke-width="3"/><path d="M140 380V725M262 371V735" stroke="#E2D6BF" stroke-width="2"/></g>
      <g id="p05-right-fold"><path d="M351 315L638 336L631 780L347 811Z" fill="#FFF4DA" stroke="{INK}" stroke-width="2.7"/><path d="M389 412L575 421M387 440L540 446M389 661L583 657M384 688L539 683" stroke="#D7C7A8" stroke-width="3" stroke-linecap="round"/><path d="M600 726L631 780L569 785Z" fill="#DBC9A8" stroke="#BAAA8D" stroke-width="2"/><path d="M351 321V807" stroke="#D7C3A1" stroke-width="6"/></g>
    </g>
    <g id="p05-pedestal"><ellipse cx="324" cy="930" rx="129" ry="22" fill="#CDE6DD" stroke="{INK}" stroke-width="2.7"/><path d="M195 922V942Q321 988 453 940V923Q321 963 195 922Z" fill="#A4CFBF" stroke="{INK}" stroke-width="2.7"/></g>
    {house('p05-new-house',244,715,.9,'#FFD6A5')}
    <g id="p05-keepsake"><path d="M74 970L125 900L181 964L175 1005L82 1005Z" fill="#E7DDF4" stroke="#8E849A" stroke-width="2.5"/><path d="M73 970L125 920L177 969" fill="none" stroke="#8E849A" stroke-width="2.5"/><path d="M117 1005V975H138V1005" fill="#ADCED8" stroke="#8E849A" stroke-width="2"/></g>
    {mascot(sid,477,790,1.12)}
    </svg>'''
    text='<div id="p05-title" class="place">MALTA</div>'
    js='''
    tl.fromTo('#p05-far-path',{attr:{d:'M0 0Q-30 14-42 23'}},{attr:{d:'M0 0Q-79-14-141-53'},duration:.65,ease:'power2.inOut'},.35);
    tl.fromTo('#p05-far-hand',{attr:{cx:-42,cy:23}},{attr:{cx:-141,cy:-53},duration:.65,ease:'power2.inOut'},.35);
    tl.fromTo('#p05-left-fold',{scaleX:1,svgOrigin:'79 550'},{scaleX:.015,duration:1.65,ease:'power2.inOut'},1.15);
    tl.fromTo('#p05-right-fold',{scaleX:1,svgOrigin:'638 550'},{scaleX:.015,duration:1.65,ease:'power2.inOut'},1.15);
    tl.to('#p05-left-fold,#p05-right-fold',{opacity:0,duration:.15},2.7);
    tl.to('#p05-far-path',{attr:{d:'M0 0Q60-15 115-53'},duration:1.65,ease:'power2.inOut'},1.15);
    tl.to('#p05-far-hand',{attr:{cx:115,cy:-53},duration:1.65,ease:'power2.inOut'},1.15);
    tl.to('#p05-far-path',{attr:{d:'M0 0Q65-45 112-80'},duration:.3,ease:'power2.inOut'},2.85);
    tl.to('#p05-far-hand',{attr:{cx:112,cy:-80},duration:.3,ease:'power2.inOut'},2.85);
    tl.fromTo('#p05-pedestal',{opacity:0,scaleY:.1,svgOrigin:'324 944'},{opacity:1,scaleY:1,duration:.5,ease:'power2.out'},3.05);
    tl.fromTo('#p05-new-house',{scaleY:.015,svgOrigin:'90 212',opacity:0},{scaleY:1,opacity:1,duration:.78,ease:'back.out(1.05)'},3.12);
    tl.fromTo('#p05-title',{y:12,opacity:0,rotation:-2},{y:0,opacity:1,rotation:0,duration:.28,ease:'back.out(1.1)'},4.05);
    tl.to('#p05-eyes',{x:-3,y:-7,duration:.3},4.08);
    tl.to('#p05-near-path',{attr:{d:'M0 0Q29 10 37-18'},duration:.32},4.35);
    tl.to('#p05-near-hand',{attr:{cx:37,cy:-18},duration:.32},4.35);
    '''
    return art,text,js,'#FFF0E5'

def platform(name,x,y,color):
    return f'''<g id="{name}"><ellipse cx="{x}" cy="{y+18}" rx="100" ry="23" fill="#D5CBDE" opacity=".45"/><path d="M{x-87} {y-12}V{y+12}Q{x} {y+52} {x+87} {y+12}V{y-12}Z" fill="{color}" stroke="{INK}" stroke-width="3"/><ellipse cx="{x}" cy="{y-12}" rx="87" ry="26" fill="#FFFDF5" stroke="{INK}" stroke-width="3"/><path d="M{x-57} {y+12}Q{x} {y+31} {x+57} {y+12}" fill="none" stroke="#FFFFFF" opacity=".55" stroke-width="2"/></g>'''

def token(name,x,y):
    return f'''<g transform="translate({x} {y})"><g id="{name}"><ellipse cx="6" cy="8" rx="39" ry="44" fill="#E9B45D" stroke="{INK}" stroke-width="3"/><ellipse cx="0" cy="0" rx="39" ry="44" fill="#FFCE75" stroke="{INK}" stroke-width="3"/><ellipse cx="0" cy="0" rx="29" ry="34" fill="#FFDB99" stroke="#D5A55C" stroke-width="2"/><path d="M-16 5L0-13L16 5L0 23Z" fill="#FFF6DA" stroke="{INK}" stroke-width="2.6"/><path d="M-21-21Q-15-29-8-30" fill="none" stroke="#FFF4D3" stroke-width="3" stroke-linecap="round"/></g></g>'''

def s09():
    art=svg_start('p09')+f'''
    <g id="p09-tracks"><path id="p09-track-b" d="M214 507C411 467 356 661 521 705" fill="none" stroke="#B8ADCF" stroke-width="20" stroke-linecap="round"/><path d="M214 507C411 467 356 661 521 705" fill="none" stroke="#FFFDF5" stroke-width="12" stroke-linecap="round"/><path id="p09-track-c" d="M167 520C67 637 111 811 223 938" fill="none" stroke="#B8ADCF" stroke-width="20" stroke-linecap="round"/><path d="M167 520C67 637 111 811 223 938" fill="none" stroke="#FFFDF5" stroke-width="12" stroke-linecap="round"/></g>
    {platform('p09-platform-a',185,530,'#BBA3D6')}
    <g id="p09-market-b">{platform('p09-platform-b',521,745,'#85C4D8')}</g>
    <g id="p09-market-c">{platform('p09-platform-c',223,982,'#A9D3BD')}</g>
    {token('p09-token-a',182,474)}
    {token('p09-token-b',187,383)}
    {token('p09-token-c',190,298)}
    <g id="p09-risks" fill="none" stroke="#B47849" stroke-width="3.4" stroke-linecap="round"><path id="p09-wiggle-a" d="M270 464Q286 454 297 464Q307 475 319 464"/><path id="p09-wiggle-b" d="M551 654Q567 644 579 654Q590 665 603 654"/><path id="p09-wiggle-c" d="M276 908Q290 898 301 908Q315 921 328 908"/></g>
    </svg>'''
    text='<div id="p09-title-a" class="allocation">MỘT NƠI</div><div id="p09-title-b" class="allocation long">NHIỀU THỊ TRƯỜNG</div>'
    js='''
    tl.fromTo('#p09-title-a',{opacity:0,y:8},{opacity:1,y:0,duration:.3},.1);
    tl.fromTo('#p09-market-b,#p09-market-c',{opacity:.25},{opacity:1,duration:.5},1.25);
    tl.fromTo('#p09-tracks',{opacity:0},{opacity:1,duration:.4},1.25);
    // Release the TOP token first. Removing the middle token first leaves a floating stack.
    tl.to('#p09-token-c',{x:27,y:205,rotation:22,svgOrigin:'0 0',duration:.5,ease:'power2.in'},2.2);
    tl.to('#p09-token-c',{x:147,y:255,rotation:38,duration:.4,ease:'none'},2.7);
    tl.to('#p09-token-c',{x:227,y:318,rotation:25,duration:.4,ease:'none'},3.1);
    tl.to('#p09-token-c',{x:331,y:391,rotation:0,duration:.6,ease:'power2.out'},3.5);
    tl.to('#p09-token-b',{x:-32,y:135,rotation:-22,svgOrigin:'0 0',duration:.5,ease:'power2.in'},3.35);
    tl.to('#p09-token-b',{x:-87,y:265,rotation:-35,duration:.5,ease:'none'},3.85);
    tl.to('#p09-token-b',{x:-72,y:415,rotation:-20,duration:.5,ease:'none'},4.35);
    tl.to('#p09-token-b',{x:36,y:543,rotation:0,duration:.6,ease:'power2.out'},4.85);
    tl.to('#p09-title-a',{opacity:0,y:-8,duration:.2},2.6);
    tl.fromTo('#p09-title-b',{opacity:0,y:8},{opacity:1,y:0,duration:.3,ease:'power2.out'},4.95);
    tl.fromTo('#p09-risks',{opacity:0},{opacity:1,duration:.25},5.52);
    tl.to('#p09-wiggle-a',{x:4,y:2,duration:.16,yoyo:true,repeat:3,ease:'sine.inOut'},5.6);
    tl.to('#p09-wiggle-b',{x:-4,y:2,duration:.17,yoyo:true,repeat:3,ease:'sine.inOut'},5.82);
    tl.to('#p09-wiggle-c',{x:3,y:-2,duration:.15,yoyo:true,repeat:3,ease:'sine.inOut'},6.02);
    '''
    return art,text,js,'#F0EAFB'

CSS='''
@font-face{font-family:PilotDisplay;src:url('assets/segoe-ui-black.ttf');font-weight:900;font-display:block}
@font-face{font-family:PilotSans;src:url('assets/arial.ttf');font-display:block}
*{box-sizing:border-box}html,body{width:100%;height:100%;margin:0;overflow:hidden}
.composition{position:relative;width:100%;height:100%;overflow:hidden;color:#30313B;font-family:PilotDisplay,sans-serif}
.ground{position:absolute;inset:0}.art{position:absolute;inset:0;width:720px;height:1280px;overflow:hidden}
.feature,.place,.allocation{position:absolute;z-index:5;white-space:nowrap;font-weight:900;line-height:1.24;text-align:center}
.feature{top:172px;left:155px;width:410px;padding:17px 20px;background:#087BC1;color:#FFFDF4;font-size:54px;box-shadow:5px 7px 0 #30313b12}
.feature.long{left:62px;width:596px;font-size:46px;top:173px;padding:18px 12px}
.place{font-size:76px;left:90px;top:164px;width:540px;color:#0870AC;letter-spacing:1px}
.allocation{top:168px;left:82px;width:556px;font-size:55px;color:#30313B}
.allocation.long{font-size:44px;top:170px}
'''

def main():
    for sid,fn in [('S01',s01),('S05',s05),('S09',s09)]:
        scene=next(s for s in BOARD['scenes'] if s['scene_id']==sid)
        folder=ROOT/'pilots'/sid; (folder/'assets').mkdir(parents=True,exist_ok=True)
        for name in ['segoe-ui-black.ttf','arial.ttf']:
            shutil.copy2(ROOT/'assets/fonts'/name,folder/'assets'/name)
        shutil.copy2(ROOT/'assets/runtime/gsap.min.js',folder/'assets/gsap.min.js')
        if sid=='S05':shutil.copy2(ROOT/'assets/valletta.jpg',folder/'assets/valletta.jpg')
        parts=[]
        for i in scene['source_segments']:
            with wave.open(str(ROOT/f'inputs/audio/seg_{i:02d}.wav'),'rb') as w: parts.append(w.readframes(w.getnframes()))
        with wave.open(str(folder/'assets/voice.wav'),'wb') as w:
            w.setnchannels(1);w.setsampwidth(2);w.setframerate(24000);w.writeframes(b''.join(parts))
        art,text,js,bg=fn(); comp='v33-'+sid.lower(); duration=scene['duration']
        html=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{sid} · {scene['title']}</title><script src="assets/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="{comp}" class="composition" data-composition-id="{comp}" data-width="720" data-height="1280" data-start="0" data-duration="{duration:.12f}" data-fps="30">
<div class="ground" style="background:{bg}"></div>{art}{text}
<audio id="{comp}-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="2"></audio>
</div><script>(()=>{{const tl=gsap.timeline({{paused:true}});{js}
tl.to({{hold:0}},{{hold:1,duration:{duration:.12f},ease:'none'}},0);
window.__timelines['{comp}']=tl;}})();</script></body></html>'''
        (folder/'index.html').write_text(html,encoding='utf-8')
        (folder/'assets/layered-art.svg').write_text(art,encoding='utf-8')
        (folder/'hyperframes.json').write_text(json.dumps({'$schema':'https://hyperframes.heygen.com/schema/hyperframes.json','registry':'https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry','paths':{'blocks':'compositions','components':'compositions/components','assets':'assets'},'authoringSkill':'general-video','media':{'autoProxy':False}},indent=2),encoding='utf-8')
        (folder/'package.json').write_text(json.dumps({'name':'video33-'+sid.lower(),'private':True,'scripts':{'check':'npx hyperframes@0.8.170 check','preview':'npx hyperframes@0.8.170 preview','render':'npx hyperframes@0.8.170 render --fps 30 --quality delivery --output renders/pilot.mp4'}},indent=2),encoding='utf-8')
        (folder/'frame.md').write_text(f'# {sid} frame contract\n\n720×1280, 30fps, voice {duration:.12f}s.\n\n{scene["composition"]}\n\nNguồn raw/corrected/sample bounds: ../../scenes/{sid}/packet.json. Hình/vector layer chỉnh trực tiếp trong index.html hoặc layered-art.svg rồi đồng bộ source. Runtime là một paused GSAP timeline, key trùng root id. Không sửa voice để khớp hình.\n',encoding='utf-8')
        print(f'{sid}: {duration:.9f}s; source HTML, SVG and original PCM ready')
    (ROOT/'CREDITS.md').write_text('# Credits\n\n“Skyline of Valletta.jpg” — Juliana da Costa José, https://commons.wikimedia.org/wiki/File:Skyline_of_Valletta.jpg . CC BY-SA 3.0, https://creativecommons.org/licenses/by-sa/3.0/ . The photo is cropped/reframed in a paper collage, not a property listing. Preserve attribution and applicable share-alike terms when distributing adaptations.\n\nMascot identity and local Segoe UI Black / Arial files copied from user-provided approved reference package. Font files are included for this handoff; redistribution subject to their original license. GSAP runtime copied locally from the supplied reference; preserve vendor license header. New prop vectors and directing/source code authored for VIDEO-33.\n',encoding='utf-8')

if __name__=='__main__':main()
