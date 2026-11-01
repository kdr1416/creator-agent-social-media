> **S05 R1 đã duyệt:** đặt ghim Malta → cắt sang ảnh nhà thật. Dùng [hướng dẫn Antigravity](handoff/S05_STORYBOARD_RESTART_R1/ANTIGRAVITY_PROMPT.md) để dựng pilot riêng. Chưa duyệt frame/motion S05 mới; không dựng full phim. Thông báo này thay trạng thái chờ duyệt S05 ở lịch sử bên dưới.

> **Cập nhật S05:** Album v5 không được duyệt. Mọi mô tả/hình S05 bên dưới là lịch sử và được thay bằng [storyboard viết lại R1](handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md), đang chờ duyệt. Hai pilot đã duyệt là S01 bản đầu + S09 motion r1. Chưa dựng frame/pilot mới hoặc full phim.

# Asset plan

Giữ mascot từ reference 12; làm pose/rig theo cảnh. Segoe UI Black và GSAP copy local. Không dùng kit human/muted của trial bị từ chối.

Pilot: S01 cuốn sách/trang gấp/mái nhà/nhóm gia đình; S05 ảnh Valletta + viền ảnh/giấy gấp/ngôi nhà/mascot; S09 cơ cấu rãnh cong/ba bệ/ba đồng tài sản/dấu dao động. Mỗi lớp điều khiển độc lập, không flatten video thành một ảnh.

11 cảnh còn lại chỉ có kế hoạch, xem scenes/Sxx/packet.json. Antigravity cần tạo layer theo asset_contract; chưa có asset không được đổi sang card generic.

Ảnh Valletta: Juliana da Costa José, Wikimedia Commons, CC BY-SA 3.0. Dùng để nhận biết nơi chốn; không là dự án bất động sản, không coi cảnh chụp cũ là bằng chứng giá hiện tại. Credit và link license nằm trong ASSET_PLAN.json và CREDITS.md.

Tất cả asset pilot được đóng gói local; status final phải đối chiếu file thực tế, không suy từ bảng này.

## Phiên bản hình đã duyệt

Người dùng duyệt frame kết **S05 v3**: `revisions/S05-final-frame-v3/frames/frame-00-at-0.5s.png`; source `revisions/S05-final-frame-v3/index.html`. Chọn góc nhà phố với ban công gỗ xanh, tường đá sáng, một nếp giấy. Bản S05 v2 bị loại. Đây là duyệt frame tĩnh; chưa duyệt chuyển động S05 hoặc dựng full; S09 có xác nhận riêng ở cập nhật bên dưới. Chi tiết và checksum: `research/visual-approvals.json`.


## Cập nhật duyệt S09 v2

Người dùng đã duyệt frame kết **S09 v2**: `revisions/final-frames-v2/S09/frames/frame-00-at-0.5s.png`; source `revisions/final-frames-v2/S09/index.html`. Chọn bàn phân bổ có chất liệu gỗ, chốt chia, đường dẫn cong và nhóm tài sản nhiều lớp. Đây là duyệt frame tĩnh; chuyển động sửa S09 chưa được dựng/duyệt. Hai frame được chọn hiện tại: **S05 v3 + S09 v2**. Xem `APPROVED_VERSIONS.md` và `research/visual-approvals.json`.


## Hai pilot chuyển động mới · r1

Đã dựng S05 theo frame v3 và S09 theo frame v2 đã duyệt. Xem `revisions/pilots-approved-frames-r1/REVIEW.html`; MP4/source/asset local nằm trong các thư mục S05 và S09 cạnh trang đó. Voice PCM đúng lát gốc. Bản chuyển động r1 đang chờ người dùng duyệt; không tự coi việc yêu cầu render là duyệt motion, không dựng full. Pilot cũ giữ nguyên để đối chiếu.

Mốc cue mới: S05 bắt đầu mở ban công khoảng 4.32s local theo cụm bất động sản trong ASR; S09 mở phân bổ khoảng 2.43s local theo cụm nhiều thị trường. Đây là bằng chứng timing ASR, không thẩm âm độc lập. Xem DIRECTION.json và verification.json ở revision.
