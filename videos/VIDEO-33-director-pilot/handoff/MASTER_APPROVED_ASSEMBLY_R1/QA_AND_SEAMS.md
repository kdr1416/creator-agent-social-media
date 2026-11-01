# Kiểm toàn phim sau ghép

Phát toàn bộ master có tiếng từ0 tới hết, ít nhất1 lượt không tua để kiểm mạch kể. Tiếp đó xem riêng13điểm nối, mỗi điểm từ1giây trước tới1giây sau, có voice. Ghi thời gian và PASS/FAIL/NEEDS_REVIEW thực tế; không suy diễn pass từ ffprobe.

Kiểm continuity: kích thước/nét mascot, màu nền, hướng nhìn, ngôn ngữ chữ, độ sáng và nhịp giữa cảnh. Đặc biệt S04→S05 câu hỏi tài sản sang lựa chọn địa điểm; zoom0.8s S05→đặt/nhả ghim→ảnh nhà ở cue “bất động sản”; S05→S06 ảnh nhà sang bàn gia đình; S09→S10 thay cơ chế phân bổ bằng nội dung tiếp theo; S12→S13→S14 giữ mạch con ra thế giới→tài sản→lựa chọn tương lai. Không ép biến cửa nhà thành bàn hoặc nối bước chân không phù hợp.

Dùng cut sạch trước. Chỉ thêm xử lý nối ngắn khi có lỗi nhìn thấy và không che động tác/đổi ý/cắt voice. Không tự thiết kế lại cảnh đã duyệt. Nếu seam chưa ổn, xuất A/B ngắn và ghi đề xuất, không tự thêm morph/wipe/flash hàng loạt. Mọi thay đổi đối với ý tưởng hoặc key pose đã duyệt phải ghi rõ để người dùng xem.

Kiểm voice: full original WAV từt0, mọi sample đủ1,803,840@24kHz; audio từ pilot bị bỏ. Nghe đủ câu, không click/đúp tiếng/mất khoảng nghỉ. Đối chiếu cue và ranh giới audio ở từng seam; không speed/pitch shift để khớp duration video. AAC đối chiếu source decode về24kHz mono, kiểm offset/correlation và mức gain; không auto-normalize. Voice75.16s, video75.166667s có hold cuối6.667ms là đúng.

Kiểm hình: không đen/flash/frame thiếu/ảnh tĩnh bất ngờ; không tay lìa, clip mascot, pin trượt, lệch phông, lỗi dấu. Kiểm full master và13seam ở360×640, mở/giữa/cuối các cảnh thay và grayscale/thumbnail. S02–S04 là bản nền giữ lại, vẫn phải review trong mạch mới, không coi là đã qua duyệt pilot mới.

Kiểm kỹ thuật:720×1280,30fps,2255frames; video H.264, tiếng AAC từ source WAV nguyên bản; clean/master cùng frame count. Manifest nêu chính xác frame nào trim/hold ở đuôi. Đếm frame trên timeline toàn phim; đừng cộng thời lượng lẻ từng pilot. Không thay frame đầu hoặc semantic-action giữa cảnh để bù duration. Nếu cần pad hơn1frame, hoặc timeline lệch >1frame, dừng chỉnh tự động và báo vấn đề cụ thể.

Bàn giao INSPECTION_REPORT.md có evidence đường dẫn (MP4 cuối, seam-clips, mobile proofs, ffprobe và audio check); liệt kê lỗi còn lại trung thực. Không ghi toàn phim đã được người dùng duyệt chỉ vì các pilot đã duyệt.
