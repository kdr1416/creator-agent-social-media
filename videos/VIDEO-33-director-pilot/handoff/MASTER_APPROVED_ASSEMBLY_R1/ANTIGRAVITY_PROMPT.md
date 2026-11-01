# ANTIGRAVITY — Ghép VIDEO-33 master mới từ các pilot đã duyệt

Người dùng đã duyệt các pilot được khóa trong gói này và yêu cầu: “oke giờ bàn giao cho antigravity ghép các bản đã duyệt vào master mới và xem lại mạch phim, chuyển cảnh, đồng bộ voice một lượt di”. Hãy thực hiện assembly và review toàn phim, không chỉ lập kế hoạch.

Project root: `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot`
Handoff folder: `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\handoff\MASTER_APPROVED_ASSEMBLY_R1`
Output riêng: `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\build\master-approved-r1`

Đọc ASSEMBLY_MANIFEST.json, SELECTED_VERSIONS.md và QA_AND_SEAMS.md trước khi sửa. Xác minh hash11pilot đã duyệt,3cảnh nền, voice và2master cũ. Có đủ source editable/assets/font trong project, không cần tái tạo asset. Không sửa workflow chính hay thư mục dự án tham chiếu. Giữ nguyên các pilot/source đã duyệt.

11pilot được duyệt: S01 bản đầu; S05 S05-zoom-motion-r1 (bản cuối đã sửa lớp bàn tay, SHA c53f14fdaff26500bac4bcd529fc6aee614a4126c3c87c8b35e72a12365f6a7b); S06/S11 S06-S11-motion-r1; S07/S08 S07-S08-motion-r1; S09 motion-r1 trong pilots-approved-frames-r1; S10/S12 S10-S12-motion-r1; S13/S14 S13-S14-motion-r1. S02–S04 giữ build/scenes/S02–S04/renders/pilot.mp4. Đọc path và SHA chính xác trong manifest, không lấy “bản mới nhất” theo thời gian file. Tuyệt đối không lấy S05 album/v5 hoặc native-auto-gain-history/native-grip-fixed.

Ghép hình theo global frame ranges manifest:720×1280@30fps2255frames. Từng scene dùng source từframe0, cắt hold dư ở đuôi hoặc lặp frame cuối tối đa1frame khi thiếu, theo target_frames; không đụng hành động chính. Nếu lệch khác mức ghi trong manifest, kiểm tra nguồn trước. Không cộng duration ceil của các MP4. Thời gian voice cố định75.16s. Bỏ toàn bộ tiếng trong MP4pilot; dùng duy nhất `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\inputs\source_audio.wav` từt0. Giữ đủ1,803,840samples24kHzmono, không TTS/normalize/limiter/auto gain/pitch/time stretch. Encode AAC trực tiếp được, giữ WAV gốc nguyên hash. Bản clean không tiếng.

Giữ bố cục, hình, nhịp hành động, font và cut nội cảnh đã duyệt. S05 zoom0–0.8s, đặt ghim0.9–2.55s, nhả2.7–3.35s, cutảnhnhà4.35s; chữ MALTA từ đầu, không Sicily. S13 camera mở khung, S14 mẹ mở cổng đều giữ motion hiện tại. Phần linh hoạt: trim/hold đuôi <=1frame, encoding và xử lý seam nhỏ có lý do; không tự redesign, không đảo thứ tự cảnh. Nếu phát hiện vấn đề ở cảnh được duyệt thì ghi timestamp và A/B đề xuất, không âm thầm thay bản.

Phát toàn phim có voice trọn1lượt, sau đó kiểm13seam có tiếng, mobile360×640 và frame đầu/giữa/cuối cảnh sửa. Theo QA_AND_SEAMS.md, sửa lỗi assembly/encode/sync trong phạm vi này; báo riêng nếu lỗi đòi đổi ý tưởng cảnh. Cần evidence thực tế; không chỉ dựa technical pass.

Xuất trong output folder mới:
- VIDEO-33-master-approved-r1.mp4 có voice gốc.
- VIDEO-33-clean-approved-r1.mp4 cùng hình không tiếng.
- Source assembly editable và script/config tái lập, manifest nguồn và SHA-256 output.
- REVIEW.html xem full master, các seam clip và mobile proofs.
- INSPECTION_REPORT.md ghi kết quả mạch phim,13seam, sync voice, lỗi tồn tại, cùng ffprobe/audio evidence.
- production_status.json: assembled_pending_user_full_master_review; không tự ghi full_master_approved.

Bảo toàn `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\build\renders\VIDEO-33-master.mp4` và clean cũ nguyên hash. Không publish/upload hoặc ghi đè master cũ. Hoàn thành bản master mới cho người dùng xem duyệt rồi dừng.
