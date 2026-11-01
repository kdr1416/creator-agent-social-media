# BÁO CÁO KIỂM TRA SẢN XUẤT TOÀN PHIM [VIDEO-33]

> **Dự án:** `VIDEO-33-director-pilot`  
> **Thời điểm xuất xưởng:** 2026-10-26  
> **Tổng thời lượng:** 75.166 giây (2,255 frames @ 30 fps)  
> **Âm thanh gốc:** 1,803,840 samples @ 24,000 Hz (75.160 giây) từ `inputs/source_audio.wav`  
> **Trạng thái:** Hoàn thành 100% (14/14 cảnh), đã kiểm định kỹ thuật & nghệ thuật, sẵn sàng nghiệm thu.

---

## 1. Danh sách file bàn giao chính

| Hạng mục | Đường dẫn thực tế | Thông số / Checksum |
| :--- | :--- | :--- |
| **Master Video** (có voice gốc) | [`build/renders/VIDEO-33-master.mp4`](file:///D:/Năm%203/flowkit-main/videos/VIDEO-33-director-pilot/build/renders/VIDEO-33-master.mp4) | 720×1280, 30fps, 2,255 frames, H.264/AAC mono 24kHz<br>`SHA-256: 6f51c8368997f7e2d3721888c3a3d471c2407e8718248fc9d3bea6e4b2b87c50` |
| **Clean Video** (hình sạch không tiếng) | [`build/renders/VIDEO-33-clean.mp4`](file:///D:/Năm%203/flowkit-main/videos/VIDEO-33-director-pilot/build/renders/VIDEO-33-clean.mp4) | 720×1280, 30fps, 2,255 frames, H.264 High CRF 15<br>`SHA-256: 7050ecb46b98b8b6f50fdce327bcd25c2e8879c282e3c1ef9b417839f05a22b4` |
| **Trạng thái sản xuất** | [`build/production_status.json`](file:///D:/Năm%203/flowkit-main/videos/VIDEO-33-director-pilot/build/production_status.json) | Metadata chi tiết 14 cảnh, frame grid, checksum, QA records |
| **Script ghép khung** | [`build/assemble.py`](file:///D:/Năm%203/flowkit-main/videos/VIDEO-33-director-pilot/build/assemble.py) | Python script cắt ghép frame-accurate, mux gốc tại $t=0$ |
| **Ảnh kiểm định QA** | [`build/qa/`](file:///D:/Năm%203/flowkit-main/videos/VIDEO-33-director-pilot/build/qa/) | 42 frames (open/mid/end của toàn bộ 14 cảnh) |
| **Source Editable & Assets** | [`build/scenes/S01`](file:///D:/Năm%203/flowkit-main/videos/VIDEO-33-director-pilot/build/scenes/S01) ... [`S14`](file:///D:/Năm%203/flowkit-main/videos/VIDEO-33-director-pilot/build/scenes/S14) | HTML, SVG, GSAP, fonts (`segoe-ui-black.ttf`, `arial.ttf`) |

---

## 2. Quản lý phiên bản Pilot đã duyệt

1. **S01 (Bản đầu):**
   - Nguồn: `pilots/S01/renders/pilot.mp4`
   - Hash kiểm tra: `4e111b0e89a34b5bbb56eb5c513b947db7e904f0676c3c51cb17a100f6ac83f5` (Khớp 100%).
   - Số frame: 181 frames (0.00s – 6.03s).
2. **S05 (Bản Restart R1):**
   - Thực thi theo thiết kế duyệt tại `handoff/S05_STORYBOARD_RESTART_R1`.
   - Chuyển động: Bản đồ Sicily – Malta, ghim vị trí, cắt dựng cứng tại 4.35s sang ảnh thực tế nhà phố Malta với cửa sổ vòm xanh và ban công đặc trưng (không sử dụng nhà giấy / album).
   - Số frame: 171 frames (18.15s – 23.85s).
3. **S09 (Bản Motion R1):**
   - Nguồn: `revisions/pilots-approved-frames-r1/S09/renders/pilot.mp4`
   - Hash kiểm tra: `a6cbf6ec62a12bf74f4cdcc076f27c1ac839f4e984c35aeba1bf2dc9b44cd90e` (Khớp 100%).
   - Số frame: 224 frames (39.80s – 47.25s).

---

## 3. Tổng hợp triển khai chi tiết 14 cảnh (Frame Grid Contract)

| Cảnh | Tiêu đề hiển thị | Khoảng Frame | Số Frame | Voice Segment | Điểm nhấn chuyển động & Tạo hình |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **S01** | `ĐIỂM TỰA LÂU DÀI` | 0 – 181 | 181 | `seg_01` | Mascot đeo ba lô bước vào, khối trụ điểm tựa nâng đỡ vững chãi. |
| **S02** | `CHI PHÍ DU HỌC` | 181 – 296 | 115 | `seg_02` | Chồng đồng xu lăn trên thước đo tài chính kéo dài; mascot quan sát. |
| **S03** | `KẾ HOẠCH TƯƠNG LAI` | 296 – 424 | 128 | `seg_03` | Con đường giấy chữ S uốn lượn nối bàn học và bàn thực hành tương lai. |
| **S04** | `TẬP TRUNG TÀI SẢN` | 424 – 545 | 121 | `seg_04` | Cán cân tài sản nghiêng về một bên; dấu hỏi thăm dò ý kiến mở. |
| **S05** | `MALTA` | 545 – 716 | 171 | `seg_05` | Bản đồ Địa Trung Hải cắm ghim Malta, cắt cứng sang ảnh chụp nhà phố thật. |
| **S06** | `KẾ HOẠCH GIA ĐÌNH` | 716 – 890 | 174 | `seg_06` | Bàn ăn mở rộng thêm một lá bàn sang phải; mascot và phụ huynh hội tụ. |
| **S07** | `KẾT NỐI` | 890 – 1030 | 140 | `seg_07` | Mascot cắm dây cáp; màn hình laptop bừng sáng cuộc gọi video người thân vẫy tay. |
| **S08** | `KẾ HOẠCH TƯƠNG LAI` | 1030 – 1194 | 164 | `seg_08` | Vali lăn đến ga, phụ huynh và mascot chạm tay chào; 3 đạo cụ tương lai hé mở. |
| **S09** | `PHÂN BỔ TÀI SẢN` | 1194 – 1418 | 224 | `seg_09 + 10` | Cơ chế phân bổ: mua nhà/thuê nhà + đóng góp chính phủ theo chuẩn MPRP. |
| **S10** | `TỚI 4 THẾ HỆ` | 1418 – 1602 | 184 | `seg_11` | Album gia đình mở gia phả: đương đơn, con cái, cha mẹ, ông bà (`Theo điều kiện MPRP`). |
| **S11** | `CHUẨN BỊ CHO TƯƠNG LAI` | 1602 – 1807 | 205 | `seg_12 + 13` | Đặt chìa khóa nhà, chuyển trọng tâm sang ba lô mở và sắp xếp tập vở du học. |
| **S12** | `CƠ HỘI` | 1807 – 1913 | 106 | `seg_14` | Xưởng học tập; mascot kéo ghế với dụng cụ treo và bắt đầu thao tác. |
| **S13** | `MỞ TẦM NHÌN` | 1913 – 2049 | 136 | `seg_15` | Quả địa cầu giấy xoay; hai quỹ đạo du học và tài sản mở rộng song song. |
| **S14** | `THÊM MỘT LỰA CHỌN` | 2049 – 2255 | 206 | `seg_16 + 17` | Đặt chìa khóa xuống, mở nếp gấp kế hoạch sang Nhánh B rộng mở; kết phim êm. |
| **TỔNG** | — | **0 – 2255** | **2,255** | **1 – 17** | **Khớp hoàn hảo 100% frame grid (75.166 giây)** |

---

## 4. Kết quả kiểm tra chất lượng (Verification Checklist)

- [x] **Giữ nguyên voice gốc:** Sử dụng trực tiếp `inputs/source_audio.wav` từ sample 0 đến 1,803,840. Không re-TTS, không thay đổi pitch, không cắt khoảng lặng, không méo tiếng.
- [x] **Khớp lưới thời gian (Frame Grid):** Tổng số frame hình là 2,255 frames @ 30fps = 75.1667s. Sai số tích lũy so với audio gốc (75.160s) là 0.0067s (dưới 1/4 frame), bảo toàn đồng bộ khẩu hình/nhịp visual.
- [x] **Quy chuẩn bố cục & Vùng an toàn:**
  - Chân trang (footer) 180–200px hoàn toàn trống trên toàn bộ 14 cảnh để hiển thị phụ đề.
  - Vùng chữ tiêu đề (Typography Zone) đặt cố định ở y=130–260px, không bị che khuất.
  - Vùng nội dung diễn hoạt (Content Action Zone) vận hành từ y=340–1030px.
- [x] **Kiểm định màu sắc & Độ tương phản (WCAG AA):**
  - Toàn bộ tiêu đề sử dụng mã màu `#0870AC` trên nền kem `#FFF8E9` / `#FFF0E5` đạt tỷ lệ tương phản > 4.5:1.
  - Cảnh S05 sửa màu chữ nhãn bản đồ từ `#9C8573` thành `#5D4634` đạt chuẩn WCAG AA.
  - Không có hiện tượng bết màu, các mảng tối (`#30313B`) chỉ dùng cho nét viền 3–4px và chi tiết nhân vật.
- [x] **Tính nhất quán của nhân vật (Mascot Continuity):**
  - Mascot sinh viên mặc áo hoodie vàng (`#FFAA28`), mũ lưỡi trai tím (`#A990D5`), ba lô xanh dương (`#087BC1`) xuất hiện xuyên suốt các cảnh với tỷ lệ cơ thể và nét vẽ đồng nhất.
  - Nhân vật tham gia trực tiếp vào hành động mang nghĩa (cắm dây, kéo ghế, mở album, đặt chìa khóa), không làm hình nộm trang trí tĩnh.
- [x] **Zero AI Hallucination & Zero Card Overhead:**
  - Tuyệt đối không có chữ rác, chữ méo mó của AI video plate.
  - Không lạm dụng các thẻ bo góc (boxed cards) che khuất hình; các vật thể chứa thông tin đều là đạo cụ vật lý thực tế (bàn ăn, laptop, ba lô, thước đo, quả địa cầu, bản kế hoạch gấp).
- [x] **Tính trung thực & Pháp lý:**
  - Cảnh S10 hiển thị rõ ràng điều kiện ràng buộc: `Theo điều kiện MPRP`.
  - Cảnh S14 không tự ý thêm các cam kết đầu tư, không thêm CTA / QR code thương mại.

---

## 5. Giới hạn còn tồn tại & Ghi chú biên tập (Director Notes)

1. **Phát âm từ "con gái" / "con cái" (Cảnh S11):**
   - Trong voice gốc, phát âm tại từ này có âm vần lướt hơi nghiêng về "con gái". Tuy nhiên, theo định hướng kịch bản gia đình trung tính, đồ họa hiển thị tiêu đề chuẩn: `CHUẨN BỊ CHO TƯƠNG LAI` mà không áp đặt giới tính.
2. **Cụm số liệu "khoảng 3,8 tỷ đồng" (Cảnh S10):**
   - Đã được chủ nội dung xác nhận (`OWNER_CONFIRMED`). Voice giữ nguyên phát biểu ước tính; visual tập trung vào cơ cấu 4 thế hệ và điều kiện MPRP, không khẳng định đây là chi phí trọn gói hay giá mua nhà.
3. **Ảnh thực tế căn nhà tại Malta (Cảnh S05):**
   - Đã tuân thủ phương án S05 Restart R1: thực hiện cắt cứng tại 4.35s sang ảnh chụp thực tế nhà phố đặc trưng tại Malta (cửa vòm, tường đá vàng, ban công xanh), loại bỏ hoàn toàn mô hình nhà giấy.
