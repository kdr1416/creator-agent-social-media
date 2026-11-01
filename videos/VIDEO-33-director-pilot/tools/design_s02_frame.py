"""Static S02 design proposal; preserve assembly sources and original voice."""
from pathlib import Path
import shutil,json,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'revisions/S02-design-r1'
if OUT.exists():raise SystemExit('Review revision already exists')
OUT.mkdir();a=OUT/'assets';a.mkdir()
for src,dest in [(ROOT/'assets/fonts/segoe-ui-black.ttf','font.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js')]:shutil.copy2(src,a/dest)
INK='#30313B'
def coin(i,x,y,w=158,h=20):
 return f'''<g id="coin-{i}" stroke="{INK}" stroke-width="2.7"><path d="M{x-w/2} {y}v{h}a{w/2} 19 0 0 0 {w} 0v-{h}" fill="#F5B746"/><ellipse cx="{x}" cy="{y}" rx="{w/2}" ry="19" fill="#FFD47A"/><ellipse cx="{x}" cy="{y}" rx="{w/2-13}" ry="11" fill="none" stroke="#D69D39" stroke-width="2"/><path d="M{x-w/2+16} {y+12}v11M{x+w/2-16} {y+12}v11" stroke="#D99F39" stroke-width="2"/></g>'''
art=f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="1280" viewBox="0 0 720 1280" style="width:100%;height:100%"><rect width="720" height="1280" fill="#FFF0E5"/>
<text id="hero" x="360" y="214" text-anchor="middle" fill="#195D8C" font-family="Scene" font-weight="900" font-size="55">H&#192;NG T&#7926; &#272;&#7890;NG</text>
<ellipse cx="362" cy="1015" rx="292" ry="27" fill="#DFC8BA" opacity=".55"/>
<g id="open-ledger" stroke="{INK}" stroke-width="3" stroke-linejoin="round">
<path d="M72 795Q211 747 359 800Q503 748 650 789L652 988Q501 957 359 1015Q212 963 72 997Z" fill="#3B8EB8"/>
<path d="M83 766Q221 730 359 782Q503 729 638 765V967Q504 939 359 995Q221 945 83 975Z" fill="#EDDFCD"/>
<path d="M83 755Q220 721 359 771V982Q221 934 83 962Z" fill="#FFFCF1"/>
<path d="M359 771Q504 719 638 752V959Q505 929 359 982Z" fill="#FFF8E8"/>
<path d="M359 778V978" fill="none" stroke="#C6B9AB" stroke-width="3"/>
<path d="M105 941Q222 920 338 959M382 960Q501 919 617 939" fill="none" stroke="#D8CABA" stroke-width="2"/>
<g id="ledger-rules" fill="none" stroke="#C1D7DC" stroke-width="2.5"><path d="M112 852Q224 833 331 871M112 881Q224 861 331 900M112 910Q224 890 331 929M388 874Q504 844 610 862M388 905Q504 876 610 892"/></g>
<path d="M359 982L374 977V1026L362 1017L351 1027V980Z" fill="#B398D4" stroke-width="2"/>
</g>
<g id="graduation-cap" stroke="{INK}" stroke-width="3" stroke-linejoin="round"><ellipse cx="235" cy="812" rx="94" ry="16" fill="#C8BFB4" opacity=".35" stroke="none"/>
<path d="M168 746V785Q230 829 297 783V745Z" fill="#8C77BA"/><path d="M133 734L235 683L337 734L235 783Z" fill="#B59BD5"/><path d="M235 733L310 756V798" fill="none" stroke="#FFD47A" stroke-width="5"/><path d="M305 794L315 794L322 817H299Z" fill="#FFD47A" stroke-width="2.5"/>
</g>
<ellipse cx="491" cy="931" rx="94" ry="20" fill="#B9A78B" opacity=".28"/>
<g id="coin-stack">'''
for i in range(14):art+=coin(i,491,900-i*22)
art+='</g>'
art+=coin('loose-a',170,944,92,13)+coin('loose-b',249,959,86,13)
# A physical, unnumbered height gauge. No numeric scale or evidence claim.
art+=f'''<g id="measuring-rule" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"><path d="M609 551L641 551V925H609Z" fill="#E0D4F0"/><path d="M610 578H628M610 608H620M610 638H628M610 668H620M610 698H628M610 728H620M610 758H628M610 788H620M610 818H628M610 848H620M610 878H628" fill="none" stroke="#8F78AC"/></g>
</svg>'''
(OUT/'layered-art.svg').write_text(art,encoding='utf-8')
(OUT/'index.html').write_text('''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@font-face{font-family:Scene;src:url('assets/font.ttf');font-weight:900}html,body{width:100%;height:100%;margin:0;overflow:hidden}#root{width:100%;height:100%}</style><script src="assets/gsap.min.js"></script></head><body><div id="root" class="clip" data-composition-id="root" data-width="720" data-height="1280" data-fps="30" data-duration="1">'''+art+'''</div><script>window.__timelines=window.__timelines||{};window.__timelines.root=gsap.timeline({paused:true});</script></body></html>''',encoding='utf-8')
s=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'))['scenes'][1]
spec={k:s[k] for k in ['scene_id','raw_text','corrected_text','start_sample','end_sample','sample_frames','duration','audio_source','render_mode']}
spec.update({'phase':'static_frame_pending_user_review','takeaway':'Gia đình dành nguồn lực lớn cho du học.','opening':'Sổ chi phí mở, vài đồng xu trên trang; mũ tốt nghiệp có sẵn.','signature_motion_plan':'Xu bổ sung vào cùng chồng; thước đo trượt để nhấn quy mô ở cụm hàng tỷ đồng. Không biểu đồ tăng trưởng hoặc lợi nhuận.','final':'Chồng xu chiếm trọng tâm trên sổ; mũ tốt nghiệp bên trái và gauge nhỏ bên phải.','text_inventory':[{'text':'HÀNG TỶ ĐỒNG','font':'Segoe UI Black','size':55}],'text_override_reason':'Thay nhãn CHI PHÍ DU HỌC bằng cụm nhấn đúng voice, mũ tốt nghiệp giữ ngữ cảnh du học. Không thêm số cụ thể.','mascot_role':'Không dùng mascot; cận cảnh đồ vật và trọng lượng mang ý.','assets':'New layered SVG coin14+2, ledger pages, cap/tassel, gauge; existing local font/runtime.','containers':['Sổ chi phí vật lý, giữ quan hệ xu nằm trên trang; không khung thông tin.'],'accent_treatment':'none','mobile_legibility_plan':'Hero55px→27.5px at360x640; coin and cap silhouettes remain distinct. Footer1080–1280 clear.','dark_mass_strategy':'No large navy/charcoal fills; neutral thin outlines, purple cap and pale pages.','continuity':'S01 sách mở ra điểm tựa → S02 cận khoản đầu tư học tập → S03 kế hoạch nhiều năm. Không match-morph nhà/ledger.','preservation':'Frame proposal only. Does not replace S02 base selected in MASTER_APPROVED_ASSEMBLY_R1 until user approves motion/assembly update. Original voice and all approved pilots unchanged.'})
(OUT/'DIRECTION.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'DIRECTION.md').write_text('''# S02 — Khoản đầu tư cho du học / frame R1

Đề xuất frame kết của cảnh3.8555s. Không dựng motion ở vòng này. Chồng xu lớn đặt trực tiếp trên sổ chi phí mở; mũ tốt nghiệp ở trang trái để giữ ý “cho hành trình du học”. Thước không số bên phải là prop nhấn chiều cao, không phải đồ thị lợi nhuận hay bằng chứng định lượng. Chữ HÀNG TỶ ĐỒNG55px native Segoe UI Black. Không mascot ở cận đồ vật này. Xu không đại diện đúng một số tiền; không gán giá cho một trường/cá nhân.

Khi dựng motion: bắt đầu ít xu, thêm vào cùng chồng theo lời, gauge dịch ngắn để chỉ quy mô; không làm trang sổ lõm quá mức hay đồng xu bay xuyên vật thể. Bố cục cuối giữ y550–1030, footer1080–1280 sạch. Nét mảnh, nền đào/kem, vàng tiền tươi, mũ tím, bìa xanh. Toàn bộ SVG tách lớp editable. Không dùng asset generative hoặc ảnh bên ngoài.

Đây là đề xuất mới của S02, chưa được duyệt; manifest master đã bàn giao vẫn chọn bản S02 nền hiện có. Không tự thay nguồn assembly trước khi có quyết định mới. Raw transcript, voice và sample bounds giữ nguyên trong DIRECTION.json.
''',encoding='utf-8')
(OUT/'REVIEW.html').write_text('''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>S02 · Frame R1</title><style>body{margin:32px auto;max-width:1000px;padding:0 20px;background:#fff8e9;color:#30313b;font:17px system-ui}.row{display:flex;gap:36px;flex-wrap:wrap}img{width:360px;max-width:100%;height:auto}aside{max-width:450px}a{color:#195d8c}</style><h1>S02 · Khoản đầu tư cho du học</h1><p>Frame R1 để duyệt thiết kế; chưa dựng motion.</p><div class="row"><a href="frames/frame-00-at-0.5s.png"><img src="frames/frame-00-at-0.5s.png" alt="Frame S02: hàng tỷ đồng đầu tư cho du học"></a><aside><p>Ý chính: gia đình dành nguồn lực lớn cho hành trình học tập.</p><p>Chồng xu trên sổ chi phí; mũ tốt nghiệp giữ rõ ngữ cảnh du học. Không gán một mức học phí cụ thể.</p><p>Motion dự kiến: thêm xu vào cùng chồng, thước trượt ngắn để nhấn quy mô ở cụm “hàng tỷ đồng”.</p><p><a href="index.html">Source editable</a> · <a href="DIRECTION.md">Chỉ dẫn thiết kế</a></p><p>Đề xuất này chưa thay S02 trong master/manifest bàn giao.</p></aside></div></html>''',encoding='utf-8')
print('Created isolated S02 keyframe proposal')
