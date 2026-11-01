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
