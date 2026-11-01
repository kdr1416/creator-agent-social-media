# S06/S11 — kiểm tra pilot motion R1

Hai pilot mới chờ người dùng duyệt. Không thay master hoặc các pilot đã duyệt.

- 720×1280, 30fps. S06: 174 frames/5.800s; S11: 205 frames/6.833333s.
- S06 giữ WAV gốc seg_06. S11 nối nguyên PCM seg_12 + seg_13; payload được đối chiếu cả các lát gốc và đúng khoảng sample trong source_audio.wav. Không sửa lời/timing/tốc độ.
- AAC correlation: S06 0.999774; S11 0.999902. Có đủ audio, không im tiếng. Hình chỉ giữ thêm đuôi dưới một frame để khớp grid.
- HyperFrames check cả hai: không có findings ở lint/runtime/layout/contrast. Render screenshot capture bằng hardware GPU.
- Đã trích và xem opening/mid/final cùng các giai đoạn hành động từ MP4; contact sampling 12fps cho đoạn lên ghế và chuyển giao/cất vở. Mobile/grayscale được tạo để kiểm độ đọc, không coi check kỹ thuật là duyệt sáng tạo.
- Sáu frame design R1 và master/clean trước không đổi hash; các MP4 S01/S09/S07/S08 đã duyệt cũng đã đối chiếu lại.

Đã phát cả hai MP4 trong browser, thấy trạng thái kết thúc S06 5.80s và S11 6.83s. Cue nội cảnh là quyết định đạo diễn trong timeline voice cố định; cần người dùng duyệt cảm giác nhịp và hành động.
