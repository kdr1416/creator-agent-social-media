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
