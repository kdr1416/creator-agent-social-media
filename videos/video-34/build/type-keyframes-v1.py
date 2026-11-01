"""Static typography studies only. Never modifies production sources or MP4s."""
from pathlib import Path
import re,json,shutil,hashlib
P=Path(__file__).resolve().parents[1];O=P/'creative/typography-keyframes-v1';O.mkdir(exist_ok=True)
(O/'fonts').mkdir(exist_ok=True)
for src,dst in [('bahnschrift.ttf','display.ttf'),('constani.ttf','editorial-italic.ttf')]:shutil.copy2(Path('C:/Windows/Fonts')/src,O/'fonts'/dst)
N='#092e4d';W='#fffdf6'
def t(x,y,size,text,fill=N,family='Display',extra=''):
 return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" {extra}>{text}</text>'
studies=[
 ('S03-01','S03',1.2,'Đi bộ — chữ đặt trên mặt lối dạo, tiếp nối hướng bước chân',
 t(85,1040,66,'đi',N,'Editorial')+t(82,1205,158,'BỘ',N,extra='font-weight="750" letter-spacing="-6"')),
 ('S03-02','S03',4.2,'Cà phê ngoài trời — chữ nghiêng gắn vào mái hiên café',
 t(103,560,82,'cà phê',W,'Editorial','transform="rotate(-16 103 560)"')+t(172,662,28,'NGOÀI TRỜI',N,extra='letter-spacing="3"')),
 ('S03-03','S03',8.1,'Gia đình — chuyển sang nét chữ mềm, cạnh nhóm nhân vật',
 t(50,650,106,'gia',N,'Editorial')+t(64,760,119,'đình',N,'Editorial')),
 ('S08-01','S08',2.5,'Công việc — chữ theo mảng tường phía bàn làm việc',
 t(57,292,83,'CÔNG',N,extra='font-variation-settings="\'wght\' 730, \'wdth\' 80" letter-spacing="-3"')+t(58,390,91,'VIỆC',N,extra='font-variation-settings="\'wght\' 730, \'wdth\' 80" letter-spacing="-3"')),
 ('S08-02','S08',3.65,'Thời gian — trọng tâm chữ chuyển sang không gian ngoài trời',
 t(405,415,72,'thời',N,'Editorial')+t(400,516,101,'GIAN',N,extra='font-variation-settings="\'wght\' 720, \'wdth\' 80" letter-spacing="-4"')),
 ('S08-03','S08',5.3,'Gia đình — chữ kết ở vùng biển, để trống gương mặt và bàn tay',
 t(420,480,27,'THỜI GIAN',N,extra='letter-spacing="3"')+t(408,586,101,'gia',N,'Editorial')+t(410,700,110,'đình',N,'Editorial')),
]
motion=(P/'components/pilot-motion.js').read_text(encoding='utf-8')
manifest=[]
for id,sid,at,label,typeart in studies:
 src=(P/f'scenes/{sid}/index.html').read_text(encoding='utf-8');svg=re.search(r'<svg\b[\s\S]*?</svg>',src).group()
 # Remove the wall picture in this proposed S08 composition only, giving type a real wall surface.
 cleanup="""document.querySelectorAll('svg > path').forEach(e=>{const d=e.getAttribute('d');if(d.startsWith('M46 306')||d.startsWith('M58 318')||d.startsWith('M58 491'))e.remove();});document.querySelectorAll('svg > ellipse').forEach(e=>{if(e.getAttribute('cx')==='190'&&e.getAttribute('cy')==='365')e.remove();});""" if sid=='S08' else ''
 if id=='S03-02':
  cleanup="document.querySelectorAll('#world path').forEach(e=>{if(e.getAttribute('d')==='M34 574L282 503 337 602 35 690Z'||e.getAttribute('fill')==='#ff7053')e.setAttribute('fill','#ff6b4f');});"
 css="""@font-face{font-family:Display;src:url('fonts/display.ttf')}@font-face{font-family:Editorial;src:url('fonts/editorial-italic.ttf')}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#e8f6fd}.frame{position:relative;width:100%;height:100%}.frame>svg{position:absolute;inset:0;width:100%;height:100%;display:block}.type text[font-family=Display]{font-weight:750;font-variation-settings:'wght' 750,'wdth' 85}.type text{font-kerning:normal;text-rendering:geometricPrecision}.type{pointer-events:none}"""
 html=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{id} · Typography keyframe</title><link rel="icon" href="data:,"><style>{css}</style><script src="../../assets/vendor/gsap.min.js"></script></head><body><div class="frame">{svg}<svg class="type" viewBox="0 0 720 1280" aria-label="Proposed typography">{typeart}</svg></div><script>{motion}\nconst tl=createPilotTimeline('{sid}');tl.seek({at});{cleanup}window.keyframeReady=true;</script></body></html>'''
 (O/f'{id}.html').write_text(html,encoding='utf-8')
 manifest.append({'id':id,'scene':sid,'local_time':at,'label':label,'status':'STATIC STUDY — NOT IMPLEMENTED IN PILOT','html':id+'.html','png':id+'.png'})
before={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for base in ['scenes','inputs'] for f in (P/base).rglob('*') if f.is_file() and '.hyperframes' not in f.parts}
(O/'protected-before.json').write_text(json.dumps(before,indent=2),encoding='utf-8')
(O/'studies.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
css="""*{box-sizing:border-box}body{margin:0;background:#edf3f7;color:#102f4b;font-family:system-ui,sans-serif}main{max-width:1250px;margin:auto;padding:32px}h1{font-size:30px;font-weight:500}p{max-width:900px;color:#486174}.row{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}figure{margin:0;min-width:0}img{display:block;width:100%}figcaption{font-size:13px;line-height:1.5;padding:10px 0 18px}.sub{font-size:12px;color:#62788b;letter-spacing:.12em;text-transform:uppercase}@media(max-width:700px){main{padding:18px}.row{grid-template-columns:1fr}figure{max-width:420px;margin:auto}}"""
body='<main><div class="sub">VIDEO-34 · Typography study 01 · Static design only</div><h1>Chữ tham gia vào bố cục.</h1><p>Bahnschrift đậm cho hành động / Constantia Italic cho nhịp café và gia đình. Không phủ navy, không underline lặp lại. Các khung này đề xuất bố cục và trạng thái chữ; chưa dựng animation, chưa sửa pilot.</p>'
for sid in ['S03','S08']:
 body+=f'<section id="{sid}"><h2>{sid}</h2><div class="row">'
 for x in manifest:
  if x['scene']==sid:body+=f'<figure><a href="{x["html"]}"><img src="{x["png"]}" alt="{x["label"]}"></a><figcaption><b>{x["id"]}</b> · {x["local_time"]:.2f}s local<br>{x["label"]}</figcaption></figure>'
 body+='</div></section>'
body+='<p>S08: đề xuất bỏ bức tranh trên mảng tường dùng cho chữ. Font được lấy từ Windows hiện có và kiểm tra đủ glyph tiếng Việt; chỉ dùng trong study local. Các vị trí/phong cách này đang chờ phản hồi, chưa phải approval hay pilot mới.</p></main>'
(O/'index.html').write_text(f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VIDEO-34 · Typography studies</title><style>{css}</style><link rel="icon" href="data:,"></head><body>{body}</body></html>',encoding='utf-8')
print('Six static typography studies authored; pilot sources and outputs untouched')
