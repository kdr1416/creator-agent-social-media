# VIDEO-33 · Bàn giao đạo diễn

Mở REVIEW.html để xem 3 MP4; xem STORYBOARD.html cho chuỗi 14 khung và STORYBOARD.md/.json cho đặc tả toàn phim. Đọc DIRECTOR_BRIEF.md → CONTINUITY.md → RESEARCH.md → ASSET_PLAN.md → packet scenes/Sxx → TECHNICAL_HANDOFF.md.

Đã hoàn thành phạm vi storyboard + 3 pilot, chờ người dùng duyệt. 11 cảnh còn lại chỉ thiết kế. Không dựng full hoặc xuất bản tự động. Người dùng đã xác minh text “3.8 tỷ” cho S10; điểm chờ số tiền đã được gỡ. Storyboard/pilot vẫn chờ duyệt.

MP4: pilots/S01/renders/pilot.mp4, pilots/S05/renders/pilot.mp4, pilots/S09/renders/pilot.mp4. Editable source cạnh từng render. Source audio + raw/timing nằm trong inputs/ và được hash bảo toàn.

Minh chứng: qa/PILOT_OVERVIEW.jpg, qa/ALL_FRAME_PROOFS.jpg, qa/REFERENCE_COMPARISON.jpg, qa/GRAYSCALE_THUMBNAIL.png, qa/media-verification.json.


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
