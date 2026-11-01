# Bàn Giao Kỹ Thuật Audio — Handoff To Codex & Đạo Diễn `[VIDEO-33]`

## 1. Thông Tin Tổng Quan Bàn Giao

- **Tên Dự Án**: `[VIDEO-33]`
- **Thư Mục Dự Án Riêng Biệt**: `videos/VIDEO-33/` (Cách ly hoàn toàn, không đè bất kỳ workflow hay dữ liệu sẵn có).
- **Trạng Thái Hiện Tại**: `audio_ready_for_direction` (Hoàn thành Phase A: Phân tích audio & transcript chuẩn xác).
- **Quy Tắc Thực Hiện**: Giữ nguyên vẹn 100% audio gốc (không can thiệp pitch, speed, EQ, TTS hay cắt khoảng nghỉ làm lệch duration).

## 2. Đường Dẫn Đầu Vào & Cấu Trúc Bàn Giao

```
videos/VIDEO-33/
├── audio_handoff.json       # Metadata kỹ thuật, checksum và danh sách 17 lát audio
├── transcript.json          # Transcript chuẩn máy đọc gồm raw_text, corrected_text, timing, sample bounds
├── transcript.md            # Bảng chi tiết đối chiếu transcript, uncertainties và fact-check table
├── production_status.json   # Trạng thái dự án: audio_ready_for_direction
├── HANDOFF_TO_CODEX.md     # Tài liệu bàn giao này cho Codex và Đạo diễn
├── inputs/
│   └── source_audio.wav     # Bản copy nguyên vẹn bit-for-bit từ file audio gốc
└── audio_slices/            # 17 lát audio cắt chuẩn zero-crossing (seg_01.wav -> seg_17.wav)
```

## 3. Các Điểm Kỹ Thuật Đã Được Kiểm Tra & Chứng Minh

1. **Sample Contiguity (Tính nối liền tuyệt đối)**:
   - Toàn bộ 17 đoạn được nối tiếp liên tục: `start_sample[0] = 0`, `start_sample[i] = end_sample[i-1]`, `end_sample[16] = 1803840`.
   - Không mất mát và không trùng lặp dù chỉ 1 sample.
2. **Zero-Crossing Cut Points**:
   - Mọi lát cắt đều nằm ở khoảng nghỉ tự nhiên và được tối ưu tại điểm `amp = 0` (zero-crossing), triệt tiêu hoàn toàn tiếng lách cách (click/pop) ở đầu/cuối lát audio.
3. **PCM Reassembly Bit-for-bit Match**:
   - Ghép 17 lát PCM lại bằng code tạo ra chuỗi byte chính xác 100% so với file WAV gốc.
   - Source PCM SHA-256: `80e095d3d1f20219de642dec538560a51aadf97fec1493f59524da228b5e0e00`
   - Reconstructed PCM SHA-256: `80e095d3d1f20219de642dec538560a51aadf97fec1493f59524da228b5e0e00`

## 4. Những Điểm Lưu Ý Quan Trọng Cho Codex / Đạo Diễn

### Lưu Ý 1: File Script Tham Chiếu Ban Đầu Rỗng
- Đường dẫn người dùng chỉ định: `scratch/video 33.txt` có dung lượng **0 bytes**.
- Do đó, transcript được nhận dạng bằng ASR đa tầng (Whisper Small + Domain Initial Prompt), kết hợp thẩm âm chi tiết trên từng waveform.
- Đã phân tách rành mạch `raw_text` (âm nhận dạng thô) và `corrected_text` (bản chuẩn hoá sau đối chiếu thuật ngữ chuyên ngành).

### Lưu Ý 2: Các Điểm Fact-Check Trọng Yếu Cần Thẩm Định Trước Khi Lên Visual
1. **Số liệu 'Khoảng 3,8 tỷ đồng' (Seg 11)**:
   - Đây là chi phí ước tính tham gia chương trình Thẻ Xanh Malta (MPRP) theo diện thuê bất động sản (~140.000 - 150.000 EUR gồm thuê BĐS 5 năm + phí đóng CP 98k€ + từ thiện 2k€ + phí hành chính).
   - *Khuyến nghị*: Không hiển thị con số cố định tuyệt đối trên màn hình mà kèm chữ 'Từ khoảng ~3,8 tỷ VND*' kèm chú thích điều kiện thuê.
2. **Chính sách 'Định cư 4 thế hệ' (Seg 11)**:
   - MPRP cho phép đi kèm 4 thế hệ: đương đơn, con cái, cha mẹ hai bên, ông bà hai bên (điều kiện con trưởng thành độc thân và cha mẹ/ông bà phụ thuộc tài chính).
   - *Khuyến nghị*: Đồ họa gia phả / tree chart trực quan hóa 4 thế hệ rất đắt giá và đúng luật di trú Malta.
3. **Từ mở đầu 'Trước nhiều phụ huynh...' (Seg 02)**:
   - Audio phát âm rõ chữ 'Trước'. Nếu Đạo diễn thấy câu văn cần chỉnh ngữ pháp có thể để text overlay là `Trước thực tế nhiều phụ huynh sẵn sàng chi hàng tỷ đồng...` hoặc giữ nguyên phụ đề theo voice.
4. **Từ 'con cái' vs 'con gái' (Seg 13)**:
   - Audio phát âm lướt âm cuối; nếu video là explainer chung thì text nên là `con cái`; nếu là câu chuyện thương hiệu riêng có thể là `con gái`.

### Lưu Ý 3: Hướng Dẫn Routing & Storyboarding Tiếp Theo
- 17 đoạn ý trên là đơn vị nội dung logic và mốc nhịp tự nhiên của người nói. Đạo diễn có thể:
  - Giữ nguyên 17 cảnh (mỗi cảnh từ 2.5s - 6.2s, rất lý tưởng cho Veo 3 / HyperFrames).
  - Hoặc gộp các đoạn ngắn có cùng bối cảnh thị giác (ví dụ Seg 09 + Seg 10 thành 1 cảnh 7.45s về 'Đa dạng hóa danh mục đầu tư thay vì phụ thuộc 1 quốc gia').
- Tuyệt đối tuân thủ quy tắc Flow Kit & HyperFrames:
  - Zero-text trên video plate của Flow (không prompt chữ trên Veo 3).
  - Không dùng card chữ đóng hộp che phủ toàn bộ video.
  - Chừa trống footer 180 - 200px cho subtitle.

---
*Báo cáo bàn giao được khởi tạo tự động bởi Antigravity vào lúc 2026-10-26T18:35:00+07:00.*
