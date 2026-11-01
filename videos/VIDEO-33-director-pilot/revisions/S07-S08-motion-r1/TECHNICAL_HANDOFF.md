# Bàn giao kỹ thuật S07/S08 motion R1

720×1280, 30fps. S07: 141 frames / 4.700s; voice 4.668833333333s. S08: 165 frames / 5.500s; voice 5.477125s. Voice WAV copy nguyên file; MP4 encode AAC. Chỉ phần đuôi hình giữ thêm dưới một frame để khớp grid. DIRECTION.json giữ sample bounds, raw transcript và corrected text tách biệt.

Một paused GSAP timeline root cho mỗi scene. S07 dùng một SVG với hai lớp screen, rig vai cố định, path và hand tween cùng điểm. S08 dùng một shot arrival có wrapper di chuyển chung parent+vali và ba shot hoạt động cắt đúng cue. Không animate tọa độ placement bằng offset tuyệt đối nhỏ. Trạng thái ẩn ban đầu đặt CSS để frame0 đúng.

File PNG design-r1 là mốc đã duyệt; motion-r1 chưa được người dùng duyệt. Sau khi được duyệt mới thay vào bản master theo sample timeline, không concat hai pilot độc lập mà bỏ qua grid làm tròn. Không thay hai pilot S01/S09 đã duyệt.
