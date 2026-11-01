# S06/S11 motion R1

720×1280 @30fps. S06: 174 frames / 5.800s, voice 5.796583333333s. S11: 205 frames / 6.833333s, voice 6.811833333333s. S06 giữ nguyên file WAV seg_06; S11 nối nguyên PCM seg_12 và seg_13. PCM đã đối chiếu lại với source gốc, không TTS/cắt khoảng nghỉ/time-stretch. MP4 encode AAC; sai khác mẫu AAC được kiểm bằng correlation trong qa-verification.json.

S06: ghế di chuyển với grip, actor travel dùng wrapper riêng, giữ transform placement. Sau khi nhả ghế, mascot đi ra trước ghế rồi vịn ghế/đặt chân lên thanh ngang để lên ngồi. Thanh ngang là chi tiết thi công thêm để có chỗ tựa chân. Keyframe chân có cùng topology để nội suy không giật. Bàn không đổi kích thước.

S11: vai cố định; tay nhận chạm trước khi phụ huynh nhả. Book wrapper và hand grip hạ cùng cue/ease; rear/front backpack tạo occlusion khi cất. Tay nghỉ ngoài mặt, không có ba lô trùng trên lưng. Các nguồn SVG thiết kế đã duyệt được giữ nguyên ở design-r1, chỉ xây runtime ở folder mới này.

Sau khi người dùng duyệt motion mới dùng hai clip trong bản ghép. Khi ghép, theo sample timeline và lưới frame chung, tránh cộng đuôi hold của các pilot độc lập gây lệch timeline. Không thay hai pilot S07/S08 hoặc S01/S09 đã duyệt bằng bản dựng lại.
