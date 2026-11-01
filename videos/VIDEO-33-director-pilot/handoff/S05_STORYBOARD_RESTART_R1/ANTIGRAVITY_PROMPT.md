# Antigravity — dựng pilot S05 theo storyboard R1 đã duyệt

Người dùng đã duyệt storyboard S05_STORYBOARD_RESTART_R1 bằng lời “oke duyệt”. Dựng riêng pilot S05 để người dùng xem tiếp. Chưa dựng full phim.

Đọc S05_STORYBOARD.md/.json và ASSET_PLAN.json trong folder này. Ý đã khóa: mascot đặt ghim lên Malta trên bản đồ; tới “bất động sản”, cắt thẳng sang ảnh lớn mặt tiền nhà thật ở Malta. Giữ hai shot tách rõ. Không dùng album v5, nhà giấy, morph nhà hoặc các pilot S05 lịch sử làm mẫu hiện hành.

Voice: ../../inputs/audio/seg_05.wav, 24kHz, 136952 samples, 5.706333333s. Global [435629,572581). Giữ raw transcript, sample timing và voice; không TTS hay time-stretch. Cut dự kiến local 4.35s theo ASR; đối chiếu voice để chỉnh cue, không sửa ranh giới audio.

Engine HF_ONLY, 720×1280, 30fps. Mascot cam bo góc/mũ tím/ba lô xanh; tiếp xúc ghim rồi nhả tay, không kéo dài tay. Nền kem/đào/xanh nhạt, nét mảnh. Một nhãn MALTA, font ../../assets/fonts/segoe-ui-black.ttf. Footer y1080–1280 sạch. Map phải có nguồn địa lý; ảnh phải là nhà ở Malta, đủ giấy phép và credit. ../../assets/townhouse.jpg chỉ là ứng viên; chọn crop rõ cửa và ban công, không bắt buộc giữ ảnh này.

Hai pilot đã duyệt: S01 bản đầu và S09 motion r1; file/hash trong APPROVED_PILOTS.json. Bản S05 mới chỉ được duyệt storyboard, chưa duyệt frame/motion. Có thể chỉnh crop, pose, easing, sắc độ và cue nhỏ để thi công; giữ ý trung tâm và các must_keep trong JSON.

Xuất vào folder revision mới. Bàn giao editable source, asset nhiều lớp, local font, credits và MP4 có voice gốc. Kiểm opening, tiếp xúc ghim, trước/sau cut, final; 360×640, thumbnail, grayscale, font và playback; kiểm hash voice/timing. Ghi kết quả thực tế và giới hạn QA. Dừng ở pilot S05 để người dùng duyệt.
