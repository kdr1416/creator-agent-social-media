# S13/S14 motion R1

720×1280 @30fps. S13:137 frames/4.566667s, voice4.553208333333s. S14:206 frames/6.866667s, voice6.855625s. S13 giữ WAV seg15 nguyên file; S14 nối nguyên PCM seg16+17, không trim/time-stretch/TTS. Khi ghép theo lưới frame chung, tránh cộng phần hold lẻ từng pilot độc lập.

S13: student/campus shot rồi cut2.32s sang property shot. Hai site trong một camera wrapper; origin được set đúng một lần lúc node còn identity, trước pan/scale. From(94,-250,scale1.4) to(0,0,scale1) trong3.0–4.03s. Viewport620→720 có clip; phần world ngoài viewport là intentional overflow. Giữ modal CÓ THỂ và nhãn MALTA ở overlay root để không bị cắt chữ. Hai endpoint lossless so với PNG đã duyệt đều MAE0. Không thêm svgOrigin vào cả from/to sau khi translate đã áp dụng — sẽ tạo offset sai.

S14: key được trình ra bằng tay cùng rig, cut3.8s sang ngã rẽ. Gate mở4.32–5.82s quanh bản lề[(570,700),(570,900)]. Phép chiếu x=570-d*cos(theta), y=y0+k*d*sin(theta), k=24/(130*sin120deg), theta0→120deg. Panel, bars và handle dùng cùng phép chiếu; chiều cao luôn200. Các keyframe thuộc tính nhìn thấy được được tính trước theo lưới30fps, không onUpdate/clock. Thân mẹ đi cùng handle, vai giữ trong placement-space; grip local quy về cùng world point. Điểm cuối rigid handle(622.5,779.3846) lệch frame phác tay(625,780) dưới3px để bảo toàn hình cứng. Hai lối giữ mở tới hết voice.

One paused GSAP timeline/root mỗi scene. Source, fonts, runtime và WAV local. Giữ source/frame design-r1 nguyên hash. Các pilot S01/S09/S07/S08/S06/S11/S10/S12 đã duyệt và master cũ không đổi. Motion hai clip mới chưa duyệt.
