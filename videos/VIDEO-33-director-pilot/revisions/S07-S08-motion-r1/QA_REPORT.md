# S07/S08 motion R1 — kiểm tra

Hai MP4 có voice gốc, bản WAV copy khớp SHA256, AAC correlation >0.99, 720×1280 @30fps. HyperFrames check cả hai: không có lỗi/cảnh báo lint, runtime, layout hoặc contrast. Render cục bộ screenshot capture với GPU phần cứng.

Đã tạo frame mở/giữa/cuối, mobile/grayscale và contact sampling 12fps từ MP4. Xem qa-verification.json cho số đo thật. Voice/sample giữ nguyên; hình làm tròn lên frame 30fps nên có đuôi hold tối đa một frame. Đã phát cả hai pilot trong browser và quan sát trạng thái kết thúc S07 4.70s / S08 5.50s. Đã xem proof tiếp xúc 12fps, mobile, chuỗi frame và grayscale. Không coi encode/check là duyệt sáng tạo.

Tạo hình/bố cục dựa trên 8 frame R1 đã duyệt; động tác và cue nội cảnh là thực thi mới đang chờ người dùng duyệt. Các khoảng cảnh học/sống/làm ngắn theo voice; mỗi shot có một thao tác nhỏ, không thêm nội dung vào voice. Không thay master, không sản xuất các cảnh khác.
