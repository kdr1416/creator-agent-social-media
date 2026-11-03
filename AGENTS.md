# AGENTS.md — Điểm vào mới, Phase 0 và Phase 1

Đọc theo thứ tự này, không đọc toàn bộ repo cũ trước:

1. `DECISION.md`
2. `docs/workflow.md` (trong plan, sẽ viết đầy đủ ở Phase 2)
3. `styles/README.md` và `styles/<style>/STYLE.md` của style đang làm
4. `projects/_template/` và `tools/codex_project.py`
5. Scene contract của scene đang làm
6. `production_status.json` của project đang làm

## Renderer

- Mặc định: HyperFrames.
- Remotion: chỉ cho series template.
- Flow/Veo và stock: chỉ làm plate sạch, không chữ, không số, không logo.

## Workflow bắt buộc

Brief và khóa style -> audio làm chủ timeline -> routing từng scene -> look frames -> storyboard panels -> character và asset library -> pilot -> batch -> assemble -> QA.

Pilot phải được người dùng duyệt bằng văn bản rõ ràng trước khi dựng hàng loạt. Nhận xét "tương đối ổn" không tính là duyệt.

## Luật scene contract

- Mỗi scene có 1 file JSON contract hợp lệ trước khi dựng.
- Mỗi scene có đúng 1 signature motion, 1 visual verb, text budget tối đa.
- Timeline liên tục, không chồng, không hở, tổng thời lượng khớp audio master.
- Scene lỗi chỉ làm lại scene đó, tối đa 2 lần.

## Luật skill và legacy

- Chỉ dùng tối đa 6 skill đang hoạt động, router đọc đầu tiên. Thêm 1 skill thì bỏ 1 skill cũ.
- Flow Kit cũ nằm ở `legacy/flowkit/` từ Phase 2 trở đi, không phải mặc định.
- Không chạy `setup.py sync` trên nhánh Phase 0 và Phase 1 cho tới khi Phase 2 cập nhật `setup.py`, vì nó sẽ ghi đè file này.
