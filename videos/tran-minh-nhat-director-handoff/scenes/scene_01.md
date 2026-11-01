# 01 · Góc học tập mở ra thế giới

**Voice gốc:** Tôi có thể học ở bất kỳ đâu, vì tôi dám khác biệt.

**Thời lượng:** 3.211958333s · sample 0–77087 · audio `inputs/audio/scene_01.wav`.

**Ý cần đọc được:** Đặt tính chủ động và khác biệt làm tinh thần mở đầu; chưa hứa được nhận vào bất kỳ trường nào.

**Dàn khung:** Medium shot căn phòng: cửa sổ x135–610/y350–670; bàn x95–615/y790–955; Nhật x340–480/y685–1000. Không vẽ bản đồ hoặc ba icon ngành.

**Mở cảnh:** Nhật đang học bên một cửa sổ đóng rèm; cuốn sổ xanh và ba lô ở trong tầm tay.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.800s|Tôi có thể học|Nhật ngẩng khỏi sổ; tay rời mép trang để chạm rèm.|
|0.80–2.000s|ở bất kỳ đâu|Nhật kéo rèm, bên ngoài mở thành một góc phố có lớp mái nhà xa gần; chiều sâu của môi trường xuất hiện thay cho màn hình thông tin.|
|2.00–2.700s|vì tôi dám khác biệt|Nhật tự dán một miếng đánh dấu cam lên sổ xanh rồi cầm cuốn sổ lên; headline xuất hiện.|
|2.70–3.212s|khác biệt — kết câu|Giữ một nhịp ánh mắt tự tin và cuốn sổ, cắt trên hành động nâng sổ.|

**Chốt:** Cuốn sổ xanh có dấu cam ở tay Nhật, cửa sổ đã mở.

**Nhân vật:** Đọc → mở rèm → chủ động đánh dấu sổ; không mascot đứng cạnh nền chuyển động.

**Chữ trên hình:** DÁM KHÁC BIỆT. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `room` — **to_draw**. Một góc phòng học lilac sáng, cửa sổ lớn có rèm kéo, đèn nhỏ và một cây;09 thêm dấu vết bản nháp. Không lấp phòng bằng đồ trang trí ngẫu nhiên. Tách: wall/window frame, moving blind, far roofs layers, desk plane, lamp, plant. Nguồn: original vector layers; no room photo needed.
- `notebook` — **to_draw**. Sổ xanh bìa mềm, một dấu cam ở góc và gáy rõ; có bìa đóng/mở, mép trang và clip. Chữ tên chỉ khi scene yêu cầu. Tách: front cover, spine, page block, opening page, orange bookmark. Nguồn: design based on selected blue/orange roles; not the old envelope.

**Nối sang cảnh sau:** 02 tiếp tục đúng cuốn sổ và tay đang nâng, đổi sang góc nhìn giới thiệu; không morph cả căn phòng thành chữ.

**Vì sao HF_ONLY:** Ý chính là khung cửa giấy mở lớp môi trường và dấu cá nhân trên sổ. HYBRID người thật sẽ thay đổi phong cách của chủ thể biểu tượng và không thể hiện lớp giấy mở; organic acting không cần để đọc quan hệ này.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
