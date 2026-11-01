> **S05 R1 đã duyệt:** đặt ghim Malta → cắt sang ảnh nhà thật. Dùng [hướng dẫn Antigravity](handoff/S05_STORYBOARD_RESTART_R1/ANTIGRAVITY_PROMPT.md) để dựng pilot riêng. Chưa duyệt frame/motion S05 mới; không dựng full phim. Thông báo này thay trạng thái chờ duyệt S05 ở lịch sử bên dưới.

> **Cập nhật S05:** Album v5 không được duyệt. Mọi mô tả/hình S05 bên dưới là lịch sử và được thay bằng [storyboard viết lại R1](handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md), đang chờ duyệt. Hai pilot đã duyệt là S01 bản đầu + S09 motion r1. Chưa dựng frame/pilot mới hoặc full phim.

# Đạo diễn · Một điểm tựa, thêm lựa chọn

Phim 75.16s đặt việc học của con cạnh kế hoạch dài hạn của gia đình. Kể bằng các vật thể có chức năng: sách nâng đỡ, giấy mở nơi chốn, bàn mở chỗ, dây kết nối, rãnh phân bổ và kế hoạch mở nhánh. Mỗi hành động phải giúp hiểu quan hệ, không chỉ đưa các danh từ bay vào.

Giữ nền cream #FFF8E9, peach #FFF0E5, lilac #F0EAFB; nét #30313B mảnh; cam #FFAA28, mũ #A990D5, túi #087BC1. Font local Segoe UI Black đầy đủ dấu; body Arial nếu cần trong tài liệu. Không Arial Black, không chữ Hình minh hoạ/Không gian minh hoạ trên video.

Giữ nguyên toàn bộ WAV, raw transcript và sample timing; corrected_text riêng chỉ chuẩn ASR/tên Malta. Không sửa câu giá/rights trong voice. Có vấn đề fact-check phải giữ trạng thái chưa duyệt xuất bản (RESEARCH.md), không ngầm sửa hoặc khẳng định bằng đồ họa.

Ba pilot là S01 biến đổi sách/điểm tựa; S05 collage địa điểm thật và giấy gấp; S09 cơ chế phân bổ nhiều thị trường. Chọn có chủ đích để thử ba bài toán khác nhau. Không sản xuất các cảnh khác.

Bắt buộc giữ: ý nghĩa/quan hệ từng packet, identity mascot, voice/timing, visual chủ đạo và signature action, không hứa việc làm/quốc tịch/lợi nhuận. Linh hoạt: cân khung, pose, easing, nếp giấy, chi tiết nét và mốc cử động trong cùng lát voice sau khi nghe đối chiếu. Đổi visual chủ đạo/engine phải ghi override có lý do.

Đây là bản đề xuất để người dùng duyệt, không phải phong cách mới đã được chấp nhận. Reference nguồn và workflow chính giữ read-only.

## Xác nhận nội dung từ người dùng

Người dùng đã xác minh text “3.8 tỷ” trong chat. Gỡ điểm chờ xác minh con số ở S10; giữ voice gốc “khoảng 3,8 tỷ”. Xác nhận này chỉ áp dụng số liệu, chưa là duyệt storyboard/pilot hoặc lệnh dựng full. Nguồn xác nhận lưu tại research/user-confirmations.json.


## Phiên bản hình đã duyệt

Người dùng duyệt frame kết **S05 v3**: `revisions/S05-final-frame-v3/frames/frame-00-at-0.5s.png`; source `revisions/S05-final-frame-v3/index.html`. Chọn góc nhà phố với ban công gỗ xanh, tường đá sáng, một nếp giấy. Bản S05 v2 bị loại. Đây là duyệt frame tĩnh; chưa duyệt chuyển động S05 hoặc dựng full; S09 có xác nhận riêng ở cập nhật bên dưới. Chi tiết và checksum: `research/visual-approvals.json`.


## Cập nhật duyệt S09 v2

Người dùng đã duyệt frame kết **S09 v2**: `revisions/final-frames-v2/S09/frames/frame-00-at-0.5s.png`; source `revisions/final-frames-v2/S09/index.html`. Chọn bàn phân bổ có chất liệu gỗ, chốt chia, đường dẫn cong và nhóm tài sản nhiều lớp. Đây là duyệt frame tĩnh; chuyển động sửa S09 chưa được dựng/duyệt. Hai frame được chọn hiện tại: **S05 v3 + S09 v2**. Xem `APPROVED_VERSIONS.md` và `research/visual-approvals.json`.


## Hai pilot chuyển động mới · r1

Đã dựng S05 theo frame v3 và S09 theo frame v2 đã duyệt. Xem `revisions/pilots-approved-frames-r1/REVIEW.html`; MP4/source/asset local nằm trong các thư mục S05 và S09 cạnh trang đó. Voice PCM đúng lát gốc. Bản chuyển động r1 đang chờ người dùng duyệt; không tự coi việc yêu cầu render là duyệt motion, không dựng full. Pilot cũ giữ nguyên để đối chiếu.

Mốc cue mới: S05 bắt đầu mở ban công khoảng 4.32s local theo cụm bất động sản trong ASR; S09 mở phân bổ khoảng 2.43s local theo cụm nhiều thị trường. Đây là bằng chứng timing ASR, không thẩm âm độc lập. Xem DIRECTION.json và verification.json ở revision.


## S05 motion r2 — sửa tính hợp lý, chờ duyệt

S05 motion r1 bị người dùng phản hồi ảo/phi logic. Bản r2 tại `revisions/S05-motion-r2/renders/pilot.mp4` bỏ mọi co giãn mặt nhà/ban công. Giữ ngôi nhà và ban công nguyên hình, không scale/skew/morph/fade. Mascot mở một bìa giấy có bản lề ở góc phải; bước ngang theo mép bìa đang quay, buông tay trước khi bước về vị trí kết. Bìa che được mở đi để lộ kiến trúc có sẵn, không biến giấy thành nhà. Voice nguyên lát nguồn. Frame kiến trúc v3 là tham chiếu đã duyệt; pose kết được chỉnh sau nhả tay để đúng hành động, chưa tự coi motion r2 là đã duyệt. S09 r1 giữ nguyên. Trang xem mới: `revisions/S05-motion-r2/REVIEW.html`.


## S05 hiện tại · album v5 / pilot r1

Người dùng đã duyệt frame album v5 và yêu cầu dựng pilot. MP4 hiện tại: `revisions/S05-album-pilot-v5-r1/renders/pilot.mp4`; source cạnh đó. Mascot ngồi sau bàn, hai tay giữ đúng mép trang album ảnh nhà thật. Cuốn sổ đang mở được hạ phẳng dần để giới thiệu ảnh; ảnh luôn in trên giấy, không trở thành khối nhà. Kết bám frame v5 đã duyệt. Bản chuyển động đang chờ duyệt; voice giữ nguyên, S09 r1 giữ nguyên. Các hướng nhà giấy/phố trước đây là lịch sử, không dùng để thi công tiếp. CREDITS.md/.json trong revision lưu nguồn ảnh và license.
