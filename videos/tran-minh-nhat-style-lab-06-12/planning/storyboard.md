# Hai cảnh thử — 06 và 12

Giữ routing HF_ONLY đã khoá trong storyboard gốc. Giữ nguyên hai lát voice: 06 = 5.1926666667s, 12 = 4.41925s. Không cắt lại, không thêm nhạc/TTS. Toàn bộ đầu ra nằm trong thư mục lab; không ghi vào scratch hay pilot cũ.

## 06 — Nhiều lĩnh vực trong cùng một trường

Mở bằng ảnh VU trên một mặt giấy; tờ ảnh mở ra thành mô hình kiến trúc có sàn/cột liên tục. Kinh doanh là một bàn phân tích, dữ liệu là workstation, AI là bảng mạng nghiên cứu, luật là phòng đọc, sức khoẻ là bàn thí nghiệm. Các không gian xuất hiện theo lời thoại và cùng tồn tại. Không nối thành dây chuyền, không minh hoạ thứ hạng hay quan hệ liên ngành cụ thể. Không gian bên trong hoàn toàn minh hoạ, không phải bản đồ phòng thật của VU.

Tại mỗi cue chỉ có một nhãn ngành chính, nhãn trước được thay thế; hình đã xuất hiện được giữ lại. Nhân vật được bỏ vì 5 lĩnh vực trong 5.19s cần dành ưu tiên cho kiến trúc và thao tác chuyên môn. Asset mới là cả mô hình và năm workspace; chỉ ảnh campus/font/runtime được tái sử dụng.

## 12 — Hồ sơ có dấu riêng

Một hồ sơ mở trên nền kem. Góc trang lật lên cạnh nhân vật. Một mảnh giấy cam xoay khớp vào cấu trúc hình ghép (tư duy); màu cam ấy kéo thành nét riêng (cá tính); nét phát triển thành một dải đường giấy nhô khỏi trang (định hướng). Nhân vật theo dõi/hướng tay về diễn biến này, không đóng vai cầm mọi vật thể. Không gán cho Nhật sở thích hoặc thành tích chưa có trong voice.

Chữ lần lượt TƯ DUY → CÁ TÍNH → ĐỊNH HƯỚNG, không dồn ba khối thông tin. Asset mới: bìa hồ sơ, spread giấy, góc lật, hình ghép tách lớp, nét cam và dải đường giấy. Nhân vật từ pilot được tái sử dụng vì là cùng chủ thể, nhưng có pose/timing mới.

## Ngôn ngữ chung và QA

Nét than #30313B, màu cam #FFAA28, xanh #087BC1, nền kem/tím nhạt; font Arial local từ pilot. Headline strip giữ gu, hình chủ đạo hoàn toàn khác cảnh phong bì. Nội dung chính nằm trên y1080, footer 200px trống. Nhãn >=36px, kiểm tra ở 360×640. Không dùng số điểm, xếp hạng, bằng cấp hay giấy tờ giả. Các mục asset, container, cue, routing, style candidates và dark-mass nằm trong storyboard.json.

Catalog tìm “architectural cutaway building rooms paper pop up book”: words tier, kết quả gần nhất paper-collage-reveal là tán mảnh giấy, không giải quyết mô hình mặt cắt hay hồ sơ tự mở; dùng cơ chế SVG riêng thay vì cài hiệu ứng chuyển cảnh không phù hợp.

## Revision 2 — theo feedback

Tiêu đề/nhãn cả hai cảnh đổi sang Arial Black900. Cảnh12: nhãn **Tư duy** gắn ngay dưới hình ghép, có nét nối; **Định hướng** gắn trên đầu đường giấy. Hai nhãn được giữ tới hết cảnh, không còn chỉ chạy ở đầu màn hình. Cá tính vẫn là nhãn tạm theo cue. Vị trí được kiểm tra trên khung hình MP4 ở360×640.

## Revision 3 — sửa font tiếng Việt

Thay Arial Black bằng Segoe UI Black900. Font trước thiếu các glyph ư/ạ/Ấ/ẻ/ệ/ị/ọ/ớ/ứ/ữ; font mới đã kiểm tra đủ tất cả chữ đang hiển thị. Layout và nhãn gắn trực tiếp của revision2 giữ nguyên.

## Revision4

Bỏ toàn bộ dòng chú thích minh hoạ trên hình theo yêu cầu. Giữ thông tin nguồn và tính chất minh hoạ trong tài liệu dự án.

## Revision5 — dựng lại cảnh12 theo storyboard đã chốt

0–1.5s: hình ghép → Tư duy. 1.5–2.7s: chân dung giấy tự đội mũ/đeo ba lô, có nét mặt riêng → Cá tính. 2.7–3.7s: bản phác bản thân tương lai hiện phía trên và được chọn bằng dấu ngắm → Định hướng. 3.7–4.41925s: giữ đủ ba thành phần, ba nhãn. Bỏ toàn bộ đường cam/đường giấy cũ; chân dung giấy là chủ thể hành động, không thêm một nhân vật góc dưới trùng lặp. Tương lai là hình dung minh hoạ, không gán nghề nghiệp hay thành tích.

## Revision6 — mục tiêu học tập cụ thể

Bỏ nét nối chú thích. Giữ tư duy/hình ghép và cá tính/tự đội mũ đeo ba lô. Định hướng đổi thành chọn ảnh VU Amsterdam, đặt lên một bản kế hoạch có vị trí mục tiêu còn trống rồi khoanh lựa chọn. Không bản sao tương lai, không dấu ngắm, không đường đi. Ba nhãn chỉ đặt gần hình tương ứng.
