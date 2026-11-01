> CURRENT: R1 direction and mapping at end supersede the original warm/pastel draft. Pilot NOT APPROVED; AWAITING HUMAN REVIEW.

# VIDEO-34 — Storyboard toàn phim

**Trạng thái: DRAFT để review, không phải pilot approval.** Ngày lập: 2026-11-01.
Working preferred direction: **Warm Mediterranean Editorial Illustration**. 9:16 đã được người dùng chọn; palette, nhân vật, font, độ phân giải, FPS và chi tiết art direction dưới đây vẫn là đề xuất.

## Nguồn và giới hạn

Tiếp tục project video-34; không tạo lại manifest. Nguồn timing duy nhất: `../inputs/scene-manifest.json`, schema v2, 17 scene, PCM 24.000 Hz, tổng 2.232.960 samples = 93,04 giây. Master WAV giữ nguyên; không viết lại voice, không time-stretch và không kéo dài outro.

Các khoảng bên dưới là `[start_sample, end_sample)` chính xác. Số giây in 6 chữ số thập phân chỉ để đọc; giá trị chính xác là sample/24000. Chưa quy đổi sang frame vì FPS chưa được chốt. Transcript ASR và corrected_text được chép nguyên từ manifest, không phải bản sửa nội dung mới. Anchor dùng ID từ 1 trong `word-timestamps.json`; giữ nguyên token ASR để đối chiếu, không gán timestamps mới cho bản sửa chính tả. Các khoảng anchor là cửa sổ nhận diện từ, không ép toàn bộ cử động hoàn tất trong một âm tiết.

Tham chiếu: proposal hiện có, audio-intake-verification, logo thật trong asset ledger; các skill HyperFrames, animation/GSAP, creative và voice-to-scene-design. Toàn bộ scene được **đề xuất HF_ONLY / HyperFrames + GSAP**, vì cần minh họa SVG, phối cảnh 2D, acting theo từ và seeking độc lập. Đây là lựa chọn theo capability, không phải quy tắc engine cho phong cách. Không cần Google Flow, footage sinh mới hoặc Remotion cho kế hoạch này. FFmpeg dành cho assembly sau này. Không tạo source/entry/render command ở bước storyboard.

## Mạch kể và continuity

**Câu chuyện thị giác:** “Một nhịp sống quen thuộc, trong một nơi ở mới; giá trị cuối cùng là có mặt bên nhau.” Không minh họa từng danh từ bằng một icon. Mỗi cảnh có một thay đổi có thể quan sát được, thay đổi ấy dẫn người xem đến ý tiếp theo.

| Chặng | Scenes | Sự phát triển / nhịp cảm xúc |
|---|---|---|
| Nhận ra điểm chung | S01–S05 | Hai nơi có thói quen giống nhau. Mở gọn → mở rộng thế giới Malta ở S03 → nhận diện Việt Nam bằng chi tiết phin/cử chỉ ở S04 → góc trên cao ở S05. |
| Từ nơi chốn đến thuộc về | S06–S08 | Vật quen trong ngôi nhà mới → nhìn ra hạ tầng xung quanh → chuyển trọng tâm sang hành động dành thời gian cho con. S08 là điểm xoay cảm xúc đầu tiên. |
| Chất lượng sống được trải nghiệm | S09–S12 | Tò mò của trẻ → sự thư thả của người lớn → mong muốn của phụ huynh → trẻ chủ động kết nối. Không biến thành checklist quyền lợi. |
| Cầu nối thương mại | S13–S14 | Một khoảnh khắc tham vấn trung tính, rồi hình ảnh ngưỡng cửa gia đình. S13 phải factual review; không dùng visual để làm mạnh lời hứa còn chưa xác minh. |
| Lời kết con người | S15–S17 | Bỏ nhịp vội → bước cùng con → ngồi bên người thân. Góc máy gần dần, ít sự kiện hơn; logo Esora là chữ ký cuối trong thời lượng có sẵn. |

### Không gian, thời gian và chủ thể

- Malta: phố đá vôi, ban công kín/gallarija có màu, lối dạo sát biển, quảng trường nhỏ/café; nhà và sân nhìn ra ánh sáng. Đây là **thế giới minh họa tổng hợp lấy cảm hứng Malta**, không gán một bãi biển cát vào tuyến phố Valletta có thật. Không dùng mái vòm trắng-xanh kiểu hình ảnh du lịch nơi khác để thay Malta.
- Việt Nam: phin, bóng cây, công viên và bờ sông; dùng chi tiết sinh hoạt, không dồn nón lá/cờ/landmark vào khung hình để báo quốc gia.
- S01 là hai vignette tách địa lý. S02–S03 là thế giới Malta; S04 là match cut vật thể sang Việt Nam; S05 duy trì Việt Nam. S06 đổi sang nhà ở Malta bằng cut rõ, có vật quen làm cầu nối, không giả chuyến di chuyển hay tuyến đường địa lý liên tục.
- Đề xuất một gia đình Việt lặp lại ở S06/S08/S11/S14–S17: hai phụ huynh khoảng 30–40 tuổi, một con khoảng 7–9 tuổi. Casting, tuổi và trang phục chưa được duyệt; không giả là khách hàng thật. Cư dân S01/S03 là người nền khác; không morph họ thành gia đình chính. Người lớn tuổi ở S10 có thể độc lập, không bắt buộc tăng số thế hệ của family rig.
- Buổi chiều ấm là ánh sáng chính cho chuỗi Malta; S03 không đổi sáng sang chiều chỉ vì voice nói hai thời điểm. Các cảnh Việt Nam là hình ảnh đối chiếu, không dựng như cùng một buổi đi bộ. Nhịp kết chậm hơn nhờ ít hành động/camera hơn, không đổi tốc độ voice.
- Esora hiện diện rõ ở cuối S17 bằng logo gốc. Chưa tự đặt CTA/số điện thoại/slogan hay watermark mọi scene. S13 chỉ là ngữ cảnh tham vấn, không giao dịch/giấy phép đã được chấp thuận.

### Ngữ pháp chuyển cảnh

Dùng cut theo ý nghĩa và điểm nhìn là chính. Match đường chân trời S01→02; cup match S03→04; chuyển tiêu điểm cửa sổ S07→08; gaze cut S08→09; cut hình bàn tay S15→16. Các nối khác dùng cut sạch hoặc che khuất bởi vật thể đã có lý do trong cảnh. Không dùng một wipe/morph cho mọi scene; không nhét chuyển cảnh vào từ cuối làm mất ý. Chỉ carry visual handle trong khoảng scene hiện có; không chồng/di chuyển master audio. Các cảnh độc lập phải có trạng thái đầu/cuối có nghĩa, không phụ thuộc timeline toàn phim để render đúng.

### Kiểm soát lặp hình

| Cặp / nhóm dễ lặp | Cách phân biệt bắt buộc khi dựng bản nháp |
|---|---|
| S03 / S05: chuỗi sinh hoạt | S03 đường bờ biển nhìn xiên, chiều sâu và người chạy; S05 góc cao công viên/bờ sông, lộ trình ngắn, không lặp một lượt camera ghé café rồi ra biển. |
| S03 / S10 / S14 / S16: biển & gia đình | Toàn cảnh nhiều hoạt động / người lớn ngồi yên / nhìn qua ngưỡng cửa / cận bước chân và bàn tay. Không dùng lại cùng một panorama chỉ đổi nhân vật. |
| S07 / S11: trường học | S07 nhìn bối cảnh khu dân cư; S11 cận phản ứng phụ huynh và bức vẽ của trẻ. |
| S08 / S15 / S16: thời gian cho con | Quyết định rời công việc / dừng cử chỉ vội / cùng thực hiện hoạt động. Mỗi cảnh phải có một trạng thái mới, không ba lần đóng laptop. |
| S09 / S12: trẻ phát triển | Khám phá cây cỏ / tương tác trao bóng với bạn; không hai lần chạy ngoài trời. |
| Cup motif S01 / S04 / S17 | Mở là sự giống nhau; giữa là cầu nối văn hóa; cuối là sự hiện diện bên nhau. Không thêm cup match cut ở các chỗ khác. |

## 17 scene — kế hoạch chi tiết

### S01 — Hai nơi, một nhịp sống

1. **Scene ID:** S01.
2. **Audio chính xác:** `[0, 112563) samples`; `0/24000 → 112563/24000 s` (xấp xỉ 0.000000 → 4.690125 s; dài 4.690125 s).
3. **Transcript gốc ASR:** Người mau ta và người Việt có một điểm rất giống nhau, đều yêu thích cuộc sống ngoài trời.

   **Corrected_text có sẵn:** Người Malta và người Việt có một điểm rất giống nhau: Đều yêu thích cuộc sống ngoài trời

4. **Mục tiêu truyền đạt:** Mở bằng sự gần gũi để người xem Việt có lý do quan tâm đến câu chuyện Malta.
5. **Visual concept:** Hai không gian ban công Việt Nam/Malta cùng hướng ra ánh sáng; hai cử chỉ nâng cốc ăn khớp làm rõ một thói quen chung.
6. **Bối cảnh:** Hai vignette kiến trúc riêng, nối bằng đường chân trời đồ họa; không giả là hai quốc gia kề nhau.
7. **Chủ thể / props / assets dự kiến:** ENV-MT-STREET, ENV-VN-CAFE; hai cư dân nền, cốc gốm/phin; ánh nắng.
8. **Bố cục & hierarchy:** Khung dọc lệch trục: ban công Malta phía trên-trái, sân Việt phía dưới-phải; đường nhìn hội tụ ở bàn tay/cốc, không viền card.
9. **Trạng thái mở:** Cả hai không gian đã có mặt; người xem thấy một hành động đang bắt đầu, không chờ logo intro.
10. **Hành động chính:** Hai người ở hai nơi thực hiện cùng một cử chỉ đời thường.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Hai cảnh vẫn tách biệt về địa lý, cùng nhịp sinh hoạt.
13. **Chuyển sang scene sau:** Đường chân trời ở vị trí khớp dẫn sang S02; không dùng bản đồ nối Việt Nam–Malta.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 2–3: “mau ta” | 0.48–0.90 | 0.480000–0.900000 | Đưa chi tiết ban công Malta vào vùng nhìn chính. |
| 5–6: “người Việt” | 1.10–1.50 | 1.100000–1.500000 | Mở tầng cảnh Việt Nam bằng tán cây và phin cà phê. |
| 11–12: “giống nhau,” | 2.28–2.76 | 2.280000–2.760000 | Hai cử chỉ nâng cốc khớp nhịp; không biến người này thành người kia. |
| 18–19: “ngoài trời.” | 4.06–4.54 | 4.060000–4.540000 | Mở bố cục ra khoảng trời chung về mặt đồ họa. |

15. **Độ phức tạp ước tính:** Vừa — hai vignette, hai cử chỉ ngắn. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Mug, phin, balcony modules, gesture library; không bê cả layout sang cảnh khác.
17. **Creative / factual risks:** So sánh văn hóa là góc kể của script, không thống kê về mọi người Việt/Malta.

**Text inventory:** Tùy chọn “Nhịp sống quen thuộc”; không subtitle. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S02 — Biển và nắng là bối cảnh sống

1. **Scene ID:** S02.
2. **Audio chính xác:** `[112563, 243986) samples`; `112563/24000 → 243986/24000 s` (xấp xỉ 4.690125 → 10.166083 s; dài 5.475958 s).
3. **Transcript gốc ASR:** Có lẽ việc cùng gắn liền với biển và khi hậu nhiều nắng, người mau ta cũng có lối sống khá giống người Việt.

   **Corrected_text có sẵn:** Có lẽ vì cùng gắn liền với biển và khí hậu nhiều nắng, người Malta cũng có lối sống khá giống người Việt.

4. **Mục tiêu truyền đạt:** Đặt chất Địa Trung Hải bằng không gian, không bằng một danh sách biểu tượng.
5. **Visual concept:** Điểm nhìn qua hiên đá ra mặt biển; bóng lan can và ánh sáng cho thấy nơi chốn có thể sống, không chỉ một bưu thiếp.
6. **Bối cảnh:** Coastal street minh họa lấy cảm hứng Malta: đá màu mật ong, ban công gỗ khép, mặt biển xa.
7. **Chủ thể / props / assets dự kiến:** ENV-MT-STREET, sea horizon, balcony, awning; không cần nhân vật.
8. **Bố cục & hierarchy:** Khung cửa tiền cảnh tạo chiều sâu; biển chiếm điểm nghỉ phía trên, bóng nắng dẫn mắt xuống tuyến đi bộ.
9. **Trạng thái mở:** Chân trời kế thừa S01; tiền cảnh vẫn mở.
10. **Hành động chính:** Cảnh quan được lộ dần bằng chuyển điểm nhìn nhẹ qua mép hiên.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Một promenade có thể đi vào, không phải màn hình thông tin.
13. **Chuyển sang scene sau:** Mép lan can dẫn vị trí người đi bộ ở S03; giữ chiều ánh sáng.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 24–27: “gắn liền với biển” | 5.70–6.50 | 1.009875–1.809875 | Lộ đường ven biển dưới hiên. |
| 29–32: “khi hậu nhiều nắng,” | 6.66–7.42 | 1.969875–2.729875 | Bóng nắng trên đá trở thành nét dẫn mắt, không sun-icon bật ra. |
| 38–43: “lối sống khá giống người Việt.” | 8.66–9.84 | 3.969875–5.149875 | Đặt đường đi bộ vào khung; chuẩn bị cho người xuất hiện ở S03. |

15. **Độ phức tạp ước tính:** Thấp–vừa — ánh sáng và reframe nhỏ. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** MT street kit, balcony, rail, sea plane.
17. **Creative / factual risks:** Không mô tả nắng quanh năm hay khí hậu Malta giống hệt Việt Nam; không gắn địa danh cụ thể cho cảnh tổng hợp.

**Text inventory:** “Malta” nếu cần định vị, xuất hiện một lần. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S03 — Một bờ biển đang sống — PILOT CANDIDATE

1. **Scene ID:** S03.
2. **Audio chính xác:** `[243986, 458528) samples`; `243986/24000 → 458528/24000 s` (xấp xỉ 10.166083 → 19.105333 s; dài 8.939250 s).
3. **Transcript gốc ASR:** Họ thích đi bộ vào buổi sáng hoặc chiều muộn, chạy bộ dọc bơ biển, ngồi cà phê ngoài trời, gặp gỡ bạn bè tại các quản trường, hay dành cuối tuần cùng gia đình bên bãi biển.

   **Corrected_text có sẵn:** Họ thích đi bộ vào buổi sáng hoặc chiều muộn, chạy bộ dọc bờ biển, ngồi cà phê ngoài trời, gặp gỡ bạn bè tại các quảng trường hay dành cuối tuần cùng gia đình bên bãi biển.

4. **Mục tiêu truyền đạt:** Cho thấy nhiều cách tận hưởng ngoài trời trong một thế giới có spatial continuity.
5. **Visual concept:** Theo một dải promenade nối quán café, pocket-square và góc nhìn ra vịnh; thay điểm chú ý trong không gian liên tục thay vì thay icon.
6. **Bối cảnh:** Coastal composite có logic tiếp giáp: đường đi bộ trước dãy nhà đá, café mở ra quảng trường nhỏ, vịnh xa; không tuyên bố đây là bản đồ Valletta.
7. **Chủ thể / props / assets dự kiến:** ENV-MT-COAST-PLAZA, walkers, runner, café friends, beach family; rail, bàn/cốc, ghế, parasol, beach silhouettes.
8. **Bố cục & hierarchy:** Tuyến nhìn chéo từ giữa lên-phải rồi về thấp-phải; hero thay đổi theo cue, các khu còn lại được thấy trước ở mức phụ.
9. **Trạng thái mở:** Walkers đã ở promenade; café và vịnh là ngữ cảnh, chưa tranh sự chú ý.
10. **Hành động chính:** Camera/layout chuyển trọng tâm trong cùng một môi trường, từng hành động khớp cụm lời đọc.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Gia đình bên bờ biển là trọng tâm; dấu café còn ở tiền cảnh, giữ cảm giác một thế giới.
13. **Chuyển sang scene sau:** Trong bản phim đầy đủ, cốc/cánh tay ở mép tiền cảnh tạo điểm nối S04; không kéo dài audio hay overlap voice. Pilot phải có entry/resolve tự đủ.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 46–53: “đi bộ vào buổi sáng hoặc chiều muộn,” | 10.50–12.18 | 0.333917–2.013917 | Walkers bước đều trong ánh chiều; không đổi sáng–chiều trong một giây. |
| 54–58: “chạy bộ dọc bơ biển,” | 12.40–13.26 | 2.233917–3.093917 | Runner vượt theo cùng tuyến; cận cảnh bàn chân/nhịp tay đủ gợi chạy. |
| 59–63: “ngồi cà phê ngoài trời,” | 13.58–14.52 | 3.413917–4.353917 | Trọng tâm chuyển sang café; một người đặt cốc xuống mặt bàn thật. |
| 64–71: “gặp gỡ bạn bè tại các quản trường,” | 14.84–16.34 | 4.673917–6.173917 | Người bạn chào bằng mắt/tay; quảng trường lộ sau bàn, không thêm một sân khấu mới. |
| 74–81: “cuối tuần cùng gia đình bên bãi biển.” | 16.88–18.58 | 6.713917–8.413917 | Tầm nhìn mở về gia đình bên vịnh; child/parent gesture trở thành điểm chốt. |

15. **Độ phức tạp ước tính:** Cao — nhiều hoạt động trong 8.93925 s, kiểm soát camera và mức chú ý. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Coast/plaza/café modules, runner and walk poses, hand/cup contact, path-based attention choreography.
17. **Creative / factual risks:** Quá tải nhân vật/camera; rút bớt secondary acting trước khi tăng tốc. Vịnh/café/plaza là môi trường tổng hợp, không claim địa lý thật hay bãi cát nằm trong Valletta.

**Text inventory:** Không có text mô tả hoạt động. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S04 — Cử chỉ ấy rất quen

1. **Scene ID:** S04.
2. **Audio chính xác:** `[458528, 533049) samples`; `458528/24000 → 533049/24000 s` (xấp xỉ 19.105333 → 22.210375 s; dài 3.105042 s).
3. **Transcript gốc ASR:** Đó cũng là những hình ảnh rất quen thuộc ở Việt Nam.

   **Corrected_text có sẵn:** Đó cũng là những hình ảnh rất quen thuộc ở Việt Nam.

4. **Mục tiêu truyền đạt:** Tạo cú nhận ra Việt Nam bằng chi tiết, không lặp lại panorama.
5. **Visual concept:** Cận bàn tay/cốc từ S03 khớp sang ly café/phin ở một sân Việt; âm hưởng hoạt động giống nhau, dụng cụ và vật liệu khác nhau.
6. **Bối cảnh:** Sân café Việt có bóng lá và ghế thấp; chỉ đủ dấu hiệu bối cảnh, không địa danh hư cấu.
7. **Chủ thể / props / assets dự kiến:** PROP-PHIN, cup, hands; ENV-VN-CAFE close crop.
8. **Bố cục & hierarchy:** Macro tabletop chiếm trung tâm; mặt người không cần xuất hiện; khoảng trời nhỏ phản trong ly.
9. **Trạng thái mở:** Điểm chạm cốc còn khớp vị trí cuối S03.
10. **Hành động chính:** Dùng match composition để chuyển nơi, giữ hành động nâng/đặt cốc.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Một chi tiết Việt đủ rõ; không cần mở thêm bộ icon quốc gia.
13. **Chuyển sang scene sau:** Bóng lá trên bàn mở thành tán cây công viên S05.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 86–88: “hình ảnh rất” | 20.34–20.92 | 1.234667–1.814667 | Cho thấy chất liệu bàn, ly và bóng lá thay đổi. |
| 89–93: “quen thuộc ở Việt Nam.” | 20.92–21.82 | 1.814667–2.714667 | Phin và nhịp tay xác lập cảm giác quen thuộc ở Việt Nam. |

15. **Độ phức tạp ước tính:** Thấp — một raccord vật thể, ít nhân vật. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Cup/hand kit; phin silhouette; leaf shadows.
17. **Creative / factual risks:** Chỉ 3.105 s; không nhồi montage hay dùng biểu tượng văn hóa rập khuôn.

**Text inventory:** Tùy chọn “Việt Nam”, không đồng thời thêm tiêu đề khác. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S05 — Nhịp Việt ở góc nhìn khác

1. **Scene ID:** S05.
2. **Audio chính xác:** `[533049, 682209) samples`; `533049/24000 → 682209/24000 s` (xấp xỉ 22.210375 → 28.425375 s; dài 6.215000 s).
3. **Transcript gốc ASR:** Người Việt thích dạo công viên, đi bộ ven xong, ngồi quán cà phê trò chuyện, hay đưa con đi biển vào dịp cuối tuần.

   **Corrected_text có sẵn:** Người Việt thích dạo công viên, đi bộ ven sông, ngồi quán cà phê trò chuyện hay đưa con đi biển vào dịp cuối tuần.

4. **Mục tiêu truyền đạt:** Phản chiếu S03 nhưng có cách dựng riêng, tránh hai cảnh liệt kê cùng layout.
5. **Visual concept:** Góc nhìn chếch cao của công viên ven sông: cùng một tuyến cây xanh chứa người đi dạo, café mép đường; cuối cảnh đổi sang cận tay đưa con đi.
6. **Bối cảnh:** Park/riverside Việt minh họa; biển cuối tuần là một ý nghĩ nối hình, không giả sông và biển nằm cùng địa điểm.
7. **Chủ thể / props / assets dự kiến:** ENV-VN-PARK-RIVER, small café cluster, parent/child hands, bag, water plane.
8. **Bố cục & hierarchy:** Tán cây tạo mảng lớn phía trên; tuyến đi bộ uốn trong nền, ending cận tay phá layout toàn cảnh.
9. **Trạng thái mở:** Tán cây từ S04 chuyển thành park canopy nhìn từ trên.
10. **Hành động chính:** Theo một tuyến sinh hoạt rồi chuyển độ lớn sang tương tác cha/mẹ–con.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Tay người lớn nắm tay trẻ; không kết bằng một stock beach icon.
13. **Chuyển sang scene sau:** Bàn tay đưa chiếc túi quen vào S06, nối thói quen sang câu chuyện chuyển nơi sống.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 97–103: “dạo công viên, đi bộ ven xong,” | 23.16–24.78 | 0.949625–2.569625 | Đi dạo công viên và ven sông chia sẻ một đường đi, không hai shot lặp. |
| 104–109: “ngồi quán cà phê trò chuyện,” | 25.10–26.24 | 2.889625–4.029625 | Café đã có trong mép cảnh; nhịp trò chuyện được gợi bằng hai cử chỉ. |
| 111–118: “đưa con đi biển vào dịp cuối tuần.” | 26.54–28.02 | 4.329625–5.809625 | Cận tay đưa con, chuyển nền nước thành gợi ý chuyến đi biển cuối tuần. |

15. **Độ phức tạp ước tính:** Vừa — overhead world và một scale-change có động cơ. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** VN park/café kit, family hands, bag; không reuse S03 camera path.
17. **Creative / factual risks:** Dễ lặp S03; giữ overhead và intimate ending, chỉ ba trọng tâm. Không dùng bản đồ sai để nối sông với biển.

**Text inventory:** Không cần text mới. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S06 — Mang điều quen thuộc đến một nơi mới

1. **Scene ID:** S06.
2. **Audio chính xác:** `[682209, 856238) samples`; `682209/24000 → 856238/24000 s` (xấp xỉ 28.425375 → 35.676583 s; dài 7.251208 s).
3. **Transcript gốc ASR:** Chính sự tương đồng trong nhiệm sống này giúp nhiều gia đình Việt cảm thấy mau ta không quá xa lạ khi chuyển đến sân sống.

   **Corrected_text có sẵn:** Chính sự tương đồng trong nhịp sống này giúp nhiều gia đình Việt cảm thấy Malta không quá xa lạ khi chuyển đến sinh sống.

4. **Mục tiêu truyền đạt:** Chuyển từ quan sát hai cộng đồng sang sự gắn bó của một gia đình.
5. **Visual concept:** Gia đình đặt chiếc túi/cốc quen xuống một căn nhà mới; trẻ nhận ra biển ngoài cửa, người lớn thả lỏng khi mở ban công.
6. **Bối cảnh:** ENV-MT-HOME, góc bàn/giá đồ và cửa ban công nhìn ra khu phố.
7. **Chủ thể / props / assets dự kiến:** Family A, bag, cup, small plant, balcony door; không hồ sơ visa được đóng dấu.
8. **Bố cục & hierarchy:** Cận tay/vật dụng dẫn lên gương mặt rồi khoảng cửa; dùng chiều dọc để thể hiện từ đồ vật đến nơi chốn.
9. **Trạng thái mở:** Bắt đầu ở chiếc túi, tận dụng khoảng thở trước từ đầu tiên mà không kéo audio.
10. **Hành động chính:** Đặt vật quen vào nhà mới rồi hướng sự chú ý ra không gian ngoài trời.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Cả nhà cùng hướng nhìn ra ngoài; vật quen còn giữ tiền cảnh.
13. **Chuyển sang scene sau:** Khung cửa nối điểm nhìn ra khu phố S07.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 121–125: “tương đồng trong nhiệm sống” | 29.64–30.58 | 1.214625–2.154625 | Cốc/túi được đặt đúng chỗ, nhịp hoạt động quen thuộc. |
| 129–135: “gia đình Việt cảm thấy mau ta” | 31.44–32.68 | 3.014625–4.254625 | Gia đình cùng nhìn hướng cửa Malta; một ánh mắt trao nhau. |
| 136–144: “không quá xa lạ khi chuyển đến sân sống.” | 32.68–34.80 | 4.254625–6.374625 | Cửa mở, vai người lớn thư giãn; không màn ăn mừng nhập cư thành công. |

15. **Độ phức tạp ước tính:** Vừa — hand contact, gaze và body settling. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Home/workspace/terrace kit dùng tiếp S07–08; cup/bag; family poses.
17. **Creative / factual risks:** Không ngụ ý mọi gia đình đều hòa nhập dễ dàng; cảnh minh họa, không testimonial thật hoặc bảo đảm hồ sơ.

**Text inventory:** Không text mới; cảm giác “thuộc về” do acting. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S07 — Giá trị không dừng ở các công trình

1. **Scene ID:** S07.
2. **Audio chính xác:** `[856238, 966480) samples`; `856238/24000 → 966480/24000 s` (xấp xỉ 35.676583 → 40.270000 s; dài 4.593417 s).
3. **Transcript gốc ASR:** Một trong những điều làm nên chất lượng sống của mau ta không chỉ là hệ thống giáo dục hay y tế,

   **Corrected_text có sẵn:** Một trong những điều làm nên chất lượng sống của Malta không chỉ là hệ thống giáo dục hay y tế,

4. **Mục tiêu truyền đạt:** Chuẩn bị câu “không chỉ… mà còn…” mà không kết luận sớm.
5. **Visual concept:** Từ cửa nhà nhìn ra một khu phố có trường học và cơ sở chăm sóc sức khỏe giản lược; điểm nhìn rời công trình để tiến về một cửa sổ có con người.
6. **Bối cảnh:** MT neighbourhood generic; trường/clinic không dùng tên, xếp hạng hoặc logo thật.
7. **Chủ thể / props / assets dự kiến:** ENV-MT-STREET + school/clinic façades; window/workspace aperture.
8. **Bố cục & hierarchy:** Kiến trúc là ngữ cảnh, một cửa sổ sáng có hoạt động là điểm đến; không ba feature cards.
9. **Trạng thái mở:** Tiếp khung nhìn ngoài cửa từ S06, giữ cùng tông đá/biển.
10. **Hành động chính:** Đổi trọng tâm từ hạ tầng sang nhịp sống trong căn nhà.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Cửa sổ làm điểm nối, câu chuyện chưa “đóng” vì lời đọc vẫn nối.
13. **Chuyển sang scene sau:** Cut qua khung cửa vào cùng không gian làm việc S08; không title bumper.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 151–156: “chất lượng sống của mau ta” | 36.96–38.06 | 1.283417–2.383417 | Đặt chất lượng sống trong cả khu phố thay vì badge chứng nhận. |
| 157–166: “không chỉ là hệ thống giáo dục hay y tế,” | 38.06–40.20 | 2.383417–4.523417 | Đi qua school/clinic cues, dừng sự chú ý ở cửa sổ dẫn sang S08. |

15. **Độ phức tạp ước tính:** Vừa — kiến trúc và một push-in có mục đích. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** MT street façades, window/door module, home stage.
17. **Creative / factual risks:** Không gán cấp chất lượng giáo dục/y tế, miễn phí hay quyền hưởng dịch vụ chưa xác minh. S07/S11 khác nhau: nơi chốn so với góc nhìn phụ huynh.

**Text inventory:** Không nhãn “giáo dục tốt/y tế tốt”. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S08 — Từ công việc đến hiện diện bên gia đình — PILOT CANDIDATE

1. **Scene ID:** S08.
2. **Audio chính xác:** `[966480, 1101123) samples`; `966480/24000 → 1101123/24000 s` (xấp xỉ 40.270000 → 45.880125 s; dài 5.610125 s).
3. **Transcript gốc ASR:** mà còn là văn hóa sống chậm, cân bằng giữa công việc và thời gian dành cho bản thân, gia đình.

   **Corrected_text có sẵn:** mà còn là văn hóa sống chậm, cân bằng giữa công việc và thời gian dành cho bản thân, gia đình.

4. **Mục tiêu truyền đạt:** Làm thấy sự chuyển đổi nhịp sống qua hành động và quan hệ, không biểu tượng cân bằng.
5. **Visual concept:** Một phụ huynh kết thúc thao tác ở bàn, khép laptop và xoay người về phía con trong không gian nhà–terrace liền nhau.
6. **Bối cảnh:** ENV-MT-HOME-WORK-TERRACE, cùng căn nhà S06, không đổi setting giữa hai câu.
7. **Chủ thể / props / assets dự kiến:** Parent A, child, laptop với màn hình không đọc được nội dung, ghế, bàn, cửa mở, cây, hand-contact poses.
8. **Bố cục & hierarchy:** Bàn ở thấp-trái/giữa; terrace và con ở sâu-phải; điểm nhìn chuyển theo ánh mắt và tay, không chia đôi bằng khung card.
9. **Trạng thái mở:** Parent đang làm việc; ánh sáng và terrace đã tồn tại như một khả năng, không xuất hiện phép màu.
10. **Hành động chính:** Rời thao tác công việc, đổi hướng cơ thể và dành sự chú ý cho người thân.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Hai người đã có kết nối, bàn làm việc còn trong môi trường nhưng không còn là focal point.
13. **Chuyển sang scene sau:** Trong phim, hướng nhìn của trẻ dẫn xuống S09; pilot tự resolve, không giả S03→S08 là cùng một đoạn voice.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 167–173: “mà còn là văn hóa sống chậm,” | 40.42–41.82 | 0.150000–1.550000 | Nhịp tay chậm lại; vai/hơi thở dịu, không đóng laptop quá sớm. |
| 174–175: “cân bằng” | 42.14–42.48 | 1.870000–2.210000 | Hands settle; chuẩn bị đổi ưu tiên chứ không bật icon cân. |
| 177–178: “công việc” | 42.68–42.98 | 2.410000–2.710000 | Khép laptop có hinge/contact rõ ràng. |
| 180–185: “thời gian dành cho bản thân.” | 43.30–44.48 | 3.030000–4.210000 | Xoay ghế/nhìn về terrace; tay rời bàn, người hướng sang con. |
| 186–187: “Giá đình,” | 45.00–45.38 | 4.730000–5.110000 | Tay con và phụ huynh chạm nhau, ánh mắt có reciprocity. |

15. **Độ phức tạp ước tính:** Cao — 5.610125 s nhưng contact/acting phải tự nhiên, không mannequin. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Home stage, laptop-hinge, half-turn/hand-hold poses, gaze/attention handoff.
17. **Creative / factual risks:** Không thể hiện MPRP tự cấp quyền làm việc; đây là nhịp sinh hoạt minh họa. Token ASR “Giá đình” được map về lời hiệu đính “gia đình”, giữ nguyên timing.

**Text inventory:** Không cần text “work/life balance”. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S09 — Thế giới ở tầm mắt trẻ

1. **Scene ID:** S09.
2. **Audio chính xác:** `[1101123, 1210802) samples`; `1101123/24000 → 1210802/24000 s` (xấp xỉ 45.880125 → 50.450083 s; dài 4.569958 s).
3. **Transcript gốc ASR:** trẻ em có nhiều cơ hội tham gia các hoạt động ngoài trời, vận động và khám phá thiền nhiên.

   **Corrected_text có sẵn:** Trẻ em có nhiều cơ hội tham gia các hoạt động ngoài trời, vận động và khám phá thiên nhiên.

4. **Mục tiêu truyền đạt:** Cho thấy cơ hội khám phá bằng một trải nghiệm nhỏ có thể cảm nhận.
5. **Visual concept:** Trẻ hạ người nhìn một chồi cây/chi tiết tự nhiên, bước qua dấu nền rồi mời bạn cùng quan sát.
6. **Bối cảnh:** Community garden/đường dạo gần khu ở; người lớn trong ngữ cảnh, không trẻ một mình trên mép biển.
7. **Chủ thể / props / assets dự kiến:** Child + friend, plant/leaf/stone, safe path, low planting bed; magnifier tùy chọn nếu không quá tải.
8. **Bố cục & hierarchy:** Low-angle gần tầm mắt trẻ, vật khám phá đủ lớn để đọc; không grid hoạt động.
9. **Trạng thái mở:** Tiếp hướng nhìn của trẻ từ S08 bằng một chi tiết tự nhiên.
10. **Hành động chính:** Cúi xuống khám phá, chuyển từ vận động sang tò mò.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Một khám phá được chia sẻ, chuẩn bị điểm nhìn sang người lớn.
13. **Chuyển sang scene sau:** Đường nhìn của trẻ ra ngoài frame nối sang S10; không lặp zoom biển.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 188–200: “trẻ em có nhiều cơ hội tham gia các hoạt động ngoài trời,” | 46.06–48.28 | 0.179875–2.399875 | Trẻ bước vào nơi có thể chơi và khám phá, không school guarantee. |
| 201–202: “vận động” | 48.66–48.96 | 2.779875–3.079875 | Một bước/đổi tư thế có trọng lượng. |
| 204–207: “khám phá thiền nhiên.” | 49.18–49.92 | 3.299875–4.039875 | Dừng ở chi tiết thiên nhiên; ánh mắt/gesture mời cùng nhìn. |

15. **Độ phức tạp ước tính:** Vừa — child acting, không cần camera bay. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Family child poses, garden kit, gaze component; dùng lại S12 theo vai trò khác.
17. **Creative / factual risks:** Không minh họa lợi ích sức khỏe như kết quả bảo đảm; không hoạt động nguy hiểm hoặc chạm động vật được bảo vệ.

**Text inventory:** Không text. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S10 — Khoảng nghỉ dành cho người lớn

1. **Scene ID:** S10.
2. **Audio chính xác:** `[1210802, 1329535) samples`; `1210802/24000 → 1329535/24000 s` (xấp xỉ 50.450083 → 55.397292 s; dài 4.947208 s).
3. **Transcript gốc ASR:** Người lớn có thể tận hưởng không gian công cộng an toàn, sạch đẹp và gần gũi với biển.

   **Corrected_text có sẵn:** Người lớn có thể tận hưởng không gian công cộng an toàn, sạch đẹp và gần gũi với biển.

4. **Mục tiêu truyền đạt:** Tạo khoảng thở và mở rộng lifestyle ra ngoài trẻ em.
5. **Visual concept:** Hai người lớn/người lớn tuổi ngồi nhìn biển từ một ghế công cộng; bàn tay đặt trên tay vịn, một cử chỉ trao đổi yên tĩnh.
6. **Bối cảnh:** Một public terrace có bóng cây và lan can; biển là nền xa, không mở lại panorama S03.
7. **Chủ thể / props / assets dự kiến:** Grandparent/support adult, bench, rail, tree shade, sea strip.
8. **Bố cục & hierarchy:** Side profile rộng vừa; tay/ghế foreground, khoảng biển thoáng phía sau; camera có thể đứng yên.
9. **Trạng thái mở:** Một bàn tay/ghế công cộng đón hướng nhìn S09.
10. **Hành động chính:** Ngồi xuống và trao nhau sự chú ý trong không gian công cộng.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Một khoảng nghỉ có con người, không một biểu tượng tiện ích.
13. **Chuyển sang scene sau:** Bàn tay trên ghế nối bàn tay phụ huynh cầm bản vẽ S11.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 208–217: “Người lớn có thể tận hưởng không gian công cộng” | 50.50–52.64 | 0.049917–2.189917 | Chuyển focal point sang người lớn và môi trường chung. |
| 218–221: “an toàn, sạch đẹp” | 52.64–53.80 | 2.189917–3.349917 | Chỉ biểu đạt nơi chốn được chăm sóc, không shield/checkmark “an toàn tuyệt đối”. |
| 223–226: “gần gũi với biển.” | 54.02–54.70 | 3.569917–4.249917 | Để khoảng biển hoàn tất cảm giác gần gũi. |

15. **Độ phức tạp ước tính:** Thấp–vừa — subtle acting phải có vai trò, không idle loop. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Bench, sea horizon, adult profiles; phối khác S03.
17. **Creative / factual risks:** “An toàn/sạch đẹp” là nhận định trong voice, không claim phổ quát hoặc chỉ số được kiểm chứng.

**Text inventory:** Không thêm safety labels. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S11 — Điều phụ huynh nhìn thấy

1. **Scene ID:** S11.
2. **Audio chính xác:** `[1329535, 1432624) samples`; `1329535/24000 → 1432624/24000 s` (xấp xỉ 55.397292 → 59.692667 s; dài 4.295375 s).
3. **Transcript gốc ASR:** Đối với nhiều bực phủ huyên, điều đáng giá không chỉ là con được học ở một ngôi trường tốt,

   **Corrected_text có sẵn:** Đối với nhiều bậc phụ huynh, điều đáng giá không chỉ là con được học ở một ngôi trường tốt,

4. **Mục tiêu truyền đạt:** Làm rõ góc nhìn phụ huynh trước khi mở ý phát triển toàn diện.
5. **Visual concept:** Một phụ huynh nhìn bức vẽ trẻ mang về; ngôi trường trong hình chỉ là điểm khởi đầu, ánh mắt chuyển sang trẻ bên ngoài khung.
6. **Bối cảnh:** Home tabletop intimate, không bản sao cảnh lớp học/campus S07.
7. **Chủ thể / props / assets dự kiến:** Parent hands, child drawing, bag, table/cup peripheral.
8. **Bố cục & hierarchy:** Over-shoulder/cận bàn tay; bức vẽ không phải chứng chỉ hay brochure trường.
9. **Trạng thái mở:** Bàn tay nhận một vật có ý nghĩa từ S10 về mặt raccord.
10. **Hành động chính:** Từ nhìn trường trong hình sang nhìn chính đứa trẻ.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Trẻ nằm ngoài hướng mắt, cần S12 hoàn thành ý.
13. **Chuyển sang scene sau:** Theo eyeline sang sân chơi/community court S12, không dissolve bức vẽ thành “bằng chứng thật”.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 230–235: “bực phủ huyên, điều đáng giá” | 56.15–57.61 | 0.752708–2.212708 | Parent nâng bản vẽ, phản ứng ấm áp có tiết chế. |
| 236–246: “không chỉ là con được học ở một ngôi trường tốt,” | 57.61–59.67 | 2.212708–4.272708 | School drawing được đặt xuống; ánh nhìn chuyển ra trẻ, câu chưa kết luận. |

15. **Độ phức tạp ước tính:** Vừa — hand/artwork contact và eye line. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Parent close-up poses, drawing prop, tabletop.
17. **Creative / factual risks:** Không logo/ranking trường, không gán kết quả học tập hay tạo chứng từ giả.

**Text inventory:** Không “Trường hàng đầu”. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S12 — Lớn lên trong quan hệ với thế giới

1. **Scene ID:** S12.
2. **Audio chính xác:** `[1432624, 1614842) samples`; `1432624/24000 → 1614842/24000 s` (xấp xỉ 59.692667 → 67.285083 s; dài 7.592417 s).
3. **Transcript gốc ASR:** mà còn là được lớn lên trong một ngôi trường khuyến khích, vận động, giao tiếp và phát triển toàn diện cả về thể chất lẫn tinh thần.

   **Corrected_text có sẵn:** mà còn là được lớn lên trong một môi trường khuyến khích vận động, giao tiếp và phát triển toàn diện cả về thể chất lẫn tinh thần.

4. **Mục tiêu truyền đạt:** Thể hiện vận động, giao tiếp và cảm xúc bằng một chuỗi tương tác liên hệ nhau.
5. **Visual concept:** Trong sân cộng đồng, trẻ chuyền một quả bóng cho bạn; bạn đáp lại, cả hai cùng theo trò chơi. Một hành động có cả vận động và giao tiếp.
6. **Bối cảnh:** Courtyard/garden gắn với môi trường sống, không cam kết dịch vụ giáo dục cụ thể.
7. **Chủ thể / props / assets dự kiến:** Child + friend, adult peripheral, ball, paving, low plants; no brain/heart icon set.
8. **Bố cục & hierarchy:** Wide vừa ở tầm trẻ, nhiều khoảng cho đường bóng và hướng mắt; không infographic cơ thể/tinh thần.
9. **Trạng thái mở:** Trẻ trong eyeline S11 đã ở sân; thế giới mở hơn bức vẽ.
10. **Hành động chính:** Đưa vật cho người khác, nhận đáp lại và tiếp tục chơi.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Quan hệ giữa hai trẻ rõ hơn số lượng hoạt động.
13. **Chuyển sang scene sau:** Hình tròn quả bóng khớp chi tiết ảnh gia đình trong hồ sơ trung tính S13; tránh dùng vòng tròn làm transition mặc định.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 251–258: “lớn lên trong một ngôi trường khuyến khích,” | 60.53–62.25 | 0.837333–2.557333 | Trẻ bước vào môi trường khuyến khích tham gia; pose đón bạn. |
| 259–260: “vận động,” | 62.49–62.83 | 2.797333–3.137333 | Chuyền bóng có tiếp xúc/đường đi và trọng lượng. |
| 261–262: “giao tiếp” | 63.23–63.51 | 3.537333–3.817333 | Eye contact, nhận bóng, đổi lượt. |
| 264–274: “phát triển toàn diện cả về thể chất lẫn tinh thần.” | 63.89–66.21 | 4.197333–6.517333 | Để niềm vui và sự tự tin hiện qua acting; không cộng các chỉ số phát triển. |

15. **Độ phức tạp ước tính:** Vừa–cao — hai nhân vật/contact, nhưng cùng một hành động xuyên cảnh. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Child/gaze/hand kit, ball arc component, garden/court pieces.
17. **Creative / factual risks:** Không medical/educational efficacy claim; không biến bốn ý thành bốn icon.

**Text inventory:** Không bullet list. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S13 — Cân nhắc bước tiếp theo — FACTUAL REVIEW REQUIRED

1. **Scene ID:** S13.
2. **Audio chính xác:** `[1614842, 1753804) samples`; `1614842/24000 → 1753804/24000 s` (xấp xỉ 67.285083 → 73.075167 s; dài 5.790083 s).
3. **Transcript gốc ASR:** Chỉ với khoảng 3,8 tỷ đồng, chương trình thể sân mau ta mang đến cơ hội định cư cho 4 thế hệ,

   **Corrected_text có sẵn:** Chỉ với khoảng 3,8 tỷ đồng, chương trình Thẻ xanh Malta mang đến cơ hội định cư cho 4 thế hệ.

4. **Mục tiêu truyền đạt:** Dành chỗ cho thông tin chương trình mà không khuếch đại phạm vi giá/điều kiện chưa rõ.
5. **Visual concept:** Still-life một hồ sơ tư vấn trung tính bên ảnh gia đình và cửa sổ; bàn tay chỉ mở trang, không đóng dấu “được duyệt”.
6. **Bối cảnh:** Góc bàn Esora/home consultation, không cơ quan nhà nước.
7. **Chủ thể / props / assets dự kiến:** Generic consultation folder, family photo minh họa, hands, small original Esora logo nếu dùng trên bìa; no passport/permit mockup.
8. **Bố cục & hierarchy:** Một vật thể thật làm focal point, ít chi tiết; giữ nhịp đọc số, không hero-price/giá gạch ngang.
9. **Trạng thái mở:** Ảnh gia đình nhận raccord từ S12, không thêm lời hứa.
10. **Hành động chính:** Mở trang thông tin và nhìn về không gian gia đình.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Thông tin còn ở trạng thái cân nhắc/tư vấn, không kết quả pháp lý.
13. **Chuyển sang scene sau:** Mép cửa sổ dẫn sang khung kiến trúc thật S14; không visa-stamp wipe.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 278–281: “3 ,8 tỷ đồng,” | 68.18–69.10 | 0.894917–1.814917 | Giữ visual trung tính trong lúc voice đọc giá; không hiện số hoặc “trọn gói”. |
| 282–293: “chương trình thể sân mau ta mang đến cơ hội định cư” | 69.46–71.76 | 2.174917–4.474917 | Trang mở cho hành động tìm hiểu, không tiến độ phê duyệt hồ sơ. |
| 295–297: “4 thế hệ,” | 72.02–72.64 | 4.734917–5.354917 | Nhìn về ảnh gia đình, không vẽ sơ đồ bốn thế hệ tự động đủ điều kiện. |

15. **Độ phức tạp ước tính:** Thấp về hình; cao về factual sign-off. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Folder/hand/photo props, home surface; original logo optional.
17. **Creative / factual risks:** FACTUAL REVIEW REQUIRED: phạm vi “3,8 tỷ”, điều kiện người phụ thuộc, cách gọi “Thẻ xanh”. Voice giữ nguyên; chưa chốt public release cảnh này chỉ bằng visual trung tính.

**Text inventory:** Không hiện “3,8 tỷ”, “4 thế hệ”, “trọn gói” hay badge quyền lợi trước factual review. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S14 — Một cánh cửa mở vào đời sống

1. **Scene ID:** S14.
2. **Audio chính xác:** `[1753804, 1952400) samples`; `1753804/24000 → 1952400/24000 s` (xấp xỉ 73.075167 → 81.350000 s; dài 8.274833 s).
3. **Transcript gốc ASR:** không chỉ mở ra cánh cưa đến châu Âu, đây còn là cơ hội để cả gia đình tận hữu một lối sống lạnh mạnh gần của vi thi nhiên dạc cân bằng hơn mỗi ngày.

   **Corrected_text có sẵn:** Không chỉ mở ra cánh cửa đến Châu Âu, đây còn là cơ hội để cả gia đình tận hưởng một lối sống lành mạnh, gần gũi với thiên nhiên và cân bằng hơn mỗi ngày.

4. **Mục tiêu truyền đạt:** Đưa cảm xúc trở lại sau đoạn thông tin chương trình.
5. **Visual concept:** Qua một doorway Malta, cùng gia đình bước ra một khoảng sân/đường đi có thiên nhiên; “cánh cửa” là không gian sống, không cổng pháp lý vào toàn EU.
6. **Bối cảnh:** Doorway + courtyard + biển xa, ghép từ home/street kit theo một góc mới.
7. **Chủ thể / props / assets dự kiến:** Family A, timber door/stone frame, tree, shared path; không EU passport, flags hay map cấp quyền.
8. **Bố cục & hierarchy:** Doorframe lệch trục, nhân vật ở độ sâu giữa; bầu trời mở dần rồi hạ trọng tâm về quan hệ trong nhà.
9. **Trạng thái mở:** Khung cửa kế thừa S13, chưa là logo reveal.
10. **Hành động chính:** Đi qua cửa vào một hoạt động đời thường của gia đình.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Giữ nhịp êm ở đoạn cuối; không hard transition lên từ “Bởi” đang băng boundary.
13. **Chuyển sang scene sau:** Match vị trí bàn tay sang S15; hình chuyển nhẹ, master audio liên tục không bị trim/overlap.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 300–306: “mở ra cánh cưa đến châu Âu,” | 73.52–75.02 | 0.444833–1.944833 | Mở cửa vật lý và lộ không gian Malta. |
| 313–322: “cả gia đình tận hữu một lối sống lạnh mạnh” | 76.28–78.38 | 3.204833–5.304833 | Gia đình bước cùng nhau; vai/ánh mắt tạo cảm giác nhẹ nhõm. |
| 323–333: “gần của vi thi nhiên dạc cân bằng hơn mỗi ngày.” | 78.38–80.88 | 5.304833–7.804833 | Hạ tốc độ, đặt thiên nhiên trong ngữ cảnh để chuẩn bị kết luận cảm xúc. |

15. **Độ phức tạp ước tính:** Vừa — door occlusion + family staging. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Door/home/street/family kit, nhưng camera angle không lặp S06.
17. **Creative / factual risks:** Không ngụ ý quốc tịch/quyền sống-làm việc toàn EU. ASR w334 “Bởi” 80.88–81.56 băng ranh 81.35; giữ timing và đánh dấu nghe lại.

**Text inventory:** Không map quyền lợi hoặc thêm “EU citizenship”. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S15 — Không cần nhanh hơn

1. **Scene ID:** S15.
2. **Audio chính xác:** `[1952400, 2027167) samples`; `1952400/24000 → 2027167/24000 s` (xấp xỉ 81.350000 → 84.465292 s; dài 3.115292 s).
3. **Transcript gốc ASR:** Bởi đôi khi, hạnh phúc không đến từ việc sống nhanh hơn,

   **Corrected_text có sẵn:** Bởi đôi khi, hạnh phúc không đến từ việc sống nhanh hơn,

4. **Mục tiêu truyền đạt:** Đổi nhịp từ lời hứa lớn về một lựa chọn nhỏ có thể cảm.
5. **Visual concept:** Cận người lớn hạ tay đang nhìn giờ/định cầm điện thoại, đổi ánh mắt sang con. Không làm thời gian dừng lại bằng phép màu.
6. **Bối cảnh:** Close crop trong cùng nhà/sân, bóng sáng êm; không mở thêm locale.
7. **Chủ thể / props / assets dự kiến:** Parent hand/profile, simple watch hoặc phone không UI đọc được; child ở ngoài hướng nhìn.
8. **Bố cục & hierarchy:** Cận lệch trục, một khoảng trống có động cơ theo eyeline; camera đứng yên.
9. **Trạng thái mở:** Kế thừa vị trí tay S14; không gắn một beat giả vào local 0 cho từ “Bởi”.
10. **Hành động chính:** Ngừng một thao tác vội để chú ý đến người thân.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Bàn tay đã sẵn để kết nối, không còn bận kiểm tra.
13. **Chuyển sang scene sau:** Cắt theo hướng tay sang S16; không một morph nữa.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 335–336: “đôi khi,” | 81.56–81.88 | 0.210000–0.530000 | Giữ cảnh có thời gian thở ở “đôi khi”. |
| 337–338: “hạnh phúc” | 82.24–82.60 | 0.890000–1.250000 | Gaze mềm hơn, không hiện chữ hạnh phúc như khẩu hiệu. |
| 343–345: “sống nhanh hơn,” | 83.48–84.28 | 2.130000–2.930000 | Tay hạ xuống/điện thoại cất đi; không speed-lines hay clock-stop effect. |

15. **Độ phức tạp ước tính:** Thấp–vừa — micro-acting chính xác. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Parent hand/gaze, watch/phone prop; không lặp toàn bộ hành động đóng laptop S08.
17. **Creative / factual risks:** Phân biệt dừng thao tác với bảo đảm ít áp lực/công việc. Boundary w334 phải review audio; anchor trong cảnh dùng “đôi khi”, không tự dời ASR.

**Text inventory:** Không text hoặc đồng hồ đếm ngược. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S16 — Theo nhịp bước của con

1. **Scene ID:** S16.
2. **Audio chính xác:** `[2027167, 2126040) samples`; `2027167/24000 → 2126040/24000 s` (xấp xỉ 84.465292 → 88.585000 s; dài 4.119708 s).
3. **Transcript gốc ASR:** mà đến từ việc có nhiều thời gian hơn để đi dạo cùng con,

   **Corrected_text có sẵn:** mà đến từ việc có nhiều thời gian hơn để đi dạo cùng con,

4. **Mục tiêu truyền đạt:** Cụ thể hóa thời gian bên nhau bằng tốc độ và tương tác.
5. **Visual concept:** Từ ngang tầm tay, người lớn điều chỉnh bước để nắm tay con; hai nhịp bước trở nên cùng nhau.
6. **Bối cảnh:** Promenade Malta đã quen nhưng crop thấp, không lặp wide S03.
7. **Chủ thể / props / assets dự kiến:** Parent + child hands/feet, paving/rail fragments, soft tree shadow.
8. **Bố cục & hierarchy:** Bàn tay và bước chân là hero; chỉ một dải background đủ định vị.
9. **Trạng thái mở:** Tay hạ xuống từ S15 đi vào cùng hướng tay con.
10. **Hành động chính:** Bước chậm hơn và đi cùng trẻ.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Hai người cùng hướng đến café phía trước, không pose vẫy tay chào camera.
13. **Chuyển sang scene sau:** Hướng đi dẫn vào bàn café S17; dùng cut theo hành động, không tua nhanh quãng đường.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 350–354: “có nhiều thời gian hơn” | 85.46–86.74 | 0.994708–2.274708 | Người lớn đổi nhịp bước về cùng trẻ, không kéo dài thời gian thực. |
| 356–359: “đi dạo cùng con,” | 87.22–88.18 | 2.754708–3.714708 | Nắm tay và bước cùng nhau đúng trọng âm đi dạo/cùng con. |

15. **Độ phức tạp ước tính:** Vừa — bước/contact ở cự ly gần phải tự nhiên. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Walk/hand-hold poses, coast paving fragments; crop và tempo khác pilot S03.
17. **Creative / factual risks:** Tránh biến cảnh này thành walk cycle trang trí hoặc lặp hành động gia đình của S08.

**Text inventory:** Không text mới. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

### S17 — Một điều giản dị đủ để nhớ

1. **Scene ID:** S17.
2. **Audio chính xác:** `[2126040, 2232960) samples`; `2126040/24000 → 2232960/24000 s` (xấp xỉ 88.585000 → 93.040000 s; dài 4.455000 s).
3. **Transcript gốc ASR:** rồi cà phê với người thân và tận hưởng những điều dạn dị cuộc cuộc sống.

   **Corrected_text có sẵn:** ngồi cà phê với người thân và tận hưởng những điều giản dị của cuộc sống.

4. **Mục tiêu truyền đạt:** Khép cảm xúc và gắn ký ức lifestyle với Esora, không thêm CTA ngoài voice.
5. **Visual concept:** Một góc bàn café có người thân; hai bàn tay đưa cốc gần nhau, cảnh lắng để logo Esora xuất hiện trong phần resolve.
6. **Bối cảnh:** Café/terrace ở Malta trong ánh chiều; không cần mở toàn cảnh thêm lần nữa.
7. **Chủ thể / props / assets dự kiến:** Family/adult hands, cups, table, sea hint; original Esora JPEG có nền xanh.
8. **Bố cục & hierarchy:** Cận bàn/tương tác ở nửa trên; vùng resolve thật trong bố cục cho logo, không footer bị bỏ trống suốt phim.
9. **Trạng thái mở:** Tay/cốc tiếp tục hướng hành động S16 bằng cut, không nối thời gian giả.
10. **Hành động chính:** Chia sẻ một khoảnh khắc bình thường rồi để thương hiệu lưu lại.
11. **Transformation / animation beats:** theo bảng ở mục 14; mỗi hàng là một thay đổi trong cùng ý cảnh, không phải một card mới.
12. **Trạng thái kết:** Bàn café, cảm xúc và logo cùng ổn định đến 93.04 s.
13. **Chuyển sang scene sau:** Kết thúc tại đúng master end; không fade voice sớm hoặc thêm branded outro ngoài thời lượng.
14. **Word anchors & choreography:**

| Word IDs / token ASR nguyên bản | Master start–end (s) | Local start–end (s) | Visual beat đề xuất |
|---|---|---|---|
| 360–365: “rồi cà phê với người thân” | 88.68–89.98 | 0.095000–1.395000 | Cốc và bàn tay định vị người thân, không lặp toàn bộ café montage S03. |
| 367–372: “tận hưởng những điều dạn dị” | 90.50–92.02 | 1.915000–3.435000 | Hạ chuyển động, logo bắt đầu hiện trong resolve ở “giản dị”. |
| 373–375: “cuộc cuộc sống.” | 92.02–92.72 | 3.435000–4.135000 | Giữ logo đủ rõ đến hết master, không thêm end-slate kéo dài. |

15. **Độ phức tạp ước tính:** Vừa — resolve/brand readability trong thời lượng ngắn. Đây là mức tương đối, chưa phải cam kết giờ dựng.
16. **Khả năng reuse:** Cup/hands/table, terrace cues, original logo lockup (contain).
17. **Creative / factual risks:** Không thêm hotline/CTA/slogan hoặc biến logo thành huy hiệu chính phủ. Không crop vòng sao, không vẽ lại chữ.

**Text inventory:** Chỉ logo Esora hiện có; không tự thêm lời hứa. Không có subtitle mặc định.

**Engine đề xuất:** HyperFrames + GSAP; SVG/HTML 2D và timeline seekable đáp ứng concept trên. Chưa tạo entry hoặc render configuration cho scene.

## Pilot design chi tiết — S03

**Mục đích sample:** kiểm tra world-building 2D, phối cảnh, nhân vật nhỏ và điều phối chú ý theo lời kể, thay cho năm biểu tượng hoạt động rời nhau. Không phải render đã thực hiện.

### Shot / staging

Một continuous illustrated world ven biển: lối dạo nối khoảng quảng trường/café, xa hơn là một vịnh/bãi biển. Đây là composite Malta-inspired, không ghi tên địa điểm hay cho người xem hiểu toàn bộ là một tuyến đi bộ thực tế. Giữ ánh sáng chiều muộn xuyên shot, không đổi ngày/đêm theo câu “buổi sáng hoặc chiều muộn”.

Trong frame 9:16 đề xuất: khoảng trên 15–40% chiều cao dành cho phố và quảng trường; trung cảnh 35–65% là café/lối dạo; tiền cảnh 60–90% là mặt đường/lan can, với vịnh ở khoảng nhìn thoáng một bên. Đây là sơ đồ khởi đầu, không các band cứng hay safe zones. Đường đi chéo dẫn ánh mắt từ walker đến runner, sau đó giao điểm café/quảng trường; gia đình ở bờ vịnh được nhìn thấy như một điểm đến có chiều sâu. Không chồng năm nhân vật quan trọng thành một hàng ngang không đọc được trên điện thoại.

Bố trí người trước animation: walker có ground path; runner dùng làn khác để không chạy xuyên café; hai người ở bàn đã ngồi sẵn; nhóm bạn gặp tại quảng trường; gia đình ở vịnh có vị trí riêng. Nhân vật phụ không teleport theo từng từ. Tại mỗi beat, chỉ một nhóm giữ chuyển động tương phản nổi bật; nhóm đã kể xong lắng xuống tự nhiên hoặc ra khỏi crop. Không freeze toàn bộ thế giới rồi nhấp nháy từng actor.

### Choreography theo scene-local time

Các cửa sổ trong bảng 17-scene là anchors ASR. Dưới đây là kế hoạch hành động rộng hơn, được phép chuẩn bị trước khi câu gọi tên hoạt động; phải test bằng playback sau này.

| Local time (s, xấp xỉ) | Chủ thể / hành động | Camera / trạng thái |
|---|---|---|
| 0–0.333917 | Người đi bộ đã có tư thế và mặt đường rõ; thiết lập hướng di chuyển | Khung mở nhìn xiên, không mở bằng icon/tiêu đề |
| 0.333917–2.013917 | Walkers hoàn tất một nhịp đi, một người nhìn ra biển | Chú ý ở walkway; không hai lần đổi ánh sáng để nói sáng/chiều |
| 2.233917–3.093917 | Runner đi vào đường dẫn cùng thế giới; cadence khác walking | Tái định khung nhẹ lần 1 nếu thật sự cần, không đuổi sát từng bước |
| 3.413917–4.353917 | Người ở bàn nhấc/đặt cốc có tiếp xúc, đối diện nhìn đáp lại | Bàn café được thấy đủ chân và bề mặt; không isolate cốc trong card |
| 4.673917–6.173917 | Một người đến, người bạn nghiêng người nhận ra; trao đổi ánh nhìn | Quảng trường mở ra sau café, giữ landmark chung để chứng minh cùng không gian |
| 6.713917–8.413917 | Gia đình ở vịnh tiến gần nhau, trẻ cầm tay người lớn; bãi biển được nhận diện ở lời cuối | Tái định khung lần 2 nếu cần; không thêm một chuyến đi dài hoặc cảnh xe chạy |
| 8.413917–8.939250 | Giữ trạng thái cuối đủ đọc, chuyển chú ý sang chiếc cốc tiền cảnh | Resolve khoảng 0.525s sau từ cuối ASR; cup match cut sang S04, không thêm thời lượng |

Nhãn “buổi sáng/chiều muộn”, “chạy bộ”, “café”, “gia đình” không cần xuất hiện; voice đã truyền đạt chúng. Motion chính phải vẫn hiểu được khi tắt chữ. Nếu thử nghiệm cho thấy quá tải trong 8,93925s, giảm số cử chỉ/chi tiết background trước; không cắt bỏ ý voice hoặc chia lại manifest.

### Assets, tách phần và reuse

- ENV-MT-COAST: ground path/lan can, mặt tiền đá và ban công, café/plaza, vịnh/bãi biển. Occlusion phải nhất quán; không tái dựng landmark cụ thể thiếu reference.
- CHAR-RESIDENTS: walker pair, một runner, café pair, nhóm bạn tối giản, family group cuối. Chỉ chủ thể gần cần tay/đầu riêng; silhouette xa có thể ít joints.
- Props: cốc/bàn/ghế/chậu cây, chân đế có contact shadow. Không scatter icon mặt trời/giày/cốc/ô bãi biển thay môi trường.
- Components dự kiến: WorldStage, WalkTravel, AttentionReframe, CharacterPose và PropPlacement. Reuse vật liệu/architecture cho S02/S10, không copy world-camera của S03 sang S05.
- S02→S03 trong phim: nối hướng nhìn biển; standalone S03 vẫn đủ ground/world ngay từ frame đầu. S03→S04: cup/detail match, crop riêng Việt Nam phải rõ ngữ cảnh phin sau cut.

### QA khi build được chỉ thị

Kiểm tra opening, midpoint của từng cửa sổ hành động, resolve và playback đúng voice; preview 360×640. Từ silhouette có phân biệt đi bộ/chạy/café/gặp bạn/gia đình không? Có hơn một focal action cạnh tranh không? Feet có trượt, nhân vật xuyên lan can, bàn/ghế không cùng mặt đất, camera lộ vùng chưa vẽ hoặc vịnh bị nối sai địa lý không? Kiểm tra seek thẳng giữa scene cho ra cùng pose/world; rendering độc lập không thiếu asset từ S02. Không coi storyboard đầy đủ là đã PASS các kiểm tra visual/runtime này.

## Pilot design chi tiết — S08

**Mục đích sample:** một quyết định có cảm xúc và hành động hoàn tất: phụ huynh tạm gác công việc, chuyển sự chú ý và chạm tay con. Không dùng cân thăng bằng, đồng hồ hay hai icon “work/family”.

### Shot / staging

Cùng căn nhà giới thiệu ở S06. Góc medium đủ thấy torso, ghế, mặt bàn và tay; desk nằm trái/giữa tiền cảnh, hướng mở ra terrace bên phải/phía sau. Trẻ đã ở khoảng cách có thể với tay, không ở tận ban công rồi chạy đến trong nửa giây. Tầm nhìn của phụ huynh từ laptop chuyển sang con là đường dẫn mắt chủ đạo. Không chia khung thành hai ô “công việc” và “gia đình”.

Sơ đồ 9:16 đề xuất: torso phụ huynh trong vùng x≈25–55%, y≈35–65%; trẻ x≈65–80%, y≈50–75%; vùng tay gặp nhau gần x≈55–65%, y≈60–70%. Tỉ lệ phải điều chỉnh theo model sheet; đây không phải tọa độ rig đã được xác minh. Cửa/terrace dẫn ánh sáng, không hút mắt hơn acting. Hai gương mặt và tay cần cùng đọc được ở 360×640, ưu tiên crop gần hơn việc thêm phòng lớn.

### Choreography theo scene-local time

| Local time (s, xấp xỉ) | Hành động có nguyên nhân | Anchor / trạng thái |
|---|---|---|
| 0–0.15 | Tay còn ở laptop, có một tác vụ nhỏ đang kết thúc | Mở độc lập hiểu được tình huống; không cần frame cuối S07 |
| 0.15–1.55 | Nhịp tay giảm, vai buông nhẹ, phụ huynh bắt đầu nhận ra hiện diện của con | Word 167–173, “mà còn là văn hóa sống chậm” |
| 1.87–2.21 | Tay rời thao tác, thân ổn định trước quyết định | Word 174–175 “cân bằng”; không đồ thị balance |
| 2.41–2.71 | Nắp laptop khép về base theo pivot thật | Word 177–178 “công việc”; tránh kẹp/xuyên tay, có thể bắt đầu chuẩn bị trước cửa sổ từ |
| 3.03–4.21 | Ghế/thân quay vừa đủ, gaze sang con, đưa tay theo hướng đã staging | Word 180–185 “thời gian dành cho bản thân”; không bật khỏi ghế như lò xo |
| 4.21–4.73 | Con đáp lại, tay tiến đến điểm chạm; tạo anticipation có nghĩa nếu cần | Chuẩn bị tiếp xúc để không phải ôm/đi bộ dài trong 0.38s |
| 4.73–5.11 | Hai tay chạm, mắt gặp nhau, nét mặt đổi nhẹ | Word 186–187 raw “Giá đình”, corrected_text “gia đình”; không gán lại ASR mới |
| 5.11–5.610125 | Giữ sự kết nối, bắt đầu hướng nhìn ra ngoài | Resolve trong interval thật; không thêm hug/walk/outro làm dồn động tác |

S07→S08: cut theo cửa sổ/điểm nhìn khu dân cư vào góc nhà. S08→S09: gaze của trẻ dẫn sang cảnh trẻ khám phá bên ngoài, là cut ý nghĩa, không hàm ý hai hành động cùng giây hay cùng địa điểm thật. Preview độc lập cần vào được tình huống và kết thúc có nghĩa.

### Assets / contact map / reuse

ENV-HOME dùng chung ground/perspective với S06, phiên bản crop phù hợp S08; PROP-HOME gồm laptop lid/base, desk, ghế. CHAR-FAMILY chỉ cần identity đã chốt và pose theo hành động. Điểm tựa cần thiết: chân ghế xuống sàn, cẳng tay trên bàn lúc đầu, pivot laptop, vai/khuỷu/cổ tay gần, contact point hai bàn tay, vị trí mắt. Không phát triển full character system ngoài nhu cầu pilot.

Components dự kiến: CharacterPose, LaptopLid, HandContact, PropPlacement. Reuse contact logic cho S16 nếu phù hợp nhưng pose tay đi bộ là biến thể riêng. Workstation tại nhà chỉ minh họa quyết định dành thời gian, không quảng bá quyền làm việc tự động từ một chương trình cư trú.

### QA khi build được chỉ thị

Xem opening, lúc tay rời bàn, nắp khép, gaze đổi, chạm tay và resolve; playback cùng voice, preview 360×640 và seek giữa shot. Có đọc được “chọn dành thời gian” khi không có text không? Cần thấy con trước quyết định để acting có lý do. Không tay xuyên nắp/nhân vật, ghế xoay trượt sàn, trẻ đổi scale, mắt nhìn sai contact, cánh tay co giãn thiếu joint hoặc thiếu thời gian cho phản ứng. Tránh cười sẵn từ đầu làm mất biến đổi. Chưa có visual/runtime test cho shot này.

## Cách review hai sample sau này

S03 là interval 10.166083…–19.105333…s, S08 là 40.270000–45.880125s của master. Hai scene không liền nhau. Khi có chỉ thị build pilot, xuất hai sample riêng dùng đúng đoạn audio tương ứng; nếu có trang review chung, ghi rõ ID/timing và không autoplay nối như voice liên tục. Không sinh câu dẫn, không time-stretch hoặc lắp voice để giả một câu chuyện khác. Hai sample cùng thử style system, nhưng một cảnh kiểm tra không gian đa hoạt động và một cảnh kiểm tra diễn xuất cận. Chưa tạo source/preview/render/approval.

## Open decisions và factual risk register

| ID | Vấn đề | Cách xử lý / phạm vi ảnh hưởng |
|---|---|---|
| D01 | Hướng Warm Mediterranean Editorial có đủ đúng thương hiệu? | Người dùng review style bible/palette/độ trưởng thành; hướng ưu tiên chưa phải approval. |
| D02 | Casting gia đình và mức cách điệu | Xác nhận hai phụ huynh + một trẻ có phù hợp đối tượng; tuổi/trang phục là đề xuất, không khóa rig. |
| D03 | Resolution/FPS/font | Đề xuất 1080×1920/30 FPS và thử Be Vietnam Pro; cần chốt + kiểm tra file/license trước triển khai; manifest hiện còn null được giữ nguyên. |
| D04 | Text và branding | Chữ tối thiểu như inventory, không subtitle; Esora cuối S17 khoảng 1.66s là đề xuất. Nếu cần CTA/logo lâu hơn phải phân bổ visual trong audio hiện có, không tự kéo dài master. |
| D05 | Pilot scope | S03/S08 là hai candidate có thiết kế chi tiết; cần chỉ thị build riêng, chưa locked/approved/rendered. |
| F13 | **S13 — FACTUAL REVIEW REQUIRED** | Chưa có bằng chứng cho “3,8 tỷ” là chi phí gì/phạm vi nào/thời điểm nào. Cần nguồn chính thức và đơn vị tư vấn xác nhận điều kiện, cấu phần và quy đổi. Không tự thêm số, bảo đảm hay quyền lợi. |
| F13b | “4 thế hệ”, “Thẻ xanh”, quyền cư trú | [Residency Malta — MPRP legal framework](https://residencymalta.gov.mt/legal-framework-mprp-2/) nói khả năng nhiều thế hệ theo điều kiện; không suy thành mọi gia đình đều đủ điều kiện, quốc tịch EU hay quyền làm việc tự động. Nội dung cụ thể vẫn cần review chuyên môn trước sử dụng quảng cáo. |
| F14 | Mở cửa Châu Âu | Minh họa ngưỡng cửa gia đình, không bản đồ quyền tự do cư trú/làm việc khắp EU. Không thêm passport/visa stamps hoặc nhãn quyền lợi. |
| F-LIFE | “an toàn”, giáo dục/y tế, phát triển toàn diện | Voice là narrative đầu vào, chưa phải bằng chứng đo chất lượng. Tránh xếp hạng, bảo đảm hay nhãn so sánh mới; nếu đưa claim lên màn hình cần nguồn/duyệt tương ứng. |
| T334 | Word 334 “Bởi”: ASR 80.88–81.56s, cắt qua boundary S14/S15=81.35s | Giữ timing/manifest nguyên vẹn. Đây là xung đột interval ASR, chưa chứng minh tiếng thật bị cắt. Không neo “Bởi” ở local 0 của S15; dùng word335 “đôi khi” từ 81.56s. Trước render scene độc lập cần nghe/kiểm tra waveform quanh boundary. Final master liên tục không splice voice; chưa tuyên bố zero-click hay sample-exact audiovisual sync. |

S13 được giữ trong storyboard với concept tham vấn trung tính để các scene khác vẫn có thể review/phát triển. **Visual trung tính không sửa được claim trong voice**: không phát hành bản final chứa claim chưa được xác minh. Nếu factual review yêu cầu đổi lời, báo người dùng xử lý audio và timing bằng quy trình riêng; không tự thay master/manifest trong nhiệm vụ này.

## Điều gì đã và chưa được kiểm chứng

Đã đối chiếu đủ 17 ID, sample bounds, raw/corrected transcript và 53 nhóm word anchors với inputs; kiểm tra hash các file nguồn được bảo vệ trước/sau viết tài liệu. Evidence ở `../build/storyboard-planning-evidence/`. Đây là kiểm tra tính nhất quán tài liệu, **không** là render/visual quality PASS. Chưa tạo minh họa, rig, font mới, animation source, browser preview hoặc video. Chưa đo readability, frame alignment hay A/V sync mới. Approval vẫn pending; pilot chưa được bắt đầu.


## R1 — Current direction and voice-synced highlights (supersedes earlier text inventories)

MODERN PREMIUM 2D ADVERTISING MOTION GRAPHICS — MEDITERRANEAN LIFESTYLE. Previous pilot was NOT APPROVED. Navy/azure/turquoise/clean white/coral/sunlight are experimental project colors, not official brand colors. Selected kinetic phrases are mandatory for VIDEO-34; subtitles remain disabled. Detailed earlier shot concepts remain reference, but R1 source and the following mapping supersede old palette, character coordinates and text inventories. Only S03/S08 are implemented; all other rows are planning only. Anchors below are source ASR windows, not a new alignment.

| Scene / key message | Candidate text | Voice anchor (global seconds; source words) | Illustration action | Motion/effect | State |
|---|---|---|---|---|---|
| S01 — Hai nơi, một nhịp sống | Ngoài trời | 4.06–4.54: ngoài trời. | Hai người ở hai nơi thực hiện cùng một cử chỉ đời thường. | Matched gesture + word reveal | PLAN ONLY / NOT IMPLEMENTED |
| S02 — Biển và nắng là bối cảnh sống | Biển · Nắng | 8.66–9.84: lối sống khá giống người Việt. | Cảnh quan được lộ dần bằng chuyển điểm nhìn nhẹ qua mép hiên. | Horizon reveal + sunlight sweep | PLAN ONLY / NOT IMPLEMENTED |
| S03 — Một bờ biển đang sống — PILOT CANDIDATE | Đi bộ / Chạy bộ / Cà phê / Gia đình | 16.88–18.58: cuối tuần cùng gia đình bên bãi biển. | Camera/layout chuyển trọng tâm trong cùng một môi trường, từng hành động khớp cụm lời đọc. | Camera focal handoff + path stroke + kinetic keywords | R1 implemented; exact selected word cues in revision-r1.md |
| S04 — Cử chỉ ấy rất quen | Quen thuộc | 20.92–21.82: quen thuộc ở Việt Nam. | Dùng match composition để chuyển nơi, giữ hành động nâng/đặt cốc. | Prop match + short mask | PLAN ONLY / NOT IMPLEMENTED |
| S05 — Nhịp Việt ở góc nhìn khác | Nhịp sống Việt | 26.54–28.02: đưa con đi biển vào dịp cuối tuần. | Theo một tuyến sinh hoạt rồi chuyển độ lớn sang tương tác cha/mẹ–con. | Overhead path + distributed words | PLAN ONLY / NOT IMPLEMENTED |
| S06 — Mang điều quen thuộc đến một nơi mới | Cảm giác thuộc về | 32.68–34.80: không quá xa lạ khi chuyển đến sân sống. | Đặt vật quen vào nhà mới rồi hướng sự chú ý ra không gian ngoài trời. | Prop placement + restrained type settle | PLAN ONLY / NOT IMPLEMENTED |
| S07 — Giá trị không dừng ở các công trình | Không chỉ trường học | 38.06–40.20: không chỉ là hệ thống giáo dục hay y tế, | Đổi trọng tâm từ hạ tầng sang nhịp sống trong căn nhà. | Window focus + negative-to-positive hierarchy | PLAN ONLY / NOT IMPLEMENTED |
| S08 — Từ công việc đến hiện diện bên gia đình — PILOT CANDIDATE | Sống chậm / Thời gian / Gia đình | 45.00–45.38: Giá đình, | Rời thao tác công việc, đổi hướng cơ thể và dành sự chú ý cho người thân. | Gaze/hinge/contact + two-stage typography | R1 implemented; exact selected word cues in revision-r1.md |
| S09 — Thế giới ở tầm mắt trẻ | Khám phá | 49.18–49.92: khám phá thiền nhiên. | Cúi xuống khám phá, chuyển từ vận động sang tò mò. | Child viewpoint + discovery stroke | PLAN ONLY / NOT IMPLEMENTED |
| S10 — Khoảng nghỉ dành cho người lớn | Khoảng nghỉ | 54.02–54.70: gần gũi với biển. | Ngồi xuống và trao nhau sự chú ý trong không gian công cộng. | Quiet camera + soft rule draw | PLAN ONLY / NOT IMPLEMENTED |
| S11 — Điều phụ huynh nhìn thấy | Điều đáng giá | 57.61–59.67: không chỉ là con được học ở một ngôi trường tốt, | Từ nhìn trường trong hình sang nhìn chính đứa trẻ. | Drawing-to-child focus + keyword reveal | PLAN ONLY / NOT IMPLEMENTED |
| S12 — Lớn lên trong quan hệ với thế giới | Cùng lớn lên | 63.89–66.21: phát triển toàn diện cả về thể chất lẫn tinh thần. | Đưa vật cho người khác, nhận đáp lại và tiếp tục chơi. | Ball handoff + connected-word rhythm | PLAN ONLY / NOT IMPLEMENTED |
| S13 — Cân nhắc bước tiếp theo — FACTUAL REVIEW REQUIRED | CHƯA CHỐT — factual review | 72.02–72.64: 4 thế hệ, | Mở trang thông tin và nhìn về không gian gia đình. | Neutral folder only; no price/eligibility graphic until verified | PLAN ONLY / NOT IMPLEMENTED |
| S14 — Một cánh cửa mở vào đời sống | Một lối sống mới | 78.38–80.88: gần của vi thi nhiên dạc cân bằng hơn mỗi ngày. | Đi qua cửa vào một hoạt động đời thường của gia đình. | Door opening mask + environmental depth | PLAN ONLY / NOT IMPLEMENTED |
| S15 — Không cần nhanh hơn | Không cần nhanh hơn | 83.48–84.28: sống nhanh hơn, | Ngừng một thao tác vội để chú ý đến người thân. | Hand pause + decelerating type | PLAN ONLY / NOT IMPLEMENTED |
| S16 — Theo nhịp bước của con | Đi dạo cùng con | 87.22–88.18: đi dạo cùng con, | Bước chậm hơn và đi cùng trẻ. | Matched steps + path phrase | PLAN ONLY / NOT IMPLEMENTED |
| S17 — Một điều giản dị đủ để nhớ | Điều giản dị | 92.02–92.72: cuộc cuộc sống. | Chia sẻ một khoảnh khắc bình thường rồi để thương hiệu lưu lại. | Cup contact + brand signature; no added CTA | PLAN ONLY / NOT IMPLEMENTED |
