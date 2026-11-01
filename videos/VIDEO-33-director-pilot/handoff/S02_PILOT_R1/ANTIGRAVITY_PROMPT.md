# Antigravity — pilot S02 mới

Project: `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot`
Bản cần lấy: **S02-approved-frame-motion-r1**.
Folder source/asset/font/voice/MP4: `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\revisions\S02-approved-frame-motion-r1`
MP4: `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\revisions\S02-approved-frame-motion-r1\renders\pilot.mp4`
SHA-256: `d4dd9e8e46b788c0eff89f333fc8a0b54c259fce1a09afdff4eb3e7a9fde63f3`
Source editable: index.html + layered-art.svg; assets/ chứa font, GSAP và voice.wav. Đọc DIRECTION.json, README.md và QA_REPORT.md trong cùng folder. Voice92532samples@24kHz, global[144466,236998),3.8555s. MP4 hình116frames/3.866667s720×1280@30fps. Không lấy thư mục S02-motion-r1 hoặc build/scenes/S02 thay cho bản mới này.

Người dùng đã duyệt frame S02-design-r1 và yêu cầu dựng pilot. Pilot đã render/check/playback xong; chưa có xác nhận riêng duyệt motion trong hồ sơ hiện tại. Giữ trạng thái này trung thực khi tiếp nhận, không tự ghi full-master approved. Gói này bàn giao nguồn và phiên bản mới; chưa tự cập nhật manifest ghép master.

Khi phiên bản S02 này được chọn thay vào master, dùng hướng dẫn toàn phim ở `D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\handoff\MASTER_APPROVED_ASSEMBLY_R1\ANTIGRAVITY_PROMPT.md` và thay đúng entry S02, lưu manifest phiên bản mới. Khung master S02 là[181,296),115frames: bỏ1frame hold cuối của pilot116frames, không cắt động tác. Bỏ audio pilot khi ghép; dùng source_audio.wav xuyên suốt75.16s từt0, giữ nguyên voice. Không normalize/TTS/time-stretch. Giữ các pilot/cảnh khác và master cũ. Xuất master riêng rồi review seam S01→S02→S03 và full-film sync. Không tự redesign các lớp, chữ hoặc motion đã được người dùng chọn.
