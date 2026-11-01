"""Author static review frames for S10 and S12 without changing any video."""
from pathlib import Path
import ast, re, json, shutil, xml.etree.ElementTree as ET
from build_pilots import mascot

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'revisions/S10-S12-design-r1'
if OUT.exists():raise SystemExit('Refusing to overwrite review round')
OUT.mkdir(parents=True)
INK='#30313B'
ns={'INK':INK,'mascot':mascot,'re':re}
for name in ['design_s07_s08_frames.py','design_s06_s11_frames.py']:
    file=ROOT/'tools'/name;tree=ast.parse(file.read_text(encoding='utf-8'))
    exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),str(file),'exec'),ns)
arm,parent,dad,title=ns['arm_rig'],ns['parent'],ns['dad'],ns['title']

def svg(body,bg):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280" style="width:100%;height:100%"><rect width="720" height="1280" fill="{bg}"/>{body}</svg>'

def grandma(x,y,s=.95,linked=True):
    hand=(61,185) if linked else (52,155)
    return f'''<g id="oldest-generation" transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
    <ellipse cx="0" cy="335" rx="61" ry="9" fill="#E4CFC6" opacity=".6" stroke="none"/>
    <path d="M-34 279V324H-9L-6 278M12 278L15 324H39L36 276" fill="#F2C8AE"/><path d="M-35 318H-9V333H-53Q-52 323-35 318ZM16 318H39L55 330Q52 336 16 333Z" fill="#927CA9"/>
    <path d="M-39 85Q-70 96-68 143L-72 280Q0 299 70 280L60 143Q60 94 34 85Z" fill="#D8C4DC"/>
    <path d="M-31 86L-22 119L2 106L27 121L36 86" fill="#FFF2DA"/>
    <path d="M-4 109V279M-53 187Q1 200 54 185" fill="none" stroke="#B59BC3"/>
    <path d="M-42 104Q-66 136-51 175" fill="none" stroke-width="17"/><path d="M-42 104Q-66 136-51 175" fill="none" stroke="#D8C4DC" stroke-width="11"/>
    <path d="M-69 179V163Q-54 148-42 164L-42 330" fill="none" stroke="#9A7D69" stroke-width="7"/>
    <circle cx="-51" cy="175" r="9" fill="#FFD7B5"/>
    <path d="M35 102Q56 132 {hand[0]} {hand[1]}" fill="none" stroke-width="17"/><path d="M35 102Q56 132 {hand[0]} {hand[1]}" fill="none" stroke="#D8C4DC" stroke-width="11"/>
    <circle cx="{hand[0]}" cy="{hand[1]}" r="9" fill="#FFD7B5"/>
    <circle cx="29" cy="-39" r="24" fill="#DADDE4"/>
    <path d="M-47 17Q-61-44-19-58Q18-71 46-38L49 26Z" fill="#DADDE4"/>
    <path d="M-44-8Q-38-45 0-44Q40-44 44-9L40 36Q35 73 0 76Q-39 73-43 36Z" fill="#FFD7B5"/>
    <path d="M-44 0Q-30-4-20-28Q13-7 44-9L43-31Q10-61-21-42Q-49-31-44 0Z" fill="#DADDE4"/>
    <g id="grandparent-glasses" fill="none" stroke="#796A91" stroke-width="2.7"><ellipse cx="-21" cy="20" rx="17" ry="13"/><ellipse cx="20" cy="20" rx="17" ry="13"/><path d="M-4 18H3"/></g>
    <circle cx="-20" cy="20" r="2.5" fill="{INK}" stroke="none"/><circle cx="20" cy="20" r="2.5" fill="{INK}" stroke="none"/>
    <path d="M-12 49Q0 60 13 49M-37 38L-30 40M29 40L36 38" fill="none" stroke-width="2.5"/>
    </g>'''

def mother(x=420,y=600,s=1.2,linked=True):
    art=parent(x,y,s,False)
    if linked:
        art=art.replace('M49 108Q84 124 88 91L91 118','M49 108Q86 123 78 156').replace('cx="91" cy="118"','cx="78" cy="156"')
    return art

def older_parent(x=255,y=655,s=.98):
    art=dad(0,0).replace('fill="#67527C"','fill="#A6ABB6"')
    art=art.replace('</g>','<circle cx="-105" cy="230" r="10" fill="#FFD7B5"/><circle cx="105" cy="230" r="10" fill="#FFD7B5"/></g>')
    return f'<g id="parent-generation" transform="translate({x} {y}) scale({s})">{art}</g>'

def s10(phase):
    c='<path d="M34 1032H686" stroke="#E0C9BC" stroke-width="3"/>'
    if phase=='cost':
        c+=title('KHOẢNG',y=303,size=44)+title('3,8 TỶ',y=440,size=116)
        c+=mother(300,600,1.2,False)+arm('generation-child',455,785,1.2,(-43,-31),(25,7))
    else:
        c+=title('TỚI 4 THẾ HỆ',y=337,size=65)
        c+='<text x="360" y="398" text-anchor="middle" font-family="Scene" font-weight="900" font-size="28" fill="#67527C">Theo điều kiện MPRP</text>'
        dx=-28 if phase=='arrive' else 0
        c+=grandma(95+dx,705,.95,phase=='family')+older_parent(255+dx*.35,655,.98)
        c+=mother()+arm('generation-child',535,785,1.2,(-43,-70),(25,7))
        # The four labels describe relationships to the principal applicant.
        for x,t in [(95,'ÔNG BÀ'),(255,'CHA MẸ'),(420,'ĐƯƠNG ĐƠN'),(610,'CON')]:
            c+=f'<text x="{x}" y="1065" text-anchor="middle" font-family="Scene" font-weight="900" font-size="24" fill="#67527C">{t}</text>'
    return svg(c,'#FFF0E5')

def rotor(angle):
    blade='M-13 1Q-23-41-8-105Q-4-128 13-125Q31-120 29-101L10 2Z'
    blades=''.join(f'<path transform="rotate({a})" d="{blade}" fill="{color}" stroke="{INK}" stroke-width="3"/>' for a,color in [(0,'#84C9DA'),(120,'#B9A2DA'),(240,'#A3D4BF')])
    return f'<g id="rotor-placement" transform="translate(490 505)"><g id="rotor" transform="rotate({angle})">{blades}<circle r="24" fill="#FFD18B" stroke="{INK}" stroke-width="3.2"/><circle r="8" fill="#FFF0C7" stroke="{INK}" stroke-width="2.5"/></g></g>'

def s12(phase):
    hand={'ready':(368,799),'press':(385,829),'result':(368,799)}[phase]
    near=((hand[0]-110)/1.65-109,(hand[1]-680)/1.65-83)
    c=title('THỬ SỨC',y=193,size=56)
    c+='''<circle cx="490" cy="505" r="168" fill="#F1E9F8"/>
    <path d="M42 1034H682" stroke="#D6C3B4" stroke-width="3"/>
    <g id="workbench" stroke="#30313B" stroke-width="3.2" stroke-linejoin="round"><path d="M76 898H644L680 928H52Z" fill="#F1D5AF"/><path d="M52 928H680V948H52Z" fill="#DDB68E"/><path d="M85 948L79 1031M646 948L654 1031" stroke="#AA8A74" stroke-width="11"/></g>
    <g id="prototype-base" stroke="#30313B" stroke-width="3" stroke-linejoin="round"><path d="M300 858H600L642 886H278Z" fill="#F7E8CE"/><path d="M278 886H642V896H278Z" fill="#D8BF99"/></g>
    <g id="tower" stroke="#30313B" stroke-width="3"><ellipse cx="490" cy="851" rx="55" ry="15" fill="#A4C9D7"/><path d="M482 528H499L505 851H475Z" fill="#C6E3E7"/><path d="M491 541V834" fill="none" stroke="#83B6C7" stroke-width="3"/></g>'''
    c+=rotor(48 if phase=='result' else 0)
    c+='''<g id="circuit" stroke="#30313B" stroke-width="3" stroke-linejoin="round"><path d="M386 848Q410 864 432 844M473 845Q483 853 490 837" fill="none" stroke="#5F8EB7" stroke-width="4"/>
    <rect x="430" y="820" width="46" height="34" rx="6" fill="#AA93D0"/><path d="M433 821H473V833H433Z" fill="#E7B38C" stroke="none"/><path d="M440 820V814H449V820M458 820V814H467V820" fill="#A8AFB8" stroke-width="2"/>
    <path d="M356 828H414V852Q385 866 356 852Z" fill="#C8D6E5"/><ellipse cx="385" cy="828" rx="29" ry="10" fill="#E7EEF6"/>'''
    cy=829 if phase=='press' else 822
    c+=f'<ellipse id="push-button" cx="385" cy="{cy}" rx="20" ry="7" fill="#EC9D8F"/><circle id="power-indicator" cx="405" cy="849" r="4" fill="{"#52A985" if phase!="ready" else "#AAB2BD"}"/></g>'
    art=arm('experiment',110,680,1.65,(-30,35),near)
    # A stable eye-line to the project is part of the action pose, not idle acting.
    art=art.replace('id="experiment-eyes"','id="experiment-eyes" transform="translate(5 -4)"')
    c+=art
    if phase=='result':
        c+='''<g id="rotation-notation" fill="none" stroke="#8CB5CA" stroke-width="3.2" stroke-linecap="round"><path d="M581 375Q620 398 631 446M359 493Q354 453 379 421"/></g>'''
    return svg(c,'#FFF8E9')

items=[('S10/01-cost','Khoảng 3,8 tỷ',s10('cost')),('S10/02-arrive','Các thế hệ cùng vào khung',s10('arrive')),('S10/03-family','Bốn thế hệ trong một nhóm gia đình',s10('family')),('S12/01-ready','Mô hình đang chờ chạy',s12('ready')),('S12/02-press','Mascot bấm nút',s12('press')),('S12/03-result','Cánh quay, mascot quan sát',s12('result'))]
ledger=[]
for rel,label,art in items:
    folder=OUT/rel;a=folder/'assets';a.mkdir(parents=True)
    for f,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(f,a/dest)
    (folder/'layered-art.svg').write_text(art,encoding='utf-8')
    (folder/'index.html').write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{margin:0;width:100%;height:100%;overflow:hidden}}#root{{width:100%;height:100%}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="1" data-fps="30">{art}</div><script>const tl=gsap.timeline({{paused:true}});tl.to({{v:0}},{{v:1,duration:1}},0);window.__timelines['root']=tl;</script></body></html>''',encoding='utf-8')
    ledger.append({'path':rel,'label':label,'status':'proposal_pending_user_frame_approval'})
(OUT/'frame_inventory.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
