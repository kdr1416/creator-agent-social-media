# Trần Minh Nhật · Style lab 06 + 12

Hai cảnh độc lập theo voice gốc, không phải hai cảnh nối tiếp của phim đầy đủ.

- `renders/scene_06-v4.mp4`: nhiều lĩnh vực cùng một campus, 5.20s export (voice 5.1926666667s).
- `renders/scene_12-v6.mp4`: hồ sơ có dấu riêng, 4.433333s export (voice 4.41925s).
- `planning/storyboard.md` và `.json`: bản thiết kế riêng cho lần thử này.
- `planning/asset-ledger.json`: asset dùng lại, asset mới, nguồn và các lớp sửa được.
- `render_handoff.json`: đầu vào cho Antigravity; mọi đường dẫn output tương đối với thư mục lab này.
- `scene_06/index.html`, `scene_12/index.html`: nguồn chỉnh sửa được, asset local trong mỗi scene.
- `qa/`: trước/sau về tính nguyên vẹn, so sánh reference và kết quả QA.

## Phạm vi cô lập

Không cập nhật bất kỳ file nào trong `scratch/`, không thay storyboard/pilot trước, không cập nhật database/API hay workflow chính. Voice được copy nguyên file vào `scene_XX/assets/audio.wav`. Khi tiếp tục thử, chỉ ghi trong folder lab này hoặc folder thử mới. Bản MP4 dùng AAC; WAV gốc không bị xử lý hoặc time-stretch.

## Render lại

Cần Node.js, HyperFrames 0.8.170, FFmpeg trên PATH. Chạy từ folder lab:

```powershell
./tools/render-single-voice.ps1 -ProjectPath ./scene_06 -NarrationPath ./scene_06/assets/audio.wav -OutputName scene_06-v5.mp4
./tools/render-single-voice.ps1 -ProjectPath ./scene_12 -NarrationPath ./scene_12/assets/audio.wav -OutputName scene_12-v5.mp4
```

Script từ chối thay output đã có. Mỗi scene có một entry `index.html`; nguồn picture-only nằm ở `render-src/` và được tạo từ entry, rồi ghép một voice track bằng FFmpeg. Không dùng root picture-only làm entry thứ hai của Studio.

## Tiếp tục với Antigravity

Đọc `render_handoff.json`, `planning/storyboard.json`, `planning/asset-ledger.json`, `qa/visual-review.json` và nguồn từng cảnh. Giữ grammar màu/nét/chữ/nhân vật; thiết kế asset theo nghĩa từng cảnh, không sao chép bố cục. Các cảnh này và pilot 04 vẫn là thử nghiệm có thể sửa, không phải template bắt buộc hoặc phê duyệt thẩm mỹ toàn phim.

## Revision 2

Arial Black900 cho tiêu đề và nhãn. Tư duy/Định hướng gắn cạnh hình tương ứng trong cảnh12. Bản v1 và gói source v1 giữ nguyên để so sánh. Output mới có hậu tố-v2; dùng tên-v3 khi render lần tiếp theo.

## Revision3

Font hiện tại: Segoe UI Black900. Arial Black là bản lỗi thiếu glyph tiếng Việt, không dùng lại. Bản-v3 đã xuất và kiểm tra glyph, frame mobile, audio. Bản-v2 giữ lại để đối chiếu.

## Revision4

Đã bỏ chú thích minh hoạ trên hình trong cả hai cảnh, giữ font Việt và nhãn nội dung.

## Revision5 — scene12 redesign

Cảnh06 giữ bản-v4. Cảnh12 hiện là scene_12-redesign.mp4: hình ghép/Tư duy, chân dung tự cá nhân hoá/Cá tính, bản phác tương lai được chọn/Định hướng. Nguyên voice4.41925s. Nguồn mới dùng assets/portrait-v5.js, các bản cũ vẫn giữ nguyên.

## Revision6

Cảnh12 bỏ nét nối chú thích, thay bản phác tương lai bằng chọn và khoanh ảnh campus VU trên kế hoạch học tập. Bản hiện tại scene_12-v6.mp4. Cảnh06 giữ nguyên.
