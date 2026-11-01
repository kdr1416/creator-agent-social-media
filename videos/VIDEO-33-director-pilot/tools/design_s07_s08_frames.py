"""Editable review frames only. Does not touch Antigravity builds or render video."""
from pathlib import Path
import json, re, shutil, hashlib
from build_pilots import mascot

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'revisions/S07-S08-design-r1'
if OUT.exists():
    raise SystemExit('Refusing to overwrite review revision')
OUT.mkdir(parents=True)
INK='#30313B'

def arm_rig(sid,x,y,scale,far,near=None,seated=False):
    a=mascot(sid,x,y,scale)
    fx,fy=far
    a=re.sub(rf'(<path id="{sid}-far-path" d=")[^"]+',rf'\g<1>M0 0Q{fx*.55:.1f} {fy*.35:.1f} {fx} {fy}',a)
    a=re.sub(rf'(<circle id="{sid}-far-hand" )cx="[^"]+" cy="[^"]+"',rf'\g<1>cx="{fx}" cy="{fy}"',a)
    if near:
        nx,ny=near
        a=re.sub(rf'(<path id="{sid}-near-path" d=")[^"]+',rf'\g<1>M0 0Q{nx*.6:.1f} {ny*.3:.1f} {nx} {ny}',a)
        a=re.sub(rf'(<circle id="{sid}-near-hand" )cx="[^"]+" cy="[^"]+"',rf'\g<1>cx="{nx}" cy="{ny}"',a)
    if seated:
        a=a.replace('M48 143L41 190L18 194M90 143L98 190L120 194','M48 143V226H25M90 143V226H111')
    return a

def face(x,y,s=1,wave=False):
    return f'''<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-linejoin="round">
    <path d="M-69 15Q-87-55-51-73Q-12-111 35-74Q83-75 76-5L63 57H-64Z" fill="#67527C" stroke-width="3"/>
    <path d="M-57-31Q-54-72 0-70Q59-67 61-19L55 29Q50 72 0 75Q-53 71-57 28Z" fill="#FFD7B5" stroke-width="3"/>
    <path d="M-58-26Q-36-31-25-59Q14-29 60-28L61-59Q32-91-7-83Q-62-83-65-32Z" fill="#67527C" stroke-width="3"/>
    <path d="M-26 68L-28 91L26 91L24 68" fill="#FFD7B5" stroke-width="3"/>
    <path d="M-28 83Q-94 78-105 133L-119 229H119L104 130Q92 80 28 83L0 113Z" fill="#80C9C3" stroke-width="3.4"/>
    <path d="M-28 83L0 113L28 83L35 134L0 120L-35 134Z" fill="#FFE8B5" stroke-width="2.5"/>
    <path d="M0 123V226M-91 151L-98 215M90 150L98 215" fill="none" stroke="#4D9F9B" stroke-width="2.6"/>
    <ellipse cx="-24" cy="7" rx="4.2" ry="6.2" fill="{INK}" stroke="none"/><ellipse cx="25" cy="7" rx="4.2" ry="6.2" fill="{INK}" stroke="none"/>
    <path d="M-13 36Q0 49 14 36M-30-10Q-23-15-16-11M17-11Q24-15 31-10" fill="none" stroke-width="2.8" stroke-linecap="round"/>
    <ellipse cx="-42" cy="29" rx="10" ry="6" fill="#EF9B8F" stroke="none"/><ellipse cx="42" cy="29" rx="10" ry="6" fill="#EF9B8F" stroke="none"/>
    {('<path d="M95 135Q154 151 157 90L153 39" fill="none" stroke="#30313B" stroke-width="21" stroke-linecap="round"/><path d="M95 135Q154 151 157 90L153 39" fill="none" stroke="#80C9C3" stroke-width="15" stroke-linecap="round"/><path d="M153 40L148 13Q151 0 157 13L162 26L169 4Q178-3 177 13L176 35L185 22Q195 18 190 33L181 54Q163 66 153 40Z" fill="#FFD7B5" stroke-width="2.8"/>') if wave else ''}
    </g>'''

def parent(x=235,y=570,scale=1.3,hello=False):
    # Complete body with fixed shoulder anchors; suitcase hand at (-72,194).
    return f'''<g id="adult-placement" transform="translate({x} {y}) scale({scale})" stroke="{INK}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
    <ellipse cx="0" cy="353" rx="78" ry="10" fill="#E5CFC1" opacity=".6" stroke="none"/>
    <path d="M-45 214L-42 330L-9 331L1 239L14 331H48L43 214Z" fill="#BC86AD"/>
    <path d="M-43 328H-8L-8 346H-65Q-66 336-43 328ZM15 329H48L65 343Q64 350 17 347Z" fill="#67527C"/>
    <path d="M-49 105Q-70 143-72 194" fill="none" stroke-width="20"/>
    <path d="M-49 105Q-70 143-72 194" fill="none" stroke="#80C9C3" stroke-width="14"/>
    <circle cx="-72" cy="194" r="10" fill="#FFD7B5"/>
    <path d="M-45 85Q-57 90-58 118L-57 212Q0 230 58 212L55 117Q52 90 43 85Z" fill="#80C9C3"/>
    <path d="M-24 84L0 112L25 84L32 130L0 118L-31 129Z" fill="#FFE8B5" stroke-width="2.5"/>
    <path d="M0 122V215M-41 164H-18M18 164H41" stroke="#4D9F9B" stroke-width="2.5" fill="none"/>
    <g transform="translate(0 39) scale(.57)">
    <path d="M-68 12Q-90-60-45-76Q12-104 57-67Q87-49 68 49H-64Z" fill="#67527C"/>
    <path d="M-56-28Q-47-72 0-68Q59-63 59-17L53 32Q45 69 0 72Q-49 70-54 29Z" fill="#FFD7B5"/>
    <path d="M-58-25Q-32-29-25-58Q14-29 59-28L61-56Q29-91-9-80Q-64-80-65-29Z" fill="#67527C"/>
    <ellipse cx="-23" cy="7" rx="4.2" ry="6.4" fill="{INK}"/><ellipse cx="25" cy="7" rx="4.2" ry="6.4" fill="{INK}"/>
    <path d="M-13 36Q0 49 14 36" fill="none" stroke-width="3"/>
    <ellipse cx="-41" cy="29" rx="10" ry="6" fill="#EF9B8F" stroke="none"/><ellipse cx="42" cy="29" rx="10" ry="6" fill="#EF9B8F" stroke="none"/>
    </g>
    <path d="M49 108Q84 124 88 91L91 {55 if hello else 118}" fill="none" stroke-width="20"/>
    <path d="M49 108Q84 124 88 91L91 {55 if hello else 118}" fill="none" stroke="#80C9C3" stroke-width="14"/>
    <circle cx="91" cy="{55 if hello else 118}" r="10" fill="#FFD7B5"/>
    </g>'''

def suitcase(x,y):
    return f'''<g id="suitcase" transform="translate({x} {y})" stroke="{INK}" stroke-width="3" stroke-linejoin="round">
    <path d="M-15 0V-43Q0-52 15-43V0" fill="none"/><path d="M-15-43H15" stroke-width="7" stroke-linecap="round"/>
    <rect x="-42" y="0" width="84" height="151" rx="15" fill="#81CADB"/><path d="M-31 15V132M-12 16V132M10 16V132M29 16V132" stroke="#BDE8EC" stroke-width="3"/>
    <rect x="28" y="28" width="22" height="40" rx="5" fill="#FFD18B"/><path d="M34 28V16" fill="none"/>
    <circle cx="-24" cy="160" r="8" fill="#67527C"/><circle cx="25" cy="160" r="8" fill="#67527C"/>
    </g>'''

def svg(content,bg='#FFF8E9'):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280"><defs><clipPath id="screen-mask"><rect x="89" y="389" width="542" height="326" rx="14"/></clipPath></defs><rect width="720" height="1280" fill="{bg}"/>{content}</svg>'''

def title(text,y=180,size=52):
    return f'<text x="360" y="{y}" text-anchor="middle" font-family="Scene" font-weight="900" font-size="{size}" fill="#195D8C">{text}</text>'

def s07(phase):
    active=phase!='ready'
    # Button contact is derived in the mascot shoulder's coordinate space.
    target={'ready':(-28,-32),'touch':((450-490)/1.45-25,(754-730)/1.45-72),'connected':(-18,-97)}[phase]
    content=title('GẦN NHAU HƠN')
    content+='''<path d="M49 1033Q362 1063 670 1033" fill="none" stroke="#E1CDBC" stroke-width="3"/>
    <ellipse cx="352" cy="903" rx="300" ry="22" fill="#E3D6D6" opacity=".52"/>
    <g id="device" stroke="#30313B" stroke-width="3.2" stroke-linejoin="round">
    <rect x="60" y="350" width="600" height="447" rx="27" fill="#CBBBE2"/>
    <rect x="78" y="371" width="564" height="407" rx="18" fill="#F9F7FF"/>
    <circle cx="360" cy="360" r="3" fill="#67527C" stroke="none"/>
    </g>'''
    if active:
        content+='<g clip-path="url(#screen-mask)"><rect x="89" y="389" width="542" height="326" fill="#E2F1EE"/><path d="M105 687Q380 643 630 687V715H89Z" fill="#CADFD7"/>'+face(310,484,.99,phase=='connected')+'</g>'
    else:
        content+='''<rect x="89" y="389" width="542" height="326" rx="14" fill="#E6E0EF"/><circle cx="360" cy="510" r="45" fill="#B4A5C9"/><path d="M269 639Q276 571 360 571Q444 571 451 639Z" fill="#B4A5C9"/>
        <circle cx="340" cy="674" r="5" fill="#846EAB"/><circle cx="360" cy="674" r="5" fill="#846EAB"/><circle cx="380" cy="674" r="5" fill="#846EAB"/>'''
    content+='''<g id="call-controls"><circle cx="262" cy="750" r="20" fill="#E8E2F2"/><path d="M259 737V751Q263 759 267 751V737M253 750Q253 766 263 766Q273 766 273 750M263 767V774" fill="none" stroke="#67527C" stroke-width="3" stroke-linecap="round"/>
    <circle cx="340" cy="750" r="20" fill="#E8E2F2"/><rect x="326" y="740" width="20" height="17" rx="4" fill="#67527C"/><path d="M345 745L356 740V757L345 752Z" fill="#67527C"/>'''
    content+=f'<rect x="411" y="731" width="78" height="44" rx="22" fill="{"#D96D75" if active else "#25836A"}"/>'
    content+='''<path d="M435 751Q450 741 466 751L463 758L456 756V752H445V756L438 758Z" fill="#FFFDF4"/></g>
    <path d="M60 797L659 797L697 859Q701 873 678 879H41Q18 872 26 859Z" fill="#E9DFF3" stroke="#30313B" stroke-width="3.2"/>
    <path d="M86 812H622L638 841H70Z" fill="#C5B8D7"/>
    <path d="M110 817H600M99 829H608M135 812L128 840M184 812L181 840M234 812L233 840M285 812V840M337 812V840M388 812V840M440 812L444 840M491 812L498 840M542 812L553 840M589 812L603 840" stroke="#F8F4FD" stroke-width="3"/>
    <path d="M281 850H430L437 866H275Z" fill="#F8F4FD" stroke="#B2A3C5" stroke-width="2"/>
    '''
    content+=arm_rig('call',490,730,1.45,target,(26,9))
    return svg(content)

def s08(phase):
    content=title('NHỮNG CHUYẾN THĂM CON',size=42)
    content+='''<path d="M46 1024H675" stroke="#D6BFB2" stroke-width="3"/>
    <path d="M44 413Q180 354 310 386T670 409" fill="none" stroke="#E3D7E8" stroke-width="3"/>
    <g id="arrival-door" opacity=".8"><path d="M418 427H638V807H418Z" fill="#E6DDF2"/><path d="M438 447H617V787H438Z" fill="#F7EFF8"/><path d="M527 447V787" stroke="#C9B8DB" stroke-width="3"/><path d="M482 588H574M561 576L574 588L561 600" fill="none" stroke="#8A73AF" stroke-width="5" stroke-linecap="round"/></g>'''
    # Suitcase handle center equals parent far-hand world position.
    px=235 if phase=='arrive' else 270
    content+=suitcase(px-72*1.3,570+194*1.3+46)
    content+=parent(px,570,1.3,phase=='greet')
    content+=arm_rig('travel',455,680,1.8,(-43,-31) if phase=='arrive' else (-42,-70),(25,7))
    return svg(content,'#FFF0E5')

def vignette(kind):
    labels={'study':'HỌC TẬP','living':'SINH SỐNG','work':'LÀM VIỆC'}
    c=title(labels[kind],size=56)
    c+='<path d="M53 1032H670" stroke="#D6BFB2" stroke-width="3"/>'
    if kind=='living':
        c+='''<g id="room"><rect x="94" y="340" width="229" height="259" rx="7" fill="#B5DDE5" stroke="#30313B" stroke-width="3"/><path d="M209 342V597M96 469H322" stroke="#FFFDF4" stroke-width="11"/><path d="M101 348L169 348L101 427M227 348H280L227 400" fill="#DDF2F2"/>
        <path d="M395 397H612V680H395Z" fill="#F8E4BE" stroke="#30313B" stroke-width="3"/><path d="M409 488H600M409 581H600" stroke="#CFB387" stroke-width="5"/>
        <path d="M428 484V427H447V484M454 484V419H475V484M483 484V435H508V484" stroke="#30313B" stroke-width="2.5" fill="#B7A0D6"/>
        <path d="M115 824Q100 770 140 760H418Q456 766 441 824V925H115Z" fill="#B7D6B9" stroke="#30313B" stroke-width="3.5"/><rect x="97" y="823" width="368" height="112" rx="20" fill="#91C6AB" stroke="#30313B" stroke-width="3.5"/><path d="M125 934V970M438 934V970M281 824V931" stroke="#30313B" stroke-width="4"/><path d="M142 776H229V844H142Z" fill="#E7C3D6" stroke="#30313B" stroke-width="3"/>
        </g>'''
        # Hand on a book being placed on a reachable shelf, not floating.
        c+='<g id="coffee-table"><path d="M290 939H470V951H290Z" fill="#EBC8A2" stroke="#30313B" stroke-width="3"/><path d="M306 952V1028M454 952V1028" stroke="#9A7C69" stroke-width="8"/></g>'
        c+=arm_rig('home',440,756,1.3,(-38,44),(25,7))
        c+='<g id="held-book" transform="translate(515 803) rotate(-8)"><rect x="-18" y="-33" width="42" height="62" rx="4" fill="#A990D5" stroke="#30313B" stroke-width="3"/><path d="M-10-29V24" stroke="#E9E0F4" stroke-width="3"/></g>'
        # Anchor the book to the near hand: (440 + (109-35)*1.3, 756 + (83-60)*1.3).
        c=c.replace('translate(515 803)','translate(423.1 906.8)')
        c+='<circle cx="423.1" cy="906.8" r="8" fill="#FFAC3C" stroke="#30313B" stroke-width="2.5"/>'
    else:
        c+='''<g id="desk"><path d="M74 822H646L676 855H55Z" fill="#F2D3A9" stroke="#30313B" stroke-width="3.5"/><path d="M55 855H676V877H55Z" fill="#DFB687" stroke="#30313B" stroke-width="3"/><path d="M92 877L83 1025M635 877L645 1025" stroke="#9A7C69" stroke-width="13" stroke-linecap="round"/></g>
        <rect x="170" y="660" width="143" height="165" rx="33" fill="#C8B8DD" stroke="#30313B" stroke-width="3"/><rect x="156" y="820" width="169" height="28" rx="10" fill="#B7A0CF" stroke="#30313B" stroke-width="3"/><path d="M176 848V1025M304 848V1025" stroke="#8A73AF" stroke-width="9"/>'''
        c+=arm_rig('activity',166,622,1.34,(54,52),(30,45),seated=True)
        c+='<path d="M55 855H676V877H55Z" fill="#DFB687" stroke="#30313B" stroke-width="3"/>'
        if kind=='study':
            c+='''<g id="open-book"><path d="M329 803L431 777L435 850L331 869Z" fill="#FFFDF2" stroke="#30313B" stroke-width="3"/><path d="M431 777L562 793L555 866L435 850Z" fill="#FFFDF2" stroke="#30313B" stroke-width="3"/><path d="M431 779L435 849" stroke="#CAB997" stroke-width="3"/><path d="M353 810L409 797M353 825L409 812M457 801L532 811M457 818L529 827" stroke="#CAB997" stroke-width="3"/><path d="M456 837L505 842" stroke="#087BC1" stroke-width="5"/></g>
            <path d="M355 795L385 826" stroke="#67527C" stroke-width="7" stroke-linecap="round"/><path d="M385 826L391 833L382 831Z" fill="#30313B"/>
            <g id="study-lamp"><path d="M560 815V660L515 600" fill="none" stroke="#8A73AF" stroke-width="12" stroke-linecap="round"/><path d="M473 587Q511 562 538 601L547 633L484 647Z" fill="#FFE09A" stroke="#30313B" stroke-width="3"/><ellipse cx="563" cy="817" rx="42" ry="10" fill="#8A73AF" stroke="#30313B" stroke-width="3"/></g>'''
        else:
            c+='''<g id="work-laptop"><path d="M347 633H599Q608 633 609 645V805H347Z" fill="#8DCBD8" stroke="#30313B" stroke-width="3"/><rect x="364" y="651" width="228" height="134" rx="5" fill="#FFFDF5"/>
            <path d="M382 756V710H410V756M427 756V686H455V756M472 756V717H500V756M517 756V675H545V756" fill="#A990D5"/><path d="M377 763H566" stroke="#AFCFC8" stroke-width="3"/>
            <path d="M347 806H609L644 845H321Z" fill="#E6E2F0" stroke="#30313B" stroke-width="3"/><path d="M374 819H582M364 830H593" stroke="#B4A5C9" stroke-width="4"/></g>'''
    return svg(c,'#F0EAF8' if kind=='study' else '#FFF8E9')

items=[('S07/01-ready','Chờ kết nối',s07('ready')),('S07/02-contact','Chạm nút gọi',s07('touch')),('S07/03-connected','Vẫy tay đáp lại',s07('connected')),('S08/01-arrive','Phụ huynh kéo vali',s08('arrive')),('S08/02-greet','Gặp và chào con',s08('greet')),('S08/03-study','Hoạt động học tập',vignette('study')),('S08/04-living','Góc sinh hoạt',vignette('living')),('S08/05-work','Hoạt động làm việc',vignette('work'))]
ledger=[]
for rel,label,art in items:
    folder=OUT/rel;assets=folder/'assets';assets.mkdir(parents=True)
    for source,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(source,assets/dest)
    art=art.replace('<svg ', '<svg style="width:100%;height:100%" ',1)
    (folder/'layered-art.svg').write_text(art,encoding='utf-8')
    content=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{{font-family:Scene;src:url('assets/font.ttf');font-weight:900}}*{{box-sizing:border-box}}html,body{{margin:0;width:100%;height:100%;overflow:hidden}}#root{{width:100%;height:100%}}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="1" data-fps="30">{art}</div><script>const tl=gsap.timeline({{paused:true}});tl.to({{v:0}},{{v:1,duration:1,ease:'none'}});window.__timelines['root']=tl;</script></body></html>'''
    (folder/'index.html').write_text(content,encoding='utf-8')
    ledger.append({'path':rel,'label':label,'status':'static_design_proposal_not_approved','engine':'HF_ONLY','no_voice_or_video_created':True})
(OUT/'frame_inventory.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'DIRECTION.md').write_text('''# S07/S08 — thiết kế frame R1, chờ duyệt

Đây là các tư thế tĩnh/khung hoạt động để duyệt ý và tạo hình, không phải motion đã dựng. Không thay source trong build, không đổi voice/timing hay trạng thái các pilot đã duyệt.

S07: một người thân lớn trong laptop; mascot chạm nút gọi, sau đó thu tay và vẫy đáp lại. Phụ huynh áo mint/tóc tím than là cùng một nhân vật với S08. Nút là bộ phận của giao diện cuộc gọi có chức năng; không có hộp thông tin trang trí. Frame 01/02/03 lần lượt là chờ, tiếp xúc và kết nối. Giữ nguyên voice/sample bounds từ STORYBOARD.json khi sản xuất. Không tạo file audio mới ở vòng frame.

S08: phụ huynh toàn thân, vali tới hông, tay bám cần kéo, mascot và phụ huynh cùng mặt sàn. Frame 01 và 02 minh họa đến nơi/chào con, chưa phải kết quả nội suy giữa hai pose. Ba khung sau là ba hoạt động dự kiến thay lần lượt theo học tập/sinh sống/làm việc; không đặt cả ba icon nhỏ đồng thời. Đây là các khả năng kế hoạch, không là bằng chứng quyền làm việc/nhập học. Khi đối chiếu voice nếu không đủ thời gian, giảm động tác mỗi khung, không tăng tốc voice. Giữ footer 200px, chữ ngắn Segoe UI Black.

Rig: node placement chỉ đặt vị trí/scale; motion dùng wrapper riêng. Giữ vai cố định trong torso-space; forearm/hand cùng chain; tính điểm chạm theo matrix sang scene-space. Không animate y=-6 trên node có translate y≈760. Vali và tay dùng cùng điểm grip; bánh chạm sàn. Trước motion phải duyệt hình phụ huynh và laptop.

Thời lượng: S07 ≈4.70s, S08 ≈5.45s (số chính xác từ packet/audio gốc). S07 dự kiến 0–1.2s đưa tay/chạm, 1.2–2s kết nối, 2–4.7s vẫy/resolve. S08 dự kiến 0–1.5s gặp con, ba shot học/sống/làm thay lần lượt trong phần còn lại theo lời; đối chiếu word cue trước khi khóa. Không suy ra các pose tĩnh đã chứng minh rig chuyển động đúng.

Sau duyệt mới dựng motion thử. Kiểm frame tiếp xúc quanh event và playback thật. Chưa sản xuất lại các cảnh khác; đề xuất S10–S14 nằm trong qa/antigravity-review-r1/REVIEW_AND_REVISION_PROPOSAL.md.
''',encoding='utf-8')
print(OUT)
