# 04 · Phong thư mở ra điểm đến

**Voice gốc:** Xin chúc mừng Minh Nhật đã nhận thư mời nhập học từ: Vrije Universiteit Amsterdam (VU Amsterdam).

**Thời lượng:** 6.020625000s · sample 298236–442731 · audio `inputs/audio/scene_04.wav`.

**Ý cần đọc được:** Phong bì mở, ảnh campus VU xuất hiện và Nhật mừng kết quả.

**Dàn khung:** Giữ bố cục nguồn pilot đã đóng băng, không tự thiết kế lại.

**Mở cảnh:** Lấy frame đầu chính nguồn pilot.

**Dùng bản đã có:** `reference_pilots/scene_04/renders/pilot.mp4`. Nguồn: `reference_pilots/scene_04/index.html`.

Không tự dựng lại hình chính. Cảnh trước/sau hấp thụ nối cảnh; chỉ xử lý frame/audio theo kế hoạch kỹ thuật.

Bản04 giữ nội dung/typography của chính pilot đó; default font mới ở các cảnh khác lấy06/12. Không âm thầm reskin04.

**Chốt:** Lấy frame cuối chính nguồn pilot.

**Nhân vật:** Phản ứng mừng nhận thư.

**Chữ trên hình:** CHÚC MỪNG / MINH NHẬT! / VU AMSTERDAM / THƯ MỜI NHẬP HỌC. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `envelope` — **available_source**. Phong bì giấy kem có nắp/đáy/mặt trước tách lớp.03 chỉ gấp/đặt,04 mở như nguồn. Tách: back, hinged flap, front, inner paper. Nguồn: reference_pilots/scene_04/index.html #envelope-back/#envelope-flap/#envelope-front.
- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.

**Nối sang cảnh sau:** 05 bắt đầu từ đúng ảnh campus và phong bì cuối04.

**Vì sao HF_ONLY:** Cơ chế phong bì/collage là ẩn dụ thành quả; HYBRID mở thư thật dễ gợi bằng chứng tuyển sinh chưa được cung cấp.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.

### Ghi chú assembly04

Nguồn04cũ có #illustration-note; bỏ node đó trong bản phái sinh build/ rồi tái xuất hình, không sửa thiết kế hoặc source frozen. Xem TECHNICAL_HANDOFF.
