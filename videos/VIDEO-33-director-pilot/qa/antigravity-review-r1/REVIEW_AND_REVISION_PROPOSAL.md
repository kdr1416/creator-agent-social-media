# Review bản Antigravity — VIDEO-33 / R1

Trạng thái: kiểm tra và đề xuất sửa, chưa thay source, storyboard đã duyệt, status sản xuất hoặc render lại. Đây không phải duyệt phương án sửa.

## Khóa đúng bản kiểm tra

Master: build/renders/VIDEO-33-master.mp4 — SHA256 6f51c8368997f7e2d3721888c3a3d471c2407e8718248fc9d3bea6e4b2b87c50.
Clean: build/renders/VIDEO-33-clean.mp4 — SHA256 7050ecb46b98b8b6f50fdce327bcd25c2e8879c282e3c1ef9b417839f05a22b4.
Hai hash đã đo lại, khớp danh sách người dùng. File MP4 S01 và S09 trong build bằng từng byte với hai pilot đã duyệt. Không đề xuất dựng lại chúng.

Bản có 14 cảnh dựng / 17 đoạn voice. Số dưới đây dùng số đoạn voice để đối chiếu phản hồi 11–17, kèm scene dựng và thời gian master xấp xỉ. Có thể lệch dưới một frame giữa sample audio và hình ghép.

## Bằng chứng và giới hạn

Đã trích 4 thời điểm từ MP4 từng cảnh S06, S07, S08, S10, S11, S12, S13, S14; xem contact-1.jpg và contact-2.jpg, samples.json. Đã đọc source động tác liên quan; S08 được phát tới 0:05/0:05 trong browser. Chưa xem liên tục toàn master hoặc thẩm định lại từng âm voice. Không coi 4 frame là kiểm tra mọi lỗi thoáng qua.

S14 vẫn có đổi màu nhánh và cử động nhỏ; không phải mọi frame giống hệt nhau. Bộ phát hiện freeze ở ngưỡng -50dB báo freeze từ t0 trong cả đoạn; kết quả phản ánh lượng thay đổi toàn khung rất ít, không chứng minh tuyệt đối ảnh tĩnh.

## Chẩn đoán chung

1. Lỗi rig: nhiều tween x/y ghi đè tọa độ SVG đã đặt sẵn; đây là tọa độ đích tuyệt đối theo cách tween hiện tại, không phải dịch tương đối vài pixel như comment mô tả. Có bằng chứng hình và source ở S07/S08, các cảnh khác cần kiểm kỹ từng pose trước khi chốt cùng nguyên nhân.
2. Thiếu tiếp xúc: tay, prop và mục tiêu được animate riêng, không chia cùng điểm bám. Hành động chạm/kéo/cất không đọc được.
3. Phân cấp yếu: quá nhiều hình nhỏ và chi tiết nằm xa nhau; chữ dẫn dắt nhưng hình không cho thấy quan hệ.
4. Ý tưởng trước đây cũng có phần chưa đủ rõ: dụng cụ = cơ hội, hai quỹ đạo = con/tài sản, nhánh cây = lựa chọn là những phép ẩn dụ chưa tự giải thích được trong thời lượng này. Cần sửa thiết kế, không chỉ vá easing.

## Hướng sửa từng đoạn

### Voice 06 → S06 / 23.86–29.65s

Voice: “Không chỉ là sở hữu một tài sản ở Châu Âu, đây còn là cách xây dựng một nền tảng lâu dài cho cả gia đình.”
Hiện thấy: người nhỏ lơ lửng sau bàn; một người chạy ra mép trái; phần mở bàn thành đĩa/khối rời. Mối liên hệ kéo bàn không rõ. Source animate x:-18 cho người đã translate(540,665), scaleX cho lá bàn không đồng bộ bàn chính/chân/điểm nắm.
Đề xuất: bỏ cơ chế bàn kéo. Một góc sinh hoạt gia đình rõ sàn và phối cảnh; hai người thân ngồi sẵn, mascot kéo một chiếc ghế còn trống ra mời người còn lại. Kết là cả nhà cùng quanh một bàn nhỏ, cùng nhìn một bản kế hoạch. Mở đầu là chỗ chưa sẵn sàng; thay đổi là có chỗ cho người thân, không phải vật thể phình ra. Nhân vật phụ có thân/tay/chân/ghế đầy đủ, cùng tỷ lệ; không để bust bay trên bàn. 0–1.4s đọc không gian, 1.4–3.7s kéo ghế/contact, 3.7–5.8s cả nhà ổn định. Không phải cảnh trao quyền cư trú.

### Voice 07 → S07 / 29.65–34.35s

Voice: “Khi có một tài sản tại Malta, gia đình có thêm một điểm kết nối với Châu Âu,”
Hiện thấy: tay/đầu cắm xa thân, dây không tới đúng tay/cổng; hai người trong màn hình còn rất nhỏ. Source dịch cả nhóm vai p07-mascot-far-arm từ translate(25,72) sang x:-20,y:-25 làm đổi điểm gốc thay vì giữ vai cố định.
Đề xuất: giữ ý cuộc gọi, bỏ thao tác cắm cáp. Laptop/screen lớn, hình người chiếm khoảng 65–75% vùng màn hình, một người vẫy tay rõ. Mascot chạm nút cuộc gọi bằng tay cùng rig → cuộc gọi kết nối → vẫy đáp lại. Giữ vai cố định, cổ tay khớp điểm chạm. Hạ chân bàn/chi tiết phụ khỏi vai trò chủ đạo. Đây là hình ảnh liên hệ gia đình, không chứng minh mua nhà tự cấp quyền pháp lý.

### Voice 08 → S08 / 34.35–39.80s

Voice: “thuận tiện hơn cho những chuyến thăm con, cho các kế hoạch học tập, sinh sống, hoặc làm việc trong tương lai.”
Hiện thấy: người phụ là bust nhỏ cạnh vali quá lớn; không có cơ thể/bước đi thuyết phục. Mascot nhảy lên hàng icon; ba icon chỉ co giãn nhẹ. Source tween mascot y:-6 trên gốc translate(450,800) giải thích cú nhảy lớn.
Đề xuất: dựng lại người phụ là phụ huynh toàn thân phong cách gọn cùng nét với mascot; cao tương đương hoặc nhỉnh hơn mascot, vali tới hông. Tay giữ đúng tay kéo, bánh chạy cùng sàn. 0–1.6s hai người gặp nhau, chào hoặc ôm; sau đó chuyển trọng tâm lần lượt tới ba vignette lớn không hộp: bàn học / góc sinh hoạt / bàn làm việc. Mỗi vignette thay nhau chiếm vùng hình chính đúng từ tương ứng, không để cả ba icon nhỏ treo mãi phía trên. Chỉ một hành động đơn giản ở mỗi vignette: mở sách / đặt đồ cá nhân / thao tác laptop. Không nhảy mascot lên hàng icon; không làm người dùng hiểu việc làm được bảo đảm.

### Voice 11 → S10 / 47.25–53.41s

Voice: “Chỉ với khoảng 3,8 tỷ đồng, chương trình Thẻ Xanh Malta mang đến cơ hội định cư cho 4 thế hệ.”
Hiện thấy: một khối giấy rỗng lớn, những hình người tí hon khó phân biệt bốn thế hệ. Giá 3,8 tỷ không được thể hiện trong hình hiện tại.
Đề xuất: bỏ khối album/cube. Đầu câu hiện bare metric “3,8 TỶ” trên nền sáng theo xác nhận nội dung trước của người dùng; tới “4 thế hệ”, chuyển trọng tâm sang một nhóm gia đình bốn thế hệ có dấu hiệu tuổi rõ, đứng/ngồi trên cùng mặt sàn. Người lớn tuổi ngồi ghế, trẻ cạnh cha mẹ; nhóm người là hình chủ đạo, không phải 4 ô thông tin. Giữ câu điều kiện hiện có theo brief và rà nguồn pháp lý riêng trước khi đưa claim mới; không thêm lời khẳng định chi phí trọn gói hay ai chắc chắn đủ điều kiện.

### Voice 12–13 → S11 / 53.41–60.22s

Voice: “Đây không chỉ là quyết định đầu tư vào một bất động sản, mà còn là quyết định đầu tư vào sự chuẩn bị cho tương lai của con cái”.
Hiện thấy: chìa khóa, quyển vở bay và ba lô như hộp trên bàn, mascot nhỏ bên dưới. Không thấy động tác tay cất vở. Mở/che miệng túi không đọc rõ; vật thể đang di chuyển độc lập.
Đề xuất: giữ ý chuẩn bị cho con nhưng dựng cận một hành động duy nhất. Chìa khóa nằm sẵn bên trái mặt bàn; người phụ huynh và mascot ở bên phải. Khi tới “chuẩn bị”, phụ huynh đưa quyển vở cho mascot; mascot nhận bằng hai tay, đặt vào túi đang mở. Bàn tay, sách, mép túi phải cùng contact và occlusion. Kết có ba lô đã sẵn sàng, người thân đứng cạnh. Không thêm đồ bay hoặc nhiều nấc biến đổi. Không cần lắc cả nhân vật để giả cảm xúc.

### Voice 14 → S12 / 60.22–63.75s

Voice: “và những cơ hội mà các thế hệ sau có thể nắm bắt tại Châu Âu.”
Hiện thấy: thanh treo, dụng cụ giống móc/tất, một khối tím; nhân vật với tay nhưng vật và tay không gặp nhau. Không xác định được đang học hay làm gì.
Đề xuất thay ý tưởng: cận một buổi thực hành, mascot ngồi ở bàn, trước mặt là mô hình nhỏ có thể nhận ra (ví dụ chong chóng trong bài thực hành) và nút khởi động. Mascot bấm, cánh mô hình quay; ánh nhìn chuyển theo kết quả. Một hoạt động học hỏi/thực hành có đầu và kết, không phải chụp lấy dụng cụ trừu tượng. 3.53s chỉ đủ một thao tác. Đây là tình huống tượng trưng về cơ hội phát triển, không là cam kết được nhận học/việc; không thêm tên trường/chương trình chưa có nguồn.

### Voice 15 → S13 / 63.75–68.30s

Voice: “Khi con đã bước ra thế giới, tài sản của gia đình cũng có thể bước ra thế giới.”
Hiện thấy: quả cầu có lưới, hai đường cong và chấm; không có hình con/ngôi nhà gắn với hai quỹ đạo. Người xem không thể suy ra đường nào là hành trình của con, đường nào là tài sản. Chấm chuyển động theo đường thẳng dù path cong.
Đề xuất: thay địa cầu bằng bản đồ giản lược có nguồn và hai điểm đến cụ thể theo nội dung. Nhịp đầu: ký hiệu sinh viên có ba lô đi theo đường hành trình tới Châu Âu. Nhịp “tài sản… cũng có thể”: lộ thêm marker nhà tại Malta, trong khi tài sản ở điểm gốc vẫn giữ nguyên. Không cho nhà/tiền bay qua biên giới. Chỉ hai nhãn ngắn “CON” / “TÀI SẢN” nếu thật sự cần phân biệt; icon phải có hình đại diện. Khác S05: S05 định vị một nơi rồi xem nhà, S13 cho thấy hai kế hoạch có thể mở rộng song song. Nếu thử khung thấy lặp S05 hoặc quá dày, ưu tiên hai shot trực tiếp: sinh viên ở môi trường học tập → hai địa điểm tài sản được đối chiếu, thay vì cố giữ một map.

### Voice 16–17 → S14 / 68.30–75.16s

Voice: “Bởi đôi khi, điều giá trị nhất không phải là sở hữu thêm một căn nhà, mà là sở hữu thêm một lựa chọn cho tương lai.”
Hiện thấy: ngôi nhà cạnh tờ giấy hình nhánh cây; nhánh đổi màu, mắt/mồm nhúc nhích. Chìa khóa tween y:845 còn bị đặt xuống ngoài vùng hình dự kiến; không có hành động mở thêm lựa chọn đọc được. Ảnh trông gần tĩnh do phần có nghĩa hầu như không đổi.
Đề xuất thay kết: một ngã rẽ thực trong không gian minh họa, nhánh cũ vẫn mở. Đầu câu cận biểu tượng nhà/chìa khóa, mascot giữ yên. Tới “mà là”, camera nới khung để thấy cả gia đình và một cổng nhỏ ở nhánh thứ hai; mascot trực tiếp đẩy cổng, lộ một lối đi thứ hai vốn có ở sau. Đích là hai tình huống tương lai có thể nhận ra: thăm/gần con và kế hoạch dài hạn, không thêm quyền lợi cụ thể. Kết giữ cả hai lối đang mở, gia đình đứng ở điểm lựa chọn, không bắt buộc đi qua lối mới. Text chỉ “THÊM MỘT LỰA CHỌN”. Không morph nhà thành cửa hay dùng nhánh cây đổi màu làm toàn bộ cao trào. Cần duyệt khung để tránh liên tưởng mua nhà tự động mở quyền cư trú; đây là ẩn dụ lựa chọn, không sơ đồ thủ tục.

## Phân loại công việc

- Giữ hai pilot S01/S09 đã duyệt, voice và toàn bộ timeline.
- Dựng lại asset/rig và staging S06/S08; giữ ý cuộc gọi nhưng sửa bố cục S07; S11 giữ quan hệ chuẩn bị nhưng làm lại hành động cận.
- Viết lại hình chủ đạo S10/S12/S13/S14 theo đề xuất, chờ người dùng chọn hướng trước khi sản xuất.
- Mẫu rig bắt buộc: root đặt vị trí → wrapper chuyển động tương đối → body/shoulder cố định → forearm/hand nối cùng chain; đừng animate x/y đích nhỏ trên nhóm đang translate lớn. Ghim vai vào thân, prop bám tay khi cầm, khi nhả chuyển sang tọa độ cảnh. Không thay engine để che lỗi vector.
- Kiểm pose tiếp xúc ở 10–12fps hoặc frame quanh event, không chỉ open/mid/end. Sau đó xem playback có voice và bản 360×640. Kiểm cả master sau ghép.

Thứ tự sửa đề nghị: 1) rig mẫu S07 và phụ huynh S08; 2) duyệt keyframe/hành động S06/S08/S11; 3) duyệt lại ý tưởng S10/S12/S13/S14; 4) dựng clip thử từng nhóm; 5) mới ghép master. Không tiếp tục render cả lô từ cùng rig đang hỏng.

## Đối chiếu báo cáo Antigravity

INSPECTION_REPORT.md tự ghi đã kiểm định nghệ thuật/sẵn sàng nghiệm thu, nhưng frame xuất có lỗi lộ rõ. Không thể dùng checklist đó làm bằng chứng đã đạt chất lượng. Báo cáo còn mô tả S09 như cơ chế chi phí MPRP dù source/voice đã duyệt là đa dạng hóa danh mục; đây là lỗi diễn giải trong báo cáo, không phải bằng chứng MP4 S09 đã đổi (hash vẫn khớp). Tương tự S05 mới được duyệt storyboard, không thể nâng thành pilot đã được người dùng duyệt chỉ vì có tên trong mục approved_pilots_used.

Chưa sửa source, chưa đổi trạng thái đã duyệt, chưa tạo asset/frame thiết kế hoặc render mới. Các contact sheet là ảnh trích phục vụ review, không phải visual đề xuất.
