# VIDEO-34 — Character Design Reset R3

**AWAITING CHARACTER DESIGN REVIEW**. R2 character design được người dùng **REJECTED — NOT APPROVED**. Không tiếp tục scene development, không animation hoặc MP4. Đây là ba hướng artwork vector để chọn direction, chưa là character bible đã khóa.

[Review gallery](index.html) · [R2 vs three options](R2-vs-options.png) · [S08 interaction A](S08-interaction-A.png).

| Direction | Design sheet 1800×1600 | Editable vector | Source preview | Actual scene-size/mobile proof |
|---|---|---|---|---|
| A — Premium stylized vector | [PNG](option-A.png) | [SVG](option-A.svg) | [HTML](option-A.html) | [1080×1920](scene-scale-A.png) · [360×640](scene-scale-A-mobile.png) |
| B — Modern editorial | [PNG](option-B.png) | [SVG](option-B.svg) | [HTML](option-B.html) | [1080×1920](scene-scale-B.png) · [360×640](scene-scale-B-mobile.png) |
| C — Expressive geometric | [PNG](option-C.png) | [SVG](option-C.svg) | [HTML](option-C.html) | [1080×1920](scene-scale-C.png) · [360×640](scene-scale-C-mobile.png) |

Mỗi sheet có full-body parent và child, second adult, resident; mặt nhìn three-quarter; ba biểu cảm parent (warm/present, listen/consider, joy/recognition) và child close-up; standing, seated-at-desk, walking, turning toward child và seated hand-contact. Biểu cảm listening được vẽ có chút quan tâm/lo nghĩ, khác với smile/joy; không coi đó là một neutral listening pose đã chốt.

## Vì sao R2 chưa đạt

Đã đọc root AGENTS, ba style playbooks, R2 source SVG/generator/frames/asset ledger, project assets-components-plan/storyboard và current production status. Các nhận định dưới đây là art-direction diagnosis từ artwork thực tế, không phải đánh giá rendering engine.

| Thành phần | Vấn đề quan sát ở R2 | Thay đổi trong R3 |
|---|---|---|
| Silhouette và personality | Các figure có contour thân khá gần nhau; nhân vật nền chủ yếu đổi costume; pose chưa bộc lộ ý định | Ba shape languages, outfit construction và footwear khác nhau; hair silhouette/face planes theo direction |
| Head/body | Adult và child chưa khác đủ về cấu trúc; neck/torso kéo dài làm parent mất cân bằng | A medium stylization, B đầu nhỏ/tỷ lệ dài hơn, C đầu và counterforms mạnh hơn; child có proportions/face/hair riêng |
| Face và hair | Mắt, nose wedge và smile dùng cùng công thức; đổi gaze ít làm thay đổi expression | Ba face constructions; eyebrows/mouth/eye emphasis khác giữa ba expression states; bob, ponytail, geometric crop và child hair riêng |
| Shoulder/torso | Near sleeve là mảng đắp, shoulder transitions gắt, torso đứng khá thẳng | Sleeve cap có shoulder volume; collar/neck overlap rõ; drape, waist, shirt panels và slight upper-body lean |
| Arms/elbows/hands | Cánh tay reach dài, một số pose thành đường chéo thẳng; endpoint trùng không đảm bảo hand design | Near arm tiếp xúc được bẻ tại elbow; forearm đổi hướng; hand/wrist riêng với finger/thumb contour và child hand nhỏ hơn |
| Seated posture/legs | Seat support/hip/knee chưa đọc rõ, chair legs dễ lẫn với chân người | Seated trouser contours dựng riêng cho thigh–knee–calf, knee fold và shoe-ground points; không chỉ biến dạng standing legs |
| Clothing | Đường áo/quần đơn giản, ít chức năng tạo hình | A soft collared shirt/belt/sneakers; B tailored cream blouse/teal trousers/sandals, child polo/shorts; C overshirt/pockets/color-block/hoodie/chunky shoes |
| Poses | Body và head chưa cùng chuyển attention, tay hơi mannequin | Upper-body lean có chủ đích, opposing limbs trong walk, turn hướng vào child, contact pose bẻ khuỷu thay vì kéo dài reach |

## Ba direction khác nhau ở đâu

**A — Premium stylized vector:** soft cheek/jaw contours, mắt có white/iris rõ, bob tóc tạo silhouette dễ nhận, coral collared shirt và teal trousers. Child curly hair, fuller cheeks, yellow pocket top; second adult tóc ngắn/tee và resident tóc bạc dùng cùng language nhưng khác nhận diện. Ưu tiên warmth và readability. Đây là **ứng viên mình chọn để thử context**, vì parent/child faces vẫn đọc rõ trên mobile; không phải lựa chọn được người dùng phê duyệt.

**B — Modern editorial:** adult head nhỏ hơn, long silhouette, jaw/side-plane rõ, mắt tiết chế, ponytail và tailored blouse/collar/belt. Second adult có kính/beard treatment; child có eye treatment mềm hơn adult, polo + shorts/socks. Phù hợp premium lifestyle theo hướng ít cartoon hơn. Head và facial features nhỏ ở mobile là tradeoff cần người dùng đánh giá; chưa tự chọn B làm primary chỉ vì nhãn “editorial”.

**C — Expressive geometric:** pentagonal/wedge-like head, angular hair/counterforms, broad overshirt, color block, wider cropped trousers và chunky footwear. Child có hoodie/pocket và head silhouette riêng. Khác A/B ở cả tỷ lệ, contour, face planes và wardrobe, không chỉ palette. Gần language kinetic graphics hơn nhưng có thể quá graphic so với tone cảm xúc S08; đây là câu hỏi creative review, không lỗi engine.

Không sao chép mascot hoặc tài sản nhận diện từ studio tham khảo. Drawing source là [draw_characters.py](draw_characters.py); các SVG xuất ra vẫn editable theo paths/groups, không trace raster hoặc giấu ảnh bitmap dưới vector. Source chỉ là static drawing helpers, không runtime rig framework, không IK hoặc animation system mới.

## S08 interaction test — chỉ thử A trong environment hiện có

[Full PNG](S08-interaction-A.png) · [Mobile](S08-interaction-A-mobile.png) · [SVG](S08-interaction-A.svg) · [HTML](S08-interaction-A.html) · [Contact detail](qa/contact-detail-A.png).

Environment, camera, terrace/rail, desk và closed laptop được đọc trực tiếp từ **R2 S08-B source**, không thiết kế lại. Chỉ bỏ R2 parent/child/ghế và ẩn typography để nhìn rõ nhân vật, chèn A pair + seat mới trong bản sao revision. Production và R2 source không bị sửa. Desk vẫn occlude thân/legs ở foreground. Cảnh này là neutral character evaluation trong context cũ, không phải scene redesign hoặc một frame được gọi là approved.

Pose A contact dùng parent shoulder `(43,-126)`, elbow `(71,-55)`, wrist `(128,-80)` trong local hip space; projected segment lengths xấp xỉ **76/62 drawing units**. Child shoulder/elbow/wrist sau placement là `(176,-55)`, `(163,-19)`, `(147,-60)`, xấp xỉ **38/44 units**. Hai bàn tay được vẽ riêng và xoay về nhau; đã xem crop thật để loại bỏ khoảng hở của bản thử đầu. Đây là **light finger/palm contact**, không claim đã dựng finger interlock hoặc hand hold tự nhiên qua motion.

Seated A near hip–knee/knee–ankle là khoảng **117/113 units**, gần với standing reference tương ứng khoảng **115/119 units**. Những đo này kiểm sự bất thường của projected drawing, không phải giải phẫu 3D hay human-performance validation. Knee fold và shoe baseline giúp đọc support. Feet được kiểm ở pose tĩnh; walking sheet là một pose có chân nhận trọng lượng và chân kia nhẹ hơn, chưa phải gait/contact solve.

## Quality checks và giới hạn

- Render bằng existing Puppeteer/headless Chrome, cùng tooling của R2; không cài engine/dependency/font. SVG XML, source requests/runtime, duplicate IDs và repeated static capture được kiểm; kết quả/hashes ở [qa/verification.json](qa/verification.json), [browser checks](qa/browser-checks.json), [asset ledger](asset-ledger.json).
- Đã xem cả ba sheet render, actual R2 comparison, scene-size mobile A/B/C, S08 mobile và contact crop. Chữ design-sheet chỉ là nhãn review, không được đưa vào video như subtitle.
- Cast silhouettes/wardrobe/head treatment đã khác nhau; phần soft tissue và biểu cảm vẫn được giản lược. Các pose đứng/đi chưa có turnaround đầy đủ; nét mặt resident cố ý đơn giản vì chỉ là background candidate.
- **Chưa kiểm:** chuyển động, anatomical continuity qua mọi góc, gaze tracking động, finger articulation/IK, walk/run cycles, chair rotation và AV sync. Đồ họa đẹp hay appealing không thể kết luận chỉ bằng render pass.
- Giới hạn của cách author bằng code ở đây là kiểm soát nét/contour tinh tế và diễn xuất tay: việc có tọa độ/joint hợp lý không tự tạo một pose đẹp. Nếu các hướng này vẫn chưa đạt taste bạn cần, bước thực tế nên là một **draw-over/sketch art pass được duyệt**, rồi vẽ sạch Bézier trong vector editor hoặc nhận SVG gốc từ illustrator. Sau đó mới tách đúng nhóm để animate trong tooling hiện có. Không tiếp tục tạo nhiều biến thể bằng đổi màu hoặc thêm chi tiết mắt để thay cho art pass đó; cũng không cần engine mới.

## Safety và review gate

R2 và production được hash trước/sau, dữ liệu trong [protected-before.json](protected-before.json) và verification. Original audio, 17 intervals, manifest, timestamps, Esora logo, AGENTS, setup và historical projects không được ghi bởi source/capture của revision này. R2 rejected characters giữ nguyên để đối chiếu/rollback; quyết định từ chối chỉ ghi vào [review-state.json](review-state.json) mới, không sửa state cũ thành approved.

**Dừng tại CHARACTER DESIGN REVIEW.** Bạn có thể chọn A/B/C hoặc chỉ rõ phần nào cần thay. Không animate S03/S08, không render pilot MP4 và không mở scene khác trước khi có bước được ủy quyền tiếp theo.
