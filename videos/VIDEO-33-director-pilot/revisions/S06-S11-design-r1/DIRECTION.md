# S06/S11 — frame và chuỗi hành động đề xuất R1

Trạng thái: chờ duyệt frame. Không có motion mới, không đổi voice/master, không thay hai pilot S07/S08 đã duyệt. Số cảnh theo 14 cảnh dựng: S06 = voice 06; S11 = voice 12–13. VOICE_REFERENCE.json giữ nguyên raw/corrected text và sample bounds từ storyboard hiện tại.

## S06 — Có chỗ cho cả gia đình

Ý cần đọc: từ một tài sản riêng lẻ tới sự chuẩn bị có cả gia đình tham gia. Bỏ toàn bộ cơ chế bàn mọc/mở lá bàn. Bàn giữ nguyên kích thước và cấu trúc suốt cảnh.

Bố cục: nền lilac; cha/mẹ ngồi ở phía xa bàn, thân gắn với ghế và bị mặt bàn che đúng lớp. Một ghế trống phía gần, mascot ở cạnh ghế. Cả khối bàn–người chiếm vùng giữa/thấp, footer 200px sạch. Chữ duy nhất “CẢ GIA ĐÌNH”. Phụ huynh nữ giữ tạo hình tóc tím/áo mint đã duyệt, phụ huynh nam là asset mới đang đề xuất.

Pose 01: mascot đã nắm cạnh lưng ghế trống. Pose 02: ghế dịch ra trái 35px/xuống 20px, bàn không đổi; tay vẫn bám đúng cạnh. Pose 03: mascot đã ngồi cùng bàn, nhìn/chỉ vào bản kế hoạch chung. Khi dựng phải có đường đi quanh mép ghế và tư thế ngồi xuống, không nhảy hoặc xuyên qua lưng ghế để đến pose 03. Đừng suy ra ba pose tĩnh đã chứng minh chuyển động ngồi đúng. Nếu cần, thêm pose trung gian trước khi render.

Dự kiến nhịp: mở cảnh đọc chỗ trống, tới ý “xây dựng một nền tảng” bắt đầu kéo ghế, tới “cả gia đình” ổn định nhóm cùng bàn. Đối chiếu WAV để khóa cue, giữ trọn 5.796583333333s. Phụ huynh có thể chuyển ánh nhìn theo mascot/bản kế hoạch, không bắt buộc vẫy liên tục.

## S11 — Chuẩn bị cho con

Ý cần đọc: đầu tư đi cùng chuẩn bị cho tương lai của con, thông qua một hành động gia đình cụ thể. Chìa khóa nằm trên bàn làm tín hiệu tài sản; trọng tâm chuyển tới vở và ba lô. Không thêm nhà/giá/claim pháp lý.

Pose 01: phụ huynh đang giữ cạnh trái quyển vở; mascot ở cạnh túi, tay nhận chưa chạm vở. Pose 02: tay mascot đã chạm cạnh phải; có một nhịp cả hai cùng giữ trước khi phụ huynh nhả. Pose 03: vở đã hạ vào ba lô và bị túi trước che phần dưới; tay nhả sau khi vở được đỡ, không biến mất/fade để giả cất. Tay còn lại nghỉ bên hông; túi đứng vững trên bàn nên không cần cưỡng ép thêm một động tác giữ. Không có cánh tay chạy ngang mặt. Ba lô xanh được đặt trên bàn, không vẽ thêm một ba lô trùng trên lưng.

Dự kiến nhịp: đầu câu giữ chìa khóa và vở trong cùng không gian; cụm “mà còn” bắt đầu chuyển giao; cụm “sự chuẩn bị” nhận và cất; “tương lai của con cái” giữ kết quả túi sẵn sàng. Voice S11 gồm nguyên seg_12 + seg_13, 6.811833333333s; không chia/cắt lời để vừa thao tác.

## Asset/layer và phần giữ

- Giữ mascot cam/mũ tím, mẹ tóc tím/áo mint và font Segoe UI Black từ vòng đã duyệt. Tạo hình cha, bàn/ghế, túi và các pose mới ở vòng này vẫn chờ duyệt.
- S06 tách: ghế nền, người thân/đầu/mắt/tay/chân, bàn/plan, ghế trống, mascot/chi/hand. Ghế và grip phải chung tọa độ tiếp xúc; không scale bàn.
- S11 tách: phụ huynh/tay cho vở, mascot/tay nhận/tay nghỉ bên hông, vở, túi sau/miệng túi/túi trước, bàn/chìa khóa. Chuyển quyền giữ vở sau tiếp xúc, không tween prop độc lập trong lúc đang cầm.
- Lớp placement giữ tọa độ/scale; motion dùng wrapper riêng, vai nằm cố định trong rig. Không dùng y=-6 trên node có translate y lớn.
- Có thể chỉnh crop, pose, đường cong khuỷu, màu tint và cue nhỏ cho hợp voice. Đổi hành động trung tâm cần cập nhật thiết kế trước.

Sau khi người dùng duyệt frame mới dựng pilot từng cảnh để kiểm motion, contact quanh event ở 10–12fps, mobile và playback. Không render full phim từ các pose tĩnh này.
