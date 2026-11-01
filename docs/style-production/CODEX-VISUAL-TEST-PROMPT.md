# Codex prompt — VIDEO-34 four visual tests, STOP at Human Review

Prompt dưới đây dành cho **lượt triển khai được giao tiếp theo**. Nó chưa được thực thi trong nghiên cứu này. Copy toàn bộ phần sau vào chat làm visual tests. Research documents là đề xuất, không phải human approval. Không cần tạo agent hoặc engine mới.

---

Bạn làm việc tại `D:\Năm 3\flowkit-main`. Nhiệm vụ: tạo bốn visual test frames thực sự từ source artwork nguyên gốc dự kiến dùng trong pilot VIDEO-34, rồi dừng chờ **Human Review Gate 1 — Visual Art Direction**. Không animate/render MP4 ở lượt này, không tự sản xuất các scenes khác.

Đọc root AGENTS.md, `videos/video-34/project_manifest.json`, `production_status.json`, `creative/storyboard.md`, `creative/style-bible.md`, `creative/style-tokens.json`, `creative/revision-r1.md`, `build/pilot-working-config.json` trước. Kiểm tra nested instructions ở đường dẫn sẽ làm. Đọc HyperFrames entry/core/CLI và các capability skills cần thiết đang cài; giữ versions hiện có, không upgrade/install/sync/setup. Không gọi Google Flow service/provider/preflight cho công việc 2D này. Không cần subagents.

Đọc theo thứ tự:

1. `references/ANIMATION-STYLES.md`.
2. `docs/style-production/VIDEO-34-REDESIGN.md`.
3. `docs/style-production/SHARED-PRODUCTION.md`.
4. `docs/style-production/kurzgesagt.md`, phần spatial/hinge của `izometrik.md` và type integration của `bauhaus.md`.
5. `docs/style-production/RESEARCH-AUDIT.md` để hiểu giới hạn evidence và sự khác nhau giữa baseline/R1/static studies.

Nếu structural exploration cần thiết, dùng installed codebase-memory skill, kiểm coverage, rồi đọc source cho vùng missing/stale. Không dựa báo cáo cũ để kết luận file hiện diện. Root catalog đã được khôi phục bằng docs; các skills/generator chưa được sửa để tự động load playbooks.

Workspace có thay đổi đồng thời trong nghiên cứu: bản cuối đã sang Typography V2, vẫn pending. Đọc `build/type-pilot-delivery.json`, `components/type-design.py`, `components/type-motion.js` nếu còn là source hiện tại và latest review evidence. Một số quyết định typography đã được luồng khác ghi là người dùng yêu cầu; đối chiếu ngữ cảnh phê duyệt thực có khi resume và giữ các constraints đã xác nhận. Không rollback V2 về R1, không coi critique navy wash của R1 là lỗi V2, không ghi đè source mới bằng snapshot cũ trong prompt này. Proposal dưới đây cần thích nghi với latest authorized state.

**Bảo toàn trước khi làm:** kiểm Git status; nếu không có Git metadata như lượt nghiên cứu, tạo scoped backup/hash tại scratch cho mọi existing file dự định sửa. Không dùng destructive Git. Snapshot master, 17 intervals, raw transcript/ASR, logo, manifest/status, S03/S08 source/assets/components và MP4 hiện tại. Preserve lịch sử, không overwrite typography studies cũ hay chạy `build_pilot_art.py` để đè R1. Tạo một thư mục revision mới trong project, ví dụ `videos/video-34/creative/visual-tests-core-r2/`; nếu tên tồn tại chọn revision suffix mới. Chỉ author source/PNGs/evidence/review page trong revision đó. Giữ production source/render/manifest/status nguyên vẹn ở bước này.

Primary style là `kurzgesagt`: original rich vector illustration, purposeful human acting poses, expressive silhouettes. Spatial discipline của `izometrik` giúp architecture/desk/props có geometry nhất quán; không ép coastline lifestyle thành rigid isometric diagram. `bauhaus` hỗ trợ typography hierarchy/masks/graphic composition trong cùng palette và motion personality. Không bắt cả ba xuất hiện trong mọi frame, không chọn lại ba Core Styles.

Palette thử nghiệm: cool clean environment, deep navy ink, azure/turquoise sea, near-white light, warm limestone có cool shadows, controlled coral và sunlight accents. Đây là creative palette, không official Esora colors. Có thể sửa value relationships của R1 theo hình thật; không chỉ đổi HEX. Không paper wash/grain/vintage treatment ngoài brief. Không giant dark top overlay để cứu chữ. Original logo Esora giữ nguyên ratio/pixels/colors; không trace/recolor/morph hoặc đưa vào hai scene nếu chưa có yêu cầu mới. Không thêm CTA, watermark, subtitles, new narration, BGM/SFX, residence-rights claims. S13 vẫn factual review required.

Master giữ nguyên SHA256 `6b92d56bb90f3c4e702903d53d098d7c1765daf716879e8de60826a3110425c1`: 24kHz mono, 2,232,960 samples = 93.04s. Không sửa 17 intervals. S03 `[243986,458528)`, S08 `[966480,1101123)`. Working canvas 1080×1920/30 FPS, chưa là full-film approved configuration. Cumulative frame bounds S03 `[305,573)` và S08 `[1208,1376)`. Không thay manifest để phục vụ test.

**Build bốn frame sau từ cùng source construction có thể reuse trong pilot:**

| ID | Pose/layout cần thấy | Anchor chọn từ ASR thực tế | Frame capture zero-based |
|---|---|---|---|
| S03-A | Malta-inspired coastal environment, rõ limestone architecture/depth, một focal activity có silhouette chất lượng; không text | “đi bộ” bắt đầu global 10.50s | Global frame 315; local picture frame 10 = 0.333333s |
| S03-B | Cùng visual identity; café/hand-cup pose và keyword “Cà phê” tích hợp canopy hoặc negative space hợp lý | “cà phê” global 13.68s | Global frame 411; local picture frame 106 = 3.533333s |
| S08-A | Parent/child + workspace/terrace; anatomy, seat support, hand clearances, lid/base/hinge thiết kế riêng; không text | “cân bằng” global 42.14s | Global frame 1265; local picture frame 57 = 1.900000s |
| S08-B | Parent chuyển gaze và tương tác với child; contact pose rõ, emotional expression; “Gia đình” không che tay/mặt | Raw ASR “Giá đình” global 45.00s; corrected wording “Gia đình” | Global frame 1350; local picture frame 142 = 4.733333s |

Đây là static pose/layout tests gắn với cue: ghi `type_state=settled_layout_test`, không giả animation đã settle ngay ở onset. Không dùng still để khẳng định gait/hinge motion/voice sync đã pass. Local audio cue khác picture-local: S03 0.333917/3.513917s; S08 1.870000/4.730000s. Giữ cả hai trong evidence để không lệch convention. Word numbers 1-based lần lượt 46–47, 60–61, 174–175, 186–187 từ `inputs/word-timestamps.json`; không dùng chúng như zero-based indices. Không phát minh word timestamps mới. Chữ sửa sai tách khỏi raw ASR.

S03 requirements: thiết kế lại composition/focal hierarchy trước detail. Người nền không bắt viewer đọc mọi activity cùng lúc; walker/runner/café có pose/contour khác nhau, không thay áo cùng rig chống hông. Không tòa nhà khổng lồ + nhiều người quá nhỏ ở đáy. Use coherent surfaces và supporting local architecture, không gán một landmark có thật vào composite chưa kiểm chứng. Café type có thể theo một mặt vật liệu nếu readable; không bóp méo chữ để vừa.

S08 requirements: parent có pelvis/seat support và neck pivot rõ; child cùng family design nhưng proportions theo tuổi. Hand target, elbow, wrist, gaze cùng kể một action, không kéo dài cẳng tay để chạm. Laptop base/lid riêng, hinge vertices có ý nghĩa; không scaleY toàn laptop. Một frame chuẩn bị và một frame contact đủ để review visual quality, nhưng chưa chứng minh chuyển động giữa chúng. Giữ text ở vùng terrace/wall được thiết kế, không overlay vào face/hand/gaze path. Type có thể yên ở emotional payoff; không mặc định underline/arc/glow sau mọi từ.

Source delivery:

- Original editable SVG/HTML cùng scene components/pose-state definitions trong revision directory. Semantic IDs cho building, ground, actors, joints, hand/cup/lid/hinge và type wrappers; placement tách motion. Không dùng screenshots upstream, ảnh AI/moodboard hoặc screenshot studies cũ làm output mới. Có thể reuse asset/component local phù hợp có ghi provenance, nhưng phải cải thiện visual construction, không chỉ đổi text trên frame cũ.
- PNG full 1080×1920 và proof 360×640 cho mỗi ID; một contact sheet/review HTML có nhãn ID, pose/cue và revision.
- Dùng renderer/browser stack đang có. Ưu tiên HyperFrames snapshot/capture với source preview; kiểm `--help` của binary local cho args/version thay vì chạy npx có thể tải package. Nếu CLI snapshot không đáp ứng static pose, dùng existing browser capture đúng viewport và font readiness, ghi rõ phương pháp. Không install tool để làm test.
- Không author full animation timeline. Source có thể expose các layout/pose states thuần hoặc static composition entries riêng dùng chung asset functions; sau Gate 1 chúng trở thành đầu vào animation. Nếu dùng HyperFrames entry, tuân thủ root ID/duration/paused registration. Không auto-play clock, no rAF riêng, không Date.now/random unseeded. Repeated capture cùng pose phải deterministic trong cùng môi trường.
- Nếu cần một named graphic primitive, xem HyperFrames registry skill và tìm bằng local catalog trước hand-authoring; không gửi feedback ra ngoài hoặc install item/dependency ngoài phạm vi. Nếu không phù hợp, ghi ngắn lý do và dựng geometry nguyên gốc.

QA cần làm trước trình review:

1. Inspect cả bốn PNG thực tế bằng image-view tool ở full-size và mobile; ghi focus, value contrast, illustration richness, geometry và hand/face/text overlaps. Nếu chưa đẹp hoặc typography chưa đọc được, sửa trong test revision và capture lại.
2. Glyph check đủ dấu cho “Cà phê”, “Gia đình” và mọi text khác thật sự dùng; xác nhận font local tải đúng, provenance/rights có trong ledger revision. Đừng coi Latin-ext là bằng chứng đủ Vietnamese. Không phân phối font có quyền chưa rõ; có thể tham chiếu font local cho review trên máy và ghi limitation.
3. Grayscale/thumbnail để xem hierarchy; silhouette/pose check cho parent/child/hero; parallel edge/surface attachment cho architecture/desk/laptop; contact and occlusion ở pose thử.
4. Record source/assets/font hashes, capture params, exact pose/cue/frame, renderer/browser version, image dimensions và runtime/missing-request checks. Re-capture cùng pose từ fresh page và seek/pose-order khác, compare output nếu method cho phép. Không ghi “PASS” nếu chưa thực sự kiểm.
5. Rehash protected files và báo changed/missing. Nếu production source/MP4/master/manifest/intervals/logo vô tình thay đổi, dừng bàn giao để bảo toàn, điều tra và chỉ khôi phục file của chính lượt làm bằng backup; không revert unrelated user edits.

Tạo review-state riêng trong revision directory: `visual_review.status=pending`, reviewer/timestamp/evidence/revision hash chưa điền cho tới khi người dùng chấp thuận thật. Gate 1 approval nếu có phải ghi reviewer, timestamp, evidence và artifact revision được xem; nó chỉ khóa visual direction, không tự ghi `production_status.approval=approved` cho pilot/full film. Không giả phê duyệt từ im lặng hoặc kỹ thuật pass.

Kết quả cuối của lượt triển khai: hiển thị bốn frame và link source/review page, giải thích ngắn phân vai ba style, ghi checks đã làm/chưa làm và xin người dùng đánh giá màu/nhân vật/bố cục/depth/type. **Dừng tại Gate 1.** Nếu chưa đạt, sửa frames trước. Chỉ sau explicit visual approval mới bước sang animation S03/S08 theo timing thật, render hai MP4 rồi trình Gate 2. Không tự làm 15 scene còn lại dù pilot được duyệt trong một lượt sau, trừ khi người dùng ủy quyền full production rõ ràng.
