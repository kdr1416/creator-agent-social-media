# VIDEO-34 — Style Bible đề xuất

Trạng thái: **working preferred direction / chưa duyệt chính thức**. Đọc cùng storyboard.md. Đây là hệ thiết kế cho video-34, không phải instructions chung của Flow Kit.

## Những gì đã có và những gì còn là đề xuất

| Hạng mục | Trạng thái |
|---|---|
| Tỉ lệ 9:16; thương hiệu Esora Immi | Người dùng xác nhận |
| Avatar thật | `../assets/brand/esora-avatar-original.jpg`; JPEG 2046×2048, nền gradient xanh, chữ trắng và motif chìa khóa/vòng sao; nguồn và hash trong ledger |
| Màu/font chính thức của Esora | Chưa có brand guidelines; không suy ra mã màu/font chính thức từ JPEG |
| Warm Mediterranean Editorial Illustration | Hướng ưu tiên để phát triển storyboard; chưa phải approved style |
| 1080×1920, 30 FPS | Đề xuất production sau khi duyệt, chưa ghi vào project manifest |
| Gia đình, palette, type, texture, motion dưới đây | Đề xuất; chưa có asset nhân vật/font được cấp phép và kiểm tra |

## Ý đồ hình ảnh

Ấm, sáng, có đời sống; sự chỉn chu đến từ cấu trúc cảnh và acting nhỏ. Phố đá vôi, tán cây, cốc và bàn tay tạo liên hệ giữa nơi chốn với cảm giác quen thuộc. Không biến “premium” thành nền đen-vàng hay một loạt căn hộ xa hoa. Không cố mô phỏng một studio/video tham khảo chưa được người dùng cung cấp.

Kiến trúc Malta được gợi bằng vật liệu đá, cấu trúc cửa, ban công và bóng nắng; chi tiết đủ để có nơi chốn nhưng không đòi tái tạo một địa chỉ có thật. Tham chiếu hình thái: [Central Bank of Malta — stone balcony](https://www.centralbankmalta.org/1975-stone-balcony), mô tả truyền thống ban công Malta. Reference này không chứng minh mọi cảnh ven biển trong storyboard là một tuyến đường thực tế.

## Palette chức năng — tất cả là proposal

| Token | Hex đề xuất | Vai trò |
|---|---|---|
| ink | #243343 | Chi tiết tối, chữ ngắn, nét cần đọc |
| esora_related_navy | #252B68 | Điểm neo liên hệ cảm giác với logo; không gọi là màu brand chính thức |
| esora_related_blue | #2E64A5 | Chi tiết cửa/trang phục, không phủ xanh cả Malta |
| limestone | #E9D3AC | Kiến trúc/đá; cần phân mảng sáng tối để không phẳng |
| warm_ground | #F6F1E7 | Khoảng thở hoặc nền sáng |
| sea | #3F8D9B | Nước/điểm nhìn xa; biến thể theo chiều sâu |
| clay | #B96C51 | Mái/chậu/đồ vật ấm, chỉ khi có vật mang màu |

Không bắt mỗi scene đủ mọi màu; không dùng accent chạy quét theo quota. Trang phục nhân vật chính cần ít màu ổn định sau khi chốt casting. Màu da và cây cỏ phát triển riêng từ cảnh, không bị bó trong 7 token này. Contrast, cân bằng giá trị và đọc ở màn hình điện thoại **chưa được kiểm tra bằng render**.

## Typography và text

Đề xuất thử **Be Vietnam Pro**, medium/semibold cho nhãn ngắn; đây không phải font logo. Chưa xác minh file local, license hay render dấu tiếng Việt, chưa tải/cài. Nếu không có font phù hợp trong môi trường, lựa chọn thay thế phải được review bằng mẫu có dấu.

Phim chủ yếu kể bằng minh họa/voice. Text inventory ở từng scene là giới hạn dự kiến; không chuyển transcript thành tiêu đề dày đặc. Không hiện mức giá, số thế hệ hoặc quyền lợi chưa được kiểm chứng. Không subtitle mặc định, không giữ một footer cố định. Với canvas đề xuất 1080×1920, thử headline khoảng 64–80px và nhãn 40–48px trước; đây là dải thử nghiệm theo nội dung, không phải tiêu chuẩn đã đo. Preview 360×640 quyết định giữ/rút chữ. Logo raster được hiển thị trực tiếp, không typeset lại.

## Shapes, linework, chiều sâu và ánh sáng

- Mặt phẳng kiến trúc có cấu trúc: bậu cửa, lan can, nền đất và đường viền bờ biển làm đường dẫn mắt. Nhân vật có silhouette phân biệt được khi thu nhỏ. Không gom mọi khối thành hình chữ nhật bo góc giống UI.
- Contour chỉ dùng ở chỗ cần tách tay/props hoặc silhouette. Cỡ nét biến theo kích thước đối tượng và khoảng cách; không một stroke đồng đều cho mọi thứ, không bắt buộc mọi vật có viền.
- Chiều sâu từ chồng lớp, tỉ lệ xa/gần, bóng tiếp xúc và phối cảnh ổn định. Không yêu cầu số layer cố định; không giả camera bay 3D qua các mặt phẳng 2D bị méo.
- Ánh sáng chính ấm từ trên-trái trong chuỗi Malta, giữ phía bóng nhất quán. Bóng mềm tại chân/ghế/cốc để người và vật có trọng lượng; không glow mọi asset. Mặt thứ cấp sáng hơn các khối chính, tránh nhiều mảng navy hợp thành một khối tối.
- Texture giấy/grain mịn là tùy chọn sau pilot, nằm trong vật liệu hoặc nền, không gây flicker. Chưa có texture được tạo hoặc mua; nếu dùng phải có provenance và bản local. Không dùng noise động chỉ để lấp cảnh tĩnh.

## Hệ nhân vật đề xuất

Một gia đình Việt có nhận diện ổn định qua trang phục/tóc/tỉ lệ: hai phụ huynh 30–40 tuổi và một trẻ 7–9 tuổi. Đây là casting giả định để review, không chân dung khách hàng. Người dùng có thể đổi cấu trúc gia đình trước khi xây asset. Không bắt nhân vật xuất hiện theo phần trăm thời lượng.

Đầu/hướng mắt, thân, tay gần/xa chỉ tách khi hành động cần. Không xây rig đầy đủ cho mọi cư dân nền. S08 cần vai–khuỷu–bàn tay–ghế và laptop có điểm tựa đúng; S03 ưu tiên dáng đi/chạy dễ đọc ở kích thước nhỏ. Chỉ một hành động chủ đạo tại một thời điểm. Cử chỉ có mục đích và điểm tiếp xúc, không nhân vật đứng vẫy/nhún ở góc khung để trang trí. Phụ huynh và trẻ không đổi vóc dáng/quần áo khi đổi cảnh, trừ thay đổi có ghi chú.

## Motion language cho project

Ba nguyên tắc chọn dùng: **quan hệ nhân quả**, **thứ bậc chú ý**, **liên tục không gian/chuyển động**. Chúng phục vụ ý cảnh, không buộc mọi cảnh cùng preset.

| Loại hành động | Cách chuyển động dự kiến |
|---|---|
| Đi/chạy | Quãng đường và nhịp chân liên hệ; travel tương đối đều, bàn chân không trượt. Chu kỳ chỉ khi cần; không dùng idle loop đồng loạt. |
| Đóng laptop / đưa tay | Pivot vật lý rõ, dừng có trọng lượng và tiếp xúc; không overshoot mặc định. |
| Chuyển chú ý / nhìn | Mắt và đầu dẫn nhẹ trước thân nếu hợp acting; phải đọc được thay đổi ý định. |
| Dịch khung cảnh | Camera phục vụ không gian, không zoom vào từng danh từ. S03 tối đa hai lần tái định khung chính là mục tiêu dựng thử. |
| Cảnh lắng S04/S10/S15 | Cho phép ít chuyển động, bố cục và acting mang ý nghĩa; không thêm hạt bay để chứng minh có animation. |

Khi được yêu cầu triển khai: timeline GSAP paused, scene-local và seek-safe theo hợp đồng HyperFrames; không dựa vào thời gian thực hoặc state từ scene trước. Chọn easing/duration theo từng tác động sau khi xem pilot. Chưa có animation code hoặc motion preset được triển khai ở phase này.

## Bố cục dọc và logo

Bố cục thay đổi theo khoảng cách kể chuyện: panorama dọc có chiều sâu, góc cao, over-shoulder, medium acting, cận tay. Một focal action rõ; khoảng trống có lý do của ánh sáng/đường nhìn, không mặc định để nửa dưới rỗng. Vùng tránh UI nền tảng sẽ kiểm tra bằng overlay thực tế khi dựng, không tự khóa safe padding chung.

Logo dùng nguyên JPEG theo tỉ lệ **2046/2048**, contain đầy đủ nền gradient/chữ/chìa khóa/sao. Không crop vòng sao, không tách nền, vẽ lại, recolor hoặc kéo giãn để giả logo vector. S17 đề xuất logo khoảng 30–34% bề rộng khung, tách rõ khỏi gương mặt và tay; phải test kích thước avatar có đọc được hay không. Không thêm một endcard dài ra ngoài 93,04s. Khả năng cần file vector/transparent chính chủ là quyết định sau review, không tự tạo thay thế.

## Điều kiện review style

Style Bible này chưa chứng minh chất lượng visual. Trước khi build cần phản hồi về độ ấm/trưởng thành của minh họa, casting, palette/font và cách xuất hiện Esora. Pilot sau đó kiểm tra silhouette, da/tay/gaze, light continuity, đặc trưng Malta, logo gốc, text tiếng Việt nếu dùng và độ đọc ở 360×640. Không chuyển trạng thái approved từ việc tài liệu đầy đủ.
