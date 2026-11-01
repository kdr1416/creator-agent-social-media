# 12 · Ba thành phần cốt lõi

**Voice gốc:** mà còn phản ánh rõ tư duy, cá tính và định hướng phát triển của bản thân.

**Thời lượng:** 4.419250000s · sample 1073073–1179135 · audio `inputs/audio/scene_12.wav`.

**Ý cần đọc được:** Hình ghép/Tư duy, tự cá nhân hoá/Cá tính, ảnh mục tiêu trên kế hoạch/Định hướng; không leader lines.

**Dàn khung:** Giữ bố cục nguồn pilot đã đóng băng, không tự thiết kế lại.

**Mở cảnh:** Lấy frame đầu chính nguồn pilot.

**Dùng bản đã có:** `reference_pilots/scene_12/renders/pilot.mp4`. Nguồn: `reference_pilots/scene_12/index.html`.

Không tự dựng lại hình chính. Cảnh trước/sau hấp thụ nối cảnh; chỉ xử lý frame/audio theo kế hoạch kỹ thuật.

Bản04 giữ nội dung/typography của chính pilot đó; default font mới ở các cảnh khác lấy06/12. Không âm thầm reskin04.

**Chốt:** Lấy frame cuối chính nguồn pilot.

**Nhân vật:** Tự đội mũ/đeo ba lô, nhìn và hướng tay vào ảnh mục tiêu.

**Chữ trên hình:** DẤU ẤN RIÊNG / Tư duy / Cá tính / Định hướng / VU Amsterdam. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.
- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `core_cutouts` — **available_source_extract**. Hình ghép, chân dung đã cá nhân hoá và ảnh VU từ12.14 chỉ lấy mảnh nhỏ làm chất liệu cho cùng một trang; không lặp nguyên bố cục12. Tách: tangram group, portrait group, campus paper photo. Nguồn: reference_pilots/scene_12/index.html #p12-puzzle/#p12-goal-photo and assets/portrait-v5.js.
- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.

**Nối sang cảnh sau:** 13 mở rộng sang các sổ vật lý khác; không sửa đuôi12.

**Vì sao HF_ONLY:** Ba lớp tư duy/cá tính/định hướng biểu hiện bằng cấu trúc hình; ẩn dụ giấy mở không phải người đang biểu diễn.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
