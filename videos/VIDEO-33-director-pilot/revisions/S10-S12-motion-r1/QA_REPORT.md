# S10/S12 motion R1 — QA

Hai pilot mới chờ người dùng duyệt. Không thay master hoặc sáu pilot đã duyệt.

- S10: 185 frames/6.166667s; S12:106 frames/3.533333s;720×1280 @30fps.
- WAV seg_11/seg_14 giữ nguyên; PCM đối chiếu với nguồn và các lát gốc. AAC correlation S10=0.999890, S12=0.999836; có audio không im tiếng, không đổi tốc độ/voice.
- HyperFrames check cả hai: không findings lint/runtime/layout/contrast sau sửa. Render screenshot capture/hardware GPU.
- Lỗi trục quay xuất hiện ở lượt chẩn đoán đầu đã được sửa trước render. Đo hub từ MP4 ở1.4/2.2/3.4s giữ trong1.5px của(490,505). Các cảnh báo drift ban đầu còn ghi trong lịch sử, không phải đầu ra cuối.
- Đã tạo opening/mid/final, mobile/grayscale và contact12fps từ MP4; cần xem các proof cuối trong qa/, không dùng snapshot trước sửa ở proofs/.
- Frame nguồn đã duyệt, master/clean cũ và sáu pilot S01/S09/S07/S08/S06/S11 không đổi hash.

Đã phát cả hai clip trong browser và quan sát trạng thái kết thúc S10 6.17s, S12 3.53s. Tạo hình đã duyệt không đồng nghĩa motion đã duyệt. Các con số giá/điều kiện giữ nguồn như design-r1/RESEARCH_NOTE.json; không thêm claim hoặc sửa voice.
