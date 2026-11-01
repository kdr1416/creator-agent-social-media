"""Next review round: static action poses for S06 and S11, preserving all builds."""
from pathlib import Path
import ast, re, json, shutil, sys, xml.etree.ElementTree as ET
from build_pilots import mascot

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'revisions/S06-S11-design-r1'
if OUT.exists():raise SystemExit('Refusing to overwrite existing design round')
OUT.mkdir(parents=True)
INK='#30313B'
source=ROOT/'tools/design_s07_s08_frames.py'
tree=ast.parse(source.read_text(encoding='utf-8'))
kit={'INK':INK,'mascot':mascot,'re':re}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),str(source),'exec'),kit)
arm,face,title=kit['arm_rig'],kit['face'],kit['title']
ET.register_namespace('','http://www.w3.org/2000/svg');NS='{http://www.w3.org/2000/svg}'

def svg(body,bg):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280" style="width:100%;height:100%"><rect width="720" height="1280" fill="{bg}"/>{body}</svg>'

def chair(id,x,y):
    return f'''<g id="{id}" transform="translate({x} {y})" stroke="{INK}" stroke-width="3" stroke-linejoin="round">
    <rect x="0" y="0" width="100" height="168" rx="22" fill="#C6B6DF"/><rect x="12" y="15" width="76" height="118" rx="15" fill="#DED2ED" stroke="none"/>
    <path d="M-10 161H113L127 180H-15Z" fill="#B99ED3"/><path d="M-15 180H127V194H-15Z" fill="#AA8DC7"/>
    <path d="M-1 194L-6 262M113 194L119 262" stroke="#8A73AF" stroke-width="10" stroke-linecap="round"/>
    </g>'''

def dad(x,y):
    return f'''<g id="father" transform="translate({x} {y})" stroke="{INK}" stroke-width="3" stroke-linejoin="round">
    <path d="M-66 194L-60 363L-25 363L-10 230L7 363H45L58 194Z" fill="#B9C8D9"/>
    <path d="M-62 359H-24V378H-85Q-87 367-62 359ZM7 359H45L69 374Q71 382 8 379Z" fill="#647C97"/>
    <path d="M-37 75Q-101 76-111 136L-105 224H109L107 137Q100 79 38 75Z" fill="#E8B9A9"/>
    <path d="M-26 74V98L0 114L29 97V72" fill="#FFD7B5"/><path d="M-37 78L0 114L-25 140L-49 86M39 78L0 114L27 140L51 86" fill="#F7D7C7"/>
    <path d="M0 114V224M-86 154L-85 220M85 154L87 220" stroke="#C99A8B" fill="none"/>
    <path d="M-55-32Q-49-75 3-72Q55-69 57-23L53 28Q45 74 0 76Q-48 72-54 30Z" fill="#FFD7B5"/>
    <path d="M-56-17Q-72-61-41-75Q-3-96 23-76Q64-72 62-28L47-14L42-49Q5-32-22-53Q-31-20-56-17Z" fill="#67527C"/>
    <ellipse cx="-23" cy="11" rx="4" ry="6" fill="{INK}" stroke="none"/><ellipse cx="23" cy="11" rx="4" ry="6" fill="{INK}" stroke="none"/>
    <path d="M-12 41Q0 53 14 40" fill="none" stroke-width="3" stroke-linecap="round"/>
    <ellipse cx="-39" cy="31" rx="10" ry="6" fill="#EF9B8F" stroke="none"/><ellipse cx="40" cy="31" rx="10" ry="6" fill="#EF9B8F" stroke="none"/>
    </g>'''

def s06(phase):
    c=title('CẢ GIA ĐÌNH',size=56)
    c+='''<path d="M42 1043H677" stroke="#D5C9E0" stroke-width="3"/><ellipse cx="366" cy="1008" rx="274" ry="38" fill="#E1D6EB"/>
    <g id="room-window"><rect x="266" y="314" width="188" height="168" rx="36" fill="#FAF5FF" stroke="#DBCEE7" stroke-width="3"/><path d="M360 316V480M268 397H452" stroke="#DBCEE7" stroke-width="3"/></g>'''
    c+=chair('mother-chair',181,640)+chair('father-chair',401,640)
    # Seated figures continue below the tabletop; their bodies share the chairs.
    c+='''<g id="mother-legs" stroke="#30313B" stroke-width="3"><path d="M199 737L205 946H230L239 790L249 946H275L281 737Z" fill="#C7A4C9"/><path d="M205 945H231V960H188Q187 953 205 945ZM249 945H275L288 957H250Z" fill="#8A73AF"/></g>'''
    c+=face(235,565,.85,False)
    c+='<g transform="translate(455 565) scale(.85)">'+dad(0,0)+'</g>'
    c+='''<g id="family-table" stroke="#30313B" stroke-width="3.2" stroke-linejoin="round">
    <path d="M168 841L156 1006H174L191 841M548 841L565 1006H584L571 841" fill="#D6B79C"/>
    <ellipse cx="362" cy="835" rx="252" ry="89" fill="#DFC4A8"/>
    <ellipse cx="362" cy="815" rx="252" ry="89" fill="#FFFDF3"/>
    <path d="M125 810Q143 746 311 735" fill="none" stroke="#F1E5D4" stroke-width="5"/>
    <g id="shared-plan"><path d="M287 774L441 774L457 824L275 824Z" fill="#EDF4F1"/><path d="M314 789H414M301 805H430" fill="none" stroke="#9EC4BA" stroke-width="3"/><path d="M336 816H401" stroke="#087BC1" stroke-width="4"/></g>
    </g>'''
    dx,dy=(0,0) if phase=='ready' else (-35,20)
    c+=chair('invited-chair',188+dx,778+dy)
    if phase in ['ready','pull']:
        x=32 if phase=='ready' else 20;y=810;s=1.05
        grip=(198+dx,864+dy);near=((grip[0]-x)/s-109,(grip[1]-y)/s-83)
        c+=arm('family',x,y,s,(-14,30),near)
    else:
        c+=arm('family',140,798,1.12,(-20,30),(33.86,-67.82),seated=True)
    return svg(c,'#F0EAF8')

def parent_offer(hand):
    art=kit['parent'](195,570,1.3,False)
    # Repose the near arm from a shoulder fixed at local (49,108).
    x,y=hand;lx=(x-195)/1.3;ly=(y-570)/1.3
    art=re.sub(r'M49 108Q84 124 88 91L91 118',f'M49 108Q{(49+lx)*.5:.3f} {(108+ly)*.5:.3f} {lx:.3f} {ly:.3f}',art)
    art=art.replace('cx="91" cy="118"',f'cx="{lx:.3f}" cy="{ly:.3f}"')
    return art

def notebook(x,y):
    return f'''<g id="notebook" transform="translate({x} {y})" stroke="{INK}" stroke-width="3" stroke-linejoin="round"><rect width="80" height="100" rx="7" fill="#A990D5"/><path d="M11 4V96" stroke="#E2D9F0" stroke-width="5"/><rect x="25" y="20" width="39" height="22" rx="3" fill="#EDE5F5" stroke="none"/><path d="M78 7H83V96H78" fill="#FFFDF3"/></g>'''

def s11(phase):
    c=title('CHUẨN BỊ CHO CON',size=49)
    c+='<path d="M42 1035H680" stroke="#E0C9BC" stroke-width="3"/><ellipse cx="377" cy="1029" rx="274" ry="17" fill="#EEDCD0"/>'
    c+=parent_offer((330,730) if phase!='packed' else (310,805))
    farhand={'offer':(398,790),'receive':(410,730),'packed':(435,840)}[phase]
    nearhand=(610,900)
    def local(point,shoulder):return ((point[0]-390)/1.55-shoulder[0],(point[1]-725)/1.55-shoulder[1])
    student=arm('prepare',390,725,1.55,local(farhand,(25,72)),local(nearhand,(109,83)))
    # The same blue backpack is on the table, rather than duplicated on his back.
    rr=ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg">'+student+'</svg>')
    for par in rr.iter():
        for node in list(par):
            if (node.tag==NS+'rect' and node.get('x')=='103' and node.get('y')=='50') or node.get('d','').startswith(('M113 69','M111 48')):par.remove(node)
    student=''.join(ET.tostring(n,encoding='unicode') for n in rr)
    c+=student
    c+='''<g id="preparation-table" stroke="#30313B" stroke-width="3.2" stroke-linejoin="round"><path d="M81 923H650L679 946H55Z" fill="#F0D4AF"/><path d="M55 946H679V965H55Z" fill="#DEB78E"/><path d="M85 965V1031M648 965V1031" stroke="#AA8A74" stroke-width="10"/></g>
    <g id="house-key" transform="translate(126 906)" stroke="#30313B" stroke-width="3"><ellipse cx="0" cy="0" rx="15" ry="12" fill="#FFD18B"/><path d="M14 0H59M42 0V9M53 0V7" stroke-width="5" stroke-linecap="round"/></g>
    <g id="backpack-rear" stroke="#30313B" stroke-width="3.2"><path d="M329 813V796Q332 750 390 754Q449 752 450 796V813Z" fill="#7ABED3"/><path d="M367 759V744Q391 731 414 744V758" fill="none" stroke-width="6"/><ellipse cx="390" cy="812" rx="74" ry="28" fill="#3D859F"/><path d="M319 816L312 880M460 816L469 880" stroke="#087BC1" stroke-width="14" stroke-linecap="round"/></g>'''
    c+=notebook(330,790 if phase=='packed' else 680)
    # Foreground pocket occludes the lower part of the inserted book.
    c+='''<g id="backpack-front" stroke="#30313B" stroke-width="3.2" stroke-linejoin="round"><path d="M316 839Q390 869 464 839L460 917Q460 938 438 938H341Q319 936 319 917Z" fill="#087BC1"/><path d="M337 882Q390 867 443 882V919H338Z" fill="#54A7C6"/><path d="M345 886H432" stroke="#C0E3EC" stroke-width="3"/><circle cx="431" cy="891" r="3" fill="#FFE0A0"/></g>'''
    # Visible palms establish ownership/contact rather than a floating notebook.
    if phase!='packed':
        c+='<circle cx="330" cy="730" r="11" fill="#FFD7B5" stroke="#30313B" stroke-width="3"/>'
        if phase=='receive':c+='<circle cx="410" cy="730" r="10" fill="#FFAC3C" stroke="#30313B" stroke-width="3"/>'
    c+='<circle cx="610" cy="900" r="10" fill="#FFAC3C" stroke="#30313B" stroke-width="3"/>'
    return svg(c,'#FFF0E5')

items=[('S06/01-ready','Có một chỗ còn trống',s06('ready')),('S06/02-pull','Mascot kéo ghế',s06('pull')),('S06/03-together','Cùng quanh bàn',s06('together')),('S11/01-offer','Phụ huynh đưa vở',s11('offer')),('S11/02-receive','Mascot nhận vở',s11('receive')),('S11/03-packed','Vở đã vào ba lô',s11('packed'))]
ledger=[]
for rel,label,art in items:
    f=OUT/rel;assets=f/'assets';assets.mkdir(parents=True)
    for a,b in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(a,assets/b)
    (f/'layered-art.svg').write_text(art,encoding='utf-8')
    (f/'index.html').write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{margin:0;width:100%;height:100%;overflow:hidden}}#root{{width:100%;height:100%}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="1" data-fps="30">{art}</div><script>const tl=gsap.timeline({{paused:true}});tl.to({{v:0}},{{v:1,duration:1}},0);window.__timelines['root']=tl;</script></body></html>''',encoding='utf-8')
    ledger.append({'path':rel,'label':label,'status':'proposal_pending_user_frame_approval'})
(OUT/'frame_inventory.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
