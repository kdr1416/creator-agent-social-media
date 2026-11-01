# 05 · Từ phong thư tới môi trường học thuật

**Voice gốc:** Một trong những trường đại học nghiên cứu hàng đầu Hà Lan và châu Âu,

**Thời lượng:** 3.220708333s · sample 442731–520028 · audio `inputs/audio/scene_05.wav`.

**Ý cần đọc được:** Cho VU một không gian cụ thể, tránh dựng thành tích xếp hạng chưa kiểm chứng.

**Dàn khung:** Ảnh campus VU bắt đầu tại đúng vị trí cuối04, tiến tới x104–616/y383–946; vỏ kiến trúc giấy của06 xuất hiện quanh mép trong đoạn chốt.

**Mở cảnh:** Giữ ảnh VU vừa nhô khỏi phong bì ở04; không chèn một title card mới.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.750s|Một trong những trường|Máy bám ảnh campus, phong bì hạ khỏi đáy sân khấu; dải tên trường được giữ để đọc.|
|0.75–2.250s|đại học nghiên cứu hàng đầu|Ảnh đứng lại như một tờ ảnh lớn. Hai chi tiết đời sống học thuật ở mép dưới: sách mở và một mặt bàn thí nghiệm trong cùng bối cảnh, không phải hai icon nổi.|
|2.25–3.221s|Hà Lan và châu Âu|Mép khung ảnh trở thành vỏ mô hình campus; chốt hình theo frame đầu06. Chi tiết sách/bàn ra ngoài crop.|

**Chốt:** Ảnh trên mặt mô hình có tỉ lệ/vị trí như đầu06, sẵn sàng bóc mở mặt cắt.

**Nhân vật:** Không thêm nhân vật: ảnh địa điểm và cấu trúc học thuật cần ưu tiên trong3.22s.

**Chữ trên hình:** VU AMSTERDAM. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.
- `campus_shell` — **available_source_extend_only**. Vỏ mô hình campus có sàn/cột từ06.05 chỉ cần bao quanh ảnh để nối sang06; không tự dựng phòng khác trong pilot. Tách: roof, side walls, floors, columns, photo cover. Nguồn: reference_pilots/scene_06/index.html #c6-drawing and #c6-photo.
- `research_props` — **to_draw**. Mép một cuốn sách mở và một phần bàn thí nghiệm làm tiền cảnh môi trường học thuật; không xếp huy chương hoặc icon danh hiệu. Tách: book paper/leaves, bench edge, one glass silhouette. Nguồn: consistent line weight with scene06 workspaces.

**Nối sang cảnh sau:** Cắt sang đầu pilot06 khi cùng mặt ảnh/vỏ kiến trúc. 06 tự thực hiện phần mở mặt cắt.

**Vì sao HF_ONLY:** Biến đổi ảnh cắt thành mô hình lớp giấy mang ý chính. HYBRID campus moving footage không hỗ trợ phép chuyển từ địa điểm sang cấu trúc lĩnh vực ở06; live motion sẽ chỉ thành wallpaper.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
