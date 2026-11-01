# 10 · Mentor giúp Nhật làm rõ lựa chọn

**Voice gốc:** Với sự đồng hành của đội ngũ Mentor Esora hơn 14 năm kinh nghiệm,

**Thời lượng:** 3.486125000s · sample 903862–987529 · audio `inputs/audio/scene_10.wav`.

**Ý cần đọc được:** Thể hiện đồng hành bằng góp ý cụ thể, Nhật vẫn là tác giả và người quyết định.

**Dàn khung:** Góc chéo qua bàn: Nhật trái x180–335/y650–1000; mentor phải x430–580/y625–1000; một trang lớn chung x210–510/y500–770. Mentor dáng gọn màu xanh lục nhạt, kính tròn, tỉ lệ cùng thế giới Nhật; không giống người thật cụ thể.

**Mở cảnh:** Trang nháp từ09 nằm giữa hai người. Mentor dùng đầu bút chỉ một đoạn trên chính trang.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.750s|Với sự đồng hành|Mentor nghiêng người xem trang, Nhật nhìn theo đầu bút.|
|0.75–2.000s|đội ngũ Mentor Esora|Mentor khoanh gọn một đoạn cần làm rõ, rồi đưa lại bút; nhãn MENTOR ESORA đặt gần nhân vật mentor, không có nét nối.|
|2.00–3.000s|hơn14năm kinh nghiệm|Nhật tự viết lại đoạn ấy bằng bút cam, mentor quan sát và gật đầu. Không hiển thị số14 hoặc huy hiệu kinh nghiệm.|
|3.00–3.486s|kết câu|Giữ trang có một điểm sửa rõ; Nhật kéo trang về phía mình để đưa vào hồ sơ11.|

**Chốt:** Trang sửa tốt hơn nhưng nét viết vẫn thuộc Nhật; mentor không viết hộ toàn bài.

**Nhân vật:** Hai vai rõ: mentor chỉ/góp ý; Nhật chỉnh sửa và sở hữu trang.

**Chữ trên hình:** MENTOR ESORA. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `mentor` — **to_draw**. Mentor riêng biệt nhưng cùng tỉ lệ mascot: thân nhỏ xanh lục nhạt #91B59F, kính tròn, tay áo kem; không cap/ba lô của Nhật. Chỉ xem trang, chỉ/góp ý và giữ kẹp; không thêm hành động thắng cúp. Tách: body, glasses/head, far arm, near arm, contact hands, nod pose. Nguồn: original symbolic adviser, not real person likeness.
- `work_desk` — **to_draw**. Bàn09/10/15 cùng màu gỗ sáng, đèn phía trái, ngăn giấy cạnh phải. Có wide room, chéo qua bàn, close tay dùng chung asset. Tách: back desk edge, surface, front edge for hand occlusion, lamp. Nguồn: reuse scene01 desk language without cloning whole composition.
- `draft_pages` — **to_draw**. Một tờ nháp có dấu cam và hai bản cũ. Các nét dòng là texture giấy, không tạo chữ nhỏ đọc được hay paragraph mô tả; vị trí một đoạn sửa được khoanh bằng bút rồi viết lại. Tách: current page, old drafts, circle/correction ink, new orange strokes. Nguồn: original illustrative writing, no actual application content.
- `pen_pair` — **to_draw**. Bút góp ý màu đất đỏ và bút cam của Nhật; đổi tay sau khi mentor góp ý, không để bút dịch mà bàn tay không nắm. Tách: two pens, grip overlays. Nguồn: one signature correction on real paper, not label pointers.

**Nối sang cảnh sau:** 11 chuyển overhead ngay khi Nhật kéo trang; dùng đúng tờ giấy ấy, không mở một bộ hồ sơ từ đầu khác.

**Vì sao HF_ONLY:** Hai nét bút/động tác trên cùng mặt giấy diễn đạt quyền tác giả và hỗ trợ, cần các lớp minh hoạ phối hợp. HYBRID cuộc tư vấn diễn viên có thể bị nhận là cuộc gặp thật chưa được cung cấp; không cần organic actor performance.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.

**Cần kiểm chứng trước công bố:** voice nói Mentor hơn14năm. Nguồn Esora hiện ghi tổ chức hơn13năm, chưa chứng minh trải nghiệm đội Mentor. Vẫn giữ nguyên voice cho workprint riêng; không làm số14/huy hiệu trên hình và không tự sửa audio. Xem RESEARCH.md.
