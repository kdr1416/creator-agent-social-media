# Flow Kit V2 — Three Core Style Production System

Ngày nghiên cứu: 01/11/2026, Asia/Saigon. Trạng thái: **guidance đề xuất, chưa được kiểm chứng bằng pilot mới và chưa được human-approved**. Phạm vi lần này chỉ gồm tài liệu và bằng chứng kiểm toán. Không sửa production VIDEO-34.

Ba Core Styles đã được người dùng quyết định: `kurzgesagt`, `izometrik`, `bauhaus`. Không đánh giá lại tập lựa chọn này. Tên Kurzgesagt-inspired chỉ nguyên tắc minh họa, không đại diện cho một tài liệu chính thức hay quan hệ với studio Kurzgesagt. Artwork phải là bản gốc.

## Đọc theo nhu cầu

| Tài liệu | Nội dung sở hữu |
|---|---|
| [Research & audit](RESEARCH-AUDIT.md) | Inventory upstream, giới hạn license, nguồn kiểm chứng, thiếu hụt tích hợp và chẩn đoán pilot |
| [Shared production contracts](SHARED-PRODUCTION.md) | Voice highlights/effects, seek-safe, QA, phối style và đề xuất tích hợp skills |
| [Kurzgesagt playbook](kurzgesagt.md) | Minh họa, môi trường, nhân vật, acting và narrative transformation |
| [Isometric playbook](izometrik.md) | Hệ tọa độ, hình học, không gian, ánh sáng và chuyển động nhất quán |
| [Bauhaus playbook](bauhaus.md) | Bố cục đồ họa, kinetic type và geometric transformation |
| [VIDEO-34 redesign](VIDEO-34-REDESIGN.md) | Đề xuất S03/S08, bảng cue thực tế và kế hoạch bốn visual tests |
| [Codex implementation prompt](CODEX-VISUAL-TEST-PROMPT.md) | Prompt đầy đủ cho lượt triển khai keyframes sau này; dừng trước animation |
| [Global catalog](../../references/ANIMATION-STYLES.md) | Entry point ngắn, giữ IDs và compatibility |

Không cần nạp cả ba playbook vào mọi scene. Đọc shared contract cùng playbook chính; chỉ đọc phần bổ trợ khi thực sự dùng. Các bảng trong bộ tài liệu là recipe có thể điều chỉnh sau visual review, không phải luật số lớp, số nhân vật, easing hoặc palette toàn cục.

## Nhãn bằng chứng

- **[U] Upstream:** nội dung có thật ở commit `09e451d8b64ec85c1ec035fd39e00725c1ed5593`; không mặc định là best practice hay được cấp quyền tái sử dụng.
- **[L] Local:** file/source/trạng thái thật trong Flow Kit tại thời điểm kiểm toán.
- **[O] Output:** trực tiếp quan sát frame của clip đã encode; không đồng nghĩa đã xem toàn bộ playback hay human approval.
- **[A] Analysis:** suy luận thiết kế, chẩn đoán từ bằng chứng; có thể cần thử nghiệm để xác nhận.
- **[P] Proposal:** hướng dẫn hoặc thiết kế mới cho Flow Kit; chưa tạo output mới.

## Phạm vi và cách tiếp tục

Repo local không có Git metadata. Danh sách hash trước thay đổi ở [protected-before.json](evidence/protected-before.json); kết quả so sánh cuối ở [verification.json](evidence/verification.json). Chỉ thêm catalog, bộ tài liệu này và research cache trong `scratch/style-research-upstream/`. Không chạy setup, không cài package/engine, không gọi Google Flow, không chỉnh root AGENTS hay skills.

Prompt bàn giao **chưa được thực thi**. Lượt tiếp theo được giao prompt mới tạo bốn frame từ source dự kiến dùng lại cho pilot; người dùng duyệt Gate 1 trước khi authorize animation S03/S08. Gate 2 là review MP4 sau đó; không có ủy quyền sản xuất 15 cảnh còn lại trong nhiệm vụ này.
