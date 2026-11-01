"""S05 still v5: a genuine house photograph in an ordinary viewing album."""
import json,shutil,re,hashlib
from prepare import ROOT,digest
from final_frames_v2 import p,r,e
from build_pilots import mascot

OUT=ROOT/'revisions/S05-final-frame-v5'

def scene():
    art='''<defs><filter id="paper-shadow" x="-20%" y="-20%" width="150%" height="160%"><feDropShadow dx="0" dy="7" stdDeviation="5" flood-color="#7C6C62" flood-opacity=".14"/></filter><clipPath id="photo-spread"><path d="M96 637L338 645L350 637L366 642L614 631L618 923L366 936L350 930L335 938L91 930Z"/></clipPath><clipPath id="arms-over-table"><rect x="0" y="548" width="720" height="130"/></clipPath></defs>'''
    # The chair is behind the seated character; the tabletop will occlude lower torso/legs.
    art+=r(479,394,160,218,'#E7DCF1',25)+p('M495 418Q556 400 624 418','none','#BAA3CD',3)
    rig=mascot('s05v5',475,418,1.10)
    rig=rig.replace('M0 0Q-27-8-43-31','M0 0Q-35 59-20.45455 84.36364').replace('cx="-43" cy="-31"','cx="-20.45455" cy="84.36364"')
    rig=rig.replace('M0 0Q20 24 38 7','M0 0Q27 46 13.72727 77.90909').replace('cx="38" cy="7"','cx="13.72727" cy="77.90909"')
    rig=rig.replace('id="s05v5-eyes"','id="s05v5-eyes" transform="translate(-3 5)"')
    # A seated reader does not cast the standing-floor shadow from the old rig.
    rig=re.sub(r'<ellipse id="s05v5-student-shadow"[^>]*/>','',rig)
    far=re.search(r'<g transform="translate\(25 72\)"><g id="s05v5-arm-far"[^>]*>.*?</g></g>',rig,re.S).group(0)
    near=re.search(r'<g transform="translate\(109 83\)"><g id="s05v5-arm-near"[^>]*>.*?</g></g>',rig,re.S).group(0)
    art+=rig
    # One continuous table surface supports the entire album.
    art+='<g id="viewing-table">'
    art+=p('M71 560H649L682 993L38 993Z','#E4C5A5')
    art+=p('M38 993H682V1011H38Z','#C7A17F')
    art+=p('M83 1011H112L106 1068H85ZM608 1011H637L638 1068H615Z','#D4B18C')
    art+=p('M91 575H626M54 973H661','none','#D4AE86',2)
    art+='</g>'
    art+='<g id="open-viewing-album" filter="url(#paper-shadow)">'
    # Blue hard cover, visible page stack, curved spread/gutter; all are one physical book.
    art+=p('M69 592L341 606L634 584L647 952L349 983L61 963Z','#087BC1')
    art+=p('M74 590L341 603L629 582L640 946L350 976L66 957Z','#E1D4BD')
    art+=p('M70 582Q202 571 348 601V962Q203 940 65 951Z','#FFFEF3')
    art+=p('M350 601Q491 574 629 577L639 942Q494 935 350 962Z','#FFFCF0')
    art+=p('M79 949Q212 943 340 965M363 966Q496 942 630 948','none','#C8BAA1',2)
    art+='<image id="house-photo" href="assets/townhouse.jpg" x="91" y="619" width="530" height="322" preserveAspectRatio="xMidYMid slice" clip-path="url(#photo-spread)"/>'
    # The two-page print continues across the binding. The crease belongs to the album.
    art+=p('M348 605L350 960','none','#C8B99B',5)
    art+=p('M353 610L355 953','none','#FFF9E8',2)
    # Corners secure the photographic print; no fabricated listing labels or floor plans.
    art+=p('M94 636L117 638L93 659Z','#D5C1A1','none',0)
    art+=p('M594 633L615 631L616 653Z','#D5C1A1','none',0)
    art+=p('M92 907L111 930L91 930ZM597 925L618 903L618 923Z','#D5C1A1','none',0)
    # A normal lifted paper corner, pinched by the near hand. No architectural shape changes.
    art+=p('M608 578L629 577L630 612Z','#E5D6BC','#B4A58C',1.8)
    art+='</g>'
    # Restore only the parts of the arms over the tabletop/pages. The upper arms stay behind torso.
    art+='<g clip-path="url(#arms-over-table)"><g transform="translate(475 418) scale(1.10)">'+far+near+'</g></g>'
    return art

def main():
    if (OUT/'index.html').exists():raise RuntimeError('v5 source already exists; refuse to overwrite')
    if not (OUT/'assets/townhouse.jpg').exists():raise RuntimeError('Download the credited photo before authoring')
    for src,name in [(ROOT/'assets/fonts/segoe-ui-black.ttf','display.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(src,OUT/'assets'/name)
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280">'+scene()+'</svg>'
    (OUT/'art.svg').write_text(svg,encoding='utf-8')
    page='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>S05 final frame v5</title><script src="assets/gsap.min.js"></script><style>@font-face{font-family:Display;src:url('assets/display.ttf');font-weight:900;font-display:block}html,body{width:100%;height:100%;margin:0;overflow:hidden}#s05-v5{position:relative;width:100%;height:100%;background:#FFF3E8;overflow:hidden}svg{position:absolute;inset:0}h1{position:absolute;left:60px;top:164px;width:600px;text-align:center;margin:0;color:#0870AC;font:900 64px/1.3 Display,sans-serif}</style></head><body><div id="s05-v5" data-composition-id="s05-v5" data-width="720" data-height="1280" data-duration="1">'''+svg+'''<h1>MALTA</h1></div><script>const tl=gsap.timeline({paused:true});tl.to({hold:0},{hold:1,duration:1});window.__timelines['s05-v5']=tl;</script></body></html>'''
    (OUT/'index.html').write_text(page,encoding='utf-8')
    (OUT/'hyperframes.json').write_text(json.dumps({'authoringSkill':'general-video','media':{'autoProxy':False}}),encoding='utf-8')
    credit={'asset':'assets/townhouse.jpg','title':'Townhouse in Zejtun.jpg','author':'Marika Caruana','source':'https://commons.wikimedia.org/wiki/File:Townhouse_in_Zejtun.jpg','license':'CC BY-SA 4.0','license_url':'https://creativecommons.org/licenses/by-sa/4.0/','modifications':'Cropped into a two-page album spread; no generative changes.','sha256':digest(OUT/'assets/townhouse.jpg'),'purpose':'Architectural context for Malta; not an actual property listing, client property, or claim that this house is available for purchase.'}
    (OUT/'CREDITS.json').write_text(json.dumps(credit,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'CREDITS.md').write_text('# Photo credit\n\n“Townhouse in Zejtun.jpg” — Marika Caruana, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Townhouse_in_Zejtun.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Cropped within an illustrated album spread. No endorsement or property-sale claim. Preserve credit and applicable share-alike terms on redistribution.\n\nThe unused Houseofmalta.jpg candidate is by Dronehyven, same license; it is not displayed because it includes a visible watermark. Its original file is preserved untouched.\n',encoding='utf-8')
    (OUT/'DESIGN.md').write_text('# S05 final frame v5 · pending review\n\nMeaning: considering a property connection with Malta. Scene: a seated mascot studies an ordinary open photographic album on a single table. The genuine Maltese house photograph is printed in the spread. One hand rests on the page margin, the other pinches a small page corner. Hands operate only on paper. Chair, reader, tabletop, album and foreground forearms are ordered explicitly for occlusion.\n\nA house does not grow, fold or emerge as a 3D object. This is a new static design only; no video revision and no changes to original audio, previous sources or S09. Any later animation should be normal looking / page handling / comparison, with the photographic house remaining a print throughout. No fake listing, price, contract or certified plan.\n',encoding='utf-8')
    print(OUT)

if __name__=='__main__':main()
