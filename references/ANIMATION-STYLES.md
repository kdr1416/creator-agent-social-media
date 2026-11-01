# Flow Kit V2 — Core visual style catalog

Quyết định người dùng ngày 01/11/2026: ba phong cách chủ đạo mặc định là **Kurzgesagt-inspired, Isometric, Bauhaus**. Áp dụng cho quảng cáo, explainer và motion graphics phù hợp, không giới hạn video du học. Mỗi phim chọn một visual identity; không cần dùng đủ ba, không cần so lại style ở mọi scene. Explicit user requests có thể chọn cách diễn đạt khác.

| Style ID giữ nguyên | Nhãn | Vai trò gợi ý | Production playbook |
|---|---|---|---|
| `kurzgesagt` | 01 · Kurzgesagt-inspired | Original rich vector illustration, characters, environments, visual metaphors, narrative transformation | [Build recipe](../docs/style-production/kurzgesagt.md) |
| `izometrik` | 02 · İzometrik / Isometric | Spatial storytelling, architecture, places, systems and processes | [Build recipe](../docs/style-production/izometrik.md) |
| `bauhaus` | 03 · Bauhaus-inspired | Bold composition, kinetic type, highlights, geometry and graphic transitions | [Build recipe](../docs/style-production/bauhaus.md) |
| `hf_existing:<treatment>` | Existing HyperFrames treatment | Compatibility và yêu cầu đặc biệt; ghi treatment thực tế | Đọc workflow/registry phù hợp; không thay thế ba Core Styles |

Đọc [shared contracts](../docs/style-production/SHARED-PRODUCTION.md) và playbook primary. Secondary treatment là tùy chọn, giữ palette roles, typography, proportions và motion personality của project. Style không khóa renderer; dùng engine đang có theo capability. Không mặc định Flow generation, fixed footer, subtitles, mascot quota, layer quota hoặc easing preset.

Nguồn tham khảo đã xác minh: [animasyon-stil-katalogu](https://github.com/yasinozmeen/animasyon-stil-katalogu/tree/09e451d8b64ec85c1ec035fd39e00725c1ed5593). Đây là demo Canvas và clip tham khảo, không phải engine mới hay production template. Artwork phải nguyên gốc; không sao chép mascot/logo/layout nhận diện. Chưa xác minh quyền phân phối lại source/media của upstream.

[Research, inventory, evidence và limits](../docs/style-production/RESEARCH-AUDIT.md) · [VIDEO-34 proposal](../docs/style-production/VIDEO-34-REDESIGN.md) · [Visual-test prompt](../docs/style-production/CODEX-VISUAL-TEST-PROMPT.md).
