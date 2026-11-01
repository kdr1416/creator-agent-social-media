# REPOSITORY REVERSE ENGINEERING REPORT INDEX

Toàn bộ báo cáo phân tích kiến trúc chuyên sâu đã được tổng hợp và xuất bản:

- **Báo cáo tổng hợp toàn diện (Single Master Report):** [BAO_CAO_TOAN_DIEN_REVERSE_ENGINEERING.md](file:///d:/Năm%203/flowkit-main/BAO_CAO_TOAN_DIEN_REVERSE_ENGINEERING.md)

---

## Chi tiết từng chuyên đề (Modular Analysis Chapters):

1. [00-executive-summary.md](file:///d:/Năm%203/flowkit-main/repository-analysis/00-executive-summary.md) — Tóm tắt chiến lược, số liệu & phát hiện cốt lõi
2. [01-repository-inventory.md](file:///d:/Năm%203/flowkit-main/repository-analysis/01-repository-inventory.md) — Khảo sát toàn bộ cây thư mục, modules & entry points
3. [02-technology-stack.md](file:///d:/Năm%203/flowkit-main/repository-analysis/02-technology-stack.md) — Runtime Python, JavaScript MV3, React Vite & Dependencies
4. [03-system-architecture.md](file:///d:/Năm%203/flowkit-main/repository-analysis/03-system-architecture.md) — Kiến trúc hệ thống, các tầng, coupling & boundaries
5. [04-module-deep-dive.md](file:///d:/Năm%203/flowkit-main/repository-analysis/04-module-deep-dive.md) — Phân tích chi tiết 7 module cốt lõi & responsibilities
6. [05-end-to-end-workflows.md](file:///d:/Năm%203/flowkit-main/repository-analysis/05-end-to-end-workflows.md) — 5 Workflows E2E kèm sequence diagrams & bảng truy vết
7. [06-data-architecture.md](file:///d:/Năm%203/flowkit-main/repository-analysis/06-data-architecture.md) — SQLite DDL, WAL mode, State machines & ER Diagram
8. [07-api-and-integrations.md](file:///d:/Năm%203/flowkit-main/repository-analysis/07-api-and-integrations.md) — 14 REST Routers, WebSocket protocols & third-parties
9. [08-execution-and-deployment.md](file:///d:/Năm%203/flowkit-main/repository-analysis/08-execution-and-deployment.md) — Vòng đời khởi chạy, Chrome extension setup & troubleshooting
10. [09-testing-and-quality.md](file:///d:/Năm%203/flowkit-main/repository-analysis/09-testing-and-quality.md) — 27 bộ unit test, fixtures & quality gates
11. [10-git-history-and-decisions.md](file:///d:/Năm%203/flowkit-main/repository-analysis/10-git-history-and-decisions.md) — Tiến hóa kiến trúc (REST -> batchexecute, anti-hijack trap)
12. [11-customization-guide.md](file:///d:/Năm%203/flowkit-main/repository-analysis/11-customization-guide.md) — Hướng dẫn tùy biến & mở rộng provider/model/style/audio
13. [12-impact-analysis.md](file:///d:/Năm%203/flowkit-main/repository-analysis/12-impact-analysis.md) — Ma trận ảnh hưởng, breaking change scenarios & checklist
14. [13-glossary.md](file:///d:/Năm%203/flowkit-main/repository-analysis/13-glossary.md) — Thuật ngữ chuyên sâu & danh mục Google Flow RPC IDs

---

## Thư mục Sơ đồ Mermaid Độc lập:
- [diagrams/system-architecture.mmd](file:///d:/Năm%203/flowkit-main/repository-analysis/diagrams/system-architecture.mmd)
- [diagrams/module-dependencies.mmd](file:///d:/Năm%203/flowkit-main/repository-analysis/diagrams/module-dependencies.mmd)
- [diagrams/main-workflows.mmd](file:///d:/Năm%203/flowkit-main/repository-analysis/diagrams/main-workflows.mmd)
- [diagrams/data-model.mmd](file:///d:/Năm%203/flowkit-main/repository-analysis/diagrams/data-model.mmd)
