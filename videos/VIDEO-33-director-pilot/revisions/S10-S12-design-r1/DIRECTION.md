> **27/10/2026: Thiết kế frame S10/S12 R1 đã được người dùng duyệt.** Motion chưa được dựng hoặc duyệt. APPROVAL.json khóa phiên bản và manifest ảnh tham chiếu.

# S10/S12 — frame đề xuất R1

Trạng thái: chờ người dùng duyệt frame/tạo hình/hướng hành động. Chưa có motion hoặc MP4 mới; chưa đổi master. S06 và S11 motion R1 đã được duyệt riêng, không phải đối tượng sửa ở vòng này.

## S10 — Chi phí được nêu, gia đình bốn thế hệ

Scene dựng S10 = voice 11, 6.156875s, sample [1134024,1281789). Giữ raw/corrected text tách biệt và voice nguyên bản; metadata trong VOICE_REFERENCE.json.

Ý chính: lời dẫn nêu khoảng 3,8 tỷ và khả năng tới bốn thế hệ. Hình thay thế khối giấy rỗng: nhóm người thân có tuổi tác khác nhau, cùng một mặt sàn, đủ tỷ lệ đọc được. Không dựng hộ chiếu EU, thẻ có tên/ngày thật, con dấu duyệt hoặc cảnh trao quyền pháp lý.

Pose 01: “KHOẢNG / 3,8 TỶ” là hero metric trên nền đào; người mẹ và mascot ở dưới. Nhân vật hướng chú ý sang khoảng trống dành cho người thân tới. Không gán con số lên ngôi nhà hay ghi trọn gói.
Pose 02: hai thế hệ lớn tuổi bước vào phía trái để nhóm hình thành. Đây là state định vị nhân vật, không phải phép tự xuất hiện/tăng kích thước.
Pose 03: bốn thế hệ đứng trong một nhóm; người lớn tuổi vịn gậy và nắm tay người con, đương đơn nắm tay mascot. Tới nhịp “4 thế hệ” mới đọc đủ tiêu đề và nhãn quan hệ. “ÔNG BÀ / CHA MẸ / ĐƯƠNG ĐƠN / CON” đều tính theo đương đơn ở áo mint; không phải bốn thế hệ hậu duệ của mascot.

Nhịp dự kiến khi dựng: metric bám cụm “khoảng 3,8 tỷ”; chuyển trọng tâm khi voice nói chương trình/cơ hội; nhóm hoàn tất theo “4 thế hệ”, giữ ngắn tới hết câu. Chưa khóa word cue bằng nghe độc lập. Đối chiếu WAV trước motion; không kéo dài voice để vừa việc di chuyển. Nhãn nhỏ có thể chỉ hiện ở resolve, không tích lũy với giá.

Giữ chữ “TỚI 4 THẾ HỆ” và “Theo điều kiện MPRP”. Nguồn chính thức kiểm ngày 27/10/2026: https://residencymalta.gov.mt/legal-framework-mprp-2/ — nêu khả năng tới bốn thế hệ trong một hồ sơ. Giá 3,8 tỷ tiếp tục là nội dung chủ dự án đã xác nhận, không nâng thành báo giá độc lập hay phí bao trọn mọi người thân. RESEARCH_NOTE.json ghi rõ nguồn/phạm vi.

## S12 — Thử sức qua một hoạt động cụ thể

Scene dựng S12 = voice 14, 3.531458333333s, sample [1445273,1530028). Lời nói về cơ hội cho thế hệ sau; mô hình là một tình huống học hỏi/thực hành tượng trưng, không đại diện một chương trình/trường/việc làm được bảo đảm.

Một mô hình chong chóng có trụ, cánh, nguồn điện, nút điều khiển và bệ thật trên bàn. Mascot là người thao tác. Pose 01: ngón tay ở trên nút, mô hình chưa chạy. Pose 02: chạm và ấn đúng mặt nút, đèn trạng thái sáng. Pose 03: cánh ở góc khác, có ký hiệu chiều quay trong frame; mascot nhả nút và nhìn kết quả. Các nét cong trong frame chỉ mô tả trạng thái chuyển động dự kiến; chưa có rotor motion được kiểm.

Khi dựng: đầu cảnh khoảng 0–0.7s đọc tình huống, 0.7–1.1s bấm, 1.1–2.4s cánh bắt đầu quay/mascot thu tay; cuối giữ hoạt động đang chạy tới hết voice. Cue là đề xuất đạo diễn để đối chiếu audio. Nút là điều khiển bật mô hình; không diễn tả phát điện nhờ bấm nút. Chỉ quay cụm cánh quanh trục hub (490,505); trụ/bệ không trượt hoặc nhảy. Tay bám nút (385,829) tại press; vai cố định, cẳng tay/bàn tay cùng hệ tọa độ. Không để ba lô che điểm bấm.

## Tạo hình, layer và phần giữ

Nền S10 đào, S12 kem/lilac nhẹ; mascot cam/mũ tím/ba lô xanh, người mẹ cùng tạo hình các vòng đã duyệt. Người lớn tuổi, các pose và mô hình mới đều chờ duyệt. Segoe UI Black hỗ trợ tiếng Việt; footer y1080–1280 sạch. Engine giữ HF_ONLY, chưa thay routing.

S10: tách metric, global title/condition, nhãn từng thế hệ, từng người/chi/mắt, gậy, bóng sàn và điểm nắm tay. Phải giữ đúng bốn thế hệ; người thay cho một thế hệ là đại diện đồ họa, không bản danh sách đầy đủ người được chấp thuận.
S12: tách rotor-placement / rotor / hub, trụ, bệ, pin/dây, vỏ nút, mặt nút/LED, bàn, rig và mắt mascot. Đây là prop riêng có tương tác cụ thể; catalog đã tra trong catalog-search.json, không dùng component chung để thay mô hình.

Giữ hình chính và quan hệ nhân–quả; được chỉnh pose/crop/tint/easing/cue nhỏ sau khi đối chiếu voice. Chưa được đổi chủ đề thí nghiệm, biến giá thành giá căn nhà, hay thêm quyền lợi/claim không có trong voice.

S10 khác S11: nhóm gia đình trên không gian mở, không thêm một bàn/album. S12 khác S11 dù cùng có mặt bàn: một mascot + máy thử cao/rotor lớn, thao tác nút → phản ứng; S11 là hai người chuyển giao vở/túi. Không nối cưỡng ép cùng quyển vở hay bàn giữa hai cảnh.

Sau duyệt hình mới dựng pilot, kiểm tiếp xúc quanh event và playback thật, mobile/grayscale. Hai pose rotor khác góc không chứng minh chuyển động quay đã đúng.
