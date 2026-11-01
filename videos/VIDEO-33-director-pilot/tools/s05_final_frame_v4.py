"""Redesign S05 as an inhabitable street vignette, not a house/paper mechanism."""
import json,shutil
from prepare import ROOT
from final_frames_v2 import p,r,e
from build_pilots import mascot

OUT=ROOT/'revisions/S05-final-frame-v4'

def scene():
    # A shared pavement anchors every building/character. The bottom 200px stays clear.
    a=p('M47 955L443 915L681 1013L672 1069H48Z','#E8DFD6','none',0)
    a+=p('M48 1021L440 971L679 1014M213 1000L260 1068M393 977L509 1068M541 999L638 1068','none','#C9BDB0',2)
    a+=p('M429 916L455 804L533 787L596 975Z','#F4EDE1','none',0)
    # Neighbouring residence is a setting plane at the edge, not another display model.
    a+=p('M537 472L676 405V1007L537 944Z','#F3DFCA')
    a+=p('M525 461L676 388V411L537 482Z','#FFF3DF')
    for y in [533,593,653,713,773,833,893]:a+=p(f'M539 {y}L675 {y-64}','none','#DDC5AC',1.4)
    a+='<g id="neighbour-balcony">'
    a+=p('M552 553L625 517L647 531V647L573 685L552 665Z','#AB98CB')
    a+=p('M573 570L647 531V647L573 685Z','#927AB8')
    a+=p('M546 547L625 506L656 526L648 539L573 579L549 563Z','#C8B5E3')
    a+=p('M581 579L600 568V616L581 627ZM610 563L636 550V596L610 610Z','#E6EFF0','#6D5B8C',2)
    a+=p('M568 686L649 643L656 655L576 700L550 680V666Z','#B7A1D3')+'</g>'
    a+=p('M574 956V823Q578 789 601 780Q629 764 629 797V980Z','#89AEB1')
    a+=p('M587 844L614 830M587 860L614 846M587 876L614 862','none','#D6E5DE',2)
    # Main facade extends to a real curb and is composed as architecture, not an isolated cube.
    a+='<g id="street-residence">'
    a+=p('M55 374L389 403V1000L55 1019Z','#F3DEB9')
    a+=p('M389 403L432 425V1009L389 1000Z','#DCC5A5')
    for row,y in enumerate(range(424,1006,49)):
        a+=p(f'M57 {y}L388 {y+28}','none','#D8C09D',1.5)
        for x in ([123,246,351] if row%2==0 else [181,302]):
            yy=y+(x-57)*28/331
            a+=p(f'M{x} {yy:.1f}V{yy+48:.1f}','none','#D8C09D',1.3)
    a+=p('M43 351L391 382L447 410L434 431L389 416L43 386Z','#FDEED3')
    a+=p('M43 351L391 382L447 410L437 418L389 398L43 369Z','#FFF7E7')
    a+=p('M55 405L389 434L431 452','none','#C9AF8B',3)
    # Enclosed timber balcony is part of this facade, at a believable scale above the entrance.
    a+='<g id="green-timber-balcony">'
    a+=p('M105 477L132 452L336 470L354 491L130 478Z','#A5CABB')
    a+=p('M105 477L130 491V631L105 617Z','#387B70')
    a+=p('M130 491L354 507V647L130 631Z','#448F7B')
    a+=p('M97 469L130 443L341 462L364 488L355 506L130 487L100 487Z','#2E675E')
    a+=p('M99 468L132 454L349 473L364 488L130 478Z','#ABD1BC')
    for j in range(4):
        x=141+j*52;y=503+j*3.7
        a+=p(f'M{x} {y+14}Q{x+17} {y-7} {x+35} {y+17}V{y+74}L{x} {y+71}Z','#C8E2D7','#275950',2)
        a+=p(f'M{x+17} {y+3}V{y+73}M{x} {y+40}L{x+35} {y+43}','none','#689D8A',1.8)
        a+=p(f'M{x} {y+81}L{x+35} {y+84}V{y+109}L{x} {y+106}Z','#77AF93','#275950',2)
        a+=p(f'M{x+5} {y+89}L{x+29} {y+91}M{x+5} {y+97}L{x+29} {y+99}','none','#4B8E73',1.2)
    a+=p('M106 499L120 507V593L106 586Z','#BEDCCF','#275950',2)
    a+=p('M103 619L129 634L358 651L363 667L131 651L99 636Z','#397466')
    a+=p('M131 651L363 667V676L131 661L99 647V636Z','#93B99E')
    for x,y in [(151,665),(244,671),(333,678)]:a+=p(f'M{x} {y}L{x+21} {y+1}Q{x+21} {y+22} {x+5} {y+31}L{x} {y+26}Z','#E8CEA9','#B49A78',2)
    a+='</g>'
    # Tall recessed door: frames, jamb and attached threshold, no disembodied stairs.
    a+=p('M219 1007V785Q219 704 292 699Q370 695 370 778V997Z','#FCECD0','#B99B77',3)
    a+=p('M234 1003V786Q234 722 293 717Q356 712 356 778V995Z','#6AA3A4')
    a+=p('M238 781Q241 730 293 729Q345 726 352 776Z','#C6DCD2','#416F71',2)
    a+=p('M293 730V779M250 747L273 779M337 744L313 779','none','#81A69C',2)
    a+=p('M238 792L352 788V995L238 1002Z','#117D91')
    a+=p('M295 792V998','none','#9AC4BC',2)
    for x in [249,307]:
        a+=p(f'M{x} 812H{x+33}V875L{x} 877ZM{x} 896L{x+33} 894V970L{x} 973Z','#468FA0','#115E75',2)
    a+=e(344,851,4.5,4.5,'#E9BD68')
    a+=p('M226 1009L367 998L379 1009L233 1022Z','#D8BE9A','#A78F71',2)
    # Left window and shutters read as physical residential details, not labelled icon panels.
    a+=r(73,741,110,153,'#EAD2AD',2)+r(83,752,90,131,'#DCE9DF',1)
    a+=p('M128 754V881M84 808H172','none','#8EA89C',2.5)
    a+=p('M58 749L83 755V881L58 889Z','#9BBA9D')+p('M173 755L195 745V893L173 881Z','#79A58D')
    for y in range(766,873,15):a+=p(f'M63 {y}L77 {y+3}M178 {y+1}L190 {y-3}','none','#4F7F70',1.7)
    a+=p('M69 895L185 892L197 903L74 910Z','#FFF0D3','#B59A76',2)
    a+=p('M47 1020L391 1001L433 1013L397 1030L49 1044Z','#D9C7B1','#AA947D',2)
    a+='</g>'
    # A real planted pot is grounded beside the window, with restrained foliage.
    a+=p('M81 996L89 1031H124L133 996Z','#D78D72','#8C6757',2)
    a+=e(107,995,27,7,'#F0B392')
    a+=p('M108 992V938M108 964Q80 950 84 931Q112 934 108 964M109 977Q139 966 138 948Q114 950 109 977M107 948Q101 926 117 918Q128 939 107 948Z','#87AF83','#517C65',2)
    # Mascot considers the residence, using a plan rather than magically producing a building.
    rig=mascot('s05v4',460,800,1.15)
    rig=rig.replace('M0 0Q-27-8-43-31','M0 0Q-63-22-120-29').replace('cx="-43" cy="-31"','cx="-120" cy="-29"')
    rig=rig.replace('M0 0Q20 24 38 7','M0 0Q-8 34-37 52').replace('cx="38" cy="7"','cx="-37" cy="52"')
    rig=rig.replace('id="s05v4-eyes"','id="s05v4-eyes" transform="translate(-3 -3)"')
    plan='<g id="folded-viewing-plan">'+p('M-64 128L0 112L72 128V190L0 174L-64 190Z','#FFFCF1','#30313B',2.2)+p('M0 114V174','none','#C9BEA6',2)+p('M-52 139L-12 130V166L-52 176ZM-33 135V171M-52 156L-33 151','none','#71999B',1.6)+p('M14 135L58 145V173L14 163ZM23 138V166M44 143V171','none','#71999B',1.6)+'</g>'
    rig=rig.replace('<g transform="translate(109 83)">',plan+'<g transform="translate(109 83)">',1)
    a+=rig
    return a

def main():
    if OUT.exists():raise RuntimeError('New v4 folder already exists; do not overwrite')
    (OUT/'assets').mkdir(parents=True)
    for src,name in [(ROOT/'assets/fonts/segoe-ui-black.ttf','display.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(src,OUT/'assets'/name)
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280">'+scene()+'</svg>'
    (OUT/'art.svg').write_text(svg,encoding='utf-8')
    html='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>S05 final frame v4</title><script src="assets/gsap.min.js"></script><style>@font-face{font-family:Display;src:url('assets/display.ttf');font-weight:900;font-display:block}html,body{width:100%;height:100%;margin:0;overflow:hidden}#s05-v4{position:relative;width:100%;height:100%;background:#FFF8E9;overflow:hidden}svg{position:absolute;inset:0}h1{position:absolute;left:60px;top:163px;width:600px;margin:0;text-align:center;font:900 64px/1.3 Display,sans-serif;color:#0870AC}</style></head><body><div id="s05-v4" data-composition-id="s05-v4" data-width="720" data-height="1280" data-duration="1">'''+svg+'''<h1>MALTA</h1></div><script>const tl=gsap.timeline({paused:true});tl.to({hold:0},{hold:1,duration:1});window.__timelines['s05-v4']=tl;</script></body></html>'''
    (OUT/'index.html').write_text(html,encoding='utf-8')
    (OUT/'hyperframes.json').write_text(json.dumps({'authoringSkill':'general-video','media':{'autoProxy':False}}),encoding='utf-8')
    (OUT/'DESIGN.md').write_text('# S05 final frame v4 · NEW PROPOSAL, not approved\n\nA close residential street vignette. The house is part of an inhabitable streetscape, anchored to continuous paving and a neighbouring facade. Orange mascot holds an illustrative folded plan and compares it with the entrance. No key, contract, transaction, citizenship or ownership claim. No separate house model in front of a photograph, popup struts, paper hinges or morphing architecture.\n\nCream ground, sandstone/peach wall, green timber gallery, blue entrance, lilac secondary gallery, thin neutral outlines. The original approved mascot and local Segoe UI Black remain. Photography is intentionally omitted: a separate photo panel would recreate the rejected display-model setup. The street and plan are invented illustration, not an actual property/listing or certified floor plan.\n\nOnly one static proposed final frame is authorized here. Voice, original inputs, prior renders and S09 are unchanged. No new animation/full film. If approved, choreograph a viewing/comparison gesture in the existing street rather than constructing a house magically.\n',encoding='utf-8')
    print(OUT)

if __name__=='__main__':main()
