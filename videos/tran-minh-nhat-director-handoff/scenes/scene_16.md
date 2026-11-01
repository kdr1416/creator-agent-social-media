# 16 · Chương mới được chúc mở ra

**Voice gốc:** Chúc Minh Nhật sẽ có một hành trình thật rực rỡ tại Hà Lan,

**Thời lượng:** 3.082500000s · sample 1448462–1522442 · audio `inputs/audio/scene_16.wav`.

**Ý cần đọc được:** Lời chúc cho hành trình Hà Lan, không khẳng định Nhật đã nhập cảnh hay tốt nghiệp.

**Dàn khung:** Wide cảnh kênh đào minh hoạ: cầu x80–650/y730–940; nước y840–1060; dãy mái nhà xa x100–630/y380–680. Nhật trên cầu x340–475/y700–980; một mép trang giấy còn thấy ở góc để rõ đây là chương mở.

**Mở cảnh:** Mép hồ sơ lật khỏi15; mặt sau trang là một phố kênh đào vẽ tay, không copy ảnh thành phố làm plate.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.700s|Chúc Minh Nhật|Trang mở, Nhật bước vào nhịp đầu trên cầu; tạm không có headline.|
|0.70–2.000s|hành trình thật rực rỡ|Nhật đeo ba lô và nhìn qua cầu; ánh nền mở sáng hơn, mặt nước gợn nhẹ, không pháo hoa hay cúp.|
|2.00–3.083s|tại Hà Lan|Nhật quay chào rồi hướng lại về phía trước; CHƯƠNG MỚI hiện ngắn trên vùng trời.|

**Chốt:** Đường phố thật trong tranh tiếp diễn về phía phải; Nhật sẵn sàng bước tiếp.

**Nhân vật:** Bước vào bối cảnh, nhìn và chào, sau đó quay lại phía trước; không đứng góc filler.

**Chữ trên hình:** CHƯƠNG MỚI. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_walk` — **to_extend_reference_rig**. Cùng mascot, stride2–3 tư thế và quay chào; bước chân có tiếp đất, tay giữ sổ khi đi. Tách: hips/body, alternating legs, free arm, book arm, head turn. Nguồn: library/student.js.
- `canal_scene` — **to_draw**. Phố Hà Lan minh hoạ, cầu thấp qua kênh, ba mái nhà gable, cửa sổ và nước. Không lấy landmark làm campus VU hoặc diễn tả đã tới địa điểm thực. Tách: far roofs, near facades, water, far bridge, bridge walking plane, near rail, page edge reveal. Nguồn: generic illustrated Dutch canal setting, no specific named landmark.
- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.

**Nối sang cảnh sau:** 17 tiếp đúng bước chân/không gian, không reset nhân vật về đầu cầu hoặc đổi trang phục.

**Vì sao HF_ONLY:** Trang giấy mở thành môi trường khát vọng là lời chúc được minh hoạ. HYBRID footage diễn viên ở Hà Lan dễ bị đọc thành chuyến đi đã xảy ra; lớp giấy là nội dung chứ không chỉ lớp trang trí.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
