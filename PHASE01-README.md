# Phase 0 và Phase 1 — Gói đã làm xong, chưa đẩy lên GitHub

## Đã làm xong trong gói này

- Phase 0: `DECISION.md`, `AGENTS.md`, `.gitignore` mới.
- Phase 1: style kit `crosshatch-clean` và `sketchbook-fresh`, mỗi style có `STYLE.md`, `palette.json`, `typography.md`, `motion-rules.md`.
- Phase 1: project pilot `projects/esora-canada-pilot/` với `project_manifest.json`, `creative/storyboard.md`, `creative/look-frames.md`, `scenes/S08/scene-contract.json`, `scenes/S08/pilot.html`, `production_status.json`.
- Pilot HTML mở được trong trình duyệt, animation 6.2 giây, kèm 3 khung hình QA. Đây chưa phải MP4 render bằng HyperFrames CLI.

## Chưa làm, và vì sao

- Chưa tạo nhánh `chore/creator-cleanup` trên GitHub: đã thử tạo nhánh từ `main` (commit `7f859b4`) và nhận lỗi 403, GitHub App chưa được cài cho repo này. Tài khoản đã xác thực là `kdr1416`, nhưng quyền ghi qua App chưa có.
- Chưa xóa video cũ khỏi `main`: Phase 0 yêu cầu backup trước, và repo clone rất nặng vì video cũ, nên không xóa khi chưa có xác nhận backup.
- Chưa chuyển Flow Kit cũ vào `legacy/flowkit/`: đây là việc của Phase 2, cần làm sau khi nhánh Phase 0 và Phase 1 đã được duyệt và đưa lên GitHub.
- Chưa chạy `setup.py sync`: sẽ ghi đè `AGENTS.md` mới cho tới khi Phase 2 cập nhật `setup.py`.

## Cách đưa gói này lên GitHub

### Cách 1: Cài GitHub App rồi để Muse đẩy

1. Mở link cài đặt GitHub App của Muse, chọn repo `kdr1416/creator-agent-social-media`.
2. Báo lại trong chat là đã cài xong.
3. Muse sẽ tạo nhánh `chore/creator-cleanup` từ `main`, đưa các file trong gói này lên nhánh đó, không sửa `main` trực tiếp.

Link cài đặt: https://github.com/apps/meta-muse-ai/installations/new

### Cách 2: Tự đưa lên bằng tay, nếu không muốn cài App

1. Tạo nhánh `chore/creator-cleanup` từ `main` trên máy bạn.
2. Copy toàn bộ nội dung trong thư mục `phase01/` vào root của repo, giữ đúng cấu trúc thư mục.
3. Commit và push nhánh đó, mở PR vào `main` để duyệt, không merge trực tiếp.

## Cần Tuan duyệt tiếp

- Duyệt pilot HTML scene 8: bố cục, text budget, nhịp đặt vật thể có đạt không, hay cần sửa khung nào?
- Chọn style mặc định sau khi thử song song: crosshatch-clean hay sketchbook-fresh?
- Xác nhận đã backup video cũ chưa, trước khi làm bước xóa video cũ khỏi `main` ở Phase 2.
