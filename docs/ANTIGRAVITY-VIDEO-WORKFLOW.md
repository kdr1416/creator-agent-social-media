# Pipeline phối hợp Antigravity → Codex → Antigravity

## 1. Mục đích và phạm vi

Phân công đã chốt: **Antigravity phân tích và chia audio; Codex nghiên cứu, lập routing/storyboard và dựng pilot; Antigravity dựng các cảnh còn lại, QA và ghép phim.** Người dùng chuyển giao file giữa hai công cụ trong cùng workspace; không tự gửi tin nhắn giữa chat. Dùng cho video du học/giáo dục và các chủ đề đã có transcript. Giữ nguyên pipeline engine; bộ phong cách chỉ bổ sung khả năng lựa chọn trong HF_ONLY.

Người dùng ngày 17/10/2026 nhận xét phong cách pilot scene_04 tương đối ổn. Đây là tham chiếu thị giác có thể tiếp tục cải thiện, không phải lệnh sao chép bố cục hoặc duyệt toàn bộ phim.

### Nguồn hướng dẫn

Đường dẫn trong tài liệu tính từ thư mục gốc project:

1. `AGENTS.md`: quy tắc chung và API.
2. `references/ANIMATION-STYLES.md`: chính sách lựa chọn phong cách.
3. `skills/fk-edu-motion-explainer.md`: workflow giải thích và các reference của giai đoạn đang làm.
4. `.agents/skills/hyperframes/SKILL.md`: điểm vào dựng bằng HyperFrames; core/animation/creative/CLI đọc khi cần.
5. Brief, routing, storyboard và trạng thái của video đang làm.

Chỉ dẫn trực tiếp của người dùng có ưu tiên cao hơn. Không đọc lại toàn bộ kho skills mỗi bước. `.agents/skills/fk-edu-motion-explainer/SKILL.md` là bản Antigravity đã sinh; nếu khác nguồn `skills/`, đồng bộ bằng setup thay vì sửa tay bản sinh. `AGENTS.md` cũng được sinh từ `setup.py`.

## 2. Chuỗi công việc

**Antigravity: audio + transcript + slices → Codex: fact-check + routing + style + storyboard + pilot → người dùng duyệt → Antigravity: cảnh còn lại + QA + ghép phim.**

Không gọi sinh ảnh/video cho toàn bộ cảnh ngay sau khi đọc transcript. Không coi một lệnh `fk-pipeline` là đủ để dựng phim có ba nhánh engine: phải kiểm tra cách orchestrator xử lý routing trước, chỉ gửi request Flow cho cảnh cần Flow.

| Giai đoạn | Chủ trì | Công việc | Đầu ra / điều kiện bàn giao |
|---|---|---|---|
| A. Audio | Antigravity | Kiểm tra WAV, phiên âm, chia lát theo ý nghĩa, giữ toàn bộ audio | Transcript JSON/MD, WAV từng cảnh, `audio_handoff.json`; timing liên tục, sample totals/hash được xác minh |
| B. Kế hoạch | Codex | Kiểm tra đầu vào, nghiên cứu dữ kiện, corrected_text riêng, khóa engine rồi đánh giá style HF_ONLY | Routing JSON/MD, storyboard chi tiết, ghi điểm dữ kiện cần duyệt; không sửa raw/audio |
| C. Pilot | Codex | Chọn một cảnh, dựng/render/QA rồi sửa theo phản hồi | Source sửa được, MP4, proof, QA; ghi thiết kế và cấu trúc rig tham chiếu |
| D. Duyệt/chuyển giao | Người dùng + Codex | Chốt bản pilot dùng làm chuẩn và các điểm cần giữ | `render_handoff.json`; không coi nhận xét “tương đối ổn” là lệnh dựng cả phim |
| E. Cảnh còn lại | Antigravity | Kiểm tra handoff, tạo asset và dựng theo mode/style đã khóa | MP4 từng cảnh, QA từng cảnh, cập nhật `production_status.json` |
| F. Ghép/nghiệm thu | Antigravity + người dùng | Ghép audio liên tục, kiểm tra chuyển cảnh/mobile/âm thanh | Final MP4 và báo cáo; người dùng đánh giá bản cuối |

Antigravity ở giai đoạn A không tự lập storyboard hoặc dựng cảnh. Codex ở giai đoạn B/C chỉ dựng pilot được giao. Antigravity ở giai đoạn E được sửa lỗi triển khai để đạt kế hoạch; nếu phải đổi nội dung, engine hoặc ý đồ chủ đạo, ghi đề xuất override và chờ quyết định thay vì tự viết lại kế hoạch.

Không gọi sinh ảnh/video cho toàn bộ cảnh ngay sau transcript. `fk-pipeline` không thay thế việc đọc routing; chỉ gửi request Flow cho cảnh cần Flow. Không hỏi lại các quyết định đã được chốt.

## 3. Hai lớp quyết định phải tách riêng

### Lớp A — Engine

- `HF_ONLY`: sự thay đổi của minh họa/sơ đồ/dữ liệu/lớp đồ họa mang phần lớn ý nghĩa.
- `FLOW_ONLY`: diễn xuất, tiếp xúc vật lý, môi trường hoặc camera chân thực mang phần lớn ý; không cần đồ họa chính xác.
- `HYBRID`: hành động hữu cơ mang ý chính, thêm một callout/metric chính xác để làm rõ.

Không chọn HF_ONLY chỉ vì muốn dùng Kurzgesagt. Chữ hoặc số xuất hiện không tự quyết định engine. Nếu đổi mode sau khi khóa, ghi `previous_mode`, `new_mode`, `routing_override_reason`.

### Lớp B — Phong cách trong HF_ONLY

Tập lựa chọn gồm treatment HyperFrames hiện có + Kurzgesagt + Isometric + Bauhaus. HyperFrames là framework, không phải một style duy nhất.

Mỗi cảnh HF_ONLY so sánh ít nhất hai ứng viên, gồm Kurzgesagt; ghi nhận xét ngắn thay vì tự bịa điểm số. Đánh giá theo mục tiêu giải thích, hình/asset, signature motion, mobile và độ liền mạch. Kurzgesagt được ưu tiên khi các lựa chọn phù hợp tương đương; chọn phong cách khác khi diễn giải tốt hơn.

Không ép đủ ba style, không quota, không thay style theo từng câu. Giữ bảng màu, font và nhân vật chung. FLOW_ONLY/HYBRID giữ hợp đồng footage riêng, không ép theo style minh họa của HF_ONLY.

## 4. Hồ sơ và bộ nhớ công việc

### Đầu vào chuẩn

```text
scratch/voice_transcript.json
scratch/voice_transcript.md
scratch/audio_slices/scene_01.wav ... scene_NN.wav
```

Giữ nguyên ID tương ứng audio. Không chia lại hoặc gộp audio tùy ý. Chữ đã sửa ASR không đồng nghĩa audio đã được thu lại; các beat bên trong cảnh cần nghe/align trước khi dựng.

### Đầu ra chuẩn

```text
scratch/scene_routing.json
scratch/scene_routing.md
scratch/storyboard.md
scratch/production_status.json
scratch/audio_handoff.json
scratch/render_handoff.json
videos/<project-slug>/
  BRIEF.md
  frame.md hoặc design.md
  hyperframes.json
  package.json
  index.html và các composition
  assets/
  qa/
  renders/
output/<project-slug>/scene_NN.mp4
output/<project-slug>/final.mp4
```

Kế hoạch phải ghi `project_slug` và nguồn transcript để không tiếp tục nhầm video cũ. Trước khi chuyển video, lưu kế hoạch cũ vào `scratch/archive/`. Không xóa media cũ hoặc reset project chỉ để bắt đầu video mới.

`production_status.json` là sổ trạng thái, không là công cụ tự chạy. Tạo khi bắt đầu sản xuất, cập nhật sau mỗi mốc thật:

```json
{
  "project_slug": "your-project",
  "stage": "pilot_review",
  "routing_file": "scratch/scene_routing.json",
  "storyboard_file": "scratch/storyboard.md",
  "pilot_scene": "scene_04",
  "scenes": {
    "scene_04": {
      "mode": "HF_ONLY",
      "style": "kurzgesagt",
      "status": "rendered_awaiting_feedback",
      "source_project": "videos/your-project",
      "output": "output/your-project/scene_04.mp4",
      "qa_report": "videos/your-project/qa/review.json"
    }
  },
  "next_action": "Collect pilot feedback before expanding production."
}
```

Các status gợi ý: `planned`, `assets_ready`, `built`, `qa_failed`, `rendered_awaiting_feedback`, `accepted`. Chỉ dùng `accepted` khi có phản hồi phù hợp của người dùng. Không đánh dấu asset tồn tại chỉ vì đã ghi tên trong storyboard.

### Hai gói bàn giao

**Antigravity → Codex: `scratch/audio_handoff.json`**

Ghi `project_slug`, `source_audio`, `source_audio_sha256`, `sample_rate`, `channels`, `total_sample_frames`, `total_duration`, đường dẫn transcript JSON/MD và danh sách scene. Mỗi scene có ID, đường dẫn WAV, `start_sample`, `end_sample`, số sample thực, thời lượng và hash file. Ghi ASR uncertainty riêng; không tự xác nhận tên trường/chính sách là đúng. Tính ranh giới bằng sample nguyên để không mất/lặp audio.

**Codex → Antigravity: `scratch/render_handoff.json`**

Ghi `project_slug`, nguồn audio handoff, đường dẫn/hash routing và storyboard, thiết kế chung, `pilot_scene`, source project/index, MP4, QA, phản hồi người dùng, phiên bản pilot được chọn, `scenes_to_build`, `scope_authorized` và `open_issues`. Mỗi cảnh chỉ rõ WAV, engine/style, asset contract và đường dẫn output. Chuyển giao source/asset/font/audio/GSAP local cùng MP4; chỉ có MP4 thì chưa đủ để tái sử dụng rig.

Nếu có điểm cần xác minh ảnh hưởng trực tiếp tới cảnh, ghi `production_hold` cho cảnh đó. Antigravity có thể làm cảnh khác đã được phép; không xuất final như thể mọi dữ kiện đã đạt. Hash mismatch phải được đối chiếu để tránh dùng kế hoạch cũ; không tự bỏ qua hoặc ghi hash mới cho khớp.

`production_status.json` giữ tiến độ thay đổi; routing/storyboard/handoff giữ quyết định đã chốt. Khi có sửa kế hoạch được chấp thuận, tạo phiên bản bàn giao mới, ghi thay đổi và cập nhật hash tương ứng.

## 5. Hợp đồng dựng từng nhánh

### HF_ONLY

1. Đọc cảnh đã khóa và các quy tắc HyperFrames cần thiết.
2. Xem source/tham chiếu style; tìm registry trước khi tự viết named effect. Kết quả không phù hợp thì tạo asset riêng, ghi lý do.
3. Liệt kê và tạo từng lớp cần điều khiển: thân/đầu/tay nhân vật, đạo cụ, đường nối, cảm biến, bóng…
4. Copy audio đúng cảnh, không sinh TTS thay thế. Xây một timeline seek được; không đồng hồ riêng hoặc network khi render.
5. Hành động phải chứng minh ý của lời đọc: tay cắm đầu nối → tín hiệu đi theo dây → mô hình phản hồi. Fade/slide không đủ làm signature.
6. Chạy check, lấy proof, sửa hình thực sự nếu chưa đạt rồi render MP4.

### FLOW_ONLY

1. Health/provider phải sẵn sàng trước sinh media. Có material và reference UUID cần thiết trước scene image.
2. Prompt mô tả hành động vật lý, dùng timing sub-clip; zero text/numbers/letters/logos/badges.
3. Gửi qua batch, không script vòng lặp API hoặc tự stagger.
4. Review light; scene dưới 7.5 sửa prompt theo lỗi, tối đa hai chu kỳ review-regen.
5. Kiểm tra thời lượng thực. Chỉ trim/retime phần hình khi hợp lý để vừa audio, giữ voice gốc; không kéo giãn voice để khớp footage.

### HYBRID

1. Thực hiện reference/batch/review như Flow.
2. Plate có 40–50% negative space được hoạch định, camera ổn định, zero text.
3. Xem footage rồi mới chốt timing overlay; không giả định lúc đặt vật theo prompt là timing thực.
4. HF chỉ thêm pointer nổi hoặc bare metric trong vùng trống; tối đa một datum/keyword dưới 5 từ, không boxed cards.

## 6. QA bắt buộc, có bằng chứng

### Kỹ thuật

- Dùng CLI pin trong `package.json` của project; kiểm tra version theo skill khi tiếp tục project cũ. Không nâng phiên bản hàng loạt các video không liên quan.
- `check` phải thực sự chạy runtime/layout/contrast; kết quả 0 sample không phải pass hình ảnh.
- MP4 phải tồn tại, có video/audio, đúng kích thước và lệch thời lượng không quá 0.05s so với WAV. 30fps có thể làm tròn tới một frame; ghi sai số.
- Kiểm tra audio không im lặng, không clipping, không thiếu đầu/cuối. Copy WAV trước encode phải giống nguồn.

Ví dụ trong thư mục project HyperFrames đã có:

```powershell
npm run check
npm run render -- --output renders/scene_04.mp4 --fps 30 --quality delivery
```

Dùng lệnh snapshot/preview đúng schema của CLI đang cài. Khi chia sẻ Studio, mở server nền, kiểm tra HTTP 200 và dùng URL có `#project/<project-name>`. Không đưa link server đã tắt.

### Thị giác

- Xem opening, signature-motion-in-progress và final; không chọn toàn frame đã đứng yên.
- Xem playback; contact sheet chỉ bổ sung, không thay thế việc đánh giá nhịp toàn clip. Nếu chỉ xem frame, ghi rõ giới hạn đó.
- Kiểm tra 360×640, thumbnail và grayscale.
- Tay phải chạm vật, chuyển động phải gây thay đổi có nghĩa; nhân vật không đứng trang trí. Kiểm tra thứ tự lớp ở mọi pose: tay xa sau thân, tay gần trước thân; không dùng opacity để giả che khuất.
- Không generic cards/pills, chữ như transcript, nhãn trùng lặp hoặc naked digit circles.
- Không upper-only, không đè footer 180–200px, không khối tối dính nhau.
- So sánh các cảnh lân cận, sửa nếu lặp bố cục hoặc hiệu ứng mà không có lý do nội dung.
- Không tuyên bố giống phong cách chỉ vì dùng palette gần nhau; phải có hệ minh họa/lớp hình/choreography phù hợp.

## 7. Prompt dùng theo đúng công cụ

Thay thông tin trong ngoặc vuông; chạy trong cùng workspace FlowKit. Mỗi prompt chỉ cấp phạm vi của giai đoạn đó.

### A. Gửi Antigravity — phân tích audio mới

```text
Bắt đầu project [slug] từ input_voice/[file-audio].
Đọc docs/ANTIGRAVITY-VIDEO-WORKFLOW.md và AGENTS.md.
Bạn phụ trách giai đoạn audio, không lập storyboard hoặc dựng video.

Archive transcript/slices/kế hoạch/status/handoff cũ nếu thuộc project khác;
giữ nguyên source/output cũ. Kiểm tra audio thật rồi phiên âm và chia lát
theo ý nghĩa, không cắt giữa từ, không làm mất hoặc lặp sample.

Tạo scratch/voice_transcript.json, voice_transcript.md và audio_slices/scene_NN.wav.
Mỗi record có ID, raw_text, start/end sample, start/end giây, duration, audio_slice.
Chữ sửa ASR ghi riêng; chỗ nghe không chắc ghi uncertainty, không đoán tên riêng.
Tạo scratch/audio_handoff.json có project_slug, hash nguồn, sample metadata,
danh sách lát/hash và kết quả kiểm tra contiguity/PCM nối lại.

Giữ nguyên audio gốc. Dừng khi đủ file bàn giao cho Codex;
báo tổng thời lượng, số cảnh và những chỗ ASR chưa chắc. Chưa sinh media.
```

### B. Gửi Codex — lập kế hoạch và dựng pilot

```text
Tiếp nhận project [slug] từ scratch/audio_handoff.json.
Đọc docs/ANTIGRAVITY-VIDEO-WORKFLOW.md, AGENTS.md và tài liệu phong cách.
Kiểm tra hash, audio slices và transcript trước khi dùng; giữ nguyên raw/audio/timing.

Nghiên cứu dữ kiện, tạo corrected_text và ghi điểm chưa xác minh riêng.
Lập scratch/scene_routing.json, scene_routing.md và storyboard.md cho toàn phim.
Khóa HF_ONLY/FLOW_ONLY/HYBRID trước; chỉ sau đó đánh giá style cho HF_ONLY:
giữ treatment HyperFrames hiện có cùng Kurzgesagt/Isometric/Bauhaus,
ưu tiên Kurzgesagt khi phù hợp, không bắt buộc.

Mỗi cảnh đủ schema: visual action, hành động nhân vật, beat, asset contract,
text budget, bố cục, signature motion và lý do engine/style.
Chọn một cảnh đại diện có lý do, rồi dựng riêng cảnh đó tới MP4 có audio và QA.
Dùng project riêng videos/[slug]-pilot/; không dựng cả phim ở lượt này.

Gửi pilot để mình phản hồi. Cập nhật production_status.json và chuẩn bị
render_handoff.json cho Antigravity: source sửa được, asset/font/rig,
thiết kế chung, bản pilot, routing/storyboard, QA và vấn đề còn mở.
Không đánh dấu đã duyệt hoặc được phép dựng cả phim trước phản hồi của mình.
```

Nếu muốn xem kế hoạch trước khi Codex dựng, thêm: “Lượt này chỉ lập routing/storyboard và đề xuất pilot; đợi mình giao dựng”.

### C. Gửi Codex — chốt/sửa pilot và đóng gói bàn giao

```text
Project [slug], pilot [scene_ID].
Phản hồi: [điểm giữ lại / lỗi cần sửa].
Sửa và render lại pilot nếu cần; giữ audio, engine và nội dung đã chốt.
Cập nhật QA, bản source/MP4 mới và render_handoff.json.
Ghi rõ thiết kế dùng chung, thứ tự lớp rig, điều nên tái sử dụng và phần
phải thiết kế riêng từng cảnh. Nếu bản sửa cần mình duyệt, ghi pending_review.
Không tự dựng các cảnh còn lại.
```

### D. Gửi Antigravity — dựng các cảnh còn lại và ghép phim

```text
Project [slug]. Mình duyệt pilot [scene_ID / phiên bản] với các điểm giữ:
[nhân vật, palette, nét vẽ, chiều sâu, nhịp...]. Các điểm cần chỉnh: [nếu có].
Cho phép bạn dựng các cảnh còn lại và ghép final.

Đọc docs/ANTIGRAVITY-VIDEO-WORKFLOW.md, scratch/render_handoff.json,
production_status.json, routing, storyboard và source/QA pilot của Codex.
Kiểm tra đúng project/hash và những cảnh production_hold trước khi làm.

Giữ raw/audio/timing và mode/style đã khóa. Dùng lại rig/asset/font/palette
phù hợp, nhưng action/layout phục vụ từng nội dung; không copy toàn cảnh pilot.
Rig phải đúng chiều sâu: tay phía xa sau thân, tay phía gần trước thân;
tay/prop có tiếp xúc và occlusion hợp lý trong toàn bộ chuyển động.
Chỉ sinh Flow cho FLOW_ONLY/HYBRID; HF_ONLY dựng bằng HyperFrames.
Thiếu asset thì tạo/source đúng contract, không fallback thành card.
Nếu cần thay đổi engine/nội dung/ý đồ chủ đạo, ghi đề xuất override để mình chốt.

QA và xuất MP4 từng cảnh, cập nhật production_status.json theo kết quả thật.
Sau khi các cảnh được phép đều đạt và không còn hold ảnh hưởng final,
ghép phim, kiểm tra audio liên tục, thời lượng, chuyển cảnh và mobile.
Gửi final.mp4 và báo cáo ngắn; ghi rõ những kiểm tra chưa thực hiện.
```

### E. Tiếp tục trong chat mới

```text
Tiếp tục project [slug], vai trò của bạn là [Antigravity xử lý audio /
Codex kế hoạch+pilot / Antigravity sản xuất].
Đọc workflow và handoff/status đúng giai đoạn; đối chiếu file thực tế.
Báo gọn phần đã xong và next_action, rồi tiếp tục trong phạm vi đã được phép.
Không làm lại scene đã xong hoặc dùng kế hoạch của video khác.
```

## 8. Mốc hiện tại của video đang làm

- Routing/storyboard: 12 cảnh, 69.880s, chủ đề đào tạo kỹ thuật tại một số học viện quân sự Trung Quốc.
- Pilot đã render: `scene_04`, HF_ONLY, Kurzgesagt, 5.033333s ở 30fps; audio nguồn 5.026s.
- Source: `videos/china-education-scene-04/index.html`.
- QA: `videos/china-education-scene-04/qa/review.json`.
- MP4: `output/china-military-education-ai-2026/scene_04.mp4`.
- Phản hồi: phong cách tương đối ổn. Chưa có chỉ thị dựng cả 11 cảnh còn lại.
- Pilot v2 đã sửa occlusion tay xa; `scene_04_v2.mp4` và QA mới sẵn sàng. Chờ đánh giá v2 trước chốt bàn giao sản xuất.
- Không mặc định preview port 3014 còn hoạt động trong phiên khác; kiểm tra hoặc mở lại.

Đây là hướng dẫn thao tác và hợp đồng file, chưa phải phần mềm tự động hóa mới hoặc nút bấm trên dashboard.
