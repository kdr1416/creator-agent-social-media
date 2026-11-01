> **27/10/2026: Bộ frame S13/S14 design R1 đã được người dùng duyệt.** Motion chưa dựng/chưa duyệt. APPROVAL.json khóa đúng manifest ảnh. Thông báo này thay trạng thái chờ duyệt hình trong lịch sử bên dưới.

# S13/S14 — thiết kế cảnh kết R1

Trạng thái: đề xuất chờ duyệt frame. Sáu pose tĩnh, chưa có motion mới, chưa thay master. S10/S12 motion R1 đã được duyệt riêng. Hai cảnh này giữ HF_ONLY; không đổi voice hay routing.

## S13 — Con và kế hoạch tài sản mở rộng phạm vi

Voice segment15, sample [1530028,1639305), 4.553208333333s: “Khi con đã bước ra thế giới, tài sản của gia đình cũng có thể bước ra thế giới.” Raw/corrected text giữ nguyên trong VOICE_REFERENCE.json.

Bỏ quả địa cầu và hai quỹ đạo không nhận ra chủ thể. Cảnh có hai shot: một hành trình học tập cụ thể rồi một khung so sánh địa điểm tài sản.

Pose 01: mascot tới trước một campus không mang tên trường thật. Cổng vào, bậc thang và con đường đủ lớn để đọc môi trường học tập; nhãn CHÂU ÂU là nhãn địa lý, không tên cơ sở. Mascot có bước đi/ánh nhìn hướng lối vào, không đi xuyên cửa hoặc nhảy lên bậc.
Pose 02: cắt sang căn nhà Việt Nam ở khung cận, nhãn Việt Nam gắn với mặt đất. Nhà là minh họa tài sản đã có trong lập luận của phim, không phải tài sản cụ thể của một gia đình có thật.
Pose 03: mở rộng khung để thấy thêm một địa điểm Malta bên cạnh; nhà Việt Nam vẫn còn. Từ CÓ THỂ giữ đúng tính cân nhắc của câu. Hai công trình đứng nguyên tại các site; không cho căn nhà bay qua biên giới hoặc tự biến thành căn nhà khác.

Khi dựng dùng một camera wrapper cho cả không gian hai site. Khung đầu camera translate(94,-250) scale1.4, khung rộng translate(0,0) scale1; không scale từng nhà để giả phát sinh tài sản. Site Malta nằm ngoài vùng nhìn lúc đầu; xử lý phần shadow/ground ở mép ảnh bằng crop/viewport chung, không để một mẩu asset bị cắt vô nghĩa. Nếu nội suy camera làm chật chữ, label/overlay có thể để ở root và đổi vị trí theo framing, nhưng không lặp nhãn.

Nhịp đề xuất: khoảng 0–1.8s campus/con; tới vế “tài sản của gia đình” cắt sang nhà Việt Nam; “cũng có thể” bắt đầu pull-out; resolve hai địa điểm tới hết4.5532s. Đây là cue dự kiến, cần đối chiếu WAV. Rút bớt bước đi thay vì nhồi animation hoặc kéo dài voice.

Chữ: HÀNH TRÌNH CỦA CON / CHÂU ÂU ở shot1; TÀI SẢN GIA ĐÌNH, VIỆT NAM, MALTA và CÓ THỂ ở shot2. Không transcript paragraph, chart lợi nhuận, mũi tên chuyển tiền hoặc biểu tượng quyền làm việc/cư trú. Không thêm người đứng chỉ vào hai ngôi nhà trong shot dày hình; mascot chỉ xuất hiện có nhiệm vụ ở shot campus.

## S14 — Thêm lựa chọn cho tương lai

Voice segments16+17, sample [1639305,1803840), 6.855625s. Giữ trọn câu và cả khoảng nghỉ nguồn; không fade đen/cắt đuôi voice.

Bỏ tờ giấy hình nhánh cây chỉ đổi màu. Một chìa khóa cụ thể dẫn tới một không gian có hai lối đi, và việc mở cổng làm lộ thêm một khả năng.

Pose 01: mascot cầm chìa khóa nhà. Tay gắn với vai và vòng khóa; có một charm mái nhà nhỏ. Đây là cận vật thể kết nối lời “thêm một căn nhà”, không hồ sơ hay quyền pháp lý.
Pose 02: cắt rộng sang ngã rẽ. Lối thăm con đã mở; lối kế hoạch dài hạn có một cổng nhỏ đang đóng. Hai đích xa là một môi trường học tập và một môi trường sinh sống được vẽ tượng trưng, không chương trình/địa chỉ cụ thể. Người mẹ nắm đúng tay nắm cổng, mascot nhìn theo.
Pose 03: người mẹ bước theo tay nắm và mở cổng, đứng sang bên để cả hai lối cùng mở. Gia đình dừng ở điểm có thể lựa chọn, không bị đẩy đi qua lối mới. Text kết là THÊM MỘT LỰA CHỌN. Không phải hai kết quả đã được cấp phép/đảm bảo.

Bản lề cố định tại(570,700)/(570,900). Gate đóng có cạnh tự do x440; handle(465,760). Gate mở dự kiến panel[(570,700),(635,724),(635,924),(570,900)], handle(625,780). Người mẹ dịch từ x360 sang x505, y620/scale1.2 giữ nền, tay theo handle; không kéo dài cánh tay để chạm vị trí cuối trong khi thân đứng yên. Khi dựng dùng hinged/projected rigid leaf hoặc mô hình3D phù hợp, không bóp/morph toàn cổng độc lập với thanh/handle. Chưa khẳng định các pose đã chứng minh nội suy hình học đúng.

Nhịp đề xuất: đầu0–2.4s đọc chìa khóa; cắt ngã rẽ/cổng đóng để giới thiệu lựa chọn; theo cụm “mà là… lựa chọn” mở cổng; giữ cả hai lối mở tới hết voice. Đối chiếu WAV trước khi khóa thời điểm. Không nối chìa khóa nhà thành chìa mở quyền đi lại: có editorial cut, cổng là ẩn dụ quyết định gia đình, không biên giới/checkpoint/giấy phép. Các nhãn THĂM CON và KẾ HOẠCH DÀI HẠN bám ý các chuyến thăm/kế hoạch trước đó trong voice; không thêm quyền lợi mới.

## Continuity, style và asset

S13 dùng campus lớn → hai mặt tiền tài sản; S14 đổi sang vật thể cận → môi trường ngã rẽ/cổng. Không nối đúng cùng bước chân/cửa/căn nhà giữa hai scene. S09 đã nói cơ chế phân bổ, S13 chỉ nhắc khả năng mở rộng phạm vi bằng hình cụ thể. S03 từng có hành trình học/career; S14 là lựa chọn của gia đình, với cổng đang được mở và hai lối cùng giữ lại.

Nền kem/đào/lilac/địa hình tint sáng; mascot cam mũ tím ba lô xanh, người mẹ tóc tím/áo mint theo các vòng duyệt. Font Segoe UI Black local. Footer y1080–1280 sạch. Buildings là vector gốc tượng trưng, không listing, không tên/logo trường hoặc giấy tờ chính thức. Không có text “Hình minh họa/Không gian minh họa” trên hình.

Tách lớp S13: campus/tường/cửa/bậc/ground; mascot/mắt/tay/chân; hai site; từng facade/roof/balcony/door; camera wrapper; country/modal labels.
Tách lớp S14: key/loop/charm và palm; ground/left path/right path; hai endpoint vignettes; gate posts/hinges/panel/bars/handle; mẹ và mascot với shoulders/forearms/hands/eyes; headline/labels. Foreground/background phải giữ occlusion, không cho tay/vật rời nhân vật.

Phần giữ: chủ thể và quan hệ, hai site không thay thế nhau, tính “có thể”, hai lối cùng mở, voice/sample bounds, nhận diện, footer. Linh hoạt: crop/pose/tint/easing, mức đơn giản kiến trúc, cue nội cảnh sau đối chiếu audio. Nếu gate mở vẫn che lối đi, ưu tiên chỉnh vị trí mẹ/leaf trong safe area để đọc rõ, không tự đổi sang thông điệp khác.

Sau khi duyệt hình mới dựng pilot; kiểm frame tiếp xúc/hinge/camera trong tiến trình, 360×640, grayscale và playback. Hiện chưa tạo MP4 hoặc thay master.
