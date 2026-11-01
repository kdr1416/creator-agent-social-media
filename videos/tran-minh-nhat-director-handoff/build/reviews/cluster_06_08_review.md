# Đánh giá cụm cảnh 06–08 · Trần Minh Nhật

**Mốc hoàn thành:** Dailies cụm 06–08 (21.667s – 34.267s)  
**File xuất khẩu cụm 06–08:** `build/renders/tran-minh-nhat-cluster-06-08.mp4` (378 frames · 12.600s)  
**File xuất khẩu lũy kế 01–08 (nửa phim):** `build/renders/tran-minh-nhat-cluster-01-08.mp4` (1028 frames · 34.267s)  
**Audio mux:** Trích xuất chính xác 302,136 samples (sample 520,028 – 822,164) từ `inputs/full_voice.wav` (độ dài 12.589s, correlation: 0.999960, 0 clipped samples)

---

## 1. Chi tiết tạo hình và chuyển cảnh từng cảnh trong cụm 06–08

### Cảnh 06: Nhiều lĩnh vực cùng một campus (156 frames · 5.200s)
- **Nguồn & Tích hợp:** Sử dụng bản pilot chuẩn đã chọn trong `reference_pilots/scene_06/`.
- **Xử lý kỹ thuật:**
  - Tách luồng hình ảnh sạch (video-only) với đúng 156 frames chuẩn picture grid @ 30fps.
  - Loại bỏ audio phát riêng trong file HTML gốc của pilot để bảo đảm chỉ có một nguồn voice duy nhất trong bản ghép.
  - Giữ nguyên toàn bộ diễn hoạt mặt cắt kiến trúc mở 5 không gian đào tạo và nghiên cứu: Kinh doanh, Khoa học dữ liệu, Trí tuệ nhân tạo, Luật, Khoa học sức khoẻ.

### Cảnh 07: Giá trị học thuật trong bối cảnh quốc tế (128 frames · 4.267s)
- **Ý nghĩa & hình chủ đạo:** Khái niệm giá trị bằng cấp ở cấp độ trường đại học nghiên cứu trong môi trường quốc tế; tuyệt đối không diễn giải thành việc Nhật đã tốt nghiệp hay có job offer/hợp đồng việc làm.
- **Tạo hình & Diễn hoạt (Đã nâng cấp theo phản hồi Đạo diễn - Phương án 7A):**
  - 0.00–1.00s ("Tấm bằng từ VU Amsterdam"): Cắt chuyển cảnh dứt khoát từ 06 sang cuộn bằng parchment danh dự buộc dải lụa xanh (`#087BC1`). Dải lụa mở bung ngang, để lộ biểu tượng huy hiệu trường và tên định danh `VU AMSTERDAM` cùng hoa văn viền vàng tinh tế; không vẽ chữ ký/con dấu/điểm số/mã hiệu giả tạo.
  - 1.00–2.60s ("được các doanh nghiệp và tổ chức quốc tế"): Góc nhìn mở rộng ra hai cánh không gian học thuật - làm việc song hành (bàn nghiên cứu với đèn kiến trúc, tài liệu chuyên sâu bên trái; bàn làm việc nhóm quốc tế với màn hình dữ liệu phân tích mạng lưới toàn cầu bên phải). Hai không gian được tạo hình tự nhiên theo chiều sâu, không dùng card/box thông tin generic.
  - 2.60–3.70s ("đánh giá cao"): Bàn tay người đọc/chuyên gia (`reader_hand`) được định vị chuẩn xác tại góc dưới phải (`x: 450, y: 680–760`), tách nhóm neo toạ độ tĩnh độc lập khỏi GSAP animation. Bàn tay được vẽ tự nhiên, lịch thiệp với ống tay áo tối màu (`#3A3644`), cổ tay áo sơ mi trắng tinh khôi và các ngón tay ôm nâng nhẹ mép phải tấm bằng, ngón cái đặt trân trọng trên mặt giấy. Dải tiêu đề `GIÁ TRỊ HỌC THUẬT` xuất hiện trang nhã, không còn bị vật thể lạ che khuất hay dính vào góc trần.
  - 3.70–4.267s: Giữ nhịp ổn định, dải lụa xanh dẫn hướng màu chuyển sang quả địa cầu ở cảnh 08.

### Cảnh 08: Cơ hội là các lựa chọn mở (94 frames · 3.133s)
- **Ý nghĩa & hình chủ đạo:** Thể hiện phạm vi toàn cầu và hai hướng khả năng song song (tiếp tục học tập & phát triển nghề nghiệp) mà không cam kết hay giới hạn trước kết quả cụ thể.
- **Tạo hình & Diễn hoạt (Đã nâng cấp xoay quả địa cầu 3D):**
  - 0.00–0.80s ("mở ra nhiều cơ hội"): Quả địa cầu để bàn được thiết kế lại theo đúng quy chuẩn địa cầu cổ điển: khung bán nguyệt meridian bằng đồng đỡ trục nghiêng chuẩn 23.5°. Cả hệ thống bản đồ (bao gồm các khối lục địa và các đường kinh tuyến/vĩ tuyến) được đồng bộ xoay cùng nhau quanh trục nghiêng 23.5°. Lớp đổ bóng mặt cầu đa lớp (radial spherical gradient) và viền sáng specular rim highlight tạo khối cầu 3D tròn đầy. Tay Nhật chạm tiếp xúc chuẩn xác vào mặt cầu và xoay một góc mềm mại với gia tốc tự nhiên (`power2.out`).
  - 0.80–2.00s ("học tập và nghề nghiệp"): Hai bối cảnh thu nhỏ mở bung lên từ bề mặt địa cầu qua các nếp gấp giấy:
    - Bối cảnh 1 (trên trái): Góc bàn học tập chuyên sâu với đèn bàn, chồng sách và tab `HỌC TẬP`.
    - Bối cảnh 2 (bên phải): Bàn làm việc dự án với bản kế hoạch/màn hình và tab `NGHỀ NGHIỆP`.
    - Hai cơ hội đặt ngang hàng, không có mũi tên nhân quả cưỡng ép.
  - 2.00–3.133s ("trên toàn cầu"): Nhật nhìn bao quát cả hai hướng mở với nụ cười tự tin; dải chữ `CƠ HỘI RỘNG MỞ` xuất hiện với chuyển động nảy mềm.

---

## 2. Kiểm tra chất lượng kỹ thuật & QA
- **Độ phân giải & Tốc độ:** 720×1280 (9:16 dọc), 30fps.
- **Picture Grid cụm 06–08:** 156 + 128 + 94 = 378 frames (12.600s).
- **Picture Grid lũy kế 01–08:** 650 + 378 = 1028 frames (34.267s, đạt 50.2% tổng thời lượng toàn phim 2046 frames / 68.2s).
- **Audio Integrity:** Tương quan âm thanh giải mã với file gốc = `0.999960`, 0 clipped samples, khớp hoàn hảo từng nhịp thoại không có độ trôi (drift).
- **Độ tương phản chữ:** 100% text vượt qua kiểm tra WCAG AA (đã tinh chỉnh nhãn tab `NGHỀ NGHIỆP` sang tone cam đậm `#B34418` để bảo đảm độ tương phản tối ưu trên nền trắng).
- **Safe Area:** Giữ trống hoàn toàn vùng chân trang 180–200px (y: 1080–1280).
