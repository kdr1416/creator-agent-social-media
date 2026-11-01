"""Rebuild the isolated, editable ending study from its original vector assets."""
from pathlib import Path
import re, json, shutil, wave, hashlib

P = Path(__file__).resolve().parent
B = P.parent / 'tran-minh-nhat-director-handoff'
for directory in ['assets', 'renders', 'qa']:
    (P / directory).mkdir(exist_ok=True)
for name in ['gsap.min.js', 'segoe-ui-black.ttf', 'arial.ttf']:
    shutil.copy2(B / 'build/scenes/scene_16/assets' / name, P / 'assets' / name)
source = B / 'build/scenes/scene_16/index.html'
old = source.read_text(encoding='utf-8')
svg = re.search(r'(<svg class="art".*?</svg>)', old, re.S).group(1)
svg = svg.replace('transform="translate(320, 640)"', 'transform="translate(0,0)"')
svg = svg.replace(' transform-origin="95 45"', '').replace(' transform-origin="38 45"', '')
with wave.open(str(B / 'inputs/full_voice.wav'), 'rb') as voice:
    voice.setpos(1448462)
    pcm = voice.readframes(188338)
    params = voice.getparams()
with wave.open(str(P / 'assets/voice.wav'), 'wb') as voice:
    voice.setparams(params)
    voice.writeframes(pcm)
originals = [source, B / 'build/scenes/scene_17/index.html', B / 'inputs/full_voice.wav']
hashes = {str(x): hashlib.sha256(x.read_bytes()).hexdigest() for x in originals}
audit = P / 'qa/source-before.json'
if not audit.exists():
    audit.write_text(json.dumps(hashes, indent=2), encoding='utf-8')

art = '''<svg class="art" viewBox="0 0 720 1280" aria-label="Cuốn sổ mở thành thế giới giấy">
<defs><filter id="soft"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#6C5480" flood-opacity=".15"/></filter></defs>
<ellipse cx="360" cy="961" rx="260" ry="25" fill="#BCA3CB" opacity=".16"/>
<g id="folio-camera" data-layout-allow-overflow="true">
<g id="cover-under"><path d="M92 770L353 820L640 741L640 866L355 965L92 898Z" fill="#087BC1" stroke="#30313B" stroke-width="3"/><path d="M353 820L355 965" stroke="#045E94" stroke-width="6"/></g>
<g filter="url(#soft)">
<g id="fold-left"><path d="M92 762L272 720L272 865L92 907Z" fill="#FFFDF5" stroke="#5C4A65" stroke-width="2.5"/><path d="M92 897L272 855L272 865L92 907Z" fill="#ECE2D4"/></g>
<g id="fold-middle"><path d="M272 720L453 775L453 920L272 865Z" fill="#F2E8F0" stroke="#5C4A65" stroke-width="2.5"/><path d="M272 720L272 865" stroke="#D5BFD7" stroke-width="3"/></g>
<g id="fold-right"><path d="M453 775L635 714L635 859L453 920Z" fill="#FFFDF5" stroke="#5C4A65" stroke-width="2.5"/><path d="M453 775L453 920" stroke="#DDCCD7" stroke-width="3"/><path d="M606 725L635 714L635 859L606 869" fill="#FFFDF9" stroke="#D9CCD7" stroke-width="1.5" stroke-dasharray="5 7"/></g>
<path id="paper-path" d="M114 858Q197 813 272 815T453 856Q532 840 609 794" fill="none" stroke="#F2C498" stroke-width="18"/>
</g>
<!-- One miniature room with a working table, shelving, book and lamp. -->
<g id="study-popup">
<path d="M107 766L107 554L237 522L237 734Z" fill="#D9CDEC" stroke="#5C4A65" stroke-width="2.5"/><path d="M119 581L224 555M119 647L224 621" stroke="#A18AB6" stroke-width="5"/>
<path d="M129 577L129 545L142 542L142 573M151 570L151 533L168 529L168 566M178 563L171 536L183 531L194 559" fill="#FFF6DF" stroke="#5C4A65" stroke-width="2.5"/>
<path d="M104 733L225 701L267 730L143 764Z" fill="#F0C296" stroke="#5C4A65" stroke-width="2.5"/><path d="M143 764L143 815M250 738L250 786M112 744L112 792" stroke="#5C4A65" stroke-width="5"/>
<path d="M141 731L174 723L193 731L219 721L238 732L195 746Z" fill="#FFFEF8" stroke="#5C4A65" stroke-width="2"/><path d="M193 731L195 746" stroke="#B6A2BB" stroke-width="2"/>
<path d="M122 726L132 677L156 663" fill="none" stroke="#087BC1" stroke-width="5"/><path d="M144 650Q170 643 171 673L145 680Z" fill="#087BC1" stroke="#4A414C" stroke-width="2"/><ellipse cx="133" cy="727" rx="15" ry="4" fill="#087BC1"/>
<path d="M149 678L133 716L195 706L167 673Z" fill="#FFE9A2" opacity=".45"/>
</g>
<!-- Peers interact over one drawing, rather than floating career symbols. -->
<g id="exchange-popup">
<path d="M293 752L293 596L427 637L427 793Z" fill="#F5C9AD" stroke="#674F5C" stroke-width="2.5"/><path d="M305 621L412 653M305 640L398 668" stroke="#E8A983" stroke-width="4"/>
<g id="peer-a"><path d="M306 731L313 682Q329 670 346 688L350 745Z" fill="#87BCA6" stroke="#4A414C" stroke-width="2.5"/><circle cx="329" cy="663" r="18" fill="#87BCA6" stroke="#4A414C" stroke-width="2.5"/><path d="M320 663L322 663M335 663L337 663M323 672Q329 677 336 672" fill="none" stroke="#4A414C" stroke-width="2.5" stroke-linecap="round"/></g>
<g id="peer-b"><path d="M376 752L378 710Q395 697 412 714L417 768Z" fill="#A990D5" stroke="#4A414C" stroke-width="2.5"/><circle cx="395" cy="690" r="18" fill="#A990D5" stroke="#4A414C" stroke-width="2.5"/><path d="M386 690L388 690M400 690L402 690M389 698Q395 703 401 698" fill="none" stroke="#4A414C" stroke-width="2.5" stroke-linecap="round"/></g>
<path d="M297 758Q355 724 428 773L431 790Q364 825 298 777Z" fill="#FFF4D9" stroke="#4A414C" stroke-width="2.5"/><path d="M316 784L313 826M410 799L414 843" stroke="#4A414C" stroke-width="5"/>
<path d="M338 758L374 755L397 775L360 780Z" fill="#FFFDF9" stroke="#A990D5" stroke-width="2"/>
<path id="peer-arm" d="M344 702Q354 735 368 763" fill="none" stroke="#4A414C" stroke-width="4" stroke-linecap="round"/><circle cx="368" cy="763" r="5" fill="#87BCA6"/><path d="M391 722L383 753" stroke="#4A414C" stroke-width="4" stroke-linecap="round"/>
</g>
<!-- Unfinished landscape: an opening, not a promised qualification or job. -->
<g id="horizon-popup">
<path d="M464 810L464 611Q518 533 578 580Q609 595 628 565L628 757Z" fill="#CFDECF" stroke="#6D8A7A" stroke-width="2.5"/><path d="M464 810L464 719Q505 663 550 707Q586 740 628 658L628 757Z" fill="#94BAA9" stroke="#6D8A7A" stroke-width="2"/>
<path d="M487 785Q519 731 541 737T605 677" fill="none" stroke="#FFF6E5" stroke-width="15"/><circle id="horizon-sun" cx="579" cy="538" r="35" fill="#FFC16A"/><path d="M522 527Q536 514 547 523M598 496Q614 483 627 492" fill="none" stroke="#A990D5" stroke-width="3" stroke-linecap="round"/>
<path d="M611 586L645 565L645 746L628 757" fill="#FFFDF9" stroke="#B9B5C7" stroke-width="2" stroke-dasharray="4 7"/>
</g>
<g id="left-hand"><path d="M39 1035Q53 969 86 877" stroke="#30313B" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M73 886Q67 866 78 858Q89 851 94 865L99 882Q108 858 116 864Q121 870 110 893Q94 910 81 899Z" fill="#FFAA28" stroke="#30313B" stroke-width="3"/></g>
<g id="right-hand"><path d="M679 1009Q662 932 638 843" stroke="#30313B" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M626 851Q613 831 622 825Q631 818 639 836L640 816Q643 803 652 813L657 838Q656 860 640 866Z" fill="#FFAA28" stroke="#30313B" stroke-width="3"/></g>
<g id="front-cover"><path d="M92 762L353 820L353 965L92 907Z" fill="#087BC1" stroke="#30313B" stroke-width="3"/><path d="M111 787L111 882" stroke="#68BBE0" stroke-width="3"/><path d="M135 773L165 780L165 824L150 812L135 817Z" fill="#FF8E38" stroke="#30313B" stroke-width="2"/></g>
</g></svg>'''
css = '''@font-face{font-family:Display;src:url(assets/segoe-ui-black.ttf);font-weight:900}@font-face{font-family:Body;src:url(assets/arial.ttf)}*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden}#ending{position:relative;width:100%;height:100%;overflow:hidden;background:#FDF1E6;color:#30313B;font-family:Body,sans-serif}.scene{position:absolute;inset:0}#scene17{opacity:0}.art{position:absolute;inset:0;width:720px;height:1280px}.title{position:absolute;z-index:5;font-family:Display;font-weight:900;background:#087BC1;color:#fff;padding:12px 21px;box-shadow:5px 6px 0 #30313b13;white-space:nowrap}.s16title{top:200px;left:190px;font-size:41px}.s17title{top:230px;left:93px;font-size:35px}.paper-bg{position:absolute;inset:0;background:#F5EDF7}.paper-bg:before{content:"";position:absolute;left:70px;top:350px;width:580px;height:580px;border-radius:50%;background:#FFF9F0}'''
js = '''const tl=gsap.timeline({paused:true});

tl.set('#student-walk-anchor',{x:255,y:590,scale:1.12},0);
tl.fromTo('#student-walk-anchor',{x:195,y:600},{x:255,y:590,duration:.95,ease:'power1.inOut'},0);
tl.to('#student-rig',{y:-4,duration:.22,repeat:3,yoyo:true,ease:'sine.inOut'},0);
tl.to('#leg-left',{attr:{d:'M48 120L60 165L80 168'},duration:.23,repeat:3,yoyo:true},0);
tl.to('#leg-right',{attr:{d:'M82 120L70 165L50 168'},duration:.23,repeat:3,yoyo:true},0);
tl.to('#student-head-feature',{x:4,duration:.3},1.05);
tl.fromTo('#title16',{opacity:0,y:12,rotation:-2},{opacity:1,y:0,duration:.35,ease:'power2.out'},1.15);
tl.to('#arm-left',{rotation:155,svgOrigin:'38 45',duration:.3,ease:'power2.out'},1.2);
tl.to('#arm-left',{rotation:140,duration:.16,repeat:3,yoyo:true},1.5);
tl.to('#arm-left',{rotation:0,duration:.3},2.16);
tl.to('#right-arm-path',{attr:{d:'M95 45Q117 52 111 65'},duration:.32},2.35);
tl.to('#right-hand-circle',{attr:{cx:111,cy:65},duration:.32},2.35);
tl.to('#carried-notebook',{x:98,y:62,rotation:-8,scale:1.3,duration:.4},2.35);
tl.to('#student-head-feature',{x:0,y:4,duration:.3},2.45);
tl.to('#title16',{opacity:0,duration:.2},2.75);
const cut=3.0825;
tl.set('#scene16',{opacity:0},cut);tl.set('#scene17',{opacity:1},cut);
tl.set('#folio-camera',{scale:1.35,x:-80,y:-185,svgOrigin:'360 800'},0);
tl.set('#fold-left',{scaleX:.06,svgOrigin:'272 780'},0);
tl.set('#fold-middle',{scaleX:.06,svgOrigin:'272 780'},0);
tl.set('#fold-right',{scaleX:.06,svgOrigin:'453 800'},0);
tl.set('#study-popup',{svgOrigin:'177 760',scaleY:.02,opacity:0},0);
tl.set('#exchange-popup',{svgOrigin:'362 790',scaleY:.02,opacity:0},0);
tl.set('#horizon-popup',{svgOrigin:'550 800',scaleY:.02,opacity:0},0);
tl.set('#paper-path',{opacity:0},0);
tl.set('#left-hand',{x:162},0);tl.set('#right-hand',{x:-198},0);
tl.to('#front-cover',{scaleX:-.96,svgOrigin:'353 850',duration:.65,ease:'power2.inOut'},cut+.08);
tl.to('#front-cover',{opacity:0,duration:.15},cut+.58);
tl.to('#folio-camera',{scale:1,x:0,y:0,duration:2.25,ease:'power2.inOut'},cut+.38);
tl.to('#fold-left',{scaleX:1,duration:.8,ease:'power2.inOut'},cut+.43);
tl.to('#left-hand',{x:0,duration:.8,ease:'power2.inOut'},cut+.43);
tl.to('#fold-middle',{scaleX:1,duration:.9,ease:'power2.inOut'},cut+.75);
tl.to('#fold-right',{scaleX:1,duration:1,ease:'power2.inOut'},cut+1.2);
tl.to('#right-hand',{x:0,duration:1.5,ease:'power2.inOut'},cut+.7);
tl.to('#paper-path',{opacity:1,duration:.4},cut+1.15);
tl.to('#study-popup',{scaleY:1,opacity:1,duration:.75,ease:'back.out(1.1)'},cut+.9);
tl.to('#exchange-popup',{scaleY:1,opacity:1,duration:.8,ease:'back.out(1.1)'},cut+1.65);
tl.to('#horizon-popup',{scaleY:1,opacity:1,duration:.9,ease:'power2.out'},cut+2.45);
tl.fromTo('#peer-arm',{rotation:-9,svgOrigin:'344 702'},{rotation:3,duration:.5,ease:'sine.inOut'},cut+2.45);
tl.fromTo('#horizon-sun',{y:16},{y:0,duration:.8,ease:'power2.out'},cut+2.7);
tl.fromTo('#title17',{opacity:0,y:15,rotation:-2},{opacity:1,y:0,duration:.4,ease:'power2.out'},cut+3.7);
window.__timelines=window.__timelines||{};window.__timelines['ending']=tl;'''
html = '<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Nhật · Ending v2</title><script src="assets/gsap.min.js"></script><style>'+css+'</style></head><body><div id="ending" data-composition-id="ending" data-width="720" data-height="1280" data-duration="7.866666666666666"><div class="scene" id="scene16">'+svg+'<div class="title s16title" id="title16">CHƯƠNG MỚI</div></div><div class="scene" id="scene17"><div class="paper-bg"></div>'+art+'<div class="title s17title" id="title17">HÀNH TRÌNH CÒN TIẾP</div></div></div><script>'+js+'</script></body></html>'
(P/'index.html').write_text(html, encoding='utf-8')
(P/'hyperframes.json').write_text(json.dumps({'paths':{'assets':'assets','blocks':'compositions','components':'compositions/components'},'media':{'autoProxy':False}}),encoding='utf-8')
(P/'DESIGN.md').write_text('''# Cụm16–17 · bản thử v2
16 giữ Hà Lan, kết mở sổ;17 cận sổ, bung trang gấp thành thế giới học tập/trao đổi/tương lai mở. Không lặp đi bộ.
Voice copy nguyên PCM sample1448462–1636800,24000Hz. Cut theo voice3.0825s;236pictureframes@30fps giữ đủ âm cuối.
Không sửa source/kịch bản cũ. Asset mới là vector giấy gấp và diorama. Catalogue paper-collage-reveal là scatter reveal, không phù hợp trang accordion nên dùng chuyển động riêng.
''',encoding='utf-8')
print(P)
