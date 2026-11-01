# Báo Cáo Phân Tích Audio & Transcript — Dự Án `[VIDEO-33]`

## 1. Thông Tin Kỹ Thuật Audio Nguồn

- **Tên Dự Án**: `[VIDEO-33]`
- **Audio Gốc**: `input_voice/Generated Audio October 26, 2026 - 6_06PM.wav`
- **Bản Sao Bàn Giao**: `videos/VIDEO-33/inputs/source_audio.wav`
- **SHA-256 (File WAV)**: `cbd5a88b99c252d09ea86493377951aed1267186a5cb9ff11afe00947133e941`
- **SHA-256 (Raw PCM)**: `80e095d3d1f20219de642dec538560a51aadf97fec1493f59524da228b5e0e00`
- **Sample Rate**: 24000 Hz
- **Channels**: 1 (Mono)
- **Bit Depth**: 16-bit PCM
- **Tổng Số Sample (Frames)**: 1,803,840 samples
- **Tổng Thời Lượng**: 75.160 giây (75.16s)
- **Tổng Số Đoạn Ý (Segments)**: 17 đoạn
- **File Kịch Bản Đối Chiếu Gốc**: `scratch/video 33.txt` (Dung lượng thực tế: 0 bytes — file rỗng)

## 2. Kết Quả Kiểm Tra Tính Toàn Vẹn & Khớp Nối (Contiguity & PCM Reassembly)

- **Contiguity Check**: `PASSED` — Toàn bộ `start_sample[i]` khớp chính xác 100% với `end_sample[i-1]`, không có bất kỳ khoảng trống (gap) hay khoảng trùng (overlap) nào.
- **Độ Phủ Mẫu (Coverage)**: 0 đến 1,803,840 samples (Đạt 100% toàn vẹn).
- **Điểm Cắt (Zero-Crossing)**: Mọi điểm cắt đều rơi vào vùng khoảng lặng (silence valley) tại biên độ amp = 0, đảm bảo không gây hiện tượng click/pop âm thanh khi ghép.
- **Ghép Lại PCM (Reconstruction)**: `PASSED` — Nối tuần tự 17 lát audio PCM thu được mảng byte trùng khớp bit-for-bit với file gốc.
  - `Original PCM SHA-256`: `80e095d3d1f20219de642dec538560a51aadf97fec1493f59524da228b5e0e00`
  - `Reconstructed PCM SHA-256`: `80e095d3d1f20219de642dec538560a51aadf97fec1493f59524da228b5e0e00`

## 3. Bảng Phân Tách Đoạn Ý, Timing & Đối Chiếu Phiên Âm

| Seg | Segment ID | Timing (s) | Duration | Samples (Start -> End) | Audio Slice | Corrected Text (Chuẩn hoá) | Raw ASR Text (Gốc nhận dạng) | Uncertainties & Notes |
|:---:|:---:|:---:|:---:|:---:|:---:|---|---|---|
| 01 | `seg_01` | 0.000 - 6.019 | 6.019s | 0 -> 144466 | `audio_slices/seg_01.wav` | **Khi con du học Châu Âu, nhiều gia đình không chỉ đầu tư cho việc học, mà còn đầu tư cho một điểm tựa lâu dài.** | *Khi con du học Châu Âu, nhiều gia đình không chỉ đầu tư cho việc học, mà còn đầu tư cho một điểm tự lâu dài.* | điểm tự -> điểm tựa: Giọng nói ngắt âm/lướt âm cuối; chuẩn văn phạm và ngữ nghĩa đầu tư là 'điểm tựa lâu dài'. |
| 02 | `seg_02` | 6.019 - 9.875 | 3.856s | 144466 -> 236998 | `audio_slices/seg_02.wav` | **Trước nhiều phụ huynh sẵn sàng chi hàng tỷ đồng cho hành trình du học của con,** | *Trước nhiều phụ hình sẵn sàng chi hàng tỷ đồng cho hành trình du học của con,* | phụ hình -> phụ huynh: ASR nhận nhầm thanh âm; giọng đọc phát âm 'phụ huynh'.<br>Trước nhiều phụ huynh: Giọng phát âm rõ âm 'Trước'. Có thể câu gốc dự kiến là 'Trước việc nhiều phụ huynh...' hoặc 'Rất nhiều phụ huynh...'. Do file scratch/video 33.txt có dung lượng 0 bytes, giữ nguyên chữ 'Trước' theo đúng âm thanh audio gốc và đánh dấu để Đạo diễn thẩm định. |
| 03 | `seg_03` | 9.875 - 14.121 | 4.246s | 236998 -> 338898 | `audio_slices/seg_03.wav` | **nhưng nếu con có kế hoạch học tập và phát triển sự nghiệp tại Châu Âu trong nhiều năm,** | *nhưng nếu con có kế hoạch học tập và phát triển sự nghiệp tại Châu Âu trong nhiều năm.* | Dấu câu: Thay dấu chấm bằng dấu phẩy nối vế điều kiện với câu hỏi ở đoạn kế tiếp. |
| 04 | `seg_04` | 14.121 - 18.151 | 4.030s | 338898 -> 435629 | `audio_slices/seg_04.wav` | **Liệu toàn bộ tài sản của gia đình có nên chỉ tập trung ở Việt Nam?** | *Liệu toàn bộ tài sản của gia đình có nên chỉ tập trung ở Việt Nam.* | Dấu câu: ASR nhận dạng dấu chấm; đây là câu hỏi tu từ đặt vấn đề, chuẩn hoá thành dấu chấm hỏi '?'. |
| 05 | `seg_05` | 18.151 - 23.858 | 5.706s | 435629 -> 572581 | `audio_slices/seg_05.wav` | **Đó là lý do ngày càng nhiều gia đình lựa chọn đa dạng hóa tài sản bằng bất động sản tại Malta.** | *Đó là lý do ngày càng nhiều gia đình lựa chọn đa dạng hóa tài sản bằng bất đồng sản tại Manta.* | bất đồng sản -> bất động sản: Lỗi nhận dạng âm vị của ASR.<br>Manta -> Malta: ASR nhận dạng nhầm tên quốc đảo Nam Âu 'Malta' thành 'Manta'. |
| 06 | `seg_06` | 23.858 - 29.654 | 5.797s | 572581 -> 711699 | `audio_slices/seg_06.wav` | **Không chỉ là sở hữu một tài sản ở Châu Âu, đây còn là cách xây dựng một nền tảng lâu dài cho cả gia đình.** | *Không chỉ là sở hữu một tài sản ở Châu Âu, đây còn là cách xây dựng một nền tảng lâu dài cho cả gia đình.* | — |
| 07 | `seg_07` | 29.654 - 34.323 | 4.669s | 711699 -> 823751 | `audio_slices/seg_07.wav` | **Khi có một tài sản tại Malta, gia đình có thêm một điểm kết nối với Châu Âu,** | *Khi có một tài sản tại Manta, gia đình có thêm một điểm kết nối với Châu Âu,* | Manta -> Malta: ASR nhận nhầm tên riêng quốc gia Malta. |
| 08 | `seg_08` | 34.323 - 39.800 | 5.477s | 823751 -> 955202 | `audio_slices/seg_08.wav` | **thuận tiện hơn cho những chuyến thăm con, cho các kế hoạch học tập, sinh sống, hoặc làm việc trong tương lai.** | *thuận tiện hơn cho những chuyến thăm con cho các kế hoạch học tập, sinh sống hoặc làm việc trong tương lai.* | Dấu câu: Thêm dấu phẩy phân tách các cụm liệt kê để tăng tính mạch lạc cho phụ đề/storyboard. |
| 09 | `seg_09` | 39.800 - 44.707 | 4.907s | 955202 -> 1072972 | `audio_slices/seg_09.wav` | **Đồng thời, việc sở hữu tài sản ở nhiều thị trường cũng giúp đa dạng hóa danh mục đầu tư** | *Đồng thời, diệt sở hữu tài sản ở nhiều thị trường cũng giúp đa dạng hóa dành một đầu tư* | diệt -> việc: ASR nhận sai âm đầu.<br>dành một -> danh mục: ASR nhận sai thuật ngữ tài chính 'danh mục đầu tư'. |
| 10 | `seg_10` | 44.707 - 47.251 | 2.544s | 1072972 -> 1134024 | `audio_slices/seg_10.wav` | **thay vì phụ thuộc hoàn toàn vào một quốc gia.** | *thay vì phụ thuộc hoàn toàn do một quốc gia.* | do -> vào: Giọng nói lướt âm, chuẩn hoá giới từ ngữ pháp tiếng Việt thành 'vào một quốc gia'. |
| 11 | `seg_11` | 47.251 - 53.408 | 6.157s | 1134024 -> 1281789 | `audio_slices/seg_11.wav` | **Chỉ với khoảng 3,8 tỷ đồng, chương trình Thẻ Xanh Malta mang đến cơ hội định cư cho 4 thế hệ.** | *Chị giới khoảng 3,8 tỷ đồng, chương trình Thế San Manta mang đến cơ hội định cư cho 4 thế hệ.* | Chị giới -> Chỉ với: ASR nhận nhầm thanh âm.<br>Thế San Manta -> Thẻ Xanh Malta: ASR nhận sai tên chương trình 'Thẻ Xanh Malta' (chính sách Thường trú nhân Malta - MPRP). |
| 12 | `seg_12` | 53.408 - 56.602 | 3.195s | 1281789 -> 1358457 | `audio_slices/seg_12.wav` | **Đây không chỉ là quyết định đầu tư vào một bất động sản,** | *Đây không chỉ là quyết định đầu tư vào một bước động sáng,* | bước động sáng -> bất động sản: ASR nhận sai âm vị. |
| 13 | `seg_13` | 56.602 - 60.220 | 3.617s | 1358457 -> 1445273 | `audio_slices/seg_13.wav` | **mà còn là quyết định đầu tư vào sự chuẩn bị cho tương lai của con cái** | *mà còn là quyết định đầu tư vào sự chuẩn bị cho tương lai của con gái* | con gái -> con cái: Giọng đọc phát âm âm đuôi hơi giống 'con gái'. Tuy nhiên trong ngữ cảnh phân tích gia đình và con du học nói chung, từ chuẩn là 'con cái'. Nếu kịch bản gốc là câu chuyện riêng về con gái, Đạo diễn có thể giữ 'con gái'. Tạm ghi chú để Đạo diễn thẩm duyệt. |
| 14 | `seg_14` | 60.220 - 63.751 | 3.531s | 1445273 -> 1530028 | `audio_slices/seg_14.wav` | **và những cơ hội mà các thế hệ sau có thể nắm bắt tại Châu Âu.** | *và những cơ hội mà các thế hệ sau có thể nắm bắt tại Châu Âu.* | — |
| 15 | `seg_15` | 63.751 - 68.304 | 4.553s | 1530028 -> 1639305 | `audio_slices/seg_15.wav` | **Khi con đã bước ra thế giới, tài sản của gia đình cũng có thể bước ra thế giới.** | *Khi con đã bước ra thế giới, tài sản của gia đình cũng có thể bước ra thế giới.* | — |
| 16 | `seg_16` | 68.304 - 72.350 | 4.046s | 1639305 -> 1736406 | `audio_slices/seg_16.wav` | **Bởi đôi khi, điều giá trị nhất không phải là sở hữu thêm một căn nhà,** | *Bởi đôi khi, điều giá chỉ nhất không phải là sở hữu thêm một căn nhà,* | giá chỉ -> giá trị: ASR nhận sai phụ âm cuối; giọng đọc chuẩn 'giá trị'. |
| 17 | `seg_17` | 72.350 - 75.160 | 2.810s | 1736406 -> 1803840 | `audio_slices/seg_17.wav` | **mà là sở hữu thêm một lựa chọn cho tương lai.** | *mà là sở hữu thêm một lựa chọn cho tương lai.* | — |

## 4. Chi Tiết Các Điểm Không Chắc Chắn (Uncertainties)

Do file `scratch/video 33.txt` cung cấp là 0 bytes, các điểm dưới đây được phát hiện qua đối chiếu ngữ âm ASR và ngữ cảnh thực tế:

1. **Seg 01 (`0.000s -> 6.019s`)**: ASR nhận `điểm tự lâu dài`. Audio lướt âm cuối; theo ngữ nghĩa tiếng Việt chuẩn về đầu tư, sửa thành `điểm tựa lâu dài`.
2. **Seg 02 (`6.019s -> 9.875s`)**:
   - ASR nhận `phụ hình` -> sửa thành `phụ huynh` (phát âm rõ âm phụ huynh).
   - Giọng đọc phát âm rõ từ mở đầu là `Trước nhiều phụ huynh...`. Cần Đạo diễn đối chiếu xem kịch bản gốc ban đầu là `Trước nhiều phụ huynh...`, `Trước việc nhiều phụ huynh...` hay `Rất nhiều phụ huynh...`. Tạm thời giữ nguyên âm gốc `Trước nhiều phụ huynh`.
3. **Seg 05 (`18.151s -> 23.858s`)** & **Seg 07 (`29.654s -> 34.323s`)**: ASR nhận `Manta` -> sửa thành `Malta` (tên quốc gia Malta); `bất đồng sản` -> sửa thành `bất động sản`.
4. **Seg 09 (`39.800s -> 44.707s`)**: ASR nhận `diệt sở hữu... dành một đầu tư` -> sửa thành `việc sở hữu... danh mục đầu tư` (thuật ngữ tài chính).
5. **Seg 10 (`44.707s -> 47.251s`)**: ASR nhận `do một quốc gia` -> sửa thành `vào một quốc gia` (chuẩn giới từ tiếng Việt).
6. **Seg 11 (`47.251s -> 53.408s`)**: ASR nhận `Chị giới... Thế San Manta` -> sửa thành `Chỉ với... Thẻ Xanh Malta` (tên gọi tiếng Việt của chương trình Thường trú nhân MPRP).
7. **Seg 12 (`53.408s -> 56.602s`)**: ASR nhận `bước động sáng` -> sửa thành `bất động sản`.
8. **Seg 13 (`56.602s -> 60.220s`)**: ASR nhận `của con gái`. Âm thanh nghe như `con gái` hoặc `con cái`. Ngữ cảnh chung là `con cái`, nhưng nếu kịch bản nhắm vào đối tượng cụ thể có con gái thì có thể là `con gái`. Đạo diễn cần xác nhận.
9. **Seg 16 (`68.304s -> 72.350s`)**: ASR nhận `điều giá chỉ nhất` -> sửa thành `điều giá trị nhất`.

## 5. Danh Sách Tên Riêng, Số Liệu & Phát Biểu Cần Xác Minh (Fact-Check Table)

| Segment | Loại Thông Tin | Nội Dung Trong Audio | Thực Tế / Tiêu Chuẩn Thẩm Định | Mức Độ Ưu Tiên | Ghi Chú Đạo Diễn & Pháp Lý |
|:---:|:---:|---|---|:---:|---|
| Seg 01 | **Khái niệm** | `Du học Châu Âu kết hợp đầu tư tích luỹ lâu dài` | Mô hình xu hướng gia đình đầu tư định cư cho con du học | `Bình thường` | Dùng làm hook mở bài định vị vấn đề. |
| Seg 02 | **Số liệu** | `Hàng tỷ đồng cho hành trình du học` | Chi phí du học thực tế tại Châu Âu dao động 400tr - 2 tỷ/năm | `Bình thường` | Con số hợp lý với thực tế chi phí các nước Tây/Bắc Âu. |
| Seg 05 | **Địa danh** | `Bất động sản tại Malta` | Cộng hòa Malta (quốc đảo Nam Âu, thành viên EU & Schengen) | `Quan trọng` | Đảm bảo hình ảnh/bản đồ hiển thị chính xác cờ/quốc đảo Malta. |
| Seg 08 | **Quyền lợi** | `Thăm con, học tập, sinh sống, làm việc` | Quyền lợi của Thường trú nhân Malta (MPRP) | `Quan trọng` | Người giữ thẻ cư trú Malta được tự do đi lại khối Schengen tối đa 90 ngày/180 ngày; được sinh sống lâu dài tại Malta; muốn đi làm cần giấy phép lao động. |
| Seg 09 | **Thuật ngữ** | `Đa dạng hóa danh mục đầu tư` | Wealth Portfolio Diversification | `Bình thường` | Trực quan hóa đồ họa phân bổ tài sản. |
| Seg 11 | **Số liệu trọng yếu** | `Khoảng 3,8 tỷ đồng` | Chi phí tham gia chương trình Thẻ Xanh Malta (MPRP) diện thuê BĐS | `CỰC KỲ QUAN TRỌNG` | Cần xác minh bảng tính pháp lý của đối tác/đơn vị tư vấn: MPRP diện thuê yêu cầu thuê tối thiểu 10.000€/năm (Gozo/South) hoặc 12.000€/năm + phí CP 98.000€ + từ thiện 2.000€ + phí thẩm định -> Tổng xấp xỉ 140.000 - 150.000€ (~3,8 - 4,0 tỷ VND). Cần kiểm tra xem 3,8 tỷ đã gồm toàn bộ phí thẩm định/hành chính chưa. |
| Seg 11 | **Chính sách trọng yếu** | `Chương trình Thẻ Xanh Malta mang đến cơ hội định cư cho 4 thế hệ` | Quy định chương trình MPRP (Malta Permanent Residence Programme) | `CỰC KỲ QUAN TRỌNG` | Luật MPRP cho phép 4 thế hệ: (1) Đương đơn & vợ/chồng; (2) Con cái phụ thuộc; (3) Cha mẹ hai bên; (4) Ông bà hai bên. Điều kiện: thế hệ cha mẹ/ông bà và con trưởng thành phải chứng minh phụ thuộc tài chính vào đương đơn. |
| Seg 13 | **Đối tượng** | `Tương lai của con cái (hoặc con gái)` | Nhóm đối tượng khách hàng mục tiêu | `Quan trọng` | Đạo diễn chốt visual nhân vật là con cái chung hay hình tượng một người con gái cụ thể. |
| Seg 15-17 | **Thông điệp** | `Tài sản bước ra thế giới; Sở hữu thêm một lựa chọn cho tương lai` | Key takeaway & punchline kết thúc video | `Bình thường` | Visual kết thúc ấn tượng, truyền cảm hứng. |
