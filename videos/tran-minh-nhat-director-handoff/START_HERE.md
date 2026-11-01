# Trần Minh Nhật — bộ storyboard đạo diễn cho Antigravity

**Phần hoàn tất:**14thiết kế mới +17packet đầy đủ, mạch toàn phim68.2s, kế hoạch27nhóm asset, bản sao voice và ba pilot hiện tại. **Chưa làm trong lượt này:**asset mới, render14cảnh và assembly toàn phim.

## Đọc theo thứ tự

1. [DIRECTOR_BRIEF.md](DIRECTOR_BRIEF.md): gu và ranh giới giữa thiết kế cảnh / chi tiết thi công linh hoạt.
2. [STORYBOARD.md](STORYBOARD.md): toàn bộ voice, bố cục, nhịp và nối cảnh. [STORYBOARD.json](STORYBOARD.json) để đọc bằng máy; mỗi cảnh còn có packet trong scenes/.
3. [ASSET_PLAN.md](ASSET_PLAN.md):27nhóm asset, trạng thái, nguồn, lớp độc lập. Không phải mọi cảnh dùng asset của pilot.
4. [TECHNICAL_HANDOFF.md](TECHNICAL_HANDOFF.md):sample voice, grid2046frames và tránh audio chồng/drift.
5. [REVIEW_GUIDE.md](REVIEW_GUIDE.md) và [RESEARCH.md](RESEARCH.md).

[ANTIGRAVITY_PROMPT.md](ANTIGRAVITY_PROMPT.md) là đoạn giao việc có thể copy nguyên cho Antigravity. Chưa có tin nhắn/tác vụ nào được gửi tự động cho ứng dụng khác.

## Chỗ đặt dữ liệu

- inputs/:voice gốc và17lát +manifest; original_audio_handoff chỉ là snapshot lịch sử, đường dẫn vận hành dùng audio_manifest.
- reference_pilots/:đúng04gốc /06v4 /12v6, gồm source editable và MP4, không lẫn bản thử cũ bị bác.
- library/:font Việt đã kiểm, runtime, rig và ảnh VU có sẵn. Các môi trường/pose mới vẫn phải dựng.
- scenes/:17packet;14cảnh mới ghi rõ thao tác,3pilot ghi cách dùng lại.
- build/:chỗ Antigravity sẽ tạo scene,asset,review,render. Hiện trống.
- render_handoff.json và production_status.json:độc lập với workflow chính.

Đây là bộ thiết kế cụ thể cho phim này, không phải một skill chứa nhiều luật cứng. Tinh chỉnh kỹ thuật được khuyến khích; đổi ý nghĩa/hình chủ đạo cần được nhận diện là đổi storyboard.

**Một bước dọn pilot cũ:**04còn dòng Hình minh hoạ; builder bỏ node này trong bản copy build/ trước assembly. Giữ nguyên source frozen và toàn bộ thiết kế04. Xem TECHNICAL_HANDOFF.
