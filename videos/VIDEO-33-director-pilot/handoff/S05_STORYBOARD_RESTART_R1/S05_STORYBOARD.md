# S05 — storyboard viết lại từ đầu / R1

**Trạng thái: storyboard R1 đã được người dùng duyệt (“oke duyệt”). Sẵn sàng bàn giao Antigravity dựng pilot S05; chưa có frame/pilot mới được duyệt.**

Album S05 v5 không được duyệt theo yêu cầu mới nhất. Toàn bộ cơ chế album, giấy lật, nhà giấy và nhà biến hình đã bị loại khỏi hướng hiện tại. Các bản cũ chỉ còn là lịch sử.

## Ý tưởng: Chọn địa điểm, thấy tài sản thật

Mascot đặt một ghim lên Malta trên bản đồ. Khi voice tới “bất động sản”, cắt thẳng sang ảnh lớn mặt tiền một căn nhà thật ở Malta. Đây là hai shot được nối bằng dựng phim: người xem đi từ địa điểm tới loại tài sản cụ thể. Không có công trình mọc lên từ bản đồ và không có cảnh nhân vật tương tác với vật thể bên trong ảnh.

Lời thoại nói về đa dạng hóa; cảnh này làm rõ một địa điểm và một loại tài sản đang được cân nhắc. Không dùng nhiều gia đình hay biểu đồ tăng để biến lời “ngày càng nhiều” thành bằng chứng thống kê. S09 đã kể cơ chế phân bổ nên S05 không lặp lại.

## Voice giữ nguyên

Global **18.151208333–23.857541667s**, **[435629, 572581)** tại 24kHz; **136952 samples / 5.706333333s**. Nguồn `inputs/audio/seg_05.wav`.

Raw transcript: “Đó là lý do ngày càng nhiều gia đình lựa chọn đa dạng hóa tài sản bằng bất đồng sản tại Manta.”

Corrected text, chỉ để đọc hiểu: “Đó là lý do ngày càng nhiều gia đình lựa chọn đa dạng hóa tài sản bằng bất động sản tại Malta.” Không thu lại, thay chữ trong voice, kéo giãn hoặc cắt mất khoảng nghỉ.

## Kịch bản theo nhịp

| Thời gian nội cảnh | Nhịp lời | Hình ảnh / hành động |
|---|---|---|
| 0–0.49s | Đầu lát voice | Bản đồ nam Sicily–Malta đã trong khung; mascot cầm ghim ở dưới trái, nhìn điểm định vị. |
| 0.49–2.49s | “Đó là lý do… ngày càng nhiều gia đình” | Mascot nghiêng người, đưa ghim tới Malta. Map đứng yên, tay đi một quãng ngắn tự nhiên. |
| 2.49–3.55s | “lựa chọn… đa dạng hóa tài…” | Ghim chạm đúng điểm rồi tay nhả, thu về. Nhãn **MALTA** hiện một lần sau tiếp xúc. |
| 3.55–4.35s | “…sản bằng…” | Giữ kết quả: ghim đứng yên, mascot nhìn điểm chọn. Không thêm icon hay nhãn. |
| 4.35–5.706s | “bất động sản tại Malta” | Cắt thẳng sang ảnh thật mặt tiền nhà ở. Thấy rõ cửa và ban công; nhãn MALTA giữ nguyên vị trí. Giữ hình đến hết voice. |

Mốc nội cảnh dựa trên word timing ASR, là cue đề xuất chưa xác minh độc lập từng âm. Khi dựng, đối chiếu WAV để hard cut trúng từ “bất”; không đổi ranh giới sample. Shot ảnh chỉ khoảng 1.36s nên đứng yên, không thêm chuỗi hiệu ứng.

## Bố cục và hình cuối

Canvas 720×1280. Nền kem, mặt đất trên bản đồ đào nhạt, biển xanh rất nhạt. Mascot cam bo góc, mũ tím, ba lô xanh; nét mảnh trung tính. Nhãn MALTA ở y=160–235, Segoe UI Black 56px.

Shot bản đồ: vùng hình x≈40–680, y≈300–1030. Crop bản đồ để Malta nằm gần tầm tay, không dịch đảo khỏi vị trí thật. Mascot ở dưới trái; cánh tay không kéo dài, không cắm ghim xuyên người. Không dùng bản đồ làm card có viền.

Shot nhà: ảnh trải hết bề rộng x=0–720, y=290–1080. Khung lấy một mặt tiền nhà ở, ưu tiên đá sáng, cửa và ban công rõ ở kích thước điện thoại. Không viền, băng dính, album, khung ảnh hoặc mô hình kiến trúc. Không có mascot trong shot ảnh. Hình cuối chỉ còn mặt tiền nhà và nhãn MALTA phía trên. Footer y=1080–1280 sạch.

## Asset và tách lớp

- Bản đồ: cần lấy dữ liệu địa lý có nguồn rồi cách điệu, không tự phác đảo theo trí nhớ. Tách biển, đất, điểm neo Malta.
- Mascot: giữ nhận diện nguồn đã có; cần pose mới với thân, tay xa, tay gần, bàn tay cầm/nhả và mắt tách lớp. Không bê pose album v5.
- Ghim: một ghim đồ họa tách lớp, neo theo bản đồ; chuyển quyền giữ từ tay sang map tại tiếp xúc.
- Ảnh nhà ở: chưa chọn cuối cùng. `assets/townhouse.jpg` là ứng viên có sẵn, không bắt buộc dùng. Có thể tìm ảnh khác hợp crop hơn, có nguồn và giấy phép. Không dùng skyline nhà thờ làm bất động sản đang bán, không dựng giao dịch/sở hữu hay gán giá cho ảnh.
- Chữ MALTA: text native, font Segoe UI Black đã có. Không tạo chữ bằng AI.

Engine giữ **HF_ONLY**: rig vector + map + ảnh tĩnh thật + editorial cut. Không cần Flow. Asset mới chưa được tạo.

## Nối cảnh và kiểm tra logic

S04 đặt câu hỏi tập trung tài sản; cắt sang một địa điểm được cân nhắc ở S05, không để tiền tự bay khỏi Việt Nam. S06 tiếp tục ý gia đình bằng bàn chung; cắt theo ý, không kéo cửa nhà thành mặt bàn. S09 giữ riêng cơ chế phân bổ ba phần.

Trước khi render phải nhìn rõ chuỗi cầm → chạm → nhả. Ghim không nhảy trước bàn tay. Ảnh nhà không morph, skew, nở hoặc dính vào map. Không thể hiện chìa khóa trao tay, hợp đồng, lợi nhuận hay quyền cư trú tự phát sinh.

Kiểm sau khi được duyệt: opening, tiếp xúc ghim, trước/sau cut và final; bản 360×640, thumbnail, grayscale; playback với voice gốc. Hiện chưa thực hiện các kiểm này vì chưa sản xuất hình/motion.

## Phần giữ / phần linh hoạt

Giữ: ý định vị → nhà ở thật; hai shot tách rõ; voice/sample gốc; nhận diện mascot; một nhãn MALTA; footer; hành động tay hợp lý. Không kế thừa album hoặc cơ chế nhà giấy.

Linh hoạt: crop, pose, vị trí trong safe area, sắc độ, easing và mốc động tác nhỏ sau khi đối chiếu voice. Đổi ý tưởng trung tâm cần cập nhật storyboard, không thay bằng một cơ chế mới lúc thi công.

Nguồn kiểm địa lý: [Government of Malta — The Maltese Islands](https://govcms.gov.mt/en/About%20Malta/Pages/The%20Maltese%20Islands.aspx). Ảnh có sẵn là ứng viên: [Townhouse in Zejtun — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Townhouse_in_Zejtun.jpg); cần giữ attribution/giấy phép nếu sử dụng.
