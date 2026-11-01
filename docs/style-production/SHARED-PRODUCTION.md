# Shared production: style composition, voice, effects & QA

Toàn bộ recipe mới dưới đây là **[P]**; nguồn kỹ thuật và quan sát upstream nằm trong [audit](RESEARCH-AUDIT.md). Không xem những con số thử nghiệm là mặc định của mọi project.

## 1. Routing đơn giản, identity thống nhất

Chọn project-level primary style trước; dùng secondary treatment để giải quyết một việc cụ thể. Scene có thể có creative exception với lý do, nhưng palette roles, typography, figure family và motion personality vẫn thuộc project. Renderer chọn độc lập theo capability; cả ba style đều có thể dựng SVG/HTML với GSAP hoặc React/frame functions khi phù hợp. `hf_existing:<treatment>` giữ nguyên để tương thích và yêu cầu riêng, không thay thế Core Styles.

| Tình huống | Phân vai | Điểm phải khóa ở visual review |
|---|---|---|
| Một style | Character explainer → kurzgesagt; spatial process → izometrik; brand message → bauhaus | Cách thể hiện phù hợp nội dung, không cần thêm style để đủ bộ |
| Hai style | Illustration + Bauhaus type; iso world + graphic labels; illustrated characters trong spatial environment | Type dùng cùng palette/roundness và vùng trống; figures phải cùng projection với nền ở nơi tiếp xúc |
| Cả ba | Primary illustrated narrative; một số cảnh spatial; type/transition cùng ngữ pháp đồ họa | Chuyển vai theo beat/scene; không đặt rigid diagram, expressive close-up và huge type cùng tranh ưu tiên |
| Exception | Một technical diagram cụ thể có treatment khác | Ghi điều thay đổi, lý do, điểm continuity được giữ; đổi approved constraints thì review lại |

Một record nhỏ trong project art direction là đủ (đề xuất nội dung, không thêm schema runtime):

```json
{
  "primary_style": "kurzgesagt",
  "secondary_treatments": ["izometrik:architecture", "bauhaus:keyword_composition"],
  "palette_roles": "project-owned",
  "character_language": "project-owned pose sheet",
  "typography": "project-owned licensed local font with Vietnamese coverage",
  "motion_personality": "illustrated acting; restrained graphic handoffs",
  "voice_highlights": "selective; no subtitles",
  "scene_exceptions": [],
  "review": {"status": "proposed", "reviewer": null, "evidence": null}
}
```

Identity lock kiểm: cùng role của accent, cùng cách xử lý bóng/viền, cùng figure proportions theo độ tuổi, cùng type weight/line spacing và motif chuyển tiếp. Không chỉ giữ HEX rồi đổi toàn bộ texture, lens và easing. Một motif có thể lặp khi nó giữ ý nghĩa; không ép mỗi cue một effect mới.

Illustration → typography: lấy cạnh mái hiên, đường bờ biển hoặc shape của prop làm điểm neo; giảm hoạt động phụ trong lúc type nhận focus; giữ một màu/vật thể qua cut. Typography → illustration: thu shape về prop hoặc dùng mask để mở bối cảnh mới; text đã đọc xong rời đi trước lúc diễn xuất cần mắt người xem. Không làm camera giật chỉ để đồng bộ mọi âm tiết.

## 2. Voice-to-visual cue contract

1. Đọc câu và chọn phần ý nghĩa mà hình khó truyền đạt một mình: tương phản, từ khóa, kết luận hoặc tên cần nhớ. Bỏ keyword nếu hình đã đủ rõ hoặc không có thời gian đọc. Không tự chọn mọi danh từ.
2. Lấy word start/end từ file timestamp bất biến; lưu `word_number_1based` hoặc `word_index_0based` rõ tên. `corrected_text` thay chữ sai riêng, không phát minh alignment cho chữ mới. Một phrase có thể bao gồm vài ASR tokens.
3. Ghi ba anchor khác nhau: onset voice, thời điểm chữ đọc được, và action payoff. Một action chuẩn bị trước voice có thể hợp lý; nêu đó là creative lead, không gọi là timestamp đo được. Dùng tối thiểu chữ đủ nghĩa, không sao chép cả câu voice thành caption.
4. Đặt hình/pose trước, rồi đặt type vào vùng trống có dự tính. Essential type ở screen-space; type gắn lên vật liệu được affine-transform cùng mặt phẳng và có thể khó đọc, nên proof ở mobile. Không ép mọi chữ vào một footer.
5. Voice onset không phải thời lượng hold. Hold là lựa chọn editorial dựa trên tốc độ đọc/ý tiếp theo; đặt rõ và kiểm bằng playback. Nếu chỉ có keyframe thì chưa xác nhận hold/nhịp.

Với sample interval `[a,b)` và sample rate `R`: scene start audio `a/R`; local audio cue `word.start - a/R`. Với FPS `F`, cumulative frame boundary dùng cùng chính sách rounding của project: `B(s)=round(s*F/R)`; số frame scene `B(b)-B(a)`, không làm tròn duration riêng. Nếu picture global anchor theo cumulative grid, local frame cue là `ceil(word.start*F)-B(a)`. Trong pilot source cũ timeline local được neo vào audio start; hai convention lệch nhau dưới một frame ở các scene này. Chọn và ghi rõ convention, không cộng trừ sai hai lần. Frame test mới dùng cumulative global grid và lưu cả audio-local lẫn picture-local.

Word timestamps là ASR estimates, không phải ground truth phoneme/trọng âm. Trước Gate 2 nghe lại voice và xem reveal ở tốc độ thường; lệch nhỏ vẫn có thể cảm thấy muộn nếu entrance quá lâu. Chọn beat chuyển động theo semantic stress, không giả đo được trọng âm chỉ từ word start. Nếu không có alignment đáng tin thì đánh dấu cần xác minh, không viết timestamp giả.

## 3. Thư viện kỹ thuật có điều kiện

Mỗi hàng phải gắn với một ý nghĩa/action. GSAP/SVG đủ cho các recipe dưới đây với assets local; không yêu cầu plugin trả phí hoặc dependency mới.

| Kỹ thuật | Dùng khi / tránh khi | Triển khai seek-safe | QA render / dấu hiệu lạm dụng |
|---|---|---|---|
| Phrase mask reveal | Cần đọc một từ khóa / tránh che mặt hoặc câu quá dài | SVG clipPath hoặc HTML overflow wrapper; tween inner x/y từ giá trị đầu xác định, entrance tại cue | Kiểm trước/đang/settled, dấu không bị cắt; lạm dụng khi mọi câu thành headline từ dưới đi lên |
| Word/group stagger | Phrase có hai nhịp ý / tránh tách dấu hoặc từ ghép gây hiểu sai | Tạo spans lúc init; tween từng word với absolute positions; không split trong onComplete | Kiểm thứ tự đọc và onset cuối; lạm dụng khi người xem đọc đuổi theo chữ |
| Animated underline/accent stroke | Nhấn contrast hoặc một đường liên hệ / tránh underline mặc định sau mọi chữ | Một path cố định, dasharray/dashoffset bằng chiều dài đã đo lúc setup; hoặc scaleX với pivot rõ | Nét không xuyên glyph, không giống progress giả; lạm dụng khi hàng loạt đường vàng không chỉ vào đâu |
| Shape-to-text handoff | Một shape có vai trò khái niệm chuyển thành vùng type / tránh morph glyph không cần thiết | Mask shape mở vùng chữ; tween hai trạng thái. Morph path chỉ khi topology tương thích, không giả cần plugin | Kiểm giữa morph có hình rác/flash; lạm dụng khi transition được nhớ hơn message |
| Geometric framing | Cần regroup ý hoặc brand beat / tránh đóng khung emotional close-up | Bracket/bar/circle segments ở screen-space, ẩn/hiện bằng timeline; thống nhất tokens | Không lấn face/hands, không biến mọi shot thành card |
| Path/trail theo action | Người chạy/lộ trình có hướng / tránh vẽ mũi tên hàm ý flow không có trong voice | Reveal path cố định hoặc precomputed positions; trail samples tính từ t, không push history theo frame | Kiểm có nối đúng chủ thể, ngắn và tắt sau cue; lạm dụng nếu biển/lối đi toàn đường phát sáng |
| Contact/gaze accent | Cần đưa mắt đến một tương tác / tránh dùng glow che anatomy sai | Pose/contact xác lập trước; accent opacity/radius sau contact time đã chọn; không callback tích lũy | Xem frame có/không accent; nếu bỏ accent không đọc được contact thì sửa pose trước |
| Light/color handoff | Đổi chú ý sang khu vực sáng hoặc trạng thái / tránh đổi giờ/thời tiết ngoài nội dung | Overlay gradient có mask và opacity tween cố định; không global filter làm sai skin/logo | Kiểm trước/sau cùng value, không clipping/cháy trắng; lạm dụng nếu “cảm xúc” chỉ là bật glow |
| Parallax/camera reframe | Cần reveal bối cảnh hoặc nối chủ thể / tránh di chuyển khi đang đọc chữ hay cảm xúc tinh tế | Nested camera/world/plane groups; finite tracks; tính đủ painted bounds | Kiểm mép khung, tốc độ đọc, scale figure; lạm dụng khi mọi lớp trôi độc lập làm đồ vật trượt sàn |
| Occlusion/match transition | Có vật/đường nối ý giữa scenes / tránh xóa thời gian hold của từ cuối | Vật che đủ canvas trong khoảng scene đã có; scene đầu/cuối tự render được | Kiểm cut frame, seam, camera và audio không đổi; lạm dụng khi mỗi câu dùng wipe khác nhau |

## 4. Pattern kỹ thuật cho mọi playbook

Đọc HyperFrames core/CLI đang cài trước authoring. Pattern minh họa sau **không phải composition chạy độc lập**; nó cần DOM, duration, assets và registration đúng root. Giữ `placement` ngoài node GSAP điều khiển; đừng dùng CSS transform để center chính node đang tween x/y. Asset fetch/fonts phải hoàn tất trước khi register timeline.

```js
// Values/cues supplied by the scene; no universal ease or duration.
await document.fonts.ready;
const tl = gsap.timeline({ paused: true });
tl.set('#keyword-motion', { x: 0, y: 0, opacity: 0, scale: 1 }, 0);
tl.fromTo('#keyword-motion',
  { y: revealOffset, opacity: 0 },
  { y: 0, opacity: 1, duration: entrance, ease: chosenEase,
    immediateRender: false }, cuePictureLocal);
tl.to('#keyword-motion',
  { opacity: 0, duration: exitDuration, ease: exitEase }, exitAt);
window.__timelines ??= {};
window.__timelines[compositionId] = tl; // matches root data-composition-id
```

Mọi state phải tái tạo từ time: không Date.now/random không seed, timer tự chạy, rAF riêng, callback tạo/hủy DOM hoặc biến đếm phụ thuộc số lần seek. Relative tweens không bị cấm tuyệt đối, nhưng absolute endpoints dễ audit hơn. Path morph cần cùng số/thứ tự segments; không tween `d` giữa topology tùy ý rồi mong GSAP tự sửa. Không hide clip cuối scene bằng visibility vì framework quản clip lifecycle.

Character chain hoặc projection cập nhật phức tạp: ưu tiên precomputed pose/geometry ở frame anchors, rồi nội suy thuần từ t. Nếu dùng adapter hàm render(t), kiểm contract seek thực tế của engine cài sẵn; không nối một hàm vào clock ngoài framework. `onUpdate` không được tích lũy state; cũng không dựa callback chạy khi engine seek suppressEvents. Đối với HyperFrames GSAP nên tween trực tiếp DOM/attr đã chuẩn bị. Remotion dùng `useCurrentFrame()`/FPS và pure pose function, không chạy đồng thời một GSAP clock.

Giữ world asset IDs scene-local (`s03-cafe-awning`, `s08-parent-hand-near`); defs/clipPath cũng prefix để không xung đột khi mount scene cùng trang. Vẽ asset theo chức năng occlusion/pivot, không chẻ thành layer để đạt quota.

## 5. Đo chất lượng và sửa lỗi

| Kiểm | Cách đo/quan sát | Khi thất bại |
|---|---|---|
| Hierarchy | Full frame + thumbnail + grayscale: mô tả được điểm nhìn thứ nhất/thứ hai, so với scene intent | Giảm contrast/detail vùng cạnh tranh hoặc reframe; không tăng mọi saturation |
| Silhouette | Xem shape fill một màu; các dáng/prop có nhận ra không | Sửa contour, negative space ở elbow/hand/torso trước details |
| Mobile | Full-size và 360×640 cho VIDEO-34; người xem đọc được câu chữ đã chọn không cần zoom | Rút chữ, đổi line break/size/position; không scale toàn canvas ngang thành video dọc |
| Anatomy/contact | Pose mở/giữa/đích; check joint lengths, chân sàn, hand/prop contact và occlusion | Chỉnh chain, điểm đỡ và poses; accent không sửa được tay xuyên vật |
| Depth/perspective | Theo dõi một bộ parallel edges, mặt bàn/cửa/bóng, figure scale theo mặt sàn | Chọn một projection cho vùng đó rồi dựng lại từ world points |
| Type/glyph | Text thật: “Sống chậm”, “Cân bằng”, “Thời gian”, “Gia đình”; kiểm dấu trên/dưới và font thực sự tải | Dùng font local có quyền, đổi mask padding theo measured bounds; không giả Latin-ext là Vietnamese |
| Seek | Cùng frame theo thứ tự 0→mid→end→mid và từ trang mới; so pixel hashes/bounds cùng môi trường | Tìm state tích lũy, font late load, transform conflict; hash giống chỉ chứng minh determinism trong môi trường đó |
| Voice sync | ASR IDs + master seconds + global frame index; xem/nghe trước/onset/settled | Sửa creative entrance duration/offset đã ghi, không sửa raw word times cho khớp animation |
| Paint bounds | Camera extremes và frame sát cut; không có unpainted edges hay mask cắt glyph | Extend asset hoặc đổi crop/camera; không che lỗi bằng wash lớn |
| Motion/AV | Sau Gate 1 mới xem playback, frame count/dimension/FPS, mux lag/duration | Phân biệt sample-exact PCM với AAC delay; không gọi encode thành approval |

Keyframe review không xác minh được gait, hold, smoothness hay cảm xúc theo thời gian. Sau Gate 1 mới motion-test joint/contact/hinge trên toàn phase, sau đó render pilot và Gate 2. Mỗi evidence ghi source hash, media hash, frame/time, tool/version, điều đã/ chưa kiểm. Không tái dùng screenshot cũ làm QA của revision mới.

## 6. Tích hợp skills mà không overengineering

**Đã làm trong lượt tài liệu:** tạo catalog entry point ở đường dẫn root đang tham chiếu; ba playbook độc lập, shared contracts, audit và prompt. Không sửa AGENTS/setup/generated skills.

**Đề xuất cho một lần tích hợp được ủy quyền sau:** chỉ thêm link catalog/playbook vào sidecar `skills/fk-edu-motion-explainer.references/visual-design.md` và link khi cần type/voice vào `motion-and-qa.md`; giữ nguyên capability của các skills khác. `setup.py` là nguồn sinh root, nên nếu cần đổi câu root thì sửa nguồn generator và regenerate có backup/kiểm diff, không hand-edit AGENTS. Không tạo style engine, bộ dispatcher, agent orchestration hoặc dependency mới. Khi sync sidecars phải dùng cơ chế hiện có và kiểm canonical/mirror parity.

Root chỉ cần: “Read the core style catalog and the selected production playbook before visual construction; project identity and human approval own the final constraints.” Đây là **đề xuất**, chưa ghi vào root. Bộ docs được viết bởi Codex trong chat hiện tại; không gắn tác giả Antigravity hay coi đã có một cuộc bàn giao agent bên ngoài.
