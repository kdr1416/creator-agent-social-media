"""Author the S05 restart storyboard; preserve source media and rejected revisions."""
import copy
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'handoff/S05_STORYBOARD_RESTART_R1'
if OUT.exists():
    raise SystemExit('Refusing to overwrite restart packet')
OUT.mkdir(parents=True)

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

board = read(ROOT / 'STORYBOARD.json')
old_scenes = copy.deepcopy(board['scenes'])
old = next(s for s in board['scenes'] if s['scene_id'] == 'S05')
save(OUT / 'history/S05_packet_before_restart.json', old)
shutil.copy2(ROOT / 'research/visual-approvals.json', OUT / 'history/visual-approvals-before.json')
shutil.copy2(ROOT / 'production_status.json', OUT / 'history/production-status-before.json')

# Source fields are copied, never retyped or normalized.
source_keys = ['scene_number', 'scene_id', 'start', 'end', 'start_sample', 'end_sample',
               'source_segments', 'raw_text', 'corrected_text', 'audio_source',
               'duration', 'sample_frames', 'raw_segments']
s = {k: copy.deepcopy(old[k]) for k in source_keys}
beats = [
    {'local_range': [0, .49], 'spoken_cue': 'khoảng đầu lát voice',
     'action': 'Bản đồ nam Sicily–Malta đã nằm trong khung. Mascot ở góc dưới trái, cầm một ghim, nhìn đúng điểm Malta; không chờ asset bay vào.'},
    {'local_range': [.49, 2.49], 'spoken_cue': 'Đó là lý do / ngày càng nhiều gia đình',
     'action': 'Mascot nghiêng người và đưa tay đang giữ ghim tới vị trí Malta. Bản đồ giữ nguyên; chỉ cơ thể, cánh tay và ghim chuyển động.'},
    {'local_range': [2.49, 3.55], 'spoken_cue': 'lựa chọn / đa dạng hóa / tài…',
     'action': 'Đầu ghim chạm điểm Malta rồi được đặt xuống. Bàn tay nhả sau tiếp xúc, thu về; nhãn MALTA hiện một lần. Không thêm cờ, tiền, đường bay hay địa điểm thứ hai.'},
    {'local_range': [3.55, 4.35], 'spoken_cue': '…sản bằng / chuẩn bị tới bất động sản',
     'action': 'Giữ kết quả định vị. Mascot nhìn ghim; tay đã rời ghim. Bản đồ không zoom xuyên vào công trình.'},
    {'local_range': [4.35, 5.706333333333333], 'spoken_cue': 'bất động sản tại Malta',
     'action': 'Cắt thẳng sang ảnh thật mặt tiền nhà ở Malta. Mặt tiền chiếm phần lớn vùng hình, thấy rõ cửa ra vào và ban công. Giữ nhãn MALTA cùng vị trí; ảnh đứng yên để nhận diện. Không có mascot chạm vào nhà trong ảnh.'},
]
assets = [
    {'layer': 'map-base', 'status': 'needs_sourcing_and_vector_styling', 'source': 'Dữ liệu địa lý có nguồn, thí dụ Natural Earth; kiểm coastline/đảo trước khi cách điệu.', 'required_separate_layer': True},
    {'layer': 'malta-anchor', 'status': 'needs_creation', 'source': 'Điểm neo theo bản đồ, không phải tâm màn hình; tách khỏi hình ghim.', 'required_separate_layer': True},
    {'layer': 'mascot-rig', 'status': 'existing_identity_new_pose_required', 'source': 'assets/approved-student-source.js: giữ nhận diện; tạo pose với vai/khuỷu/cổ tay đúng tầm.', 'required_separate_layer': True},
    {'layer': 'pin', 'status': 'needs_creation', 'source': 'Ghim đồ họa đơn giản, đầu ghim tách lớp, không phải tượng đài/nhà.', 'required_separate_layer': True},
    {'layer': 'residential-photo', 'status': 'existing_candidate_not_selected', 'source': 'assets/townhouse.jpg / Wikimedia Townhouse in Zejtun.jpg; kiểm crop và provenance trước khi chọn. Có thể thay bằng ảnh nhà ở Malta có giấy phép phù hợp.', 'required_separate_layer': True},
    {'layer': 'MALTA-label', 'status': 'existing_font_new_text_layer', 'source': 'assets/fonts/segoe-ui-black.ttf, text native; không bake trong ảnh.', 'required_separate_layer': True},
    {'layer': 'warm-ground-and-footer', 'status': 'needs_creation', 'source': 'Nền kem, biển xanh rất nhạt, đất đào nhạt; ảnh không tràn footer.', 'required_separate_layer': True},
]
s.update({
    'design_revision': 'S05_STORYBOARD_RESTART_R1',
    'status': 'storyboard_proposal_pending_user_approval',
    'title': 'Chọn địa điểm, thấy tài sản thật',
    'takeaway': 'Malta được đưa vào cân nhắc như một địa điểm cho tài sản bất động sản; cảnh làm rõ địa điểm và loại tài sản, không chứng minh xu hướng ngày càng nhiều gia đình.',
    'semantic_type': 'location-to-concrete-property',
    'visual_family': 'map-location editorial cut to real residential exterior',
    'visual_center': 'Ghim Malta, rồi mặt tiền nhà thật',
    'visual_verb': 'định vị / cắt sang đối tượng cụ thể',
    'preferred_mode': 'HF_ONLY', 'render_mode': 'HF_ONLY',
    'routing_confidence': 'high',
    'routing_reason': 'Hành động chính là mascot vector đặt ghim và chuyển cảnh biên tập sang ảnh tĩnh thật; không cần diễn viên hay video sinh. Giữ engine đã khóa, thay toàn bộ ý tưởng hình.',
    'routing_override': None, 'flow_contribution': 'none',
    'hf_contribution': 'Rig tiếp xúc ghim, bản đồ nhiều lớp, text native và cắt ảnh; không dùng morph công trình.',
    'organic_motion_need': 'Cử động tay/người vector có tiếp xúc rõ; không cần Flow.',
    'exact_graphics_need': 'Vị trí ghim có nguồn; ảnh nhà không méo; nhãn native.',
    'character': 'yes', 'pilot': True,
    'style_id': 'hf_existing:warm-doodle-mixed-media',
    'style_reference': 'inputs/reference/DIRECTOR_BRIEF.md; S01 original and S09 motion r1 are approved motion references.',
    'style_candidates': ['warm-doodle mixed media: selected', 'all-vector architectural street: discarded; lacks real-asset specificity'],
    'style_reason': 'Mascot và bản đồ thân thiện dẫn tới ảnh thật có lý do nội dung; nền sáng và chữ ngắn giữ ngữ pháp đã duyệt.',
    'composition': '720×1280. Nhãn y=160–235. Shot A: bản đồ lớn không viền x=40–680,y=300–1030, Malta ở vùng giữa thấp bên phải để tay chạm được; mascot x≈70–270,y≈690–1040. Crop bản đồ theo Malta và nam Sicily, không vẽ lại vị trí địa lý để vừa tay. Shot B: ảnh x=0–720,y=290–1080, crop thấy trọn cửa và ban công; bầu nền kem phía trên nối nhãn. Footer y=1080–1280 luôn sạch.',
    'composition_reason': 'Điểm ghim là tâm hành động của shot A; mặt tiền thật là hình chủ đạo shot B. Hai shot dùng cùng vùng nội dung lớn, không phải ảnh nhỏ trong khung hay bảng thông tin.',
    'opening_state': beats[0]['action'],
    'transformation': 'Tay đưa ghim → chạm → nhả → nhìn kết quả; tại từ bất, cắt dựng sang kiến trúc nhà ở thật. Không có quan hệ biến hình giữa bản đồ và nhà.',
    'final_state': 'Mặt tiền nhà ở Malta đứng yên trong vùng hình lớn, nhãn MALTA duy nhất, không mascot/ghim/đạo cụ chồng lên ảnh.',
    'protagonist_action': 'Cầm và đặt ghim bằng một tay, thân nghiêng nhẹ để đạt tầm, mắt nhìn đúng điểm tiếp xúc, thu tay sau khi nhả.',
    'mascot_role': 'Dẫn người xem tới địa điểm qua hành động định vị; rời hình tại hard cut để ảnh nhà được đọc theo tỷ lệ thật.',
    'timed_beats': beats,
    'cue_accuracy': 'Các mốc nội cảnh là đề xuất từ word timing ASR có sẵn, chưa xác minh độc lập từng âm. Đối chiếu voice khi dựng, đặc biệt mốc bất ≈4.349s; không thay audio/sample bounds.',
    'motion_emphasis_sequence': ['chuẩn bị định vị', 'đặt ghim và nhả', 'giữ điểm lựa chọn', 'cắt sang mặt tiền nhà thật'],
    'hf_signature_motion': 'Tiếp xúc–nhả ghim đọc rõ, sau đó editorial cut đúng từ bất động sản; nhà không chịu bất cứ biến dạng/hiệu ứng nở nào.',
    'flow_action': None, 'flow_camera': None,
    'overlay_zone': 'MALTA ở y=160–235; không đặt chữ lên cửa/ban công; footer y=1080–1280 sạch.',
    'asset_contract': assets,
    'container_required': False, 'container_inventory': [], 'container_semantics': [],
    'visible_text_budget': {'max_simultaneous_words': 1, 'max_levels': 1, 'paragraphs': 0},
    'visible_text_inventory': [{'text': 'MALTA', 'size_px': 56, 'role': 'location anchor', 'appears_after': 'pin contact', 'held_across_cut': True}],
    'text_treatment': 'Segoe UI Black local; một nhãn xanh tím đậm trên nền kem, không hộp, không lặp nhãn trong bản đồ.',
    'accent_reason': 'none', 'accent_treatment': 'none',
    'mobile_legibility_plan': '360×640: MALTA tương đương 28px; ghim và tay phải phân biệt được, không phụ thuộc chữ địa danh nhỏ. Cửa và ban công chiếm ít nhất nửa bề rộng ảnh. Không thêm micro-label.',
    'dark_mass_strategy': 'Bản đồ tint sáng, mascot cam và túi xanh; ảnh ưu tiên đá sáng, tránh crop nhiều bóng tối. Chữ/nét là khối tối nhỏ.',
    'handoff': 'S04 → S05: cắt từ câu hỏi tập trung sang bản đồ, không chuyển xu hay mang khay qua. S05 → S06: cắt từ mặt tiền sang bàn gia đình; kết nối bằng ý tài sản → nền tảng gia đình, không cố nối cửa nhà với bàn.',
    'continuity_risk': 'S09 đã kể phân bổ tài sản bằng cơ cấu ba phần; S05 không chia đồng xu/ba ngôi nhà/ba thị trường. S13 nếu có địa cầu kể quyền di chuyển, không lặp ghim và ảnh nhà.',
    'must_keep': ['Voice gốc và toàn bộ sample bounds', 'Hai shot: định vị rồi nhà thật; cắt dựng rõ', 'Nhận diện mascot, tầm tay tự nhiên, tiếp xúc rồi nhả ghim', 'Ảnh đúng nhà ở Malta có nguồn; không dựng nhà trên ảnh skyline', 'Một nhãn MALTA; footer 200px', 'Không dùng lại album, trang giấy lật, nhà giấy, nhà biến hình hay bảng phân bổ'],
    'flexible': ['Crop bản đồ/ảnh, pose, nét và sắc độ trong brief', 'Thời lượng reach/contact/hold sau khi đối chiếu voice', 'Nguồn ảnh nhà ở phù hợp hơn nếu kiểm được giấy phép; không giữ ảnh v5 chỉ vì có sẵn'],
    'reference_alignment': {k: {'assessment': 'proposal_not_rendered', 'candidate_evidence': v} for k, v in {
        'colour_relationships': 'kem/đào/xanh nhạt và cam–tím–xanh mascot',
        'typography_treatment': 'Segoe UI Black, duy nhất MALTA',
        'asset_mix': 'vector địa lý/mascot và ảnh nhà thật trong hai shot rõ ràng',
        'composition': 'hình chủ đạo lớn, footer sạch, không card',
        'mascot_language': 'mascot gọn, đặt ghim có tiếp xúc',
        'motion_rhythm': 'reach/contact/release, hold rồi hard cut theo ý thoại'}.items()},
    'research': [{'claim': 'Malta nằm ở Địa Trung Hải, phía nam Sicily; kiểm bản đồ dựa trên dữ liệu địa lý.', 'url': 'https://govcms.gov.mt/en/About%20Malta/Pages/The%20Maltese%20Islands.aspx'}],
    'unresolved': ['Chưa duyệt ý tưởng mới.', 'Chưa chọn crop/ảnh nhà cuối cùng và chưa làm bản đồ.', 'Không có frame hay pilot mới; chưa có kiểm chứng thị giác hoặc playback cho phương án này.'],
})

md = '''# S05 — storyboard viết lại từ đầu / R1

**Trạng thái: đề xuất chờ duyệt kịch bản. Không có frame hay pilot mới.**

Album S05 v5 không được duyệt theo yêu cầu mới nhất. Toàn bộ cơ chế album, giấy lật, nhà giấy và nhà biến hình đã bị loại khỏi hướng hiện tại. Các bản cũ chỉ còn là lịch sử.

## Ý tưởng: Chọn địa điểm, thấy tài sản thật

Mascot đặt một ghim lên Malta trên bản đồ. Khi voice tới “bất động sản”, cắt thẳng sang ảnh lớn mặt tiền một căn nhà thật ở Malta. Đây là hai shot được nối bằng dựng phim: người xem đi từ địa điểm tới loại tài sản cụ thể. Không có công trình mọc lên từ bản đồ và không có cảnh nhân vật tương tác với vật thể bên trong ảnh.

Lời thoại nói về đa dạng hóa; cảnh này làm rõ một địa điểm và một loại tài sản đang được cân nhắc. Không dùng nhiều gia đình hay biểu đồ tăng để biến lời “ngày càng nhiều” thành bằng chứng thống kê. S09 đã kể cơ chế phân bổ nên S05 không lặp lại.

## Voice giữ nguyên

Global **18.151208333–23.857541667s**, **[435629, 572581)** tại 24kHz; **136952 samples / 5.706333333s**. Nguồn `inputs/audio/seg_05.wav`.

Raw transcript: “Đó là lý do ngày càng nhiều gia đình lựa chọn đa dạng hóa tài sản bằng bất đồng sản tại Manta.”

Corrected text, chỉ để đọc hiểu: “Đó là lý do ngày càng nhiều gia đình lựa chọn đa dạng hóa tài sản bằng bất động sản tại Malta.” Không thu lại, thay chữ trong voice, kéo giãn hoặc cắt mất khoảng nghỉ.

## Kịch bản theo nhịp

| Thời gian nội cảnh | Nhịp lời | Hình ảnh / hành động |
|---|---|---|
| 0–0.49s | Đầu lát voice | Bản đồ nam Sicily–Malta đã trong khung; mascot cầm ghim ở dưới trái, nhìn điểm định vị. |
| 0.49–2.49s | “Đó là lý do… ngày càng nhiều gia đình” | Mascot nghiêng người, đưa ghim tới Malta. Map đứng yên, tay đi một quãng ngắn tự nhiên. |
| 2.49–3.55s | “lựa chọn… đa dạng hóa tài…” | Ghim chạm đúng điểm rồi tay nhả, thu về. Nhãn **MALTA** hiện một lần sau tiếp xúc. |
| 3.55–4.35s | “…sản bằng…” | Giữ kết quả: ghim đứng yên, mascot nhìn điểm chọn. Không thêm icon hay nhãn. |
| 4.35–5.706s | “bất động sản tại Malta” | Cắt thẳng sang ảnh thật mặt tiền nhà ở. Thấy rõ cửa và ban công; nhãn MALTA giữ nguyên vị trí. Giữ hình đến hết voice. |

Mốc nội cảnh dựa trên word timing ASR, là cue đề xuất chưa xác minh độc lập từng âm. Khi dựng, đối chiếu WAV để hard cut trúng từ “bất”; không đổi ranh giới sample. Shot ảnh chỉ khoảng 1.36s nên đứng yên, không thêm chuỗi hiệu ứng.

## Bố cục và hình cuối

Canvas 720×1280. Nền kem, mặt đất trên bản đồ đào nhạt, biển xanh rất nhạt. Mascot cam bo góc, mũ tím, ba lô xanh; nét mảnh trung tính. Nhãn MALTA ở y=160–235, Segoe UI Black 56px.

Shot bản đồ: vùng hình x≈40–680, y≈300–1030. Crop bản đồ để Malta nằm gần tầm tay, không dịch đảo khỏi vị trí thật. Mascot ở dưới trái; cánh tay không kéo dài, không cắm ghim xuyên người. Không dùng bản đồ làm card có viền.

Shot nhà: ảnh trải hết bề rộng x=0–720, y=290–1080. Khung lấy một mặt tiền nhà ở, ưu tiên đá sáng, cửa và ban công rõ ở kích thước điện thoại. Không viền, băng dính, album, khung ảnh hoặc mô hình kiến trúc. Không có mascot trong shot ảnh. Hình cuối chỉ còn mặt tiền nhà và nhãn MALTA phía trên. Footer y=1080–1280 sạch.

## Asset và tách lớp

- Bản đồ: cần lấy dữ liệu địa lý có nguồn rồi cách điệu, không tự phác đảo theo trí nhớ. Tách biển, đất, điểm neo Malta.
- Mascot: giữ nhận diện nguồn đã có; cần pose mới với thân, tay xa, tay gần, bàn tay cầm/nhả và mắt tách lớp. Không bê pose album v5.
- Ghim: một ghim đồ họa tách lớp, neo theo bản đồ; chuyển quyền giữ từ tay sang map tại tiếp xúc.
- Ảnh nhà ở: chưa chọn cuối cùng. `assets/townhouse.jpg` là ứng viên có sẵn, không bắt buộc dùng. Có thể tìm ảnh khác hợp crop hơn, có nguồn và giấy phép. Không dùng skyline nhà thờ làm bất động sản đang bán, không dựng giao dịch/sở hữu hay gán giá cho ảnh.
- Chữ MALTA: text native, font Segoe UI Black đã có. Không tạo chữ bằng AI.

Engine giữ **HF_ONLY**: rig vector + map + ảnh tĩnh thật + editorial cut. Không cần Flow. Asset mới chưa được tạo.

## Nối cảnh và kiểm tra logic

S04 đặt câu hỏi tập trung tài sản; cắt sang một địa điểm được cân nhắc ở S05, không để tiền tự bay khỏi Việt Nam. S06 tiếp tục ý gia đình bằng bàn chung; cắt theo ý, không kéo cửa nhà thành mặt bàn. S09 giữ riêng cơ chế phân bổ ba phần.

Trước khi render phải nhìn rõ chuỗi cầm → chạm → nhả. Ghim không nhảy trước bàn tay. Ảnh nhà không morph, skew, nở hoặc dính vào map. Không thể hiện chìa khóa trao tay, hợp đồng, lợi nhuận hay quyền cư trú tự phát sinh.

Kiểm sau khi được duyệt: opening, tiếp xúc ghim, trước/sau cut và final; bản 360×640, thumbnail, grayscale; playback với voice gốc. Hiện chưa thực hiện các kiểm này vì chưa sản xuất hình/motion.

## Phần giữ / phần linh hoạt

Giữ: ý định vị → nhà ở thật; hai shot tách rõ; voice/sample gốc; nhận diện mascot; một nhãn MALTA; footer; hành động tay hợp lý. Không kế thừa album hoặc cơ chế nhà giấy.

Linh hoạt: crop, pose, vị trí trong safe area, sắc độ, easing và mốc động tác nhỏ sau khi đối chiếu voice. Đổi ý tưởng trung tâm cần cập nhật storyboard, không thay bằng một cơ chế mới lúc thi công.

Nguồn kiểm địa lý: [Government of Malta — The Maltese Islands](https://govcms.gov.mt/en/About%20Malta/Pages/The%20Maltese%20Islands.aspx). Ảnh có sẵn là ứng viên: [Townhouse in Zejtun — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Townhouse_in_Zejtun.jpg); cần giữ attribution/giấy phép nếu sử dụng.
'''
save(OUT / 'S05_STORYBOARD.json', s)
(OUT / 'S05_STORYBOARD.md').write_text(md, encoding='utf-8')
save(OUT / 'ASSET_PLAN.json', {'scene_id': 'S05', 'revision': s['design_revision'], 'assets': assets, 'production_started': False})
(OUT / 'ANTIGRAVITY_PROMPT_DRAFT.md').write_text('''# Bản nháp bàn giao — chưa cho phép thi công phương án mới

Đọc S05_STORYBOARD.md và .json trong folder này. Đây là storyboard S05 viết lại từ đầu, đang chờ chủ dự án duyệt. Chưa tạo frame hoặc pilot theo bản này.

Sau khi chủ dự án duyệt: sản xuất asset đúng contract, dựng hai shot bản đồ đặt ghim → cắt sang ảnh nhà ở thật, giữ voice seg_05.wav và sample bounds. Không lấy album v5, nhà giấy hoặc bất cứ S05 MP4 lịch sử nào làm mẫu hình hiện hành. S01 bản đầu và S09 motion r1 là hai pilot đã được duyệt, xem APPROVED_PILOTS.json để xác định đúng file/hash.

Khi triển khai, giữ local font, editable source, asset nhiều lớp và attribution. Kiểm tiếp xúc tay/ghim, cut theo voice, opening/mid/final, 360×640, thumbnail, grayscale và playback. Bàn giao riêng pilot S05 cho người dùng duyệt. Chưa dựng full phim.
''', encoding='utf-8')

approved = []
for sid, version, rel in [('S01', 'original_pilot', 'pilots/S01/renders/pilot.mp4'), ('S09', 'motion-r1', 'revisions/pilots-approved-frames-r1/S09/renders/pilot.mp4')]:
    file = ROOT / rel
    approved.append({'scene_id': sid, 'version': version, 'approval_status': 'approved', 'approval_scope': 'pilot motion with original voice', 'video_path': rel, 'absolute_path': str(file), 'video_sha256': sha(file), 'user_message_verbatim': 'S01 bản đầu + S09 motion r1', 'full_film_production_authorized': False})
save(OUT / 'APPROVED_PILOTS.json', approved)
save(OUT / 'production_status.json', {'phase': 'storyboard_proposal', 'S05': 'pending_storyboard_approval', 'S05_album_v5': 'rejected_by_latest_user_instruction', 'new_frames_created': False, 'new_pilots_rendered': False, 'approved_pilots': approved, 'full_film_authorized': False})
(OUT / 'README.md').write_text('# S05 — hướng mới R1\n\nĐọc S05_STORYBOARD.md để duyệt kịch bản. Chưa có frame hay pilot mới. Album v5 không được duyệt. Hai pilot đã duyệt: S01 bản đầu và S09 motion r1; xem manifest đúng phiên bản. ANTIGRAVITY_PROMPT_DRAFT.md là hướng dẫn dự thảo sau khi kịch bản mới được duyệt.\n', encoding='utf-8')

# Replace the active S05 packet from scratch; other scene objects stay identical.
board['scenes'] = [s if x['scene_id'] == 'S05' else x for x in board['scenes']]
save(ROOT / 'STORYBOARD.json', board)
save(ROOT / 'scenes/S05/packet.json', s)
(ROOT / 'scenes/S05/PACKET.md').write_text(md, encoding='utf-8')

approvals = read(ROOT / 'research/visual-approvals.json')
for a in approvals.get('approved', []):
    if a['scene_id'] == 'S05':
        a.update(current_selection=False, approval_status='superseded_not_current', historical_note='S05 design restarted; latest user explicitly rejects album v5.')
        if a.get('version') == 'final-frame-v5':
            a.update(approval_status='rejected_by_latest_user_instruction', pilot_render_authorized=False, latest_user_message_verbatim='frame abum s05 v5 toio khong duyệt. yêu cầu viết lại kịch bản storyboard của s05 từ đầu luôn.')
approvals['approved'] = [a for a in approvals['approved'] if not (a['scene_id'] in ['S01', 'S09'] and a.get('approval_scope') == 'pilot motion with original voice')] + approved
approvals['pending'] = [{'scene_id': 'S05', 'version': s['design_revision'], 'scope': 'new storyboard only; no frame or motion approved'}]
save(ROOT / 'research/visual-approvals.json', approvals)
status = read(ROOT / 'production_status.json')
status.update(phase='S05_storyboard_restart_pending_approval', approval_scope='Approved pilots: S01 original + S09 motion r1. S05 album v5 rejected; new S05 storyboard R1 pending. No full-film authorization.', next_action='User reviews handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md before any new frame or S05 pilot production.', visual_approvals=approvals, approved_pilots=approved, active_S05_storyboard='handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.json', active_S05_frame=None, storyboard_visual_sheet='STORYBOARD.html: S05 historical pictures superseded; use linked restart script; no new frame.')
for r in status.get('revised_pilot_renders', []):
    if r.get('scene_id') == 'S05':
        r['approval'] = 'historical_rejected_direction_do_not_use_as_current'
save(ROOT / 'production_status.json', status)
(ROOT / 'APPROVED_VERSIONS.md').write_text('# Phiên bản đang được duyệt\n\n- **S01 bản đầu**: `pilots/S01/renders/pilot.mp4` — pilot đã duyệt.\n- **S09 motion r1**: `revisions/pilots-approved-frames-r1/S09/renders/pilot.mp4` — pilot đã duyệt.\n- **S05**: album v5 không được duyệt; các S05 cũ chỉ là lịch sử. Hiện chỉ có storyboard mới R1, chờ duyệt; chưa có frame/pilot được duyệt cho hướng mới.\n\nKịch bản hiện hành: `handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md`. File/hash hai pilot: `handoff/S05_STORYBOARD_RESTART_R1/APPROVED_PILOTS.json`. Chưa cho phép dựng full phim.\n', encoding='utf-8')

notice = '> **Cập nhật S05:** Album v5 không được duyệt. Mọi mô tả/hình S05 bên dưới là lịch sử và được thay bằng [storyboard viết lại R1](handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md), đang chờ duyệt. Hai pilot đã duyệt là S01 bản đầu + S09 motion r1. Chưa dựng frame/pilot mới hoặc full phim.\n\n'
for name in ['STORYBOARD.md', 'DIRECTOR_BRIEF.md', 'ASSET_PLAN.md', 'CONTINUITY.md', 'TECHNICAL_HANDOFF.md', 'REVIEW_GUIDE.md', 'ANTIGRAVITY_PROMPT.md']:
    path = ROOT / name
    path.write_text(notice + path.read_text(encoding='utf-8-sig'), encoding='utf-8')
asset_plan = read(ROOT / 'ASSET_PLAN.json')
asset_plan['active_S05_override'] = {'revision': s['design_revision'], 'status': 'proposal_not_produced', 'assets': assets, 'supersedes': 'all previous S05 album/house assets as active direction'}
save(ROOT / 'ASSET_PLAN.json', asset_plan)
html = ROOT / 'STORYBOARD.html'
body = html.read_text(encoding='utf-8-sig')
banner = '<aside style="background:#fff1cf;color:#292633;padding:22px;font:700 18px Segoe UI,sans-serif;border-bottom:3px solid #8054ca">S05: album v5 KHÔNG được duyệt. Hình S05 cũ bên dưới đã hết hiệu lực. <a href="handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md">Đọc storyboard mới R1 (chờ duyệt)</a>. Chưa có frame/pilot mới. Pilot đã duyệt: S01 bản đầu + S09 motion r1.</aside>'
import re
body, count = re.subn(r'(<body\b[^>]*>)', lambda m: m[0] + banner, body, count=1, flags=re.I)
if count == 0:  # Existing storyboard is an HTML fragment without a body tag.
    body = banner + body
html.write_text(body, encoding='utf-8')

assert all(a == b for a, b in zip(old_scenes, board['scenes']) if a['scene_id'] != 'S05')
assert all(old[k] == s[k] for k in source_keys)
voice = ROOT / 'inputs/audio/seg_05.wav'
assert sha(voice) == old['raw_segments'][0]['sha256']
save(OUT / 'verification.json', {'other_13_scene_objects_unchanged': True, 'S05_source_fields_unchanged': True, 'voice_sha256': sha(voice), 'new_frames_or_renders': False, 'approved_pilots_file_hashes_verified': True})
print(str(OUT))
