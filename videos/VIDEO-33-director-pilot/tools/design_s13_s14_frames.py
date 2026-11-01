"""Ending-scene static design proposals; no video or master mutations."""
from pathlib import Path
import ast,json,re,shutil
from build_pilots import mascot

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'revisions/S13-S14-design-r1'
if OUT.exists():raise SystemExit('Refusing to overwrite review round')
OUT.mkdir(parents=True)
INK='#30313B'
kit={'INK':INK,'mascot':mascot,'re':re}
src=ROOT/'tools/design_s07_s08_frames.py';tree=ast.parse(src.read_text(encoding='utf-8'))
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),str(src),'exec'),kit)
arm,parent,title=kit['arm_rig'],kit['parent'],kit['title']
def svg(body,bg='#FFF8E9'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280" style="width:100%;height:100%"><rect width="720" height="1280" fill="{bg}"/>{body}</svg>'

def campus(id,x,y,s=1):
    windows=''.join(f'<path d="M{xx} {yy}h46v58h-46Z" fill="#ADD7E4"/><path d="M{xx+23} {yy}v58M{xx} {yy+29}h46" fill="none" stroke="#F5FBF8" stroke-width="3"/>' for xx,yy in [(42,112),(119,112),(335,112),(412,112),(42,210),(119,210),(335,210),(412,210)])
    return f'''<g id="{id}" transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="3" stroke-linejoin="round">
    <ellipse cx="250" cy="449" rx="265" ry="18" fill="#E4D3C2" opacity=".6" stroke="none"/>
    <path d="M8 83H492V420H8Z" fill="#F1D9B4"/><path d="M-4 73H503V99H-4Z" fill="#D8B18D"/>
    {windows}
    <path d="M194 55H306V420H194Z" fill="#FAEBD0"/>
    <path d="M177 69L250 18L323 69Z" fill="#B9A0D7"/><path d="M180 69H320V84H180Z" fill="#9C81C1"/>
    <circle cx="250" cy="131" r="26" fill="#FFFDF3"/><path d="M250 113V132L263 142" fill="none" stroke-width="3" stroke-linecap="round"/>
    <path d="M220 420V263Q250 220 280 263V420Z" fill="#4D7B92"/>
    <path d="M221 267L252 282V420H221Z" fill="#91C3CF"/><path d="M280 267L260 280V420H280Z" fill="#B2D8DE"/>
    <path d="M207 421H293L308 438H191Z" fill="#DCC8B0"/><path d="M191 438H308V450H191Z" fill="#CDB498"/>
    </g>'''

def home(id,x,y,s=1,malta=False):
    c=f'<g id="{id}" transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="3" stroke-linejoin="round"><ellipse cx="120" cy="319" rx="142" ry="20" fill="#DCCEBE" opacity=".55" stroke="none"/>'
    if malta:
        c+='''<path d="M9 48H231V303H9Z" fill="#EED7AE"/><path d="M0 42H240V60H0Z" fill="#DDC297"/><path d="M15 26H225V43H15Z" fill="#F7E4BF"/>
        <path d="M20 167H220M20 231H73M171 231H220M20 270H73M171 270H220" stroke="#D7BC90" stroke-width="2"/>
        <path d="M87 302V207Q120 159 153 207V302Z" fill="#73AEAB"/><path d="M120 188V301" stroke="#4C8B88" stroke-width="3"/><circle cx="132" cy="251" r="4" fill="#FFD18B"/>
        <path d="M66 86H174V157H66Z" fill="#6BAAA7"/><path d="M71 91H169V141H71Z" fill="#C4E3DE"/>
        <path d="M99 89V156M141 89V156M66 143H174M74 154L80 170H89L87 154M153 154L151 170H160L167 154" stroke="#4C8B88" stroke-width="4" fill="none"/>
        <path d="M58 156H183V166H58Z" fill="#4C8B88"/>
        <path d="M27 195H64V258H27Z" fill="#BDE0DF"/><path d="M45 196V258M27 226H64" stroke="#5F9D9B" stroke-width="3"/>
        <path d="M179 195H215V258H179Z" fill="#BDE0DF"/><path d="M197 196V258M179 226H215" stroke="#5F9D9B" stroke-width="3"/>'''
    else:
        c+='''<path d="M10 80H230V303H10Z" fill="#FFE2AF"/><path d="M-8 82L119 9L248 82L232 101L120 40L7 101Z" fill="#D78F9C"/>
        <path d="M55 302V210Q82 193 108 210V302Z" fill="#75B4D0"/><circle cx="96" cy="256" r="4" fill="#FFE0A0"/>
        <path d="M38 111H90V166H38ZM149 111H201V166H149ZM150 214H201V267H150Z" fill="#D7EDE9"/>
        <path d="M64 112V165M38 139H90M176 112V165M149 139H201M175 215V266M150 240H201" stroke="#75B4D0" stroke-width="3"/>
        <path d="M24 187H218" stroke="#EDC58E" stroke-width="4"/>'''
    return c+'</g>'

def s13(phase):
    if phase=='student':
        c=title('HÀNH TRÌNH CỦA CON',y=190,size=45)
        c+='<text x="360" y="297" text-anchor="middle" font-family="Scene" font-weight="900" font-size="30" fill="#796A91">CHÂU ÂU</text>'
        c+='<path d="M36 1040H684" stroke="#DBCBBC" stroke-width="3"/><path d="M235 1045Q214 960 333 924T395 881L411 848" fill="none" stroke="#E6D2B7" stroke-width="60" stroke-linecap="round"/>'
        c+=campus('study-campus',105,365,1.02)
        c+=arm('world-student',155,820,1.1,(-30,22),(28,-12))
        return svg(c)
    c=title('TÀI SẢN GIA ĐÌNH',y=190,size=47)
    transform='translate(94 -250) scale(1.4)' if phase=='local' else 'translate(0 0) scale(1)'
    if phase=='local':c+='<defs><clipPath id="local-crop"><rect x="0" y="0" width="620" height="1080"/></clipPath></defs><g clip-path="url(#local-crop)">'
    c+=f'<g id="asset-camera" transform="{transform}">'
    c+='<path d="M29 840H333M381 840H688" stroke="#DBC5B7" stroke-width="3"/>'
    c+=home('vietnam-home',70,500,1,False)+home('malta-home',455,548,.85,True)
    for x,t in [(190,'VIỆT NAM'),(557,'MALTA')]:c+=f'<text x="{x}" y="900" text-anchor="middle" font-family="Scene" font-weight="900" font-size="32" fill="#195D8C">{t}</text>'
    c+='<text id="possibility" x="557" y="446" text-anchor="middle" font-family="Scene" font-weight="900" font-size="30" fill="#796A91">CÓ THỂ</text></g>'
    if phase=='local':c+='</g>'
    return svg(c,'#FFF0E5')

def mother_gate(x,hand):
    art=parent(x,620,1.2,False);lx=(hand[0]-x)/1.2;ly=(hand[1]-620)/1.2
    art=art.replace('M49 108Q84 124 88 91L91 118',f'M49 108Q{(49+lx)*.5:.4f} {(108+ly)*.5:.4f} {lx:.4f} {ly:.4f}')
    art=art.replace('cx="91" cy="118"',f'cx="{lx:.4f}" cy="{ly:.4f}"')
    return art

def gate(opened=False):
    if opened:
        pts='570,700 635,724 635,924 570,900';bars=[(586,706,586,906),(603,712,603,912),(620,719,620,919)];handle=(625,780)
    else:
        pts='440,700 570,700 570,900 440,900';bars=[(467,700,467,900),(500,700,500,900),(536,700,536,900)];handle=(465,760)
    c=f'<g id="choice-gate" stroke="{INK}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M435 687V922M570 685V921" stroke="#AA8A74" stroke-width="12"/>'
    c+=f'<g id="gate-leaf"><polygon id="gate-panel" points="{pts}" fill="#C2DDD3"/>'
    for i,(x,y,xx,yy) in enumerate(bars):c+=f'<path id="gate-bar-{i}" d="M{x} {y}L{xx} {yy}" stroke="#7BAA9D" stroke-width="7"/>'
    c+=f'<circle id="gate-handle" cx="{handle[0]}" cy="{handle[1]}" r="8" fill="#FFD18B"/></g>'
    c+='<circle cx="570" cy="715" r="5" fill="#8C796A"/><circle cx="570" cy="885" r="5" fill="#8C796A"/></g>'
    return c

def s14(phase):
    if phase=='key':
        c=title('THÊM MỘT CĂN NHÀ',y=250,size=49)
        c+='<circle cx="365" cy="765" r="209" fill="#F0E6F5"/><path d="M42 1039H680" stroke="#D6C3B4" stroke-width="3"/>'
        c+=arm('choice',170,715,1.5,(-29,27),((364-170)/1.5-109,(790-715)/1.5-83))
        c+='''<g id="house-key" stroke="#30313B" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="386" cy="790" r="21" fill="#FFD18B"/><circle cx="386" cy="790" r="10" fill="#F0E6F5"/><path d="M407 790H477M450 790V806M467 790V801" stroke-width="8"/><path d="M377 809L370 838" fill="none" stroke-width="3"/><path d="M349 859L368 839L389 858V885H349Z" fill="#BCA4DB"/><path d="M345 859L368 835L394 859" fill="none"/><path d="M363 885V869H376V885" fill="#D9EBEA" stroke-width="2.4"/></g>
        <circle cx="364" cy="790" r="10" fill="#FFAC3C" stroke="#30313B" stroke-width="3"/>'''
        return svg(c)
    opened=phase=='open'
    c=title('THÊM MỘT LỰA CHỌN',y=181,size=46)
    c+='''<path d="M0 637Q159 572 355 630T720 618V1080H0Z" fill="#E8E8D9"/>
    <path d="M369 1040L360 850C282 764 220 633 175 522M360 850C470 797 541 671 555 527" fill="none" stroke="#CDBEA6" stroke-width="72" stroke-linecap="round"/>
    <path d="M369 1040L360 850C282 764 220 633 175 522M360 850C470 797 541 671 555 527" fill="none" stroke="#FFF7E5" stroke-width="60" stroke-linecap="round"/>
    <text x="171" y="333" text-anchor="middle" font-family="Scene" font-weight="900" font-size="29" fill="#195D8C">THĂM CON</text>
    <text x="549" y="333" text-anchor="middle" font-family="Scene" font-weight="900" font-size="24" fill="#195D8C">KẾ HOẠCH DÀI HẠN</text>'''
    c+=campus('visit-campus',72,368,.40)+home('future-home',475,367,.63,True)
    c+=gate(opened)
    c+=mother_gate(505 if opened else 360,(625,780) if opened else (465,760))
    c+=arm('choices-student',145,815,1.1,(-30,18),(30,-19))
    return svg(c,'#FFF8E9')

items=[('S13/01-student','Hành trình của con',s13('student')),('S13/02-local','Tài sản tại Việt Nam',s13('local')),('S13/03-expand','Có thể thêm địa điểm Malta',s13('expand')),('S14/01-key','Từ chìa khóa căn nhà',s14('key')),('S14/02-gate','Lối thứ hai đang đóng',s14('closed')),('S14/03-open','Cả hai lối đều mở',s14('open'))]
ledger=[]
for rel,label,art in items:
    f=OUT/rel;a=f/'assets';a.mkdir(parents=True)
    for src,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(src,a/dest)
    (f/'layered-art.svg').write_text(art,encoding='utf-8')
    (f/'index.html').write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}html,body{{margin:0;width:100%;height:100%;overflow:hidden}}#root{{width:100%;height:100%}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="1" data-fps="30">{art}</div><script>const tl=gsap.timeline({{paused:true}});tl.to({{v:0}},{{v:1,duration:1}},0);window.__timelines['root']=tl;</script></body></html>''',encoding='utf-8')
    ledger.append({'path':rel,'label':label,'status':'proposal_pending_user_frame_approval'})
(OUT/'frame_inventory.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
