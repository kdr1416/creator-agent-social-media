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
