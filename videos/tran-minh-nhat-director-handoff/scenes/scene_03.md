# 03 · Điểm đến Hà Lan

**Voice gốc:** vừa chính thức chinh phục thành công một trong những trường đại học nghiên cứu danh tiếng nhất Hà Lan.

**Thời lượng:** 4.839625000s · sample 182085–298236 · audio `inputs/audio/scene_03.wav`.

**Ý cần đọc được:** Cho người xem thấy địa điểm của thành quả, chuẩn bị cho cảnh nhận thư.

**Dàn khung:** Cận mặt bàn. Bản đồ Hà Lan x160–540/y370–810; chấm Amsterdam có nhãn x360–595/y470–535; tay Nhật đi vào từ dưới, không route bay hoặc nhảy qua quốc gia khác.

**Mở cảnh:** Trang mở thành một bản đồ giấy gấp; chưa có tên VU hoặc huy chương.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.100s|vừa chính thức chinh phục thành công|Nhật mở nếp gấp bản đồ bằng hai tay; giấy chiếm phần lớn khung.|
|1.10–2.800s|một trong những trường đại học nghiên cứu|Chấm Amsterdam và một khối campus giấy nhỏ nâng lên tại chấm; chỉ định vị thành phố, không mô phỏng tỉ lệ campus.|
|2.80–4.100s|danh tiếng nhất Hà Lan|Nhãn HÀ LAN được đọc rõ; hai tay gấp bản đồ xuống, một phong bì kem được đặt lên trước.|
|4.10–4.840s|kết câu|Đưa phong bì và Nhật về vùng bố cục mở đầu pilot04; giữ nắp đóng.|

**Chốt:** Phong bì đóng lớn x75–645/y650–950; Nhật về phía phải; không mở thư sớm.

**Nhân vật:** Mở bản đồ rồi đặt phong bì; không cầm cúp, không đưa thêm học bổng.

**Chữ trên hình:** HÀ LAN / Amsterdam. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_hands` — **to_draw_from_reference**. Bàn tay/ống tay của Nhật nhìn overhead; ba tư thế: mở/gấp, giữ giấy, đặt mảnh. Chỉ tay thật của nhân vật, không bàn tay người thật lạc style. Tách: far hand, near hand, contact/grip layer. Nguồn: reference_pilots/scene_12/assets/portrait-v5.js as colour/line reference.
- `netherlands_map` — **to_draw_from_geographic_reference**. Outline Hà Lan trên giấy gấp, chấm Amsterdam ở vùng tây; không bản đồ hàng xóm hoặc đường bay. Dùng outline địa lý kiểm chứng thay đa giác tuỳ ý. Tách: paper folds, land outline, Amsterdam dot, HÀ LAN label, Amsterdam label. Nguồn: official geographic reference to be resolved before drawing; VU official address confirms Amsterdam.
- `envelope` — **available_source**. Phong bì giấy kem có nắp/đáy/mặt trước tách lớp.03 chỉ gấp/đặt,04 mở như nguồn. Tách: back, hinged flap, front, inner paper. Nguồn: reference_pilots/scene_04/index.html #envelope-back/#envelope-flap/#envelope-front.

**Nối sang cảnh sau:** Match cut sang frame đầu pilot04 theo phong bì. Lấy ảnh chụp frame0 của pilot để căn, không sửa pilot04.

**Vì sao HF_ONLY:** Bản đồ giấy gấp và định vị chính xác là nội dung chính; HYBRID map prop thật thêm cảnh quay chứ không giúp đọc điểm đến tốt hơn, còn có nguy cơ chữ tự sinh trên bản đồ.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
