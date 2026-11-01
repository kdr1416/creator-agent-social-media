# `bauhaus` — Graphic composition & kinetic typography playbook

[A/P] Đây là production interpretation hiện đại, không phải khẳng định Bauhaus lịch sử có một bộ animation rules cố định. [U/O] Demo upstream có grid, masked letters, shape actions, circle wipe và clock transformation. [Nguồn/audit](RESEARCH-AUDIT.md); [shared runtime/voice/effects/QA](SHARED-PRODUCTION.md).

## 1. Style Identity

Trọng tâm là quan hệ hình–chữ–khoảng trống: thông điệp đọc rõ, tỷ lệ mạnh, đường trục có chủ đích, shape có chức năng và chuyển động tạo cấu trúc lập luận. Hình tròn/tam giác hay đỏ-vàng-xanh chỉ là vocabulary; thiếu hierarchy và rhythm thì vẫn là random geometry. Có thể dùng làm phong cách chính cho ad ngắn hoặc ngôn ngữ bổ trợ cho illustration/spatial film.

Giữ khác biệt giữa Bauhaus, Swiss typography và các diễn giải thương mại hiện nay; demo tham khảo pha chúng với nhau. Flow Kit dùng ID `bauhaus` tương thích để chỉ một treatment được project định nghĩa rõ, không dùng nhãn để tuyên bố tính xác thực lịch sử. Không bắt buộc font mang tên “Bauhaus”, paper grain hoặc palette primary colors.

## 2. Art Direction Recipe

### Color system và contrast

Chọn field/ink/accent roles trước. Trong primary poster mode có thể dùng một field lớn, chữ ink tương phản và một color mass dẫn mắt; secondary hue giúp phân nhóm. Trong overlay mode dùng palette project, không đem nguyên đỏ cobalt/vàng/cream từ demo vào phim cyan/coral. Hue distribution theo diện tích: accent phải có chỗ nghỉ và vai trò, không mọi circle/word cùng saturation.

Value hierarchy quyết định headline/shape/support. Một shape lớn saturated có thể mạnh hơn chữ nhỏ black; quyết định ai dẫn dắt rồi cân lại diện tích/contrast. Text trên màu rực cần proof thực tế; đừng cho rằng mọi white trên cyan đều đủ rõ. Lighting thường không cần mô phỏng; flat graphic là lựa chọn hợp lệ khi tương quan mass/figure-ground đã mạnh. Nếu thêm shadow/extrusion hãy thống nhất như một vật liệu, không mix một chữ 3D plastic với background print khi không có brief.

Hiện đại trong phạm vi Flow Kit: neutral sạch, edges sắc, palette roles nhất quán, type đọc tốt, spacing được biên tập, motion bám meaning. Tránh cảm giác cũ bằng bỏ grain/cream nếu không cần, không phải tăng saturation mọi hue. Màu dịu hoặc retro vẫn hợp nếu người dùng chọn; không biến preference VIDEO-34 thành global ban.

### Typography và hierarchy

Đọc câu thật và chọn một hierarchy: keyword, phrase support, optional label. Bắt đầu bằng font có đầy đủ dấu tiếng Việt và quyền dùng; kiểm rendered glyphs, không chỉ tên font. Tạo baseline/line-height theo chữ có dấu, đặc biệt “Sống”, “Cân bằng”, “Thời gian”, “Gia đình”. Uppercase có thể tăng graphic presence nhưng tốn chiều ngang; title case hoặc mixed case có thể hợp emotional beat. Không dùng tracking âm đến mức dấu/letter đụng nhau.

Thiết lập grid theo artboard và nội dung, không bắt buộc 12 cột. Align cạnh shape với một trục type hoặc counterform có ý nghĩa; optical alignment có thể lệch mathematical bounds để nhìn cân. Tỷ lệ chữ chính/phụ cần đủ khác để đọc được order tại thumbnail. Không tăng kích thước một từ chỉ vì nó dài hơn trong transcript; ý nghĩa quyết định độ mạnh. Tránh nhét quá nhiều weight/family để mỗi keyword trông như một font ad khác.

### Shape language, composition và depth

Circle có thể thành vùng tập trung/thời gian, bar chia trạng thái, triangle làm hướng/chuyển trạng thái khi nội dung cho phép; không gán ý nghĩa phổ quát cho hình. Dùng negative space như counterweight, đặt mass có tension nhưng focal rõ. Shape cut-out tạo depth graphically bằng overlap/mask; không cần scene có bốn lớp. Texture chỉ theo project treatment.

Dọc 9:16: không crop poster ngang. Dựng phrase thành stack có nhịp đọc từ trên xuống, giữ word group có nghĩa; để illustration hoặc shape lớn cân trọng lượng. Đừng tách “cân” và “bằng” ra hai nơi chỉ để lấp khung. Essential text phải đọc ở 360×640; logo giữ tỷ lệ/clearance của asset thật, không trở thành một shape bị morph.

## 3. Asset Construction Recipe

SVG cho shape/mask, HTML text cho typography linh hoạt là đủ. Đo bounds sau font readiness; lưu layout constants trước timeline. Với text gắn vào plane illustration, áp affine lên outer wrapper/ SVG group; animated inner wrapper chỉ xử lý reveal. Một glyph không phải một UTF-16 code unit: ưu tiên word/phrase grouping; nếu cần letter animation dùng grapheme segmentation (`Intl.Segmenter` nếu runtime hỗ trợ), bảo toàn dấu kết hợp.

```text
scene-root
  graphic-field
  geometry-placement
    circle-motion / bar-motion / bracket-motion
  phrase-placement
    phrase-mask
      phrase-motion
        word-main / word-support
  illustration-slot (optional; original artwork)
  brand-slot (unchanged asset, when requested)
```

Semantic IDs như `s08-family-word`, `s08-balance-rule`; có measured padding quanh diacritics. Chỉ tạo từng-letter spans khi chúng có vai trò rhythm rõ. Dùng reusable underline/bracket/mask primitive với explicit timing/ease, không tạo một hàm “animate everything premium” áp cùng move cho mọi câu. Reuse grid/tokens, không clone trọn bố cục poster.

## 4. Motion Construction Recipe

### Rhythm theo ngữ nghĩa

Lập phrase rhythm: setup → stress → hold → handoff. Stress có thể là đối lập, trọng tâm câu, hoặc một chuyển ý. Graphic entrance thường có acceleration rõ và settle ngắn; emotional support nên nhẹ hơn để không đè diễn xuất. Exponential ease hợp một snap graphic nhưng không phải tất cả object cần expo. Linear wipe hợp cơ chế/ruler; decelerated slide hợp phrase settle; hold yên là phần của rhythm.

Anticipation hợp một shape tích lực để expand thành wipe, không bắt một chữ quan trọng lùi lại mỗi lần xuất hiện. Overshoot rất nhỏ có thể làm playful ad, nhưng repeated bounce khiến câu nghiêm túc thành game. Secondary motion là response của shape cùng hệ, không hạt confetti vô nghĩa. Camera thường không cần nếu type/shape đã chuyển động; tránh zoom cả khung làm mất reading stability.

### Recipes dùng trực tiếp

1. **Mask theo cụm:** phrase đã layout ở vị trí cuối; inner group đi từ ngoài clip vào. Clip có padding theo dấu; chọn direction hợp visual line. Nếu phrase ngắn một nhịp thì reveal cả cụm, không stagger để chứng tỏ công nghệ.
2. **Geometric framing:** một bar/bracket phát triển vào khoảng trống rồi chữ nhận focus. Bracket có nghĩa “nhóm ý” hoặc chỉ action. Nếu vùng trống nhỏ, bỏ bracket, ưu tiên đọc chữ.
3. **Animated underline:** nét theo baseline/plane, scale hoặc dash. Có thể resolve tại keyword thứ hai để thể hiện quan hệ, ví dụ cân bằng; không underline mọi noun.
4. **Shape-to-type:** circle mở thành mask để hiện chữ bên trong, bar thành mép của word group. Đây là continuity bằng shape, không bắt buộc morph outline glyph. Nếu muốn path morph phải topology-compatible và có lý do đọc.
5. **Keyword hierarchy swap:** từ cũ giảm contrast/scale về secondary, từ mới vào vùng trống đã thiết kế; không để các headline cũ xếp chồng dần lên scene. Geometry giữ một anchor chung để người xem không lạc.
6. **Rhythmic transition:** shape đã có trong scene mở che cut, rồi thành prop/frame của scene mới. Dùng thời gian scene có sẵn; không rút audio hoặc thêm tail. Không bắt mọi transition cùng move.

Khi hỗ trợ illustration, chuyển động lớn của type và action chính nên được dàn để mắt đọc theo thứ tự. Contact/emotional payoff có thể chỉ cần phrase giữ yên; không phủ chữ lên face hoặc tay. Nhân vật không bắt buộc trong Bauhaus. Nếu có, dùng character design của project, gaze/pose hướng vào thông điệp; không buộc anatomy thành circle/triangle chỉ để đồng bộ vocabulary.

## 5. Voice-to-Visual Mapping

| Phrase ví dụ | Main visual action | Highlight | Effect | Timing anchor |
|---|---|---|---|---|
| “ít hơn, nhưng rõ hơn” | Mảng shapes rối thu thành một graphic mass có trục | “Rõ hơn” | Mask reveal qua vùng vừa được dọn | K từ word timestamps thực tế; hold không kéo qua ý tiếp theo |
| “cân bằng giữa công việc và gia đình” | Hai vùng graphic nhường attention từ desk sang người | “Cân bằng” hoặc “Gia đình”, chọn theo scene | Bar đổi thành đường cân đối hoặc keyword handoff | K theo phrase; không tự tạo timing cho câu ví dụ |

Nếu type đã nói đủ ý, illustration có thể là support; nếu diễn xuất đã kể mạnh, type có thể vắng. Đừng biến playbook này thành caption generator.

## 6. Technical Implementation

GSAP + SVG/HTML với one paused timeline; root duration/FPS và `__timelines` theo core. Không cần SplitText/plugin mới: words có thể được author sẵn trong DOM, hoặc dùng grapheme segmentation lúc init. Mask/reveal endpoints cố định, không layout trong tween callback. Example recipe (pseudocode, chưa render):

```text
await local fonts ready; measure phrase and diacritics
place phrase wrapper on approved layout grid
create clip extent = measured bounds + glyph padding
timeline.set(inner, known hidden offset, t=0)
timeline.fromTo(inner, hidden offset -> final pose, at=cue, immediateRender=false)
timeline.animate(rule, 0 -> full length, at=semantic resolve cue)
timeline.fade old phrase at editorial out; keep new phrase independent
register completed paused timeline with composition root ID
```

Một mask không cần animate DOM height/width; tween inner translation/scale hoặc SVG attr phù hợp. Không CSS keyframes tự chạy song song. Remotion có thể render cùng design qua frame interpolation; giữ cùng text measures/fonts và anchors, không chuyển style vì engine khác.

## 7. Visual Quality Checklist

| Kiểm | Cách xem | Lỗi → sửa |
|---|---|---|
| Reading order | Thumbnail grayscale và target mobile | Shape hút mắt hơn keyword → giảm area/contrast hoặc dùng shape dẫn mắt |
| Grid/optical balance | Overlay guides, tắt guides rồi xem lại | Mathematical align vẫn lệch → optical correction theo glyph/mass |
| Vietnamese | Crop chữ trước/during/settled | Mask cắt dấu → đo glyph padding và line-height thật |
| Voice | ASR cue + playback sau Gate 1 | Từ đọc được quá muộn → đổi entrance/stagger, không sửa ASR |
| Integration | Bật/tắt illustration và type | Hai layer như hai phim ghép → dùng shared palette, anchor và timing personality |
| Rhythm | Playback có hold, xem không audio và có audio | Mọi cue cùng bounce/stagger → dàn lại stress/hold theo ý nghĩa |
| Clutter | Frame có nhiều cue cùng tồn tại | Headline cũ tồn lưu → exit hoặc giảm role rõ ràng |
| Runtime | Fresh seek/repeated seek, fonts/requests | Font fallback/DOM side effects → local readiness, init một lần, absolute state |

## 8. Anti-Patterns theo ngữ cảnh

Không chỉ rải primary-color shapes; không mặc định beige/grain = Bauhaus; không dùng font tên Bauhaus mà bỏ hierarchy; không tween từng ký tự của mọi câu; không làm chữ thành một cơn mưa xoay; không đổi palette của cả phim chỉ để chuyển style; không underline/flare sau mọi lời; không zoom đọc chữ như camera quay poster. Graphic simplicity có thể rất mạnh, miễn tỷ lệ, spacing và motion có chủ đích. Quiet type không phải motion kém nếu nó làm người xem chú ý diễn xuất.

## 9. Practical Example — attention becomes family

Ví dụ original mixed illustration/type: desk ở trái, terrace ở phải, người lớn/con ở lower-middle. Mảng tường trống cạnh desk là vùng type đầu; vùng trời không chạm faces là vùng kết. Palette lấy từ illustrated world, chữ navy trên light wall; chỉ một accent coral dùng để nối word/prop. Không đổi nền thành paper poster.

Beats: phrase “Công việc” nằm yên theo wall → một bar ngắn thu lại khi hand rời laptop → attention chuyển sang terrace và từ “Thời gian” → khi ánh mắt/hand contact đã đọc được, “Gia đình” settle ở negative space và giữ. Không cần cùng lúc ba phrase. Anchor lấy từ master audio thật, hold bằng thử playback sau Gate 1. Bốn still test sẽ kiểm type composition/diacritics và chỗ contact, nhưng chưa kiểm nhịp. Final QA sau animation: không che tay/mặt, không split dấu, chữ đọc đúng stress, bar không làm giả claim và tone cùng character scene. Đây là recipe chưa được render mới.
