# 06 · Nhiều lĩnh vực cùng một campus

**Voice gốc:** nổi tiếng với các lĩnh vực Kinh doanh, Khoa học Dữ liệu, Trí tuệ nhân tạo, Luật và Khoa học Sức khỏe.

**Thời lượng:** 5.192666667s · sample 520028–644652 · audio `inputs/audio/scene_06.wav`.

**Ý cần đọc được:** Mặt cắt kiến trúc mở năm không gian cùng trường; không chuỗi nhân quả.

**Dàn khung:** Giữ bố cục nguồn pilot đã đóng băng, không tự thiết kế lại.

**Mở cảnh:** Lấy frame đầu chính nguồn pilot.

**Dùng bản đã có:** `reference_pilots/scene_06/renders/pilot.mp4`. Nguồn: `reference_pilots/scene_06/index.html`.

Không tự dựng lại hình chính. Cảnh trước/sau hấp thụ nối cảnh; chỉ xử lý frame/audio theo kế hoạch kỹ thuật.

Bản04 giữ nội dung/typography của chính pilot đó; default font mới ở các cảnh khác lấy06/12. Không âm thầm reskin04.

**Chốt:** Lấy frame cuối chính nguồn pilot.

**Nhân vật:** Không nhân vật; tập hợp ngành cần diện tích.

**Chữ trên hình:** VU AMSTERDAM / Kinh doanh / Khoa học dữ liệu / Trí tuệ nhân tạo / Luật / Khoa học sức khoẻ. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `campus_shell` — **available_source_extend_only**. Vỏ mô hình campus có sàn/cột từ06.05 chỉ cần bao quanh ảnh để nối sang06; không tự dựng phòng khác trong pilot. Tách: roof, side walls, floors, columns, photo cover. Nguồn: reference_pilots/scene_06/index.html #c6-drawing and #c6-photo.
- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.

**Nối sang cảnh sau:** 07 hard cut sang cuộn bằng ở bối cảnh học thuật.

**Vì sao HF_ONLY:** Quan hệ tập hợp ngành trong cùng trường cần các lớp đồng hiện; người thật đi qua từng phòng sẽ biến thành hành trình sai nghĩa.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
