> **S05 R1 đã duyệt:** đặt ghim Malta → cắt sang ảnh nhà thật. Dùng [hướng dẫn Antigravity](handoff/S05_STORYBOARD_RESTART_R1/ANTIGRAVITY_PROMPT.md) để dựng pilot riêng. Chưa duyệt frame/motion S05 mới; không dựng full phim. Thông báo này thay trạng thái chờ duyệt S05 ở lịch sử bên dưới.

> **Cập nhật S05:** Album v5 không được duyệt. Mọi mô tả/hình S05 bên dưới là lịch sử và được thay bằng [storyboard viết lại R1](handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md), đang chờ duyệt. Hai pilot đã duyệt là S01 bản đầu + S09 motion r1. Chưa dựng frame/pilot mới hoặc full phim.

# Prompt bàn giao cho Antigravity

Tiếp nhận folder `videos/VIDEO-33-director-pilot/`. Trong trạng thái hiện tại chỉ đọc, kiểm tra và chuẩn bị sản xuất; đợi người dùng duyệt storyboard/pilot trước khi dựng 11 cảnh còn lại. Không coi sự tồn tại của prompt này là lệnh tự chạy full.

Đọc START_HERE.md, DIRECTOR_BRIEF.md, STORYBOARD.md/.json, CONTINUITY.md, ASSET_PLAN.md/.json, RESEARCH.md, TECHNICAL_HANDOFF.md, REVIEW_GUIDE.md và production_status.json. Sau đó đọc scenes/Sxx/PACKET.md cùng packet.json cho từng cảnh. Source audio/raw ASR/timing nằm trong inputs/; sample bounds là nguồn sự thật.

Khi người dùng đã duyệt sản xuất, bạn phụ trách tạo asset tách lớp/pose và dựng các cảnh chưa làm. Codex đã quyết định ý chính, hình chủ đạo, trạng thái đầu–biến đổi–kết, vai trò mascot và điểm chuyển cảnh. Không tự đoán lại nội dung từ một câu voice hoặc thay hình bằng stock icon/card. Chọn asset đúng asset_contract; ghi nguồn, license, checksum. Nếu thiếu asset chính, giữ ý thiết kế, báo vướng mắc cụ thể và làm cảnh độc lập khác.

Giữ: mascot cam bo góc/mũ tím/ba lô xanh; warm cream/peach/lilac + accents tươi, nét mảnh; voice gốc không sửa sample/pitch/speed/EQ; font Segoe UI Black full dấu; subtitle footer 200px; physical contact/semantic action; quan hệ hình và ý chính trong packet. Không ghi Hình minh hoạ hoặc Không gian minh hoạ lên video. Không tự thêm CTA, thành tích, nghề, giá, lợi nhuận, quyền visa/quốc tịch hoặc quyền làm việc EU.

Linh hoạt: cân khung, tỷ lệ vật thể, nếp giấy, số nét, pose/ánh mắt, easing và dời cue cử động bên trong cùng lát voice sau nghe đối chiếu. Cue đạo diễn không phải word-alignment. Nếu cần thay prop chủ đạo hoặc engine, ghi previous_mode/new_mode/routing_override_reason và lý do giữ nghĩa; không đổi âm thầm.

S01/S05/S09 có source editable, assets/fonts local và MP4. Giữ chúng như mốc review, không ghi đè khi sửa; tạo revision riêng. Khai thác ngữ pháp, không nhân bản nguyên cảnh sách/ảnh/ba bệ sang mọi đoạn. 11 cảnh còn lại chưa có asset/render dù packet đầy đủ. Không sửa dự án VIDEO-33 hoặc tran-minh-nhat-director-handoff, không đổi workflow chính.

S10: chủ nội dung đã xác minh text “3.8 tỷ”; gỡ điểm chờ xác minh về con số này và giữ voice gốc “khoảng 3,8 tỷ”. Xem research/user-confirmations.json để biết nguồn và phạm vi xác nhận. Không tự mở rộng thành giá mua nhà/tổng phí trọn gói hoặc đổi thiết kế sang hero metric. Các điều kiện MPRP về gia đình và quyền cư trú/lao động vẫn giữ theo packet. Xác nhận số liệu không đồng nghĩa đã duyệt storyboard/pilot hoặc cho phép dựng full.

QA mỗi cảnh: actual HyperFrames check; opening/signature-in-progress/final frames; playback voice gốc; mobile 360×640; font dấu; grayscale; tiếp xúc tay/đạo cụ; đủ thời gian kết. Film QA: không lặp visual meaning/action/layout, không card ngụy trang, không nhân vật mannequin, không mã hóa quyền lợi chưa xác minh. Assemble sau cùng theo global picture_frame_plan, một track full WAV duy nhất. Không nối AAC pilot để thay voice tổng.


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
