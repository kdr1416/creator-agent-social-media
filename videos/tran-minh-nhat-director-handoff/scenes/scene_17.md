# 17 · Hành trình còn tiếp

**Voice gốc:** tiếp tục phát huy bản lĩnh, khám phá những cơ hội mới và chinh phục nhiều cột mốc lớn hơn trong tương lai.

**Thời lượng:** 4.764916667s · sample 1522442–1636800 · audio `inputs/audio/scene_17.wav`.

**Ý cần đọc được:** Kết bằng sự chủ động và tương lai mở, không invent nghề nghiệp/học vị/mức lương.

**Dàn khung:** Bám Nhật từ góc3/4 trong cùng phố16. Nhật x300–435/y685–1005; không gian phía trước mở x430–680/y390–940. Máy kéo rộng vừa phải; nội dung vẫn chiếm đến y1040.

**Mở cảnh:** Nhật tiếp bước trên cầu rồi mở cuốn sổ xanh bên mình; những trang phía sau còn trắng.

|Thời gian cục bộ|Cue thoại|Hành động thực hiện|
|---|---|---|
|0.00–1.300s|tiếp tục phát huy bản lĩnh|Nhật dừng một nhịp, mở sổ và kẹp trang mới; giữ dấu cam của cảnh01 như callback.|
|1.30–2.800s|khám phá những cơ hội mới|Nhật khép sổ vào tay và bước khỏi nhịp cầu, khung nhìn mở thêm khoảng phố phía trước, không bay qua các career icons.|
|2.80–4.150s|chinh phục nhiều cột mốc lớn hơn|Nhật bước tiếp trong môi trường, mái nhà/tiền cảnh dịch theo parallax thật của góc nhìn; không mốc số/đích nghề nghiệp.|
|4.15–4.765s|trong tương lai|Giữ Nhật đang hướng tới phần phố ngoài khung cùng HÀNH TRÌNH CÒN TIẾP; kết nhẹ0.6s, không thêm CTA.|

**Chốt:** Có người đang đi tiếp và những trang chưa viết; không chốt một kết quả ngoài voice.

**Nhân vật:** Mở sổ, đánh dấu trang mới rồi chủ động đi tiếp; không chinh phục mục tiêu bịa.

**Chữ trên hình:** HÀNH TRÌNH CÒN TIẾP. Voice kể phần giải thích; không thêm câu dài hoặc leader line cho nhãn.

**Asset và lớp cần có:**

- `student_walk` — **to_extend_reference_rig**. Cùng mascot, stride2–3 tư thế và quay chào; bước chân có tiếp đất, tay giữ sổ khi đi. Tách: hips/body, alternating legs, free arm, book arm, head turn. Nguồn: library/student.js.
- `canal_scene` — **to_draw**. Phố Hà Lan minh hoạ, cầu thấp qua kênh, ba mái nhà gable, cửa sổ và nước. Không lấy landmark làm campus VU hoặc diễn tả đã tới địa điểm thực. Tách: far roofs, near facades, water, far bridge, bridge walking plane, near rail, page edge reveal. Nguồn: generic illustrated Dutch canal setting, no specific named landmark.
- `notebook` — **to_draw**. Sổ xanh bìa mềm, một dấu cam ở góc và gáy rõ; có bìa đóng/mở, mép trang và clip. Chữ tên chỉ khi scene yêu cầu. Tách: front cover, spine, page block, opening page, orange bookmark. Nguồn: design based on selected blue/orange roles; not the old envelope.

**Nối sang cảnh sau:** Kết phim bằng hold0.6s và kết voice gốc; không logo/đăng ký/mời liên hệ tự thêm.

**Vì sao HF_ONLY:** Thế giới vẽ tiếp ra khỏi trang và callback cuốn sổ mang ý hành trình chưa hoàn tất. HYBRID montage công việc/tốt nghiệp sẽ thêm kết quả chưa có; chuyển động lớp giấy và bước đi vector đủ rõ.

**Kiểm hình của cảnh:** xem mở/đang hành động/chốt. Hành động phải đọc được ở360×640, tay tiếp xúc đúng đạo cụ khi cầm, nhãn không che vật thể, không tạo thành tích/đích đến ngoài lời thoại. Footer y1080–1280 giữ trống.
