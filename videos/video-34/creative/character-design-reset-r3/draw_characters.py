"""Three original character directions. Authored static art, not a rigging engine.

All coordinates are drawing-space landmarks. Animation is intentionally absent.
R2 scene art is only read for the requested contextual test and comparisons.
"""
from pathlib import Path
import json, math, copy
from html import escape
import xml.etree.ElementTree as ET
ET.register_namespace('','http://www.w3.org/2000/svg')

ROOT=Path(__file__).resolve().parent
R2=ROOT.parent/'visual-tests-core-r2'
INK='#173D50'; PAPER='#F5F8F3'

def p(d,c,attrs=''):return f'<path d="{d}" fill="{c}" {attrs}/>'
def ln(d,c,w=2,attrs=''):return p(d,'none',f'stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {attrs}')
def e(x,y,rx,ry,c,attrs=''):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {attrs}/>'
def r(x,y,w,h,c,rad=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rad}" fill="{c}"/>'
def g(id,b,tr='',attrs=''):return f'<g id="{id}" transform="{tr}" {attrs}>{b}</g>'
def tx(x,y,n,s,c=INK,attrs=''):return f'<text x="{x}" y="{y}" font-size="{n}" fill="{c}" font-family="Display" {attrs}>{escape(s)}</text>'
def at(x,y,scale=1):return f'translate({x} {y}) scale({scale})'

STYLES={
 'A':dict(name='PREMIUM STYLIZED VECTOR',sub='Soft sculpted shapes / warm, observant / everyday ease',skin='#EAB18D',shade='#CC8A69',hi='#F8D3AD',hair='#253C4B',shine='#496574',shirt='#E77759',cloth='#F8E8CF',pants='#226D7B',shadow='#174F64',child='#EAB74F',head=-193,hs=.86,foot=250),
 'B':dict(name='MODERN EDITORIAL',sub='Longer proportions / tailored silhouette / quiet confidence',skin='#C89371',shade='#A96C52',hi='#E6B18C',hair='#252F3F',shine='#4D5262',shirt='#F4E4C9',cloth='#E0C9A5',pants='#14566A',shadow='#0E3D55',child='#D76E51',head=-201,hs=.67,foot=265),
 'C':dict(name='EXPRESSIVE GEOMETRIC',sub='Angular counterforms / graphic charm / elastic personality',skin='#F1AE83',shade='#D5805F',hi='#FFD1A0',hair='#243958',shine='#4A5E7B',shirt='#298A9E',cloth='#8AC8C4',pants='#E16B53',shadow='#BE4D43',child='#F3C550',head=-176,hs=1.05,foot=225),
}

def face(style,identity='parent',expression='warm',look=(1,0)):
    s=STYLES[style];sk=s['skin'];sh=s['shade'];hair=s['hair'];b=''
    child=identity=='child';second=identity=='second';resident=identity=='resident'
    if style=='A':
        contour='M-40-12C-45-40-24-58 3-56C31-55 46-34 42-8L38 22C34 42 15 51-3 45C-22 43-34 31-36 14Z' if not child else 'M-43-7Q-47-47-9-55Q28-61 44-31L45 10Q42 41 14 48Q-17 51-34 29Z'
    elif style=='B':
        contour='M-34-18Q-35-50-7-58Q19-63 33-43L37-18 46 2 36 8 33 27 13 47-4 48Q-25 38-30 19Z' if not child else 'M-38-13Q-42-45-12-53Q16-60 36-38L40-10 39 20Q27 45 6 45Q-21 42-32 22Z'
    else:
        contour='M-42-27L-13-54 24-49 42-20 38 2 51 11 35 17 30 37 3 49-29 29Z' if not child else 'M-45-19Q-37-48-9-51L29-40 41-11 37 19 14 42-20 35-41 12Z'
    b+=p(contour,sk)
    if style=='B':b+=p('M15-38L27-20 25 1 37 9 31 28 13 47-4 48 7 30Z',sh,'opacity=".5"')
    elif style=='A':b+=p('M-34 13Q-24 37-2 40Q21 45 38 23Q31 48 8 48Q-23 46-34 26Z',sh,'opacity=".36"')
    else:b+=p('M-9-36L2-10-9 13 6 31 30 37 3 49-29 29-36 7Z',sh,'opacity=".45"')
    b+=e(-36,6,9,13,sk)+ln('M-40 3Q-31-3-33 12',sh,2)
    # Four identities, not a recolored head; hairstyles alter the silhouette.
    if resident:
        b+=p('M-42-2Q-48-34-25-51Q1-69 29-49L40-30 25-23 15-38Q-8-25-29-20L-30 9Z','#DDE7DE')
        b+=ln('M-12-17L0-15M17-17L29-14','#7C837D',2)
    elif second:
        if style=='A':b+=p('M-41 0Q-48-29-30-43Q-38-56-16-57Q-4-71 8-58Q28-65 34-47Q49-36 39-15L24-20 13-35Q-10-23-30-21L-30 9Z',hair)
        elif style=='B':b+=p('M-36-4Q-48-44-15-57Q10-74 34-50L43-32Q28-18 12-35Q-10-21-28-22L-27 11Z',hair)+p('M-24 24Q-3 43 17 33L32 24 24 42 7 52-10 45Z',hair,'opacity=".6"')
        else:b+=p('M-43-24Q-48-63 3-64L35-49 39-24 16-31-6-18-29-20-30 8Z',hair)+p('M-40-31L-56-2-48 43-30 48-27 9Z',hair)
    elif child:
        if style=='A':b+=p('M-44 6Q-55-18-40-32Q-48-53-26-52Q-15-72 4-57Q25-70 32-49Q52-44 44-20L27-23 13-34Q1-10-18-23L-33-8-32 11Z',hair)
        elif style=='B':b+=p('M-41 6Q-51-28-32-45Q-10-67 22-49Q44-56 47-27L39-9 27-23 8-31Q-3-5-31-13L-29 12Z',hair)
        else:b+=p('M-46-12L-42-39-17-57 27-50 43-24 39-5 18-15 2-32-19-12Z',hair)+p('M-29-35L-13-42 1-37-16-30Z',s['shine'])
    elif style=='A':
        b+=p('M-43 17Q-59-21-40-43Q-25-65-2-59Q29-69 43-44Q55-19 42 5L32-12 21-36Q4-18-15-29Q-23-5-32 19Z',hair)
        b+=p('M-39-42Q-66-22-55 14Q-48 31-34 35L-30 17-35-1Z',hair)
        b+=ln('M-37-32Q-20-55 2-51M9-49Q28-55 36-37',s['shine'],3)
    elif style=='B':
        b+=p('M-34-16Q-49-48-17-63Q3-78 31-60Q45-49 42-26L29-18 18-43Q-7-22-29-24L-27 7Z',hair)
        b+=p('M-33-32Q-72-37-65-1Q-62 16-74 34Q-53 33-43 19L-31-10Z',hair)
        b+=ln('M-31-43Q-7-65 20-55',s['shine'],2.4)
    else:
        b+=p('M-43 9L-53-18-36-51-1-67 34-47 43-21 23-25 3-42-11-18-31-15-30 14Z',hair)
        b+=p('M-36-37L-24-52-6-57 7-51-16-42Z',s['shine'])
    dx,dy=look
    if style=='A':
        eyeL='M-18-9Q-8-20 3-10Q-7 0-17-6Z';eyeR='M17-10Q27-18 35-8Q26-1 18-5Z'
        b+=p(eyeL,'#FFFBF0')+p(eyeR,'#FFFBF0')
        b+=e(-5+dx*2,-9+dy,4,5.4,INK)+e(27+dx,-9+dy,3.6,5.1,INK)
        b+=e(-5+dx*2-1,-11+dy,1.2,1.5,'#FFFDF4')
        b+=p('M12-6Q18 3 17 10L10 12',sh)
    elif style=='B':
        if child:
            b+=p('M-17-7Q-7-17 3-8Q-6 1-16-3Z','#FFF6E6')+p('M18-8Q27-14 34-5Q26 1 19-2Z','#FFF6E6')
            b+=e(-5+dx*2,-7+dy,3.4,4.8,INK)+e(27+dx,-6+dy,3.1,4.4,INK)+p('M12-3Q18 7 10 10',sh)
        else:
            b+=ln('M-16-9Q-6-14 1-8M19-9Q27-12 32-6',INK,2.6)
            b+=e(-5+dx*2,-7+dy,2.3,3.4,INK)+e(27+dx,-6+dy,2.1,3.1,INK)
            b+=ln('M11-7L17 9 10 11',sh,2)
    else:
        b+=p('M-22-12L-12-21 3-15-2-4-16-2Z','#FFF8E6')+p('M16-14L29-17 36-8 24-2 16-5Z','#FFF8E6')
        b+=e(-6+dx*2,-10+dy,4.2,6,INK)+e(27+dx,-8+dy,3.2,5.5,INK)
        b+=p('M10-7L19 7 9 12Z',sh)
    # Expressions change brows, eye emphasis and mouth; gaze remains directional.
    if expression=='listen':
        b+=ln('M-19-23Q-10-29 1-23M19-24L32-17',hair,3 if style!='B' else 2)
        b+=ln('M4 28Q12 24 23 26','#9D5345',2.4)
    elif expression=='joy':
        b+=ln('M-18-23Q-8-30 1-24M18-23Q25-28 33-19',hair,3)
        b+=p('M-1 23Q12 36 28 22Q22 46 8 40Q2 38-1 23Z','#8C4742')+p('M1 25Q13 34 26 25L23 31Q11 35 3 29Z','#FFF6DF')
        b+=ln('M-20 10L-25 14M34 12L38 15',sh,1.8)
    else:
        b+=ln('M-18-22Q-8-27 1-21M18-22Q26-25 33-17',hair,3 if style!='B' else 2)
        b+=ln('M3 27Q15 35 27 23','#A25B4B',2.5 if style!='B' else 1.9)
        if style=='B':b+=p('M9 29Q17 28 22 26L17 32Z','#A95E50')
    if style!='B' or child:b+=e(-16,15,8,4,'#DC7C6E','opacity=".38"')
    if not child and not second and not resident:
        b+=e(-34,22,3.5,5,'#E9B856')
        if style=='B':b+=ln('M-35 18v8','#F6D28A',3)
    if second and style=='B':b+=ln('M-24-10Q-12-20 4-12L3 1Q-12 6-23-2ZM14-12Q28-19 38-8L35 3Q24 8 15 0ZM4-9H15',hair,1.6)
    return b

def unit(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy)
    return dx/length,dy/length
def ribbon(points,widths,c):
    # A small drawing helper: variable width contour through authored joints.
    a,b,z=points;u=unit(a,b);v=unit(b,z);n=[(-u[1],u[0]),(-v[1],v[0])]
    m=(n[0][0]+n[1][0],n[0][1]+n[1][1]);ml=math.hypot(*m);m=(m[0]/ml,m[1]/ml)
    off=lambda q,k,w:(q[0]+k[0]*w,q[1]+k[1]*w)
    A=off(a,n[0],widths[0]);B=off(b,m,widths[1]);Z=off(z,n[1],widths[2])
    aa=off(a,n[0],-widths[0]);bb=off(b,m,-widths[1]);zz=off(z,n[1],-widths[2])
    mid=lambda x,y:((x[0]+y[0])/2,(x[1]+y[1])/2)
    fmt=lambda q:f'{q[0]:.2f} {q[1]:.2f}'
    return p(f'M{fmt(A)}L{fmt(mid(A,B))}Q{fmt(B)} {fmt(mid(B,Z))}L{fmt(Z)}L{fmt(zz)}L{fmt(mid(zz,bb))}Q{fmt(bb)} {fmt(mid(bb,aa))}L{fmt(aa)}Z',c)

def hand(style,x,y,angle=0,size=1,kind='relax',id='hand'):
    s=STYLES[style]
    if kind=='contact':
        d='M-6-4Q0-7 7-1L17 9Q21 13 18 16Q15 19 12 15L6 10 12 20Q14 24 10 25Q6 25 3 20L-5 11Q-9 4-6-4Z'
    elif kind=='desk':d='M-7-3Q-2-8 7-3L24 0Q29 2 25 5L12 5 24 8Q27 11 23 13L7 10Q-5 12-9 5Z'
    else:d='M-6-5Q3-7 7 1L12 16Q14 22 10 23Q6 24 4 19L1 12 1 24Q0 29-4 26L-10 14Q-13 7-9 0Z'
    b=p(d,s['skin'])+ln('M6 10L12 17M2 13L7 21',s['shade'],1.1)
    return g(id,b,f'translate({x} {y}) rotate({angle}) scale({size})')

def shoe(style,x,y,flip=1,child=False,id='shoe'):
    s=STYLES[style]
    if style=='B':
        b=p('M-13-6L11-5 15 3 35 9Q40 15 31 16H-13Q-19 11-13-6Z','#D9A477')+p('M-17 8L35 12 35 17H-17Z',s['hair'])+ln('M4 0L20 9',s['hair'],5)
    elif style=='C':b=p('M-20-7H13L24 2 42 5V20H-20Z','#FFF2CF')+p('M-20 15H42V21H-20Z',s['hair'])+p('M1-5H12V9H1Z',s['hair'])
    else:b=p('M-17-7Q-3-10 11-4L19 3 36 7Q43 15 32 18H-17Q-24 12-17-7Z','#FFFAED')+ln('M-17 14H34','#8BB6B8',2)+ln('M6 0L16 3M1 4L11 7','#E3A76D',2)
    return g(id,b,f'translate({x} {y}) scale({flip} 1)')

def adult(style,pose='stand',identity='parent',expression='warm',id='adult'):
    s=STYLES[style];C=style=='C';B=style=='B';second=identity=='second';resident=identity=='resident'
    shoulderY=-137 if B else -126 if not C else -109
    headY=s['head'];headS=s['hs'];foot=s['foot']
    shirt=s['shirt'];pants=s['pants'];shadow=s['shadow']
    if second:shirt='#2F7E8D' if style=='A' else '#CC7558' if B else '#F5C951';pants='#263F57' if not C else '#305475'
    if resident:shirt='#A8BBB4';pants='#5B7479'
    if pose in ['sit','contact']:
        legs=[([(-21,0),(66,79),(32,191)],[29,23,13]), ([(18,0),(111,71),(101,184)],[31,25,14])]
        far=[(-45,shoulderY+2),(-66,-67),(-36,8)]
        near=[(43,shoulderY),(71,-55),(128,-80)] if pose=='contact' else [(43,shoulderY),(77,-79),(6,-66)]
        turn=10 if pose=='contact' else -5
    elif pose=='walk':
        legs=[([(-18,0),(-35,112),(-92,218)],[27,21,12]), ([(19,0),(83,93),(120,207)],[29,23,13])]
        far=[(-43,shoulderY+2),(-75,-75),(-37,-16)];near=[(43,shoulderY),(82,-77),(117,-99)];turn=2
    elif pose=='turn':
        legs=[([(-20,0),(-29,113),(-33,foot-20)],[29,22,13]), ([(18,0),(41,109),(63,foot-20)],[31,23,14])]
        far=[(-42,shoulderY+2),(-60,-67),(-35,-4)];near=[(43,shoulderY),(71,-61),(123,-71)];turn=12
    else:
        legs=[([(-20,0),(-32,116),(-34,foot-20)],[29,22,13]), ([(18,0),(39,113),(58,foot-20)],[31,23,14])]
        far=[(-43,shoulderY+2),(-66,-63),(-55,6)];near=[(43,shoulderY),(64,-58),(51,10)];turn=0
    if C:
        # Blockier garments and lower centre of gravity, not an A/B recolor.
        legs=[([(q[0],q[1]*.87) for q in pts],[w*1.27 for w in widths]) for pts,widths in legs]
    ground=max(pts[-1][1]+(21 if C else 18) for pts,widths in legs)
    b=e(0,ground+3,86,8,'#ADC8C5','opacity=".3"') if pose not in ['sit','contact'] else ''
    for k,(pts,widths) in enumerate(legs):
        if B:widths=[widths[0]*.92,widths[1]*.92,widths[2]*1.14]
        if pose in ['sit','contact']:
            contour='M-40-8Q-19-24 9-6L82 60Q94 78 83 99L49 191Q37 199 22 189L45 98-30 37Q-49 19-40-8Z' if k==0 else 'M4-14Q25-24 50-1L117 48Q137 63 132 84L116 181Q111 196 91 192L87 170 98 86Q91 80 73 73L7 40Q-14 23 4-14Z'
            cloth=p(contour,shadow if k==0 else pants)
            cloth+=ln('M-19 7L65 78 34 177' if k==0 else 'M31 0L112 64 101 175','#75A29D' if not C else '#F39474',1.8,'opacity=".65"')
            if k==1:cloth+=ln('M97 70Q113 62 128 76',shadow if not C else '#AC5145',2.2)
            if C:cloth=g(id+'-geometric-seated-trouser-'+str(k),cloth,'scale(1 .87)')
        else:
            cloth=ribbon(pts,widths,shadow if k==0 else pants)+ln(f'M{pts[0][0]+6} {pts[0][1]+12}Q{pts[1][0]+6} {pts[1][1]} {pts[2][0]+3} {pts[2][1]-12}', '#75A29D' if not C else '#F39474',1.8,'opacity=".6"')
        b+=g(f'{id}-leg-{k}',cloth+shoe(style,*pts[-1],id=f'{id}-shoe-{k}'))
    upper_start=len(b)
    b+=g(id+'-arm-far',ribbon(far,[15,12,7],s['shade'])+hand(style,*far[-1],size=.88,id=id+'-hand-far'))
    # Neck is a small plane within the collar, not a tall exposed tube.
    neckTop=headY+37*headS;neckBottom=shoulderY+14
    b+=p(f'M-16 {neckTop}L-18 {neckBottom}Q0 {neckBottom+20} 19 {neckBottom-1}L15 {neckTop-4}Z',s['shade'])
    if style=='A':
        torso=p('M-19-145Q-46-147-62-123L-53-83-45-28Q-50-7-43 15Q-4 29 39 13L42-57 57-111Q45-137 18-145L6-130-6-131Z',shirt)
        torso+=p('M-45-107Q-38-76-37-33L-45 9Q-17 21 2 19L-13-42-16-130Z','#D56750','opacity=".4"')
        torso+=p('M-17-145L-7-129-23-116-29-140ZM18-145L6-130 23-116 31-138Z','#FFD4A6')
        torso+=ln('M-7-127L2 14M-33-39L-22-16M19-6L33-13','#F8B48A',2)
        for yy in [-99,-72,-45]:torso+=e(-1,yy,2.2,2.2,'#FCE3BE')
        torso+=p('M-44 10Q-7 23 39 8L37 18Q-5 31-42 20Z','#E9B65A')
    elif style=='B':
        torso=p('M-16-159Q-40-157-55-140L-65-113-46-100-42-51-48 9Q-12 31 41 10L36-55 51-109 57-128Q39-151 16-160L0-144Z',shirt)
        torso+=p('M-38-145L-29-98-37 4Q-17 18-4 16L-8-139Z',s['cloth'])
        torso+=p('M-17-159L-3-141-20-114-31-150ZM16-160L0-142 19-117 31-147Z','#FFFAE9')
        torso+=ln('M-3-137L1 10M24-71Q13-29 24 1M-33-44L-21-17','#BBA78D',1.8)
        for yy in [-103,-78,-53,-28]:torso+=e(0,yy,1.7,1.7,'#9A8F7F')
        torso+=p('M-46 8Q0 21 41 6L40 17Q-4 32-45 19Z','#BB6C4F')+r(-3,15,14,7,'#E9BD75',2)
    else:
        torso=p('M-20-130L-55-120-72-87-48-66-44 21 40 25 47-63 68-88 48-119 20-131 1-112Z',shirt)
        torso+=p('M-20-130L-12-100-16 19 6 23 6-111Z','#F5C957')
        torso+=p('M17-125L26-108 17-92 5-112ZM-20-126L-13-104-34-92-43-114Z',s['cloth'])
        torso+=p('M28-56H42V-29H28ZM-43-58H-25V-31H-43Z','#1B6B88')
        torso+=ln('M27-50H40M-41-52H-27M-16 12L-33 6',s['cloth'],3)
    if second or resident:
        # Distinct silhouette/wardrobe construction, not just another skin-colored head.
        torso=p(f'M-20 {shoulderY-12}Q-50 {shoulderY-9}-64 {shoulderY+22}L-48-89-45 19Q1 35 47 16L44-80 62 {shoulderY+27}Q47 {shoulderY-8}20 {shoulderY-13}L1 {shoulderY+8}Z',shirt)
        torso+=ln(f'M-18 {shoulderY-8}Q0 {shoulderY+26}20 {shoulderY-8}',s['cloth'],4)
        if second:torso+=p('M-34-83H-10V-56H-34Z','#D9DAB8','opacity=".5"')
    b+=g(id+'-torso',torso)
    b+=g(id+'-arm-near',ribbon(near,[16 if not B else 13,12 if not B else 10,7],s['skin']))
    # Tailored sleeve follows the upper arm rather than a rectangle pasted to the torso.
    ax,ay=near[0];bx,by=near[1];sleeveEnd=(ax+(bx-ax)*.43,ay+(by-ay)*.43)
    sleeveAngle=math.degrees(math.atan2(by-ay,bx-ax))-90
    cap=p('M-21-5Q-20-21-3-22Q15-23 21-6L22 33Q2 42-21 32Z',shirt)
    if style=='C':cap=p('M-22-6L-8-23 12-18 24-3 24 33-22 33Z',shirt)+r(-22,28,46,6,'#9FD4C6')
    else:cap+=ln('M-18 31Q2 38 19 32','#BCA88B' if B else '#F8B18B',2)
    sleeve=g(id+'-sleeve-cap',cap,f'translate({ax} {ay}) rotate({sleeveAngle})')
    b+=g(id+'-sleeve-near',sleeve)
    if pose=='contact':b+=hand(style,*near[-1],angle=0,size=.96,kind='contact',id=id+'-contact-hand')
    elif pose=='sit':b+=hand(style,*near[-1],angle=160,size=.9,kind='desk',id=id+'-desk-hand')
    else:b+=hand(style,*near[-1],angle=-25 if pose=='turn' else 2,size=.92,id=id+'-near-hand')
    f=face(style,identity,expression,(1,4 if pose=='contact' else 1))
    b+=g(id+'-head',f,f'translate(2 {headY}) rotate({turn}) scale({headS})')
    if pose in ['stand','walk','turn']:
        lean=-3 if pose=='stand' else 4 if pose=='walk' else 5
        b=b[:upper_start]+g(id+'-upper-body',b[upper_start:],f'rotate({lean} 0 0)')
    return g(id,b)

def child(style,pose='stand',expression='joy',id='child'):
    s=STYLES[style];C=style=='C';B=style=='B';foot=169
    if pose=='contact':
        hip=15 if C else 40
        near=[(-29,-95),(-29,-35-hip) if C else (-42,-19-hip),(-58,-60-hip)]
    else:near=[(-29,-95),(-47,-51),(-55,-15)]
    far=[(29,-93),(43,-46),(35,-1)]
    b=e(0,foot+4,62,8,'#ADC8C5','opacity=".32"')
    legpoints=[([(-16,0),(-24,73),(-27,151)],[19,14,9]), ([(15,0),(28,71),(37,150)],[21,15,10])]
    if B:
        # Shorts, visible knee/calf shapes and socks distinguish child from adult.
        for k,(pts,w) in enumerate(legpoints):
            b+=ribbon(pts,[w[0]*.65,w[1]*.65,w[2]],s['skin'])+r(pts[-1][0]-9,136,18,18,'#E5E9D7',3)+shoe(style,*pts[-1],child=True,id=f'{id}-shoe-{k}')
            b+=p(f'M{pts[0][0]-20}-8L{pts[0][0]+21}-8 {pts[1][0]+18} 67 {pts[1][0]-18} 67Z','#2C5E72')
    else:
        for k,(pts,w) in enumerate(legpoints):
            b+=ribbon(pts,w,s['shadow'] if k==0 else s['pants'])+shoe(style,*pts[-1],child=True,id=f'{id}-shoe-{k}')
    b+=ribbon(far,[10,8,5],s['shade'])+hand(style,*far[-1],size=.6,id=id+'-far-hand')
    b+=p('M-12-112L-13-94Q0-79 14-95L12-115Z',s['shade'])
    if style=='A':
        body=p('M-13-105Q-34-102-45-80L-34-53-32 12Q0 28 35 13L32-55 43-78Q34-100 13-106L0-94Z',s['child'])+p('M-12-101L-1-92 12-103 18-94Q0-78-18-94Z','#FFF2C5')
        body+=p('M-23-51L-3-61 21-51 20-29-20-29Z','#F6D57D')+ln('M-19-49L0-39 17-49','#C9903D',1.8)
        body+=ln('M-24 8Q0 18 27 8','#C99A48',2)
    elif style=='B':
        body=p('M-13-106Q-32-104-42-83L-32-55-32 15Q0 24 33 12L32-51 41-79Q32-103 13-106L0-95Z',s['child'])+p('M-13-106L0-95-12-82-23-99ZM13-106L0-95 13-82 23-99Z','#EFA27F')
        body+=ln('M0-93V-55M-24-24L-17-9','#B95848',1.8)+e(0,-82,1.5,1.5,'#F8D4AE')
    else:
        body=p('M-14-109L-37-94-49-65-31-50-32 23 37 19 32-47 48-67 34-96 14-110 0-94Z',s['child'])+p('M-13-109L-25-96 0-78 23-98 13-108 0-96Z','#FFE4A0')
        body+=p('M-18-24L0-38 22-25 17-2-15-1Z','#D8A73E')+ln('M-8-80V-55M9-80V-56','#997944',2.5)
    b+=g(id+'-clothes',body)+g(id+'-arm-near',ribbon(near,[10,8,5],s['skin']))
    if pose=='contact':b+=hand(style,*near[-1],angle=180,size=.61,kind='contact',id=id+'-contact-hand')
    else:b+=hand(style,*near[-1],size=.6,id=id+'-near-hand')
    hscale=.66 if B else .77 if not C else .91
    b+=g(id+'-head',face(style,'child',expression,(1,-3 if pose=='contact' else -1)),f'translate(0 -132) rotate({-9 if pose=="contact" else -4}) scale({-hscale} {hscale})')
    return g(id,b)

def desk_prop(style):
    return g('desk-prop',p('M-130-69L20-100 83-62-67-31Z','#DDB887')+p('M-130-69V-58L-67-20 83-52V-62L-67-31Z','#BA946C')+ln('M-112-53V196M57-43L76 187',INK,7)+p('M-101-77L-30-91-43-146-114-132Z','#2B6176')+p('M-101-77L-30-91 0-72-70-57Z','#316F7D')+ln('M-107-122L-52-133M-103-111L-66-119','#75B4BB',2))

def chair(id='chair'):return g(id,p('M-51-51Q-71-62-76-39L-67 8 4 28 54 13V1L-49-23Z','#D0A27C')+ln('M-53 9L-63 194M31 19L54 190',INK,7))

def pose_pair(style,id='pair'):
    hip=15 if style=='C' else 40
    return g(id,chair(id+'-chair')+adult(style,'contact',id=id+'-parent')+g(id+'-child-placement',child(style,'contact',id=id+'-child'),f'translate(205 {hip})'))

def svg_doc(body,w,h,label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{escape(label)}"><style>@font-face{{font-family:Display;src:url(assets/display.ttf)}}text{{font-variation-settings:"wght" 600,"wdth" 95;letter-spacing:.3px}}</style>{body}</svg>'''

def sheet(style):
    s=STYLES[style];b=r(0,0,1800,1600,PAPER)
    b+=tx(66,72,20,'VIDEO-34 / CHARACTER RESET / '+style,'#447E85',attrs='letter-spacing="3"')+tx(66,132,43,s['name'])+tx(68,174,22,s['sub'],'#637B7D')
    b+=ln('M66 205H1734','#D2E0DA',2)+tx(68,244,17,'01   CAST / THREE-QUARTER FULL BODY','#597B7D',attrs='letter-spacing="2"')
    # Cast has a shared baseline, different identities and age proportions.
    norm=.83 if style=='B' else .98 if style=='C' else .86
    castY=492 if style=='B' else 515 if style=='C' else 497
    b+=g('cast-parent',adult(style,id='cast-parent-art'),at(186,castY,norm))
    b+=g('cast-child',child(style,id='cast-child-art'),at(390,551,.94))
    b+=g('cast-second',adult(style,identity='second',id='cast-second-art'),at(613,castY,norm))
    b+=g('cast-resident',adult(style,identity='resident',id='cast-resident-art'),at(829,710-(710-castY)*.86,norm*.86))
    for x,slabel in [(117,'PARENT'),(341,'CHILD / 7–9'),(548,'SECOND ADULT'),(765,'RESIDENT')]:b+=tx(x,770,16,slabel,'#6D8584')
    b+=ln('M960 250V780','#D2E0DA',2)+tx(1012,245,17,'02   FACE / EXPRESSION','#597B7D',attrs='letter-spacing="2"')
    for x,expression,label in [(1112,'warm','WARM / PRESENT'),(1372,'listen','LISTEN / CONSIDER'),(1615,'joy','JOY / RECOGNITION')]:
        b+=g('expression-'+expression,face(style,'parent',expression,(1,1)),at(x,407,1.85))
        b+=tx(x-99,539,15,label,'#597B7D')
    # Child face close-up clarifies identity relative to the parent's face vocabulary.
    b+=g('child-face-closeup',face(style,'child','joy',(1,-1)),at(1103,658,1.04))
    b+=tx(1190,640,18,'AGE + IDENTITY')+tx(1190,677,16,'Child cheeks, hair, gaze and wardrobe','#667F7E')+tx(1190,705,16,'are designed separately from the adult.','#667F7E')
    b+=ln('M66 815H1734','#D2E0DA',2)+tx(68,856,17,'03   POSE / WEIGHT / CONTACT','#597B7D',attrs='letter-spacing="2"')
    # Lower panels are intentionally large, with no scene decoration hiding anatomy.
    b+=tx(74,909,19,'SEATED / DESK SUPPORT')
    b+=g('pose-seated',chair('pose-seated-chair')+adult(style,'sit',id='seated-parent')+desk_prop(style),at(225,1236,.94))
    b+=tx(520,909,19,'WALK / WEIGHT SHIFT')+g('pose-walk',adult(style,'walk',id='walk-parent'),at(636,1216,norm))
    b+=tx(920,909,19,'TURN / ATTENTION')
    turnbody=adult(style,'turn',expression='listen',id='turn-parent')+g('turn-child-placement',child(style,expression='listen',id='turn-child'),'translate(205 81)')
    b+=g('pose-turn',turnbody,at(990,1208,.8))
    b+=tx(1355,909,19,'CONTACT / SHARED TARGET')+g('pose-contact',pose_pair(style,'contact-pair'),at(1431,1257,.79))
    for x,caption in [(73,'Pelvis rests on seat; knees bend forward.'),(520,'Opposing limbs; feet have different jobs.'),(920,'Head and body turn toward a person.'),(1355,'Bent elbows; adult and child hands overlap.')]:
        b+=tx(x,1505,14,caption,'#718A87')
    b+=ln('M66 1533H1734','#D2E0DA',2)+tx(68,1570,16,'ORIGINAL EDITABLE VECTOR / STATIC DESIGN STUDY / AWAITING CHARACTER DESIGN REVIEW','#64827F')
    return svg_doc(b,1800,1600,'Direction '+style+' character design sheet')

def save_art(name,svg,w,h):
    (ROOT/(name+'.svg')).write_text(svg,encoding='utf8')
    (ROOT/(name+'.html')).write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width={w},height={h}"><title>{name}</title><link rel="icon" href="data:,"><style>html,body{{margin:0;width:100%;height:100%;overflow:hidden}}svg{{width:100%;height:100%;display:block}}@font-face{{font-family:Display;src:url(assets/display.ttf)}}</style></head><body>{svg}<script>document.fonts.load('24px Display').then(()=>document.fonts.ready).then(()=>window.artReady=true)</script></body></html>''',encoding='utf8')

def context(style='A'):
    # Read-only extraction: leave environment, camera, floor, desk and terrace unchanged.
    tree=ET.fromstring((R2/'S08-B.svg').read_text(encoding='utf8'))
    parentmap={c:parent for parent in tree.iter() for c in parent}
    for node in list(tree.iter()):
        if node.get('id') in ['s08-parent','s08-child','s08-family-type']:
            parentmap[node].remove(node)
    camera=next(x for x in tree.iter() if x.get('id')=='s08-camera')
    # R2 chair lived inside its parent group; the new parent comes with its own seat.
    pair=pose_pair(style,'context-pair')
    pair=g('new-parent-child-placement',pair,'translate(330 1190) scale(1.22)')
    wrap=ET.fromstring('<g xmlns="http://www.w3.org/2000/svg">'+pair+'</g>')
    # Place actors behind the original foreground desk, preserving its visible support.
    desk=next(x for x in camera if x.get('id')=='s08-desk');camera.insert(list(camera).index(desk),wrap)
    ET.register_namespace('','http://www.w3.org/2000/svg')
    tree.set('width','1080');tree.set('height','1920');tree.set('aria-label','Original R2 workspace, new direction '+style+' parent-child static contact')
    return ET.tostring(tree,encoding='unicode')

def comparison():
    # Actual editable R2 vector characters are used for comparison, not invented proxies.
    root=ET.fromstring((R2/'S08-B.svg').read_text(encoding='utf8'))
    defs=next(x for x in root if x.tag.endswith('defs'))
    parent=next(x for x in root.iter() if x.get('id')=='s08-parent')
    childnode=next(x for x in root.iter() if x.get('id')=='s08-child')
    old=ET.tostring(defs,encoding='unicode')+ET.tostring(parent,encoding='unicode')+ET.tostring(childnode,encoding='unicode')
    b=r(0,0,1800,940,PAPER)+tx(50,67,22,'VIDEO-34 / CHARACTER RESET / ACTUAL VECTOR COMPARISON','#507D81')
    b+=tx(50,124,40,'Rejected R2 and three new directions')
    b+=ln('M450 170V850M900 170V850M1350 170V850','#D3DFD9',2)
    b+=tx(45,204,24,'R2 / REJECTED','#B76B58')
    b+=g('rejected-r2',old,'translate(-50 -215) scale(.65)')
    for i,style in enumerate(['A','B','C']):
        x=500+i*450;b+=tx(x,204,24,'OPTION '+style)
        scale=.86 if style=='A' else .88 if style=='B' else .93
        ground=187 if style=='C' else 209
        body=pose_pair(style,id='compare-'+style)
        b+=g('compare-option-'+style,body,at(x+80,750-ground*scale,scale))
    b+=tx(50,901,17,'Seated contact comparison. Adult drawings normalized to roughly 400px high for review; no physical size comparison.','#68837F')
    return svg_doc(b,1800,940,'Rejected R2 versus three new character designs')

def scene_scale(style):
    b=r(0,0,1080,1920,PAPER)+tx(65,120,30,'OPTION '+style+' / SCENE-SIZE CHARACTER PROOF')
    b+=tx(65,175,22,'1080 × 1920 / static silhouette, face and clothing check','#6E8584')
    b+=ln('M90 1590H1000','#CEDFD9',3)
    body=adult(style,id='scale-parent')+g('scale-child-placement',child(style,id='scale-child'),'translate(205 81)')
    b+=g('scene-size-cast',body,at(320,1130,1.7))
    return svg_doc(b,1080,1920,'Option '+style+' actual scene-size character proof')

def build():
    for style in STYLES:
        save_art('option-'+style,sheet(style),1800,1600)
        save_art('scene-scale-'+style,scene_scale(style),1080,1920)
    save_art('R2-vs-options',comparison(),1800,940)
    save_art('S08-interaction-A',context('A'),1080,1920)
    (ROOT/'directions.json').write_text(json.dumps(STYLES,indent=2),encoding='utf8')
    print('Built A/B/C sheets, actual R2 comparison, and context A candidate')

if __name__=='__main__':build()
