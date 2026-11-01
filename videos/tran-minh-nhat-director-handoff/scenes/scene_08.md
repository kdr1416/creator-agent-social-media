# 08 · Cơ hội là các lựa chọn mở

**Voice gốc:** mở ra nhiều cơ hội học tập và nghề nghiệp trên toàn cầu.

**Thời lượng:** 3.113000000s · sample 747452–822164 · audio `inputs/audio/scene_08.wav`.

**Ý cần đọc được:** Thể hiện phạm vi toàn cầu và hai hướng học tập/nghề nghiệp mà không đảm bảo kết quả.

**Dàn khung:** Globe giấy x140–585/y390–870; không gian học nhóm nhỏ nhô phía trên trái x110–315/y360–550; bàn làm việc phía phải x430–625/y565–760; Nhật ở tiền cảnh x385–540/y815–1010.

**Mở cảnh:** Nhật nhìn một địa cầu giấy, các lục địa là mảng sáng có nét viền mảnh.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.800s|mở ra nhiều cơ hội|Nhật đẩy địa cầu xoay một góc nhỏ; không chạy máy bay qua các điểm.|
|0.80–2.000s|học tập và nghề nghiệp|Một cảnh bàn học nhóm và một cảnh bàn làm việc mở lên từ bề mặt địa cầu, hai lựa chọn ngang hàng, không nối mũi tên nhân quả.|
|2.00–3.113s|trên toàn cầu|Nhật nhìn lần lượt hai hướng và giữ cả hai hiện diện; chỉ một headline ngắn nếu đọc đủ.|

**Chốt:** Hai khả năng cùng mở trên một thế giới, nhân vật chưa chọn kết quả.

**Nhân vật:** Xoay globe và quan sát lựa chọn; không đứng chỉ trang trí.

**Chữ trên hình:** CƠ HỘI RỘNG MỞ. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `paper_globe` — **to_draw**. Địa cầu giấy có trục, lục địa đơn giản tương đối đúng; mở hai bối cảnh ngang hàng từ mặt cầu. Tách: sphere, continents clipping group, axis/base, foreground rim. Nguồn: original vector geometry; no country data or flight paths.
- `opportunity_settings` — **to_draw**. Một bàn học nhóm và một bàn công việc thật trong hình minh hoạ; mỗi nhóm gồm mặt bàn/ghế/người nhỏ đang làm việc, không icon briefcase/mũ tốt nghiệp đứng rời. Tách: study table setting, work table setting, paper tabs connecting to globe. Nguồn: generic possible settings, no claim of job/visa outcome.

**Nối sang cảnh sau:** Cắt tương phản sang cận ảnh VU trên tường ở09: từ khả năng lớn quay về công việc rất cụ thể.

**Vì sao HF_ONLY:** Địa cầu giấy và hai khả năng cùng nâng từ bề mặt biểu đạt phạm vi/khả năng. HYBRID đi tới điểm đến thật có thể thêm kết quả du học hoặc công việc chưa xảy ra; organic camera không cải thiện quan hệ song song này.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
