# Báo cáo Bàn giao Toàn bộ Tác phẩm · Trần Minh Nhật

**Dự án:** Sản xuất phim hoạt hoạ giới thiệu học bổng & hành trình du học của Trần Minh Nhật  
**Địa điểm bàn giao:** `videos/tran-minh-nhat-director-handoff/build/`  
**File xuất khẩu hoàn chỉnh (Full Film):** `build/renders/tran-minh-nhat-final.mp4`  
**Tổng số cảnh:** 17 cảnh (14 cảnh thiết kế mới + 3 cảnh pilot tham chiếu)  
**Tổng số frame:** 2,046 frames @ 30.0 fps  
**Thời lượng video:** 68.200s (01:08.20)  
**Âm thanh:** Mux trực tiếp toàn bộ 1,636,800 samples từ `inputs/full_voice.wav` (AAC mono 24kHz, correlation: `0.999958`, 0 clipped samples, 0 audio drift)

---

## 1. Danh mục các file xuất xưởng (Master Deliverables)

| Tên sản phẩm | Đường dẫn file | Thời lượng / Frame | Mô tả |
|---|---|---|---|
| **Full Film Master** | `build/renders/tran-minh-nhat-final.mp4` | 68.200s · 2,046 f | Bản phim hoàn chỉnh 17 cảnh mux cùng voice gốc `full_voice.wav` |
| **Full Visual Stream** | `build/renders/film_01_17_visual.mp4` | 68.200s · 2,046 f | Luồng hình ảnh sạch (video-only) ghép từ 17 scene renders |
| **Cluster 01–05** | `build/renders/tran-minh-nhat-cluster-01-05.mp4` | 21.667s · 650 f | Cụm 1: Mở đầu, học bổng VU, định hướng ngành |
| **Cluster 06–08** | `build/renders/tran-minh-nhat-cluster-06-08.mp4` | 12.600s · 378 f | Cụm 2: Môi trường campus, giá trị học thuật, cơ hội toàn cầu |
| **Cluster 09–12** | `build/renders/tran-minh-nhat-cluster-09-12.mp4` | 14.867s · 446 f | Cụm 3: Phía sau thành quả, Mentor Esora, hồ sơ Minh Nhật, 3 cốt lõi |
| **Cluster 13–17** | `build/renders/tran-minh-nhat-cluster-13-17.mp4` | 19.067s · 572 f | Cụm 4: Câu chuyện riêng, kể có trọng tâm, hoàn tất hồ sơ, Hà Lan, tương lai |

---

## 2. Bảng đối chiếu 17 Cảnh theo Kế hoạch Khung hình (Picture Frame Plan)

| Scene | Tên phân cảnh | Start Frame | End Frame | Frames | Duration | Engine / Pilot Ref |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| **01** | Bàn làm việc & Giấc mơ du học | 0 | 96 | 96 | 3.200s | HF_ONLY (New) |
| **02** | Hành trình kết tinh thành kết quả | 96 | 228 | 132 | 4.400s | HF_ONLY (New) |
| **03** | Học bổng cử nhân VU Amsterdam | 228 | 373 | 145 | 4.833s | HF_ONLY (New) |
| **04** | Ngành Khoa học Máy tính | 373 | 553 | 180 | 6.000s | Ref Pilot 04 (Bỏ dòng "Hình minh hoạ") |
| **05** | Trường đại học nghiên cứu hàng đầu | 553 | 650 | 97 | 3.233s | HF_ONLY (New) |
| **06** | Nhiều lĩnh vực cùng một campus | 650 | 806 | 156 | 5.200s | Ref Pilot 06 (5 không gian đào tạo) |
| **07** | Giá trị học thuật quốc tế | 806 | 934 | 128 | 4.267s | HF_ONLY (New, tay cầm bằng tinh tế) |
| **08** | Cơ hội là các lựa chọn mở | 934 | 1028 | 94 | 3.133s | HF_ONLY (New, địa cầu xoay 3D nghiêng 23.5°) |
| **09** | Đằng sau thành quả là bàn làm việc | 1028 | 1130 | 102 | 3.400s | HF_ONLY (New) |
| **10** | Mentor giúp Nhật làm rõ lựa chọn | 1130 | 1234 | 104 | 3.467s | HF_ONLY (New, no fake badges) |
| **11** | Thành tích là chất liệu của hồ sơ | 1234 | 1341 | 107 | 3.567s | HF_ONLY (New, 3D page flip) |
| **12** | Ba thành phần cốt lõi | 1341 | 1474 | 133 | 4.433s | Ref Pilot 12 (Tư duy, Cá tính, Định hướng) |
| **13** | Mỗi câu chuyện có cấu trúc riêng | 1474 | 1537 | 63 | 2.100s | HF_ONLY (New, 3 notebooks) |
| **14** | Kể có trọng tâm | 1537 | 1678 | 141 | 4.700s | HF_ONLY (New, essay hierarchy) |
| **15** | Hoàn tất cùng người đồng hành | 1678 | 1811 | 133 | 4.433s | HF_ONLY (New, portfolio binder) |
| **16** | Chương mới được chúc mở ra | 1811 | 1903 | 92 | 3.067s | HF_ONLY (New, canal scene) |
| **17** | Hành trình còn tiếp | 1903 | 2046 | 143 | 4.767s | HF_ONLY (New, open future) |
| **Tổng** | **Toàn bộ bộ phim** | **0** | **2046** | **2,046** | **68.200s** | **17/17 Hoàn tất** |

---

## 3. Tổng kết Tuân thủ Đạo diễn & Kỹ thuật

1. **Bảo tồn âm thanh nguyên bản:** Giữ nguyên vẹn 100% file thoại `full_voice.wav`, không TTS lại, không thêm nhạc nền (BGM), hiệu ứng âm thanh (SFX) hay CTA cưỡng ép. Tương quan âm thanh đạt `0.999958`.
2. **Tuân thủ Fact-check & Tôn trọng thực tế:**
   - Không bịa GPA, chứng chỉ hay thư trúng tuyển giả.
   - Ở Cảnh 10: Không hiển thị số "14" hay huy hiệu kinh nghiệm chưa được kiểm chứng.
   - Ở Pilot 04: Đã loại bỏ hoàn toàn dòng ghi chú "Hình minh hoạ" trong bản sao `build/scenes/scene_04/`.
   - Ở Cảnh 16–17: Thể hiện Amsterdam dưới dạng phong cảnh minh hoạ khát vọng nghệ thuật, không giả định Nhật đã nhập cảnh hay tốt nghiệp.
3. **Safe Area & Khả năng tiếp cận:**
   - Vùng chân trang y: 1080–1280 được giữ trống 100% trong toàn bộ 17 cảnh.
   - 100% văn bản đạt chuẩn tương phản tiếp cận WCAG AA.
4. **Cô lập mã nguồn:** Toàn bộ sản phẩm được tạo trong `build/`, không xâm phạm hay sửa đổi các thư mục gốc `reference_pilots/`, `inputs/` hay `scratch/`.
