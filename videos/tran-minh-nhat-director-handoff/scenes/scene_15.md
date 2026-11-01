# 15 · Hoàn tất cùng người đồng hành

**Voice gốc:** Đó cũng chính là điều Esora đã đồng hành cùng Minh Nhật trong suốt hành trình ứng tuyển.

**Thời lượng:** 4.417291667s · sample 1342447–1448462 · audio `inputs/audio/scene_15.wav`.

**Ý cần đọc được:** Chốt vai trò hỗ trợ của Esora, quyền sở hữu câu chuyện vẫn ở Nhật.

**Dàn khung:** Góc bàn gần: bìa hồ sơ x150–565/y540–855; Nhật phải x425–575/y700–1010, mentor trái x145–285/y690–1010. Bàn cùng09/10, không dựng cảnh bắt tay mới.

**Mở cảnh:** Nhật đặt trang hoàn chỉnh từ14 vào bìa; mentor đang giữ một chiếc kẹp mở.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.100s|Đó cũng chính là điều Esora|Mentor giữ kẹp, Nhật đưa tờ cuối vào đúng chỗ, hai bàn tay phối hợp trên cùng đạo cụ.|
|1.10–2.700s|đồng hành cùng Minh Nhật|Nhật tự đóng bìa và gắn nhãn tên mình; mentor buông kẹp sau khi giấy đã chắc.|
|2.70–3.800s|suốt hành trình ứng tuyển|Nhật cầm bộ hồ sơ, mentor bước lùi nửa nhịp; Esora hiện dưới dạng chữ gần mentor, không logo tự chế.|
|3.80–4.417s|kết câu|Nhật mang hồ sơ ra phía phải khung; máy để lại một khoảng nhìn về chương tiếp theo.|

**Chốt:** Nhật cầm sản phẩm của chính mình, mentor ở vai trò hỗ trợ.

**Nhân vật:** Giữ kẹp → đặt giấy → đóng bìa → mentor buông → Nhật mang đi; không mannequin/handshake filler.

**Chữ trên hình:** MINH NHẬT / ESORA. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `mentor` — **to_draw**. Mentor riêng biệt nhưng cùng tỉ lệ mascot: thân nhỏ xanh lục nhạt #91B59F, kính tròn, tay áo kem; không cap/ba lô của Nhật. Chỉ xem trang, chỉ/góp ý và giữ kẹp; không thêm hành động thắng cúp. Tách: body, glasses/head, far arm, near arm, contact hands, nod pose. Nguồn: original symbolic adviser, not real person likeness.
- `work_desk` — **to_draw**. Bàn09/10/15 cùng màu gỗ sáng, đèn phía trái, ngăn giấy cạnh phải. Có wide room, chéo qua bàn, close tay dùng chung asset. Tách: back desk edge, surface, front edge for hand occlusion, lamp. Nguồn: reuse scene01 desk language without cloning whole composition.
- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.
- `binder_clip` — **to_draw**. Kẹp giấy đủ lớn để thấy hai tay giữ/luồn/nhả, tỉ lệ với hồ sơ. Tách: clip back, moving jaws, foreground hinge. Nguồn: new vector physical prop.

**Nối sang cảnh sau:** 16 dùng một page-turn của hồ sơ ở mép khung để mở minh hoạ Hà Lan; không thêm chuyến bay/hộ chiếu chưa có trong voice.

**Vì sao HF_ONLY:** Hành động ghép giấy/kẹp phối hợp và chuyển chủ thể sở hữu là semantic choreography trong thế giới giấy đã thống nhất. HYBRID handshake không diễn tả quyền tác giả, footage gặp mặt cũng chưa được cung cấp.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
