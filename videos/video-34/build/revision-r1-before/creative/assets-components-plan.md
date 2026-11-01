# VIDEO-34 — Assets & reusable components plan

Trạng thái: **kế hoạch, chưa tạo assets/animation mới**. Các ID dưới đây là định danh thiết kế, không phải đường dẫn file đang tồn tại. `assets/ledger.json` vẫn chỉ ghi tài nguyên thật; không thêm asset giả vào ledger.

## Inventory theo tính có thật

| ID | Nội dung / nơi dùng | Trạng thái, nguồn và reuse |
|---|---|---|
| BRAND-ESORA | Avatar cuối S17 | **Đã có:** `../assets/brand/esora-avatar-original.jpg`, giữ nguyên nguồn Facebook trong ledger và hash. Không sửa file. |
| MASTER-VOICE | Master 93,04s, cả phim | **Đã có:** WAV trong inputs, sha256 6b92d56bb90f3c4e702903d53d098d7c1765daf716879e8de60826a3110425c1. Chỉ tham chiếu. |
| ENV-MT-STREET | Đá vôi, cửa, ban công; S01/02/07 | **Planned illustration:** module kiến trúc tham chiếu Malta, không hứa tái tạo địa điểm chính xác. Recompose theo góc nhìn. |
| ENV-MT-COAST | Promenade/plaza/café/bay; S03, phần S10 | **Planned:** world layout liên tục cho S03; S10 lấy vật liệu/đường chân trời, không sao cả bố cục. Bãi biển là composite không gắn tọa độ. |
| ENV-VN-CAFE | Phin, bóng cây, góc bàn; S01/04/05 | **Planned:** dựng từ ngữ cảnh Việt Nam, không chép biển hiệu thương mại. |
| ENV-VN-PARK | Bờ sông/lối dạo; S05 | **Planned:** góc cao riêng, không recolor bờ biển S03. |
| ENV-HOME | Nhà/desk/terrace; S06/08/14 | **Planned:** sơ đồ không gian chung để cửa, ghế và vị trí trẻ không đổi vô lý. Góc crop khác nhau. |
| ENV-LEARNING | Trường và sân; S07/11/12 | **Planned:** không logo trường thật, không chứng chỉ/chất lượng bảo đảm. S11 ưu tiên props cận. |
| ENV-GARDEN | Cây thấp/đường khám phá; S09/12 | **Planned:** cây có cấu trúc, không số lượng icon cây tùy tiện; khu chơi an toàn chỉ là ngữ cảnh minh họa. |
| CHAR-FAMILY | Hai phụ huynh, trẻ; S06/08/11/14–17 | **Planned, casting pending:** model sheet trước asset acting. Reuse nhận diện, không reuse một cử chỉ cho mọi scene. |
| CHAR-RESIDENTS | Walkers/runner/café friends S01/03 | **Planned:** silhouette nhỏ, tách nhân vật chạy khỏi người đi bộ; không dựng full rig khi không cần. |
| CHAR-OLDER-ADULT | Người lớn tuổi S10 | **Planned/optional:** không gọi là người thụ hưởng chương trình đã được duyệt. |
| PROP-MUG-PHIN | Cốc, phin, bàn; S01/04/05/17 | **Planned:** cùng thiết kế vật thể nếu thuộc cùng gia đình; bố cục/phân vai khác. |
| PROP-HOME | Túi, laptop lid/base, ghế, bàn; S06/08/15 | **Planned:** pivot/ground plane cần xác định; S15 không lặp đóng laptop. |
| PROP-CHILD | Bức vẽ, bóng, cây quan sát; S09/11/12 | **Planned:** bức vẽ không phải certificate, bóng có tiếp xúc tay/đất. |
| PROP-CONSULT | Folder không chữ, ảnh gia đình; S13 | **Planned:** không passport/visa/thẻ cư trú giả, dấu chính phủ hay số tiền chưa kiểm chứng. |
| TYPE-VI | Font cho nhãn tùy chọn | **Chưa chọn file/license:** Be Vietnam Pro là candidate. Không tải dependency/font ở bước này. |
| TEXTURE-PAPER | Grain/vật liệu rất nhẹ | **Optional, chưa có:** chỉ thêm nếu pilot chứng minh có ích; ghi provenance khi có thật. |

Các tên mô tả cụ thể trong storyboard là biến thể của nhóm trên: `ENV-MT-COAST-PLAZA` thuộc `ENV-MT-COAST`; `ENV-MT-HOME` và `ENV-MT-HOME-WORK-TERRACE` thuộc `ENV-HOME`; `ENV-VN-PARK-RIVER` thuộc `ENV-VN-PARK`. Chúng không chỉ đến những file đã tồn tại hoặc yêu cầu tạo ba bộ nhà khác nhau.

Khi build được chỉ thị, minh họa có thể là SVG tự dựng/code-native; texture raster chỉ nếu cần. Mỗi file thực tế phải có nguồn, license/quyền dùng, hash và cảnh sử dụng trong ledger. Không dùng ảnh chân dung khách hàng hay stock có watermark. Mô tả vật thể bổ sung không có ID vẫn phải được ghi ledger nếu thành asset ngoài scene.

## Components theo hành vi — chưa triển khai code

| Component dự kiến | Input / output contract | Reuse và giới hạn |
|---|---|---|
| WorldStage | ViewBox, ground plane, camera viewport → nhóm tọa độ scene-local | S03/05 có topology khác; không một layout cho mọi scene. |
| ArchitectureModule | Cửa/ban công/vật liệu, perspective → illustration group | S01/02/07; tránh cùng facade nguyên vẹn ở mọi góc. |
| CharacterPose | Identity, pose, gaze, facing, contact points → SVG group | Chỉ tách joint cần dùng; không bắt scene nào cũng có rig. |
| WalkTravel | Distance, foot cycle, ground baseline, start/end → vị trí/pose seekable | S03/16; S16 cận cần profile riêng, không nhân tốc clip. |
| HandContact | Hai contact points, thời điểm chạm/rời → bàn tay và thân có quan hệ | S08/16; tính trạng thái từ thời gian scene, không tích lũy callback. |
| LaptopLid | Pivot, open/closed angle, interval → trạng thái nắp | Chỉ S08, có thể giữ module để tái dùng, không ép dùng lại. |
| AttentionReframe | Scene-local rectangle/scale, beat window → vùng nhìn | S03/07; không camera toàn phim hoặc state từ scene trước. |
| PropPlacement | Prop, support surface, contact shadow → nhóm có trọng lượng | Cốc/túi/bóng; bóng không dùng cùng physics giả cho cốc. |
| BrandSignature | Original JPEG, contain ratio, reveal interval → logo đầy đủ | S17; không mutate file, không tự thêm CTA. |

Mỗi component khi triển khai cần reset/seek cho ra cùng trạng thái tại cùng thời điểm. Dependencies dùng chung phải khai báo; việc sửa asset/component cần stale tracking theo cơ chế hiện có. Không xây agent orchestration hay framework mới. `components/motion.js` hiện có được bảo toàn; chưa khẳng định nó đã đáp ứng toàn bộ hợp đồng đề xuất này.

## Ưu tiên nếu được giao xây pilot

1. Review casting/mẫu hình gia đình và palette; kiểm tra font/nguồn nếu cần chữ.
2. S03: khóa sơ đồ world, 5 nhóm hành động, silhouette nhỏ rồi mới thêm kiến trúc. Đây là test spatial storytelling và điều phối nhiều chủ thể.
3. S08: khóa desk–chair–child contact map, pose đầu/cuối rồi mới animation. Đây là test acting và chuyển trạng thái cảm xúc.
4. Hai sample độc lập dùng đúng audio interval riêng; source/asset ở cùng video-34, preview không giả chúng liền nhau trong phim.
5. Chỉ sau chỉ thị riêng mới tạo source, assets và render; chỉ sau human approval thật mới tiếp tục production còn lại. Không ghi approval từ kế hoạch asset.

## Kiểm tra reuse

Reuse giúp giữ tỉ lệ, nét, vật liệu, identity và tọa độ nhà; **không** đồng nghĩa paste nguyên scene. Review mỗi shot theo silhouette, hành động và khoảng cách máy. Nếu một module buộc sai perspective hoặc biến S05 thành S03 recolor, vẽ biến thể phù hợp thay vì cố reuse. Chưa có kết quả runtime/render mới nào cho danh sách kế hoạch này.
