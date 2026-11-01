# S02 pilot R1 — QA

- 720×1280 @30fps, 116frames, hình 3.866667s; source voice 3.855500000000s / 92532samples@24kHz.
- Voice WAV nguyên file, PCM đối chiếu đúng source toàn phim [144466,236998); không TTS/retime. AAC decoded correlation 0.999919. Phần hình lẻ cuối làm tròn lên1frame, không cắt voice.
- HyperFrames check: pass; không lint warning. Snapshot đầu/giữa/cuối, các xu tiếp xúc và nhịp thước/chữ; qa/ trích trực tiếp từ MP4 cuối. Có bản360×640 và grayscale.
- Các pilot đã duyệt trước, frame S02 R1 và master/clean cũ giữ nguyên hash.
- Browser playback: observed ended at3.87s in IAB. Motion chờ người dùng duyệt; không thay master.

Final audio: original WAV encoded directly to AAC192kbps/24kHz mono; native automatic gain bypassed. Final source snapshot pixel-identical to approved frame (ImageChops bbox None). Master assembly manifest unchanged.
