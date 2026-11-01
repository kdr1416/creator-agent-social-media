---
workflow: general-video
mode: autonomous
duration:15
music: none
---

# First15s reference reconstruction

## Frame1
status: outline
src: compositions/yp-street.html
frame_id: yp-street
duration: 4.233
blueprint: compose
rules: viewport-change, svg-path-draw
scene: Recreate the reference traffic opening closely.
voiceover: none
sfx: none
transition_in: none
Reference images: reference/ref-00.png,ref-01.png,ref-02.png,ref-06.png,ref-08.png. Source coordinates are360×640; double all coordinates.
Scene1(0–0.45s): a CLOSE view of orange bean rider on white scooter rapidly pulls back to full street. Lavender city at y560–850, peach upper sky, road bottom. Target full-frame stage matches ref02.
Scene2(.45–2.5s): caption centred x360,y220 'Đã học trung tâm rồi...' regular36px. White-on-red slightly tilted strip at x90,y282,w540,h60 'giờ lại phải ôn IELTS?'; pops in at.65s. Tall school at x460,y510 with clock roof and sign 'TRUNG TÂM', source attached 'LỚP18:30' sign nearby. Many white scooters across bottom3–4 staggered rows fill frame from y850 to1280 (their source extends to bottom; do not add empty footer). Hero orange helmet bean on central scooter around x290,y970. Gray road lane marks, moving background riders. Repeated scene props must be detailed enough and bright as source. Source vector glyph font moderate notheavy.
Scene3(1.45–2.7): Three compact small white outlined problem labels stack aroundx430,y385: '× Kẹt xe','× Trễ lớp18:30','× Học lại từ đầu', reveals staggered. These reproduce actual source labels, not genericcards.
Scene4(3.05–4.233): burst text/green strip 'Về nhà tự học!' accompanies hero scooter accelerating to right; motion/speed streaks and minor traffic response. Main reference includes 'BÍP' speech bursts. Warm saturated orange bean, blue/pink/green background riders. Build in SVG layers, YP kit available. Need read reference frame images via view_image (not docs only).
Don't replace source full environment with map or icons. All runtime animation one timeline. Camera on wrapper, captions outside camera after pullback ifneeded.

## Frame2
status:outline
src:compositions/yp-night.html
frame_id:yp-night
duration:1.1
blueprint:compose
rules:viewport-change
scene:Night exterior with warm window
voiceover:none
sfx:none
transition_in:source-like directional drift
Reference ref09.png,ref10.png. Full night sky navy with small stars and pale yellow moon x580,y150. Central house fromx120,y600 to620,y1030: cream wall, terracotta triangle roof, small chimney, brown door left, glowing window right with orange mascot and laptop silhouette inside. Tree left, groundgreen below960, warm window pool of light on ground. Small red side sign 'NHÀ ĐÂU'. Caption 'Về nhà tự học...' x360,y210 regular36white. Scene starts with smooth slight zoom-in on house then pushes toward lit window near end to motivate room cut. No full-frame source image used. Rebuild vector shapes and window silhouettes. Timing very short1.1s, don't spend half blank.

## Frame3
status:outline
src:compositions/yp-room.html
frame_id:yp-room
duration:4.067
blueprint:compose
rules:svg-path-draw
scene:Room study fear -> self-study centre arrives
voiceover:none
sfx:none
transition_in:window-to-room
Reference ref11.png,ref12.png,ref13.png,ref14.png,ref15.png,ref16.png,ref18.png. Match reference room: pale lilac wall above y1040, tan floor, pink rug ellipse x40..485,y1100–1180. Large window x370,y405,w300,h320 (night sky, distant buildings, moon), salmon curtains, shelf/books x60..310,y420, clockx310,y510, heart picturex80,y600. Plantx620,y965 withpot below1040. Cylinder desk blue/teal x220,y980,w180,h150; laptop touches orange mascot hand and barrel surface. Mascot wearing redheadband/body x110,y820,width170 approx, not human. Protagonist leans/works at keyboard with small distress marks; hands must connect not float.
Scene1(0–.7): caption 'Về nhà tự học...' atx360,y220. Redstrip beneathx170,y285,w380,h60 reveals 'mà sợ lạc hướng!'.
Scene2(.7–1.8): small yellow/pink/blue paper notes appear on wall around shelf/window: 'Học gì trước?','Ai chấm bài?','Hỏi ai đây?' at source-like positions. Mascot distressed with sweatdrops, expressive face.
Scene3(1.9–3.2): redstrip/problem notes leave; caption replaces with 'Không muốn đến trung tâm?' and orange strip 'Trung tâm tự tìm tới!'. School miniature appears IN the window with speech 'THÍCH!', as observedref15/16. Keep curtain/window constant.
Scene4(3.55–4.067): tiny school companion hops out toward mascot/laptop, anticipation for nextscene; room props remain. No paragraphs, no UIcards. Keep full-height source framing.

## Frame4
status:outline
src:compositions/yp-laptop.html
frame_id:yp-laptop
duration:1.9
blueprint:compose
rules:viewport-change
scene:Large laptop introduces course, happy mascot and school companion
voiceover:none
sfx:none
transition_in:source push
Reference ref19.png,ref20.png,ref21.png,ref22.png. Pale lilac ground, floorline y1055 tanbottom. Giant laptop body x40,y350,w640,h440 with screen/imageassets/laptop-ui.png inside x60,y376,w600,h390. Do not use entire source video frame; UI crop is intentionally supplied actual texture. Laptop dark narrow bezel, cream screen, silverkeydeck and copperbase at y810–850. Caption centred atx360,y220 'Tự học tại nhà'. Orange strip x55,y280,w610,h55 'với Khoá YouPass Intensive' (regularwhitefont36, slightrotation). In source initial laptop expands in by9.4–9.8s and papercontent lands around10s. During yourlocal0–.35 caption/strip builds and screenshot reveals on screen; brief tilt/settle. On floor mascot atx140,y960,s~1.1 atop yellow cylindrical seat, armsraised (sharedkit canonicalmascot ~100x160). Pinkrug aroundx30..470,y1100. Smiling schoolcompanion atx565,y950,s.85, tiny legs and arms, bobs/gestures at product. Small star shapes above characters. Most ofduration hero product stays large and readable; avoid tinyfloating laptop or generic icon. Finalposition should matchref21 closely.

## Frame5
status:outline
src:compositions/yp-study.html
frame_id:yp-study
duration:3.7
blueprint:compose
rules:svg-path-draw,viewport-change
scene:Study Plan product collage and weekly progress
voiceover:none
sfx:none
transition_in:source-like wipe
Reference ref23.png,ref24.png,ref25.png,ref26.png,ref27.png,ref28.png,ref29.png. Softcream background, slightwarmvignette no brownink. Atx170,y215 smallgreen1/5 counter next to brightbluewhite 'STUDY PLAN' strip x230..570,y220–275 slighttilt. Under it centredregular heading 'Lộ trình xếp sẵn từng tuần' at y320 and smaller 'mở ra là biết hôm nay học gì' at y365. Actual source main UI assets/study-ui.png, display fromx45,y400 width630,height275 with slightlytilted whitephysical screenshot page, thin darkoutline and yellowtape at topcorners. UI reveallocal.2–.6. Sourceweekline bottom y1145: eight smalloutlined circles W1..W8 x100..620, roughthinconnector; labels small24. Mascot walks/hops fromW1 toW8 as dots fillgreen. Headline/document inupperhalf, pathmascot nearbottom, preserve source-specificlargeinterstitialspace (reconstruction, not genericnewlayout). Atlocal1.2 actualassets/progress-ui.png card enters atx400,y600 width280,height244 slighttilt/tape; it depicts realUI not a genericfeaturebox. MainUI tickmarks come on at x470,y470. Orange ellipse annotation draws over mainUI 'Ứng dụng...' row at~local2.0. At~local2.65 a smallwhiteoutlinedphysicalnotice x50,y720 w290,h95 pops in '16' large darkgreen + 'tuần' smaller, tiny 'lộ trình mẫu' allowed only ifsourceexact. Show '16 tuần' clearly; preserve originalmeaning notnewclaim. Mascot gives armupreaction once reaches W8 around3.0. Don't end on fade/black; continue finalsourcepose to15s. Fullcomposition bottomfooter not added.
