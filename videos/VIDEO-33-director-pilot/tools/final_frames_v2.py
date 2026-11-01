"""Two proposed final-state frames; does not replace pilots or authorize animation."""
from pathlib import Path
import sys,json,shutil
sys.path.insert(0,str(Path(__file__).parent))
from prepare import ROOT
from build_pilots import mascot

OUT=ROOT/'revisions/final-frames-v2'
I='#30313B'
def p(d,c='none',s=I,w=3):return f'<path d="{d}" fill="{c}" stroke="{s}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
def r(x,y,w,h,c,rad=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rad}" fill="{c}" stroke="{I}" stroke-width="2.8"/>'
def e(x,y,rx,ry,c):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" stroke="{I}" stroke-width="2.5"/>'
def window(x,y,w=42,h=72):
    return r(x,y,w,h,'#FFF4D6',w/2)+p(f'M{x+w/2} {y+5}V{y+h}M{x+3} {y+h*.55}H{x+w-3}','none','#BDA487',2)
def building(x,y,s=1,tone='#F2CEA0'):
    return f'<g transform="translate({x} {y}) scale({s})">'+p('M0 45L55 12L128 39V171L54 206L0 172Z',tone)+p('M54 76L128 39V171L54 206Z','#DCB288')+p('M0 45L55 12L128 39L54 76Z','#FFF2D6')+r(13,76,20,31,'#B5D7D9')+r(13,123,20,31,'#B5D7D9')+p('M72 90L108 73V103L72 121Z','#087BC1')+p('M72 141L108 124V154L72 172Z','#087BC1')+'</g>'

def scene05():
    a=p('M71 348L598 325L640 660L110 704Z','#FFFDF3')+'<image href="assets/valletta.jpg" x="91" y="354" width="515" height="308" preserveAspectRatio="xMidYMid slice"/>'
    a+=p('M103 697L344 627L592 790L379 982L103 910Z','#FFF4D8')
    a+=p('M379 982L344 627L592 790Z','#EBD8B4')+p('M103 910L344 627L379 982Z','#FFF9E9')
    # Pop-up architecture: one continuous residential facade, folded side wall and balcony.
    a+='<g filter="url(#shadow)">'
    a+=p('M157 453L421 431L421 846L157 871Z','#F3D8AD')
    a+=p('M421 431L501 491L501 879L421 846Z','#D7B58F')
    a+=p('M142 440L421 414L515 482L501 501L421 447L142 470Z','#FFF1CE')
    a+=p('M158 499L421 477M158 640L421 618M158 778L421 756','none','#D8BC98',3)
    for yy in (514,653):
        for xx in (185,273,357):a+=window(xx,yy,40,74)
    a+=p('M250 541L342 533L342 617L250 627Z','#168EB2')
    a+=p('M235 549L250 541L250 627L235 613Z','#076E96')
    a+=p('M250 541L274 528L361 521L342 533Z','#A4D9DF')
    a+=p('M250 580L342 571M280 539V624M313 536V620','none','#DCF3E7',3)
    a+=p('M244 629L347 620L358 638L250 650L233 636Z','#0870A0')
    a+=p('M264 859V790Q288 758 314 786V854Z','#8B73C0')
    a+=p('M250 868L328 858L351 882L266 894L237 880Z','#E9C7A1')
    a+=p('M237 880V893L266 908L351 895V882M230 899L266 920L362 904V917L266 935L222 913Z','#F5DCB9')
    a+=p('M451 530L479 549V598L451 581Z','#9ACCD3')+p('M451 681L479 700V749L451 732Z','#A1CDB6')
    # Fold joins physically connect architecture and paper rather than floating on a pedestal.
    a+=p('M157 871L136 913L177 900Z','#E9D3AC')+p('M421 846L465 915L501 879Z','#E2C295')
    a+='</g>'
    a+=p('M463 896L489 876L512 888L486 910Z','#FFCB75')
    rig=mascot('v205',497,827,1.03)
    rig=rig.replace('M0 0Q-27-8-43-31','M0 0Q-28-2-36-24').replace('cx="-43" cy="-31"','cx="-36" cy="-24"')
    a+=rig
    return a,'MALTA','#FFF0E5'

def token(x,y,typ):
    a=e(x,y+10,34,19,'#E1B767')+e(x,y,34,19,'#FFDA8A')
    if typ=='home':a+=p(f'M{x-16} {y-2}V{y-28}L{x} {y-42}L{x+16} {y-28}V{y-2}Z','#FFF7DC')+p(f'M{x-21} {y-27}L{x} {y-46}L{x+22} {y-27}','none','#9A6D50',3)
    elif typ=='office':
        a+=r(x-14,y-45,28,45,'#A6D6DE')
        a+=p(f'M{x-6} {y-34}H{x+6}M{x-6} {y-23}H{x+6}M{x-6} {y-12}H{x+6}','none','#087BC1',3)
    else:a+=e(x,y-24,18,23,'#FFCE75')+p(f'M{x-7} {y-24}L{x} {y-33}L{x+7} {y-24}L{x} {y-15}Z','#FFF9E6')
    return a

def scene09():
    a=p('M87 431L523 394L660 898L242 1030L66 915Z','#ECD4B4')
    a+=p('M66 915L242 1030L660 898V921L242 1050L66 937Z','#C8A47D')
    a+=p('M105 459L505 425M128 499L517 462M150 542L531 501','none','#E0BF99',2)
    # Splitter is a real mechanical hub, not a data-card layout.
    a+=p('M214 537C437 485 352 664 510 720M214 537C71 654 131 815 220 909','none','#B79D8F',30)
    a+=p('M214 537C437 485 352 664 510 720M214 537C71 654 131 815 220 909','none','#FFFCED',20)
    a+=p('M214 537C437 485 352 664 510 720M214 537C71 654 131 815 220 909','none','#8EBDD0',3)
    a+=e(214,534,62,44,'#DAB991')+e(214,523,62,44,'#FFF4DB')
    a+=p('M202 545L198 502L244 478L253 499L218 526L222 548Z','#A990D5')+e(211,528,9,7,'#FFCD74')
    a+=p('M90 468L150 412L269 443L242 493L130 513Z','#FFF3D9')+p('M90 468L130 513V535L91 491Z','#DDBA8E')
    # Three different open physical groupings, with small architecture and money sharing one surface.
    for x,y,col in [(420,460,'#D9CBEA'),(525,751,'#B9DBDF'),(235,948,'#C9DFC4')]:
        a+=e(x,y+12,94,43,col)+e(x,y,94,43,'#FFF9EB')
    a+=building(350,326,.65,'#E8CCAB')+token(447,449,'capital')+token(493,454,'home')
    a+=building(468,608,.62,'#EED6B2')+token(555,741,'office')+token(596,737,'capital')
    a+=building(164,806,.62,'#EFD7B7')+token(253,941,'home')+token(302,934,'capital')
    a+=p('M363 384Q372 374 383 384Q395 397 406 384M574 621Q585 611 596 621Q608 634 619 621M280 811Q292 801 303 811Q316 824 327 811','none','#B97A4C',3)
    # Contact hardware and small engraved screws make the surface materially legible.
    for x,y in [(107,452),(504,418),(638,887),(238,1022)]:a+=e(x,y,4,4,'#D0AE84')
    return a,'NHIỀU THỊ TRƯỜNG','#F0EAFB'

def main():
    if OUT.exists():raise RuntimeError('New revision folder already exists; do not overwrite.')
    for sid,fn in [('S05',scene05),('S09',scene09)]:
        d=OUT/sid;(d/'assets').mkdir(parents=True)
        for source,name in [(ROOT/'assets/fonts/segoe-ui-black.ttf','display.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(source,d/'assets'/name)
        if sid=='S05':shutil.copy2(ROOT/'assets/valletta.jpg',d/'assets/valletta.jpg')
        art,title,bg=fn();title=title.encode('ascii','xmlcharrefreplace').decode('ascii')
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280"><defs><filter id="shadow" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="10" stdDeviation="6" flood-color="#77636B" flood-opacity=".16"/></filter></defs>{art}</svg>'
        (d/'art.svg').write_text(svg,encoding='utf-8')
        comp='final-'+sid.lower()
        html=f'''<!doctype html><html lang="vi"><meta charset="utf-8"><script src="assets/gsap.min.js"></script><style>@font-face{{font-family:Display;src:url('assets/display.ttf');font-weight:900}}*{{box-sizing:border-box}}html,body{{width:100%;height:100%;margin:0;overflow:hidden}}#{comp}{{position:relative;width:100%;height:100%;background:{bg}}}svg{{position:absolute;inset:0}}h1{{position:absolute;left:50px;top:160px;width:620px;margin:0;text-align:center;color:#0870AC;font-family:Display,sans-serif;font-size:{68 if sid=='S05' else 44}px;font-weight:900;line-height:1.3}}</style><div id="{comp}" data-composition-id="{comp}" data-width="720" data-height="1280" data-duration="1">{svg}<h1>{title}</h1></div><script>const tl=gsap.timeline({{paused:true}});tl.to({{hold:0}},{{hold:1,duration:1}});window.__timelines['{comp}']=tl;</script></html>'''
        (d/'index.html').write_text(html,encoding='utf-8')
        (d/'hyperframes.json').write_text(json.dumps({'authoringSkill':'general-video','media':{'autoProxy':False}}),encoding='utf-8')
    (OUT/'README.md').write_text('# Proposed final frames v2\n\nS05: residential paper architecture unfolds from the photo edge; not the church in the geographic photo. S09: material allocation table, mechanical splitter, curved channels and richer asset groupings. Static final-state proposals only, awaiting user approval. Existing pilots, storyboard and narration remain untouched. Exact motion/contact during action has not been validated by these stills.\n',encoding='utf-8')
    print(OUT)
if __name__=='__main__':main()
