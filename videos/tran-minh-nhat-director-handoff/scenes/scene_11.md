# 11 · Thành tích là chất liệu của bộ hồ sơ

**Voice gốc:** Minh Nhật đã xây dựng một bộ hồ sơ không chỉ thể hiện thành tích học tập,

**Thời lượng:** 3.564333333s · sample 987529–1073073 · audio `inputs/audio/scene_11.wav`.

**Ý cần đọc được:** Hồ sơ phải có căn cứ, nhưng chưa đủ để nói hết về con người.

**Dàn khung:** Overhead folder xanh như12: x72–660/y365–1001, mở trang. Tay Nhật từ dưới. Trang nháp ở giữa; hai mảnh giấy học tập là vật liệu ở mép trái, không chữ điểm/số liệu.

**Mở cảnh:** Bìa hồ sơ mở, trang từ10 đang được đặt vào; mép giấy có dấu cam của Nhật.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.900s|Minh Nhật đã xây dựng|Nhật đặt trang đã chỉnh vào bìa và giữ góc để các lớp không rơi.|
|0.90–2.400s|một bộ hồ sơ|Hai mảnh chất liệu học tập được luồn vào cùng trang: ghi chép và một trang hoạt động học tập minh hoạ, không làm giấy chứng nhận giả.|
|2.40–3.564s|không chỉ thể hiện thành tích học tập|Nhật lật một trang, để lộ trang còn lại trống cho cách tư duy/cá tính/mục tiêu; đưa bố cục về đầu12.|

**Chốt:** Căn bố cục bìa xanh/trang trái-phải theo frame0 pilot12; những mảnh bằng chứng đã đi vào trang trước.

**Nhân vật:** Tay đặt giấy, giữ góc và lật trang; có nguyên nhân/tiếp xúc/hệ quả.

**Chữ trên hình:** HỒ SƠ MINH NHẬT. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_hands` — **to_draw_from_reference**. Bàn tay/ống tay của Nhật nhìn overhead; ba tư thế: mở/gấp, giữ giấy, đặt mảnh. Chỉ tay thật của nhân vật, không bàn tay người thật lạc style. Tách: far hand, near hand, contact/grip layer. Nguồn: reference_pilots/scene_12/assets/portrait-v5.js as colour/line reference.
- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.
- `study_evidence` — **to_draw**. Hai giấy vật liệu học tập: trang ghi chép và bản nháp hoạt động học tập với sơ đồ trung tính. Không GPA/chứng chỉ/giải thưởng/tên dự án bịa. Tách: note fragment, learning-work fragment, paper clips. Nguồn: source voice gives only general academic achievements; keep details illustrative.
- `draft_pages` — **to_draw**. Một tờ nháp có dấu cam và hai bản cũ. Các nét dòng là texture giấy, không tạo chữ nhỏ đọc được hay paragraph mô tả; vị trí một đoạn sửa được khoanh bằng bút rồi viết lại. Tách: current page, old drafts, circle/correction ink, new orange strokes. Nguồn: original illustrative writing, no actual application content.

**Nối sang cảnh sau:** Match cut sang pilot12 bảnv6. Không cho hình ghép/nhân vật/ảnh mục tiêu xuất hiện sớm ở11.

**Vì sao HF_ONLY:** Ghép vật liệu giấy thành hồ sơ và lật sang trang cá nhân là quan hệ đồ hoạ. HYBRID tài liệu thật đòi bằng chứng cá nhân chưa có và dễ làm giấy bịa trông xác thực.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
