# S05 zoom pilot R1 — QA

- 720×1280 @30fps, 172frames, hình 5.733333s; source voice 5.706333333333s / 136952samples@24kHz.
- Voice WAV nguyên file, PCM đối chiếu đúng source toàn phim [435629,572581); không TTS/retime. AAC decoded correlation 0.999943. Phần hình lẻ cuối làm tròn lên1frame, không cắt voice.
- HyperFrames check: pass; không lint warning. Snapshot zoom đầu/giữa/cuối, contact–release và cut; qa/ trích trực tiếp từ MP4 cuối. Có bản360×640 và grayscale.
- 10pilot đã duyệt trước,4frame R2 và master/clean cũ giữ nguyên hash.
- Browser playback: đã quan sát bản MP4 cuối phát hết5.73s trong IAB. Pilot đã được chọn ghép master mới theo yêu cầu người dùng; xem APPROVAL.json. Master cũ giữ nguyên.

Final audio mux uses original WAV directly to AAC; native automatic gain bypassed. Final grip stays in front of pin throughout release.
