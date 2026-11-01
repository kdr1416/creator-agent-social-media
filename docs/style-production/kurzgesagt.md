# `kurzgesagt` — Original illustrated storytelling production playbook

Đọc [shared production](SHARED-PRODUCTION.md) để lấy timing/runtime/QA contract. Nội dung construction dưới đây là **[A/P]**, không phải style guide chính thức của Kurzgesagt. [U/O] Repo demo chứng minh shaded forms, semantic palette, cached atmosphere, text rhythm và scale transition; không chứng minh human acting rig. [Nguồn và phân tích](RESEARCH-AUDIT.md).

## 1. Style Identity

Phần cần học là một thế giới minh họa có thiết kế: silhouette rõ, shape đơn giản nhưng được biên tập kỹ, màu sắc tổ chức theo vai trò, detail theo focus và biến đổi giải thích một ý. Hình cơ bản là nguyên liệu, không phải output cuối. Một mái nhà cần có độ dày, mặt đón sáng, mặt khuất, điểm gắn ban công và ngữ cảnh tỷ lệ; một người cần pose có trọng lượng và ý định, không chỉ circle head + capsule body.

Không bắt buộc vũ trụ, chim mascot, màu tím, mắt chấm hoặc outline đồng đều. Với lifestyle/ad, dùng nguyên tắc richness/clarity để dựng người và địa điểm nguyên gốc. Cảnh không có nhân vật vẫn đúng khi vật thể/metaphor là chủ thể kể chuyện.

## 2. Art Direction Recipe

### Color system và value trước HEX

Chọn một quan hệ nền–chủ thể, ví dụ cool field + warm people/architecture. Xác lập tối/sáng để silhouette đọc được trong grayscale trước khi thêm nhiều hue. Nền có thể sáng hoặc tối; chủ thể cần tách ở cạnh quan trọng, không cần mọi cạnh có viền. Primary hue tạo trường màu rộng, secondary nối material/environment, accent dành cho nơi cần chú ý. Da không phải accent phải đổi theo mỗi từ khóa.

Một palette thử cho coastal illustration: ink navy, azure sea, pale cool sky, warm limestone, coral costume, restrained sunlight. Đây là **recipe đề xuất**, không official brand. Lập các swatch theo material gồm base/light/shadow: limestone light nghiêng ấm, shadow nghiêng cool; không tạo bóng bằng giảm opacity đen lên mọi vật. Màu sáng nhất/đậm nhất không được phân phối đều ra background nếu cần một focal point. Vật ở xa có thể giảm contrast/detail; không giảm saturation toàn frame đến mức nhợt nhạt.

Lập ba thumbnail cùng artwork ở value map, color blocks và detail. Nếu value map không có focus thì sửa diện tích/độ sáng/crop trước. Màu hấp dẫn đến từ tương quan: một coral nhỏ nổi trên azure rộng, white sạch có dark support, warm stone có cool shadow. Tăng saturation mọi màu chỉ tạo cạnh tranh. “Hiện đại” ở brief này là nét sạch, màu phân vai, hình có chủ ý và typography rõ; không đồng nghĩa cấm palette dịu ở mọi project.

| Cảm giác lỗi | Nguyên nhân cần thử | Cách sửa |
|---|---|---|
| Cũ/vintage ngoài brief | Beige phủ khung, dusty hue cùng value, grain toàn màn hình | Giữ warmth ở vật liệu, dùng nền/white sạch hơn, bỏ grain nếu không có vai trò |
| Nhạt/thiếu sức sống | Figure và nền cùng value, accent nhỏ và phân tán | Tách silhouette chính, gom accent tại action, giảm mảng cạnh tranh |
| Stock vector | Object dựng từ template giống nhau, đầu/tay/thân một công thức, detail phân đều | Thiết kế contour riêng, pose/props có câu chuyện, tiết chế detail ở xa |
| Nhiều màu không hierarchy | Mỗi object có hue riêng và cùng saturation | Gán role/material tokens, recolor theo scene palette thay vì random từng asset |

### Shape, illustration, light và depth

Vẽ silhouette tổng trước: curve lớn xác định bờ biển, vertical masses kiến trúc, figure groups tạo nhịp người. Dùng tỷ lệ large/medium/small có chủ đích; tránh mọi cửa sổ/cây/người bằng nhau. Interior detail theo cấu trúc của vật: cửa nằm trên mặt, bóng ban công đổ lên mặt đứng, seam quần áo theo thể tích. Tạo highlight bằng clipped shape hoặc gradient theo mặt, không dán glow lên tất cả edges.

Chiều sâu đến từ occlusion, scale theo mặt sàn, edge contrast, ánh sáng và camera distance. Có foreground khi nó giúp cảm giác địa điểm hoặc che cut, không để đạt bốn lớp. Texture chỉ là treatment có mục đích, được cache/seed, không chữa hình đơn giản. Hai hoặc ba mảng shading có thể đủ nếu contour và lighting đúng; rất nhiều gradients cũng có thể làm mất graphic clarity.

### Composition, typography, 9:16

Viết scene intent bằng một câu. Chọn actor/prop chiếm focus và đặt điểm gaze/action vào vùng đọc tốt. Dựng line of action dẫn mắt từ người → prop → kết quả; để negative space gần nơi chữ sẽ xuất hiện. Wide shot giải thích địa điểm, medium shot đọc activity, close shot đọc cảm xúc. Không cố gom cả ba khoảng camera vào một poster tĩnh.

Video dọc cần dựng lại phân cấp theo chiều cao. Tránh để tòa nhà khổng lồ ăn hết phía trên trong khi tất cả người nhỏ nằm phía dưới. Thử thumbnail và 360×640: nếu không phân biệt đang đi/chạy/uống café, đổi scale/crop/pose trước. Chữ quan trọng phải có vùng nền sạch được thiết kế từ đầu; có thể dùng canopy, sky gap hoặc wall, không mặc định navy wash. Typeface đủ dấu, có weight/width phù hợp với hình. Geometric type có thể bổ trợ; tránh font quá bubbly khiến ad thành đồ chơi nếu brief cần premium.

## 3. Asset Construction Recipe

Đề xuất hierarchy cho một café shot; chỉ tạo group thật sự cần biến đổi/occlusion:

```text
s03-camera
  s03-world-placement
    s03-sky / s03-sea / s03-distant-mass
    s03-building
      facade-lit / facade-shadow / balcony / shutters
    s03-promenade
    s03-hero-placement
      s03-hero-motion
        far-arm / far-leg / pelvis / torso
        near-leg (thigh / shin / shoe)
        neck-head (face / eyes / mouth)
        near-arm (upper / forearm / hand)
    s03-cafe (awning / table / cup / chair)
  s03-type-placement
    s03-type-clip / s03-type-motion
```

IDs semantic, defs prefix, `placement` giữ tọa độ thiết kế; motion group giữ x/y/rotation của GSAP. Dùng SVG symbols cho balcony/window/plant khi cần reuse; parameter hóa tỷ lệ/vật liệu, không nhân bản vô thức một ngôi nhà. Keep asset path/author/rights/hash trong ledger. Artwork bên trong scene được inline nếu cần animate từng part; `<img src=...svg>` không cho GSAP chạm group nội bộ theo selector thường.

Environment xây từ blockout lớn → mặt sáng/tối → openings/balcony thickness → contact shadows → localized detail. Malta-inspired composite cần ghi rõ không phải bản đồ/landmark chính xác. Không thêm địa danh hoặc quyền cư trú qua hình mà voice không xác minh.

Character sheet trước rig: front/three-quarter silhouette, neutral/intent/contact poses; adult/child có khác shoulder width, limb taper, hand size và stride. Có thể thử adult 6–7 head heights, child 4.5–5.5 như phạm vi blockout **cho thiết kế cụ thể**, không chuẩn chung. Chốt pose sheet bằng visual review; đừng thay head/body ratio giữa scenes để vừa crop. Dáng expressive có line of action, shoulder/hip counter-angle, silhouette gaps và gaze target. Không suy sắc tộc/tính cách từ stereotype hình dạng.

## 4. Motion Construction Recipe

### Scene-local narrative và camera

Mỗi beat có động từ/ý nghĩa: người dừng nhìn bạn, tay rời laptop, đứa trẻ nhận sự chú ý. Lập opening → preparation → action → response/hold. Background motion chỉ giữ sức sống hoặc hướng mắt; đừng để biển/cây cùng pulse khi actor cần yên. Camera reframe phục vụ chuyển chú ý, giảm hoặc dừng trong lúc text cần đọc.

Timing lựa theo khối lượng và ý định: walk đều và grounded; runner có flight/stance khác; quay đầu nhẹ cần eye lead/body follow; graphic cue có thể nhanh hơn thân người. Không dùng cùng `power3.out` hay overshoot cho cả da thịt, architecture và chữ. Anticipation/follow-through có ích khi làm action rõ, không bắt mọi object nảy trước khi xuất hiện.

### Acting và contact

- Gaze: mắt hướng prop trước, head turn tiếp, torso có thể theo nhẹ. Giữ head pivot tại neck; rotation quanh bounding-box center dễ làm đầu trượt khỏi cổ.
- Walk: đặt contact/passing/up/down poses, cố định chân trụ trong world khi root đi qua. Root travel trong stance phải khớp tốc độ foot progression. Run cần thay stance/flight và lean, không chỉ tăng swing/giảm period. Kiểm pose 1/4 chu kỳ và 2–3 frame quanh contact.
- Hand/prop: định nghĩa target ở không gian chung, solve wrist và elbow cùng frame. Tay nâng cup thì cup đi cùng hand sau khi grasp; trước grasp cup thuộc table. Trong overlap phase có thể dùng hai group với trạng thái hình học tương ứng, nhưng không nhảy ownership bằng callback.
- Parent/child: child reach trước contact, parent nhận gaze rồi reach; ổn định endpoint sau chạm. Không kéo dài forearm để chạm, không ép elbow bật góc, không cho hai hands thành một blob.
- Expression: brow/eye/mouth đồng thuận nhưng không phải cùng bật; subtle smile + nghiêng người thường đọc tốt hơn giant grin hoặc sparkle.

### Type, masks và transitions

Chữ xuất hiện theo semantic stress, ăn vào vùng trống của illustration. Mask theo cạnh vật liệu, underline có thể trở thành đường lối đi nếu điều đó thật sự hướng mắt. Khi action payoff là contact, type giữ yên và nhường contrast cho hand/face. Match silhouette của prop hoặc đường chân trời nối scene; không zoom xuyên mọi vật để chứng tỏ depth.

## 5. Voice-to-Visual Mapping

Ví dụ khái niệm dưới đây dùng anchor tượng trưng, **không phải timestamps AUDIO đo được**. Bảng VIDEO-34 thực tế nằm ở redesign.

| Voice phrase | Main action | Text highlight | Effect | Timing anchors |
|---|---|---|---|---|
| “từ ý tưởng đến thử nghiệm” | Sketch prop mở thành workspace, nhân vật thử dụng cụ | “Thử nghiệm” nếu cần nhấn kết quả | Một shape từ bản vẽ mở mask workspace | Voice token “thử nghiệm” = anchor K; preparation trước K theo action; payoff sau K theo cửa sổ đọc |
| “thời gian cho gia đình” | Tay rời công việc, gaze chuyển sang child, hai người chạm tay | “Gia đình” ở khoảng trống gần terrace | Một accent ngắn sau contact, nếu pose đã rõ | Anchor từ ASR của phrase; contact không nhất thiết xảy ra đúng âm tiết đầu |

Không vẽ thêm cấp phép/benefit như một hệ quả của nhân vật hạnh phúc. Illustration minh họa cảm xúc không phải chứng cứ về claim.

## 6. Technical Implementation

Không thêm rig engine. SVG nested groups + GSAP timeline có thể làm phần lớn scene này. Pin các pivots bằng SVG coordinate đúng hệ cha; khi nested scale phải chuyển contact point về cùng coordinate space trước so sánh. Với 2-bone reach, pseudocode construction (chưa chạy trong production):

```text
root shoulder S; target wrist T; lengths L1,L2 fixed
d = length(T-S); clamp target to reachable annulus
angle to target = atan2(T.y-S.y,T.x-S.x)
shoulder offset = acos((L1²+d²-L2²)/(2*L1*d))
choose elbow bend side consistently; compute elbow and wrist
precompute key poses; write same-topology SVG paths / transform angles
```

Không chia cho d=0; xử lý target ngoài reach bằng đổi staging hoặc whole-body lean, không chỉ ép clamp rồi để tay không chạm. Solver chỉ giúp constraint, không thay pose art direction. Giữ joint contour/occlusion khi nội suy; path topology cố định. Khi tween cup/hand cần cả transform và parent placement đã tính, không cập nhật bằng một event chỉ chạy forward.

## 7. Visual Quality Checklist

| Kiểm | Cách xem | Lỗi thường gặp → sửa |
|---|---|---|
| Silhouette/story | Tắt interior details/type; có nhận ra hoạt động? | Mọi người tay chống hông → vẽ purposeful contact/gaze poses |
| Color/value | Color block và grayscale ở mobile | Face hòa nền → đổi value vùng sau mặt, không viền trắng toàn figure |
| Richness | So macro masses với localized detail | Stock windows lặp và thiếu depth → bổ sung thickness/material/occlusion tại focus |
| Character proportions | So pose sheet xuyên scene | Head lớn nhỏ tùy crop → giữ rig ratio, đổi camera/staging |
| Ground/contact | Frame ở contact, passing, reach midpoint, end | Foot slide/hand drift → world targets, stance solve, chuyển tọa độ đúng |
| Acting | Playback sau Gate 1 + still eyes/hands | Motion đều máy → thêm intention/hold/response có nghĩa, không thêm bounce ngẫu nhiên |
| Typography | Frame có chữ và không chữ tại 360×640 | Chữ như banner dán thêm → mở negative space và neo vào visual proposition |
| Technical | Seek repeat, painted bounds, runtime logs | Mid-seek khác frame fresh → absolute state và local readiness |

## 8. Anti-Patterns theo ngữ cảnh

Hình tròn, palette dịu, static camera hay fade không tự là lỗi. Chúng thành vấn đề khi thay thế cấu trúc cần có: circle head mà không có neck/pose; beige làm figure lẫn nền; thêm 30 detail mà focal vẫn yếu; mọi object cùng float; environment làm wallpaper; nhân vật chỉ là icon có tay đung đưa; text nhắc lại mọi lời; glow che sai anatomy. Sửa nguyên nhân construction/staging trước, không tăng số layer hoặc motion presets để đủ “premium”.

## 9. Practical Example — coastal pause

Scene minh họa nguyên gốc: một người dừng ở café sau đi dạo. Key visual medium-wide gồm mặt tiền limestone bên trái, sea wedge ở phải, canopy dẫn mắt đến bàn/cup, hero có silhouette rõ ở foreground. Hai người nền chỉ làm địa điểm sống; không yêu cầu người xem đọc đủ hoạt động của họ. Main outfit coral trên nền cool, face có light-dark support; shutter và balcony detail chỉ ở mảng gần focus.

Beats: mở bằng bước chân đang có trọng lượng → gaze về bạn → hand chạm cup → chữ “Cà phê” lộ theo mép canopy → giữ hình đọc được → focus trả về hai người. Timing thực tế phải lấy từ audio project, không dùng các beat này làm giây giả. Triển khai bằng scene-local world/actor/type groups, cup contact key poses và finite timeline; sau visual approval mới animate gait. Final QA kiểm cup contact, heel plant, chữ không cắt dấu, người không quá nhỏ ở mobile, absence of camera edge và voice cadence. **Ví dụ này là recipe chưa render, không phải output đã đạt chuẩn.**
