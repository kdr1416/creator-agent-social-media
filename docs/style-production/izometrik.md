# `izometrik` — Spatial illustration production playbook

[A/P] Hướng dẫn dựng nguyên gốc, đọc cùng [shared production](SHARED-PRODUCTION.md). [U] Repo tham khảo có projection thật, face primitives, room/tile assembly và camera tính từ t; [O] đã xem frame chuỗi của clip. Không suy đây là hệ 3D camera tùy ý hoặc mẫu campus có sẵn. [Audit/source](RESEARCH-AUDIT.md).

## 1. Style Identity

Isometric là tổ chức không gian bằng một phép chiếu song song nhất quán. Các trục world có hướng screen cố định, scale không nhỏ dần theo khoảng cách như perspective. Nhìn được quan hệ mặt sàn–khối đứng–đường đi, object gắn lên mặt và khoảng trống giữa chúng. Depth đến từ geometry/overlap/shading, không phải chỉ xoay rectangle thành diamond.

Chọn isometric khi cần đọc vị trí, cấu trúc hoặc thay đổi của một hệ thống; cũng có thể làm lifestyle nhưng đừng đánh đổi cảm xúc thành mô hình quá xa. Một close-up nghiêng của con người không cần ép thành isometric chỉ vì kiến trúc trước đó dùng phép chiếu này.

## 2. Art Direction Recipe

### Color, light và material

Xác lập trường nền nhẹ nhàng để platform/world nổi, nhưng không mặc định beige. Chọn một nhóm hue môi trường, một nhóm hue vật liệu và accent theo chức năng. Example spatial learning scene: cool near-white field, muted blue structure, warmer wood/desaturated stone, coral object đang hoạt động. Primary/secondary chỉ ra vùng chức năng, không mỗi tòa nhà một rainbow hue.

Mỗi material có base/top/side/shadow role. Top thường sáng hơn nếu light từ trên, hai side khác nhau theo hướng sáng đã chọn. Giữ thứ tự value cho cùng hướng mặt giữa mọi building; không auto top sáng ở một khối nhưng tối ở khối bên cạnh mà không có lý do lighting. Bóng không chỉ darken bằng đen: tint theo ambient/project palette, contact shadow sát chân vật đậm hơn cast shadow xa. Highlight bevel ở cạnh gần có thể giúp đọc độ dày, không cần viền sáng mọi cạnh.

Saturation gom vào active area; xa/secondary có thể giảm saturation và contrast có kiểm soát. Muốn modern spatial ad, dùng neutral sạch và shadow cool, warm chỉ ở vật liệu/ánh nắng, bỏ paper wash nếu brief không vintage. Isometric hoàn toàn có thể rực rỡ: hierarchy nằm ở diện tích/value/semantic grouping chứ không số lượng hue ít tuyệt đối.

### Construction, detail và composition

World blockout trước: footprint, cao độ sàn, kích thước các khối, khoảng cách đi lại, orientation. Sau đó thêm openings vào đúng wall plane, mái/ledge có thickness, furniture có legs và support. Những chi tiết cửa sổ/books/tiles gắn vào world face, không dán screen-space tùy ý. Đường cong/path cũng xuất phát từ world points rồi project. Texture theo material và direction; không phủ grain để làm “mô hình”.

Focal mass là active room/building, secondary là context, negative space để labels và camera breathing room. Chừa khoảng mở ở phía nhìn vào căn phòng; cutaway wall chỉ bỏ mặt cần mở, giữ đủ thickness để người xem đọc enclosure. Vật lớn sát camera có thể che activity; dùng wall cutaway hoặc staging khác, không làm người xuyên tường.

Dọc 9:16: tổ chức depth theo chiều cao khung nhưng không xếp city thành danh sách tầng. Dùng một khu vực hoạt động lớn, context được cắt có chủ ý. Pull-back không được biến main action thành pixel nhỏ; nếu cần hệ nhiều node, tách attention qua shots trong cùng duration thay vì chỉ thu nhỏ. Essential labels thường để screen-space ngang; chữ in trên façade có thể affine với plane nhưng phải chứng minh đọc được ở mobile.

## 3. Asset Construction Recipe

Chọn world units; đồ vật lưu x/y/z và dimensions trước projection. Hệ phép chiếu đề xuất (có thể dùng convention khác nếu project ghi rõ):

```js
// s = screen pixels per projected world unit; positive Z is up.
const project = (x, y, z, s, ox, oy) => [
  ox + s * Math.cos(Math.PI / 6) * (x - y),
  oy + s * (0.5 * (x + y) - z)
];
```

Ba world unit axes có projected length bằng s, trục mặt đất ±30° so với ngang và z thẳng đứng. Công thức trên đủ để dựng 2D isometric; không cần Three.js. Với box, project 8 vertices; dựng các mặt visible từ vertices dùng chung, tránh khe hở do tính từng mặt khác rounding. Mái có độ dày, cửa dùng origin+u+v trên plane. Circle trên sàn là ellipse từ project các điểm vòng tròn, không tự chọn rx/ry nhìn có vẻ đúng.

```text
iso-camera-placement
  iso-world-motion
    platform (top / sides / contact-shadow)
    building-back (walls / openings / roof-edge)
    furniture-far
    actor-placement (pose groups)
    furniture-near / rail-front
    cast-shadows
screen-labels (label-placement / mask / text-motion)
```

Painter order là quyết định visibility, không chỉ Z-index theo tên. Với khối không giao nhau, sort theo depth convention và kiểm thực tế; `x+y` đơn giản không đủ cho mọi extent và vật cắt nhau. Tách wall/rail thành near/far groups khi cần actor đi giữa, hoặc dùng masks cố định từ geometry. Không tuyên bố depth sort tổng quát từ một heuristic.

Reusable objects nhận dimensions/material/orientation, xuất points/faces/anchor points. Anchor gồm foot location, chair seat, handle, tabletop và light plane. Semantic IDs như `s08-desk-top`, `s08-laptop-lid`, `s08-chair-seat` giúp contact và audit. Defs scene-prefixed. SVG `<g>` điều khiển một rigid prop khi whole prop di chuyển; nếu world geometry đổi orientation, tính lại faces đúng phương pháp, không xoay polygon đã project để giả 3D rotation.

## 4. Motion Construction Recipe

### World motion và camera

Lắp ráp công trình theo structural dependency: platform → support → wall/roof → furniture, không thả props xuyên mái. Object drop cần world z cùng shadow height/opacity tương ứng; impact nhỏ có thể có settle nếu mass/brief hợp. Đường đi actor ở world x/y, feet luôn ở ground z. Elevator/layer separation dùng world z, không screen y tùy tiện làm lệch trục.

Camera pan/zoom là thay ox/oy/s chung hoặc parent group transform đồng nhất. Isometric orthographic không có perspective scale theo depth. Nếu chuyển góc nhìn thật, phải tính toàn bộ projection của vertices cùng lúc; không skew từng asset riêng. Không gọi zoom+pan là orbit. Cấu trúc đã dựng theo fixed projection nên dùng reframe; một camera orbit không cần thiết có thể phá technical clarity.

Exploded view có khoảng nghỉ cho mắt đọc quan hệ; connect line chỉ ra module gốc, không trôi tự do. Layers trở về đúng anchor. Parallax fake giữa các mặt của một rigid building làm geometry rách; chỉ dùng giữa các plane/background có lý do ngoài rigid world.

### Characters nếu cần

Figure isometric phải đặt feet trên cùng plane, head/body orientation đồng thuận với path. Không scale figure theo y-screen như perspective trong cùng iso world. Pose nhìn three-quarter có far/near limb, hand contact theo world props. Với close emotional acting, có thể cut sang illustrated medium shot cùng palette/character family; ghi scene treatment change, không đổi projection nửa khuôn mặt.

Walk/run/contact dùng các pose constraints ở Kurzgesagt playbook nhưng project ground targets vào mặt phẳng. Run phải phân biệt flight, stance và lean. Tay mở cửa/tự vịn lan can phải có support target; shadow không di chuyển khỏi feet. Không cần đưa nhân vật vào diagram nếu một moving component đã kể rõ quy trình.

### Type, reveals và transition

Labels screen-space theo dõi projected anchor nếu world reframe; leader line không đổi nghĩa khi camera đổi. Reveal mái bằng mask/lift đúng world axis, không fade toàn building khi cần thấy nội thất. Spatial node có thể phóng thành single room; giữ orientation/anchor để mắt hiểu. Bauhaus word framing dùng palette này, không thay backdrop thành poster paper đột ngột.

## 5. Voice-to-Visual Mapping

Ví dụ không có số giây giả; mọi anchor K phải bind vào audio thật khi triển khai.

| Voice phrase | Main visual action | Text | Effect | Timing anchor |
|---|---|---|---|---|
| “các bộ phận cùng hoạt động” | Hai module kết nối qua đường world, active signal đi qua đúng junction | “Kết nối” nếu bổ sung nghĩa | Path draw trên cùng mặt sàn | K = onset “cùng”; preparation phụ thuộc scene, không gán timestamp tùy ý |
| “từ không gian làm việc đến sân hiên” | Reframe từ desk đến terrace trong cùng world | Một phrase duy nhất nếu cần | Wall opening/layer mask | K từ transcript thực tế; camera settle trước thời gian cần đọc |

Đường nối không được hàm ý quan hệ nhân quả/địa lý mà nội dung không có. City/campus tổng hợp phải ghi illustration composite nếu không dựa survey/map chính xác.

## 6. Technical Implementation

World-to-SVG có thể được tính một lần cho pose tĩnh; motion dọc z của rigid object trong fixed projection tương đương translate screen y = `-s*dz`, x/y world tương đương projected vector. Dùng tween x/y absolute của outer motion group để giữ faces rigid. Camera scale chung không cần regenerate vertices.

Nếu prop cần quay 3D hoặc thay topology/occlusion, precompute vertices per frame/pose từ pure projection và dùng engine adapter phù hợp; không thêm engine chỉ để quay một lid. SVG path attr tween hợp khi cùng topology, nhưng nội suy linear projected vertices giữa hai góc không tự mô phỏng rigid rotation. Nếu hinge quan trọng, tính pose samples từ angle rồi kiểm edge lengths/arc continuity. Giữ root finite duration và timeline registration như shared contract.

Một test hình học nhỏ có ích trong authoring: project ba unit axes, so length, slope; check vertices shared trùng nhau; dựng world grid tạm rồi tắt khỏi output. Đây là kiểm construction, chưa phải visual acceptance. Đừng viết test mirror code để chứng minh ảnh đẹp.

## 7. Visual Quality Checklist

| Kiểm | Cách xem | Lỗi → cách sửa |
|---|---|---|
| Axis/scale | Overlay debug axes và parallel edges ở toàn khung | Buildings có slopes khác → dùng một project() cho tất cả |
| Surface attachment | Theo dõi window/table/feet trong reframe | Detail nổi khỏi plane → anchor theo face basis/world coords |
| Thickness | Crop mái/ban công/platform gần focus | Paper-thin building → thêm mặt cạnh có thickness phù hợp |
| Lighting | So các mặt cùng orientation và shadows | Mỗi object một light → gán lại material face roles |
| Occlusion | Midpoint lúc actor qua rail/door | Xuyên tường/đồ đè tay → tách near/far/mask hoặc đổi staging |
| Camera | Extreme crop, pull-back mobile | Main action quá bé → giảm context hoặc tách shot |
| Text | 360px-wide proof với leaders | Label quá chéo/nhỏ → screen-space essential type |
| Seek/motion | Seek shuffle và playback sau duyệt | Assembly phụ thuộc lần đã chạy → finite absolute timeline/state |

## 8. Anti-Patterns theo ngữ cảnh

Diamond floor không tự sai, nhưng floor + các rectangle vẽ theo ý tạo spatial inconsistency. Cũng cần tránh: same-value top/side làm khối phẳng; tất cả boxes drop cùng bounce; dùng pan để phô mô hình mà voice nói cảm xúc; city quá nhiều houses cùng detail; perspective vanishing point lẫn parallel projection; actor phóng lớn theo depth làm lệch scale; labels nhồi trên tất cả roofs; giả 3D orbit bằng skew toàn canvas. Những lựa chọn này chỉ bị loại khi làm mất quan hệ không gian/ý nghĩa, không là lệnh cấm mọi geometric simplification.

## 9. Practical Example — community learning space

Ví dụ nguyên gốc: một cutaway learning room nhìn cùng courtyard để giải thích kết nối hoạt động. Key visual active table ở trung tâm, rear wall có cửa sổ gắn đúng plane, courtyard bên phải, một người đặt model lên bàn; một người khác nhận gaze. Palette cool structure + warm table + một accent prop; không rainbow từng object.

Beats: platform đã có từ opening → wall cutaway lộ relationship table/courtyard → model lên bàn có hand support → camera mở ra vừa đủ thấy courtyard → một label “Kết nối” dẫn từ model đến hoạt động kế bên nếu voice yêu cầu. Không copy studio/tile map upstream. Triển khai fixed projection SVG, shared face vertices, near/far layers và timed type groups. QA axes/feet/chair height, model contact, overlap khi reveal, một focal ở mobile, labels không che tay. Timestamps phải lấy từ project; chưa render ví dụ này và chưa chứng minh smoothness.
