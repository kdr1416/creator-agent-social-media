"""Original editable vector art, four static pose proofs. No production mutation."""
from pathlib import Path
import json
from html import escape

ROOT=Path(__file__).resolve().parent
NAVY='#103A55'; INK='#16394B'; CORAL='#F46450'; LIGHT='#FFF9EE'

def path(d,fill,extra=''):
    return f'<path d="{d}" fill="{fill}" {extra}/>'
def line(d,col,w=2,extra=''):
    return path(d,'none',f'stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}')
def rect(x,y,w,h,c,r=0,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}" {extra}/>'
def ellipse(x,y,rx,ry,c,extra=''):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {extra}/>'
def group(id,content,transform=''):
    return f'<g id="{id}"'+(f' transform="{transform}"' if transform else '')+f'>{content}</g>'
def text(x,y,size,s,c=NAVY,font='Display',extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-family="{font}" fill="{c}" {extra}>{escape(s)}</text>'

DEFS='''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#80D9F0"/><stop offset="1" stop-color="#F0FDFA"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2=".4" y2="1"><stop stop-color="#169CC5"/><stop offset=".45" stop-color="#06BCCC"/><stop offset="1" stop-color="#047B9D"/></linearGradient>
<linearGradient id="stone" x1="0" y1="0" x2="1" y2=".3"><stop stop-color="#FFF1D2"/><stop offset="1" stop-color="#EDD19E"/></linearGradient>
<linearGradient id="stoneSide"><stop stop-color="#D0B583"/><stop offset="1" stop-color="#BFA077"/></linearGradient>
<linearGradient id="ground" x1="0" y1="0" x2=".55" y2="1"><stop stop-color="#FBF6E9"/><stop offset="1" stop-color="#DCECEB"/></linearGradient>
<linearGradient id="skin" x1="0" y1="0" x2="1" y2=".4"><stop stop-color="#F7C09A"/><stop offset="1" stop-color="#DE946E"/></linearGradient>
<linearGradient id="skinDark"><stop stop-color="#D89069"/><stop offset="1" stop-color="#B96A4B"/></linearGradient>
<linearGradient id="blueShirt" x1="0" y1="0" x2="1" y2=".8"><stop stop-color="#239EC0"/><stop offset="1" stop-color="#07657E"/></linearGradient>
<linearGradient id="coralShirt" x1="0" y1="0" x2="1" y2=".7"><stop stop-color="#FF8B67"/><stop offset="1" stop-color="#E94E47"/></linearGradient>
<linearGradient id="pants"><stop stop-color="#245873"/><stop offset="1" stop-color="#123E56"/></linearGradient>
<linearGradient id="room" x1="0" y1="0" x2="1" y2=".8"><stop stop-color="#FFFDF5"/><stop offset="1" stop-color="#ECEBDD"/></linearGradient>
<linearGradient id="terrace" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#FFF6DB"/><stop offset="1" stop-color="#D5E8E8"/></linearGradient>
<linearGradient id="awning" x1="0" y1="0" x2=".8" y2="1"><stop stop-color="#CD5445"/><stop offset="1" stop-color="#B6443B"/></linearGradient>
<linearGradient id="hair"><stop stop-color="#27484F"/><stop offset="1" stop-color="#122F3B"/></linearGradient>
<linearGradient id="desk"><stop stop-color="#F4BD7A"/><stop offset="1" stop-color="#DA9C60"/></linearGradient>
<radialGradient id="light"><stop stop-color="#FFFADE" stop-opacity=".8"/><stop offset="1" stop-color="#FFFADE" stop-opacity="0"/></radialGradient>
</defs>'''

def plant(id,x,y,s=1,leaves='#147B79',pot=CORAL):
    b=ellipse(0,13,52,12,'#194E60','opacity=".09"')
    b+=path('M-33-9L-26 45Q0 57 26 45L34-9Z',pot)+ellipse(0,-9,34,10,'#FFAA7E')
    b+=ellipse(0,-10,28,6,'#7C6148')
    b+=line('M0-8Q5-90 10-158M2-45Q-27-79-32-114M7-78Q40-107 43-145',leaves,5)
    for d in ['M8-120Q-18-150 7-186Q35-154 8-120Z','M2-70Q-54-72-57-119Q-16-123 2-70Z','M7-89Q15-141 57-150Q70-105 7-89Z','M-2-28Q-42-35-44-71Q-7-76-2-28Z','M5-49Q26-88 62-76Q59-42 5-49Z']:
        b+=path(d,leaves)
    b+=line('M10-155L8-124M-43-105L-10-76M45-132L18-107','#63B7A0',2,'opacity=".7"')
    return group(id,b,f'translate({x} {y}) scale({s})')

def head(id,x,y,s=1,look=1,hair='short',smile=True):
    # Original three-quarter face; ear behind jaw, whites/iris, brow and cheek planes.
    b=path('M-31-8Q-33-47 0-49Q36-49 38-9L35 21Q31 45 4 47Q-18 43-25 25Z','url(#skin)')
    b+=path('M-22 9Q-18 37 5 41Q20 44 35 25Q30 48 4 47Q-20 43-25 25Z','#CD8764','opacity=".45"')
    b+=ellipse(-27,7,9,13,'#EEAD84')+line('M-29 4Q-21-2-23 11','#C88361',1.8)
    if hair=='bun':
        b+=ellipse(-29,-43,24,25,'#183A43')
        b+=path('M-33 7Q-46-39-12-54Q17-65 37-41Q48-23 38 4L29-21Q2-8-15-28Q-18-4-26 10Z','url(#hair)')
        b+=line('M-30-31Q-18-52 6-49','#54717A',3,'opacity=".6"')
    elif hair=='wave':
        b+=path('M-33 11Q-48-21-28-45Q-5-68 23-49Q48-53 43-21L35 1 21-23Q2-13-17-28Q-20-3-27 13Z','url(#hair)')
        b+=line('M-25-34Q-4-54 19-42','#50727A',3,'opacity=".6"')
    else:
        b+=path('M-32 5Q-45-31-18-49Q13-64 38-38L40-17Q22-13 3-31Q-9-12-27-11L-26 10Z','url(#hair)')
        b+=line('M-21-34Q1-48 21-35','#4E6970',3,'opacity=".5"')
    b+=path('M-10-8Q-3-12 4-7Q-2-2-9-5Z','#FFF8EF')
    b+=path('M18-8Q25-12 31-7Q24-2 18-5Z','#FFF8EF')
    b+=ellipse(0,-7,2.6,3.6,'#173D4A')+ellipse(26,-7,2.5,3.5,'#173D4A')
    b+=line('M-11-17Q-4-21 4-16M18-17Q24-20 31-16','#24444C',2.6)
    b+=path('M15-8L21 9Q18 15 11 11','#D78D68')
    b+=ellipse(-8,15,8,4,'#EF957D','opacity=".55"')
    b+=line('M5 25Q16 33 26 22' if smile else 'M7 25Q16 29 24 24','#9F5747',2.5)
    if hair=='bun':b+=ellipse(-25,22,3.3,4,'#FFD367')
    return group(id,b,f'translate({x} {y}) scale({s*look} {s})')

def child_head():
    b=path('M-38-8Q-42-48-7-54Q28-61 43-31L42 13Q39 46 8 50Q-22 50-34 25Z','url(#skin)')
    b+=path('M-33 21Q-15 45 10 43Q29 41 40 24Q31 54 7 50Q-23 49-34 25Z','#D88E69','opacity=".36"')
    b+=ellipse(-35,10,10,14,'#EEAD84')+line('M-39 7Q-30 0-31 15','#C98965',1.7)
    b+=path('M-39 2Q-49-33-21-53Q10-70 38-45Q49-28 43-12L26-16 8-36Q-8-17-35-17L-32 8Z','url(#hair)')
    b+=line('M-27-36Q-3-55 22-39','#4C7177',3)
    b+=path('M-15-3Q-6-11 4-3Q-5 6-14 0Z','#FFFCF2')+path('M18-3Q27-10 35-2Q27 6 19 1Z','#FFFCF2')
    b+=ellipse(0,-2,3.8,5,'#173C48')+ellipse(31,-1,3.5,4.8,'#173C48')
    b+=line('M-16-14Q-6-19 3-14M20-13Q27-17 34-12','#28454A',2.4)
    b+=path('M15 3L19 13Q15 17 10 13','#DB906B')
    b+=ellipse(-12,19,10,5,'#EF967F','opacity=".68"')+ellipse(31,20,7,4,'#EF967F','opacity=".4"')
    b+=line('M1 29Q14 42 29 27','#A65C48',2.8)
    return group('s08-child-head',b,'translate(623 1133) scale(-.91 .91)')

def walker(id,x,y,s=1):
    b=ellipse(2,3,75,15,'#254D66','opacity=".12"')
    b+=group(id+'-leg-far',path('M4-174Q22-183 32-172L39-112Q39-98 48-82L78-18 58-9Q35-34 20-62Q8-79 4-95L-17-145Z','#19465B')+line('M25-157Q27-109 41-88L64-36','#2B667E',3)+path('M57-17Q76-21 85-11L100-4Q105 5 95 7L58 6 49-2Z','#EAF5ED')+line('M60 1H96','#88AFB6',3))
    b+=group(id+'-leg-near',path('M-42-174Q-21-177 0-170L-5-109Q-8-93-15-74L-32-17-56-20-43-99Z','url(#pants)')+line('M-19-158L-22-106-42-35','#47788A',2.5)+path('M-57-22L-30-19-22-4Q-16 4-28 7L-69 7Q-75 2-67-4Z',LIGHT)+line('M-66 2H-28','#86ADB4',3))
    b+=group(id+'-arm-far',path('M25-282Q45-276 52-248L72-212 89-213Q103-209 99-201Q88-191 70-197L42-229 22-256Z','#E4A17A'))
    b+=path('M-25-304L-23-279Q-3-263 16-281L15-308Z','url(#skinDark)')
    b+=path('M-28-289Q-4-276 22-287Q47-280 49-252L32-226 33-175Q-1-159-43-176L-46-244-58-260Q-53-282-28-289Z','url(#coralShirt)')
    b+=path('M-38-248L-25-245-22-180-42-176Z','#D94E46','opacity=".6"')
    b+=line('M-22-284Q-7-266 14-281','#FFC1A0',3)
    b+=line('M6-239L19-203M-31-188Q-4-180 24-189','#FFB395',2,'opacity=".65"')
    b+=path('M-28-280Q-19-274-9-276L1-190-13-187Z','#FF9A78','opacity=".4"')
    b+=group(id+'-arm-near',path('M-51-268Q-66-265-63-239L-51-195-23-174Q-16-166-8-176Q-6-183-17-190L-33-207-35-246Z','url(#skin)')+line('M-18-183L-11-179M-23-179L-16-174','#C17B5B',1.5))
    b+=line('M-44-279L9-179','#113C52',7)
    b+=path('M7-211Q29-219 47-204L41-157Q21-150 4-162Z','#F8C762')+line('M12-204Q29-213 40-199','#E29F4E',2)
    b+=head(id+'-head',-5,-335,.72,1,'wave')
    return group(id,b,f'translate({x} {y}) scale({s})')

def seated_cafe(id,x,y,s=1,mirror=False,raise_cup=False):
    b=ellipse(0,0,75,13,'#29495A','opacity=".1"')
    b+=line('M-39-121L-37-3M18-96L29-2M-40-196L-41-106 27-105','#1B6C75',7)
    b+=path('M-25-117L30-111Q48-104 38-80L17-21-7-23 8-83-38-91Z','url(#pants)')
    b+=path('M-8-26L18-24 29-10Q33-2 25 1L-18 1-22-8Z',LIGHT)
    b+=path('M-34-132L-7-114 0-66 31-22 14-10-20-53-39-98Z','#1B465E')
    b+=path('M14-19L34-23 50-9Q52-2 45 0L13 1 6-5Z',LIGHT)
    b+=path('M-25-222Q-2-232 19-215L29-125Q-4-110-35-127L-41-189Z','url(#blueShirt)')
    b+=path('M-13-244L-12-218Q0-209 12-219L11-245Z','url(#skinDark)')
    b+=head(id+'-head',-4,-260,.69,1,'short')
    if raise_cup:
        b+=path('M15-209Q32-214 37-196L48-171 65-204 79-199Q64-150 49-149Q35-149 20-174Z','url(#skin)')
        b+=ellipse(77,-207,10,8,'#EBA87D')
        b+=group(id+'-cup',path('M72-225H94L91-202Q81-196 74-204Z',LIGHT)+line('M94-222Q109-223 106-213Q104-206 94-208',LIGHT,4)+ellipse(83,-225,11,3,'#B68056'))
    else:
        b+=path('M16-211Q33-216 37-197L49-173 75-180 80-168Q43-148 34-161L17-183Z','url(#skin)')+ellipse(78,-175,11,7,'#EBA87D')
    return group(id,b,f'translate({x} {y}) scale({-s if mirror else s} {s})')

def window(x,y,w,h,balcony=False):
    b=path(f'M{x-7} {y+h+8}H{x+w+8}V{y-5}H{x-7}Z','#D4B87E')
    b+=rect(x,y,w,h,'#116B77',3)+rect(x+5,y+5,w-10,h-10,'#194F61')
    b+=path(f'M{x+7} {y+8}H{x+w-8}L{x+7} {y+h*.65}Z','#72BDC0','opacity=".42"')
    for a in [x+w*.28,x+w*.68]:b+=rect(a,y+8,3,h-16,'#6DA59E')
    b+=line(f'M{x+5} {y+h*.45}H{x+w-5}','#A0BF9F',2)
    b+=path(f'M{x-11} {y+h+7}H{x+w+13}L{x+w+18} {y+h+16}H{x-11}Z','#FFFBDF')
    if balcony:
        b+=path(f'M{x-17} {y-14}L{x+w+4} {y-14} {x+w+31} {y+2} {x+8} {y+2}Z','#72B8AB')
        b+=path(f'M{x+w+6} {y+2}L{x+w+31} {y+2}V{y+h+29}L{x+w+6} {y+h+16}Z','#125463')
        b+=rect(x-16,y+2,w+23,h+17,'#1B7E85')
        for a in range(4):b+=rect(x-6+a*(w+6)/4,y+14,(w+6)/4-7,h-17,'#B4D5BD')
        b+=rect(x-19,y+h+5,w+28,15,'#135A6A')
        b+=path(f'M{x-22} {y+h+20}H{x+w+8}L{x+w+31} {y+h+32}H{x-3}Z','#F6DFA9')
        b+=path(f'M{x-6} {y+h+31}L{x+7} {y+h+45} {x+16} {y+h+31}M{x+w-4} {y+h+31}L{x+w+9} {y+h+45} {x+w+16} {y+h+31}Z','#BAA379')
    return b

def coast(state):
    b=rect(0,0,900,1600,'url(#sky)')
    b+=ellipse(790,240,310,310,'url(#light)')
    b+=path('M445 270Q550 220 680 259T930 250V296H445Z','#F1FEF5','opacity=".7"')
    b+=path('M0 496Q365 432 900 475V1600H0Z','url(#sea)')
    b+=group('s03-distant-town',path('M530 478L555 444 590 449 619 430 650 431 650 398 664 398 664 430 708 430 708 407 733 407 733 433 763 433 763 387 796 387 796 428 827 428 827 408 854 408 854 441 900 441V503Z','#F5DDA6')+path('M549 476L900 461V493L526 500Z','#C6BD8B')+line('M681 449H700M746 452H762M808 448H820','#BB9F70',3))
    for i in range(16):
        x=520+(i*113)%420;y=540+i*27
        b+=line(f'M{x} {y}h{22+(i%4)*16}','#BFF5DE',2.5,'opacity=".5"')
    b+=group('s03-building',path('M-40-40H299L444 40V691L260 820-40 878Z','url(#stone)')+path('M299-40L444 40V690L299 742Z','url(#stoneSide)')+path('M-40 8H299L444 83V102L299 30H-40Z','#FFFAE2')+path('M-40 247H299V261H-40ZM-40 470H299V485H-40Z','#FFFAE2')+line('M306 43V719','#B9986B',2)+window(25,78,80,118,True)+window(177,90,69,112)+window(27,330,72,103)+window(169,324,76,120,True)+path('M12 700V594Q12 524 73 524T134 594V677Z','#125764')+path('M180 644V567Q180 510 231 510T280 567V621Z','#1B5260'))
    masonry=''
    for yy in [59,220,292,444,510]:
        masonry+=line(f'M-15 {yy}H295','#D4B77F',1.4,'opacity=".55"')
    for xx,yy in [(144,59),(264,220),(18,292),(134,444),(283,510)]:masonry+=line(f'M{xx} {yy}v24','#D4B77F',1.2,'opacity=".55"')
    masonry+=path('M302 104L420 164V198L302 142ZM302 488L420 548V582L302 527Z','#927D59','opacity=".16"')
    masonry+=path('M147 49H257L265 59H140Z','#FFF9DF')+rect(155,61,6,135,'#D5B880')+rect(258,61,5,135,'#D5B880')
    b+=group('s03-masonry-relief',masonry)
    balcony_garden=''
    for x,y in [(49,208),(64,214),(80,209),(101,214),(199,465),(218,466),(239,465)]:
        balcony_garden+=ellipse(x,y,12,7,'#2A997C')+ellipse(x+4,y-7,7,11,'#55B284')
    balcony_garden+=line('M39 208Q34 255 43 277M101 212Q117 245 108 259','#218B79',4)
    b+=group('s03-balcony-garden',balcony_garden)
    # Second façade is a smaller, separate volume, not a repeated recolor.
    b+=path('M-35 530L27 514V886L-35 930Z','#C7B589')
    b+=path('M-20 878L315 749 410 672 503 681Q642 783 703 865Q741 952 602 1030Q583 1101 900 1220V1600H-20Z','url(#ground)')
    b+=path('M463 718Q668 804 692 867Q723 943 586 1016Q516 1105 900 1236L900 1280Q463 1129 559 995Q681 919 657 869Q624 807 448 750Z','#C0A674')
    b+=path('M462 698Q674 792 709 868Q745 950 605 1034Q557 1095 900 1215V1243Q518 1113 581 1016Q719 931 686 873Q650 812 451 725Z','#FFFBDE')
    b+=line('M477 720Q663 804 692 871Q726 942 594 1025Q539 1101 900 1229','#E6CC9C',3)
    # Paving joins follow the shared ground direction.
    for d in ['M-30 1050L534 852','M-40 1260L635 1006','M-30 1510L740 1173','M90 1600L494 900','M458 1600L598 1096']:
        b+=line(d,'#BBD1D1',2,'opacity=".55"')
    b+=group('s03-cafe-cast-shadow',path('M30 834L418 741 512 1012 274 1188-24 1111Z','#7BB2B4','opacity=".13"')+path('M443 772L450 772 544 1020 536 1024Z','#4D8B98','opacity=".2"'))
    # Café anchored to the façade; the roof and posts use the same plane.
    cafe=line('M64 812V1115M440 726V1005','#1A626C',6)
    cafe+=path('M-26 656L358 568 471 735 81 834Z','url(#awning)')
    cafe+=path('M81 834L471 735V758L81 858Z','#C94D43')
    cafe+=line('M-17 660L359 576M89 826L463 734','#FFA781',3)
    for xx in [30,105,180,255,330]:cafe+=line(f'M{xx} {643-xx*.22}l107 164','#FFB392',2,'opacity=".38"')
    cafe+=path('M78 858L96 868 478 770 471 758Z','#1D6672','opacity=".12"')
    if state=='B':
        cafe+=group('s03-cafe-type',text(78,726,72,'cà phê','#FFF9EE','Editorial',extra='id="s03-type-main"')+text(100,789,28,'NGOÀI TRỜI','#FFF9EE',extra='letter-spacing="2.5" font-weight="700"'), 'rotate(-14 78 726)')
        cafe+=group('s03-graphic-disc',ellipse(373,654,14,14,'#FFD06A')+path('M373 640A14 14 0 0 1 387 654H373Z','#103A55'))
    b+=group('s03-cafe-roof',cafe)
    b+=seated_cafe('s03-cafe-person-left',175,1120,.86,False,state=='B')
    b+=seated_cafe('s03-cafe-person-right',365,1080,.78,True,False)
    b+=group('s03-table',line('M265 1008V1133M217 1138L265 1128 306 1140','#1D5969',7)+ellipse(269,1000,86,27,'#F9D69E')+path('M183 1000Q269 1043 355 1000V1010Q269 1053 183 1010Z','#D5AC72')+ellipse(270,999,71,18,'#FFE8BF'))
    b+=group('s03-table-props',ellipse(294,997,14,4,'#FFFCEE')+path('M283 976H303L300 994Q292 1000 286 994Z','#FFFCEE')+line('M303 979Q316 976 313 987H302','#FFFCEE',3))
    b+=group('s03-table-vase',path('M246 991Q241 977 245 966H255Q259 982 253 991Z','#EDF5DE')+line('M250 969L248 942M251 959L261 949','#4C9B7C',2)+ellipse(247,941,5,7,'#FFC966')+ellipse(261,947,6,6,'#F98968'))
    b+=plant('s03-cafe-planter',59,1150,.67,'#137F79','#E96A51')
    # One smaller active runner, on the far path; hero carries the foreground focus.
    runner=path('M-7-87L9-86 28-48 60-47 59-34 15-33-5-61Z','#103A55')+path('M-15-83L3-76-16-41-45-17-54-28-30-53Z','#194D68')
    runner+=path('M-10-144L17-140 20-88-14-82-27-118Z','#FFC961')+line('M12-132L35-113 49-135','#DE9970',12)+line('M-20-127L-39-106-57-115','#DE9970',12)+head('s03-runner-head',4,-163,.39,1,'short')
    runner+=line('M48-35H66M-57-22L-47-13','#F8FCF0',8)
    b+=group('s03-runner',runner,'translate(615 866) scale(.72)')
    b+=group('s03-hero-placement',walker('s03-hero',583 if state=='A' else 640,1460,1.28))
    b+=plant('s03-foreground-agave',-5,1550,1.65,'#146B70','#E98A65')
    b+=line('M765 279q13-14 26 0q14-14 27 0','#5C9EA8',3)
    b+=group('s03-water-geometry',path('M760 648Q823 631 900 650V665Q823 648 760 662Z','#7CE3D8','opacity=".4"')+path('M731 1082Q818 1113 900 1096V1111Q809 1129 720 1098Z','#86E7CE','opacity=".35"'))
    return b

def laptop(opened):
    # Base stationary in both poses; lid is a rigid quadrilateral with hinge endpoints.
    b=group('s08-laptop-base',path('M111 1119L264 1083 349 1135 196 1172Z','#15516C')+path('M111 1119V1127L196 1180 349 1143V1135L196 1172Z','#0E3C56')+path('M141 1125L262 1097 318 1132 198 1160Z','#4C8597')+path('M211 1145L246 1137 259 1145 225 1154Z','#8EBDC2'))
    if opened:
        d='M111 1119L264 1083 244 953 92 989Z';screen='M119 1100L248 1070 232 969 103 1000Z'
    else:
        d='M111 1119L264 1083 340 1128 187 1165Z';screen=None
    lid=path(d,'#1B526C')+line('M111 1119L264 1083','#A9D9D8',3)
    if screen:
        lid+=path(screen,'#0E7895')+line('M120 1014L218 991M125 1033L196 1016M128 1052L216 1031','#6ACACD',3)+ellipse(177,1067,8,3,'#8AD8D2')
    else:lid+=ellipse(224,1123,10,4,'#9CD3CD')
    return b+group('s08-laptop-lid',lid)

def mother(state):
    b=ellipse(351,1461,176,28,'#174B65','opacity=".1"')
    # Bentwood chair, seat and both grounded legs.
    b+=group('s08-chair',path('M215 1074Q235 1044 291 1053L360 1111 370 1220 278 1245 224 1192Z','#B66D52')+path('M230 1077Q256 1067 282 1078L340 1124 348 1203 279 1224 239 1184Z','#DA9B70')+path('M265 1228L253 1450H268L302 1240M346 1217L390 1439H406L371 1206Z','#17485A'))
    # Far leg with bent knee, then near leg; neither is a straight mannequin rod.
    b+=group('s08-parent-leg-far',path('M298 1170Q318 1167 342 1193L389 1281Q396 1300 381 1329L335 1420 310 1410 342 1305 283 1239Z','#1A4860')+path('M310 1408L338 1417 340 1433 369 1444Q374 1453 361 1457H303Q290 1451 300 1436Z','#FFF9EB')+line('M302 1451H361','#B6CEC9',3))
    b+=group('s08-parent-leg-near',path('M330 1164Q361 1155 382 1184L446 1241Q465 1258 462 1283L444 1426 411 1426 416 1291 333 1234Z','url(#pants)')+path('M411 1419L445 1423 451 1440 490 1449Q500 1461 484 1465H413Q400 1463 402 1453Z','#FFF9EB')+line('M411 1458H485','#A6C3C4',3))
    # Torso leans toward child a little in the contact proof.
    b+=path('M307 970Q336 954 364 978L396 1010 391 1114 373 1198Q336 1215 286 1189L276 1079 278 1012Z','url(#blueShirt)')
    b+=path('M290 1016L305 1019 303 1179Q332 1197 370 1187L373 1198Q334 1218 286 1189L276 1079Z','#07556E','opacity=".55"')
    b+=line('M314 1003Q333 1022 354 1002M328 1041L334 1134M333 1159L334 1175','#64BBC9',2.5)
    b+=path('M293 1012Q312 1001 323 1011L318 1168 304 1181Z','#4EB1C3','opacity=".3"')
    b+=line('M354 1099L375 1130M303 1165L315 1179M365 1181L377 1164','#0A5B76',2.8)
    b+=ellipse(332,1044,2.7,2.7,'#C2E6DF')+ellipse(333,1071,2.7,2.7,'#C2E6DF')
    b+=path('M317 949L313 974Q329 997 354 978L350 952Z','url(#skinDark)')
    b+=head('s08-parent-head',332,922,1.02,1,'bun',True)
    if state=='A':
        arm=path('M284 1007Q266 1008 257 1037L238 1085 271 1103 286 1078 302 1040Z','url(#skin)')
        arm+=path('M271 1083L286 1090 308 1082Q323 1081 328 1089L312 1102 286 1109 262 1101Z','url(#skin)')
        arm+=line('M305 1089L318 1088M302 1094L315 1092','#C17D5E',1.8)
        arm+=path('M376 1004Q395 1000 405 1024L421 1083Q426 1100 408 1107L350 1127 340 1110 390 1085 372 1042Z','url(#skin)')
        arm+=path('M347 1108L327 1103Q314 1101 305 1110L302 1117 333 1126 352 1124Z','url(#skin)')
        arm+=line('M310 1110L329 1114M306 1117L325 1120','#C17D5E',1.8)
    else:
        # Far hand rests on thigh. Near hand reaches a reachable shared endpoint.
        arm=path('M284 1007Q264 1005 264 1035L274 1136 306 1169 322 1158 297 1124 302 1040Z','url(#skin)')
        arm+=ellipse(314,1166,16,11,'#EDAD83')
        arm+=path('M375 1003Q394 997 407 1025L445 1084 496 1142 479 1160 421 1114Q407 1106 398 1087L371 1043Z','url(#skin)')
        arm+=path('M480 1141Q489 1139 499 1147L516 1157Q526 1165 520 1174Q512 1180 503 1173L488 1166 477 1157Z','url(#skin)')
        arm+=line('M497 1156L515 1167M493 1162L510 1172','#BC7658',1.8)
    b+=group('s08-parent-arms',arm)
    b+=group('s08-parent-sleeves',path('M282 1006Q292 997 304 1011L299 1041 277 1049 260 1038Q260 1017 282 1006Z','#1286A3')+path('M372 997Q393 999 403 1017L412 1035 385 1053 369 1034Z','#2197B1')+line('M278 1045L297 1039M388 1049L409 1036','#72C2C8',2))
    return group('s08-parent',b)

def child(state):
    b=ellipse(641,1479,86,18,'#144B60','opacity=".12"')
    b+=group('s08-child-leg-far',path('M631 1317L668 1312 680 1388 667 1461 642 1461 647 1386Z','#194F65')+path('M642 1457L669 1458 678 1471 697 1474Q704 1482 691 1486H641Q632 1482 636 1473Z','#FFF8E8'))
    b+=group('s08-child-leg-near',path('M595 1311L636 1319 625 1389 610 1462 585 1458 589 1382Z','#24657A')+path('M584 1457L612 1460 614 1476Q616 1485 602 1487H564Q554 1481 566 1474Z','#FFF8E8'))
    b+=path('M605 1185Q627 1172 647 1187L673 1210 671 1319Q629 1340 589 1320L585 1232Z','url(#coralShirt)')
    b+=path('M644 1205L659 1226 654 1314 633 1326 671 1319 673 1210Z','#E45449')
    b+=path('M610 1160L608 1190Q622 1208 640 1193L638 1160Z','url(#skinDark)')
    b+=line('M606 1191Q619 1211 642 1194','#FFBE96',3)
    b+=child_head()
    b+=group('s08-child-arm-far',path('M663 1210Q679 1215 682 1235L691 1292Q694 1304 685 1312Q674 1316 669 1304L659 1269 651 1235Z','url(#skin)')+line('M678 1300L682 1307','#B77756',1.6))
    if state=='A':
        near=path('M592 1214Q580 1207 571 1226L549 1264 526 1251Q514 1248 511 1259Q513 1269 526 1275L550 1285Q563 1288 572 1275L604 1241Z','url(#skin)')
        near+=line('M519 1258L528 1262M517 1263L525 1267','#C07D5A',1.6)
    else:
        near=path('M592 1214Q582 1202 568 1213L544 1224 525 1180 510 1185 524 1241Q530 1256 545 1253L580 1245 602 1234Z','url(#skin)')
        near+=path('M526 1188L522 1171Q519 1157 511 1155Q502 1154 501 1165L503 1183Q506 1194 516 1196Z','url(#skin)')
        near+=line('M507 1167L511 1181M513 1165L518 1178','#BC7658',1.7)
    b+=group('s08-child-arm-near',near)
    b+=line('M608 1221L612 1287M634 1300L653 1295','#FFA887',2.5)
    return group('s08-child',b)

def home(state):
    b=rect(0,0,900,1600,'url(#room)')
    # Arched opening with real wall thickness, terrace beyond, unobstructed sky for type.
    b+=group('s08-opening',path('M389 982V390Q389 155 642 155T917 390V1025Z','#D8DDCE')+path('M425 973V394Q425 196 649 196T895 394V996Z','url(#sky)')+path('M425 625Q654 583 900 610V1089H425Z','url(#sea)')+path('M425 639L487 603 520 606 538 579 579 579 579 550 598 550 598 579 634 579 655 560 685 560 701 603 750 604 750 578 781 578 781 614 900 615V653Z','#F4DAA4')+path('M400 998L900 900V1600H400Z','url(#terrace)'))
    for x,y,w in [(470,706,75),(660,683,100),(797,737,70),(528,800,90),(740,826,130),(439,901,55)]:b+=line(f'M{x} {y}h{w}','#AFF3D9',3,'opacity=".7"')
    b+=ellipse(742,362,177,177,'url(#light)')
    b+=path('M350 1026L900 916V944L350 1054Z','#F8F9E9')
    for xx in range(429,901,62):
        yy=1042-(xx-350)*.2
        b+=line(f'M{xx} {yy}V1205','#8BBBC2',5)
    b+=path('M350 1210L900 1100V1120L350 1230Z','#86B8BE')
    b+=path('M-30 1322L900 1138V1600H-30Z','url(#ground)')
    # Window light lays across floor, not a global overlay on people.
    b+=path('M427 1230L690 1177 900 1489 900 1600 707 1600Z','#FFF7D7','opacity=".8"')
    for d in ['M0 1450L900 1271','M0 1599L900 1420','M120 1600L502 1220','M530 1600L700 1182']:
        b+=line(d,'#BED3D0',2,'opacity=".7"')
    # Wall shelving and few purposeful materials, keeping type/action negative space.
    b+=group('s08-wall-shelf',path('M42 780L273 780 290 798H59Z','#E9BA7D')+path('M59 798H290V810H59Z','#CF985F')+rect(75,726,18,54,'#E87355')+rect(96,712,15,68,'#186D83')+rect(115,737,22,43,'#E2BB73')+line('M101 723V770','#79BEC0',2)+plant('s08-shelf-plant',233,759,.38,'#187F77','#DFAF72'))
    niche=path('M95 588V397Q95 311 178 311T261 397V588Z','#E2D8BC')+path('M108 577V401Q108 326 178 326T249 401V577Z','#F0E8D2')
    niche+=path('M108 577H249L261 588H95Z','#C3B691')
    niche+=ellipse(156,569,34,8,'#D8CCAC')+path('M135 555Q118 532 135 509L141 495H171L177 512Q194 538 177 555Q157 570 135 555Z','#E99B74')+rect(141,488,30,10,'#D48967',3)
    niche+=path('M203 567Q189 536 201 503L205 471H223L229 507Q239 548 222 567Z','#4B9991')+ellipse(214,471,9,3,'#337D79')
    b+=group('s08-wall-niche',niche)
    b+=path('M-80 155L45 155 144 656 104 673Z','#F6DEA9','opacity=".24"')
    b+=mother(state)
    # Desk has a coherent parallel projection; near edge and legs support the top.
    desk=path('M28 1141L247 1087 401 1180 180 1239Z','url(#desk)')
    desk+=path('M28 1141V1162L180 1260 401 1202V1180L180 1239Z','#BF8353')
    desk+=path('M56 1179L72 1188 56 1480H41ZM340 1212L356 1208 392 1450H377Z','#194F62')
    desk+=line('M176 1250V1469','#194F62',11)
    b+=group('s08-desk',desk)+laptop(state=='A')
    b+=group('s08-notebook',path('M63 1147L104 1137 146 1163 105 1174Z','#FFF9E5')+line('M77 1149L111 1168','#77AAA9',2)+line('M90 1145L116 1161','#AFC1AF',1))
    b+=child(state)
    b+=plant('s08-terrace-planter',847,1377,.95,'#157A72','#DF7757')
    b+=plant('s08-foreground-plant',28,1576,.84,'#1A6970','#E1AD73')
    if state=='B':
        ty=text(511,406,91,'gia',NAVY,'Editorial',extra='id="s08-type-family-a"')
        ty+=text(532,510,103,'đình',NAVY,'Editorial',extra='id="s08-type-family-b"')
        # Graphic disk/counterform ties to canopy vocabulary; no repeated underline.
        ty+=ellipse(740,380,16,16,'#F9C765')+path('M740 364A16 16 0 0 1 756 380H740Z','#E66B52')
        b+=group('s08-family-type',ty)
    # Static camera framing: bring body/gaze/contact into mobile reading range.
    return rect(0,0,900,1600,'#F7F6E9')+group('s08-camera',b,'translate(-65 -350) scale(1.25)')

CSS='''@font-face{font-family:Display;src:url('assets/display.ttf')}@font-face{font-family:Editorial;src:url('assets/editorial-italic.ttf')}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#EFF9F4}#root{width:100%;height:100%;position:relative}svg{display:block;width:100%;height:100%}text[font-family="Display"]{font-weight:700;font-variation-settings:"wght" 700,"wdth" 90}text{font-kerning:normal;text-rendering:geometricPrecision}'''

FRAMES=[
 dict(id='S03-A',scene='S03',state='A',global_voice=10.5,global_frame=315,local_frame=10,word_numbers_1based=[46,47],label='Coastal lifestyle · environment & character',type_state='none'),
 dict(id='S03-B',scene='S03',state='B',global_voice=13.68,global_frame=411,local_frame=106,word_numbers_1based=[60,63],label='Café · typography on the awning',type_state='settled_layout_test'),
 dict(id='S08-A',scene='S08',state='A',global_voice=42.14,global_frame=1265,local_frame=57,word_numbers_1based=[174,175],label='Workspace · parent & child',type_state='none'),
 dict(id='S08-B',scene='S08',state='B',global_voice=45.0,global_frame=1350,local_frame=142,word_numbers_1based=[186,187],label='Family · connection & typography',type_state='settled_layout_test'),
]

def build():
    for item in FRAMES:
        ident=item['id'];body=coast(item['state']) if item['scene']=='S03' else home(item['state'])
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1600" role="img" aria-label="{escape(item["label"])}"><style>@font-face{{font-family:Display;src:url(assets/display.ttf)}}@font-face{{font-family:Editorial;src:url(assets/editorial-italic.ttf)}}text[font-family="Display"]{{font-weight:700;font-variation-settings:"wght" 700,"wdth" 90}}</style>{DEFS}{body}</svg>'
        (ROOT/f'{ident}.svg').write_text(svg,encoding='utf8')
        duration=268/30 if item['scene']=='S03' else 168/30
        html=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=1080,height=1920"><title>{ident} — visual test</title><link rel="icon" href="data:,"><script src="assets/gsap.min.js"></script><style>{CSS}</style></head><body><main id="root" data-composition-id="{ident}" data-width="1080" data-height="1920" data-fps="30" data-duration="{duration}">{svg}</main><script>window.__timelines=window.__timelines||{{}};Promise.all([document.fonts.load('72px Display','Cà phê NGOÀI TRỜI'),document.fonts.load('72px Editorial','gia đình Cà phê')]).then(()=>document.fonts.ready).then(()=>{{const tl=gsap.timeline({{paused:true}});window.__timelines['{ident}']=tl;window.keyframeReady=true;}});</script></body></html>'''
        (ROOT/f'{ident}.html').write_text(html,encoding='utf8')
    (ROOT/'frames.json').write_text(json.dumps(FRAMES,ensure_ascii=False,indent=2),encoding='utf8')
    cards=''.join(f'''<article id="{it['id']}"><a href="{it['id']}.html"><img src="{it['id']}.png" alt="{it['id']}"></a><h2>{it['id']}</h2><p>{it['label']}</p><small>Voice {it['global_voice']:.2f}s · global frame {it['global_frame']} · STATIC POSE</small><nav><a href="{it['id']}.png">PNG 1080×1920</a> · <a href="{it['id']}.html">Editable source</a></nav></article>''' for it in FRAMES)
    (ROOT/'index.html').write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VIDEO-34 · Core styles R2</title><style>*{{box-sizing:border-box}}body{{margin:0;background:#0B2D40;color:#ECF8F4;font:16px Arial,sans-serif}}header{{padding:32px 36px 24px;max-width:1500px;margin:auto}}header small{{color:#8DCCCA;letter-spacing:2px}}h1{{font-size:32px;margin:12px 0}}header p{{max-width:850px;color:#AFCCCE;line-height:1.6}}.grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;max-width:1500px;margin:auto;padding:0 36px 40px}}article{{min-width:0}}img{{width:100%;display:block;border-radius:3px}}h2{{font-size:20px;margin-bottom:7px}}article p{{color:#BBD5D5;min-height:38px;margin:0 0 8px;font-size:14px}}small,nav{{font-size:12px;color:#8DCCCA}}nav{{margin-top:12px}}a{{color:#C2E9DC}}footer{{padding:24px 36px;background:#082536;line-height:1.7;color:#B6D4D4}}@media(max-width:950px){{.grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}@media(max-width:500px){{.grid{{grid-template-columns:1fr;padding:0 20px 30px}}header{{padding:24px 20px}}h1{{font-size:26px}}}}</style></head><body><header><small>VIDEO-34 / ORIGINAL VECTOR ART / R2</small><h1>Four frames. One visual world.</h1><p>AWAITING VISUAL STYLE REVIEW — static artwork and type-layout proofs. Modern illustrated storytelling, coherent spatial construction, environment-bound typography. No pilot animation or MP4 produced.</p></header><main class="grid">{cards}</main><footer>Palette: deep petrol · azure · turquoise · sunlit limestone · coral.<br>Typography V2 retained: Bahnschrift + Constantia Italic. Experimental creative palette, not official Esora branding.<br>Voice timestamps are source anchors. Type is shown settled for layout review; animation and effects remain planned.</footer></body></html>''',encoding='utf8')
    print('Built four original SVG/HTML pose states')

if __name__=='__main__':build()
