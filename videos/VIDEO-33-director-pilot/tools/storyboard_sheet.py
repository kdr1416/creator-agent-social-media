"""Create static staging sketches for the unproduced scenes, not production assets."""
from pathlib import Path
import json, html
from build_pilots import mascot, house, person
from prepare import ROOT, save

INK='#30313B'
def path(d,fill='none',stroke=INK,sw=3):return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def ellipse(x,y,rx,ry,c):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" stroke="{INK}" stroke-width="3"/>'
def rect(x,y,w,h,c,rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}" stroke="{INK}" stroke-width="3"/>'
def line(x1,y1,x2,y2,stroke=INK,sw=3):return path(f'M{x1} {y1}L{x2} {y2}','none',stroke,sw)
def coin(x,y,s=1):return f'<g transform="translate({x} {y}) scale({s})">'+ellipse(0,0,38,42,'#FFCE75')+path('M-13 0L0-15L13 0L0 16Z','#FFF7DA')+'</g>'
def book(x,y,s=1):return f'<g transform="translate({x} {y}) scale({s})">'+path('M0 0L80-25L170 0V130L80 110L0 130Z','#FFFDF2')+line(80,-25,80,110)+line(14,24,59,11,'#CFC3B1')+line(100,16,155,29,'#CFC3B1')+'</g>'
def desk(x,y,s=1):return f'<g transform="translate({x} {y}) scale({s})">'+rect(0,0,195,24,'#C5DFDA')+line(20,24,15,130)+line(175,24,181,130)+'</g>'

def art(n):
    if n==2:
        return path('M85 550L360 490L635 550V980L360 1010L85 960Z','#FFFCF0')+line(360,490,360,1010,'#CFBA9F')+''.join(coin(270,810-i*48,1.1) for i in range(6))+path('M415 520L470 530L515 932L461 940Z','#ABD3DE')+''.join(line(460+i*5,600+i*40,485+i*5,596+i*40) for i in range(6))
    if n==3:
        return path('M110 960C570 1060 625 735 330 700C50 670 140 390 545 395','none','#CDB5DB',44)+path('M110 960C570 1060 625 735 330 700C50 670 140 390 545 395','none','#FFF7DB',34)+desk(106,720,.8)+book(120,660,.65)+desk(440,395,.75)+rect(461,316,83,67,'#ABD6DE')+mascot('b03',250,789,1.05)
    if n==4:
        return path('M90 620L540 710L624 920L150 979Z','#FFF7DD')+path('M90 620L150 979L165 996L107 637Z','#D9C4A4')+house('b04-house',143,566,.9)+coin(350,736)+coin(405,767)+path('M474 421C474 358 577 354 574 420C572 459 520 464 520 511','none','#087BC1',15)+ellipse(520,555,8,8,'#087BC1')
    if n==6:
        return ellipse(340,720,251,95,'#F5D3B7')+path('M89 720V750Q345 858 591 750V720Q340 814 89 720Z','#E1B894')+line(170,778,156,1005)+line(520,778,535,1005)+path('M270 628L394 626L401 811L278 811Z','#FFE7C8')+person(143,642,1.4,'#A8CFD9')+person(548,629,1.3,'#C3A8D9')+rect(235,848,100,113,'#A9D3C0',12)+mascot('b06',452,820,1.03)
    if n==7:
        return desk(90,900,2.6)+path('M145 460H570V795H145Z','#ABCFDC')+rect(168,486,378,277,'#FFF6E6',10)+path('M145 795L91 861H624L570 795Z','#ECE4D2')+person(285,665,1.7,'#B7A1D7')+person(426,671,1.4,'#ABD4C0')+path('M139 699C46 703 67 925 323 953','none','#087BC1',7)+mascot('b07',398,815,1.05)
    if n==8:
        return line(70,1008,650,1008,'#C4AD9B')+rect(107,800,108,174,'#9ED3DC',15)+path('M132 800V759H189V800')+ellipse(130,988,9,9,'#30313B')+ellipse(196,988,9,9,'#30313B')+person(254,872,1.8,'#B4A0D2')+mascot('b08',397,798,1.05)+book(102,440,.8)+house('b08-h',300,398,.65)+rect(516,470,97,78,'#A8CDB9',9)+path('M545 470V452H583V470')
    if n==10:
        return path('M77 390L354 350L644 407V968L354 1019L77 970Z','#FFFDF2')+line(354,350,354,1019,'#D1BA9D',6)+person(160,487,.88,'#9BC9D4')+person(269,487,.88,'#C5ACD7')+person(214,654,1.0,'#E9B4B0')+person(421,772,1.0,'#9BC9D4')+person(539,772,1.0,'#C5ACD7')+person(481,928,.72,'#FFBC63')+path('M160 520H269M214 520V580M214 687V710H481V704M481 805V876','none','#BAA58C')+mascot('b10',524,867,.67)
    if n==11:
        return desk(73,855,2.8)+path('M84 658L155 632L173 650L153 672L131 668L109 687Z','#FFCF77')+path('M430 550Q557 509 604 598L622 837H400L409 622Q412 579 430 550Z','#8FC7D5')+path('M418 621Q511 674 604 621L599 755H417Z','#087BC1')+path('M419 621L433 561L584 557L604 621Z','#FFF1D1')+book(345,470,.82)+mascot('b11',229,824,1.04)
    if n==12:
        return desk(318,717,1.6)+rect(342,746,76,114,'#CBB3D9',10)+line(125,365,602,365,'#B39DAF',7)+path('M440 385V451L413 482L433 500L466 468V385Z','#A9D2C2')+path('M550 385V477L577 506L591 488L567 465V385Z','#9DCED8')+mascot('b12',178,745,1.12)+rect(188,987,111,23,'#F3CF9B')+line(203,1010,199,1063)+line(285,1010,290,1063)
    if n==13:
        return ellipse(352,688,247,247,'#B1D7DB')+ellipse(352,688,135,247,'#B1D7DB')+line(105,688,599,688,'#689DAA')+path('M150 553Q352 650 554 553M150 823Q352 726 554 823','none','#689DAA')+path('M140 706C220 441 515 456 594 677','none','#087BC1',6)+path('M144 747C219 994 474 922 563 813','none','#CE8855',6)+mascot('b13',458,865,.88)
    if n==14:
        return house('b14-h',72,548,1)+path('M336 538L463 487L642 567V967L465 1012L336 928Z','#FFF9DD')+path('M466 1004V757C466 651 372 704 373 607M466 757C468 675 574 710 574 611','none','#A7C4BC',18)+mascot('b14',240,820,1.05)+path('M302 822L344 805L365 822L337 842Z','#FFCE75')
    return ''

def main():
    board=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'));blocks=[]
    for s in board['scenes']:
        sid=s['scene_id'];n=s['scene_number']
        if sid in ('S01','S05','S09'):
            t={'S01':'5.80','S05':'5.50','S09':'7.20'}[sid]
            image=f'qa/{sid}/frame-{t}.png';kind='PILOT: final rendered frame'
        else:
            bg=['#FFF8E9','#FFF0E5','#F0EAFB'][(n-1)%3]
            typography=''.join(f'<text x="360" y="{195+i*55}" text-anchor="middle" fill="#0870AC" font-size="{38 if len(t["text"])>20 else 45}">{html.escape(t["text"])}</text>' for i,t in enumerate(s['visible_text_inventory']))
            svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280"><style>@font-face{{font-family:Board;src:url("../../assets/fonts/segoe-ui-black.ttf")}}text{{font-family:Board,sans-serif;font-weight:900}}</style><rect width="720" height="1280" fill="{bg}"/>{art(n)}{typography}</svg>'
            save(f'planning/boards/{sid}.svg',svg);image=f'planning/boards/{sid}.svg';kind='ROUGH STAGING: not a production asset'
        blocks.append(f'<article><h2>{sid} · {html.escape(s["title"])}</h2><small>{s["start"]:.3f}–{s["end"]:.3f}s · {kind}</small><img src="{image}" alt="{html.escape(s["title"])}"><p><strong>Hiểu:</strong> {html.escape(s["takeaway"])}</p><p><strong>Biến đổi:</strong> {html.escape(s["transformation"])}</p><p><strong>Sang cảnh:</strong> {html.escape(s["handoff"])}</p><a href="scenes/{sid}/PACKET.md">Packet chi tiết</a></article>')
    save('STORYBOARD.html','''<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VIDEO-33 · Storyboard 14 cảnh</title><style>@font-face{font-family:Board;src:url('assets/fonts/segoe-ui-black.ttf');font-weight:900}body{font-family:Segoe UI,sans-serif;color:#30313B;background:#FFF8E9;margin:24px;line-height:1.45}h1,h2{font-family:Board,sans-serif}h1{font-size:30px}h2{font-size:21px}header{max-width:950px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(275px,1fr));gap:28px}article{min-width:0;padding-top:20px;border-top:2px solid #D5C4B3}img{display:block;width:270px;max-width:100%;aspect-ratio:9/16;margin-top:14px}small{display:block;font-size:12px}a{color:#0870AC}p{font-size:16px}</style><header><h1>Một điểm tựa, thêm lựa chọn · 14 cảnh</h1><p>Storyboard toàn phim 75,16s. Ba ảnh S01/S05/S09 lấy từ pilot đã render; 11 khung còn lại là phác staging để đọc chuỗi, chưa phải asset sản xuất/animation. Mở packet để xem trạng thái đầu, nhịp thoại, layer và ràng buộc chi tiết. Duyệt ý tưởng trước khi Antigravity thi công.</p><p><a href="REVIEW.html">Xem 3 pilot có voice</a> · <a href="STORYBOARD.json">Storyboard JSON</a></p></header><div class="grid">'''+''.join(blocks)+'</div></html>')
    print('14-frame storyboard sheet created; 11 static rough sketches, 3 pilot frames.')

if __name__=='__main__':main()
