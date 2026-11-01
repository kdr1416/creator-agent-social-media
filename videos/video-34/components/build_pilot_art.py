"""Original SVG artwork for VIDEO-34 S03/S08. Run from any working directory.
No remote assets, generation services or additional Python packages.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'assets' / 'illustration'
ART.mkdir(parents=True, exist_ok=True)

def path(d, fill, extra=''):
    return f'<path d="{d}" fill="{fill}" {extra}/>'

def line(d, color, width=3, extra=''):
    return path(d, 'none', f'stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}')

def ellipse(x,y,rx,ry,fill,extra=''):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" {extra}/>'

def group(content, transform='', id=''):
    return f'<g'+(f' id="{id}"' if id else '')+(f' transform="{transform}"' if transform else '')+f'>{content}</g>'

DEFS='''<defs>
 <linearGradient id="sky" x2="0" y2="1"><stop stop-color="#dce9e2"/><stop offset="1" stop-color="#fcf0d9"/></linearGradient>
 <linearGradient id="sea" x1="0" y1="0" x2=".8" y2="1"><stop stop-color="#83b8b6"/><stop offset=".65" stop-color="#438d98"/><stop offset="1" stop-color="#2c6a7d"/></linearGradient>
 <linearGradient id="stone" x2=".8" y2="1"><stop stop-color="#f5dfb7"/><stop offset="1" stop-color="#d4ad80"/></linearGradient>
 <linearGradient id="plaster" x2="1" y2=".5"><stop stop-color="#eee1c8"/><stop offset="1" stop-color="#d8c9aa"/></linearGradient>
 <linearGradient id="floor" x2=".5" y2="1"><stop stop-color="#e8c49a"/><stop offset="1" stop-color="#f5dfbd"/></linearGradient>
 <linearGradient id="shirt" x2="1" y2="1"><stop stop-color="#fff0d6"/><stop offset="1" stop-color="#d7c6a8"/></linearGradient>
 <radialGradient id="sunwash"><stop stop-color="#fff7dd" stop-opacity=".55"/><stop offset="1" stop-color="#fff7dd" stop-opacity="0"/></radialGradient>
 <pattern id="paper" width="37" height="43" patternUnits="userSpaceOnUse"><circle cx="3" cy="8" r=".7" fill="#614d3b" opacity=".08"/><circle cx="26" cy="33" r=".55" fill="#fff" opacity=".28"/><path d="M13 20h2m18-16h1" stroke="#7b674b" stroke-opacity=".07"/></pattern>
</defs>'''

def svg(body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 1280" role="img" aria-label="{title}">{DEFS}{body}<path d="M0 0H720V1280H0Z" fill="url(#paper)" pointer-events="none"/></svg>'

def balcony(x,y,w=110,color='#416e6a'):
    s=path(f'M{x} {y}h{w}v108l-14 15h-{w-12}Z',color)
    s+=path(f'M{x+w} {y}l16-11v107l-16 15Z','#284c4f')
    s+=path(f'M{x-8} {y-9}h{w+12}l13-8h-{w+7}Z','#668a7b')
    for xx in range(int(x+9),int(x+w-8),25):
        s+=path(f'M{xx} {y+7}h18v67h-18Z','#b2bca0')
        s+=line(f'M{xx+9} {y+8}v66m-9-35h18',color,2)
    s+=path(f'M{x+5} {y+84}h{w-10}v17h-{w-10}Z','#345b59')
    s+=path(f'M{x-7} {y+110}h{w+17}v12h-{w+17}Z','#e8c89b')
    return s

def window(x,y,w=48,h=82):
    return path(f'M{x} {y+h}V{y+20}q{w/2}-{39} {w} 0v{h-20}Z','#315258')+line(f'M{x+w/2} {y+2}v{h-5}m-{w/2} -{h/2}h{w}', '#8a9c8c',2)+path(f'M{x-5} {y+h}h{w+10}v6h-{w+10}Z','#f6e0b8')

def plant(x,y,scale=1):
    c=path('M-23 0h46l-6 45h-32Z','#b76f50')+path('M-27-5h54v10h-54Z','#cd8967')
    c+=line('M0 0q-6-38 4-75m-3 61q-29-11-30-39m31 28q21-15 28-39','#416d5c',3)
    for d in ['M0-22q-30 7-36-23Q-5-53 0-22','M2-44q-14-22 4-45Q24-65 2-44','M3-28q4-33 34-34Q38-33 3-28','M-8-13q-30 3-35-18Q-20-39-8-13']:
        c+=path(d,'#52785c')
    return group(c,f'translate({x} {y}) scale({scale})')

def person(id,x,y,scale=1,shirt='#c66f52',pants='#304b58',hair='#303837',skin='#cf9975',facing=1):
    # Ground at local y=0; roughly 7-head adult silhouette, 162 SVG units tall.
    b=ellipse(0,1,29,6,'#504a3b','opacity=".15"')
    b+=group(line('M-7-66L-13-34 -18-7',pants,14)+path('M-25-8q11-4 18 0l3 8h-24Z','#344344'),'',id+'-leg-back')
    b+=group(line('M8-66L16-36 11-7',pants,15)+path('M5-8h14l12 6q0 4-27 2Z','#344344'),'',id+'-leg-front')
    b+=group(line('M-13-115L-29-91 -20-75',skin,9),'',id+'-arm-back')
    b+=path('M-16-126Q-1-132 16-122L23-71Q0-61-20-69Z',shirt)
    b+=path('M8-120q12 21 13 48l-9 2-4-48Z','#243b46','opacity=".13"')
    b+=path('M-7-139h14v16q-7 8-14 0Z',skin)
    b+=group(ellipse(0,-148,14,18,skin)+path('M-14-145q-8-22 10-24 23-4 20 17l-8-5q-7 6-22 2Z',hair)+path('M13-151l5 8h-6Z',skin)+ellipse(8,-151,1.3,1.7,'#393e3c')+line('M7-139q3 2 5-1','#9d634e',1.1),'',id+'-head')
    b+=group(line('M12-116L28-94 22-78',skin,10),'',id+'-arm-front')
    return group(group(b,f'scale({facing} 1)'),f'translate({x} {y}) scale({scale})',id)

def seated(id,x,y,scale,shirt,skin='#cd9978',flip=1):
    c=ellipse(0,0,40,7,'#77654c','opacity=".13"')
    c+=line('M-23-55v53m43-53v53M-30-112v57h55', '#63796d',5)
    c+=line('M-3-61L20-43 27-8', '#344d59',14)+path('M20-9h15l5 7H18Z','#344347')
    c+=path('M-15-117q19-10 31 2l3 55h-35Z',shirt)
    c+=ellipse(1,-138,14,18,skin)+path('M-13-137q-6-25 14-24 21 2 16 20l-16-8-12 12Z','#343e3b')
    c+=ellipse(11,-139,1.3,1.5,'#34413f')
    c+=line('M9-107l17 21 26-12',skin,10, f'id="{id}-arm"')
    return group(group(c,f'scale({flip} 1)'),f'translate({x} {y}) scale({scale})',id)

def coast():
    c=path('M0 0H720V1280H0Z','url(#sky)')
    c+=ellipse(530,165,175,175,'url(#sunwash)')
    c+=path('M0 441q178-15 328 7t392-13v845H0Z','url(#sea)')
    c+=path('M492 464l95-23 133 1v36l-94 0-88 16Z','#bbbaa1')
    # Distant Fort silhouette: deliberately unlabeled, not a site reconstruction.
    c+=path('M552 446v-31h12v-16h25v15h19v-23h37v28h23v-18h34v37h18v12Z','#b9b49a')
    c+=line('M450 514h96m49-21h73M481 565h39m37 16h83m-104 60h75M651 709h64M574 765h69','#c6ded0',2,'opacity=".65"')
    c+=path('M0 0h334v529l-87 90L0 694Z','url(#stone)')
    c+=path('M334 0l89 57v453l-89 19Z','#c3a178')
    c+=path('M0 79h334v16H0M0 296h334v13H0M0 509h334v12H0','#f8e6c4')
    for yy in [132,201,254,343,401,470,551,608]:
        c+=line(f'M0 {yy}H334','#bf9b71',1,'opacity=".38"')
    for x,y in [(43,151),(209,151),(55,360),(226,364)]: c+=window(x,y,51,88)
    c+=balcony(42,276,103,'#477f74')+balcony(213,79,96,'#355b6a')
    c+=path('M38 589v-45q0-47 44-47t44 47v38Z','#344d4c')
    c+=path('M189 570v-34q0-54 48-54t48 54v12Z','#3e5753')
    c+=path('M0 641L391 529 472 594 378 719 244 835 0 922Z','#b7a080')
    c+=path('M0 661L376 554 450 599 354 724 205 863 0 925Z','url(#floor)')
    c+=path('M0 924Q160 852 320 757T466 612L491 645Q417 790 303 879T0 1059Z','#f6dfb9')
    c+=path('M0 1018Q227 877 425 818T566 972Q517 1083 720 1149V1280H0Z','url(#floor)')
    c+=path('M0 1052Q256 901 440 846T541 981Q489 1082 720 1177','#b99772','fill-opacity="0" stroke="#b99772" stroke-width="12"')
    c+=path('M0 1040Q242 894 431 832T553 978Q507 1081 720 1160','none','stroke="#fff0d1" stroke-width="7"')
    # Small beach across the water, with a coherent family overlook in foreground.
    c+=path('M628 837q44-44 92-48v123q-51-7-92-75Z','#ead3a6')
    c+=line('M646 845q35 31 74 32','#e5ede0',4)
    for x,y in [(52,739),(151,711),(267,682),(350,629),(156,948),(274,915),(320,1040),(125,1160),(402,1190),(574,1210)]:
        c+=line(f'M{x} {y}l54-17m-25 8 9 23','#bb9d78',1.5,'opacity=".45"')
    # Café awning anchored to limestone facade, not an information panel.
    c+=path('M34 574L282 503 337 602 35 690Z','#e9d5ad')
    for i in range(6):
        x=34+i*42;y=574-i*12
        c+=path(f'M{x} {y}l21-6 55 99-26 8Z','#bd7057')
    c+=path('M35 690l302-88v16L35 707Z','#b7634d')
    c+=line('M51 703v106m266-181v122','#756b52',5)
    c+=plant(47,810,.72)+plant(340,668,.6)
    c+=seated('cafe-left',150,841,.85,'#627966')+seated('cafe-right',283,802,.8,'#c78662',flip=-1)
    c+=line('M173 775v73m58-88v73','#526660',4)
    c+=path('M140 770l90-28 40 21-92 29Z','#687f73')
    c+=path('M140 770v8l38 21 92-28v-8l-92 29Z','#3e615c')
    c+=group(ellipse(185,765,11,4,'#f6ebd3')+path('M177 752h15l-2 13h-10Z','#fcf0da')+line('M191 754q12-2 6 7h-6','#f6e7cb',2),'','cafe-cup')
    c+=person('friend-a',399,760,.69,'#bd7356')+person('friend-b',457,741,.69,'#d9c397',facing=-1)
    c+=person('walker-a',208,1044,1.1,'#e7d2a8')+person('walker-b',281,1011,.99,'#628270')
    c+=person('runner',397,967,1.03,'#be674e',pants='#344953')
    c+=person('family-parent',546,1168,.78,'#d7c098')+person('family-other',635,1198,.82,'#4e756b',facing=-1)
    c+=person('family-child',591,1182,.51,'#c78052',pants='#557b7a')
    c+=line('M558 1104L575 1117 582 1125M623 1128L611 1137 603 1143','#c89672',6,'id="family-link"')
    # Foreground leaves / edges frame the composition without hiding human action.
    c+=plant(30,1223,1.55)
    c+=path('M0 1260q68-21 134 20H0Z','#c49a71')
    c+=line('M460 374q10-9 20 0 10-9 20 0M548 319q7-7 14 0 7-7 14 0','#6f8e87',2)
    return svg(group(c,'','world').replace('id="world"','id="world" data-layout-allow-overflow'),'Original Malta-inspired promenade with café and families')

def home():
    c=path('M0 0H720V1280H0Z','url(#plaster)')
    c+=path('M341 130h379v838H341Z','#c0aa87')
    c+=path('M360 155h360v793H360Z','url(#sky)')
    c+=path('M360 522h360v426H360Z','url(#sea)')
    c+=path('M404 500l74-24 42 16 65-37 135 24v62H404Z','#d0bc96')
    c+=path('M420 490v-41h34v33m102-8v-39h25v26m63 12v-45h36v54','#bcae8e')
    c+=line('M481 575h88m29 34h91m-219 40h68','#c8e0d4',3)
    c+=path('M351 809l369-30v251H351Z','#e7d0ab')
    c+=path('M351 780l369-23v34l-369 29Z','#f6dfb8')
    for x in range(380,700,55): c+=path(f'M{x} 813h14v156h-14Z','#c4ab88')
    c+=path('M338 133h22v858h-22Z','#f8e8c8')+path('M353 133h13v858h-13Z','#bfa98a')
    c+=path('M720 970H0V1280H720Z','url(#floor)')
    c+=path('M365 797l355 21v462H119Z','#fff0cc','opacity=".42"')
    c+=path('M363 986l357-30v32l-357 26Z','#b49a79')
    c+=line('M0 1148l720-99M199 1280l254-290M542 1280l14-303','#c2a483',2,'opacity=".55"')
    c+=path('M22 218q136-37 233-10v319q-98-34-233 8Z','#ead8b7')
    c+=path('M40 239q106-26 195-6v256q-93-19-195 7Z','#9baf9e')
    c+=path('M40 403q72-112 124-20t71 4v102q-94-19-195 7Z','#69877c')
    c+=path('M40 458q104-94 195-2v33q-94-19-195 7Z','#d4b48c')
    c+=ellipse(176,287,22,22,'#f0d8a9')
    c+=path('M73 595h179v14H73Z','#9c795d')
    c+=path('M91 553h12v42H91Z','#728a7d')+path('M106 544h13v51h-13Z','#bd7c5a')+path('M124 560h13v35h-13Z','#d7bd91')
    c+=plant(210,588,.65)
    # Curtain folds and light remain quiet: no idle flutter loop.
    c+=path('M676 149h44v571q-24-26-51 2 25-238 7-573Z','#f3e8ce')
    c+=line('M699 174q-3 246-12 485','#dacfb4',3)
    c+=plant(654,999,1.6)
    c+=ellipse(327,1119,140,25,'#816b52','opacity=".15"')
    c+=ellipse(548,1125,67,13,'#816b52','opacity=".16"')
    # Grounded wooden chair with fixed four-point footprint.
    c+=line('M246 906l-30 210m152-209 34 207M252 1017h132','#7b654f',11)
    c+=path('M221 795q60-24 150 0l-9 122H237Z','#526e65')
    c+=path('M234 811q62-18 122 0l-6 80H245Z','#688476')
    c+=path('M235 905q79-17 143 3v21H235Z','#405e58')
    # Parent legs: pelvis remains seated while upper body turns toward child.
    c+=path('M283 891q45-15 73 20l-69 66 33 111-29 7-54-123q-5-16 10-29Z','#3d6262')
    c+=path('M322 910q28 1 45 18l38 49-20 115-29 6 14-107-66-43Z','#527777')
    c+=path('M288 1084l31 5 6 22-57 3q-8-8 20-30Z','#a96c4e')
    c+=path('M355 1084l31-3 26 23q5 13-55 9Z','#ab7052')
    c+=line('M270 1115h55m31 0h55','#ede0c0',4)
    c+=path('M279 718q33-20 69 8l30 174q-63 27-113-5l3-99Z','url(#shirt)', 'id="parent-torso"')
    c+=path('M344 750q-4 93 13 139l-26 14q-11-46-11-114Z','#c9b99b','opacity=".48"')
    c+=line('M297 741q7 61-6 111m-6 18 37 6','#c8b696',2)
    c+=path('M301 690h32v39q-9 17-32 0Z','#ce9575')
    # Far arm rests at desk. Near arm has explicit shoulder/elbow/wrist keyed poses.
    c+=line('M285 755Q268 784 269 812L240 832','#cc9576',24,'id="parent-far-arm"')
    c+=path('M275 738q-16 8-22 40l30 14 19-37Z','#eddfc2')
    c+=group('''<path d="M280 628q-19-42 18-55 45-12 66 23l-6 71q-2 38-39 43-33-3-39-37Z" fill="#d6a17f"/>
      <path d="M278 652q-21-12-12-43-19-28 4-48 28-24 61-9 37-2 44 33 13 36-17 58l-7-38q-44 4-59-18-11 25-14 65Z" fill="#323f3d"/>
      <path d="M266 586q-27 10-29-18-2-25 22-26 25-1 26 20Z" fill="#323f3d"/>
      <path d="M285 663q-11-13-15-2-2 16 14 17" fill="#d6a17f"/>
      <path d="M345 650l8 16-10 3" fill="none" stroke="#b67d60" stroke-width="2.5" stroke-linecap="round"/>
      <g id="parent-gaze"><path d="M303 638q5-4 11-1m17 0q6-3 11 1" fill="none" stroke="#45504a" stroke-width="2.5" stroke-linecap="round"/><ellipse cx="309" cy="644" rx="2.6" ry="3.2" fill="#303c39"/><ellipse cx="337" cy="644" rx="2.6" ry="3.2" fill="#303c39"/></g>
      <path id="parent-smile" d="M320 682Q328 684 335 680" fill="none" stroke="#a4634d" stroke-width="2.5" stroke-linecap="round"/>
      <ellipse cx="340" cy="671" rx="9" ry="4" fill="#c6816d" opacity=".32"/>
      <circle cx="282" cy="677" r="4" fill="#e9c387"/>
    ''','','parent-head')
    # Desk and laptop in front of the working hand, below the moving near arm.
    c+=line('M91 859l-20 250m222-241 13 221','#80634c',12)
    c+=path('M45 838l243-28 95 45-252 35Z','#b58b65')
    c+=path('M45 838v16l86 46 252-31v-14l-252 35Z','#8f7055')
    c+=path('M45 838l243-28 95 45-252 35Z','#d7b48a')
    c+=path('M170 835l107-13 45 19-109 15Z','#647b7d')
    c+=line('M185 837l91-9m-78 15 90-9','#c4cdc0',2)
    c+=group(path('M0 0L-28-112 82-126 110-14Z','#455d64')+path('M5-10L-18-104 75-115 99-21Z','#849b98')+path('M-18-104L75-115 99-21Z','#bdc6b1','opacity=".45"')+ellipse(39,-66,6,6,'#dde1cf'),'translate(170 835)','laptop-position')
    # Nested lid layer: animation transforms only this, preserving hinge position.
    c+=line('M340 757Q375 791 351 818L281 834','#d6a17f',25,'id="parent-near-arm"')
    c+=path('M327 739Q348 729 364 771L335 793 311 758Z','#e8d9bd','id="parent-near-sleeve"')
    c+=path('M278 828q-17-6-24 1l-3 8 24 5 12-8Z','#d6a17f','id="parent-hand"')
    # Child is staged beside the chair: constant scale, no rushed cross-room walk.
    c+=path('M521 1012l-4 98h22l16-98Z','#b77c56')+path('M550 1015l19 95h22l-14-104Z','#cf9365')
    c+=path('M513 1105h28l-4 16h-37q-9-8 13-16Z','#eee2c5')+path('M566 1107h25l17 13h-42Z','#eee2c5')
    c+=path('M518 919q24-17 51 3l16 98q-30 18-70-1Z','#b76e51')
    c+=line('M565 936l25 40-5 29','#d8a480',16)
    c+=path('M534 894h23v30q-12 8-23-2Z','#d8a480')
    c+=group('''<path d="M516 845q-2-34 31-35 36 1 37 37l-6 38q-10 28-37 22-30-6-25-62Z" fill="#dca986"/>
      <path d="M514 863q-17-35 8-54 24-21 49-5 30 9 21 48l-15-14-11-15q-18 17-44 11l-3 28Z" fill="#35413e"/>
      <path d="M523 870l-8 10 9 3" fill="none" stroke="#b57d5e" stroke-width="2" stroke-linecap="round"/>
      <ellipse cx="529" cy="860" rx="2.5" ry="3" fill="#303d39"/><ellipse cx="552" cy="860" rx="2.5" ry="3" fill="#303d39"/>
      <path id="child-smile" d="M532 888Q541 890 546 886" fill="none" stroke="#a2674f" stroke-width="2.5" stroke-linecap="round"/>
      <ellipse cx="562" cy="881" rx="8" ry="4" fill="#c77e66" opacity=".3"/>
    ''','','child-head')
    c+=line('M524 937Q502 961 494 973L476 965','#dca986',17,'id="child-near-arm"')
    c+=ellipse(475,965,10,9,'#dca986','id="child-hand"')
    c+=plant(68,1202,1.3)
    return svg(c,'Original family workspace and terrace, parent and child')

if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--scene', choices=['S03','S08'])
    args=parser.parse_args()
    for sid,name,draw in [('S03','S03-coast.svg',coast),('S08','S08-home.svg',home)]:
        if args.scene and args.scene != sid:
            continue
        content=draw()
        (ART/name).write_text(content,encoding='utf-8')
        print('Artwork:', ART/name)
