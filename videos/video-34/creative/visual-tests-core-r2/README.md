# VIDEO-34 — Core Styles Visual Tests R2

**AWAITING VISUAL STYLE REVIEW** · 01/11/2026 · Static art/pose/type-layout proofs, chưa animate.

[Xem bốn frame cạnh nhau](index.html) · [PNG comparison](comparison.png).

| Frame | PNG 1080×1920 | Mobile 360×640 | Source render / vector |
|---|---|---|---|
| S03-A · Coastal lifestyle | [PNG](S03-A.png) | [Mobile](S03-A-mobile.png) | [HTML](S03-A.html) · [SVG](S03-A.svg) |
| S03-B · Café + type | [PNG](S03-B.png) | [Mobile](S03-B-mobile.png) | [HTML](S03-B.html) · [SVG](S03-B.svg) |
| S08-A · Workspace | [PNG](S08-A.png) | [Mobile](S08-A-mobile.png) | [HTML](S08-A.html) · [SVG](S08-A.svg) |
| S08-B · Family connection | [PNG](S08-B.png) | [Mobile](S08-B-mobile.png) | [HTML](S08-B.html) · [SVG](S08-B.svg) |

Source chính là [build_frames.py](build_frames.py), có hai hàm construction `coast(state)` và `home(state)`, cùng asset primitives cho window/balcony, plants, walker, seated café figures, parent, child và laptop. Đây là artwork SVG nguyên gốc viết riêng cho test; không recolor SVG pilot cũ, không dùng screenshot/reference image thay output. HTML embed đúng SVG để glyphs/render/pivots có thể tiếp tục dùng cho animation. Mỗi file là một static pose state; registered GSAP timeline paused và chưa có animation sequence. Không được gọi đây là pilot đã animate.

## Typography V2: cái gì được giữ, cái gì được thay

Đã đọc `components/type-design.py`, `type-motion.js`, current style-bible và `build/type-pilot-delivery.json`. V2 đổi R1 Arial/top navy wash/repeated underline sang Bahnschrift + Constantia Italic, type gắn vào awning/world, phrase handoff sang terrace và không phủ wash. **Những cải tiến này được giữ trong revision mới:** font pair local giống V2; “cà phê / NGOÀI TRỜI” nằm trên vật liệu mái hiên; “gia đình” nằm trong khoảng trời; không top navy wash, không subtitle/footer/underline mặc định.

Không ghi đè `components/type-design.py`, `type-motion.js`, source/render/ledger/status production. Tạo geometry, characters và composition riêng. Mái hiên mới có sắc đỏ san hô sâu hơn để đạt contrast với chữ trắng. Type hierarchy và vị trí chỉ là đề xuất visual test, không sửa timing V2 hoặc thay quyết định đã phê duyệt trong production.

## Palette và typography

| Vai trò | Màu dùng |
|---|---|
| Ink / dark support | `#103A55`, `#16394B` |
| Sky / field | `#80D9F0` → `#F0FDFA` |
| Sea | `#169CC5` → `#06BCCC` → `#047B9D` |
| Limestone | `#FFF1D2` → `#EDD19E`; mặt khuất `#D0B583` → `#BFA077` |
| Human accent | Coral `#FF8B67` → `#E94E47`; blue shirt `#239EC0` → `#07657E` |
| Café fabric | `#CD5445` → `#B6443B` |
| Sunlight / highlight | `#FFD06A`, near-white `#FFF9EE` |

Đây là **creative palette thử nghiệm**, không official Esora brand colors. Logo Esora không được dùng trong bốn test này và file gốc không thay đổi. Fonts là các file Display/Bahnschrift và Editorial/Constantia Italic đã có trong project Typography V2, copy nguyên byte để capture local. Không cài font, không khẳng định quyền tái phân phối. Generator giữ @font-face và source text tiếng Việt editable.

## Ba playbook được áp dụng cụ thể

- **Kurzgesagt-inspired illustration:** palette theo material/light/role, foreground/background value separation, balcony/window thickness và localized detail, character silhouettes có hoạt động khác nhau. Hero ở S03 lớn hơn người nền; seated figures có chair/table support. S08 parent và child dùng construction/proportions riêng; child có mặt tròn hơn, mắt/mũi/cheeks khác adult.
- **Selective isometric/spatial design:** mặt bàn/laptop dùng các hướng mặt phẳng nhất quán; base/lid là nhóm riêng, cùng hinge endpoints. Balcony có top/side/support faces, props được đặt lên bề mặt. Coastline dùng illustrated oblique space, không ép cả không gian vào diagram 30°. Đây không phải claim toàn frame là mathematical isometric camera.
- **Bauhaus-inspired graphics:** contrast scale giữa main phrase và secondary sans, alignment theo mái hiên, graphic disc/counterform nhỏ kết nối giữa scenes, negative space giữ type và faces/hands độc lập. Chưa có kinetic movement; mask/handoff sẽ chỉ làm sau Gate 1.

## Voice-to-visual mapping

Timestamps dưới đây đọc từ `inputs/word-timestamps.json`, word numbers **1-based**. Scene Manifest cung cấp bounds/corrected_text; không giả manifest chứa word timestamps. Raw ASR “Giá đình” được display thành corrected “gia đình” mà không sửa raw/timing. JSON bằng chứng: [voice-cues.json](voice-cues.json).

| Voice Timestamp global | Spoken phrase | Visual action / state | Text highlight | Planned animation/effect — chưa implemented |
|---|---|---|---|---|
| S03 10.50–10.82s | đi bộ, words 46–47 | Một walker lớn ở foreground; café/runner là ngữ cảnh | Không chữ ở test A | Grounded gait + camera attention theo promenade, cần foot-contact solve |
| S03 13.68–14.52s | cà phê ngoài trời, words 60–63 | Café figure nâng cup; cùng environment và material | “cà phê / NGOÀI TRỜI” ở test B | Material-edge mask rồi giữ chữ; hand/cup contact cần kiểm theo toàn phase |
| S08 42.14–42.48s | cân bằng, words 174–175 | Parent còn ngồi tại workspace, con đã có mặt | Không chữ ở test A | Dừng thao tác, chuyển gaze/attention; không icon cân |
| S08 42.68–42.98s | công việc, words 177–178 | Lid/base riêng; open và closed pose assets đã có | Không thêm phrase trong bốn test | Rigid lid quanh hinge, hand clears screen; chuyển động chưa dựng |
| S08 43.30–43.68s | thời gian, words 180–181 | Attention chuyển khỏi desk | Không thêm text state thứ năm | Typography handoff theo V2 có thể tiếp tục; chờ visual decision |
| S08 45.00–45.38s | raw “Giá đình”, words 186–187 | Parent và child chạm tay, hướng mặt về nhau | “gia đình” ở test B | Phrase reveal có hold, gaze/hand response; không dùng glow che anatomy |

Frame sample anchors: S03-A global frame 315/local frame 10; S03-B 411/106; S08-A 1265/57; S08-B 1350/142, zero-based ở 30 FPS. Root picture durations 268/30 và 168/30s theo cumulative frame bounds cũ. Các file `*-B` hiện chữ ở **settled_layout_test** để duyệt bố cục, không giả entrance đã hoàn tất ngay tại onset. Bốn file không dùng để kiểm AV sync.

## Những asset mới

- Coastal world: illustrated facade, balcony/shutters/glass reflections, balcony garden, relief/cast shadows, promenade/sea wall, sea/town layers, café roof/posts/table/vase/cup, planters.
- S03 figures: walker có bag và outfit riêng, two seated café figures với cup pose khác nhau, runner nhỏ ở đường xa.
- Home world: arch/wall thickness, terrace/rail, niche ceramics, wall shelf, projected desk, separate lid/base laptop, bentwood chair, floor/light/shadow geometry.
- S08 figures: parent rig/pose groups cho open-work và contact; child body/face riêng và hai near-arm poses; chung character language với S03.
- Bốn SVG/HTML, voice-cue/frame metadata, comparison page/PNG và mobile proofs. Provenance/hashes trong [asset-ledger.json](asset-ledger.json).

## Khác biệt với pilot cũ và giới hạn còn lại

Composition và geometry được viết mới: S03 không dùng bản cũ có nhiều dáng người gần giống nhau; số activity cần đọc cùng lúc giảm, focal walker lớn hơn, café có vật liệu và contact prop. S08 thay figure construction, seated support, chi tiết child face, reachable arm chain, home architecture và desk/laptop geometry. Font/environment-bound typography của V2 được giữ, không quay lại overlay R1.

Đã xem PNG đầy đủ và mobile thực tế. Figure separation, type/face/hand clearance và sự thống nhất palette được kiểm bằng hình, không suy từ thành công render. Tuy nhiên đây vẫn là **stylized vector acting**; mức richness/character appeal cần bạn đánh giá. Một số form còn giản lược có chủ đích, không claim đã đạt tương đương studio tham khảo. S03 café actors vẫn nhỏ hơn hero để tạo depth; nếu bạn muốn café là focal ở cue đó, vòng sau cần reframe. S08 cần thêm gaze poses/expressions trong chuyển động; cùng một smile tĩnh chưa chứng minh emotional acting. Hinge, gait, hand hold trong toàn phase, timing/read time, chuyển cảnh và AV sync **chưa kiểm**.

Tooling: existing HyperFrames 0.8.170/GSAP/Puppeteer/Chrome. Usage command trả `unknown: usage_request_failed`; không suy ra quota. Không upgrade hoặc thêm dependencies. PNG chụp trực tiếp từ HTML/SVG bằng existing Puppeteer/isolated Chrome. HyperFrames `check` chạy trên bản sao entries trong `qa/check-entries/`, giữ asset paths local; không render video. Các warning về painted artwork bleed và rotated text bounding boxes được báo riêng, không coi automated pass là human approval. Kết quả cuối trong [qa/verification.json](qa/verification.json), browser checks và bốn HyperFrames JSON.

## Review gate và cách tiếp tục

Review record của revision này là [review-state.json](review-state.json), status pending; production approval vẫn pending. Cần người dùng đánh giá màu, character design, composition/depth và typography qua ID S03-A/B, S08-A/B. Nếu chưa đạt, chỉ sửa visual tests trước. Khi được duyệt hướng visual, mới đề xuất/triển khai animation S03/S08 trong bước được ủy quyền sau; không tự render pilot MP4 hoặc sản xuất 15 cảnh còn lại.
