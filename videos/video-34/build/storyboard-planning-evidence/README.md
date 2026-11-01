# Storyboard planning evidence — 2026-11-01

Đây là evidence cho bước viết storyboard, không phải approval hoặc runtime validation mới.

- `editorial-plan.json`: dữ liệu biên tập 17 scene dùng để soạn storyboard; storyboard.md là tài liệu đọc/review chính.
- `anchors.json`: 53 nhóm word anchors đối chiếu trực tiếp ASR (IDs từ 1).
- `validation.json`: kết quả kiểm tra tính nhất quán tài liệu và 12 hash file được bảo vệ.
- `changes.diff`: diff 3 file sửa và 2 tài liệu mới so với backup trước bước này.

Backup trước thay đổi ở `../storyboard-before-20261101/`: storyboard.md, style-tokens.json, production_status.json, protected-before.json và word-boundary-audit.json. Không có Git để dựa vào rollback commit.

## Rollback có phạm vi

Chỉ khi muốn hủy bản storyboard này và chưa có chỉnh sửa tiếp theo: sao chép ba file từ backup về cùng đường dẫn tương đối trong video-34 (`creative/storyboard.md`, `creative/style-tokens.json`, `production_status.json`). Nếu đã có chỉnh sửa mới, sao lưu bản hiện tại và đối chiếu changes.diff trước, không ghi đè phần việc mới.

Hai tài liệu mới `creative/style-bible.md` và `creative/assets-components-plan.md` có thể giữ dưới dạng draft cũ hoặc chuyển vào một thư mục backup có tên riêng trong video-34. Không cần xóa assets, inputs, scene source, outputs hay bất kỳ video project nào. Các file evidence có thể giữ để truy vết. Không chạy destructive Git hoặc recursive delete.

Không có source animation, render, dependency hay approval thật nào được tạo trong bước này. Không được dùng kết quả kiểm tra văn bản để tuyên bố visual quality, audio cut quality hoặc creative approval đã PASS.
