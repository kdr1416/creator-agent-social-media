# Prompt bàn giao cho Antigravity

Dựng bản thử độc lập cho project tran-minh-nhat từ bộ tài liệu tại:
D:\Năm 3\flowkit-main\videos\tran-minh-nhat-director-handoff

Bắt đầu bằng START_HERE.md, DIRECTOR_BRIEF.md và TECHNICAL_HANDOFF.md. Đây là storyboard do Codex thiết kế; bạn phụ trách asset và triển khai, không tự viết lại ý tưởng cho từng câu voice.

Đọc STORYBOARD.md/JSON và packet scenes/scene_XX.md. Có14cảnh cần dựng;04,06,12 dùng đúng nguồn/video hiện tại trong reference_pilots. ASSET_PLAN cho biết cái nào có sẵn, cái nào cần vẽ/tìm; dùng source chứ không cố kéo mọi thứ từ MP4.

Tạo asset/composition/review/render trong build/ của folder này. Có thể tinh chỉnh cân khung, độ chi tiết, pose, timing hoạt ảnh và easing để cảnh đọc tốt. Giữ hình chủ đạo, quan hệ ý nghĩa và hành động chính theo packet. Khi không dựng được ý đã chọn, ghi rõ vướng mắc ở build/reviews và tiếp tục phần độc lập, không âm thầm thay thành card/icon template.

Voice trong inputs/ là bản copy gốc: không TTS, không đổi chữ/tốc độ/âm sắc. Dùng mốc sample và picture_frame_plan; assembly cuối chỉ một full_voice.wav. Không thêm CTA, nhạc/SFX hoặc phụ đề tự động. Không cập nhật scratch/, workflow chính, database/API hay các folder pilot cũ.

Trước hết dựng dailies cụm01–05 để xem nhịp nối qua pilot04; sau đó tiếp các cụm còn lại theo REVIEW_GUIDE. Bạn không cần xin lại phép cho việc vẽ asset/render trong phạm vi bản thử này. Chỉ việc công bố/đổi audio/ghi đè workflow chính nằm ngoài scope. Cảnh10 có claim cần kiểm chứng trước công bố nhưng không cản dựng workprint riêng.

Ghi tiến độ riêng trong production_status.json của gói và build/reviews, không mượn status trong scratch. Khi xong, báo file thật đã tạo, cảnh còn thiếu và giới hạn kiểm tra; không coi14cảnh đã render khi mới có kế hoạch.
