# Storyboard & Flow Routing — Du học Canada (ESORA)

## Scene 8: Dự Trù Cho Toàn Khóa

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 8
- **timeline**: 42.4s – 48.6s (Duration: 6.20s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Khái niệm lập kế hoạch tài chính dài hạn được truyền tải trọn vẹn thông qua visual storytelling hữu cơ 2D tách lớp (nhân vật tương tác vật thể thật: lật lịch, đặt phong bì, chồng xu, hồ sơ). HyperFrames điều phối 100% chuyển động vật lý, 3D flip, kinetic text và word-level sync mà không cần Flow, loại bỏ hoàn toàn nguy cơ wallpaper/poster stack.
- **visual_verb**: Page-turn, Character Interaction & Physical Budget Object Placement (Lật lịch, nhân vật chủ động thao tác và đặt các vật thể ngân sách thực tế lên bàn).
- **visible_text_budget**: 5 từ chính (“DỰ TRÙ CHO TOÀN KHÓA”) + 3 mốc tối giản (`01`, `02`, `03`). Tổng cộng: 8 từ/ký tự. Tuyệt đối không có phụ đề transcript, không narration card, không footnote.
- **container_required**: `false` (Bố cục Open-Canvas 100%, không dùng bất kỳ card hay box bao bọc text/layout nào).
- **container_semantics**: `none` (Không gian mở: bàn làm việc, nhân vật, lịch để bàn, 3 vật thể ngân sách vật lý).
- **narrative_visual**: Chiếm 55% diện tích khung hình khả dụng (Y: 260px đến 1060px). Gồm:
  - Nhân vật lập kế hoạch (cánh tay trái trực tiếp chạm lật trang lịch, cánh tay phải lần lượt đặt vật thể ngân sách lên bàn, biểu cảm mắt kính/nụ cười tập trung tự tin).
  - Lịch để bàn lò xo chân chữ A với trang lật 3D: Lần lượt qua 3 mốc `01` → `02` → `03`.
  - Ba vật thể ngân sách vật lý thực thụ trên mặt bàn:
    1. Vật thể 1 (`01`): Phong bì tài chính niêm phong xi đỏ (Sealed Financial Envelope).
    2. Vật thể 2 (`02`): Chồng đồng xu vàng Canada xếp lớp kim loại (Stacked Gold CAD Coins).
    3. Vật thể 3 (`03`): Tập hồ sơ bảo chứng tài chính bìa cứng dập nổi lá phong (Financial Dossier / Certificate).
- **opening_state (0.0s – 1.4s)**:
  - Headline open-canvas xuất hiện mạnh mẽ: `DỰ TRÙ CHO TOÀN KHÓA`.
  - Nhân vật ngồi tại bàn làm việc ở góc nhìn 3/4.
  - Lịch để bàn hiển thị trang đầu tiên: số to `01`.
  - Tay nhân vật đặt **Phong bì niêm phong (`01`)** lên mặt bàn.
- **transformation (1.4s – 4.2s)**:
  - **1.4s – 2.7s**: Tay nhân vật vươn sang lật trang lịch `01` sang `02` (3D page-turn flip). Đồng thời tay kia đặt **Chồng đồng xu vàng (`02`)** bên cạnh phong bì.
  - **2.7s – 4.0s**: Tay nhân vật tiếp tục lật trang lịch `02` sang `03` (3D page-turn flip). Đồng thời đưa **Tập hồ sơ bảo chứng tài chính (`03`)** hoàn tất bộ ba ngân sách toàn khóa.
  - Nhân vật ngẩng đầu mỉm cười tự tin nhìn vào kế hoạch hoàn chỉnh.
- **final_state (4.2s – 6.2s)**:
  - Bàn làm việc giữ vững ba vật thể tài chính hoàn tất (`01` Phong bì, `02` Chồng xu, `03` Hồ sơ) cùng lịch ở trang `03`.
  - Dưới tiêu đề `DỰ TRÙ CHO TOÀN KHÓA` xuất hiện vệt quét Warm Yellow highlight sweep `#FDE047`.
  - Toàn bộ nhãn dài dòng đã tiêu biến, chỉ còn lại 3 số mốc `01 · 02 · 03` gắn gọn trên từng vật thể.
  - Chân trang trống chuẩn **180px – 200px** (Y: 1080px – 1280px) dành riêng cho phụ đề nền tảng, không để trống quá 200px.
- **asset_contract**:
  - Open-canvas stage không viền/card.
  - Vector Desk (Y: 780px to 1060px).
  - Character Rig với thân, đầu có biểu cảm (chớp mắt/cười), 2 cánh tay hoạt họa độc lập tương tác lịch và vật thể.
  - 3D Desk Calendar với trang xoay lật 3D (`rotateX: -140deg`).
  - 3 Physical Budget Props: SVG Phong bì niêm phong xi, SVG Chồng xu CAD 3D, SVG Tập hồ sơ tài chính.
  - Audio: `scratch/scene_08_audio.wav` (6.20s).
- **hf_signature_motion**: 3D Page-Turn + Character Interaction + Physical Object Assembly (Lật trang lịch kết hợp cử động tay nhân vật tương tác và xếp đặt 3 vật thể ngân sách thực).
- **hf_supporting_motion**: Warm Yellow highlight sweep dưới `TOÀN KHÓA` + biểu cảm nhân vật gật đầu tự tin.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1080px (Safe zones: Top 120px, Bottom 200px, Sides 50px).
- **occlusion_order**: Canvas Ambient Glow (z: 1) → Desk Surface (z: 10) → Physical Props (z: 20) → Calendar (z: 25) → Character (z: 30) → Headline (z: 40).
- **transition_in**: Clean physical entrance (nhân vật và bàn ổn định, vật thể 1 đáp nhẹ).
- **transition_out**: Stable final hold (4.8s – 6.2s) chuẩn bị cắt sang Scene 9.

---

## Scene 9: Ngoại Lệ Québec & Quy Trình CAQ

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 9
- **timeline**: 48.6s – 60.6s (Duration: 12.00s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Tỉnh bang Québec có cơ chế di trú và quy định tài chính riêng biệt so với chính phủ liên bang Canada: du học sinh bắt buộc phải có Giấy chấp thuận CAQ (Certificat d'acceptation du Québec) và chứng minh mức tài chính cao hơn (> 24.600 CAD ~ 460 triệu VNĐ cho đương đơn chính). Phân cảnh yêu cầu tính chuẩn xác cao về văn bản pháp lý, hiệu ứng dập mộc hành chính CAQ, biểu đồ so sánh nấc thang tài chính Québec vs Liên bang và kinetic numbers đồng bộ word-level trong suốt 12.0s. HyperFrames điều phối 100% chuyển động vector chuẩn xác, loại bỏ hoàn toàn hiện tượng nhòe số liệu.
- **visual_verb**: STAMP & ELEVATE (Đóng dấu phê duyệt chứng thực CAQ & Nâng mức trần định mức tài chính).
- **visible_text_budget**: 
  - Headline: `QUÉBEC: QUY ĐỊNH RIÊNG` (4 từ).
  - Document Anchor: `CAQ` (kèm mộc tròn `CHẤP THUẬN`). Toàn bộ chữ nhỏ giả lập trên tài liệu đã được tinh giản, không gây nhiễu thị giác.
  - Số liệu trên cao: `> 24.600 CAD` (~`460 TRIỆU`) (5 từ).
  - Chân cột biểu đồ: Chỉ để `LIÊN BANG` và `QUÉBEC` (loại bỏ hoàn toàn lặp số 24.600 CAD hoặc 23.400 CAD ở chân cột).
  - Loại bỏ hoàn toàn: `ĐƯƠNG ĐƠN CHÍNH`, `MỨC CAO HƠN`.
  - Tổng số từ hiển thị đồng thời: <= 9 từ. Không có phụ đề thừa lặp lại lời thoại.
- **container_required**: `true`
- **container_semantics**: `document` (Duy nhất 01 vật thể container: Bản tài liệu Chứng thực CAQ chính thức được tinh giản, chỉ giữ tiêu đề CAQ nổi bật và con dấu mộc tròn dập xuống).
- **narrative_visual**: Chiếm 55% diện tích khung hình khả dụng (Y: 230px đến 1060px):
  1. Huy hiệu Hoa Bách Hợp (Fleur-de-lis) của Québec xác lập bối cảnh tỉnh bang.
  2. Văn bản chính thức CAQ với tiêu đề CAQ và con dấu tròn mộc đỏ `CAQ CHẤP THUẬN` đóng mạnh xuống làm visual anchor.
  3. Hệ thống Cột so sánh tài chính có bệ đỡ nối đất (Y: 1060px): Cột Liên bang xám nhẹ (`LIÊN BANG`) và Cột Québec cam rực rỡ (`QUÉBEC`) vươn cao, đẩy con số `> 24.600 CAD` (~`460 TRIỆU`) lên vị thế nổi bật nhất.
- **opening_state (0.0s – 3.2s)**:
  - Lời thoại: *"Riêng Québec có quy định khác..."*
  - Headline open-canvas xuất hiện: `QUÉBEC: QUY ĐỊNH RIÊNG`.
  - Huy hiệu hoa bách hợp Fleur-de-lis xuất hiện tao nhã, xác định thẩm quyền đặc thù của Québec.
- **transformation (3.2s – 9.0s)**:
  - **3.2s – 6.5s**: Lời thoại: *"...du học sinh cần thực hiện thêm quy trình CAQ..."*
    - Bản tài liệu CAQ chính thức trượt êm vào trung tâm.
    - Con dấu cơ quan di trú dập mạnh xuống góc giấy: `CAQ • CHẤP THUẬN` (Stamp impact: đập nảy 2.3x -> 1.0x kèm vòng sóng xung lực).
  - **6.5s – 9.0s**: Lời thoại: *"...và phải chứng minh mức tài chính cao hơn mức chung..."*
    - Bản CAQ dịch chuyển sang trái làm chứng thư bảo trợ.
    - Hai cột so sánh tài chính mọc từ đường bệ đỡ đáy: Cột `LIÊN BANG` làm chuẩn, cột `QUÉBEC` bứt phá vươn cao.
- **final_state (9.0s – 12.0s)**:
  - Lời thoại: *"...hơn 24.600 Canada tương đương khoảng 460 triệu đồng cho người nộp đơn chính."*
  - Con số khổng lồ Montserrat 900 `> 24.600 CAD` sáng rực với hiệu ứng highlight Warm Yellow `#FDE047`.
  - Khối quy đổi thực tế `~460 TRIỆU` đúc nổi 2.5D tone Brand Orange viền `#FF6B2B`.
  - Hai chân cột biểu đồ chỉ ghi nhãn tinh gọn: `LIÊN BANG` và `QUÉBEC`.
  - Vùng chân trang trống tuyệt đối chuẩn **200px** (Y: 1080px – 1280px) dành cho phụ đề nền tảng.
- **asset_contract**:
  - Open-canvas background với grid nhẹ và radial glow.
  - SVG Fleur-de-lis Québec emblem.
  - SVG Official CAQ Certificate Document (họa tiết viền văn bản, tiêu đề, mã số hồ sơ).
  - SVG Official Stamp Seal (con dấu mộc đỏ tròn dập xuống giấy).
  - SVG Financial Comparative Bar / Pillar (thước đo vạch mốc Liên bang vs Québec).
  - Audio: `scratch/scene_09_audio.wav` (12.00s).
- **hf_signature_motion**: Official Document Stamp (Đóng dấu đập nảy dứt khoát lên tài liệu CAQ) + Comparative Metric Elevation (Vạch mốc tài chính vươn vọt vượt chuẩn liên bang).
- **hf_supporting_motion**: Warm Yellow highlight sweep dưới `24.600 CAD` + subtle pulse trên con dấu CAQ.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1080px (Top safe 120px, Bottom clean footer 200px, Sides safe 60px).
- **occlusion_order**: Background (z: 1) → CAQ Document (z: 10) → Stamp Seal (z: 20) → Comparative Elevation Gauge (z: 30) → Hero Numerals (z: 40) → Headline (z: 50).
- **transition_in**: Clean physical entrance, biểu tượng Québec khai mở.
- **transition_out**: Stable final hold (10.0s – 12.0s) chuẩn bị cắt sang Scene 10.

---

## Scene 10: Bước Ngoặt Tư Duy — Không Chỉ Đủ Tiền Nộp Hồ Sơ

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 10
- **timeline**: 60.6s – 67.0s (Duration: 6.40s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Phân cảnh mang tính bước ngoặt tư duy cốt lõi của video (Thesis Turning Point / Mindset Shift): chuyển đổi từ quan niệm hạn hẹp "chỉ cần đủ tiền trong sổ tiết kiệm để nộp hồ sơ visa" sang "kế hoạch tài chính dài hạn toàn khóa". Đòi hỏi sự kết hợp chính xác giữa đối tượng vật lý tập hồ sơ visa, dấu cảnh báo phủ định Brand Orange `✕`, biểu tượng lộ trình dài hạn bung mở và kinetic typography dứt khoát đồng bộ với lời thoại 6.4s. HyperFrames điều phối 100% vector và timeline chính xác, loại bỏ hoàn toàn hiện tượng video wallpaper.
- **visual_verb**: STRIKE & EXPAND (Phủ định tư duy cục bộ "đủ tiền nộp đơn" & Mở rộng tầm nhìn lộ trình dài hạn).
- **visible_text_budget**: 
  - Headline: `KHÔNG CHỈ ĐỦ TIỀN NỘP HỒ SƠ` (6 từ).
  - Điểm xuất phát: `BƯỚC ĐẦU: NỘP ĐƠN` (bị phủ định tư duy duy nhất).
  - Tầm nhìn mới: `LỘ TRÌNH TOÀN KHÓA` (4 từ).
  - Tổng số từ hiển thị đồng thời: <= 9 từ. Không có phụ đề thừa, không footnote lặp lại narration.
- **container_required**: `false` (Bố cục 100% open-canvas; tập hồ sơ là physical prop, không dùng card/box bao bọc text).
- **container_semantics**: `none`
- **narrative_visual**: Chiếm 52% diện tích khung hình khả dụng (Y: 230px đến 1060px):
  1. Tập hồ sơ thị thực Visa Dossier (vật thể vật lý với bìa kẹp và nhãn VISA).
  2. Dấu phủ định cảnh báo mang sắc cam Brand Orange `#FF6B2B` dập dấu `✕` cảnh báo tư duy hạn hẹp.
  3. Lộ trình dài hạn (Expanding Journey Path / Horizon): Con đường tương lai bung mở với các cột mốc dài hạn vươn xa.
  4. Nhân vật tư vấn / định hướng với cử chỉ chỉ tay mở rộng tầm nhìn, biểu cảm tự tin và thấu đáo.
- **opening_state (0.0s – 2.2s)**:
  - Lời thoại: *"Điều này cho thấy khi chuẩn bị du học Canada..."*
  - Headline open-canvas xuất hiện: `KHÔNG CHỈ ĐỦ TIỀN NỘP HỒ SƠ`.
  - Tập hồ sơ thị thực Visa Dossier xuất hiện trang trọng ở trung tâm.
- **transformation (2.2s – 4.8s)**:
  - Lời thoại: *"...tài chính không nên chỉ được tính đơn giản là đủ tiền để nộp hồ sơ."*
  - Dấu cảnh báo phủ định `✕` Brand Orange dập mạnh lên tập hồ sơ.
  - Tập hồ sơ thu nhỏ và trượt lùi về vạch xuất phát bên trái.
  - Từ điểm xuất phát, một con đường lộ trình năng động bung mở sang phải và vươn dài về phía trước kèm nhãn `LỘ TRÌNH TOÀN KHÓA`.
  - Nhân vật xuất hiện tự tin chỉ tay về phía tầm nhìn rộng lớn.
- **final_state (4.8s – 6.4s)**:
  - Thông điệp chốt hạ: Hồ sơ visa chỉ là `BƯỚC ĐẦU`, tâm điểm chuyển sang `LỘ TRÌNH TOÀN KHÓA`.
  - Vệt highlight Warm Yellow `#FDE047` quét dưới cụm từ `NỘP HỒ SƠ`.
  - Chân bệ đỡ nối đất vững chắc tại Y: 1060px, giữ vùng chân trang sạch sẽ tuyệt đối **200px** (Y: 1060px – 1280px) cho phụ đề nền tảng.
- **asset_contract**:
  - Open-canvas background với subtle grid và radial glow.
  - SVG Visa Dossier Folder (tập hồ sơ bìa navy, nhãn VISA, kẹp kim loại).
  - SVG Warning Denial Stamp (`✕` Brand Orange `#FF6B2B`).
  - SVG Expanding Journey Horizon / Roadmap with milestone nodes.
  - Character Rig với tư thế định hướng / chỉ đường đáng tin cậy.
  - Audio: `scratch/scene_10_audio.wav` (6.40s).
- **hf_signature_motion**: Strike & Horizon Expansion (Dấu phủ định tư duy hẹp và con đường lộ trình toàn khóa bung mở).
- **hf_supporting_motion**: Warm Yellow highlight sweep dưới headline + cử chỉ nhân vật mở rộng tầm nhìn.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 135px đến 1060px (Top safe 120px, Bottom clean footer 200px, Sides safe 60px).
- **occlusion_order**: Background (z: 1) → Ground Pedestal (z: 10) → Journey Path (z: 20) → Visa Dossier (z: 30) → Warning Strike (z: 40) → Character (z: 45) → Headline (z: 50).
- **transition_in**: Clean physical entrance.
- **transition_out**: Stable final hold (5.4s – 6.4s) chuẩn bị dẫn vào Scene 11 (bóc tách 5 khoản chi phí thực tế).

---

## Scene 11: 5 Khoản Cần Tính Trước

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 11
- **timeline**: 67.0s – 74.6s (Duration: 7.60s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Phân cảnh bóc tách chi tiết 5 hạng mục tài chính cốt lõi mà gia đình du học sinh bắt buộc phải dự tính toàn diện (Học phí, Sinh hoạt phí, Đi lại, Số người đi cùng, Kế hoạch toàn khóa học). Nội dung đòi hỏi tính kiến trúc cấu trúc mạch lạc, chuyển động lắp ghép module (modular assembly) của 5 khối vector tượng trưng độc lập, khớp chính xác từng từ của voiceover suốt 7.60s. HyperFrames kiểm soát 100% vector animation, kinetic lock và visual hierarchy, loại bỏ hoàn toàn nguy cơ video wallpaper hay card/pill dư thừa.
- **visual_verb**: DOCK & UNIFY (Lắp ghép 5 khối trụ ngân sách vật lý vào hệ thống bệ đỡ và khóa liên kết thành chỉnh thể kế hoạch dài hạn).
- **visible_text_budget**: 
  - Headline: `5 KHOẢN CẦN TÍNH TRƯỚC` (5 từ).
  - Khối neo tổng thể kết thúc: `KẾ HOẠCH DÀI HẠN` (4 từ).
  - Tổng số từ hiển thị ở final hold: 9 từ (<= 10 từ).
  - Không có phụ đề transcript lặp lại narration, không liệt kê chữ dài dòng cho từng icon ở final frame (các nhãn đã collapse thành visual states / icon tokens).
- **visible_text_inventory**:
  - `core_phrase`: `5 KHOẢN CẦN TÍNH TRƯỚC` (Headline)
  - `necessary_label`: `KẾ HOẠCH DÀI HẠN` (Total synthesis anchor)
  - `diegetic_text`: none
  - `remove`: Loại bỏ toàn bộ các câu diễn giải như "Học phí đại học", "Chi phí sinh hoạt ăn ở", "Vé máy bay đi lại" khỏi final hold để tránh tích tụ nhãn (label accumulation).
- **container_required**: `false` (Bố cục 100% open-canvas; 5 khối module là các visual prop tokens đặt trên bệ đỡ kiến trúc, không bọc card hay text box).
- **container_semantics**: `none`
- **narrative_visual**: Chiếm 58% diện tích khung hình khả dụng (Y: 230px đến 1060px):
  1. Bệ đỡ kiến trúc cân bằng tài chính (Architectural Financial Pedestal Beam) tại trục đáy Y: 860px – 920px.
  2. 5 Khối Token Ngân sách Vector độc lập (SVG separated tokens) lần lượt đáp xuống theo nhịp lời thoại:
     - Khối 1: Mũ tốt nghiệp & Bằng đại học (🎓 Học phí - Tuition)
     - Khối 2: Mái nhà ấm cúng & Đồ sinh hoạt (🏠 Sinh hoạt - Living)
     - Khối 3: Máy bay cất cánh & Tuyến hành trình (✈️ Đi lại - Travel)
     - Khối 4: Cụm gia đình gồm bố mẹ và học sinh (👨‍👩‍👧 Người đi cùng - Family)
     - Khối 5: Lịch trình toàn khóa & Vòng thời gian (📅 Toàn thời gian học - Full Duration)
  3. Cơ chế Khóa cân bằng (Total Synthesis Lock & Gold Circuit): Khi khối thứ 5 đáp xuống, một luồng ánh sáng mạch vàng `#FDE047` kết nối 5 trụ lại thành một khối thống nhất, nâng đỡ huy hiệu `KẾ HOẠCH DÀI HẠN`.
- **opening_state (0.0s – 1.8s)**:
  - Lời thoại: *"Gia đình cần tính trước..."*
  - Headline open-canvas xuất hiện: `5 KHOẢN CẦN TÍNH TRƯỚC` cùng thanh nhấn thương hiệu.
  - Khung bệ đỡ tài chính nền tảng xuất hiện định hình 5 vị trí module.
- **transformation (1.8s – 5.4s)**:
  - Lời thoại: *"...học phí, chi phí sinh hoạt, chi phí đi lại, số người đi cùng..."*
  - **1.8s – 2.6s**: Khối 1 (Mũ tốt nghiệp) rơi đáp xuống slot 1 với hiệu ứng nảy nhẹ (elastic bounce).
  - **2.6s – 3.4s**: Khối 2 (Mái nhà sinh hoạt) đáp xuống slot 2.
  - **3.4s – 4.2s**: Khối 3 (Máy bay đi lại) lướt vào slot 3.
  - **4.2s – 5.0s**: Khối 4 (Cụm gia đình) đáp xuống slot 4.
  - **5.0s – 5.8s**: Lời thoại: *"...và kế hoạch tài chính cho toàn bộ thời gian học."* Khối 5 (Lịch trình toàn khóa) khóa vào slot trung tâm/cuối cùng.
- **final_state (5.4s – 7.6s)**:
  - Cả 5 khối module đồng loạt liên kết thành một bức tường kiên cố trên bệ đỡ.
  - Huy hiệu tổng thể `KẾ HOẠCH DÀI HẠN` sáng lên ở đỉnh vòm liên kết.
  - Vùng chân trang Y: 1060px – 1280px hoàn toàn sạch sẽ, giữ đúng **220px** cho phụ đề.
- **asset_contract**:
  - Open-canvas stage với ambient glow và subtle technical grid.
  - SVG Financial Pedestal Beam & docking slots.
  - 5 Separated SVG Tokens:
    1. `token_tuition`: Graduation cap & degree diploma.
    2. `token_living`: House roof with cozy window & groceries.
    3. `token_travel`: Jet plane with travel route arc.
    4. `token_family`: 3-person family silhouette group.
    5. `token_timeline`: Master calendar with progressive gears.
  - SVG Total Synthesis Lock Beam & Gold Circuit Badge.
  - Audio: `scratch/scene_11_audio.wav` (7.60s).
- **hf_signature_motion**: Modular Pillar Docking & Total Synthesis Lock (Lắp ghép lần lượt 5 khối ngân sách vector đồng bộ voiceover và kích hoạt luồng sáng khóa liên kết toàn diện).
- **hf_supporting_motion**: Warm Yellow highlight pulse trên từng khối khi đáp + elastic micro-bounce.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1060px (Top safe 120px, Bottom clean footer 220px, Sides safe 60px).
- **handoff**: none
- **occlusion_order**: Background (z: 1) → Ground Pedestal (z: 10) → 5 Docking Slots (z: 20) → 5 Budget Tokens (z: 30) → Synthesis Lock Circuit (z: 40) → Total Badge (z: 45) → Headline (z: 50).
- **transition_in**: Clean physical entrance, bệ đỡ định hình.
- **transition_out**: Stable final hold (6.2s – 7.6s) chuẩn bị dẫn vào Scene 12.

---

## Scene 12: Bối Cảnh Chính Sách — Kiểm Soát Số Lượng & Siết Chặt Xét Duyệt

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 12
- **timeline**: 75.0s – 80.6s (Duration: 5.60s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Phân cảnh bước ngoặt thể hiện áp lực chính sách siết chặt chỉ tiêu du học sinh (intake cap) và thẩm định hồ sơ nghiêm ngặt của chính phủ Canada. Yêu cầu kể chuyện thị giác sống động (visual storytelling) thông qua sự tương tác trực tiếp giữa nhân vật du học sinh (cầm hồ sơ tiến bước) và cơ chế thẩm định chính thức: cổng van chỉ tiêu Canada thu hẹp khẩu độ và kính lúp kiểm duyệt hạ xuống quét sâu vào hồ sơ. HyperFrames điều phối 100% chuyển động nhân vật, quang học vector và timing chính xác 5.60s mà không gây lặp lại bố cục các cảnh trước.
- **visual_verb**: CONSTRICT & SCRUTINIZE (Khẩu độ chỉ tiêu thu hẹp & Kính lúp kiểm duyệt thẩm định trực tiếp hồ sơ du học sinh).
- **visible_text_budget**: 
  - Headline: `CANADA: SIẾT CHẶT XÉT DUYỆT` (5 từ).
  - Khối neo trạng thái kết thúc: `TIÊU CHÍ KHẮC KHE` (3 từ).
  - Tổng số từ ở final hold: 8 từ (<= 10 từ).
  - Không có phụ đề transcript lặp lại narration, không dùng card/box bọc text.
- **visible_text_inventory**:
  - `core_phrase`: `CANADA: SIẾT CHẶT XÉT DUYỆT` (Headline)
  - `necessary_label`: `TIÊU CHÍ KHẮC KHE` (Status anchor)
  - `diegetic_text`: `VISA CANADA` (trên bìa hồ sơ sinh viên cầm)
  - `remove`: Loại bỏ toàn bộ các câu giải thích phụ trợ dài dòng khỏi màn hình.
- **container_required**: `false` (Bố cục 100% open-canvas; nhân vật, cổng kiểm soát và kính lúp là các visual object props tách lớp độc lập).
- **container_semantics**: `none`
- **narrative_visual**: Chiếm 62% diện tích khung hình khả dụng (Y: 230px đến 1060px):
  1. Nhân vật Du học sinh (Student Character with Backpack) ở cánh trái (X: 50px – 320px, Y: 460px – 1050px), mang balo, hai tay chủ động nâng tập hồ sơ xin Visa tiến về phía cổng thẩm định.
  2. Cổng kiểm soát hạn ngạch Canada (Canadian Intake Quota Portal) ở phía trên/phải (X: 340px – 670px, Y: 240px – 580px): cổng chính phủ với huy hiệu Lá phong đỏ, hai cánh van khẩu độ (aperture gates) màu Brand Orange `#FF6B2B` siết hẹp lại.
  3. Kính lúp thẩm định quang học (Optical Scrutiny Loupe & Reticle): từ cổng thẩm định, chiếc kính lúp phóng đại hạ xuống soi trực tiếp vào tập hồ sơ trên tay sinh viên, chiếu sáng các điểm nút tài chính/kế hoạch và đóng mộc phê duyệt nghiêm ngặt.
  4. Khối neo bảo chứng an ninh: `TIÊU CHÍ KHẮC KHE` với ổ khóa bảo mật vàng `#FDE047`.
- **opening_state (0.0s – 1.6s)**:
  - Lời thoại: *"Đặc biệt, trong bối cảnh Canada đang tiếp tục..."*
  - Headline open-canvas xuất hiện: `CANADA: SIẾT CHẶT XÉT DUYỆT` cùng vệt gạch chân Warm Yellow `#FDE047`.
  - Du học sinh mang balo bước vào với dáng vẻ tự tin, hai tay nâng tập hồ sơ. Cổng tiếp nhận Canada mở rộng ở phía trên.
- **transformation (1.6s – 4.2s)**:
  - Lời thoại: *"...kiểm soát số lượng sinh viên quốc tế..."*
  - **1.6s – 2.8s**: Hai cánh van cổng hạn ngạch Canada Brand Orange siết mạnh từ 2 phía, khe nhận thu hẹp chỉ còn một vạch hẹp nghiêm ngặt (`HẠN NGẠCH`).
  - **2.8s – 4.2s**: Lời thoại: *"...và siết chặt quy trình xét duyệt."*
    - Sinh viên đưa tập hồ sơ vào vùng thẩm định.
    - Kính lúp quang học lớn hạ xuống phóng đại hồ sơ, quét chùm tia laser quang học qua các trang văn bản, khóa hồng tâm ngắm kiểm tra.
- **final_state (4.2s – 5.6s)**:
  - Cổng hạn ngạch khóa chốt; kính lúp khóa điểm kiểm duyệt với dấu tick xanh/vàng.
  - Khối bảo chứng `TIÊU CHÍ KHẮC KHE` sáng rực bên dưới cổng.
  - Sinh viên đứng vững chãi, nắm chắc hồ sơ với biểu cảm thấu đáo và kiên định.
  - Vùng chân trang Y: 1060px – 1280px hoàn toàn sạch sẽ, giữ đúng **220px** cho phụ đề nền tảng.
- **asset_contract**:
  - Open-canvas stage với ambient glow và subtle technical grid.
  - SVG Student Character Rig (đầu, thân áo jacket học sinh, balo đeo vai, cánh tay cầm hồ sơ đưa lên).
  - SVG Canadian Quota Portal with Maple Leaf Crest & Aperture Constriction Gates.
  - SVG Optical Scrutiny Loupe & Laser Scanner Reticle.
  - SVG Inspected Study Permit Dossier.
  - SVG Security Lock Shield Badge.
  - Audio: `scratch/scene_12_audio.wav` (5.60s).
- **hf_signature_motion**: Quota Constriction & Loupe Scrutiny Inspection (Cổng hạn ngạch thu hẹp khẩu độ và Kính lúp thẩm định quang học hạ xuống soi quét trực tiếp hồ sơ trên tay du học sinh).
- **hf_supporting_motion**: Warm Yellow highlight sweep dưới headline + chùm tia quét laser trên hồ sơ.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1060px (Top safe 120px, Bottom clean footer 220px, Sides safe 60px).
- **handoff**: none
- **occlusion_order**: Background (z: 1) → Ground Pedestal (z: 10) → Quota Portal (z: 20) → Aperture Gates (z: 25) → Student Rig (z: 30) → Scrutiny Loupe & Laser (z: 40) → Security Badge (z: 45) → Headline (z: 50).
- **transition_in**: Clean physical entrance.
- **transition_out**: Stable final hold (4.6s – 5.6s) chuẩn bị dẫn vào Scene 13.

---

## Scene 13: Phương Pháp Luận ESORA — Lộ Trình Chiến Lược Đa Chiều

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 13
- **timeline**: 80.6s – 86.6s (Duration: 6.00s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Phân cảnh xác lập phương pháp luận định vị thương hiệu của ESORA: phá vỡ quan niệm tư vấn du học truyền thống vốn chỉ bó hẹp ở 2 bước cơ học ("chọn trường" và "chuẩn bị hồ sơ"), nâng tầm thành một bản đồ lộ trình chiến lược dài hạn đa chiều. Đòi hỏi chuyển động bứt phá ranh giới (boundary breakthrough), trải rộng mạng lưới bản đồ quy hoạch (strategic roadmap unfurl) và la bàn định hướng hoàng kim đồng bộ chính xác từng từ với voiceover 6.00s. HyperFrames điều phối 100% vector animation, precision motion và visual hierarchy, bảo toàn hoàn hảo nhận diện thương hiệu chuẩn ESORA.
- **visual_verb**: EXPAND & NAVIGATE (Bứt phá giới hạn 2 bước cơ học truyền thống & Trải rộng mạng lưới bản đồ chiến lược cùng la bàn định hướng ESORA).
- **visible_text_budget**: 
  - Headline: `ESORA: LỘ TRÌNH CHIẾN LƯỢC` (4 từ).
  - Khối neo trạng thái kết thúc: `ĐỊNH HƯỚNG TOÀN DIỆN` (4 từ).
  - Tổng số từ ở final hold: 8 từ (<= 10 từ).
  - Không có phụ đề transcript lặp lại narration, không dùng card/box bọc text.
- **visible_text_inventory**:
  - `core_phrase`: `ESORA: LỘ TRÌNH CHIẾN LƯỢC` (Headline)
  - `necessary_label`: `ĐỊNH HƯỚNG TOÀN DIỆN` (Status synthesis anchor)
  - `diegetic_text`: `ESORA` (Brand mark)
  - `remove`: Loại bỏ toàn bộ các câu giải thích phụ trợ ("Không chỉ dừng ở việc chọn trường", "Không chỉ chuẩn bị hồ sơ") để bảo toàn text economy.
- **container_required**: `false` (Bố cục 100% open-canvas, bản đồ lộ trình là mạng lưới quy hoạch không gian mở, không bọc card hay text box).
- **container_semantics**: `none`
- **narrative_visual**: Chiếm 60% diện tích khung hình khả dụng (Y: 230px đến 1060px):
  1. Hai mốc cơ học ban đầu: Mốc 1 (🏫 Chọn trường) và Mốc 2 (📄 Chuẩn bị hồ sơ) xuất hiện đóng khung hẹp, tượng trưng cho cách làm thông thường.
  2. Mạng lưới Bản đồ Chiến lược ESORA (Strategic Roadmap Grid): Đúng nhịp *"không chỉ dừng ở việc..."*, các đường mạch quy hoạch màu Brand Orange `#FF6B2B` và ánh vàng `#FDE047` phóng tỏa đa chiều ra xung quanh, biến 2 mốc đơn lẻ thành các điểm nút trong một hệ sinh thái lộ trình rộng lớn.
  3. La bàn Định hướng Hoàng kim (ESORA Golden Strategic Compass): Chiếc la bàn kim loại tinh xảo với kim chỉ hướng vàng chỉ thẳng về phía mục tiêu tương lai, xoay và khóa góc định vị chính xác.
  4. Khối neo bảo chứng giải pháp: `ĐỊNH HƯỚNG TOÀN DIỆN` với biểu tượng ngôi sao dẫn đường đa giác.
- **opening_state (0.0s – 1.8s)**:
  - Lời thoại: *"Vì vậy, tại ESORA..."*
  - Headline open-canvas xuất hiện: `ESORA: LỘ TRÌNH CHIẾN LƯỢC` cùng vệt gạch chân Warm Yellow `#FDE047`.
  - Hai biểu tượng cơ học ban đầu (Trường học và Tập hồ sơ) xuất hiện ở trung tâm trong phạm vi hẹp.
- **transformation (1.8s – 4.2s)**:
  - Lời thoại: *"...việc xây dựng lộ trình du học không chỉ dừng ở việc chọn trường hay chuẩn bị hồ sơ."*
  - **1.8s – 3.2s**: Ranh giới hẹp bị phá vỡ; một mạng lưới lộ trình đa chiều gồm các vạch định vị, cung tọa độ và đường mạch kết nối bung tỏa mạnh mẽ ra toàn canvas (Strategic Blueprint Unfurl).
  - **3.2s – 4.2s**: Chiếc La bàn Chiến lược ESORA (với kim vàng xoay và khóa góc Bắc - Tương lai) xuất hiện ở vị trí trung tâm chỉ huy, định hướng toàn bộ lộ trình.
- **final_state (4.2s – 6.0s)**:
  - Bản đồ chiến lược giữ vững kết cấu đa chiều hoàn chỉnh, các nút liên kết phát quang rực rỡ.
  - Khối neo `ĐỊNH HƯỚNG TOÀN DIỆN` sáng rực bên dưới làm điểm tựa niềm tin cho du học sinh và gia đình.
  - Vùng chân trang Y: 1060px – 1280px hoàn toàn sạch sẽ, giữ đúng **220px** cho phụ đề nền tảng.
- **asset_contract**:
  - Open-canvas stage với ambient glow và subtle technical blueprint grid.
  - SVG 2 Conventional Step Tokens (Trường học & Hồ sơ).
  - SVG Multi-dimensional Strategic Roadmap Grid (mạng lưới đường mạch, vòng tròn tọa độ, các điểm nút phát quang).
  - SVG ESORA Golden Strategic Compass (vành la bàn kim loại, kim chỉ hướng vàng đa giác, mặt độ chia).
  - SVG Guidance Star Anchor Badge (`ĐỊNH HƯỚNG TOÀN DIỆN`).
  - Audio: `scratch/scene_13_audio.wav` (6.00s).
- **hf_signature_motion**: Boundary Expansion & Compass Alignment (Phá vỡ ranh giới 2 bước cơ học, bung tỏa mạng lưới bản đồ lộ trình đa chiều và kim la bàn vàng định vị mục tiêu tương lai).
- **hf_supporting_motion**: Warm Yellow highlight sweep dưới headline + ánh sáng chạy dọc các đường mạch chiến lược.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1060px (Top safe 120px, Bottom clean footer 220px, Sides safe 60px).
- **handoff**: none
- **occlusion_order**: Background (z: 1) → Ground Pedestal (z: 10) → Strategic Grid (z: 20) → Conventional Step Nodes (z: 25) → Strategic Compass (z: 35) → Synthesis Badge (z: 40) → Headline (z: 50).
- **transition_in**: Clean physical entrance.
- **transition_out**: Stable final hold (5.0s – 6.0s) chuẩn bị dẫn vào Scene 14 (bóc tách 5 định hướng chi tiết: trường, ngành, ngân sách, học bổng, tài chính).

---

## Scene 14: Phương Pháp Luận ESORA — 5 Trụ Cột Định Hướng Toàn Diện

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 14
- **timeline**: 86.6s – 93.6s (Duration: 7.00s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Phân cảnh bóc tách chi tiết hệ thống 5 trụ cột chiến lược dài hạn theo phương pháp luận ESORA: 1. Trường học, 2. Ngành học, 3. Ngân sách dự trù, 4. Học bổng, 5. Kế hoạch tài chính toàn trình. Toàn bộ 5 mốc liên kết trên một trục quỹ đạo hình học liên tục (Unified Strategic Trajectory Arc), kích hoạt lần lượt và khóa lại thành một cấu trúc quy hoạch vững chãi. Đòi hỏi vector precision timing tuyệt đối đồng bộ từng từ trong 7.00s thoại, tuân thủ nghiêm ngặt nhận diện thương hiệu ESORA.
- **visual_verb**: ASSEMBLE & LOCK (Kích hoạt tuần tự và khóa liên kết 5 trụ cột chiến lược vào một cung quỹ đạo quy hoạch thống nhất).
- **visible_text_budget**: 
  - Headline: `5 TRỤ CỘT CHIẾN LƯỢC` (4 từ).
  - Khối neo trạng thái kết thúc: `KẾ HOẠCH DÀI HẠN` (4 từ).
  - 5 mốc số thứ tự: `01 · 02 · 03 · 04 · 05` (diegetic counters tích hợp trong icon token).
  - Tổng số từ ở final hold: 8 từ (<= 10 từ).
  - Không có phụ đề transcript lặp lại narration, không dùng card/box bọc text.
- **visible_text_inventory**:
  - `core_phrase`: `5 TRỤ CỘT CHIẾN LƯỢC` (Headline)
  - `necessary_label`: `KẾ HOẠCH DÀI HẠN` (Status synthesis anchor)
  - `diegetic_text`: `ESORA • DU HỌC CANADA` (Brand mark)
  - `remove`: Loại bỏ toàn bộ các câu giải thích phụ trợ ("Định hướng từ trường", "Kế hoạch cho toàn bộ hành trình") để bảo toàn text economy.
- **container_required**: `false`
- **container_semantics**: `none`
- **container_inventory**: []
- **boundary_removal_test**: "Không sử dụng bất kỳ container nào. 5 trụ cột là các physical token phân bổ trên trục lộ trình dọc (Vertical Blueprint Pathway) không gian mở. Nếu vẽ khung card quanh từng mốc, scene sẽ thoái hóa thành slide checklist vi phạm quy chuẩn."
- **vertical_occupancy_plan**: "Trục lộ trình chữ S uốn lượn trải dài từ Y: 220px đến Y: 920px; 5 mốc phân bổ so le nhịp nhàng tạo luồng đọc dọc liên tục, khắc phục triệt để lỗi dồn cục ở nửa trên."
- **narrative_visual**: Chiếm 70% diện tích khả dụng (Y: 200px đến 1040px):
  1. Con đường Chiến lược May đo Dọc (Vertical Strategic Roadmap Spine): Đường dẫn vector uốn lượn liên kết không gian từ trên xuống dưới.
  2. 5 Biểu tượng Trụ cột Tách lớp (5 Physical Strategic Tokens) gắn liền trên lộ trình:
     - Mốc 01 (🏫 Trường học - Campus Gate)
     - Mốc 02 (🎯 Ngành học - Target Compass)
     - Mốc 03 (🪙 Ngân sách - Budget Vault)
     - Mốc 04 (🎓 Học bổng - Scholarship Honor)
     - Mốc 05 (🛡️ Tài chính toàn trình - Growth Shield)
  3. Dây cáp mạch dẫn năng lượng (Circuit Data Bus) chạy dọc kích hoạt lần lượt 5 trạm mốc.
  4. Khối neo giải pháp: `KẾ HOẠCH DÀI HẠN` tại Y: 940px.
- **opening_state (0.0s – 1.8s)**:
  - Lời thoại: *"Học viên và gia đình cần được định hướng..."*
  - Top branding `ESORA • DU HỌC CANADA` và Headline `5 TRỤ CỘT CHIẾN LƯỢC` xuất hiện open-canvas.
  - Trục lộ trình vector mờ xuất hiện trải dọc canvas từ Y: 220px đến 920px.
- **transformation (1.8s – 5.0s)**:
  - Lời thoại: *"...từ trường, ngành, ngân sách, học bổng, đến kế hoạch tài chính cho toàn bộ hành trình."*
  - **1.8s – 2.4s**: Mốc 01 (🏫 Trường) cắm neo phát quang.
  - **2.4s – 3.0s**: Mốc 02 (🎯 Ngành) kích hoạt với mạch dẫn cam `#FF6B2B`.
  - **3.0s – 3.6s**: Mốc 03 (🪙 Ngân sách) bừng sáng sắc vàng Warm Yellow `#FDE047`.
  - **3.6s – 4.2s**: Mốc 04 (🎓 Học bổng) sáng rực.
  - **4.2s – 5.0s**: Mốc 05 (🛡️ Tài chính toàn trình) khóa chốt lộ trình, luồng năng lượng chạy dọc toàn tuyến tạo thể thống nhất.
- **final_state (5.0s – 7.0s)**:
  - Cả 5 trụ cột đều rực sáng ổn định trên trục lộ trình dọc.
  - Khối neo `KẾ HOẠCH DÀI HẠN` trồi lên vững chãi ở Y: 940px.
  - Chân trang Y: 1060px – 1280px giữ nguyên **220px** sạch sẽ cho phụ đề nền tảng.
- **asset_contract**:
  - Open-canvas stage với ambient radial light và subtle blueprint grid.
  - SVG Vertical Strategic Roadmap Spine & Circuit Data Bus.
  - SVG 5 Pillar Physical Tokens (Campus, Target, Vault, Honor, Shield) với số hiệu `01` – `05`.
  - SVG Synthesis Badge (`KẾ HOẠCH DÀI HẠN`).
  - Audio: `scratch/scene_14_audio.wav` (7.00s).
- **hf_signature_motion**: Sequential Pathway Activation & Strategy Lock (Kích hoạt tuần tự 5 mốc dọc theo con đường quy hoạch và khóa toàn bộ lộ trình bằng dòng năng lượng hoàng kim).
- **hf_supporting_motion**: Accent sweep dưới headline + ánh sáng mạch điện chạy dọc dải cung.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1050px.
- **handoff**: none
- **occlusion_order**: Background (z: 1) → Ground Grid (z: 10) → Strategic Pathway (z: 15) → Circuit Traces (z: 20) → 5 Pillar Tokens (z: 30) → Synthesis Badge (z: 40) → Headline (z: 50).
- **transition_in**: Clean physical entrance.
- **transition_out**: Stable final hold (5.5s – 7.0s) chuẩn bị dẫn vào Scene 15.

---

## Scene 15: Tiêu Chuẩn Cốt Lõi — Cán Cân Hài Hòa Tài Chính & Dài Hạn

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 15
- **timeline**: 93.6s – 102.6s (Duration: 9.00s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Phân cảnh xác lập tiêu chuẩn cốt lõi của một hồ sơ du học bền vững: đối chiếu trực quan giữa quan niệm thiển cận "chỉ cần đủ điều kiện tối thiểu để nộp" và tiêu chuẩn thực sự của ESORA "phù hợp năng lực tài chính & kế hoạch dài hạn của gia đình". Cần chuyển động đối trọng chính xác (Precision Dual Balance Scale / Equilibrium Calibration), nâng tầm bộ hồ sơ từ mức cơ học thành trạng thái cân bằng chiến lược toàn diện. Đòi hỏi vector precision timing 9.00s, độ tương phản chuẩn WCAG AA và bảo toàn nhận diện thương hiệu ESORA.
- **visual_verb**: BALANCE & HARMONIZE (Cân bằng năng lực tài chính gia đình và kế hoạch chiến lược dài hạn trên cán cân chuẩn xác).
- **visible_text_budget**: 
  - Headline: `TIÊU CHUẨN HỒ SƠ TỐT` (4 từ).
  - Khối neo trạng thái kết thúc: `PHÙ HỢP DÀI HẠN` (4 từ).
  - Tổng số từ ở final hold: 8 từ (<= 10 từ).
  - Không có phụ đề transcript lặp lại narration, không dùng card/box bọc text.
- **visible_text_inventory**:
  - `core_phrase`: `TIÊU CHUẨN HỒ SƠ TỐT` (Headline)
  - `necessary_label`: `PHÙ HỢP DÀI HẠN` (Status synthesis anchor)
  - `diegetic_text`: `ESORA • DU HỌC CANADA` (Brand mark)
  - `remove`: Loại bỏ toàn bộ các câu giải thích phụ trợ ("Không chỉ đủ điều kiện để nộp", "Phù hợp khả năng tài chính") để bảo toàn text economy.
- **container_required**: `false` (Bố cục 100% open-canvas, cán cân chiến lược đặt trực tiếp trong không gian mở, không bọc card hay text box).
- **container_semantics**: `none`
- **narrative_visual**: Chiếm 65% diện tích khung hình khả dụng (Y: 200px đến 1050px):
  1. Tập Hồ sơ Du học Danh giá (Master Dossier) xuất hiện ở đỉnh trung tâm.
  2. Cán cân Đối trọng Chiến lược Hoàng kim (Strategic Precision Balance Scale):
     - Trục cân thẳng đứng bằng thép Deep Navy `#0F172A` vững chãi.
     - Đòn cân kim loại vàng óng `#FDE047` và cam `#FF6B2B`.
     - Đĩa cân Trái (X: 180px, Y: 480px): Khối biểu trưng Năng lực Tài chính (Biểu tượng rương tài chính vàng + các đồng xu tích lũy).
     - Đĩa cân Phải (X: 540px, Y: 480px): Khối biểu trưng Kế hoạch Dài hạn (Biểu tượng la bàn định hướng tương lai + cây lộ trình phát triển).
  3. Cơ chế Cân bằng Động (Equilibrium Calibration):
     - Ban đầu đòn cân nghiêng nhẹ tượng trưng cho sự lệch pha truyền thống (chỉ chú trọng nộp đơn mà xem nhẹ dài hạn).
     - Khi lời thoại đến *"phù hợp với khả năng tài chính và kế hoạch dài hạn"*, hai đĩa cân tiếp nhận trọng lượng chiến lược, đòn cân dao động êm dịu và khóa ngang ở trạng thái cân bằng hoàn hảo (Perfect Equilibrium).
     - Tia hào quang xanh ngọc/vàng óng lóe sáng từ tâm chốt khóa (Fulcrum Lock).
  4. Khối neo bảo chứng: `PHÙ HỢP DÀI HẠN` với huy hiệu bảo chứng chuẩn mực.
- **opening_state (0.0s – 2.0s)**:
  - Lời thoại: *"Bởi một hồ sơ du học tốt..."*
  - Top branding `ESORA • DU HỌC CANADA` và Headline `TIÊU CHUẨN HỒ SƠ TỐT` xuất hiện open-canvas.
  - Cán cân đối trọng xuất hiện cùng tập hồ sơ ở đỉnh chỉ huy.
- **transformation (2.0s – 6.5s)**:
  - Lời thoại: *"...không chỉ là đủ điều kiện để nộp, mà còn phải phù hợp với khả năng tài chính và kế hoạch dài hạn của gia đình."*
  - **2.0s – 3.5s**: Dấu tick cơ học `ĐỦ ĐIỀU KIỆN` xuất hiện nhưng đòn cân vẫn chưa cân bằng (báo hiệu tính chất chưa bền vững nếu chỉ dừng ở bước này).
  - **3.5s – 5.2s**: Hai khối giá trị cốt lõi (Tài chính Gia đình & Kế hoạch Dài hạn) lần lượt đặt lên hai đĩa cân.
  - **5.2s – 6.5s**: Đòn cân dao động nhịp nhàng và khóa chặt ở vị trí cân bằng ngang 180° hoàn mỹ (Equilibrium Lock) với vòng sóng năng lượng vàng `#FDE047`.
- **final_state (6.5s – 9.0s)**:
  - Cán cân giữ vững thế cân bằng chiến lược tuyệt đối.
  - Khối neo `PHÙ HỢP DÀI HẠN` xuất hiện vững chãi bên dưới.
  - Chân trang Y: 1060px – 1280px giữ nguyên **220px** sạch sẽ cho phụ đề nền tảng.
- **asset_contract**:
  - Open-canvas stage với ambient radial light và subtle blueprint grid.
  - SVG Master Dossier Folder with Golden Seal.
  - SVG Strategic Precision Balance Scale (Fulcrum, Beam, 2 Weighing Pans).
  - SVG Left Weight (Financial Capacity Vault & Coins).
  - SVG Right Weight (Strategic Horizon Compass & Milestone Node).
  - SVG Synthesis Badge (`PHÙ HỢP DÀI HẠN`).
  - Audio: `scratch/scene_15_audio.wav` (9.00s).
- **hf_signature_motion**: Dynamic Balance Calibration & Equilibrium Lock (Cán cân dao động cơ học và khóa thẳng thớm ở vị trí cân bằng hoàn hảo giữa tài chính và lộ trình tương lai).
- **hf_supporting_motion**: Accent sweep dưới headline + ánh sáng hào quang tỏa ra từ chốt cân bằng tâm (Fulcrum jewel).
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1050px.
- **handoff**: none
- **occlusion_order**: Background (z: 1) → Ground Line (z: 10) → Scale Stand (z: 15) → Balance Beam & Pans (z: 25) → Dossier & Weights (z: 30) → Synthesis Badge (z: 40) → Headline (z: 50).
- **transition_in**: Clean physical entrance.
- **transition_out**: Stable final hold (7.5s – 9.0s) chuẩn bị dẫn vào Scene 16 (kêu gọi hành động: liên hệ ESORA để được tư vấn lộ trình phù hợp).

---

## Scene 16: Kêu Gọi Hành Động — Kết Nối Tư Vấn Chiến Lược Cùng ESORA

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 16
- **timeline**: 102.6s – 108.6s (Duration: 6.00s)
- **render_mode**: `HF_ONLY`
- **routing_reason**: Phân cảnh Call to Action (CTA) chiến lược: kết nối gia đình và học sinh với đội ngũ chuyên gia tư vấn lộ trình 1:1 của ESORA. Chuyển động đối thoại trực quan (Consultation Bridge & Strategic Blueprint Handover) giữa đại diện gia đình và bàn tư vấn chuyên gia ESORA, mở khóa bộ hồ sơ quy hoạch may đo riêng. Đòi hỏi vector precision timing 6.00s, độ tương phản chuẩn WCAG AA và bảo toàn nhận diện thương hiệu ESORA.
- **visual_verb**: CONNECT & ADVISE (Kết nối gia đình học sinh với bàn tư vấn chuyên gia ESORA, mở khóa lộ trình chiến lược cá nhân hóa).
- **visible_text_budget**: 
  - Headline: `TƯ VẤN LỘ TRÌNH ESORA` (4 từ).
  - Khối neo trạng thái kết thúc: `KẾT NỐI CHUYÊN GIA` (4 từ).
  - Tổng số từ ở final hold: 8 từ (<= 10 từ).
  - Không có phụ đề transcript lặp lại narration, không dùng card/box bọc text.
- **visible_text_inventory**:
  - `core_phrase`: `TƯ VẤN LỘ TRÌNH ESORA` (Headline)
  - `necessary_label`: `KẾT NỐI CHUYÊN GIA` (Status synthesis anchor)
  - `diegetic_text`: `ESORA • DU HỌC CANADA` (Brand mark)
  - `remove`: Loại bỏ toàn bộ các câu giải thích phụ trợ ("Nếu gia đình đang chuẩn bị cho con", "Hãy liên hệ Esora") để bảo toàn text economy.
- **container_required**: `false`
- **container_semantics**: `none`
- **container_inventory**: []
- **boundary_removal_test**: "Tuyệt đối không dùng 2 profile card đối xứng hay avatar nhốt trong vòng tròn bo góc. Gia đình và Chuyên viên là hai cụm nhân vật vector cutout lớn đứng tự nhiên trên sàn không gian (open-canvas). Ở giữa là tập hồ sơ may đo chiến lược được mở khóa và tương tác thực tế."
- **vertical_occupancy_plan**: "Nhân vật chiếm trọn vẹn chiều cao từ Y: 360px đến Y: 880px; bàn tư vấn và hồ sơ lộ trình chiếm trung tâm Y: 440px - 700px; bên dưới là synthesis badge tại Y: 940px, lấp đầy 70% không gian sử dụng và giữ sạch 220px footer."
- **narrative_visual**: Chiếm 70% diện tích khung hình khả dụng (Y: 200px đến 1050px):
  1. Cánh trái (X: 40px – 310px, Y: 380px – 860px): Cụm nhân vật Gia đình & Học sinh (Cha mẹ và con mặc áo cam ESORA, tầm vóc lớn, biểu cảm ấm áp).
  2. Cánh phải (X: 410px – 680px, Y: 380px – 860px): Chuyên gia Tư vấn Lộ trình ESORA chuyên nghiệp bên bàn làm việc cùng laptop và tài liệu.
  3. Không gian Tương tác & Hồ sơ Chiến lược May đo 1:1 (Center Handover Zone, Y: 460px – 720px):
     - Mạch nối dữ liệu phát quang nối giữa hai phía.
     - Bộ Hồ sơ Lộ trình May đo (Personalized Strategic Blueprint) mở bung ngôi sao định hướng và đồ thị tương lai.
  4. Khối neo bảo chứng: `KẾT NỐI CHUYÊN GIA` tại Y: 940px.
- **opening_state (0.0s – 1.8s)**:
  - Lời thoại: *"Nếu gia đình đang chuẩn bị cho con du học Canada..."*
  - Top branding `ESORA • DU HỌC CANADA` và Headline `TƯ VẤN LỘ TRÌNH ESORA` xuất hiện open-canvas.
  - Gia đình và Chuyên gia xuất hiện ở hai cánh sân khấu trên đường sàn cơ sở, hướng về nhau.
- **transformation (1.8s – 4.2s)**:
  - Lời thoại: *"...hãy liên hệ Esora để được tư vấn lộ trình phù hợp."*
  - **1.8s – 3.0s**: Mạch quang học vàng/cam kết nối từ Chuyên gia sang Gia đình.
  - **3.0s – 4.2s**: Tập hồ sơ chiến lược 1:1 mở nắp phát quang ánh sáng vàng `#FDE047` cùng ngôi sao dẫn đường đa giác, gia đình tươi cười đón nhận.
- **final_state (4.2s – 6.0s)**:
  - Giao điểm kết nối hoàn tất, ánh hào quang tỏa sáng thể hiện sự an tâm, đồng lòng.
  - Khối neo `KẾT NỐI CHUYÊN GIA` xuất hiện vững chãi ở Y: 940px.
  - Chân trang Y: 1060px – 1280px giữ nguyên **220px** sạch sẽ cho phụ đề nền tảng.
- **asset_contract**:
  - Open-canvas stage với ambient radial light và subtle blueprint grid.
  - SVG Large Family & Student Cutout Rig (cha mẹ và học sinh tầm vóc lớn).
  - SVG ESORA Advisor Desk & Consultant Cutout Rig.
  - SVG Tailored Strategic Roadmap Dossier.
  - SVG Synthesis Badge (`KẾT NỐI CHUYÊN GIA`).
  - Audio: `scratch/scene_16_audio.wav` (6.00s).
- **hf_signature_motion**: Consultation Connection Arc & Tailored Roadmap Unlock (Kết nối mạch quang học hai bên, trao gửi và mở khóa lộ trình chiến lược cá nhân hóa).
- **hf_supporting_motion**: Accent sweep dưới headline + pulse hào quang vàng tại hồ sơ trung tâm.
- **flow_action**: none
- **flow_camera**: none
- **overlay_zone**: Toàn bộ canvas từ Y: 140px đến 1050px.
- **handoff**: none
- **occlusion_order**: Background (z: 1) → Ground Line (z: 10) → Consultation Arc (z: 15) → Characters & Desk (z: 25) → Central Dossier (z: 35) → Synthesis Badge (z: 40) → Headline (z: 50).
- **transition_in**: Clean physical entrance.
- **transition_out**: Stable final hold (4.8s – 6.0s) chuẩn bị dẫn vào Scene 17 (kết bài: chuẩn bị sớm, tính đúng từ đầu).

---

## Scene 17: Kết Luận & Khẳng Định Thương Hiệu — Chủ Động Vững Vàng Hành Trình

### 1. Mandatory Schema & Hard Gate Declaration

- **scene_number**: 17 (Final Scene)
- **timeline**: 108.6s – 114.6s (Duration: 6.00s)
- **render_mode**: `HYBRID`
- **routing_reason**: Phân cảnh tổng kết toàn bộ video explainer kết hợp hoàn hảo giữa cảnh quay điện ảnh hữu cơ của Flow (Veo plate: du học sinh Việt Nam tự tin, rạng rỡ sải bước trong khuôn viên đại học Canada ngập nắng mùa thu) và lớp đồ họa chính xác của HyperFrames (Top branding ESORA, kinetic headline "TÍNH ĐÚNG TỪ ĐẦU", huy hiệu định vị "AN TÂM DU HỌC"). Sự kết hợp này mang lại cảm xúc truyền cảm hứng chân thực từ con người thực tế song hành cùng sự sắc nét, chuẩn xác và uy tín của thương hiệu ESORA.
- **visual_verb**: STRIDE & EMPOWER (Du học sinh sải bước tự tin trên campus Canada dưới sự bảo trợ chiến lược vững vàng của ESORA).
- **visible_text_budget**: 
  - Headline: `TÍNH ĐÚNG TỪ ĐẦU` (4 từ).
  - Khối neo trạng thái kết thúc: `AN TÂM DU HỌC` (4 từ).
  - Top mark: `ESORA • DU HỌC CANADA` (chuẩn chính tả thương hiệu ESORA).
  - Tổng số từ ở final hold: 8 từ (<= 10 từ).
  - Không có phụ đề transcript lặp lại narration, không dùng card/box bọc text thô kệch.
- **visible_text_inventory**:
  - `core_phrase`: `TÍNH ĐÚNG TỪ ĐẦU` (Headline)
  - `necessary_label`: `AN TÂM DU HỌC` (Status synthesis anchor badge)
  - `diegetic_text`: `ESORA • DU HỌC CANADA` (Brand mark)
  - `remove`: Loại bỏ toàn bộ các câu giải thích phụ trợ ("Chuẩn bị sớm để không bị động", "Trước những thay đổi chính sách") để bảo toàn text economy.
- **container_required**: `false` (Headline bố cục open-canvas trên vùng negative space của nền trời và campus; chỉ có anchor badge dạng pill gọn gàng ở nhịp kết để neo nhận thức).
- **container_semantics**: `none`
- **narrative_visual**: 
  1. Living Background Video (Veo plate 720x1280): Du học sinh Việt Nam tự tin, rạng rỡ khoác balo, cầm tập hồ sơ du học bước đi trên sân trường đại học Canada giữa tán cây phong mùa thu và kiến trúc kính hiện đại.
  2. Bố cục lớp phủ âm bản (Atmospheric Negative Space): Tận dụng khoảng trời thoáng đãng ở nửa trên khung hình để đặt đồ họa, đảm bảo độ tương phản WCAG AA tuyệt đối.
  3. Lớp đồ họa HyperFrames:
     - Top brand badge: `ESORA • DU HỌC CANADA` (Navy `#0F172A`, viền trắng, chữ trắng, dot cam `#FF6B2B`).
     - Kinetic Headline: `TÍNH ĐÚNG TỪ ĐẦU` (chữ trắng `#FFFFFF` sắc nét với vệt gạch chân hoàng kim `#FDE047` và đổ bóng mềm bảo toàn tính tương phản).
     - Biểu tượng ngôi sao định hướng 8 cánh & Anchor Badge `✦ AN TÂM DU HỌC` khóa nhịp kết thúc tại t=3.8s.
- **opening_state (0.0s – 1.8s)**:
  - Lời thoại: *"Chuẩn bị sớm, tính đúng từ đầu..."*
  - Nền video chuyển động: Du học sinh bước đi với nụ cười rạng rỡ trong khuôn viên rực nắng.
  - Top branding `ESORA • DU HỌC CANADA` đáp nhẹ tại Y: 55px.
  - Headline open-canvas `TÍNH ĐÚNG TỪ ĐẦU` xuất hiện mạnh mẽ, gạch chân vàng `#FDE047` bung nở.
- **transformation (1.8s – 3.8s)**:
  - Lời thoại: *"...để hành trình du học không bị động vì những thay đổi chính sách."*
  - Máy quay dolly mượt mà theo bước chân du học sinh.
  - Ngôi sao dẫn đường hoàng kim 8 cánh (`#FDE047`) xuất hiện và xoay nhẹ, mở ra luồng sáng bảo chứng.
  - Huy hiệu kết `✦ AN TÂM DU HỌC` khóa chắc chắn vào vị trí trung tâm phía trên đầu nhân vật.
- **final_state (3.8s – 6.0s)**:
  - Triumphant Hold: Cảnh quay campus và du học sinh ngập tràn ánh nắng và sự tự tin.
  - Headline và huy hiệu tỏa sáng rõ nét, thể hiện thông điệp uy tín, an tâm trọn vẹn.
  - Chân trang Y: 1080px – 1280px giữ nguyên **200px** sạch sẽ cho phụ đề nền tảng.
- **asset_contract**:
  - Background Video: `assets/bg.mp4` (Veo cinematic plate: `f1ab8df3-2e6b-44af-a79d-50e2bff6e9e6`, 720x1280 @ 24fps).
  - Voice Audio: `assets/audio.wav` (6.00s, `scratch/scene_17_audio.wav`).
  - Overlay layers: Brand badge, Headline typography, Star emblem, Anchor badge.
- **hf_signature_motion**: Organic Campus Dolly Sync + Cinematic Typography & Compass Star Lock (Đồng bộ bước chân du học sinh với nhịp xuất hiện uy nghi của thông điệp chiến lược).
- **hf_supporting_motion**: Vệt gạch chân hoàng kim `#FDE047` bung mở + hiệu ứng phát quang subtle glow của ngôi sao la bàn.
- **flow_action**: A confident, radiant young Vietnamese university student smiling and walking forward on a sunlit Canadian university campus in autumn, holding a study folder.
- **flow_camera**: Smooth cinematic tracking dolly following the student's forward walk, wide-angle lens with natural golden morning light.
- **overlay_zone**: Nửa trên khung hình (Y: 55px đến 420px).
- **handoff**: Flow cung cấp video plate điện ảnh; HyperFrames căn chỉnh typography vào vùng negative space của bầu trời và tòa nhà kính.
- **occlusion_order**: Veo Video Plate (z: 1) → Top Atmospheric Contrast Gradient (z: 5) → Brand Mark (z: 20) → Headline (z: 30) → Guiding Star & Anchor Badge (z: 40).
- **transition_in**: Smooth cinematic cut.
- **transition_out**: Grand finale triumphant hold (4.2s – 6.0s) khép lại trọn vẹn toàn bộ 17 phân cảnh của dự án.




