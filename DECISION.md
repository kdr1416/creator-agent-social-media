# DECISION.md — Phase 0 và Phase 1, đã được Tuan duyệt ngày 03/11/2026

Repo: https://github.com/kdr1416/creator-agent-social-media
Nhánh làm việc: `chore/creator-cleanup`, đã tạo từ `main` commit `7f859b4`, commit Phase 0 và Phase 1 là `5debdd4`.
Main không bị sửa trực tiếp trong Phase 0 và Phase 1.

## 1. Renderer mặc định

- Mặc định cho video 2D giải thích, du học, cư trú, cảm xúc gia đình: **HyperFrames**.
- Remotion: chỉ cho series template tái sử dụng nhiều tập, dữ liệu thay đổi theo tập.
- Flow/Veo: chỉ làm plate sạch, không chữ, không số, không logo, khi cần bàn tay thật, diễn xuất thật, camera thật mà HyperFrames không diễn tả được. Toàn bộ chữ và đồ họa vẫn do HyperFrames phủ lên.
- Stock: chỉ làm plate. Không dùng stock để giải thích thủ tục, số tiền, điều kiện pháp lý.

## 2. Style kit mặc định cho đợt pilot

Thử song song trên cùng một scene, rồi chọn 1 làm mặc định:

- `crosshatch-clean`
- `sketchbook-fresh`

Style phụ, chỉ dùng khi routing gọi tên và ghi rõ lý do:

- `isometric` cho quy trình nhiều bước.
- `bauhaus` cho nguyên tắc và thông điệp mạnh.
- `kurzgesagt` cho giải thích ý tưởng lớn.

Một video chỉ khóa một style chính. Không đổi style giữa chừng chỉ vì một scene khó vẽ.

## 3. Luật skill

- Tối đa 6 skill đang hoạt động, có đúng 1 router đọc đầu tiên:
  1. `creator-router`
  2. `creator-scene-contract`
  3. `creator-style-kit`
  4. `creator-hyperframes-build`
  5. `creator-stock-plate`
  6. `creator-qa`
- Thêm 1 skill thì phải bỏ hoặc gộp 1 skill cũ.
- `skills/` là nguồn thật, `.agents/skills/` là bản sinh, không sửa tay bản sinh.
- Toàn bộ skill `fk-*` của Flow Kit chuyển vào `legacy/flowkit/` trong Phase 2, không còn trong luồng đang hoạt động.

## 4. Luật duyệt

- Pilot 1 scene khó và đại diện nhất, 10-20 giây, phải được duyệt bằng văn bản rõ ràng, ghi vào `production_status.json`.
- Nhận xét "tương đối ổn" không tính là duyệt.
- Thay đổi style, engine, rig, timing sau pilot thì phải duyệt lại pilot.
- Scene lỗi chỉ làm lại scene đó, tối đa 2 lần. Final assembly từ chối render cũ, render thiếu QA, render sai frame count, kích thước, FPS.
- Handoff giữa Antigravity và Codex bằng file, không bằng tin nhắn chat: `project_manifest.json`, `inputs/scene-manifest.json`, `creative/storyboard.md`, `creative/style-tokens.json`, `assets/ledger.json`, `production_status.json`.

## 5. Luật repo

- Output video, stock và audio master nặng không commit vào repo. Chỉ commit manifest, source, template, style kit và proof nhỏ của pilot.
- Video cũ chuyển ra khỏi `main` sau khi đã backup ngoài git. Trong Phase 0 và Phase 1, KHÔNG xóa video cũ, chỉ lập danh sách backup. Việc xóa chỉ làm sau khi Tuan xác nhận đã có backup.
- Không force-push, không xóa lịch sử. Tu sửa bằng commit mới trên nhánh riêng, có thể revert được.
- Không copy code AGPL-3.0 của OpenMontage vào repo MIT này khi chưa kiểm tra giấy phép. Chỉ tham khảo ý tưởng workflow và cổng duyệt.

## 6. Ghi chú về AGENTS.md

`.gitignore` cũ của repo có dòng `AGENTS.md`, vì file này trước đây được sinh tự động từ `setup.py`. Trong Phase 0, `AGENTS.md` trong gói này được commit thủ công làm điểm vào mới, và `.gitignore` mới đã bỏ dòng đó. Cho tới Phase 2, không chạy `setup.py sync` trên nhánh này, vì nó sẽ ghi đè AGENTS.md cũ. Phase 2 phải cập nhật `setup.py` trước rồi mới đồng bộ lại.
