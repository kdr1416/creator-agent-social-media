"""Build static, editable S05 poses from the approved restart storyboard only."""
from pathlib import Path
import ast, json, shutil, re, hashlib
from PIL import Image
from build_pilots import mascot

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'revisions/S05-design-restart-r2'
INK='#30313B'
kit={'mascot':mascot,'re':re,'INK':INK}
tree=ast.parse((ROOT/'tools/design_s07_s08_frames.py').read_text(encoding='utf-8'))
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'rig','exec'),kit)
arm=kit['arm_rig']
board=ROOT/'handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.json'
shutil.copy2(board,OUT/'STORYBOARD_SOURCE.json')
photo=ROOT/'revisions/S05-final-frame-v5/assets/townhouse.jpg'
shutil.copy2(photo,OUT/'assets/townhouse-original.jpg')
Image.open(photo).crop((340,95,1020,841)).resize((720,790),Image.Resampling.LANCZOS).save(OUT/'assets/townhouse-crop.jpg',quality=97)
geo=json.loads((OUT/'assets/ne_10m_admin_0_countries.geojson').read_text(encoding='utf-8'))
def project(lon,lat): return 340+(lon-14.37)*1250,800-(lat-35.92)*1543.2
paths=[]
for f in geo['features']:
    if f['properties'].get('ADM0_A3') not in ['MLT']: continue
    geom=f['geometry'];polys=geom['coordinates'] if geom['type']=='MultiPolygon' else [geom['coordinates']]
    for poly in polys:
        ring=poly[0]
        if not any(11.7<x<16.1 and 35.3<y<38.2 for x,y,*_ in ring):continue
        d='M'+'L'.join(f'{project(x,y)[0]:.2f},{project(x,y)[1]:.2f}' for x,y,*_ in ring)+'Z'
        paths.append(f'<path d="{d}"/>')
mapart=''.join(paths)
mx,my=project(14.37,35.92)
def pin(x,y):
    return f'<g id="location-pin" transform="translate({x:.3f} {y:.3f})" stroke="{INK}" stroke-width="2.8" stroke-linejoin="round"><path d="M0 0C-8-13-23-25-23-42A23 23 0 1 1 23-42C23-25 8-13 0 0Z" fill="#E96964"/><circle cx="0" cy="-42" r="8" fill="#FFF8E9"/></g>'
def label():return '<text id="malta-label" x="360" y="218" text-anchor="middle" font-family="Scene" font-size="56" font-weight="900" fill="#195D8C">MALTA</text>'
def frame(phase):
    body='<rect width="720" height="1280" fill="#FFF8E9"/>'
    if phase=='house':
        body+=label()+'<image id="real-house" href="assets/townhouse-crop.jpg" x="0" y="290" width="720" height="790"/>'
    else:
        body+=label()
        body+='<defs><clipPath id="map-window"><rect x="36" y="300" width="648" height="740" rx="0"/></clipPath></defs>'
        body+='<g id="geography" clip-path="url(#map-window)"><rect x="36" y="300" width="648" height="740" fill="#E4F1F0"/>'
        body+=f'<g id="land" fill="#F6D5B9" stroke="#9D8D87" stroke-width="2" stroke-linejoin="round">{mapart}</g></g>'
        # Map is a physical selection surface. No invented islands or geo displacement.
        px,py=(mx+9,my+42) if phase=='hold' else (mx,my)
        hand=(px-17,py-40)
        if phase=='release': hand=(308,832)
        nx=(hand[0]-150)/1.1-109;ny=(hand[1]-720)/1.1-83
        body+=arm('selector',150,720,1.1,(-27,22),(nx,ny))
        body+=pin(px,py)
        if phase!='release':
            body+=f'<circle id="gripping-fingers" cx="{hand[0]:.3f}" cy="{hand[1]:.3f}" r="8" fill="#FFAC3C" stroke="{INK}" stroke-width="2.7"/>'
    return '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280" style="width:100%;height:100%">'+body+'</svg>'
items=[('01-hold','Cầm ghim — trước khi chọn', 'hold'),('02-contact','Ghim chạm Malta — tay còn giữ','contact'),('03-release','Đã nhả ghim — một nhãn MALTA','release'),('04-house','Sau hard cut — mặt tiền nhà thật','house')]
for folder,title,phase in items:
    p=OUT/folder;p.mkdir(exist_ok=True);a=p/'assets';a.mkdir(exist_ok=True)
    shutil.copy2(OUT/'assets/townhouse-crop.jpg',a/'townhouse-crop.jpg') if phase=='house' else None
    shutil.copy2(ROOT/'assets/fonts/segoe-ui-black.ttf',a/'font.ttf');shutil.copy2(ROOT/'assets/runtime/gsap.min.js',a/'gsap.min.js')
    art=frame(phase);(p/'layered-art.svg').write_text(art,encoding='utf-8')
    (p/'index.html').write_text('''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{font-family:Scene;src:url('assets/font.ttf');font-weight:900}html,body{margin:0;width:100%;height:100%;overflow:hidden}#root{width:100%;height:100%}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-duration="1" data-fps="30">'''+art+'''</div><script>window.__timelines=window.__timelines||{};window.__timelines.root=gsap.timeline({paused:true});</script></body></html>''',encoding='utf-8')
ledger={'photo':{'source':'https://commons.wikimedia.org/wiki/File:Townhouse_in_Zejtun.jpg','author':'Marika Caruana','license':'CC BY-SA 4.0','license_url':'https://creativecommons.org/licenses/by-sa/4.0/','modifications':'Crop (340,95,1020,841), resize720x790. No AI edits.','purpose':'Architectural context, not an available listing or ownership evidence.','original_sha256':hashlib.sha256(photo.read_bytes()).hexdigest()},'map':{'source':'https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_10m_admin_0_countries.geojson','license':'public domain','projection':'x=340+(longitude-14.37)*1250; y=800-(latitude-35.92)*1543.2, north up. Local equirectangular ratio accounts for cos36deg.','pin_lon_lat':[14.37,35.92]},'mascot':'Existing approved compact orange rig; new reach/contact/release poses.','font':'Local Segoe UI Black'}
(OUT/'CREDITS.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'production_status.json').write_text(json.dumps({'phase':'static_frames_pending_user_review','scene':'S05','version':'design-restart-r2','frame_approved':False,'motion_produced':False,'master_modified':False,'source_storyboard':str(board.relative_to(ROOT)),'frames':[{'folder':f,'title':t} for f,t,_ in items]},ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'DIRECTION.md').write_text('''# S05 — frame mới theo storyboard restart R1

Hai shot giữ nguyên ý đã duyệt: chọn địa điểm bằng ghim trên bản đồ → hard cut sang ảnh nhà thật ở Malta. Bốn pose là minh chứng staging, chưa phải motion. Giữ sample [435629,572581), voice 5.706333333s nguyên bản. Bản đồ Natural Earth 10m, phía bắc ở trên; phóng gần toàn bộ quần đảo Malta và loại Sicily khỏi khung theo phản hồi người dùng. Giữ vị trí tương đối Gozo–Comino–Malta từ dữ liệu gốc. Ghim lớn là marker đồ họa, không phải kích thước hòn đảo. Mascot nhận diện cũ, pose tay mới. Near shoulder world (269.9,811.3); grip contact (323,760); không kéo dài cánh tay khi làm motion. Ghim từ tay chuyển sang map sau tiếp xúc.

Frame 01: đang cầm ghim; 02: tiếp xúc; 03: tay thu về; nhãn MALTA có từ frame đầu để xác định địa điểm; 04: ảnh nhà cắt thẳng ở cue “bất động sản”. Nhãn native text Segoe UI Black 56px cùng vị trí x360,y218. Ảnh full width y290–1080, footer sạch. Không morph ảnh, không nhà giấy, không album, không trao chìa khóa, không suy diễn căn nhà đang bán. Shot ảnh giữ khoảng1.36s. Không sửa voice để khớp pose.

Style alignment: palette kem/đào/xanh biển nhạt + ghim coral; mascot compact và font giữ mốc đã duyệt; mixed media chuyển từ vector sang ảnh có nguồn. Bản đồ mới thay album bị loại. Chỉ đánh giá pose/bố cục tĩnh ở vòng này, chưa xác nhận chất lượng motion. Các scene/master và toàn bộ phiên bản cũ giữ nguyên.
''',encoding='utf-8')
cards=''.join(f'<section><h2>{i+1:02d} · {t}</h2><a href="{f}/frames/frame-00-at-0.5s.png"><img src="{f}/frames/frame-00-at-0.5s.png" alt="{t}"></a><p><a href="{f}/index.html">Source editable</a></p></section>' for i,(f,t,_) in enumerate(items))
(OUT/'REVIEW.html').write_text('''<!doctype html><html lang="vi"><meta charset="utf-8"><title>S05 — frame zoom Malta R2</title><style>body{background:#fff8e9;color:#30313b;font:17px system-ui;margin:32px}h1{font-size:30px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:24px}section img{width:100%;max-width:360px;display:block}h2{font-size:18px}a{color:#195d8c}</style><h1>S05 · Frame mới / zoom Malta R2</h1><p>Bộ frame tĩnh để duyệt thiết kế. Chưa dựng motion, chưa thay master.</p><div class="grid">'''+cards+'''</div><p>Ảnh: Marika Caruana — <a href="https://commons.wikimedia.org/wiki/File:Townhouse_in_Zejtun.jpg">Townhouse in Zejtun</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>; đã crop. Bản đồ: Natural Earth, public domain. Ảnh kiến trúc tham chiếu, không phải tin rao bán.</p><p><a href="DIRECTION.md">Chỉ dẫn cảnh</a> · <a href="CREDITS.json">Nguồn asset</a></p></html>''',encoding='utf-8')
print('Built four static editable poses')
