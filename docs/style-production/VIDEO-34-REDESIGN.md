# VIDEO-34 — visual redesign recommendation & measured voice map

Trạng thái **[P] proposed / NOT APPROVED**. Không sửa project trong lượt nghiên cứu. Tài liệu này áp dụng ba Core Styles đã chốt; không chọn lại bộ style. Nhãn bằng chứng theo [README](README.md).

**Latest-state note:** lúc kiểm cuối, luồng làm việc đồng thời đã cập nhật source/MP4/status sang Typography V2, vẫn awaiting human review. V2 đã bỏ navy wash và gắn chữ lên environment; các phê bình R1 là lịch sử, không được áp máy móc vào V2. Khi tiếp tục, đọc lại latest source/status và giữ những quyết định người dùng đã thực sự xác nhận. Bốn tests bên dưới là đề xuất kiểm chất lượng illustration tổng thể, không ủy quyền rollback V2. [Audit cập nhật](RESEARCH-AUDIT.md).

## 1. Timing và trạng thái thực tế [L]

Master: `videos/video-34/inputs/Generated Audio November 01, 2026 - 5_35PM.wav`, mono PCM 24kHz, 2,232,960 samples, 93.04s; SHA256 `6b92d56bb90f3c4e702903d53d098d7c1765daf716879e8de60826a3110425c1`. Có 17 intervals, raw/word timestamps giữ nguyên. Canvas manifest 1080×1920, 30 FPS; đây là working configuration, chưa là approval full film. `production_status.json` phase `pilot_awaiting_human_review`, approval pending, prior feedback NOT APPROVED; R1 không tự trở thành approved.

| Scene | Sample bounds [start,end) | Global audio bounds | Audio duration | Cumulative frame bounds ở 30 FPS | Picture frames |
|---|---|---|---|---|---|
| S03 | [243986,458528) | 10.166083333…–19.105333333…s | 8.939250s | [305,573) | 268 |
| S08 | [966480,1101123) | 40.270000–45.880125s | 5.610125s | [1208,1376) | 168 |

Không gọi picture duration 8.933333/5.600000s là audio duration; cumulative rounding tạo chênh dưới một frame. S13 giữ **factual review required**; không nghiên cứu/diễn giải thêm residence rights, giá tiền, phạm vi thế hệ hoặc benefit trong nhiệm vụ visual này.

## 2. Project art direction [P]

**Primary: `kurzgesagt` illustrated narrative.** Nhân vật và sinh hoạt dẫn câu chuyện; thế giới được thiết kế riêng, không dùng mascot hoặc bố cục nhận diện Kurzgesagt. **Secondary spatial: `izometrik`** cung cấp discipline mặt phẳng, kiến trúc/thickness/props và một số scene spatial phù hợp, không biến toàn bờ biển thành bản đồ. **Secondary graphic: `bauhaus`** cung cấp hierarchy, masks, keyword handoff và geometric rhythm. Không cần mọi frame chứa ba style.

Visual identity dự kiến: daylight sạch, silhouette có cá tính và trọng lượng, cool environmental field cân warm human/material, địa điểm được đọc qua architecture/ground/sea thay vì stock symbols. Dùng shared character family qua cảnh; protagonist S08 giữ casting/age intent từ storyboard đến khi người dùng đổi. Không biến cư dân nền ở S03 thành gia đình chính chỉ để reuse rig.

Palette là thử nghiệm creative, **không official Esora palette**: deep navy để phân cấp/ink, azure và turquoise cho sea/space, clean near-white để sáng/thoáng, warm limestone giới hạn ở kiến trúc, coral cho trọng tâm người/prop, sunlight nhỏ và có lý do. Có thể bắt đầu từ R1 tokens để so sánh nhưng điều chỉnh value distribution thay vì chỉ đổi HEX. Avoid dusty overlay/grain toàn khung; giữ ánh nắng và vật liệu ấm mà không phủ beige. Không đặt giant navy wash lên toàn khu kiến trúc để cứu type.

Type đề xuất: một sans family có đủ dấu, dùng contrast weight/size trước khi thêm family thứ hai. Serif italic trong studies cũ là một phương án chưa duyệt, không default Bauhaus. Nếu giữ italic cho family phrase, thử nó có hợp actor/environment và có đủ quyền/font coverage; không đổi họ chữ mỗi scene. Logo gốc Esora giữ nguyên pixel/ratio/màu, không trace/recolor/morph; không đưa vào hai test scene nếu storyboard chỉ dùng ở S17. Không thêm watermark/CTA/slogan.

## 3. S03 — Coastal Lifestyle [P]

**Visual proposition:** một không gian ven biển có thể cảm nhận được nhịp sống, dẫn mắt qua hoạt động bằng framing; không phải tập hợp chín người nhỏ để minh họa đủ danh từ.

Environment: shoreline/sea wedge tạo depth; promenade có surface direction liên tục; café nằm trong một mass kiến trúc có mặt sáng và mặt khuất; balcony/cornice/openings gắn đúng face. Tham khảo tinh thần limestone + enclosed balcony từ storyboard hiện tại, không khẳng định landmark/café địa lý có thật. Nếu cần độ chính xác của một building cụ thể ở vòng sau, dùng nguồn ảnh có attribution và fact-check trước khi dựng.

Dàn cảnh thử ở 1080×1920: activity chính ở lower-middle, canopy/wall đủ lớn để đọc café, biển mở ở một phía làm negative space. Một người/nhóm làm focus tại một thời điểm; supporting figures có silhouette riêng nhưng giảm contrast/detail. Foreground plants/rail chỉ khi giúp depth hoặc che handoff. Không phóng toàn world đến mức cắt người ở mép khi camera đổi; artwork cần painted extent cho crop dự kiến.

Character design: walker có trọng lượng và foot plant, runner có forward lean/flight khác walker, café person có seated pelvis/knees và tay thật sự điều khiển cup; không chỉ thay áo cho cùng một rig chống hông. Group family gần cuối có scale đủ để đọc gaze/contact ở mobile. Có thể cắt attention trong cùng scene thay vì giữ đủ ensemble trên màn hình suốt 8.94s.

Style contribution có giới hạn: Kurzgesagt-inspired richness/silhouette/acting dẫn; isometric chỉ giúp mặt café/props/kiến trúc và spatial coherence, không ép đường bờ biển vào 30° grid nếu mất lifestyle; Bauhaus dùng phrase mask theo canopy/negative space và graphic accents có nghĩa. Một đường trail ngắn có thể theo runner; không nối mọi activity thành workflow bằng mũi tên.

Keyword strategy: chọn 2–3 điểm chính nếu thử đọc thấy bốn cue hiện tại quá dày; giữ bảng timing cho các cue khả dụng nhưng không bắt phải hiển thị tất cả. Café type có thể nằm trên mảng canopy đã thiết kế sạch; “Đi bộ” không bóp méo quá mức trên pavement. “Gia đình” ở khoảng trống gần focus cuối, không che hand/face. Camera settle trước khi chữ cần đọc; các khoảng không có text là có chủ đích.

## 4. S08 — Family / Work-Life Balance [P]

**Visual proposition:** người lớn chủ động dành sự chú ý cho con; emotional pivot đọc được ngay cả khi tắt text/effects.

Workspace và terrace là một địa điểm thống nhất. Bàn/ghế/laptop có mặt phẳng và điểm đỡ nhất quán; rear/front rail occlusion rõ. Giảm décor quanh head/hand và vùng text, không nhất thiết xóa toàn décor. Frame đủ gần để adult gaze, child reach, wrist và elbow đọc được; child cao/thấp theo character sheet chứ không scale tùy hứng để vừa tay.

Parent rig: seated pelvis nằm trên seat, torso/neck/head chain nhất quán, upper arm/forearm/hand có chiều dài giữ được giữa poses. Child design khác adult ở proportions/limb taper nhưng cùng shape language; không kéo cổ tay để bù khoảng cách. Tay rời bàn phải clear screen trước đóng laptop, rồi chuyển gaze và reach; child đáp lại, contact được giữ ở endpoint khả thi. Gaze không chỉ là dịch hai chấm mắt nếu head/torso vẫn hướng ngược.

Laptop base giữ stationary trên desk; lid là rigid part riêng xoay quanh hinge. Dựng hinge endpoints và lid vertices từ góc/pose; không scaleY cả laptop làm base méo. Một frame đóng hợp lý chưa xác minh hinge trong motion; vòng animation sau cần kiểm midpoint và trước/sau clearance.

Type: đầu scene có thể không chữ để thiết lập ý; chọn “Sống chậm” hoặc “Cân bằng” cho trọng tâm đầu, không nhất thiết cả hai. Phrase “Thời gian” chuyển visual focus sang khoảng terrace; khi “Gia đình” được đọc, giữ type yên và nhỏ hơn acting focus nếu cần. Đừng để hai headline cùng underline tồn tại vì cue `out=0` trong R1. Text tránh face/hand/child gaze path. Một light handoff nhẹ chỉ sau khi pose rõ; bỏ contact arc nếu nó làm tay trông như hai đường nối icon.

Kurzgesagt-inspired character acting là chủ đạo, iso discipline giúp desk/terrace/hinge, Bauhaus tạo typography hierarchy. Không đổi scene emotional thành diagram hai nửa “work/family” rigid nếu làm giảm quan hệ người thật.

## 5. Voice-sync mapping — timestamps thực từ project [L/P]

Nguồn: `inputs/word-timestamps.json`; số từ dưới đây là **1-based**, nhất quán với `components/pilot-highlights.json`. Global ASR seconds giữ nguyên; local audio = global − exact sample scene start. Trường illustration/text/effect mới là **đề xuất**, không nói đã render. ASR “bơ biển”, “quản trường”, “Giá đình” được hiển thị bằng corrected wording, không viết lại raw hoặc timestamps. Cue windows đo từ start token đầu đến end token cuối.

| Scene | Voice Keyword / word numbers | Timestamp global → local audio (s) | Illustration Action [P] | Text Highlight [P] | Graphic Effect [P] | Style Contribution |
|---|---|---|---|---|---|---|
| S03 | đi bộ, 46–47 | 10.50–10.82 → 0.333917–0.653917 | Walker grounded, gaze theo promenade | “Đi bộ”, tùy chọn | Short reveal theo hướng bước, không arrow workflow | K: acting; I: ground; B: phrase layout |
| S03 | chạy bộ, 54–55 | 12.40–12.72 → 2.233917–2.553917 | Runner có stance/flight, camera hướng sang active strip | Có thể bỏ chữ nếu action đủ rõ | Trail ngắn, tắt trước café | K: silhouette; I: path; B: rhythm |
| S03 | cà phê, 60–61 | 13.68–14.02 → 3.513917–3.853917 | Hand/cup contact, seated pose | “Cà phê” theo canopy | Material-edge mask | K: action; I: table/canopy plane; B: mask/type |
| S03 | bạn bè, 66–67 | 15.10–15.48 → 4.933917–5.313917 | Gaze/gesture giữa người ở café/plaza | Không cần | Không cần, giữ nhịp thở | K: social acting; I: shared ground |
| S03 | gia đình, 77–78 | 17.54–17.92 → 7.373917–7.753917 | Family group rõ ở framing gần hơn | “Gia đình”, nếu còn thời gian đọc | Quiet hierarchy handoff; không bắt contact arc | K: relationship; B: phrase hierarchy |
| S08 | sống chậm, 172–173 | 41.28–41.82 → 1.010000–1.550000 | Tay dừng thao tác, attention bắt đầu đổi | “Sống chậm” hoặc bỏ để ưu tiên cân bằng | Mask ngắn, không bounce | K: intention; B: phrase reveal |
| S08 | cân bằng, 174–175 | 42.14–42.48 → 1.870000–2.210000 | Pose nghỉ/chuyển hướng chú ý | “Cân bằng” là alternative, không thêm tự động lên phrase cũ | Một bar resolve nếu có ý nghĩa | K: pause; B: graphic relation |
| S08 | công việc, 177–178 | 42.68–42.98 → 2.410000–2.710000 | Hand clear lid; lid/base độc lập | Không cần chữ “Công việc” nếu dư tải | Geometry đóng laptop, không flash | I: hinge/desk; K: purposeful gesture |
| S08 | thời gian, 180–181 | 43.30–43.68 → 3.030000–3.410000 | Gaze/torso chuyển sang child | “Thời gian” cạnh terrace | Hierarchy handoff, light cue tùy chọn | K: gaze; B: type transfer |
| S08 | Giá đình (raw), 186–187 | 45.00–45.38 → 4.730000–5.110000 | Contact/emotional response có pose rõ | Corrected “Gia đình” | Giữ type yên; chỉ accent nếu cần | K: expression/contact; B: quiet final emphasis |

Các cửa sổ này là **word windows**, không phải entrance/hold/out đã được phê duyệt. Các thời điểm walk/café/family dùng lại onset đã có trong R1; “bạn bè” và “công việc” bổ sung từ file ASR thật. Không thêm subtitle track. Không tự khẳng định ASR word start chính xác tới mức phoneme; nghe kiểm ở lượt animate.

## 6. Bốn visual tests trước animation [P]

Tất cả phải là PNG capture từ source dự kiến reuse ở pilot mới, không moodboard/reference screenshot và không collage output upstream. Render source tại layout/pose tĩnh; không phát triển full timeline trong bước test. Artboard 1080×1920 theo working config; kèm 360×640 proof. Frame times sau là **frame lấy mẫu thiết kế**, không timestamps từ lời nói được tự tạo.

| Test | Frame anchor global, zero-based | Source pose / frame sample | Mục đích |
|---|---|---|---|
| S03-A | ceil(10.50×30)=315 | Picture-local frame 10, local 0.333333s; audio-local cue 0.333917s | Coastal environment + hero scale/silhouette, không type |
| S03-B | ceil(13.68×30)=411 | Picture-local frame 106, local 3.533333s; audio-local cue 3.513917s | Cùng hệ artwork, café type-integrated layout đã settled để review composition |
| S08-A | ceil(42.14×30)=1265 | Picture-local frame 57, local 1.900000s; audio-local cue 1.870000s | Parent/child/workspace, pose chuẩn bị rời công việc, không type |
| S08-B | ceil(45.00×30)=1350 | Picture-local frame 142, local 4.733333s; audio-local cue 4.730000s | Emotional contact pose + “Gia đình”, faces/hands unobscured |

Không giả rằng typography đã settled ngay tại onset trong animation cuối: đây là static pose/layout proof gắn cue, chưa phải temporal simulation. Lưu `pose_state` và `type_state=settled_layout_test` trong evidence. Khi animate sau Gate 1, kiểm onset/during/settled riêng tại times thực tế.

Gate 1 review: màu/value, shape richness, kiến trúc/depth, figures/anatomy, composition/mobile, type/glyph và consistency. Nếu không đạt, chỉ sửa tests rồi review lại. Gate 1 không phải Gate 2, không tạo quyền full production. Gate 2 chỉ sau explicit approval visual: animate S03/S08, text/effects theo voice, render hai MP4, trình review. Không sản xuất 15 scenes còn lại.
