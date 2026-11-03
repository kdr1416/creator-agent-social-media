# QA — Pilot scene 8

Trạng thái: pilot HTML draft, chưa duyệt, chưa render MP4.

## Kiểm tra đã làm

- [x] Scene contract JSON hợp lệ, timeline 42.4s - 48.6s, 6.2 giây.
- [x] Render mode HF_ONLY, signature motion duy nhất là page-turn kết hợp đặt vật thể.
- [x] Visible text: headline cộng 3 mốc, tối đa 8 từ/mốc, không transcript.
- [x] Thứ tự lớp: ambient glow -> bàn -> vật thể -> lịch -> nhân vật -> headline.
- [x] Vùng an toàn top 120px, bottom 200px, hai bên 50px.

## Kiểm tra chưa làm, cần Tuan và HyperFrames CLI

- [ ] Xem pilot HTML trong trình duyệt, duyệt từng khung opening, transformation, final.
- [ ] Kiểm tra dấu tiếng Việt trên headline thật ở kích thước mobile.
- [ ] Render MP4 bằng HyperFrames CLI đã cài, kiểm tra frame count, kích thước 720x1280, FPS theo manifest.
- [ ] Kiểm tra đồng bộ audio thật, vì pilot HTML hiện tại chưa gắn audio master.
- [ ] Duyệt bằng văn bản và ghi vào production_status.json. Nhận xét "tương đối ổn" không tính là duyệt.
