"""S05 residential corner and enclosed timber balcony: final-state proposal v3."""
from pathlib import Path
import shutil,json
from prepare import ROOT
from final_frames_v2 import p,r,e,I
from build_pilots import mascot

OUT=ROOT/'revisions/S05-final-frame-v3'

def scene():
    a='''<defs><clipPath id="photo"><path d="M80 330L601 313L628 621L103 646Z"/></clipPath><filter id="soft" x="-30%" y="-30%" width="170%" height="180%"><feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#7B6361" flood-opacity=".16"/></filter></defs>'''
    a+=p('M65 314L612 294L646 633L90 665Z','#FFFDF5')
    a+='<image href="assets/valletta.jpg" x="76" y="307" width="563" height="350" preserveAspectRatio="xMidYMid slice" clip-path="url(#photo)"/>'
    # One continuous folded page and two connected walls; no triangular struts.
    a+=p('M86 927L430 899L559 969L204 1030Z','#FFFAEA')
    a+=p('M430 899L430 997M86 927L204 1030','none','#DBC8AC',2)
    a+='<g filter="url(#soft)">'
    a+=p('M107 449L431 422V922L107 954Z','#F1D9B1')
    a+=p('M431 422L505 470V960L431 922Z','#DEBF96')
    # Limestone masonry: staggered joints, low contrast, under the architectural details.
    for y in range(488,936,48):
        off=(y-488)//48%2
        a+=p(f'M109 {y}L430 {y-27}','none','#D7BC93',1.5)
        for x in ([164,283,390] if off else [219,337]):
            yy=y-(x-109)*27/321
            a+=p(f'M{x} {yy:.1f}V{yy+46:.1f}','none','#D7BC93',1.3)
    for y in (528,624,720,816,912):a+=p(f'M432 {y-27}L503 {y+19}','none','#C7A77E',1.5)
    # A stepped stone cornice makes the two planes read as a street corner.
    a+=p('M94 428L430 399L520 456L508 480L431 438L94 468Z','#FCECD0')
    a+=p('M97 428L430 399L520 456L508 464L430 416L97 447Z','#FFF6E1')
    a+=p('M107 479L431 451L505 495','none','#CBB08C',3)
    # Hero enclosed timber gallery, projected beyond the wall with visible depth.
    a+=p('M144 554L181 525L389 509L409 532L181 554Z','#83B5A3')
    a+=p('M144 554L181 554V734L144 714Z','#2D796D')
    a+=p('M181 554L409 532V711L181 734Z','#3C8B79')
    a+=p('M135 548L178 516L399 499L420 526L409 539L181 562L139 561Z','#285E58')
    a+=p('M140 548L181 526L407 507L420 526L181 550Z','#A5CEB7')
    # Tall glazed bays, square frames and arched fanlights; these are not pill windows.
    for j in range(4):
        x=193+j*53; y=565-j*5.2
        a+=p(f'M{x} {y+20}Q{x+19} {y-8} {x+38} {y+16}V{y+83}L{x} {y+87}Z','#BFDBD3','#234F4C',2)
        a+=p(f'M{x+19} {y+6}V{y+85}M{x} {y+43}L{x+38} {y+39}','none','#4A8073',2)
        a+=p(f'M{x} {y+97}L{x+38} {y+93}V{y+135}L{x} {y+139}Z','#73AB93','#234F4C',2)
        a+=p(f'M{x+6} {y+107}L{x+31} {y+104}M{x+6} {y+116}L{x+31} {y+113}M{x+6} {y+125}L{x+31} {y+122}','none','#44866F',1.5)
    a+=p('M156 580L170 570V684L156 677Z','#A9CBC2','#234F4C',2)
    a+=p('M173 734L414 710L426 729L179 755L143 735L144 719Z','#386D5F')
    a+=p('M179 755L426 729V741L179 768L143 746V735Z','#8BB39B')
    # Stone corbels connect the gallery to its supporting wall.
    for x,y in [(194,769),(279,761),(368,750)]:
        a+=p(f'M{x} {y}H{x+24}Q{x+23} {y+31} {x+7} {y+43}L{x} {y+39}Z','#E8CEA5','#A68B6C',2)
    # Ground-floor door with a stone surround and a fanlight, one attached threshold.
    a+=p('M149 949V846Q149 792 203 789Q257 784 257 835V938Z','#FCEAC8','#BBA07E',3)
    a+=p('M162 947V846Q162 803 203 801Q244 797 244 838V939Z','#087B89')
    a+=p('M165 845L242 838M203 803V842','none','#90C7C3',2.5)
    a+=p('M173 859L193 857V922L173 924ZM213 855L233 853V918L213 920Z','#4B9E9D','#25696F',2)
    a+=e(229,891,3.1,3.1,'#F0C36E')
    a+=p('M151 949L252 939L262 950L158 962Z','#DFC39B','#A68B6C',2)
    # Narrow side wall with a recessed window, shutter and projecting stone sill.
    a+=p('M450 583L486 605V687L450 665Z','#C5A780','#AE8B65',2)
    a+=p('M457 596L480 610V673L457 659Z','#B6D6CE','#5F8173',2)
    a+=p('M451 671L489 693L495 687L457 665Z','#F8E4BF','#A78B69',2)
    a+=p('M447 771L487 797V881L447 857Z','#668E79')
    for y in range(787,851,10):a+=p(f'M453 {y}L482 {y+18}','none','#ABC2A3',2)
    a+='</g>'
    # The pull tab grows from the single lower paper fold, not a detached support.
    a+=p('M469 909L483 873L507 884L493 921Z','#FFD183')
    a+=p('M481 895L493 901','none','#D3A15D',2)
    rig=mascot('s05v3',508,818,1.03)
    rig=rig.replace('M0 0Q-27-8-43-31','M0 0Q-23 0-39-7').replace('cx="-43" cy="-31"','cx="-39" cy="-7"')
    # Eyes look at the architecture, instead of facing the viewer without purpose.
    rig=rig.replace(f'id="s05v3-eyes"',f'id="s05v3-eyes" transform="translate(-3 -4)"')
    a+=rig
    return a

def main():
    if OUT.exists():raise RuntimeError('Refusing to overwrite v3')
    (OUT/'assets').mkdir(parents=True)
    for src,name in [(ROOT/'assets/fonts/segoe-ui-black.ttf','display.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js'),(ROOT/'assets/valletta.jpg','valletta.jpg')]:shutil.copy2(src,OUT/'assets'/name)
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280">{scene()}</svg>'
    (OUT/'art.svg').write_text(svg,encoding='utf-8')
    (OUT/'index.html').write_text('''<!doctype html><html lang="vi"><head><meta charset="utf-8"><script src="assets/gsap.min.js"></script><style>@font-face{font-family:Display;src:url('assets/display.ttf');font-weight:900}html,body{width:100%;height:100%;margin:0;overflow:hidden}#s05-v3{position:relative;width:100%;height:100%;background:#FFF0E5}svg{position:absolute;inset:0}h1{position:absolute;left:60px;top:162px;width:600px;text-align:center;margin:0;color:#0870AC;font:900 68px Display,sans-serif;line-height:1.3}</style></head><body><div id="s05-v3" data-composition-id="s05-v3" data-width="720" data-height="1280" data-duration="1">'''+svg+'''<h1>MALTA</h1></div><script>const tl=gsap.timeline({paused:true});tl.to({hold:0},{hold:1,duration:1});window.__timelines['s05-v3']=tl;</script></body></html>''',encoding='utf-8')
    (OUT/'hyperframes.json').write_text(json.dumps({'authoringSkill':'general-video','media':{'autoProxy':False}}),encoding='utf-8')
    (OUT/'REVISION.md').write_text('# S05 final frame v3 · awaiting review\n\nReplaces the rejected v2 house proposal only. Large enclosed green timber balcony, limestone joints, stone cornice/corbels, rectangular glazing and a ground-floor door. Two joined architectural planes, one paper fold, no detached stairs or triangle struts. Geographic photo remains separate from the invented residential facade. Original pilot, S09 proposal and narration untouched. Static final state; contact throughout motion still requires animation review.\n',encoding='utf-8')
    print(OUT)
if __name__=='__main__':main()
