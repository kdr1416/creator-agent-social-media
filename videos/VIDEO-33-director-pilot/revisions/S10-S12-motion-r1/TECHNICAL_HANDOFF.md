# S10/S12 motion R1 — technical handoff

720×1280 @30fps. S10: 185 frames/6.166667s, source voice 6.156875s. S12: 106 frames/3.533333s, voice 3.531458333333s. WAV copy nguyên file seg_11/seg_14; giữ sample timing, raw/corrected text và voice. Hình có phần hold lẻ dưới một frame để khớp grid; khi ghép theo timeline toàn phim không cộng đuôi hold từng pilot độc lập.

S10: cost-shot chuyển bằng editorial cut sang family-shot rộng hơn. Người thân đã trong bước tiếp cận, bước ngắn và nối bàn tay, không scale/bay vào hay biến khối giấy thành người. Metric và bốn thế hệ thuộc hai shot khác nhau. Tiêu đề/điều kiện xuất hiện ở local4.0–4.24s để đọc trước resolve, nhãn quan hệ 4.48–4.76s. Đây là tinh chỉnh đọc hình so với cue đề xuất ban đầu; voice không đổi. Quan hệ nhãn tính theo đương đơn. Giữ “TỚI” và “Theo điều kiện MPRP”; không diễn giải giá thành phí trọn gói.

S12: tay chạm mặt nút (385,822), ấn xuống (385,829), đèn bật rồi rotor quay. Chỉ rotor quay; trụ/bệ giữ nguyên. Pivot local của rotor là (0,0) bên trong placement translate(490,505). Có circle r150 fill/stroke none định nghĩa envelope đối xứng cho rig; không tạo hình thấy được và giúp kiểm bbox của silhouette ba cánh bất đối xứng. Điểm hub trong MP4 đã đo lại ở ba góc quay, nằm trong1.5px của (490,505). Không đổi pivot sang svgOrigin(490,505) trên node con — sẽ cộng sai hệ tọa độ và quay lệch.

Một paused GSAP timeline/root mỗi scene; CSS đặt initial-hidden state. Các placement g authored giữ nguyên, hành động dùng wrapper riêng; vai, path cẳng tay và hand cùng hệ tọa độ. Mọi fonts/runtime/audio local. source/PNG design-r1 không thay đổi.

Các folder proofs/ giữ lịch sử trước sửa. Chỉ qa/ và renders/pilot.mp4 là proof/output cuối. Motion R1 chưa được người dùng duyệt. Chưa thay master hay dựng các cảnh khác.
