> Người dùng duyệt ngày 27/10/2026: “oke duyệt cái này”. Đọc ANTIGRAVITY_PROMPT.md để dựng thử motion. Không suy rộng sang các cảnh khác.

# S07/S08 — frame R1 đã duyệt; motion chưa duyệt

Đây là các tư thế tĩnh/khung hoạt động để duyệt ý và tạo hình, không phải motion đã dựng. Không thay source trong build, không đổi voice/timing hay trạng thái các pilot đã duyệt.

S07: một người thân lớn trong laptop; mascot chạm nút gọi, sau đó thu tay và vẫy đáp lại. Phụ huynh áo mint/tóc tím than là cùng một nhân vật với S08. Nút là bộ phận của giao diện cuộc gọi có chức năng; không có hộp thông tin trang trí. Frame 01/02/03 lần lượt là chờ, tiếp xúc và kết nối. Giữ nguyên voice/sample bounds từ STORYBOARD.json khi sản xuất. Không tạo file audio mới ở vòng frame.

S08: phụ huynh toàn thân, vali tới hông, tay bám cần kéo, mascot và phụ huynh cùng mặt sàn. Frame 01 và 02 minh họa đến nơi/chào con, chưa phải kết quả nội suy giữa hai pose. Ba khung sau là ba hoạt động dự kiến thay lần lượt theo học tập/sinh sống/làm việc; không đặt cả ba icon nhỏ đồng thời. Đây là các khả năng kế hoạch, không là bằng chứng quyền làm việc/nhập học. Khi đối chiếu voice nếu không đủ thời gian, giảm động tác mỗi khung, không tăng tốc voice. Giữ footer 200px, chữ ngắn Segoe UI Black.

Rig: node placement chỉ đặt vị trí/scale; motion dùng wrapper riêng. Giữ vai cố định trong torso-space; forearm/hand cùng chain; tính điểm chạm theo matrix sang scene-space. Không animate y=-6 trên node có translate y≈760. Vali và tay dùng cùng điểm grip; bánh chạm sàn. Trước motion phải duyệt hình phụ huynh và laptop.

Thời lượng: S07 ≈4.70s, S08 ≈5.45s (số chính xác từ packet/audio gốc). S07 dự kiến 0–1.2s đưa tay/chạm, 1.2–2s kết nối, 2–4.7s vẫy/resolve. S08 dự kiến 0–1.5s gặp con, ba shot học/sống/làm thay lần lượt trong phần còn lại theo lời; đối chiếu word cue trước khi khóa. Không suy ra các pose tĩnh đã chứng minh rig chuyển động đúng.

Sau duyệt mới dựng motion thử. Kiểm frame tiếp xúc quanh event và playback thật. Chưa sản xuất lại các cảnh khác; đề xuất S10–S14 nằm trong qa/antigravity-review-r1/REVIEW_AND_REVISION_PROPOSAL.md.
