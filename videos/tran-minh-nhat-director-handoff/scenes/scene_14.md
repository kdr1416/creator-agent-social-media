# 14 · Kể có trọng tâm để người đọc hiểu mình

**Voice gốc:** Điều quan trọng là biết cách kể câu chuyện đó đúng cách để tạo dấu ấn với hội đồng tuyển sinh.

**Thời lượng:** 4.702750000s · sample 1229581–1342447 · audio `inputs/audio/scene_14.wav`.

**Ý cần đọc được:** Biến chất liệu có sẵn thành câu chuyện có mạch, không dùng dấu đỗ của hội đồng.

**Dàn khung:** Overhead một trang bài luận minh hoạ x125–595/y345–965. Ba chất liệu từ12 (tangram, chân dung, ảnh mục tiêu) đang ở lề/trang nháp; tay Nhật từ góc dưới phải. Dùng dấu in/đoạn nét không đọc được như chất liệu, không paragraph DOM.

**Mở cảnh:** Trang mở có nhiều mảnh cùng tranh sự chú ý, các mảnh thừa ở lề, chưa có trọng tâm.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.050s|Điều quan trọng|Nhật chọn mảnh chính là chân dung có nét riêng và kéo vào đầu trang, các mảnh thừa được đẩy về lề.|
|1.05–2.600s|kể câu chuyện đó đúng cách|Nhật đặt chất liệu chứng minh cách tư duy vào phần giữa, mục tiêu học tập ở phần kết; động tác sắp lại cùng một trang, không bật ba card mới.|
|2.60–3.800s|tạo dấu ấn|Máy chuyển sang góc nhìn trang giấy được nhấc lên: đọc từ đầu đến kết dễ hơn, một khoảng trắng rõ quanh hình chính.|
|3.80–4.703s|hội đồng tuyển sinh|Giữ trang hoàn chỉnh trong tay Nhật, như một câu chuyện sẵn sàng được đọc; không dựng hội đồng giả hoặc con dấu trúng tuyển.|

**Chốt:** Trang có ưu tiên đọc rõ, không phải một poster đầy đủ nhãn; tất cả ý giải thích còn ở voice.

**Nhân vật:** Nhật trực tiếp biên tập và nhấc trang để đọc lại, không để mentor làm thay.

**Chữ trên hình:** KỂ CÓ TRỌNG TÂM. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_hands` — **to_draw_from_reference**. Bàn tay/ống tay của Nhật nhìn overhead; ba tư thế: mở/gấp, giữ giấy, đặt mảnh. Chỉ tay thật của nhân vật, không bàn tay người thật lạc style. Tách: far hand, near hand, contact/grip layer. Nguồn: reference_pilots/scene_12/assets/portrait-v5.js as colour/line reference.
- `essay_page` — **to_draw**. Tờ bài luận minh hoạ với vùng mở đầu/chất liệu/chốt có thể sắp lại; chỉ vài nét in texture. Không paragraph thật, không nội dung bịa vào lời của Nhật. Tách: paper, quiet print strokes, foreground margin, lifted paper pose. Nguồn: physical essay surface, not a general information panel.
- `core_cutouts` — **available_source_extract**. Hình ghép, chân dung đã cá nhân hoá và ảnh VU từ12.14 chỉ lấy mảnh nhỏ làm chất liệu cho cùng một trang; không lặp nguyên bố cục12. Tách: tangram group, portrait group, campus paper photo. Nguồn: reference_pilots/scene_12/index.html #p12-puzzle/#p12-goal-photo and assets/portrait-v5.js.

**Nối sang cảnh sau:** 15 trở lại góc bàn, Nhật hạ chính tờ hoàn chỉnh vào bìa; continuity theo mép giấy và kẹp cam.

**Vì sao HF_ONLY:** Sắp lại phân cấp trên mặt giấy chính là ý kể đúng cách. HYBRID người nói/đọc bài sẽ không cho thấy cấu trúc nội dung thay đổi rõ bằng các lớp ghép.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
