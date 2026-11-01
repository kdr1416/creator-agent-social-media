# Đánh giá cụm cảnh 01–05 · Trần Minh Nhật

**Mốc hoàn thành:** Dailies cụm 01–05 (0.0s – 21.667s)  
**File xuất khẩu:** `build/renders/tran-minh-nhat-cluster-01-05.mp4`  
**Kích thước & tốc độ khung hình:** 720×1280, 30fps, 650 frames  
**Audio mux:** Trích xuất chính xác 520,028 samples từ `inputs/full_voice.wav` (độ dài 21.6678s, tương quan âm thanh với gốc: 0.999958, 0 clipped samples)

---

## 1. Chi tiết tạo hình và chuyển cảnh từng cảnh

### Cảnh 01: Góc học tập mở ra thế giới (96 frames · 3.200s)
- **Ý nghĩa & hình chủ đạo:** Căn phòng học tone lilac sáng (`#F3EEF7`), cửa sổ lớn có rèm kéo cuốn mở ra góc phố với các lớp mái nhà đầu hồi Hà Lan xa gần; bàn học có đèn bàn, chậu cây xanh và cuốn sổ xanh bìa mềm có gáy rõ.
- **Hành động & Diễn hoạt:**
  - 0.00–0.80s ("Tôi có thể học"): Nhật đang chăm chú học cạnh cửa sổ, tay rời mép trang để chạm rèm.
  - 0.80–2.00s ("ở bất kỳ đâu"): Nhật kéo rèm cuốn lên, mở ra chiều sâu không gian phố phường phía sau; ánh sáng ấm chan hòa.
  - 2.00–2.70s ("vì tôi dám khác biệt"): Miếng đánh dấu cam (`#FF7A30`) được gắn lên góc sổ xanh; Nhật nâng cuốn sổ lên; dải chữ `DÁM KHÁC BIỆT` (Segoe UI Black 900) xuất hiện với độ nảy mềm (`back.out(1.5)`).
  - 2.70–3.20s: Giữ nhịp tự tin, cắt nối trên hành động nâng sổ sang cảnh 02.
- **Tiêu chuẩn:** Không có icon/card generic; footer y:1080–1280 hoàn toàn trống.

### Cảnh 02: Làm quen với Minh Nhật (132 frames · 4.400s)
- **Ý nghĩa & hình chủ đạo:** Giới thiệu danh xưng và bối cảnh xuất phát điểm RMIT Việt Nam gắn với linh vật, không dùng thẻ sinh viên hay ảnh người thật giả mạo.
- **Hành động & Diễn hoạt:**
  - 0.00–0.75s ("Đó cũng là tinh thần"): Cuốn sổ xanh từ 01 hạ xuống mép bàn; máy lùi để Nhật bước ra cạnh sổ.
  - 0.75–2.25s ("Trần Minh Nhật"): Tên hiện 2 nhịp `TRẦN MINH` (52px) và `NHẬT` (64px, `#087BC1`); Nhật quay về phía người xem, tự tin giữ cuốn sổ.
  - 2.25–3.65s ("chàng trai đến từ RMIT Việt Nam"): Ảnh chính thức tòa nhà campus RMIT Nam Sài Gòn xuất hiện như ảnh chụp đính kèm (có viền giấy, bóng đổ và băng keo); nhãn `RMIT VIỆT NAM` gắn liền khối ảnh.
  - 3.65–4.375s ("Việt Nam — kết câu"): Nhật mở bìa sổ, để lộ mép trang giấy chuẩn bị cho bản đồ cảnh 03.

### Cảnh 03: Điểm đến Hà Lan (145 frames · 4.833s)
- **Ý nghĩa & hình chủ đạo:** Bản đồ địa lý Hà Lan trên trang giấy gấp, xác định điểm đến Amsterdam.
- **Hành động & Diễn hoạt:**
  - 0.00–1.10s ("vừa chính thức chinh phục thành công"): Hai bàn tay Nhật (`student_hands` góc nhìn overhead) mở nếp gấp bản đồ giấy ra toàn khung.
  - 1.10–2.80s ("một trong những trường đại học nghiên cứu"): Điểm chấm Amsterdam bung ra kèm mô hình khối nhà đầu hồi/tháp khuôn viên nhỏ; nhãn `Amsterdam` trỏ rõ ràng; dải chữ `HÀ LAN` xuất hiện ở trên.
  - 2.80–4.10s ("danh tiếng nhất Hà Lan"): Hai bàn tay khép bản đồ lại, phong bì giấy kem xuất hiện và trượt vào vị trí trung tâm.
  - 4.10–4.84s: Phong bì và Nhật ổn định tại đúng tọa độ mở đầu của pilot04 (giữ nắp phong bì đóng kín).

### Cảnh 04: Phong thư mở ra điểm đến (180 frames · 6.000s)
- **Bản copy xử lý kỹ thuật từ reference pilot:**
  - Xóa bỏ selector `#illustration-note` ("Hình minh hoạ") theo yêu cầu brief.
  - Loại bỏ audio phát riêng trong composition để ghép voice chuẩn độc lập.
  - Tái xuất đúng 180 frames (6.000s) trên picture grid 30fps.
  - Giữ nguyên toàn bộ staging, diễn hoạt mascot, thư mời, ảnh campus và pháo giấy ăn mừng.

### Cảnh 05: Từ phong thư tới môi trường học thuật (97 frames · 3.233s)
- **Ý nghĩa & hình chủ đạo:** Cầu nối từ tấm ảnh thư mời pilot04 sang cấu trúc mô hình kiến trúc pilot06.
- **Hành động & Diễn hoạt:**
  - 0.00–0.75s ("Một trong những trường"): Máy bám vào ảnh khuôn viên VU Main Building; vỏ phong bì trượt xuống khỏi đáy màn hình; dải chữ `VU AMSTERDAM` tịnh tiến lên vị trí header tiêu đề (trùng khớp vị trí `#c6-title` của cảnh 06).
  - 0.75–2.25s ("đại học nghiên cứu hàng đầu"): Ảnh đứng thành tấm ảnh lớn; xuất hiện đạo cụ tiền cảnh thể hiện môi trường nghiên cứu (trang sách học thuật mở và bình tam giác/bàn thí nghiệm) với nét vẽ đồng nhất.
  - 2.25–3.233s ("Hà Lan và châu Âu"): Nền ngả sang màu tím nhạt `#EEE9F3`; vỏ kiến trúc cắt lớp của pilot06 (`#c6-drawing`: mái, các tầng sàn, cột trụ) xuất hiện bao quanh tấm ảnh; ảnh đạt đúng tỷ lệ và góc xoay của frame 0 cảnh 06, sẵn sàng cho hiệu ứng bóc mở mặt cắt trong cụm tiếp theo.

---

## 2. Kiểm tra chất lượng kỹ thuật & QA
- **Độ phân giải & Tỷ lệ:** 720×1280 (9:16 dọc), chuẩn mobile.
- **Picture Grid:** Tổng cộng 650 frames chính xác (3.2s + 4.4s + 4.833s + 6.0s + 3.233s = 21.667s).
- **Audio Integrity:** Decoded audio correlation với voice gốc = `0.999958`, RMS = `0.185`, peak = `0.889`, không bị clipping hay time-stretch.
- **Độ tương phản chữ:** Tất cả text checks đều đạt chuẩn WCAG AA.
- **Safe Area:** Vùng chân trang 180–200px (y: 1080–1280) được giữ sạch hoàn toàn cho phụ đề sau này.
