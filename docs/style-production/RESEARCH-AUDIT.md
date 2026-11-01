# Verified research & integration audit

Nhãn bằng chứng được định nghĩa trong [README](README.md). Các nhận định thẩm mỹ trong tài liệu là [A], không phải tuyên bố chính thức của các studio/phong trào. Ngày kiểm tra 01/11/2026.

## 1. Inventory upstream thực tế

[U] Nguồn là [animasyon-stil-katalogu](https://github.com/yasinozmeen/animasyon-stil-katalogu), branch `main`, tree/commit được API trả về `09e451d8b64ec85c1ec035fd39e00725c1ed5593`. Inventory recursive nguyên gốc ở [upstream-tree.json](evidence/upstream-tree.json). Bản local `references/animasyon-stil-katalogu/` không hiện diện lúc kiểm tra; không dùng đường dẫn trong báo cáo cũ làm bằng chứng nó vẫn tồn tại.

| Hạng mục | Thực tế đã xác minh |
|---|---|
| Root | `.gitignore`, `README.md`, `BRIEF.md`, `birlestir.sh`, `render_ornek.mjs`; thư mục `katalog/`, `stiller/` |
| Catalog | 20 thư mục style trong `stiller/`; README có bảng vai trò và liên kết source/video; `katalog/katalog.mp4`, `katalog/son.mp4` |
| Ba style được chọn | Mỗi thư mục có `anim.html`, MP4 cùng slug, `onizleme.gif`, `render.mjs`, `build.sh`, `sfx.json`, `synth.py`, hai file font `.woff2` |
| Source code | Canvas 2D HTML/JS; `window.draw({t})` trả JPEG base64, `window.ready` chờ fonts/assets. Không phải GSAP hoặc HyperFrames template |
| Prompts | `BRIEF.md` là brief chung có thật; chưa thấy thư viện prompt sản xuất chuyên sâu riêng cho mỗi style trong tree |
| Technical guide | README mô tả render; `render_ornek.mjs` và build scripts có mã thực thi. Không thấy hệ hướng dẫn rig/acting/visual QA chuyên sâu cho ba style trong tree |
| Reference images | `onizleme.gif` là preview animation. Có fonts/media; không thấy bộ moodboard ảnh độc lập hay thư viện nhân vật/layered SVG trong ba thư mục đã kiểm tra |
| Video examples | Có 20 MP4 style trong tree; chỉ tải và phân tích ba clip được chọn. Không tuyên bố xem 17 clip còn lại hay toàn bộ catalog |
| License | Tree recursive không có file LICENSE/COPYING/OFL riêng. README nêu Google Fonts/OFL, nhưng tuyên bố này không cấp phép toàn repo hay tự chứng minh quyền của từng binary font |

Quyền sử dụng: repo public không tự cấp quyền sao chép/phân phối. Lần này giữ source và MP4 tải về trong research cache, không dùng làm production asset, không port nguyên mã, không đưa font upstream vào project. Cần xác minh điều khoản cụ thể trước tái phân phối. Học quan hệ màu/hình/chuyển động rồi dựng artwork mới; không tái tạo mascot, logo, layout hay chuỗi animation nhận diện. Fonts Latin/Latin-ext trong demo không chứng minh đủ Vietnamese subset; U+1EA0–U+1EF1 có thể nằm ngoài các range khai báo của demo.

## 2. Nguồn đọc được và cách suy luận

| Nguồn | Điều kiểm chứng; giới hạn |
|---|---|
| [README pinned](https://github.com/yasinozmeen/animasyon-stil-katalogu/blob/09e451d8b64ec85c1ec035fd39e00725c1ed5593/README.md) | Catalog, mô tả sản xuất và dependencies do tác giả công bố; không phải thước đo chất lượng độc lập |
| [BRIEF pinned](https://github.com/yasinozmeen/animasyon-stil-katalogu/blob/09e451d8b64ec85c1ec035fd39e00725c1ed5593/BRIEF.md) | Showcase ngắn, tiêu chí một focus/chuyển cảnh, lưu ý figure/font và contract draw(t). Những luật máy Mac/công cụ của brief không được nhập thành luật Flow Kit |
| [Kurzgesagt source](https://github.com/yasinozmeen/animasyon-stil-katalogu/blob/09e451d8b64ec85c1ec035fd39e00725c1ed5593/stiller/kurzgesagt/anim.html) | Functions/assets/timing được mô tả bên dưới; demo của tác giả repo, không phải source studio Kurzgesagt |
| [Isometric source](https://github.com/yasinozmeen/animasyon-stil-katalogu/blob/09e451d8b64ec85c1ec035fd39e00725c1ed5593/stiller/izometrik/anim.html) | Projection, face primitives, room assembly và camera parameters |
| [Bauhaus source](https://github.com/yasinozmeen/animasyon-stil-katalogu/blob/09e451d8b64ec85c1ec035fd39e00725c1ed5593/stiller/bauhaus/anim.html) | Grid, masked text, geometric actions, wipe, timer, grain |
| [Renderer pinned](https://github.com/yasinozmeen/animasyon-stil-katalogu/blob/09e451d8b64ec85c1ec035fd39e00725c1ed5593/render_ornek.mjs) | Global Playwright require, macOS headless-shell lookup, URL pathname assumption, mặc định 66s, workers=4; không chạy nguyên script trên Windows |
| [Kurzgesagt — Who we are](https://kurzgesagt.org/who-we-are) | Studio tự mô tả mục tiêu khoa học dễ tiếp cận, hấp dẫn thị giác. Không công bố recipe màu/rig trong trang này; các recipe ở đây là phân tích bổ sung |
| [MoMA — Bauhaus graphic design](https://www.moma.org/explore/inside_out/2009/11/06/bauhaus-the-graphic-design-department-goes-back-to-school/) và [Letterform Archive — original Universal lettering](https://exhibitions.letterformarchive.org/bauhaus/artworks/original-lettering-for-universal-type) | Bối cảnh typography và nguyên mẫu thiết kế. Bauhaus không đồng nghĩa một font thương mại hoặc một preset motion lịch sử; playbook là diễn giải motion hiện đại |
| [GSAP Timeline docs](https://gsap.com/docs/v3/GSAP/Timeline/) | Cách tổ chức tween bằng timeline, labels và time/seek. Recipe phải đối chiếu bản runtime đang dùng |

## 3. Reverse engineering ba demo

[U] `kurzgesagt/anim.html` dùng palette vai trò, seed RNG cho stars, cached glows/atmosphere/molecule sprites, clipping và shading trong `drawPlanet`, `shadeCircle`, `drawBubble`. Hai trạng thái space/air có cầu nối zoom; `popText` tạo nhịp word-level; grid phân tử có chuyển động từ hàm thời gian. **Không có human walk rig hoặc diễn xuất cha mẹ/con được chứng minh ở demo này.** Không suy từ chất lượng hành tinh sang khả năng anatomy.

[U] `izometrik/anim.html` có projection `P`, `box`, `cyl`, `sphere`, `cone`, affine `onFace`, shadow và `drop`; `room` dựng đồ nội thất. `frame(t)` tính camera/scale lại từ `t`, sắp các tile theo depth key rồi vẽ labels sau world. Đây là giá trị tái học quan trọng: toàn bộ mặt dùng cùng phép chiếu, detail gắn trên mặt, không phải từng hình thoi xoay rời rạc. Recipe ở playbook mở rộng thành construction system riêng cho Flow Kit, không sao chép căn phòng gốc.

[U] `bauhaus/anim.html` kết hợp grid 12 cột, type Archivo, `maskedLetters`, hình tròn lăn theo baseline, square/triangle quay tại pivot, circle wipe chuyển sang clock, outro columns. Source dùng ease exponential cho chuyển đồ họa, overshoot nhẹ cho một action, cached grain. Về thẩm mỹ đây là diễn giải Swiss/Bauhaus pha trộn do chính comment source nêu; không lấy làm định nghĩa duy nhất của Bauhaus.

[O] Đã trích contact sheet 1 frame/giây cho cả ba clip: [Kurzgesagt](evidence/upstream-kurzgesagt-contact.png), [Isometric](evidence/upstream-izometrik-contact.png), [Bauhaus](evidence/upstream-bauhaus-contact.png). Đọc từ trái sang phải, hàng trên 0–4s, hàng dưới 5–9s. FFprobe đo cả ba: H.264, 1280×720, 30/1 FPS, 285 video frames, 9.500s, có AAC. Canvas source là 1920×1080; không ghi nhầm đó là resolution MP4. Frame chuỗi cho thấy cấu trúc chuyển trạng thái, chưa đủ chứng minh độ mượt ở mọi frame. Không re-render source upstream, không xem/nghe playback liên tục trong lượt này.

[A] Điều đáng học là phân cấp kích thước/value, cấu trúc hình có shading, hình học nhất quán và biến đổi có nguyên nhân. Không nhập xi nền kem/grain, sao vũ trụ, 12 cột hay palette đỏ-vàng-xanh vào mọi video. Repo là một tập demo ngắn, chưa phải phương pháp production cho phim narration 93s.

## 4. Audit tích hợp Flow Kit

[L] Graph đã được dùng: `list_projects`, `index_status`, search generator symbols và `check_index_coverage`. Index generation `2026-11-01T06:40:03Z`, fast mode; setup metadata changed; root AGENTS excluded; docs excluded subtree; VIDEO-34 paths not tracked; catalog missing. Vì vậy kết luận bên dưới dựa trên đọc source/file trực tiếp, không xem graph sạch là bằng chứng đầy đủ. Không reindex toàn repo chỉ cho nhiệm vụ tài liệu.

| File/nhóm | Bằng chứng hiện tại | Thiếu hụt và hệ quả [A] |
|---|---|---|
| `references/ANIMATION-STYLES.md` | Không có tại thời điểm bắt đầu. Bản backup cũ ở `scratch/flowkit-v2-phase-ab-backup-20261101/references/` có mô tả vai trò/IDs/engine routing | Broken discovery path; báo cáo đã tích hợp không đảm bảo file vẫn hiện diện. Catalog mới trong lượt này khôi phục đường đọc, không khẳng định ai đã xóa bản cũ |
| Catalog backup | Ưu tiên du học, so ứng viên từng scene, có footer cố định/những hạn chế type từ thời trước | Không phù hợp quyết định ba Core Styles dùng rộng và text highlights. Không khôi phục nguyên luật cũ |
| `AGENTS.md`, `setup.py` | Root sinh từ `_CRITICAL_RULES`, `_PIPELINE_OVERVIEW`, `_ENGINE_ROUTING`, `_CREATIVE_CONTRACTS`, `_agents_md_body`; link catalog hiện có | Root hợp lý ở mức routing; không nên nhét anatomy/palette recipe vào đây. Root và generator được giữ nguyên |
| `skills/fk-edu-motion-explainer.md` và bốn sidecars | Hướng dẫn chọn palette, meaningful transformation, kiểm glyph/mobile, human gate | Có quality intent nhưng chưa chỉ cách dựng value map, projection, contact rig, hierarchy handoff hoặc kiểm từng lỗi |
| `skills/voice-to-scene-design/SKILL.md` | Có meaning → visual proposition → staging → continuity; tự ghi chưa film-validated | Là cầu nối ý nghĩa tốt, cần playbook để biến thành hình cụ thể; không cần agent mới |
| Warm-doodle skill | Một creative option riêng | Không phải baseline cho 3 core; giữ nguyên, không xóa hoặc đổi tên |
| HyperFrames core/CLI/animation | DOM timing, paused timeline, runtime registration, lint/check/snapshot; rules/adapters | Giải quyết tính renderable/seekable; không tự thiết kế silhouette, màu hay staging. Không quy lỗi taste cho engine |
| Remotion motion director | Props/components, premium/brand/format/review principles | Ngắn và thiên portfolio; thiếu recipe figure/iso/type; dùng có điều kiện với cùng art direction, không gán style riêng |
| Các báo cáo `docs/EXTERNAL_REPOSITORIES_EVALUATION.md`, architecture/readiness, `FLOW_KIT_V2_PHASE_AB_IMPLEMENTATION.md` | Tập trung khả năng công cụ, tối giản dependencies, migration và preservation | Chứng minh ý định tích hợp và kỹ thuật, không chứng minh output đẹp. Báo cáo cũ có đường dẫn reference đã mất |

## 5. VIDEO-34: phân biệt baseline, R1 và static studies

**Cập nhật khi kiểm tra cuối:** workspace đã đổi đồng thời sang `Typography V2` trong lúc nghiên cứu. Status vẫn pending. File `build/type-pilot-delivery.json` ghi nguồn `type-design.py + type-motion.js`, MP4 delivery suffix `-typography-v2`; style-bible mới ghi người dùng đã yêu cầu triển khai từ typography studies. Đây là metadata do luồng làm việc khác ghi, không phải approval do nghiên cứu này xác nhận. Không rollback hoặc coi những thay đổi đó là lỗi của lượt này. Các đoạn R1 bên dưới mô tả **snapshot đã quan sát trước V2**, không mô tả source cuối cùng.

[O] Đã trích lại hai frame V2: [S03 3.8s](evidence/latest-v2-S03-3.8.png), [S08 4.9s](evidence/latest-v2-S08-4.9.png). Chúng cho thấy type trên canopy, bỏ top navy wash; S08 dùng family phrase italic trong khoảng biển và type phụ. Như vậy V2 đã giải quyết một phần vấn đề chữ tách khỏi environment. Ở frame 4.9s chữ đang vào, không được kết luận chữ thiếu contrast ở trạng thái đã settle. Chất lượng gait/hinge/hold vẫn chưa được xem playback trong nghiên cứu này. Không khuyến nghị làm lại phần V2 đã tốt chỉ vì báo cáo R1 cũ. Keyframe redesign nên tập trung phần illustration/anatomy/spatial hierarchy chưa được chứng minh, đồng thời giữ những quyết định typography thật sự được người dùng xác nhận khi tiếp tục.

[L] Đã đọc manifest, scene-manifest, status, storyboard, style-bible, style-tokens, R1 notes, working config, `components/build_pilot_art.py`, `revise_pilot_r1.py`, `pilot-motion.js`, highlights và source S03/S08. Master 2,232,960 samples/24kHz = 93.04s; 17 intervals. Approval pending; prior feedback NOT APPROVED. Không sửa trạng thái để biểu thị đã chấp thuận.

[O] File `build/pilot-evidence/S03-encoded-3.80.png` và `S08-encoded-2.60.png` được xem nhưng còn là artwork muted cũ; chúng không phản ánh source R1 lúc đọc. Đã trích MP4 tại lúc đó vào [observed R1 S03 3.8s](evidence/observed-r1-S03-3.8.png) và [observed R1 S08 4.9s](evidence/observed-r1-S08-4.9.png). Hai MP4 sau đó bị thay thế đồng thời; không thu được media hash đúng thời điểm trích R1, nên không tuyên bố association bất biến giữa các PNG này và một hash MP4. Các hash media trong verification là bản V2 ở lần kiểm cuối. Bài học: evidence phải gắn hash/revision ngay khi capture, tên thư mục QA không đủ.

[A] Baseline cũ có nhiều beige/muted green/coral cùng mức value, figure lặp dáng, đầu/thân không nhất quán giữa scene, quá nhiều hoạt động cùng tranh focus. R1 tăng azure/cyan, thay đồ/chi tiết và acting; không thể tiếp tục mô tả nó là chưa có text/effects. Tuy nhiên frame hiện tại cho thấy:

- S03: top navy wash chiếm nhiều vùng kiến trúc, chữ vẫn như một lớp headline tách khỏi vật liệu. Người đi bộ/café/runner cùng hiện, silhouette thân-tay-chân khá giống nhau; nhiều người ở xa cần camera mới đọc được. Thêm shutters/cornice không tự giải quyết focal hierarchy.
- S08: vùng biển/tường đủ chỗ cho chữ nhưng top wash và hai headline vẫn giành chú ý; parent/child contact endpoint có tiến bộ. Bàn tay chạm cùng tọa độ chưa chứng minh cẳng tay/cổ tay/elbow hợp lý trong toàn chuyển động. Không kết luận lỗi motion từ một still.
- Source `groundedStride`: xoay nguyên leg groups, dịch root tuyến tính; không có foot pin solve. `run` được nhận nhưng không đổi thuật toán gait. Đây là nguyên nhân cụ thể cần sửa khi animate, không phải lỗi GSAP.
- Source S08 đóng laptop bằng scaleY/skew của `#laptop-position`; bình luận “fixed hinge” không chứng minh lid rotation. Nếu group gồm cả base, chân đế sẽ bị biến dạng. Nên tách base/lid và tính các góc/vertices quanh hinge khi dựng mới.
- Cue IDs trong `pilot-highlights.json` là số thứ tự **1-based**, không phải zero-based array indices. onset seconds khớp ASR; không gọi off-by-one bug khi chưa hiểu convention.
- `creative/typography-keyframes-v1/`: đã có sáu HTML/PNG studies và boards; đọc README/studies và xem boards S03/S08. Chúng đề xuất type trên promenade/awning/wall/sea, không có navy wash, nhưng giữ nhiều figure/background từ artwork cũ. Đây là đầu vào thử nghiệm chưa duyệt, không phải bốn visual tests mới theo playbook.

## 6. Chẩn đoán để hành động

[A] Lỗ hổng chính nằm giữa mô tả style và construction: không có value thumbnail trước detail; recipe asset chưa quản lý mặt/pivot/contact; một world đông nhân vật được dùng để kể quá nhiều hoạt động; type được thêm sau staging nên phải tạo wash để dễ đọc; QA kỹ thuật tách rời revision media và creative QA. Tài liệu cũ cũng chứa các cấm đoán type không còn phù hợp. Chưa có bằng chứng để quy nguyên nhân cho model hoặc thiếu animation engine.

[P] Thay bằng chuỗi ngắn: **value/silhouette → illustration keyframe → type-integrated keyframe → human visual review → acting/timing implementation → MP4 review**. Playbook cung cấp cách dựng và cách sửa lỗi; bốn frame là bài kiểm tra đầu tiên, không lời hứa chất lượng.

## 7. Preservation và giới hạn snapshot

Lượt này không ghi vào VIDEO-34, AGENTS, setup hoặc skills. So 226 protected files giữa snapshot đầu/cuối phát hiện 42 file thay nội dung và 2 cache files mất, gồm source, MP4, QA và production status; thay đổi xảy ra đồng thời ngoài tập thao tác ghi của lượt nghiên cứu. Không thể báo “toàn project unchanged”. Master audio, project manifest, 17-interval manifest, raw transcript/ASR timestamps, logo gốc, root AGENTS và setup đều khớp hash đầu. Không khôi phục bất kỳ production file nào. Chi tiết cuối, hash media, cue evidence và kiểm link nằm trong `evidence/verification.json` và `voice-cue-evidence.json`.
