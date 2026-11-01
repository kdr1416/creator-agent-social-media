# Trần Minh Nhật — storyboard đạo diễn

**17 cảnh / 68,2 giây. Thiết kế mới14 cảnh; giữ ba pilot04,06v4,12v6 làm mốc hiện tại. Chưa render14 cảnh trong lần bàn giao này.**

Các cue thời gian dưới đây là phân nhịp đạo diễn dựa trên lát voice, chưa phải forced word alignment. Toạ độ là gợi ý dựng trên720×1280; ưu tiên ý nghĩa, phân cấp và sự liền mạch, có thể tinh chỉnh để hình cân/đọc tốt. Không biến mỗi quyết định của cảnh thành luật cho mọi video.

Mạch: **mở khả năng → giới thiệu Nhật → thành quả VU → môi trường/cơ hội → quay về công sức chuẩn bị → câu chuyện riêng → chương mới.**

|Cảnh|Thời gian voice|Tên cảnh|Việc cần làm|
|---|---|---|---|
|01|0.000–3.212s|Góc học tập mở ra thế giới|Dựng theo packet|
|02|3.212–7.587s|Làm quen với Minh Nhật|Dựng theo packet|
|03|7.587–12.427s|Điểm đến Hà Lan|Dựng theo packet|
|04|12.427–18.447s|Phong thư mở ra điểm đến|Dùng pilot|
|05|18.447–21.668s|Từ phong thư tới môi trường học thuật|Dựng theo packet|
|06|21.668–26.860s|Nhiều lĩnh vực cùng một campus|Dùng pilot|
|07|26.860–31.144s|Giá trị học thuật trong bối cảnh quốc tế|Dựng theo packet|
|08|31.144–34.257s|Cơ hội là các lựa chọn mở|Dựng theo packet|
|09|34.257–37.661s|Đằng sau thành quả là một bàn làm việc|Dựng theo packet|
|10|37.661–41.147s|Mentor giúp Nhật làm rõ lựa chọn|Dựng theo packet|
|11|41.147–44.711s|Thành tích là chất liệu của bộ hồ sơ|Dựng theo packet|
|12|44.711–49.131s|Ba thành phần cốt lõi|Dùng pilot|
|13|49.131–51.233s|Mỗi câu chuyện có một cấu trúc riêng|Dựng theo packet|
|14|51.233–55.935s|Kể có trọng tâm để người đọc hiểu mình|Dựng theo packet|
|15|55.935–60.353s|Hoàn tất cùng người đồng hành|Dựng theo packet|
|16|60.353–63.435s|Chương mới được chúc mở ra|Dựng theo packet|
|17|63.435–68.200s|Hành trình còn tiếp|Dựng theo packet|

# 01 · Góc học tập mở ra thế giới

**Voice gốc:** Tôi có thể học ở bất kỳ đâu, vì tôi dám khác biệt.

**Thời lượng:** 3.211958333s · sample 0–77087 · audio `inputs/audio/scene_01.wav`.

**Ý cần đọc được:** Đặt tính chủ động và khác biệt làm tinh thần mở đầu; chưa hứa được nhận vào bất kỳ trường nào.

**Dàn khung:** Medium shot căn phòng: cửa sổ x135–610/y350–670; bàn x95–615/y790–955; Nhật x340–480/y685–1000. Không vẽ bản đồ hoặc ba icon ngành.

**Mở cảnh:** Nhật đang học bên một cửa sổ đóng rèm; cuốn sổ xanh và ba lô ở trong tầm tay.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.800s|Tôi có thể học|Nhật ngẩng khỏi sổ; tay rời mép trang để chạm rèm.|
|0.80–2.000s|ở bất kỳ đâu|Nhật kéo rèm, bên ngoài mở thành một góc phố có lớp mái nhà xa gần; chiều sâu của môi trường xuất hiện thay cho màn hình thông tin.|
|2.00–2.700s|vì tôi dám khác biệt|Nhật tự dán một miếng đánh dấu cam lên sổ xanh rồi cầm cuốn sổ lên; headline xuất hiện.|
|2.70–3.212s|khác biệt — kết câu|Giữ một nhịp ánh mắt tự tin và cuốn sổ, cắt trên hành động nâng sổ.|

**Chốt:** Cuốn sổ xanh có dấu cam ở tay Nhật, cửa sổ đã mở.

**Nhân vật:** Đọc → mở rèm → chủ động đánh dấu sổ; không mascot đứng cạnh nền chuyển động.

**Chữ trên hình:** DÁM KHÁC BIỆT. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `room` — **to_draw**. Một góc phòng học lilac sáng, cửa sổ lớn có rèm kéo, đèn nhỏ và một cây;09 thêm dấu vết bản nháp. Không lấp phòng bằng đồ trang trí ngẫu nhiên. Tách: wall/window frame, moving blind, far roofs layers, desk plane, lamp, plant. Nguồn: original vector layers; no room photo needed.
- `notebook` — **to_draw**. Sổ xanh bìa mềm, một dấu cam ở góc và gáy rõ; có bìa đóng/mở, mép trang và clip. Chữ tên chỉ khi scene yêu cầu. Tách: front cover, spine, page block, opening page, orange bookmark. Nguồn: design based on selected blue/orange roles; not the old envelope.

**Nối sang cảnh sau:** 02 tiếp tục đúng cuốn sổ và tay đang nâng, đổi sang góc nhìn giới thiệu; không morph cả căn phòng thành chữ.

**Vì sao HF_ONLY:** Ý chính là khung cửa giấy mở lớp môi trường và dấu cá nhân trên sổ. HYBRID người thật sẽ thay đổi phong cách của chủ thể biểu tượng và không thể hiện lớp giấy mở; organic acting không cần để đọc quan hệ này.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 02 · Làm quen với Minh Nhật

**Voice gốc:** Đó cũng là tinh thần của Trần Minh Nhật – chàng trai đến từ RMIT Việt Nam,

**Thời lượng:** 4.374916667s · sample 77087–182085 · audio `inputs/audio/scene_02.wav`.

**Ý cần đọc được:** Gắn tên và xuất phát điểm RMIT Việt Nam với nhân vật, không tạo thẻ sinh viên hoặc giả ảnh người thật.

**Dàn khung:** Tên trần x95–625/y270–410, hai dòng 50–58px; campus cutout x105–610/y460–720; Nhật với sổ x420–570/y780–1000.

**Mở cảnh:** Cuốn sổ từ01 đi vào khung; Nhật đặt nó lên mép bàn rồi bước ra đứng cạnh.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.750s|Đó cũng là tinh thần|Theo cuốn sổ hạ xuống, máy lùi để thấy Nhật.|
|0.75–2.250s|Trần Minh Nhật|Tên hiện hai nhịp TRẦN MINH / NHẬT; Nhật quay về người xem, giữ cuốn sổ có dấu cam.|
|2.25–3.650s|chàng trai đến từ RMIT Việt Nam|Ảnh campus RMIT chính thức xuất hiện như một mảnh ảnh phía sau; nhãn RMIT Việt Nam gắn ngay vùng ảnh, không thêm logo tự chế.|
|3.65–4.375s|Việt Nam — kết câu|Nhật mở sổ, lộ mép trang giấy dùng ở03.|

**Chốt:** Tên đã đọc được; ảnh RMIT là bối cảnh; sổ vừa mở.

**Nhân vật:** Đặt sổ, đứng giới thiệu và chủ động mở trang; nhân vật là biểu tượng, không phải chân dung xác thực.

**Chữ trên hình:** TRẦN MINH NHẬT / RMIT Việt Nam. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `notebook` — **to_draw**. Sổ xanh bìa mềm, một dấu cam ở góc và gáy rõ; có bìa đóng/mở, mép trang và clip. Chữ tên chỉ khi scene yêu cầu. Tách: front cover, spine, page block, opening page, orange bookmark. Nguồn: design based on selected blue/orange roles; not the old envelope.
- `rmit_photo` — **to_source**. Một ảnh campus có sẵn ở trang giới thiệu RMIT Việt Nam, crop công trình không người. Đây là bối cảnh định danh tổ chức, không khẳng định Nhật học tại campus cụ thể trong ảnh. Tách: photo frozen local file, paper edge, tape. Nguồn: https://www.rmit.edu.vn/about-us/who-we-are ; choose official campus image, not student portrait or a web screenshot.

**Nối sang cảnh sau:** 03 cận trang sổ đang mở; tên và ảnh RMIT ra khỏi khung bằng cắt sạch.

**Vì sao HF_ONLY:** Tên, ảnh cắt và trang mở tạo chân dung đồ hoạ. HYBRID diễn viên sẽ dễ bị nhận là Nhật thật; không có portrait/footage được cung cấp. Không cần diễn xuất thật để định danh bằng thông tin đã có trong voice.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 03 · Điểm đến Hà Lan

**Voice gốc:** vừa chính thức chinh phục thành công một trong những trường đại học nghiên cứu danh tiếng nhất Hà Lan.

**Thời lượng:** 4.839625000s · sample 182085–298236 · audio `inputs/audio/scene_03.wav`.

**Ý cần đọc được:** Cho người xem thấy địa điểm của thành quả, chuẩn bị cho cảnh nhận thư.

**Dàn khung:** Cận mặt bàn. Bản đồ Hà Lan x160–540/y370–810; chấm Amsterdam có nhãn x360–595/y470–535; tay Nhật đi vào từ dưới, không route bay hoặc nhảy qua quốc gia khác.

**Mở cảnh:** Trang mở thành một bản đồ giấy gấp; chưa có tên VU hoặc huy chương.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.100s|vừa chính thức chinh phục thành công|Nhật mở nếp gấp bản đồ bằng hai tay; giấy chiếm phần lớn khung.|
|1.10–2.800s|một trong những trường đại học nghiên cứu|Chấm Amsterdam và một khối campus giấy nhỏ nâng lên tại chấm; chỉ định vị thành phố, không mô phỏng tỉ lệ campus.|
|2.80–4.100s|danh tiếng nhất Hà Lan|Nhãn HÀ LAN được đọc rõ; hai tay gấp bản đồ xuống, một phong bì kem được đặt lên trước.|
|4.10–4.840s|kết câu|Đưa phong bì và Nhật về vùng bố cục mở đầu pilot04; giữ nắp đóng.|

**Chốt:** Phong bì đóng lớn x75–645/y650–950; Nhật về phía phải; không mở thư sớm.

**Nhân vật:** Mở bản đồ rồi đặt phong bì; không cầm cúp, không đưa thêm học bổng.

**Chữ trên hình:** HÀ LAN / Amsterdam. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_hands` — **to_draw_from_reference**. Bàn tay/ống tay của Nhật nhìn overhead; ba tư thế: mở/gấp, giữ giấy, đặt mảnh. Chỉ tay thật của nhân vật, không bàn tay người thật lạc style. Tách: far hand, near hand, contact/grip layer. Nguồn: reference_pilots/scene_12/assets/portrait-v5.js as colour/line reference.
- `netherlands_map` — **to_draw_from_geographic_reference**. Outline Hà Lan trên giấy gấp, chấm Amsterdam ở vùng tây; không bản đồ hàng xóm hoặc đường bay. Dùng outline địa lý kiểm chứng thay đa giác tuỳ ý. Tách: paper folds, land outline, Amsterdam dot, HÀ LAN label, Amsterdam label. Nguồn: official geographic reference to be resolved before drawing; VU official address confirms Amsterdam.
- `envelope` — **available_source**. Phong bì giấy kem có nắp/đáy/mặt trước tách lớp.03 chỉ gấp/đặt,04 mở như nguồn. Tách: back, hinged flap, front, inner paper. Nguồn: reference_pilots/scene_04/index.html #envelope-back/#envelope-flap/#envelope-front.

**Nối sang cảnh sau:** Match cut sang frame đầu pilot04 theo phong bì. Lấy ảnh chụp frame0 của pilot để căn, không sửa pilot04.

**Vì sao HF_ONLY:** Bản đồ giấy gấp và định vị chính xác là nội dung chính; HYBRID map prop thật thêm cảnh quay chứ không giúp đọc điểm đến tốt hơn, còn có nguy cơ chữ tự sinh trên bản đồ.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 04 · Phong thư mở ra điểm đến

**Voice gốc:** Xin chúc mừng Minh Nhật đã nhận thư mời nhập học từ: Vrije Universiteit Amsterdam (VU Amsterdam).

**Thời lượng:** 6.020625000s · sample 298236–442731 · audio `inputs/audio/scene_04.wav`.

**Ý cần đọc được:** Phong bì mở, ảnh campus VU xuất hiện và Nhật mừng kết quả.

**Dàn khung:** Giữ bố cục nguồn pilot đã đóng băng, không tự thiết kế lại.

**Mở cảnh:** Lấy frame đầu chính nguồn pilot.

**Dùng bản đã có:** `reference_pilots/scene_04/renders/pilot.mp4`. Nguồn: `reference_pilots/scene_04/index.html`.

Không tự dựng lại hình chính. Cảnh trước/sau hấp thụ nối cảnh; chỉ xử lý frame/audio theo kế hoạch kỹ thuật.

Bản04 giữ nội dung/typography của chính pilot đó; default font mới ở các cảnh khác lấy06/12. Không âm thầm reskin04.

**Chốt:** Lấy frame cuối chính nguồn pilot.

**Nhân vật:** Phản ứng mừng nhận thư.

**Chữ trên hình:** CHÚC MỪNG / MINH NHẬT! / VU AMSTERDAM / THƯ MỜI NHẬP HỌC. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `envelope` — **available_source**. Phong bì giấy kem có nắp/đáy/mặt trước tách lớp.03 chỉ gấp/đặt,04 mở như nguồn. Tách: back, hinged flap, front, inner paper. Nguồn: reference_pilots/scene_04/index.html #envelope-back/#envelope-flap/#envelope-front.
- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.

**Nối sang cảnh sau:** 05 bắt đầu từ đúng ảnh campus và phong bì cuối04.

**Vì sao HF_ONLY:** Cơ chế phong bì/collage là ẩn dụ thành quả; HYBRID mở thư thật dễ gợi bằng chứng tuyển sinh chưa được cung cấp.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 05 · Từ phong thư tới môi trường học thuật

**Voice gốc:** Một trong những trường đại học nghiên cứu hàng đầu Hà Lan và châu Âu,

**Thời lượng:** 3.220708333s · sample 442731–520028 · audio `inputs/audio/scene_05.wav`.

**Ý cần đọc được:** Cho VU một không gian cụ thể, tránh dựng thành tích xếp hạng chưa kiểm chứng.

**Dàn khung:** Ảnh campus VU bắt đầu tại đúng vị trí cuối04, tiến tới x104–616/y383–946; vỏ kiến trúc giấy của06 xuất hiện quanh mép trong đoạn chốt.

**Mở cảnh:** Giữ ảnh VU vừa nhô khỏi phong bì ở04; không chèn một title card mới.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.750s|Một trong những trường|Máy bám ảnh campus, phong bì hạ khỏi đáy sân khấu; dải tên trường được giữ để đọc.|
|0.75–2.250s|đại học nghiên cứu hàng đầu|Ảnh đứng lại như một tờ ảnh lớn. Hai chi tiết đời sống học thuật ở mép dưới: sách mở và một mặt bàn thí nghiệm trong cùng bối cảnh, không phải hai icon nổi.|
|2.25–3.221s|Hà Lan và châu Âu|Mép khung ảnh trở thành vỏ mô hình campus; chốt hình theo frame đầu06. Chi tiết sách/bàn ra ngoài crop.|

**Chốt:** Ảnh trên mặt mô hình có tỉ lệ/vị trí như đầu06, sẵn sàng bóc mở mặt cắt.

**Nhân vật:** Không thêm nhân vật: ảnh địa điểm và cấu trúc học thuật cần ưu tiên trong3.22s.

**Chữ trên hình:** VU AMSTERDAM. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.
- `campus_shell` — **available_source_extend_only**. Vỏ mô hình campus có sàn/cột từ06.05 chỉ cần bao quanh ảnh để nối sang06; không tự dựng phòng khác trong pilot. Tách: roof, side walls, floors, columns, photo cover. Nguồn: reference_pilots/scene_06/index.html #c6-drawing and #c6-photo.
- `research_props` — **to_draw**. Mép một cuốn sách mở và một phần bàn thí nghiệm làm tiền cảnh môi trường học thuật; không xếp huy chương hoặc icon danh hiệu. Tách: book paper/leaves, bench edge, one glass silhouette. Nguồn: consistent line weight with scene06 workspaces.

**Nối sang cảnh sau:** Cắt sang đầu pilot06 khi cùng mặt ảnh/vỏ kiến trúc. 06 tự thực hiện phần mở mặt cắt.

**Vì sao HF_ONLY:** Biến đổi ảnh cắt thành mô hình lớp giấy mang ý chính. HYBRID campus moving footage không hỗ trợ phép chuyển từ địa điểm sang cấu trúc lĩnh vực ở06; live motion sẽ chỉ thành wallpaper.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 06 · Nhiều lĩnh vực cùng một campus

**Voice gốc:** nổi tiếng với các lĩnh vực Kinh doanh, Khoa học Dữ liệu, Trí tuệ nhân tạo, Luật và Khoa học Sức khỏe.

**Thời lượng:** 5.192666667s · sample 520028–644652 · audio `inputs/audio/scene_06.wav`.

**Ý cần đọc được:** Mặt cắt kiến trúc mở năm không gian cùng trường; không chuỗi nhân quả.

**Dàn khung:** Giữ bố cục nguồn pilot đã đóng băng, không tự thiết kế lại.

**Mở cảnh:** Lấy frame đầu chính nguồn pilot.

**Dùng bản đã có:** `reference_pilots/scene_06/renders/pilot.mp4`. Nguồn: `reference_pilots/scene_06/index.html`.

Không tự dựng lại hình chính. Cảnh trước/sau hấp thụ nối cảnh; chỉ xử lý frame/audio theo kế hoạch kỹ thuật.

Bản04 giữ nội dung/typography của chính pilot đó; default font mới ở các cảnh khác lấy06/12. Không âm thầm reskin04.

**Chốt:** Lấy frame cuối chính nguồn pilot.

**Nhân vật:** Không nhân vật; tập hợp ngành cần diện tích.

**Chữ trên hình:** VU AMSTERDAM / Kinh doanh / Khoa học dữ liệu / Trí tuệ nhân tạo / Luật / Khoa học sức khoẻ. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `campus_shell` — **available_source_extend_only**. Vỏ mô hình campus có sàn/cột từ06.05 chỉ cần bao quanh ảnh để nối sang06; không tự dựng phòng khác trong pilot. Tách: roof, side walls, floors, columns, photo cover. Nguồn: reference_pilots/scene_06/index.html #c6-drawing and #c6-photo.
- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.

**Nối sang cảnh sau:** 07 hard cut sang cuộn bằng ở bối cảnh học thuật.

**Vì sao HF_ONLY:** Quan hệ tập hợp ngành trong cùng trường cần các lớp đồng hiện; người thật đi qua từng phòng sẽ biến thành hành trình sai nghĩa.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 07 · Giá trị học thuật trong bối cảnh quốc tế

**Voice gốc:** Tấm bằng từ VU Amsterdam được các doanh nghiệp và tổ chức quốc tế đánh giá cao,

**Thời lượng:** 4.283333333s · sample 644652–747452 · audio `inputs/audio/scene_07.wav`.

**Ý cần đọc được:** Minh hoạ giá trị bằng cấp ở cấp trường, không nói Nhật đã tốt nghiệp hoặc có thư nhận việc.

**Dàn khung:** Cuộn bằng tượng trưng x180–540/y480–785; một bàn đọc tài liệu ở tiền cảnh y820–980; bối cảnh nghiên cứu trái và nơi làm việc phải là hai cánh không gian mở, không hộp thông tin.

**Mở cảnh:** Hard cut từ mô hình06 sang cuộn giấy buộc dải xanh trên bàn; không tiếp tục chuyển từng ngành.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.000s|Tấm bằng từ VU Amsterdam|Cuộn giấy bung ngang một phần; chỉ có tên trường và một dấu trang trung tính, không chữ ký/con dấu/serial chứng chỉ.|
|1.00–2.600s|được các doanh nghiệp và tổ chức quốc tế|Góc nhìn mở rộng, thấy bàn nghiên cứu bên trái và bàn làm việc nhóm bên phải trong cùng một trường nhìn; không gắn logo nhà tuyển dụng.|
|2.60–3.700s|đánh giá cao|Một bàn tay người đọc đưa tài liệu học thuật kèm cuộn giấy về vùng đọc, động tác xem xét có chủ ý; không tick đỗ hay bắt tay tuyển dụng.|
|3.70–4.283s|kết câu|Giữ cuộn giấy và hai bối cảnh đủ nhận ra; dải xanh dẫn màu sang08, không ép biến hình.|

**Chốt:** Giá trị học thuật được đặt trong môi trường học/nghiên cứu/làm việc, chưa có kết quả cá nhân.

**Nhân vật:** Không Nhật trong cảnh này để tránh hiểu rằng Nhật đã nhận bằng; chỉ tay người đọc vô danh.

**Chữ trên hình:** VU Amsterdam / GIÁ TRỊ HỌC THUẬT. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `credential_prop` — **to_draw**. Cuộn giấy học thuật tượng trưng, dải xanh, chỉ tên VU Amsterdam khi bung. Không sao chép mẫu bằng thật, chữ ký, mã số, điểm, dấu công nhận. Tách: paper curl, opening paper, ribbon, printed university name. Nguồn: original illustration; depicts institutional degree concept, not Nhật graduation.
- `international_workspaces` — **to_draw**. Hai cánh bối cảnh mở: bàn đọc/nghiên cứu và bàn làm việc nhóm. Khối bàn, ghế, đèn và tài liệu cùng không gian; không avatar cards, không logo doanh nghiệp. Tách: left reading desk, right collaboration desk, foreground table. Nguồn: new illustration, generic contexts not actual employers.
- `reader_hand` — **to_draw**. Một bàn tay vô danh đưa cuộn giấy/tài liệu về phía đọc, không đóng dấu phê duyệt. Tách: hand, paper contact. Nguồn: same neutral thin outline as other hands.

**Nối sang cảnh sau:** Hard cut sang globe08; màu xanh cuộn bằng nối bằng màu, không cần transition có hiệu ứng.

**Vì sao HF_ONLY:** Cuộn giấy và hai cánh bối cảnh là minh hoạ khái niệm/giá trị học thuật. HYBRID bằng thật hoặc actor nhận bằng dễ bị hiểu thành chứng cứ tốt nghiệp/tuyển dụng của Nhật chưa có.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 08 · Cơ hội là các lựa chọn mở

**Voice gốc:** mở ra nhiều cơ hội học tập và nghề nghiệp trên toàn cầu.

**Thời lượng:** 3.113000000s · sample 747452–822164 · audio `inputs/audio/scene_08.wav`.

**Ý cần đọc được:** Thể hiện phạm vi toàn cầu và hai hướng học tập/nghề nghiệp mà không đảm bảo kết quả.

**Dàn khung:** Globe giấy x140–585/y390–870; không gian học nhóm nhỏ nhô phía trên trái x110–315/y360–550; bàn làm việc phía phải x430–625/y565–760; Nhật ở tiền cảnh x385–540/y815–1010.

**Mở cảnh:** Nhật nhìn một địa cầu giấy, các lục địa là mảng sáng có nét viền mảnh.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.800s|mở ra nhiều cơ hội|Nhật đẩy địa cầu xoay một góc nhỏ; không chạy máy bay qua các điểm.|
|0.80–2.000s|học tập và nghề nghiệp|Một cảnh bàn học nhóm và một cảnh bàn làm việc mở lên từ bề mặt địa cầu, hai lựa chọn ngang hàng, không nối mũi tên nhân quả.|
|2.00–3.113s|trên toàn cầu|Nhật nhìn lần lượt hai hướng và giữ cả hai hiện diện; chỉ một headline ngắn nếu đọc đủ.|

**Chốt:** Hai khả năng cùng mở trên một thế giới, nhân vật chưa chọn kết quả.

**Nhân vật:** Xoay globe và quan sát lựa chọn; không đứng chỉ trang trí.

**Chữ trên hình:** CƠ HỘI RỘNG MỞ. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `paper_globe` — **to_draw**. Địa cầu giấy có trục, lục địa đơn giản tương đối đúng; mở hai bối cảnh ngang hàng từ mặt cầu. Tách: sphere, continents clipping group, axis/base, foreground rim. Nguồn: original vector geometry; no country data or flight paths.
- `opportunity_settings` — **to_draw**. Một bàn học nhóm và một bàn công việc thật trong hình minh hoạ; mỗi nhóm gồm mặt bàn/ghế/người nhỏ đang làm việc, không icon briefcase/mũ tốt nghiệp đứng rời. Tách: study table setting, work table setting, paper tabs connecting to globe. Nguồn: generic possible settings, no claim of job/visa outcome.

**Nối sang cảnh sau:** Cắt tương phản sang cận ảnh VU trên tường ở09: từ khả năng lớn quay về công việc rất cụ thể.

**Vì sao HF_ONLY:** Địa cầu giấy và hai khả năng cùng nâng từ bề mặt biểu đạt phạm vi/khả năng. HYBRID đi tới điểm đến thật có thể thêm kết quả du học hoặc công việc chưa xảy ra; organic camera không cải thiện quan hệ song song này.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 09 · Đằng sau thành quả là một bàn làm việc

**Voice gốc:** Đằng sau thành quả ấy là cả một quá trình chuẩn bị nghiêm túc.

**Thời lượng:** 3.404083333s · sample 822164–903862 · audio `inputs/audio/scene_09.wav`.

**Ý cần đọc được:** Đảo điểm nhìn từ thành quả sang quá trình chuẩn bị bằng một cú reveal môi trường.

**Dàn khung:** Mở cận ảnh VU x100–620/y350–780; lùi thành wide room: ảnh trên tường x90–340/y350–520, bàn y700–960, Nhật viết ở x330–480/y650–1000. Cùng phòng01 nhưng có nhiều dấu vết làm việc hơn.

**Mở cảnh:** Ảnh VU có băng dính treo trên tường; chưa thấy người đang viết ở dưới.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.850s|Đằng sau thành quả ấy|Máy lùi từ ảnh, lộ mép tường và đèn bàn.|
|0.85–2.600s|cả một quá trình chuẩn bị|Lộ Nhật đang sửa một trang nháp, bên cạnh có hai bản nháp cũ và cuốn sổ xanh; tay gạch một nét rồi viết lại bằng bút cam.|
|2.60–3.404s|nghiêm túc|Nhật đặt bản đã sửa lên trên, đẩy bản cũ sang bên và nhìn lại; dừng trên hành động thay vì bắn thêm checklist.|

**Chốt:** Một trang đang được cải thiện trên bàn, không chỉ chồng giấy trang trí.

**Nhân vật:** Đọc lại, sửa, thay bản; góc phòng giữ sự tập trung.

**Chữ trên hình:** PHÍA SAU THÀNH QUẢ. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `room` — **to_draw**. Một góc phòng học lilac sáng, cửa sổ lớn có rèm kéo, đèn nhỏ và một cây;09 thêm dấu vết bản nháp. Không lấp phòng bằng đồ trang trí ngẫu nhiên. Tách: wall/window frame, moving blind, far roofs layers, desk plane, lamp, plant. Nguồn: original vector layers; no room photo needed.
- `work_desk` — **to_draw**. Bàn09/10/15 cùng màu gỗ sáng, đèn phía trái, ngăn giấy cạnh phải. Có wide room, chéo qua bàn, close tay dùng chung asset. Tách: back desk edge, surface, front edge for hand occlusion, lamp. Nguồn: reuse scene01 desk language without cloning whole composition.
- `draft_pages` — **to_draw**. Một tờ nháp có dấu cam và hai bản cũ. Các nét dòng là texture giấy, không tạo chữ nhỏ đọc được hay paragraph mô tả; vị trí một đoạn sửa được khoanh bằng bút rồi viết lại. Tách: current page, old drafts, circle/correction ink, new orange strokes. Nguồn: original illustrative writing, no actual application content.
- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.

**Nối sang cảnh sau:** 10 cận đúng trang đang sửa; mentor bước vào hành động ở góc đối diện bàn.

**Vì sao HF_ONLY:** Cú lùi từ ảnh thành quả lộ lớp bản nháp là một reveal được thiết kế. HYBRID người viết thật chỉ tái hiện cảnh làm việc, mất quan hệ lớp giấy/collage và nhân vật đã thống nhất.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 10 · Mentor giúp Nhật làm rõ lựa chọn

**Voice gốc:** Với sự đồng hành của đội ngũ Mentor Esora hơn 14 năm kinh nghiệm,

**Thời lượng:** 3.486125000s · sample 903862–987529 · audio `inputs/audio/scene_10.wav`.

**Ý cần đọc được:** Thể hiện đồng hành bằng góp ý cụ thể, Nhật vẫn là tác giả và người quyết định.

**Dàn khung:** Góc chéo qua bàn: Nhật trái x180–335/y650–1000; mentor phải x430–580/y625–1000; một trang lớn chung x210–510/y500–770. Mentor dáng gọn màu xanh lục nhạt, kính tròn, tỉ lệ cùng thế giới Nhật; không giống người thật cụ thể.

**Mở cảnh:** Trang nháp từ09 nằm giữa hai người. Mentor dùng đầu bút chỉ một đoạn trên chính trang.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.750s|Với sự đồng hành|Mentor nghiêng người xem trang, Nhật nhìn theo đầu bút.|
|0.75–2.000s|đội ngũ Mentor Esora|Mentor khoanh gọn một đoạn cần làm rõ, rồi đưa lại bút; nhãn MENTOR ESORA đặt gần nhân vật mentor, không có nét nối.|
|2.00–3.000s|hơn14năm kinh nghiệm|Nhật tự viết lại đoạn ấy bằng bút cam, mentor quan sát và gật đầu. Không hiển thị số14 hoặc huy hiệu kinh nghiệm.|
|3.00–3.486s|kết câu|Giữ trang có một điểm sửa rõ; Nhật kéo trang về phía mình để đưa vào hồ sơ11.|

**Chốt:** Trang sửa tốt hơn nhưng nét viết vẫn thuộc Nhật; mentor không viết hộ toàn bài.

**Nhân vật:** Hai vai rõ: mentor chỉ/góp ý; Nhật chỉnh sửa và sở hữu trang.

**Chữ trên hình:** MENTOR ESORA. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `mentor` — **to_draw**. Mentor riêng biệt nhưng cùng tỉ lệ mascot: thân nhỏ xanh lục nhạt #91B59F, kính tròn, tay áo kem; không cap/ba lô của Nhật. Chỉ xem trang, chỉ/góp ý và giữ kẹp; không thêm hành động thắng cúp. Tách: body, glasses/head, far arm, near arm, contact hands, nod pose. Nguồn: original symbolic adviser, not real person likeness.
- `work_desk` — **to_draw**. Bàn09/10/15 cùng màu gỗ sáng, đèn phía trái, ngăn giấy cạnh phải. Có wide room, chéo qua bàn, close tay dùng chung asset. Tách: back desk edge, surface, front edge for hand occlusion, lamp. Nguồn: reuse scene01 desk language without cloning whole composition.
- `draft_pages` — **to_draw**. Một tờ nháp có dấu cam và hai bản cũ. Các nét dòng là texture giấy, không tạo chữ nhỏ đọc được hay paragraph mô tả; vị trí một đoạn sửa được khoanh bằng bút rồi viết lại. Tách: current page, old drafts, circle/correction ink, new orange strokes. Nguồn: original illustrative writing, no actual application content.
- `pen_pair` — **to_draw**. Bút góp ý màu đất đỏ và bút cam của Nhật; đổi tay sau khi mentor góp ý, không để bút dịch mà bàn tay không nắm. Tách: two pens, grip overlays. Nguồn: one signature correction on real paper, not label pointers.

**Nối sang cảnh sau:** 11 chuyển overhead ngay khi Nhật kéo trang; dùng đúng tờ giấy ấy, không mở một bộ hồ sơ từ đầu khác.

**Vì sao HF_ONLY:** Hai nét bút/động tác trên cùng mặt giấy diễn đạt quyền tác giả và hỗ trợ, cần các lớp minh hoạ phối hợp. HYBRID cuộc tư vấn diễn viên có thể bị nhận là cuộc gặp thật chưa được cung cấp; không cần organic actor performance.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.

**Cần kiểm chứng trước công bố:** voice nói Mentor hơn14năm. Nguồn Esora hiện ghi tổ chức hơn13năm, chưa chứng minh trải nghiệm đội Mentor. Vẫn giữ nguyên voice cho workprint riêng; không làm số14/huy hiệu trên hình và không tự sửa audio. Xem RESEARCH.md.


# 11 · Thành tích là chất liệu của bộ hồ sơ

**Voice gốc:** Minh Nhật đã xây dựng một bộ hồ sơ không chỉ thể hiện thành tích học tập,

**Thời lượng:** 3.564333333s · sample 987529–1073073 · audio `inputs/audio/scene_11.wav`.

**Ý cần đọc được:** Hồ sơ phải có căn cứ, nhưng chưa đủ để nói hết về con người.

**Dàn khung:** Overhead folder xanh như12: x72–660/y365–1001, mở trang. Tay Nhật từ dưới. Trang nháp ở giữa; hai mảnh giấy học tập là vật liệu ở mép trái, không chữ điểm/số liệu.

**Mở cảnh:** Bìa hồ sơ mở, trang từ10 đang được đặt vào; mép giấy có dấu cam của Nhật.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.900s|Minh Nhật đã xây dựng|Nhật đặt trang đã chỉnh vào bìa và giữ góc để các lớp không rơi.|
|0.90–2.400s|một bộ hồ sơ|Hai mảnh chất liệu học tập được luồn vào cùng trang: ghi chép và một trang hoạt động học tập minh hoạ, không làm giấy chứng nhận giả.|
|2.40–3.564s|không chỉ thể hiện thành tích học tập|Nhật lật một trang, để lộ trang còn lại trống cho cách tư duy/cá tính/mục tiêu; đưa bố cục về đầu12.|

**Chốt:** Căn bố cục bìa xanh/trang trái-phải theo frame0 pilot12; những mảnh bằng chứng đã đi vào trang trước.

**Nhân vật:** Tay đặt giấy, giữ góc và lật trang; có nguyên nhân/tiếp xúc/hệ quả.

**Chữ trên hình:** HỒ SƠ MINH NHẬT. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_hands` — **to_draw_from_reference**. Bàn tay/ống tay của Nhật nhìn overhead; ba tư thế: mở/gấp, giữ giấy, đặt mảnh. Chỉ tay thật của nhân vật, không bàn tay người thật lạc style. Tách: far hand, near hand, contact/grip layer. Nguồn: reference_pilots/scene_12/assets/portrait-v5.js as colour/line reference.
- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.
- `study_evidence` — **to_draw**. Hai giấy vật liệu học tập: trang ghi chép và bản nháp hoạt động học tập với sơ đồ trung tính. Không GPA/chứng chỉ/giải thưởng/tên dự án bịa. Tách: note fragment, learning-work fragment, paper clips. Nguồn: source voice gives only general academic achievements; keep details illustrative.
- `draft_pages` — **to_draw**. Một tờ nháp có dấu cam và hai bản cũ. Các nét dòng là texture giấy, không tạo chữ nhỏ đọc được hay paragraph mô tả; vị trí một đoạn sửa được khoanh bằng bút rồi viết lại. Tách: current page, old drafts, circle/correction ink, new orange strokes. Nguồn: original illustrative writing, no actual application content.

**Nối sang cảnh sau:** Match cut sang pilot12 bảnv6. Không cho hình ghép/nhân vật/ảnh mục tiêu xuất hiện sớm ở11.

**Vì sao HF_ONLY:** Ghép vật liệu giấy thành hồ sơ và lật sang trang cá nhân là quan hệ đồ hoạ. HYBRID tài liệu thật đòi bằng chứng cá nhân chưa có và dễ làm giấy bịa trông xác thực.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 12 · Ba thành phần cốt lõi

**Voice gốc:** mà còn phản ánh rõ tư duy, cá tính và định hướng phát triển của bản thân.

**Thời lượng:** 4.419250000s · sample 1073073–1179135 · audio `inputs/audio/scene_12.wav`.

**Ý cần đọc được:** Hình ghép/Tư duy, tự cá nhân hoá/Cá tính, ảnh mục tiêu trên kế hoạch/Định hướng; không leader lines.

**Dàn khung:** Giữ bố cục nguồn pilot đã đóng băng, không tự thiết kế lại.

**Mở cảnh:** Lấy frame đầu chính nguồn pilot.

**Dùng bản đã có:** `reference_pilots/scene_12/renders/pilot.mp4`. Nguồn: `reference_pilots/scene_12/index.html`.

Không tự dựng lại hình chính. Cảnh trước/sau hấp thụ nối cảnh; chỉ xử lý frame/audio theo kế hoạch kỹ thuật.

Bản04 giữ nội dung/typography của chính pilot đó; default font mới ở các cảnh khác lấy06/12. Không âm thầm reskin04.

**Chốt:** Lấy frame cuối chính nguồn pilot.

**Nhân vật:** Tự đội mũ/đeo ba lô, nhìn và hướng tay vào ảnh mục tiêu.

**Chữ trên hình:** DẤU ẤN RIÊNG / Tư duy / Cá tính / Định hướng / VU Amsterdam. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.
- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `core_cutouts` — **available_source_extract**. Hình ghép, chân dung đã cá nhân hoá và ảnh VU từ12.14 chỉ lấy mảnh nhỏ làm chất liệu cho cùng một trang; không lặp nguyên bố cục12. Tách: tangram group, portrait group, campus paper photo. Nguồn: reference_pilots/scene_12/index.html #p12-puzzle/#p12-goal-photo and assets/portrait-v5.js.
- `vu_photo` — **available_frozen**. Ảnh VU Main Building chính thức. Giữ nguyên nội dung công trình, chỉ crop theo mặt giấy. Không gọi là UvA hoặc dùng ảnh logo trường khác. Tách: photo raster, paper border if required, tape if required. Nguồn: library/vu-campus.jpg ; https://vu.nl/en/about-vu/more-about/vu-main-building.

**Nối sang cảnh sau:** 13 mở rộng sang các sổ vật lý khác; không sửa đuôi12.

**Vì sao HF_ONLY:** Ba lớp tư duy/cá tính/định hướng biểu hiện bằng cấu trúc hình; ẩn dụ giấy mở không phải người đang biểu diễn.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 13 · Mỗi câu chuyện có một cấu trúc riêng

**Voice gốc:** Mỗi ứng viên đều có một câu chuyện riêng.

**Thời lượng:** 2.101916667s · sample 1179135–1229581 · audio `inputs/audio/scene_13.wav`.

**Ý cần đọc được:** Khác biệt giữa ứng viên là câu chuyện, không phải phân hạng tốt/xấu.

**Dàn khung:** Ba sổ vật lý có gáy, x95–625/y390–965, xếp fan nhẹ trên bàn. Cuốn của Nhật phía trước có bìa xanh và dấu cam; hai cuốn khác có chất liệu/mép kẹp khác nhau, không avatar/profile card.

**Mở cảnh:** Từ hồ sơ của12, camera lùi vừa đủ để thấy thêm hai cuốn sổ phía sau.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.550s|Mỗi ứng viên|Hai sổ còn lại được đẩy vào cùng bàn, bố cục fan mở, không lặp clone đồng kích thước đều hàng.|
|0.55–1.500s|một câu chuyện riêng|Mỗi sổ mở hé một trang khác cách sắp xếp giấy và dấu bút: cuốn Nhật giữ dấu cam; không tự gán sở thích/giải thưởng cho ai.|
|1.50–2.102s|riêng — chốt|Cuốn Nhật ở phía trước nghiêng mở tiếp, hai cuốn sau vẫn có giá trị ngang nhau.|

**Chốt:** Một cuốn được theo tiếp vì đây là câu chuyện Nhật, không vì hai cuốn kia bị loại.

**Nhân vật:** Không thêm nhân vật trong2.1s: chính các cuốn sổ thể hiện sự riêng biệt.

**Chữ trên hình:** CÂU CHUYỆN RIÊNG. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `notebook` — **to_draw**. Sổ xanh bìa mềm, một dấu cam ở góc và gáy rõ; có bìa đóng/mở, mép trang và clip. Chữ tên chỉ khi scene yêu cầu. Tách: front cover, spine, page block, opening page, orange bookmark. Nguồn: design based on selected blue/orange roles; not the old envelope.
- `story_notebooks` — **to_draw**. Hai cuốn sổ phụ có gáy, dấu bút và cách kẹp khác cuốn của Nhật; một pastel lilac, một peach. Không gán người/ngành/nghề/sở thích cụ thể. Tách: two covers/spines, two opening pages, different abstract marks. Nguồn: same paper material as notebook; not two generic profile cards.

**Nối sang cảnh sau:** 14 bám vào cuốn của Nhật khi mở trang; cắt hai cuốn còn lại ra khỏi khung bằng crop.

**Vì sao HF_ONLY:** Khác biệt giữa ba vật thể giấy cùng loại là ý chính, thời lượng rất ngắn. HYBRID thêm ba người thật sẽ biến thành ba hồ sơ cá nhân tưởng có thật và phân tán nội dung.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 14 · Kể có trọng tâm để người đọc hiểu mình

**Voice gốc:** Điều quan trọng là biết cách kể câu chuyện đó đúng cách để tạo dấu ấn với hội đồng tuyển sinh.

**Thời lượng:** 4.702750000s · sample 1229581–1342447 · audio `inputs/audio/scene_14.wav`.

**Ý cần đọc được:** Biến chất liệu có sẵn thành câu chuyện có mạch, không dùng dấu đỗ của hội đồng.

**Dàn khung:** Overhead một trang bài luận minh hoạ x125–595/y345–965. Ba chất liệu từ12 (tangram, chân dung, ảnh mục tiêu) đang ở lề/trang nháp; tay Nhật từ góc dưới phải. Dùng dấu in/đoạn nét không đọc được như chất liệu, không paragraph DOM.

**Mở cảnh:** Trang mở có nhiều mảnh cùng tranh sự chú ý, các mảnh thừa ở lề, chưa có trọng tâm.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.050s|Điều quan trọng|Nhật chọn mảnh chính là chân dung có nét riêng và kéo vào đầu trang, các mảnh thừa được đẩy về lề.|
|1.05–2.600s|kể câu chuyện đó đúng cách|Nhật đặt chất liệu chứng minh cách tư duy vào phần giữa, mục tiêu học tập ở phần kết; động tác sắp lại cùng một trang, không bật ba card mới.|
|2.60–3.800s|tạo dấu ấn|Máy chuyển sang góc nhìn trang giấy được nhấc lên: đọc từ đầu đến kết dễ hơn, một khoảng trắng rõ quanh hình chính.|
|3.80–4.703s|hội đồng tuyển sinh|Giữ trang hoàn chỉnh trong tay Nhật, như một câu chuyện sẵn sàng được đọc; không dựng hội đồng giả hoặc con dấu trúng tuyển.|

**Chốt:** Trang có ưu tiên đọc rõ, không phải một poster đầy đủ nhãn; tất cả ý giải thích còn ở voice.

**Nhân vật:** Nhật trực tiếp biên tập và nhấc trang để đọc lại, không để mentor làm thay.

**Chữ trên hình:** KỂ CÓ TRỌNG TÂM. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_hands` — **to_draw_from_reference**. Bàn tay/ống tay của Nhật nhìn overhead; ba tư thế: mở/gấp, giữ giấy, đặt mảnh. Chỉ tay thật của nhân vật, không bàn tay người thật lạc style. Tách: far hand, near hand, contact/grip layer. Nguồn: reference_pilots/scene_12/assets/portrait-v5.js as colour/line reference.
- `essay_page` — **to_draw**. Tờ bài luận minh hoạ với vùng mở đầu/chất liệu/chốt có thể sắp lại; chỉ vài nét in texture. Không paragraph thật, không nội dung bịa vào lời của Nhật. Tách: paper, quiet print strokes, foreground margin, lifted paper pose. Nguồn: physical essay surface, not a general information panel.
- `core_cutouts` — **available_source_extract**. Hình ghép, chân dung đã cá nhân hoá và ảnh VU từ12.14 chỉ lấy mảnh nhỏ làm chất liệu cho cùng một trang; không lặp nguyên bố cục12. Tách: tangram group, portrait group, campus paper photo. Nguồn: reference_pilots/scene_12/index.html #p12-puzzle/#p12-goal-photo and assets/portrait-v5.js.

**Nối sang cảnh sau:** 15 trở lại góc bàn, Nhật hạ chính tờ hoàn chỉnh vào bìa; continuity theo mép giấy và kẹp cam.

**Vì sao HF_ONLY:** Sắp lại phân cấp trên mặt giấy chính là ý kể đúng cách. HYBRID người nói/đọc bài sẽ không cho thấy cấu trúc nội dung thay đổi rõ bằng các lớp ghép.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 15 · Hoàn tất cùng người đồng hành

**Voice gốc:** Đó cũng chính là điều Esora đã đồng hành cùng Minh Nhật trong suốt hành trình ứng tuyển.

**Thời lượng:** 4.417291667s · sample 1342447–1448462 · audio `inputs/audio/scene_15.wav`.

**Ý cần đọc được:** Chốt vai trò hỗ trợ của Esora, quyền sở hữu câu chuyện vẫn ở Nhật.

**Dàn khung:** Góc bàn gần: bìa hồ sơ x150–565/y540–855; Nhật phải x425–575/y700–1010, mentor trái x145–285/y690–1010. Bàn cùng09/10, không dựng cảnh bắt tay mới.

**Mở cảnh:** Nhật đặt trang hoàn chỉnh từ14 vào bìa; mentor đang giữ một chiếc kẹp mở.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.100s|Đó cũng chính là điều Esora|Mentor giữ kẹp, Nhật đưa tờ cuối vào đúng chỗ, hai bàn tay phối hợp trên cùng đạo cụ.|
|1.10–2.700s|đồng hành cùng Minh Nhật|Nhật tự đóng bìa và gắn nhãn tên mình; mentor buông kẹp sau khi giấy đã chắc.|
|2.70–3.800s|suốt hành trình ứng tuyển|Nhật cầm bộ hồ sơ, mentor bước lùi nửa nhịp; Esora hiện dưới dạng chữ gần mentor, không logo tự chế.|
|3.80–4.417s|kết câu|Nhật mang hồ sơ ra phía phải khung; máy để lại một khoảng nhìn về chương tiếp theo.|

**Chốt:** Nhật cầm sản phẩm của chính mình, mentor ở vai trò hỗ trợ.

**Nhân vật:** Giữ kẹp → đặt giấy → đóng bìa → mentor buông → Nhật mang đi; không mannequin/handshake filler.

**Chữ trên hình:** MINH NHẬT / ESORA. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student` — **available_reference_rig**. Nhật: mascot cam bo góc, mũ tím, ba lô xanh, tay chân mảnh; là biểu tượng, không tự vẽ giống người thật. Thêm pose theo hành động từng cảnh. Tách: body, far arm, near arm, grasp hands, eyes/mouth, cap, bag, legs. Nguồn: library/student.js and library/portrait-v5.js; prefix IDs per scene.
- `mentor` — **to_draw**. Mentor riêng biệt nhưng cùng tỉ lệ mascot: thân nhỏ xanh lục nhạt #91B59F, kính tròn, tay áo kem; không cap/ba lô của Nhật. Chỉ xem trang, chỉ/góp ý và giữ kẹp; không thêm hành động thắng cúp. Tách: body, glasses/head, far arm, near arm, contact hands, nod pose. Nguồn: original symbolic adviser, not real person likeness.
- `work_desk` — **to_draw**. Bàn09/10/15 cùng màu gỗ sáng, đèn phía trái, ngăn giấy cạnh phải. Có wide room, chéo qua bàn, close tay dùng chung asset. Tách: back desk edge, surface, front edge for hand occlusion, lamp. Nguồn: reuse scene01 desk language without cloning whole composition.
- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.
- `binder_clip` — **to_draw**. Kẹp giấy đủ lớn để thấy hai tay giữ/luồn/nhả, tỉ lệ với hồ sơ. Tách: clip back, moving jaws, foreground hinge. Nguồn: new vector physical prop.

**Nối sang cảnh sau:** 16 dùng một page-turn của hồ sơ ở mép khung để mở minh hoạ Hà Lan; không thêm chuyến bay/hộ chiếu chưa có trong voice.

**Vì sao HF_ONLY:** Hành động ghép giấy/kẹp phối hợp và chuyển chủ thể sở hữu là semantic choreography trong thế giới giấy đã thống nhất. HYBRID handshake không diễn tả quyền tác giả, footage gặp mặt cũng chưa được cung cấp.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 16 · Chương mới được chúc mở ra

**Voice gốc:** Chúc Minh Nhật sẽ có một hành trình thật rực rỡ tại Hà Lan,

**Thời lượng:** 3.082500000s · sample 1448462–1522442 · audio `inputs/audio/scene_16.wav`.

**Ý cần đọc được:** Lời chúc cho hành trình Hà Lan, không khẳng định Nhật đã nhập cảnh hay tốt nghiệp.

**Dàn khung:** Wide cảnh kênh đào minh hoạ: cầu x80–650/y730–940; nước y840–1060; dãy mái nhà xa x100–630/y380–680. Nhật trên cầu x340–475/y700–980; một mép trang giấy còn thấy ở góc để rõ đây là chương mở.

**Mở cảnh:** Mép hồ sơ lật khỏi15; mặt sau trang là một phố kênh đào vẽ tay, không copy ảnh thành phố làm plate.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–0.700s|Chúc Minh Nhật|Trang mở, Nhật bước vào nhịp đầu trên cầu; tạm không có headline.|
|0.70–2.000s|hành trình thật rực rỡ|Nhật đeo ba lô và nhìn qua cầu; ánh nền mở sáng hơn, mặt nước gợn nhẹ, không pháo hoa hay cúp.|
|2.00–3.083s|tại Hà Lan|Nhật quay chào rồi hướng lại về phía trước; CHƯƠNG MỚI hiện ngắn trên vùng trời.|

**Chốt:** Đường phố thật trong tranh tiếp diễn về phía phải; Nhật sẵn sàng bước tiếp.

**Nhân vật:** Bước vào bối cảnh, nhìn và chào, sau đó quay lại phía trước; không đứng góc filler.

**Chữ trên hình:** CHƯƠNG MỚI. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_walk` — **to_extend_reference_rig**. Cùng mascot, stride2–3 tư thế và quay chào; bước chân có tiếp đất, tay giữ sổ khi đi. Tách: hips/body, alternating legs, free arm, book arm, head turn. Nguồn: library/student.js.
- `canal_scene` — **to_draw**. Phố Hà Lan minh hoạ, cầu thấp qua kênh, ba mái nhà gable, cửa sổ và nước. Không lấy landmark làm campus VU hoặc diễn tả đã tới địa điểm thực. Tách: far roofs, near facades, water, far bridge, bridge walking plane, near rail, page edge reveal. Nguồn: generic illustrated Dutch canal setting, no specific named landmark.
- `portfolio` — **available_source_extend**. Bìa xanh/trang đôi/gáy của12.11 lắp chất liệu trang trước rồi lật đúng hướng;15 đóng lại. Cần thêm trạng thái đóng và tờ trang đang lật. Tách: blue cover, spine, left/right paper, turning page, closed cover. Nguồn: reference_pilots/scene_12/index.html #p12-folder.

**Nối sang cảnh sau:** 17 tiếp đúng bước chân/không gian, không reset nhân vật về đầu cầu hoặc đổi trang phục.

**Vì sao HF_ONLY:** Trang giấy mở thành môi trường khát vọng là lời chúc được minh hoạ. HYBRID footage diễn viên ở Hà Lan dễ bị đọc thành chuyến đi đã xảy ra; lớp giấy là nội dung chứ không chỉ lớp trang trí.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.


# 17 · Hành trình còn tiếp

**Voice gốc:** tiếp tục phát huy bản lĩnh, khám phá những cơ hội mới và chinh phục nhiều cột mốc lớn hơn trong tương lai.

**Thời lượng:** 4.764916667s · sample 1522442–1636800 · audio `inputs/audio/scene_17.wav`.

**Ý cần đọc được:** Kết bằng sự chủ động và tương lai mở, không invent nghề nghiệp/học vị/mức lương.

**Dàn khung:** Bám Nhật từ góc3/4 trong cùng phố16. Nhật x300–435/y685–1005; không gian phía trước mở x430–680/y390–940. Máy kéo rộng vừa phải; nội dung vẫn chiếm đến y1040.

**Mở cảnh:** Nhật tiếp bước trên cầu rồi mở cuốn sổ xanh bên mình; những trang phía sau còn trắng.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.300s|tiếp tục phát huy bản lĩnh|Nhật dừng một nhịp, mở sổ và kẹp trang mới; giữ dấu cam của cảnh01 như callback.|
|1.30–2.800s|khám phá những cơ hội mới|Nhật khép sổ vào tay và bước khỏi nhịp cầu, khung nhìn mở thêm khoảng phố phía trước, không bay qua các career icons.|
|2.80–4.150s|chinh phục nhiều cột mốc lớn hơn|Nhật bước tiếp trong môi trường, mái nhà/tiền cảnh dịch theo parallax thật của góc nhìn; không mốc số/đích nghề nghiệp.|
|4.15–4.765s|trong tương lai|Giữ Nhật đang hướng tới phần phố ngoài khung cùng HÀNH TRÌNH CÒN TIẾP; kết nhẹ0.6s, không thêm CTA.|

**Chốt:** Có người đang đi tiếp và những trang chưa viết; không chốt một kết quả ngoài voice.

**Nhân vật:** Mở sổ, đánh dấu trang mới rồi chủ động đi tiếp; không chinh phục mục tiêu bịa.

**Chữ trên hình:** HÀNH TRÌNH CÒN TIẾP. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_walk` — **to_extend_reference_rig**. Cùng mascot, stride2–3 tư thế và quay chào; bước chân có tiếp đất, tay giữ sổ khi đi. Tách: hips/body, alternating legs, free arm, book arm, head turn. Nguồn: library/student.js.
- `canal_scene` — **to_draw**. Phố Hà Lan minh hoạ, cầu thấp qua kênh, ba mái nhà gable, cửa sổ và nước. Không lấy landmark làm campus VU hoặc diễn tả đã tới địa điểm thực. Tách: far roofs, near facades, water, far bridge, bridge walking plane, near rail, page edge reveal. Nguồn: generic illustrated Dutch canal setting, no specific named landmark.
- `notebook` — **to_draw**. Sổ xanh bìa mềm, một dấu cam ở góc và gáy rõ; có bìa đóng/mở, mép trang và clip. Chữ tên chỉ khi scene yêu cầu. Tách: front cover, spine, page block, opening page, orange bookmark. Nguồn: design based on selected blue/orange roles; not the old envelope.

**Nối sang cảnh sau:** Kết phim bằng hold0.6s và kết voice gốc; không logo/đăng ký/mời liên hệ tự thêm.

**Vì sao HF_ONLY:** Thế giới vẽ tiếp ra khỏi trang và callback cuốn sổ mang ý hành trình chưa hoàn tất. HYBRID montage công việc/tốt nghiệp sẽ thêm kết quả chưa có; chuyển động lớp giấy và bước đi vector đủ rõ.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.

### Ghi chú assembly04

Nguồn04cũ có #illustration-note; bỏ node đó trong bản phái sinh build/ rồi tái xuất hình, không sửa thiết kế hoặc source frozen. Xem TECHNICAL_HANDOFF.
