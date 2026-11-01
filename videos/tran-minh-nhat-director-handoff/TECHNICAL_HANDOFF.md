# Handoff kỹ thuật — hình và voice

## Dữ liệu thời gian

Nguồn voice: inputs/full_voice.wav, monoPCM16,24000Hz,1636800samples,68.2s.17lát trong inputs/audio/ là bản copy nguyên file từ PhaseA; hash ở inputs/audio_manifest.json. Raw ASR và corrected_text tách riêng; không sửa lại lời đọc để cứu timing hoạt ảnh.

Các cue trong packet là phân nhịp đạo diễn ước lượng, không phải word alignment. Nghe lát gốc để dời mốc hoạt ảnh trong cảnh, giữ thứ tự ý/hành động. Khi beat quá ngắn, bớt chi tiết phụ thay vì kéo voice.

## Picture grid chung ở30fps

Dùng planning/picture_frame_plan.json hoặc.csv. Mỗi ranh giới hình được tính trực tiếp từ sample gốc: nearest frame, half-up. Tổng2046frames =68.2s. Không cộng các duration đã làm tròn trong từng MP4.

Ba pilot copy là bản xem có audio:04=181frames,06=156frames,12=133frames. Slot hình chung của04 cần180frames,06 cần156,12 cần133. Với04 chỉ lấy180frames hình đầu; không cắt/thay WAV theo clip đó. Đây là xử lý grid hình, không phải sửa nội dung pilot hay cắt câu thoại.

Các cảnh mới có thể dựng theo đúng duration voice rồi lấy/giữ frame cuối cho slot hình chung; lệch grid dưới1frame. Đừng time-stretch voice. Ưu tiên dựng toàn bộ host có mốc frame global, hoặc normalize từng picture clip theo bảng rồi concat picture-only.

## Audio cuối phim

Ghép hình trước, mute audio trong mọi clip/pilot/subcomposition ở bản assembly phái sinh. Sau đó đặt đúng một track inputs/full_voice.wav từt=0; không ghép17AAC đã mã hoá để tránh pad/drift và không để audio pilot phát chồng. Không ghi đè source pilot để bỏ audio; tạo bản phái sinh trong build/.

Không tự thêm nhạc/SFX/TTS/phụ đề trong lượt dựng này. Footer200px vẫn chừa cho pipeline sau. Encode AAC khi xuất MP4 là bình thường; giữ nguyên WAV và không lọc/đổi tốc độ giọng.

## Nguồn và namespace

Mỗi cảnh một composition có root/data-duration và timeline paused, seek-safe; prefix ID của cảnh mới để không đụng rig/host khác. Assets/font/runtime local trong composition hoặc copy từ library; mọi file render/derived nằm dưới build/.

Reference nguồn có audio và CSS/JS riêng. Khi port vào subcomposition, giữ style/script trong template theo HyperFrames contract; đừng chỉ copy body rồi làm rơi font/timeline. Không cần chuyển framework hoặc gọi Flow cho các cảnhHF_ONLY đã khoá. Antigravity đọc skill core/CLI của môi trường trước khi viết composition.

Chưa có code assembly17cảnh trong gói, chưa chạy render14cảnh. Không coi file kế hoạch là kiểm thử renderer đã pass.

## Pilot04 có một bước dọn kỹ thuật đã biết

Bản04gốc vẫn có dòng Hình minh hoạ ở selector #illustration-note. Trước assembly, tạo copy trong build/, bỏ đúng node này và audio, render picture theo grid180frames. Không cắt/crop đáy để che chữ và không sửa source frozen.06v4/12v6 đã bỏ các dòng đó. Kế hoạch này thiết kế14cảnh mới;04 cần tái xuất kỹ thuật từ nguồn sạch, không thiết kế lại cảnh. Chi tiết: planning/pilot04_assembly_cleanup.json.
