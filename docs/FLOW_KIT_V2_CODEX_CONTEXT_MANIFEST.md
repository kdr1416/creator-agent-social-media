# FLOW KIT V2 — CODEX CONTEXT MANIFEST & READING GUIDE

- **Chức danh chuẩn bị:** Repository Documentation Auditor & AI Agent Context Specialist
- **Mục tiêu:** Cung cấp bản đồ điều hướng ngữ cảnh đầy đủ, chính xác và có thể kiểm chứng để Codex CLI tiếp nhận và triển khai thành công Phase A/B của Flow Kit V2.
- **Repository Root:** `D:\Nam 3\flowkit-main` (tương đương `D:\Năm 3\flowkit-main`)
- **Ngày chuẩn bị:** 2026-11-01

---

## A. ESSENTIAL ARCHITECTURE DOCUMENTS (BÁO CÁO BẮT BUỘC CODEX PHẢI ĐỌC)

Tất cả các báo cáo cốt lõi đã được lưu trữ trực tiếp trong thư mục `docs/` và root của repository để Codex có thể đọc trực tiếp bằng lệnh `read_file` mà không phụ thuộc vào môi trường ngoài:

1. **[`docs/architecture/FLOW_KIT_V2_IMPLEMENTATION_READINESS_REPORT.md`](file:///d:/Năm%203/flowkit-main/docs/architecture/FLOW_KIT_V2_IMPLEMENTATION_READINESS_REPORT.md)**  
   - *Vai trò:* **Kế hoạch triển khai chính thức (Action Plan)**.
   - *Nội dung trọng tâm:* Kiến trúc Codex-First, danh mục file cần sửa, danh mục file bảo tồn, tiêu chuẩn nghiệm thu pilot 15–20s, kế hoạch hồi quy (regression) và rollback.
   - *Vị trí gốc:* Artifact Antigravity (Đã sao chép an toàn vào `docs/architecture/`).

2. **[`docs/architecture/FLOW_KIT_V2_ARCHITECTURE_AND_SIMPLIFICATION_REPORT.md`](file:///d:/Năm%203/flowkit-main/docs/architecture/FLOW_KIT_V2_ARCHITECTURE_AND_SIMPLIFICATION_REPORT.md)**  
   - *Vai trò:* **Báo cáo kiến trúc nền tảng toàn diện**.
   - *Nội dung trọng tâm:* Bóc tách hiện trạng, khoảng trống chất lượng chuyển động, phân tầng kiến trúc 3 tầng, và hợp đồng bàn giao giữa các bên.
   - *Vị trí gốc:* Artifact Antigravity (Đã sao chép an toàn vào `docs/architecture/`).

3. **[`docs/EXTERNAL_REPOSITORIES_EVALUATION.md`](file:///d:/Năm%203/flowkit-main/docs/EXTERNAL_REPOSITORIES_EVALUATION.md)**  
   - *Vai trò:* **Bảng đánh giá sàng lọc 18 công nghệ**.
   - *Nội dung trọng tâm:* Lý do loại bỏ 10 repos (Three.js, Rapier, Anime.js, Motion Canvas...), xác lập Minimal Stack: HyperFrames + Remotion + GSAP 3 + FFmpeg.

4. **[`BAO_CAO_TOAN_DIEN_REVERSE_ENGINEERING.md`](file:///d:/Năm%203/flowkit-main/BAO_CAO_TOAN_DIEN_REVERSE_ENGINEERING.md)**  
   - *Vai trò:* **Báo cáo reverse-engineering hệ thống gốc**.
   - *Nội dung trọng tâm:* Cấu trúc backend FastAPI (`agent/`), Chrome Extension MV3 (`extension/`), SQLite database và hệ thống SPI.

---

## B. REQUIRED IMPLEMENTATION FILES (TỆP CẦN KIỂM TRA & SỬA ĐỔI TRONG PHASE A/B)

Những tệp này trực tiếp tham gia vào việc chuẩn hóa chỉ dẫn (Instruction Cleanup) và cấu trúc Template:

1. **[`setup.py`](file:///d:/Năm%203/flowkit-main/setup.py)** *(Single Source of Truth cho AGENTS.md)*
   - *Dòng 89-135:* Hàm `generate_antigravity(skills)` sinh `.agents/skills/fk-*/SKILL.md`.
   - *Dòng 151-180:* Biến `_CRITICAL_RULES` — cần cập nhật cấu trúc 5 khối, loại bỏ footer 180–200px tại dòng 172.
   - *Dòng 182-235:* Biến `_PIPELINE_OVERVIEW` — cần cập nhật quy trình Codex-First, loại bỏ footer 180-200px tại dòng 208.
   - *Dòng 274-278:* Hàm `generate_codex(skills)` sinh `AGENTS.md`.

2. **[`AGENTS.md`](file:///d:/Năm%203/flowkit-main/AGENTS.md)** *(Root Entry Point cho Codex CLI & Antigravity)*
   - *Dòng 1-171:* Tệp đầu ra sinh tự động từ `setup.py`. Cần tái cấu trúc thành 5 khối trách nhiệm (Global Rules ➔ Workflow Routing ➔ Engine Routing ➔ Creative Contracts ➔ Skill Discovery).

3. **[`references/ANIMATION-STYLES.md`](file:///d:/Năm%203/flowkit-main/references/ANIMATION-STYLES.md)**
   - *Dòng 92:* Chứa quy định cứng: *"Giữ footer phụ đề 180–200px trên canvas 720×1280"* ➔ Cần gỡ bỏ để giải phóng Full Canvas.

4. **[`skills/fk-edu-motion-explainer.md`](file:///d:/Năm%203/flowkit-main/skills/fk-edu-motion-explainer.md)** & thư mục con:
   - File chính dòng 43: Bỏ ràng buộc 180-200px.
   - [`skills/fk-edu-motion-explainer.references/visual-design.md`](file:///d:/Năm%203/flowkit-main/skills/fk-edu-motion-explainer.references/visual-design.md) dòng 14, 39: Bỏ Safe Area footer 180-200px.
   - [`skills/fk-edu-motion-explainer.references/motion-and-qa.md`](file:///d:/Năm%203/flowkit-main/skills/fk-edu-motion-explainer.references/motion-and-qa.md) dòng 19: Bỏ tiêu chí đánh trượt visual khi chạm đáy.

5. **[`skills/warm-doodle-video/SKILL.md`](file:///d:/Năm%203/flowkit-main/skills/warm-doodle-video/SKILL.md)**
   - *Dòng 69:* Bỏ yêu cầu chừa trống footer 180-200px.

---

## C. RELEVANT SKILLS & GUIDELINES (KHO CHỈ DẪN NGHIỆP VỤ)

1. **Core Video Skills:**
   - [`skills/fk-edu-motion-explainer.md`](file:///d:/Năm%203/flowkit-main/skills/fk-edu-motion-explainer.md): Hướng dẫn motion graphics giải thích giáo dục/thương mại.
   - [`skills/voice-to-scene-design/SKILL.md`](file:///d:/Năm%203/flowkit-main/skills/voice-to-scene-design/SKILL.md): Phương pháp chuyển voice transcript thành visual metaphor và staging.
   - [`.agents/skills/hyperframes-core/SKILL.md`](file:///d:/Năm%203/flowkit-main/.agents/skills/hyperframes-core/SKILL.md): Hợp đồng composition HyperFrames (data attributes, clips, seek-safe).
   - [`.agents/skills/hyperframes-animation/SKILL.md`](file:///d:/Năm%203/flowkit-main/.agents/skills/hyperframes-animation/SKILL.md): Kỹ thuật animate GSAP, eases, transitions.
   - [`.agents/skills/remotion-motion-director/SKILL.md`](file:///d:/Năm%203/flowkit-main/.agents/skills/remotion-motion-director/SKILL.md): Chỉ dẫn làm video React/Remotion.

---

## D. PRESERVE / READ-ONLY FILES (TỆP BẢO TỒN NGUYÊN VẸN 100%)

Codex **tuyệt đối không chỉnh sửa hoặc xóa** các thành phần sau:
1. **Dự án Lịch sử trong `videos/`:**
   - `videos/VIDEO-33/`, `videos/VIDEO-33-director-pilot/`, `videos/tran-minh-nhat-*`, `videos/le-pham-nhu-quynh-*`, `videos/china-education-*`.
2. **Hạ tầng Google Flow trong `agent/` và `extension/`:**
   - `agent/db/schema.py`, `agent/main.py`, `extension/hijack_bypass.js`, `flow_agent.db`.
3. **Môi trường Remotion & Demo:**
   - `remotion-project/` (chứa `Scene2.tsx` và React 19 dependencies).
   - `hyperframes-demo/`.
4. **Kho lưu trữ phân tích gốc:**
   - `repository-analysis/` (toàn bộ 14 file báo cáo Markdown).

---

## E. DECISIONS ALREADY APPROVED (QUYẾT ĐỊNH NGƯỜI DÙNG ĐÃ PHÊ DUYỆT CHÍNH THỨC)

Codex phải bám sát 10 quyết định đã được duyệt sau đây:

1. **Codex là Primary Video Production Agent:** Chịu trách nhiệm xuyên suốt từ kịch bản, visual, pilot, sản xuất hàng loạt các scene còn lại, render và final assembly.
2. **Antigravity phụ trách Audio Analysis & Support:** Cắt sample bounds `[start, end)`, xuất `scene-manifest.json`, hỗ trợ independent QA khi được yêu cầu.
3. **Mô hình Tiếp tục Sản xuất (Pilot Continuation):** Bãi bỏ việc viết prompt bàn giao phức tạp (`ANTIGRAVITY_PROMPT.md`). Sau khi Human duyệt pilot, Codex tiếp tục sản xuất các scene còn lại ngay trong thư mục dự án đó.
4. **Minimal Technology Baseline:** Giữ HyperFrames + GSAP 3 + FFmpeg; Remotion là conditional engine. Không tích hợp 10 repos dư thừa.
5. **Loại bỏ Hoàn toàn Subtitle Footer 180–200px Cố định:** 100% không gian canvas thuộc về Art Director và Animator. Subtitle chỉ bật khi có yêu cầu cụ thể.
6. **Không Áp Đặt Mascot Quota:** Tỷ lệ xuất hiện nhân vật (70–80%) và Anti-Card Law là Style-Specific hoặc Project-Specific, không bắt buộc cho mọi video.
7. **Bảo toàn Cấu trúc 5 Khối của `AGENTS.md`:** Global Rules ➔ Workflow Routing ➔ Engine Routing ➔ Creative Contracts ➔ Skill Discovery.
8. **Đồng bộ `setup.py`:** Cập nhật biến template trong `setup.py` để chạy sync không bị ghi đè mất quy chuẩn V2.
9. **Scene-level Isolation & Editability:** Mỗi scene là một module/subcomposition độc lập, có thể sửa lẻ và render preview nhanh.
10. **AV-Sync Chính xác:** Cắt sample bounds trên PCM gốc, ghép 30fps bằng FFmpeg và phủ master PCM audio từ t=0.

---

## F. UNRESOLVED QUESTIONS & CẦN CODEX KIỂM TRA TRONG PHASE A

1. **Kiểm tra tương thích ngược của `setup.py`:** Khi cập nhật `_CRITICAL_RULES` và `_PIPELINE_OVERVIEW`, cần chạy thử lệnh dry-run `python setup.py --tool codex` để kiểm tra output text có chuẩn xác không.
2. **Cấu hình Lossless cho SVGO:** Nếu dùng SVGO để dọn dẹp vector SVG trong tương lai, cần đảm bảo tắt các cờ `cleanupIDs`, `collapseGroups`, `convertTransform` để không làm gãy animation.
3. **Cấu hình Resolution Động:** Cần kiểm tra cách `HyperFrames` và `Remotion` đọc resolution từ `project_manifest.json` thay vì hardcode 720×1280.
