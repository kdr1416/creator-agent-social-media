"""R1 original scene redesign. Uses project drawing helpers, no new dependencies."""
from pathlib import Path
import sys, shutil, re
import xml.etree.ElementTree as ET
sys.stdout.reconfigure(encoding='utf-8')
from build_pilot_art import path,line,ellipse,group,plant,window,balcony
P=Path(__file__).resolve().parents[1]
OLD=P/'build/revision-r1-before'
def wrap(c,label):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 1280" role="img" aria-label="{label}"><defs>
 <linearGradient id="sky" x2="0" y2="1"><stop stop-color="#098ee6"/><stop offset="1" stop-color="#c6f4ff"/></linearGradient>
 <linearGradient id="sea" x2=".4" y2="1"><stop stop-color="#18d4d6"/><stop offset="1" stop-color="#0066b5"/></linearGradient>
 <linearGradient id="stone" x2="1" y2=".6"><stop stop-color="#fff8ed"/><stop offset="1" stop-color="#eac791"/></linearGradient>
 <linearGradient id="floor" x2="0" y2="1"><stop stop-color="#eff9ff"/><stop offset="1" stop-color="#d2e4ef"/></linearGradient>
 <linearGradient id="room" x2="1" y2="1"><stop stop-color="#f6fcff"/><stop offset="1" stop-color="#d4ecf6"/></linearGradient>
 <linearGradient id="topShade" x2="0" y2="1"><stop stop-color="#092740"/><stop offset=".65" stop-color="#092740" stop-opacity=".95"/><stop offset="1" stop-color="#092740" stop-opacity="0"/></linearGradient>
 </defs>{c}</svg>'''

def s03():
 raw=(OLD/'assets/illustration/S03-coast.svg').read_text(encoding='utf-8')
 # Retain the topology, rebuild surface detail/characters and staging rather than only color.
 root=ET.fromstring(raw.replace('data-layout-allow-overflow>', 'data-layout-allow-overflow="true">'));ns={'s':'http://www.w3.org/2000/svg'}
 world=root.find("s:g[@id='world']",ns)
 for el in list(world):
  if el.get('id')=='family-link': world.remove(el)
 color={'#c66f52':'#ff795d','#bd7356':'#007bbb','#d9c397':'#fef6e7','#e7d2a8':'#f7fbff','#628270':'#005cba','#be674e':'#fb644e','#d7c098':'#ffffff','#4e756b':'#09558f','#c78052':'#ffc93a','#304b58':'#102c4d','#344953':'#092740','#b76f50':'#ff7658','#cd8967':'#fb9475','#bd7057':'#ff7053','#b7634d':'#cf4e39','#b7a080':'#c2a97f','#b99772':'#bd9365','#f6dfb9':'#ffffff','#f8e6c4':'#fffdf5','#c3a178':'#c49a68','#e9d5ad':'#fffefa','#345b59':'#083f72','#477f74':'#056a9a','#416e6a':'#007ba2','#355b6a':'#0e457b','#668a7b':'#56c9da','#52785c':'#168681','#416d5c':'#005c67','#3e5753':'#142e4e','#344d4c':'#173855'}
 for e in world.iter():
  if e.get('fill') in color:e.set('fill',color[e.get('fill')])
  if e.get('stroke') in color:e.set('stroke',color[e.get('stroke')])
 # Distinct silhouettes: sunhat/long hair, runner athletic outfit, family dress/hair.
 def add(id,markup):
  g=next(x for x in world.iter() if x.get('id')==id)
  inner=list(g)[0] if id in ['walker-a','walker-b','runner','family-parent','family-other','family-child'] else g
  for x in ET.fromstring('<g>'+markup+'</g>'):inner.append(x)
 add('walker-a',path('M-24-162q24-12 47 0l-1 5h-48Z','#fff7e4')+path('M-13-163l5-15h18l6 15Z','#f9c650')+line('M-17-126l33 44','#132e4b',3)+path('M11-96h14v20H11Z','#ef7959'))
 add('walker-b',path('M-15-158q-16 15-8 40l12-8 4-27Z','#122b45'))
 add('runner',path('M-16-124l9-3 4 33 14-32 6 3-2 52-33 1Z','#ff684d')+line('M-17-162l26-5','#112a45',5))
 add('family-other',path('M-12-163q-19 22-11 42l16-12 7-23Z','#122b45')+path('M-17-85l-9 28h52L17-85Z','#0069bc'))
 # Architecture refinement: shutter slats, lintels, cornice and blue ceramic details.
 detail=''
 for x,y in [(43,151),(209,151),(55,360),(226,364)]:
  detail+=path(f'M{x-8} {y-5}h67v7h-67Z','#fff7e9')
  for k in range(5):detail+=line(f'M{x+3} {y+23+k*10}h43','#58a6b8',1.5)
 for yy in [104,315]:detail+=path(f'M0 {yy}h334v5H0Z','#fffefa')
 detail+=line('M338 80l70 27v374','#b88e5e',3)
 detail+=path('M334 50l89 7v15l-89-7Z','#e6c796')
 # Accent path stays tied to the same ground plane.
 detail+=line('M328 988Q427 927 507 868','#42eced',5,'id="run-trail" stroke-dasharray="230" stroke-dashoffset="230"')
 detail+=line('M552 1090Q594 1056 634 1120','#ffd24c',3,'id="family-arc" stroke-dasharray="150" stroke-dashoffset="150"')
 serialized=ET.tostring(world,encoding='unicode').replace('ns0:','').replace(':ns0','')
 serialized=serialized.replace('</g>', '</g>',1)
 # Put architectural accents behind people, not across their faces.
 i=serialized.find('>')+1
 serialized=serialized[:i]+detail[:detail.index('<path d="M328')]+serialized[i:]
 serialized=serialized[:-4]+detail[detail.index('<path d="M328'):]+serialized[-4:]
 return wrap(serialized,'Modern Mediterranean coastal world, original R1 artwork')

def s08():
 c=path('M0 0H720V1280H0Z','url(#room)')
 c+=path('M354 100H720V982H354Z','#0c477b')+path('M373 126H720V955H373Z','url(#sky)')
 c+=path('M373 510H720V960H373Z','url(#sea)')
 c+=path('M373 501l66-31 52 18 53-42 66 16 110-10v72H373Z','#fff9e9')
 c+=path('M433 476v-37h26v37m83-19v-44h32v44m76 8v-30h37v30','#eac58b')
 c+=line('M445 563h88m49 32h97m-230 50h91','#b5faff',3)
 c+=path('M373 860l347-23v163H373Z','#e5f4f8')+line('M374 858l346-23','#fff',14)
 for x in range(395,701,50):c+=line(f'M{x} 865v122','#a7c5d2',5)
 c+=path('M348 113h25v886h-25Z','#fff')
 c+=path('M0 1000H720V1280H0Z','url(#floor)')
 c+=path('M373 987l347-14v307H90Z','#ffffff','opacity=".7"')
 c+=line('M0 1160l720-90M170 1280l240-284M540 1280l25-292','#b9d5e2',2)
 c+=path('M46 306h206v226H46Z','#082d52')+path('M58 318h182v202H58Z','#007ebd')+ellipse(190,365,24,24,'#ffd24c')+path('M58 491q76-114 182-31v60H58Z','#25ced1')
 c+=line('M63 589h185','#143b58',8)+path('M79 542h13v45H79Z','#ff7059')+path('M96 533h15v54H96Z','#047db5')+plant(216,579,.55)
 c+=ellipse(316,1118,137,24,'#133c5f','opacity=".13"')+ellipse(489,1117,61,14,'#133c5f','opacity=".12"')
 c+=line('M233 908l-19 207m143-207 26 205M221 1025h148','#133a5b',10)
 c+=path('M220 805q58-23 129-7l11 117-129 8Z','#08759a')+path('M230 909h132v22H230Z','#123e60')
 # Bent thighs and shins with a readable seated pelvis, not standing legs.
 c+=path('M274 892q43-21 69 14l-69 69 30 120-27 4-48-129q-4-15 9-27Z','#153d65')
 c+=path('M312 903q33-2 48 21l45 52-22 121h-28l13-108-68-44Z','#08659c')
 c+=path('M274 1086h29l6 24h-57q-8-8 22-24Z','#f7fbff')+path('M354 1087h27l29 18q3 11-56 6Z','#f7fbff')
 c+=line('M253 1114h56m45 0h56','#152f4c',4)
 c+=path('M273 726q37-19 65 7l19 167q-57 19-96-1l4-123Z','#ffffff')
 c+=path('M326 749q-1 99 18 143l-22 7-14-145Z','#d5eaf2')+line('M284 740l-5 139m4-9h27','#bdd4e0',2)
 c+=path('M290 698h25v34q-10 12-25-2Z','#c88a68')
 c+=line('M278 750Q259 779 267 806L239 824','#cf9674',22,'id="parent-far-arm"')
 c+=path('M270 734q-14 7-20 40l29 12 16-36Z','#f8fdff')
 head=path('M269 649q-1-41 33-43 39 0 43 37l-4 38q-4 31-35 37-31-4-37-35Z','#d69e7b')
 head+=path('M267 674q-18-29-3-48 2-26 31-29 42-9 55 31 6 25-9 41l-3-30q-29 9-56-13l-8 46Z','#102d44')
 head+=ellipse(260,619,18,20,'#102d44')+path('M276 676q-15-11-14 5 2 12 16 10Z','#d69e7b')
 head+=line('M328 660l7 13-8 3','#ac6c50',2)
 head+=group(line('M283 651q6-4 12 0m16-1q6-3 11 1','#173a4c',2)+ellipse(289,658,2.4,3,'#102d44')+ellipse(317,658,2.4,3,'#102d44'),'','parent-gaze')
 head+=line('M299 690Q306 692 314 689','#9d5748',2.5,'id="parent-smile"')+ellipse(322,681,8,4,'#d27d6b','opacity=".5"')+ellipse(273,691,3,4,'#ffd35a')
 c+=group(head,'','parent-head')
 c+=line('M82 863l-13 245m219-238 18 221','#123f60',10)
 c+=path('M43 840l244-26 86 40-249 34Z','#fff')+path('M43 840v14l81 44 249-30v-14l-249 34Z','#116d9b')
 c+=path('M170 835l107-13 45 19-109 15Z','#123e61')+line('M185 837l91-9m-78 15 90-9','#43cdda',2)
 lid=path('M0 0L-28-112 82-126 110-14Z','#102e50')+path('M5-10L-18-104 75-115 99-21Z','#157cb3')+line('M-9-91l69-9m-65 20 44-6m-39 20 59-8','#69dfea',3)
 c+=group(lid,'translate(170 835)','laptop-position')
 c+=line('M330 750Q357 789 338 810L271 827','#d69e7b',23,'id="parent-near-arm"')
 c+=path('M321 735Q343 728 355 770L330 783 309 750Z','#edf8ff','id="parent-near-sleeve"')
 c+=path('M266 820q-16-2-22 5l-2 7 24 4 13-8Z','#d69e7b','id="parent-hand"')
 # Child is closer and taller: the parent can reach with normal upper/forearm lengths.
 c+=path('M465 1001l-9 101h22l18-96Z','#244869')+path('M489 1007l20 95h22l-14-105Z','#0b659b')
 c+=path('M453 1097h27l-1 17h-39q-5-8 13-17Z','#fff')+path('M508 1098h24l16 15h-41Z','#fff')
 c+=path('M460 900q26-16 53 3l15 101q-37 17-72-1Z','#ff7156')+path('M498 916l16-5 10 83-19 10Z','#df4e40')
 c+=path('M476 878h22v27q-10 9-22-1Z','#d8a17c')
 child=path('M456 834q-4-35 28-39 37-3 42 35l-3 35q-5 29-34 31-33-3-33-34Z','#dba580')
 child+=path('M454 850q-12-26 3-43 14-25 38-20 36 2 39 34l-8 25-13-26q-28 8-43-7l-9 34Z','#13334a')
 child+=ellipse(470,848,2.5,3,'#123047')+ellipse(492,848,2.5,3,'#123047')+line('M465 855l-5 10 7 2','#ae7053',2)+line('M474 879Q481 881 489 877','#a4614c',2.5,'id="child-smile"')+ellipse(501,868,7,4,'#dc806a','opacity=".5"')
 c+=group(child,'','child-head')
 c+=line('M511 918l26 37-4 26','#dba580',16)
 c+=line('M464 918Q449 945 438 947L423 938','#dba580',17,'id="child-near-arm"')+ellipse(423,938,9,8,'#dba580','id="child-hand"')
 c+=plant(652,1128,1.35)
 c+=line('M389 883Q411 852 438 886','#ffc637',3,'id="contact-arc" stroke-dasharray="100" stroke-dashoffset="100"')
 return wrap(c,'R1 modern home with newly drawn anatomically proportioned parent and child')

if __name__=='__main__':
 for sid,name,draw in [('S03','coast',s03),('S08','home',s08)]:
  (P/f'assets/illustration/{sid}-{name}.svg').write_text(draw(),encoding='utf-8')
 fonts=P/'assets/fonts';fonts.mkdir(exist_ok=True)
 shutil.copy2('C:/Windows/Fonts/arialbd.ttf',fonts/'pilot-bold.ttf')
 print('R1 redesigned artwork and existing local font ready')
