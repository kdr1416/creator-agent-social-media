# Đánh giá Cụm 2 cảnh cuối (Scene 16–17) · Trần Minh Nhật

**Mốc hoàn thành:** Dailies riêng cụm 2 cảnh cuối (Scene 16 + Scene 17) theo yêu cầu Đạo diễn  
**File xuất khẩu:** `build/renders/tran-minh-nhat-cluster-16-17.mp4` (235 frames · 7.833s)  
**File visual sạch:** `build/renders/cluster_16_17_visual.mp4` (235 frames · 7.833s)  
**File âm thanh gốc:** `build/renders/voice_cluster_16_17.wav` (188,338 samples từ sample 1,448,462 đến 1,636,800 của `full_voice.wav`, correlation: `0.999966`, 0 clipped samples, 0 audio drift)

---

## 1. Chi tiết chuyển tiếp và đồng bộ thị giác giữa Scene 16 & Scene 17

### Cảnh 16: Chương mới được chúc mở ra (92 frames · 3.067s)
- **Bối cảnh & Đạo cụ:** Toàn cảnh kênh đào Amsterdam buổi sớm (bầu trời vàng ửng, mặt nước phản chiếu êm ả, dãy nhà đầu hồi gable cổ kính) cùng cây cầu gạch vòm cong (`canal-bridge`, màu terracotta `#C96B48`, lan can uốn cong).
- **Diễn hoạt:**
  - 0.00–1.20s ("Chúc Minh Nhật"): Nhật bước tự tin từ bên trái lên vòm cầu.
  - 1.20–2.40s ("hành trình thật rực rỡ tại Hà Lan"): Nhật dừng tại đỉnh vòm cầu, quay lại nở nụ cười rạng rỡ và vẫy tay chào vui vẻ về phía sau; dải chữ `CHƯƠNG MỚI` xuất hiện.
  - 2.40–3.07s: Nhật quay đầu lại về hướng đi phía trước, bước tiếp sang sườn dốc bên phải cây cầu vòm và dừng ở toạ độ `(x: 365, y: 642)` khi hết cảnh.

### Cảnh 17: Hành trình còn tiếp (143 frames · 4.767s)
- **Bối cảnh & Đạo cụ (Đã đồng bộ tuyệt đối với Cảnh 16):**
  - **Giữ nguyên 100% cây cầu vòm gạch cổ kính từ Cảnh 16**, kết nối tự nhiên với đoạn vỉa hè lát đá ven kênh ở góc phải màn hình (`x: 650–720`).
  - Dãy nhà đầu hồi Amsterdam giữ nguyên tỷ lệ, kích thước và màu sắc, dịch nhẹ sang trái theo hiệu ứng thị sai (parallax) khi nhân vật tiến bước.
- **Diễn hoạt (Match-cut hoàn hảo):**
  - 0.00–1.20s ("tiếp tục phát huy bản lĩnh"): Bắt đầu chính xác tại toạ độ kết của Cảnh 16 `(x: 365, y: 642)` trên sườn dốc cây cầu vòm. Nhật dừng một nhịp, mở cuốn sổ xanh và kẹp chiếc bookmark màu cam (callback gợi nhớ Cảnh 01) vào trang giấy trắng cho hành trình mới.
  - 1.20–3.00s ("khám phá những cơ hội mới"): Nhật khép sổ vào tay và sải bước **đi xuống sườn dốc cây cầu cong** (`x: 365 -> 455 -> 555`, chân hạ dần theo độ cong của cầu), bước ra khỏi nhịp cầu và tiếp đất lên vỉa hè ven kênh.
  - 3.00–4.15s ("chinh phục nhiều cột mốc lớn hơn"): Nhật tiếp tục tiến bước về phía trước đầy năng lượng trên con đường mới mở rộng.
  - 4.15–4.77s ("trong tương lai"): Dải tiêu đề `HÀNH TRÌNH CÒN TIẾP` xuất hiện trang nhã; khung hình giữ tĩnh 0.6s cuối cùng đồng điệu với voice gốc, không chèn logo hay CTA cưỡng ép.

---

## 2. Bảng kiểm tra chất lượng kỹ thuật & QA

| Hạng mục kiểm tra | Tiêu chuẩn | Kết quả thực tế (Cụm 16–17) | Đánh giá |
|---|---|---|:---:|
| **Khung hình & Tỷ lệ** | 720 × 1280 (9:16 dọc), 30 fps | 720 × 1280, 30.0 fps | **Đạt 100%** |
| **Tổng số frame** | Đúng 92 + 143 = 235 frames | 235 frames (7.833s) | **Khớp tuyệt đối** |
| **Độ khớp tại điểm nối (Cut point)** | Frame 91 -> Frame 92 không giật cục | Độ lệch điểm cầu: < 8.5px | **Match-cut mượt mà** |
| **Bảo tồn cây cầu vòm** | Cầu cong ở cả 2 cảnh, không biến thành đường thẳng | Cây cầu vòm cong xuất hiện xuyên suốt | **Khắc phục triệt để** |
| **Tương quan âm thanh** | Correlation >= 0.98 | **`0.999966`** (0 clipped samples) | **Hoàn hảo** |
| **Safe Zone chân trang** | Giữ trống hoàn toàn vùng y: 1080–1280 | 0 phần tử vi phạm | **Đạt 100%** |
