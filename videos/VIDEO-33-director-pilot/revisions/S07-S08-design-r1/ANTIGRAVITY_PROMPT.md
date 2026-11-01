# Antigravity — motion thử S07/S08 từ frame R1 đã duyệt

Người dùng duyệt bộ frame S07-S08-design-r1 ngày 27/10/2026: “oke duyệt cái này”. APPROVAL.json khóa đúng 8 PNG bằng SHA-256. Chỉ frame/tạo hình/bố cục và hướng hành động được duyệt; motion và bản master mới chưa duyệt. Các đề xuất cảnh khác trong REMAINING_SCENE_PLAN.md chưa được duyệt.

Đọc DIRECTION.md, frame_inventory.json, các index.html/layered-art.svg tương ứng. Giữ nguyên hình đã duyệt; không dùng bản S07/S08 trong build làm nền rồi vá lại. Các index.html ở đây là pose tĩnh, mỗi file 1 giây phục vụ snapshot, không phải timeline sản xuất để nối nguyên clip.

Voice gốc 24kHz, không TTS/time-stretch, không thay raw transcript/sample timing:
- S07: 4.668833333333s, global samples [711699,823751), source ../../inputs/audio/seg_07.wav.
- S08: 5.477125000000s, global samples [823751,955202), source ../../inputs/audio/seg_08.wav.

S07: cùng bố cục laptop lớn/người thân lớn, mascot chạm nút gọi → màn hình kết nối → thu tay và vẫy đáp lại. Giữ quan hệ vai–tay, không đưa cáp vào lại. Các mốc DIRECTION.md là gợi ý, phải đối chiếu WAV.

S08: giữ phụ huynh tóc tím than/áo mint/quần tím, toàn thân và tỷ lệ lớn đã duyệt. Vali chạm sàn, cần kéo dính bàn tay. Gặp/chào con rồi các shot học tập, sinh sống, làm việc thay lần lượt đúng voice; không ghép ba icon nhỏ trở lại. Không dùng nhún toàn nhân vật để thay nội dung.

Hướng dẫn rig: node placement giữ translation/scale authored; travel dùng wrapper riêng bắt đầu từ 0. Vai không dịch khỏi thân; điều khiển khuỷu/cổ tay bằng cùng chain. Khi cầm prop, grip tính cùng hệ tọa độ; khi nhả chuyển quyền neo rõ ràng. Không tween y:-6 lên node có translate y680/730. Nội suy pose cần kiểm riêng, không suy ra frame đẹp là motion đúng.

Xuất trong folder revision mới riêng, không ghi đè frame đã duyệt, hai pilot S01/S09, voice hay master hiện tại. Bàn giao MP4 riêng S07/S08 có voice gốc, source editable, asset/font local và báo cáo QA. Kiểm contact quanh event ở 10–12fps; xem opening/mid/final, 360×640 và playback liên tục. Dừng để người dùng duyệt hai pilot; chưa thay master hay triển khai các hướng cảnh khác.
