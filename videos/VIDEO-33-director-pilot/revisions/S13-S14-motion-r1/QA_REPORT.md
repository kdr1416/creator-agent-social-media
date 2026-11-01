# S13/S14 motion R1 — QA

- Hai MP4720×1280 @30fps; S13=137 frames/4.566667s, S14=206 frames/6.866667s.
- PCM giữ nguyên từ source; S14 nối nguyên hai lát16/17. AAC correlation S13=0.999928, S14=0.999861. Không thiếu audio hoặc time-stretch.
- Check lint/runtime/layout/contrast cả hai không findings sau sửa; S13 có khai báo overflow có chủ đích cho world bị camera crop. Render screenshot capture/hardware GPU.
- Camera S13 đã sửa trước encode; lossless endpoint đầu/cuối khớp PNG đã duyệt(MAE0). PNG trong S13/proofs/ là lịch sử trước sửa; qa/ là ảnh từ MP4 cuối.
- Đã trích contact12fps từ MP4 cho camera S13 và bàn tay/bản lề S14; mobile/grayscale được tạo. Hình học authored của gate giữ hinge và chiều cao200px; grip và handle trùng điểm trong45 mẫu, độc lập với kiểm ảnh thực tế.
- Frame design đã duyệt, tám pilot đã duyệt trước, master/clean cũ không đổi hash.

Browser playback: đã quan sát cả hai clip phát hết trong IAB (S13 4.57s, S14 6.87s). User approved S13/S14 motion R1 on 2026-10-27; see APPROVAL.json. Master remains unchanged.
