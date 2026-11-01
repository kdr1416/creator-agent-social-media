import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("scratch/voice_timeline.json", "r", encoding="utf-8") as f:
    tl = json.load(f)

scenes = tl["scenes"]

routing_data = [
    {
        "scene_number": 1,
        "start": 0.00,
        "end": 3.80,
        "duration": 3.80,
        "raw_text": "Dù học Australia nằm hồ sơ thì một bị tự chối vô giá.",
        "corrected_text": "DU HỌC AUSTRALIA: 5 HỒ SƠ THÌ 1 BỊ TỪ CHỐI VISA?",
        "semantic_type": "hook_question",
        "character": "no",
        "semantic_action": "None (Cảnh thuần dữ liệu/biểu tượng thống kê mở đầu. 5 cuốn hộ chiếu nan quạt tự động tách cụm và bị đóng dấu từ chối xung lực, không ép nhân vật đứng làm cảnh).",
        "visual_center": "5 biểu tượng hồ sơ hộ chiếu du học xếp vòng cung mở, hồ sơ thứ 5 bị đóng dấu từ chối đỏ chuyển động rung cảnh báo.",
        "organic_motion_need": "Không yêu cầu. Hành động mở đầu mang tính biểu tượng thống kê gây sốc (5:1 ratio).",
        "exact_graphics_need": "Kinetic typography 'DU HỌC AUSTRALIA', 5 vector passport icons, dấu stamp 'TỪ CHỐI' đỏ rực và tỷ lệ 5:1.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.98,
        "routing_reason": "Positive justification: Hook thị giác mở đầu cần tác động thị giác tức thì bằng typography động và chuyển hóa đồ họa 5:1 (1 trong 5 hồ sơ bị loại). Đồ họa vector hình học giải thích bản chất thống kê rõ ràng hơn cảnh quay người thật.",
        "flow_contribution": "None",
        "hf_contribution": "Open-canvas kinetic typography, SVG passport stack xếp vòng cung so le, hiệu ứng stamp từ chối đập xuống.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None (tự nhiên thuộc về đồ họa chuyển động)."
    },
    {
        "scene_number": 2,
        "start": 3.80,
        "end": 9.20,
        "duration": 5.40,
        "raw_text": "Nếu gia đình đang chuẩn bị cho con dù học Australia, có 1 con số rất đáng chú ý.",
        "corrected_text": "Nếu gia đình đang chuẩn bị cho con du học Australia, có một con số rất đáng chú ý:",
        "semantic_type": "parent_context_alert",
        "character": "yes",
        "semantic_action": "Phụ huynh và học sinh ngồi bên bàn gỗ thảo luận tập hồ sơ du học; phụ huynh lật giở trang tài liệu, con chăm chú nhìn theo và gật đầu nghiêm túc.",
        "visual_center": "Cha mẹ và con ngồi bên bàn làm việc cùng thảo luận tập hồ sơ du học, ánh mắt chú tâm.",
        "organic_motion_need": "Cử chỉ ấm áp, nghiêm túc của phụ huynh lật giở trang tài liệu trên bàn, thể hiện sự lo toan đời thực.",
        "exact_graphics_need": "Chấm định vị pin dot + đường chỉ hairline floating callout chỉ vào tập hồ sơ: 'CON SỐ ĐÁNG CHÚ Ý'.",
        "preferred_mode": "HYBRID",
        "routing_confidence": 0.92,
        "routing_reason": "Khung cảnh gia đình thực tế chạm vào tâm lý phụ huynh; plate Flow tạo kết nối cảm xúc, HyperFrames gắn floating callout tinh gọn không dùng hộp che khuất.",
        "flow_contribution": "Plate gia đình ngồi quanh bàn học thảo luận hồ sơ du học thực tế, camera chậm, góc nghiêng 45 độ, chừa 45% negative space bên phải.",
        "hf_contribution": "Floating pointer hairline nối vào trang hồ sơ + text bare hero 'CON SỐ ĐÁNG CHÚ Ý' với drop-shadow nhẹ.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "Nếu Flow plate không đạt biểu cảm tự nhiên hoặc camera rung lắc quá mức."
    },
    {
        "scene_number": 3,
        "start": 9.20,
        "end": 12.60,
        "duration": 3.40,
        "raw_text": "Hơn 21% hồ sơ vô giá dù học bị tự chối.",
        "corrected_text": "Hơn 21% hồ sơ visa du học bị từ chối.",
        "semantic_type": "shocking_statistic",
        "character": "no",
        "semantic_action": "None (Cảnh thuần dữ liệu số liệu sốc. Đồng hồ đo radial gauge quét vòng và counter count-up từ 0% lên >21% chiếm trọn trọng tâm thị giác).",
        "visual_center": "Vòng tròn tiến trình tỷ lệ count-up vượt ngưỡng 21% màu đỏ cam, bóc tách tỷ lệ tương phản.",
        "organic_motion_need": "Không yêu cầu. Cần diễn giải chính xác con số dữ liệu 21% và tốc độ tăng đột biến.",
        "exact_graphics_need": "Bộ đếm số count-up 0% -> 21.4%, vòng đo donut vector mở góc động, viền cảnh báo nổi bật.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.99,
        "routing_reason": "Positive justification: Trực quan hóa con số thống kê đột phá 21%. Yêu cầu độ chính xác toán học và counter animation chính xác theo từng frame của GSAP.",
        "flow_contribution": "None",
        "hf_contribution": "Đồng hồ đo phần trăm SVG động, số liệu nhảy từ 0% lên >21%, nhịp thở rung viền cảnh báo.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 4,
        "start": 12.60,
        "end": 18.10,
        "duration": 5.50,
        "raw_text": "Đây là mức cao nhất trong 10 năm qua, trong quý cảnh Australia đang sích dạc chính sách nhập cư.",
        "corrected_text": "Đây là mức cao nhất trong 10 năm qua, trong bối cảnh Australia đang siết chặt chính sách nhập cư.",
        "semantic_type": "policy_tightening",
        "character": "yes",
        "semantic_action": "Học sinh đeo ba lô kéo vali và cầm hộ chiếu thật bước qua sảnh sân bay, ngước nhìn bảng hướng dẫn di trú với ánh mắt kiên định.",
        "visual_center": "Học sinh cầm hộ chiếu đứng tại sảnh sân bay quốc tế trước cửa kiểm soát di trú nghiêm ngặt.",
        "organic_motion_need": "Cử động bước chân du học sinh, ánh nhìn hướng về cổng kiểm soát di trú mang tính hiện thực.",
        "exact_graphics_need": "Chỉ số trần 10 năm nổi trên negative space: 'ĐỈNH 10 NĂM' và đường mốc thời gian tăng vọt.",
        "preferred_mode": "HYBRID",
        "routing_confidence": 0.90,
        "routing_reason": "Môi trường sân bay/cửa khẩu di trú tạo bối cảnh thực tế cho chính sách siết chặt; HyperFrames định vị mốc 'ĐỈNH 10 NĂM' trên khoảng trống âm.",
        "flow_contribution": "Clean plate học sinh mang ba lô cầm hộ chiếu bước qua sảnh sân bay hiện đại, camera pan nhẹ sang phải chừa 50% bên trái trống.",
        "hf_contribution": "Bare hero metric 'ĐỈNH 10 NĂM' + biểu tượng đường xu hướng dốc đứng mạ vàng.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "Nếu video sinh ra chi tiết chữ sai trên bảng hiệu sân bay."
    },
    {
        "scene_number": 5,
        "start": 18.10,
        "end": 23.60,
        "duration": 5.50,
        "raw_text": "Đặc biệt với nhóm dù học nghệ VET, tí lệ hồ sơ được chắp thuận chỉ khoảng 1 nửa.",
        "corrected_text": "Đặc biệt với nhóm du học nghề VET, tỷ lệ hồ sơ được chấp thuận chỉ khoảng một nửa.",
        "semantic_type": "vocational_vet_metric",
        "character": "no",
        "semantic_action": "None (Cảnh thuần cấu trúc kỹ thuật và tỷ lệ phân đôi 50/50. Nón bảo hộ/bánh răng VET bị tia laser cắt đôi đối xứng, hai nửa tách biệt rõ ràng).",
        "visual_center": "Biểu tượng nón bảo hộ/bánh răng du học nghề VET bị chia đôi đối xứng, một nửa sáng (50% đỗ) và một nửa tối (50% rớt).",
        "organic_motion_need": "Không yêu cầu. Cần hình học hóa trực quan tỷ lệ 50/50 chính xác tuyệt đối.",
        "exact_graphics_need": "Hero icon du học nghề đa tầng, vạch phân tách 50% tỷ lệ đỗ vs trượt, badge tag VET Vocational.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.96,
        "routing_reason": "Positive justification: Thể hiện sự phân đôi 50/50 của nhóm du học nghề VET. Video người thật không thể bóc tách tỷ lệ phân rã 1/2 rõ ràng bằng đồ họa vector phân đôi mặt cắt.",
        "flow_contribution": "None",
        "hf_contribution": "Hero vector badge VET phân tách cơ học 50/50, thanh đo đỗ trượt bẻ đôi với hiệu ứng cắt laser mượt mà.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 6,
        "start": 23.60,
        "end": 31.60,
        "duration": 8.00,
        "raw_text": "Một trong những yếu tốt quan trọng hiện nay là 3 kiểm tra chê new in student, đình, GS, tức đánh giá mục đất học tập thực sự của ứng viên.",
        "corrected_text": "Một trong những yếu tố quan trọng hiện nay là bài kiểm tra Genuine Student – GS, tức đánh giá mục đích học tập thực sự của ứng viên.",
        "semantic_type": "assessment_criteria_gs",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên (hoodie, ba lô) cầm kính lúp lớn soi vào mặt phẳng công văn Genuine Student (GS), di chuyển tia quét làm sáng rực dòng chữ 'MỤC ĐÍCH THỰC SỰ'.",
        "visual_center": "Kính lúp kiểm định quét qua tờ đơn Genuine Student (GS), hé lộ lõi thẩm định: 'MỤC ĐÍCH HỌC TẬP THỰC SỰ'.",
        "organic_motion_need": "Không yêu cầu. Cần đồ họa kiểm định hồ sơ mang tính hành chính và học thuật cao cấp.",
        "exact_graphics_need": "Mô phỏng tờ công văn thực tế (semantic surface hợp lệ), kính lúp vector quét tia quét xanh, con dấu bảo chứng 'GENUINE STUDENT'.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.97,
        "routing_reason": "Positive justification: Tiêu chuẩn GS là văn bản quy chuẩn pháp lý. Sử dụng mặt phẳng tài liệu thực tế (document surface) vượt qua bài kiểm tra Boundary Removal Test để minh họa quy trình kiểm tra mục đích thật.",
        "flow_contribution": "None",
        "hf_contribution": "Mặt phẳng công văn GS chính thống, tia quét kính lúp quang học, phóng to cụm từ khóa 'MỤC ĐÍCH THỰC SỰ'.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 7,
        "start": 31.60,
        "end": 35.00,
        "duration": 3.40,
        "raw_text": "Hồ sơ không chỉ cần chứng minh bạn đủ điều kiện nhập học.",
        "corrected_text": "Hồ sơ không chỉ cần chứng minh bạn đủ điều kiện nhập học.",
        "semantic_type": "admission_contrast",
        "character": "yes",
        "semantic_action": "Học sinh ngồi bàn học cầm phong bì thư mời nhập học (Offer Letter/COE) từ trường đại học Úc, mở thư ra xem với nụ cười rồi thoáng vẻ đăm chiêu suy nghĩ.",
        "visual_center": "Học sinh cầm trên tay thư chấp thuận nhập học (Offer Letter/COE) từ trường đại học, vẻ mặt vừa mừng vừa băn khoăn.",
        "organic_motion_need": "Cầm và lật mở phong bì thư/tờ giấy thông báo nhập học từ trường Australia.",
        "exact_graphics_need": "Floating callout ghim vào góc thư: 'ĐỖ TRƯỜNG ≠ CÓ VISA' cảnh báo sự phân tách.",
        "preferred_mode": "HYBRID",
        "routing_confidence": 0.91,
        "routing_reason": "Học sinh cầm bức thư trúng tuyển thật trên tay tạo sự chân thực về cảm xúc thành công bước đầu; HyperFrames gắn nhãn nhắc nhở 'ĐỦ ĐIỀU KIỆN ≠ ĐỖ VISA' không dùng hộp thô kệch.",
        "flow_contribution": "Plate học sinh ngồi bàn học cầm tờ giấy thư mời nhập học thực tế, ánh sáng tự nhiên, 45% bên phải chừa trống.",
        "hf_contribution": "Floating pointer ghim vào dấu mộc trường + từ khóa tương phản 'ĐỖ TRƯỜNG ≠ CÓ VISA'.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "Nếu Flow render bị biến dạng bàn tay hoặc góc quay không tĩnh."
    },
    {
        "scene_number": 8,
        "start": 35.00,
        "end": 43.80,
        "duration": 8.80,
        "raw_text": "Cơ quan sách duệt, con xem xét hoàn cảnh tại quê nhà, truyến vòng học tập tại Australia, giá trị của khoá học đối với tương lai và lịch sử gì chú.",
        "corrected_text": "Cơ quan xét duyệt còn xem xét hoàn cảnh tại quê nhà, triển vọng học tập tại Australia, giá trị của khóa học đối với tương lai và lịch sử di trú.",
        "semantic_type": "four_evaluation_pillars",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên bước đi dọc theo đường cong S-curve uốn lượn zigzag, lần lượt giơ tay chạm sáng 4 trạm kiểm định của Bộ Di Trú (Quê nhà -> Úc -> Tương lai -> Di trú).",
        "visual_center": "Hệ thống 4 trụ cột kiểm định so le zigzag theo đường dẫn S-curve: 1. Quê nhà -> 2. Triển vọng Úc -> 3. Tương lai -> 4. Lịch sử di trú.",
        "organic_motion_need": "Không yêu cầu. Cần diễn giải cấu trúc ma trận 4 tiêu chuẩn xét duyệt của Bộ Di Trú.",
        "exact_graphics_need": "4 Hero vector icons có đế nổi đổ bóng: ngôi nhà, tòa tháp Sydney, biểu đồ sự nghiệp, hộ chiếu lịch sử. Không có naked digit circle.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.99,
        "routing_reason": "Positive justification: Diễn giải 4 trụ cột xét duyệt di trú toàn diện. Yêu cầu bố cục kinetic zigzag mở rộng không gian, các icon đa tầng xuất hiện theo nhịp đọc voiceover, tuyệt đối cấm danh sách gạch đầu dòng hay video người thật đóng thế vô nghĩa.",
        "flow_contribution": "None",
        "hf_contribution": "Đường dẫn động S-curve vector kết nối 4 trạm kiểm định, từng hero icon xuất hiện tuần tự theo nhịp lời dẫn.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 9,
        "start": 43.80,
        "end": 47.10,
        "duration": 3.30,
        "raw_text": "Vì vậy, câu hỏi không chỉ là, bạn hộng ngăn gì,",
        "corrected_text": "Vì vậy, câu hỏi không chỉ là: “Bạn học ngành gì?”",
        "semantic_type": "surface_level_question",
        "character": "no",
        "semantic_action": "None (Cảnh chuyển giao tư duy - Mindset Pivot thuần Kinetic Typography. Câu hỏi bề nổi xuất hiện dứt khoát rồi mờ đi để nhường chỗ cho sơ đồ 3 tầng chiều sâu).",
        "visual_center": "Câu hỏi bề nổi 'BẠN HỌC NGÀNH GÌ?' đơn độc, bị bao quanh bởi các vòng tròn mờ tượng trưng cho cái nhìn phiến diện.",
        "organic_motion_need": "Không yêu cầu. Tạo sự tương phản mạnh mẽ giữa câu hỏi bề nổi và các tầng câu hỏi chiều sâu ở cảnh tiếp theo.",
        "exact_graphics_need": "Hero typography headline >= 36px, dấu hỏi lớn mạ xám slate thu nhỏ nhường chỗ cho phân tích sâu.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.96,
        "routing_reason": "Positive justification: Cảnh chuyển giao tư duy (mindset pivot). Cần nhấn mạnh bằng kinetic typography tối giản, chuẩn bị bung mở bộ 3 câu hỏi cốt tử ở Scene 10.",
        "flow_contribution": "None",
        "hf_contribution": "Kinetic typography xuất hiện dứt khoát, đường gạch chân mờ tan biến sang câu hỏi sâu.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 10,
        "start": 47.10,
        "end": 53.90,
        "duration": 6.80,
        "raw_text": "mà còn là, vì sao bạn chọn ngăn này, chọn Australia và kế hoạt của bạn sau khi học sông là gì.",
        "corrected_text": "Mà còn là: “Vì sao bạn chọn ngành này, chọn Australia và kế hoạch của bạn sau khi học xong là gì?”",
        "semantic_type": "three_deep_questions",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên đứng ở vị trí trung tâm, xoay người chỉ tay phát xung năng lượng kích hoạt lần lượt 3 đỉnh của tam giác chiến lược (Ngành -> Úc -> Kế hoạch sau tốt nghiệp).",
        "visual_center": "3 trục mũi tên nan quạt tỏa ra 3 hướng chiến lược: 1. Tại sao ngành này? -> 2. Tại sao Australia? -> 3. Kế hoạch sau tốt nghiệp?",
        "organic_motion_need": "Không yêu cầu. Cấu trúc tư duy logic 3 tầng cần diễn đạt bằng sơ đồ phân nhánh hình học.",
        "exact_graphics_need": "3 Hero icons (ngành nghề chuyên sâu, bản đồ Australia, lộ trình sự nghiệp tương lai) xếp bố cục hình học tam giác vững chắc.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.98,
        "routing_reason": "Positive justification: Ba câu hỏi cốt lõi tạo thành tam giác logic thuyết phục của bài giải trình GS. Trực quan hóa hình học không gian mở (open-canvas) vượt trội hoàn toàn so với bất kỳ diễn xuất người thật nào.",
        "flow_contribution": "None",
        "hf_contribution": "Tam giác động lực 3 đỉnh liên kết, từng đỉnh bật sáng icon vector đồng bộ với voiceover.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 11,
        "start": 53.90,
        "end": 62.90,
        "duration": 9.00,
        "raw_text": "Bài báo cũng dẫn trường hợp một nữ sinh in Indonesia từng chuẩn bị bàn giải trình dài 27 tranh, nhưng hồ sơ vi gia vẫn bị tự chối chỉ sau một ngày.",
        "corrected_text": "Bài báo cũng dẫn trường hợp một nữ sinh Indonesia từng chuẩn bị bản giải trình dài 27 trang, nhưng hồ sơ visa vẫn bị từ chối chỉ sau một ngày.",
        "semantic_type": "case_study_real_world",
        "character": "yes",
        "semantic_action": "Nữ sinh Indonesia ngồi bên bàn học đối diện chồng tài liệu 27 trang dày cộp, tay đặt lên gáy tập tài liệu, biểu cảm sững sờ khi nhận thông báo từ chối sau 1 ngày.",
        "visual_center": "Nữ sinh ngồi bên bàn học nhìn tập hồ sơ giải trình dày cộp 27 trang với nét mặt ngỡ ngàng.",
        "organic_motion_need": "Nữ sinh đặt tay lên tập tài liệu dày 27 trang được đóng gáy cẩn thận, biểu cảm ngỡ ngàng khi nhận kết quả.",
        "exact_graphics_need": "Floating pointer ghim vào tập tài liệu: '27 TRANG GIẢI TRÌNH' chuyển trạng thái sang 'TỪ CHỐI SAU 1 NGÀY'.",
        "preferred_mode": "HYBRID",
        "routing_confidence": 0.94,
        "routing_reason": "Đây là case-study có thật về người thật việc thật (nữ sinh Indonesia cùng tập hồ sơ 27 trang). Video người thật tương tác với tập hồ sơ dày cộp mang lại tính xác thực không thể thay thế; HyperFrames hiển thị mốc 27 trang và thời gian 1 ngày từ chối.",
        "flow_contribution": "Clean plate nữ sinh châu Á ngồi bên bàn học đối diện chồng tài liệu 27 trang dày, ánh mắt ngỡ ngàng, chừa 45% khoảng trống góc trên bên phải.",
        "hf_contribution": "Floating pointer ghim vào tập tài liệu + text metric '27 TRANG' biến đổi trạng thái sang nhãn 'TỪ CHỐI SAU 1 NGÀY' với màu đỏ cam cảnh báo.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "Nếu Flow plate không tạo được độ dày thực tế của tập tài liệu hoặc biểu cảm giả tạo."
    },
    {
        "scene_number": 12,
        "start": 62.90,
        "end": 67.90,
        "duration": 5.00,
        "raw_text": "Một trong những vấn đề được đặc ra là, tại sao bạn không học ngăn này ở quê nhà.",
        "corrected_text": "Một trong những vấn đề được đặt ra là: “Tại sao bạn không học ngành này ở quê nhà?”",
        "semantic_type": "home_country_dilemma",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên đứng giữa hai cực địa lý (Quê Nhà và Australia), nhìn xuống cây cầu gãy kết nối, nhún vai thể hiện sự băn khoăn tìm lời giải trình.",
        "visual_center": "Sự đối chiếu địa lý giữa Ngôi nhà quê hương (Home Country) và Biểu tượng Australia, kèm dấu hỏi chất vấn của nhân viên xét duyệt.",
        "organic_motion_need": "Không yêu cầu. Cần hình ảnh hóa sự so sánh cơ hội đào tạo giữa quê nhà và nước ngoài.",
        "exact_graphics_need": "Hai biểu tượng vị trí địa lý kết nối bằng đường cầu nối đứt khúc, dấu chấm hỏi trung tâm phát xung cảnh báo.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.97,
        "routing_reason": "Positive justification: Trực quan hóa câu hỏi nghi vấn hóc búa nhất của Bộ Di Trú: tại sao không học ngành này tại quê nhà. Yêu cầu đồ họa đối chiếu địa lý 2 cực, nhấn mạnh vào khoảng cách giải trình.",
        "flow_contribution": "None",
        "hf_contribution": "Đồ họa phân tách 2 cực địa lý (Quê nhà vs Australia), đường truyền tín hiệu đứt gãy tượng trưng cho lỗ hổng lập luận.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 13,
        "start": 67.90,
        "end": 72.40,
        "duration": 4.50,
        "raw_text": "Điều này cho thấy, một bộ hồ sơ dài chưa chắc đồng nghĩa với một hồ sơ thuyết phục.",
        "corrected_text": "Điều này cho thấy một bộ hồ sơ dài chưa chắc đồng nghĩa với một hồ sơ thuyết phục.",
        "semantic_type": "insight_scale_balance",
        "character": "no",
        "semantic_action": "None (Cảnh ẩn dụ cơ học thuần khiết. Chiếc cân định lượng nghiêng bổng bên chồng giấy dày 27 trang lên cao, đè nặng bên viên kim cương logic thuyết phục).",
        "visual_center": "Chiếc cân định lượng nghiêng lệch: Bên chồng hồ sơ dày cộp (Độ dài) bị lơ lửng, không có trọng lượng so với bên Thuyết phục (Sức nặng lập luận).",
        "organic_motion_need": "Không yêu cầu. Trừu tượng hóa nguyên lý 'dài ≠ thuyết phục' bằng cơ học chiếc cân.",
        "exact_graphics_need": "Cán cân cân bằng vật lý vector, bên trái là tập giấy dày, bên phải là viên kim cương/chìa khóa logic đè nặng.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.98,
        "routing_reason": "Positive justification: Ẩn dụ chiếc cân định lượng so sánh độ dài số trang đối lập với giá trị thuyết phục. Hình học chiếc cân nghiêng là phương pháp giải thích trực quan chuẩn mực nhất.",
        "flow_contribution": "None",
        "hf_contribution": "Chiếc cân vector chuyển động nghiêng vật lý, giải phóng suy nghĩ sai lầm về độ dài hồ sơ.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 14,
        "start": 72.40,
        "end": 77.00,
        "duration": 4.60,
        "raw_text": "Quang trọng hơn là tính lô rích và sửa nhất quán trong toàn bộ câu chuyện dù học.",
        "corrected_text": "Quan trọng hơn là tính logic và sự nhất quán trong toàn bộ câu chuyện du học.",
        "semantic_type": "logic_and_consistency",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên dùng hai tay kéo căng sợi chỉ vàng logic (Golden Thread), kết nối xuyên suốt 3 mắt xích (Học vấn quá khứ -> Khóa học chọn -> Sự nghiệp tương lai).",
        "visual_center": "Sợi chỉ vàng logic (Golden Thread) xâu chuỗi hoàn hảo các mảnh ghép câu chuyện du học từ quá khứ, hiện tại đến tương lai.",
        "organic_motion_need": "Không yêu cầu. Trừu tượng hóa tính logic và sự kết nối mạch lạc của câu chuyện.",
        "exact_graphics_need": "Sợi dây kết nối phát sáng xuyên qua 3 nút then chốt: Học vấn quá khứ -> Khóa học chọn -> Sự nghiệp tương lai.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.97,
        "routing_reason": "Positive justification: Diễn giải khái niệm trừu tượng 'Tính logic & Nhất quán'. Sợi chỉ vàng kết nối các nút mắt xích là visual blueprint chuẩn mực của ngành giáo dục quốc tế.",
        "flow_contribution": "None",
        "hf_contribution": "Đường dây phát sáng vàng hoàng kim kết nối 3 mắt xích kim loại, khóa chặt câu chuyện thành một thể thống nhất.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 15,
        "start": 77.00,
        "end": 82.80,
        "duration": 5.80,
        "raw_text": "Vì vậy, khi Australia ngay can kiểm soát dạc hồ sơ dù học, vì chuẩn bị từ đầu can quang trọng.",
        "corrected_text": "Vì vậy, khi Australia ngày càng kiểm soát chặt hồ sơ du học, việc chuẩn bị từ đầu càng quan trọng.",
        "semantic_type": "strategic_preparation",
        "character": "yes",
        "semantic_action": "Học sinh chủ động ngồi trước bàn học với máy tính xách tay và cuốn sổ tay, tay cầm bút ghi chép từng gạch đầu dòng lộ trình chuẩn bị từ sớm với nét mặt tự tin.",
        "visual_center": "Học sinh chủ động ngồi trước bàn lập kế hoạch học tập với máy tính và sổ tay định hướng chiến lược từ sớm.",
        "organic_motion_need": "Học sinh tự tin vạch lộ trình trên cuốn sổ tay, ánh mắt kiên định hướng về phía trước.",
        "exact_graphics_need": "Floating pointer ghim vào cuốn sổ tay: 'CHUẨN BỊ TỪ ĐẦU' + mốc thời gian quy hoạch sớm.",
        "preferred_mode": "HYBRID",
        "routing_confidence": 0.91,
        "routing_reason": "Hành động chuẩn bị chủ động của học sinh trong không gian học tập thực tế khơi gợi động lực hành động; HyperFrames gắn thông điệp cốt lõi trên khoảng trống.",
        "flow_contribution": "Clean plate học sinh ngồi bàn làm việc sáng sủa viết vào sổ tay kế hoạch du học, máy tính mở bên cạnh, chừa 45% khoảng trống bên trái.",
        "hf_contribution": "Floating pointer hairline nối vào sổ tay + bare hero metric 'CHUẨN BỊ TỪ ĐẦU' nổi bật.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "Nếu cử động viết của học sinh trong Flow không tự nhiên."
    },
    {
        "scene_number": 16,
        "start": 82.80,
        "end": 87.30,
        "duration": 4.50,
        "raw_text": "Tại Esora, học viên không chỉ được hỗ trợ trọng trường hay chuẩn bị giới tờ.",
        "corrected_text": "Tại Esora, học viên không chỉ được hỗ trợ chọn trường hay chuẩn bị giấy tờ.",
        "semantic_type": "brand_differentiation",
        "character": "yes",
        "semantic_action": "Chuyên gia tư vấn Esora (nữ, vest thanh lịch) ngồi đối thoại 1:1 cùng phụ huynh và học sinh tại bàn tư vấn văn phòng hiện đại, cử chỉ tay cởi mở lắng nghe và phân tích.",
        "visual_center": "Chuyên gia tư vấn Esora ngồi đối thoại 1:1 cùng gia đình tại văn phòng tư vấn chuyên nghiệp, phong thái tận tâm.",
        "organic_motion_need": "Chuyên gia Esora mỉm cười lắng nghe và trao đổi chân thành với phụ huynh trên bàn tư vấn.",
        "exact_graphics_need": "Logo thương hiệu ESORA tinh tế + floating callout: 'ĐỒNG HÀNH TOÀN DIỆN' vượt trên giấy tờ thủ tục.",
        "preferred_mode": "HYBRID",
        "routing_confidence": 0.93,
        "routing_reason": "Xây dựng niềm tin thương hiệu ESORA bằng hình ảnh tư vấn gia đình thực tế chuyên nghiệp; HyperFrames gắn nhận diện thương hiệu chuẩn xác không dùng hộp che mặt chuyên gia.",
        "flow_contribution": "Clean plate chuyên gia tư vấn (nữ, vest thanh lịch) ngồi cùng phụ huynh và học sinh tại bàn tư vấn văn phòng hiện đại, chừa 45% bên phải trống.",
        "hf_contribution": "Thương hiệu ESORA chuẩn xác + floating tag 'ĐỒNG HÀNH TOÀN DIỆN' định vị trên khoảng trống âm.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "Nếu khuôn mặt nhân vật Flow không đạt độ sắc nét chuyên nghiệp."
    },
    {
        "scene_number": 17,
        "start": 87.30,
        "end": 94.70,
        "duration": 7.40,
        "raw_text": "Lỗ trình còn cần làm rõ, học gì, tại sao trọng anh này, tại sao trọng Australia và kế hoạt sau tốt nghiệp là gì.",
        "corrected_text": "Lộ trình còn cần làm rõ: Học gì? Tại sao chọn ngành này? Tại sao chọn Australia? Và kế hoạch sau tốt nghiệp là gì?",
        "semantic_type": "four_step_esora_roadmap",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên bước lên từng bậc nấc thang của lộ trình S-curve ESORA (Bậc 1: Học gì -> Bậc 2: Chọn ngành -> Bậc 3: Chọn Úc -> Bậc 4: Kế hoạch tương lai).",
        "visual_center": "Lộ trình chiến lược 4 nấc thang S-curve uốn lượn so le zigzag: 1. Học gì? -> 2. Chọn ngành -> 3. Chọn Australia -> 4. Sau tốt nghiệp.",
        "organic_motion_need": "Không yêu cầu. Cần diễn giải mạch lạc quy trình 4 chặng của Esora.",
        "exact_graphics_need": "4 Hero vector icons gắn nấc thang S-curve (Sách chuyên ngành, La bàn định vị, Nhà hát Con Sò Sydney, Lễ tốt nghiệp & Sự nghiệp).",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.99,
        "routing_reason": "Positive justification: Bản đồ lộ trình 4 bước chiến lược của ESORA. Đây là tài sản sư phạm độc quyền cần bố cục kinetic trajectory S-curve so le trái phải, icon đa tầng nổi, tuyệt đối cấm danh sách thẳng hàng.",
        "flow_contribution": "None",
        "hf_contribution": "Đường dẫn động S-curve vector mang sắc cam ESORA, 4 hero icon bật mở đồng nhịp lời dẫn.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 18,
        "start": 94.70,
        "end": 99.80,
        "duration": 5.10,
        "raw_text": "Để toàn bộ hồ sơ thể hiện được một mục tiêu hợp tập gió dàng và nhất quán.",
        "corrected_text": "Để toàn bộ hồ sơ thể hiện được một mục tiêu học tập rõ ràng và nhất quán.",
        "semantic_type": "unified_study_target",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên giương cung bắn mũi tên chiến lược trúng hồng tâm mục tiêu (Bulls-eye Target), kích hoạt con dấu chứng nhận 'Mục tiêu nhất quán' phát sáng ngọc bích.",
        "visual_center": "Hồng tâm mục tiêu (Bulls-eye Target) đón nhận mũi tên chiến lược bắn trúng tâm, bung nở dấu tích chứng nhận xác thực xanh ngọc.",
        "organic_motion_need": "Không yêu cầu. Biểu tượng hóa sự hội tụ của mục tiêu học tập rõ ràng và kiên định.",
        "exact_graphics_need": "Hero icon hồng tâm mục tiêu nhiều lớp, tia sáng hội tụ, con dấu 'MỤC TIÊU NHẤT QUÁN' hoàn hảo.",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.98,
        "routing_reason": "Positive justification: Thể hiện thông điệp 'Mục tiêu học tập rõ ràng & nhất quán'. Đồ họa hồng tâm hội tụ các yếu tố hồ sơ là cách diễn đạt ẩn dụ trực quan mạnh mẽ nhất.",
        "flow_contribution": "None",
        "hf_contribution": "Đồ họa vector hồng tâm hội tụ, mũi tên chạm tâm bung nở sóng xung kích nhẹ.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 19,
        "start": 99.80,
        "end": 108.00,
        "duration": 8.20,
        "raw_text": "Dù học Australia không chỉ là được chương nhân. Quân trọng là phải xây dựng được một hồ sơ đủ thuyết phục để đi tiếp đến bước vi gia.",
        "corrected_text": "Du học Australia không chỉ là được trường nhận. Quan trọng là phải xây dựng được một hồ sơ đủ thuyết phục để đi tiếp đến bước visa.",
        "semantic_type": "offer_to_visa_gateway",
        "character": "yes",
        "semantic_action": "Nhân vật 2D vector sinh viên bước qua Cánh cổng 1 (Thư mời nhập học - Offer) và tự tin tiến thẳng đến mở khóa Cánh cổng 2 (Cấp Visa - Visa Granted) phát sáng vàng rực.",
        "visual_center": "Chặng đường 2 cánh cổng: Cổng 1 (Trường nhận - Offer) mở ra để tiến tới Cổng 2 quyết định (Visa Australia được cấp - Visa Granted).",
        "organic_motion_need": "Không yêu cầu. Cần hình tượng hóa hành trình 2 bước sống còn của du học sinh.",
        "exact_graphics_need": "2 Cánh cổng mốc son: Bước 1 'ĐỖ TRƯỜNG' (bước đệm) -> Bước 2 'CÁN ĐÍCH VISA' (đích đến thực sự với dấu mộc vàng).",
        "preferred_mode": "HF_ONLY",
        "routing_confidence": 0.97,
        "routing_reason": "Positive justification: Phân định ranh giới giữa 2 nấc thang then chốt (Nhận thư mời vs Cấp Visa). Trực quan hóa 2 cánh cổng thành công là chìa khóa thay đổi nhận thức người xem.",
        "flow_contribution": "None",
        "hf_contribution": "Cơ chế đồ họa 2 cổng mốc son tuần tự, hiệu ứng mở khóa cổng Visa sáng bừng.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "None"
    },
    {
        "scene_number": 20,
        "start": 108.00,
        "end": 116.04,
        "duration": 8.04,
        "raw_text": "Nếu gia đình đang chuẩn bị hồ sơ dù học Australia, Hãy liên hệ Esora để được tư vấn lộ trình một mục tiêu hợp với từng học sinh.",
        "corrected_text": "Nếu gia đình đang chuẩn bị hồ sơ du học Australia, hãy liên hệ Esora để được tư vấn lộ trình 1:1 phù hợp với từng học sinh.",
        "semantic_type": "call_to_action",
        "character": "yes",
        "semantic_action": "Học sinh rạng rỡ kéo vali bước đi trong khuôn viên ngập nắng của trường đại học Australia, nở nụ cười tự tin hướng về phía ống kính.",
        "visual_center": "Học sinh tự tin nở nụ cười tươi bước đi cùng vali tại khuôn viên trường đại học Australia trong ánh nắng rực rỡ.",
        "organic_motion_need": "Du học sinh bước đi tự tin, nụ cười rạng rỡ của người đã đạt được ước mơ visa du học.",
        "exact_graphics_need": "Bare hero CTA 'TƯ VẤN LỘ TRÌNH 1:1', thương hiệu ESORA nổi bật trên nền video, giữ vùng an toàn 200px đáy màn hình.",
        "preferred_mode": "HYBRID",
        "routing_confidence": 0.95,
        "routing_reason": "Cảnh kết thúc mang lại cảm xúc vỡ òa của thành công đích thực khi học sinh đã đặt chân đến Australia; HyperFrames đặt lời kêu gọi hành động tư vấn 1:1 cùng ESORA nổi bật trên nền video sạch sẽ.",
        "flow_contribution": "Clean plate học sinh mang vali kéo bước đi rạng rỡ dưới hàng cây khuôn viên trường đại học Australia, camera dolly chậm, 45% bên trái trống.",
        "hf_contribution": "Logo ESORA + bare hero callout 'TƯ VẤN 1:1 CÙNG CHUYÊN GIA' thả nhẹ trên khoảng trống âm.",
        "fallback_mode": "HF_ONLY",
        "fallback_condition": "Nếu Flow plate không đạt ánh sáng khuôn viên tự nhiên."
    }
]

# Calculate summary metrics
total_scenes = len(routing_data)
hf_count = sum(1 for s in routing_data if s["preferred_mode"] == "HF_ONLY")
hybrid_count = sum(1 for s in routing_data if s["preferred_mode"] == "HYBRID")
flow_count = sum(1 for s in routing_data if s["preferred_mode"] == "FLOW_ONLY")

char_yes_count = sum(1 for s in routing_data if s["character"] == "yes")
char_no_count = sum(1 for s in routing_data if s["character"] == "no")
char_ratio = (char_yes_count / total_scenes) * 100

summary = {
    "project_name": "Du học Australia: 5 hồ sơ thì 1 bị từ chối Visa?",
    "brand": "ESORA",
    "canvas": "720x1280 (9:16 Vertical)",
    "total_duration": 116.04,
    "total_scenes": total_scenes,
    "distribution": {
        "hf_only_count": hf_count,
        "hf_only_ratio": f"{hf_count/total_scenes*100:.1f}%",
        "hybrid_count": hybrid_count,
        "hybrid_ratio": f"{hybrid_count/total_scenes*100:.1f}%",
        "flow_only_count": flow_count,
        "flow_only_ratio": f"{flow_count/total_scenes*100:.1f}%"
    },
    "character_budget": {
        "character_present_count": char_yes_count,
        "character_present_ratio": f"{char_ratio:.1f}%",
        "character_absent_count": char_no_count,
        "character_absent_ratio": f"{(char_no_count/total_scenes)*100:.1f}%",
        "target_band": "70% - 80%",
        "status": "PASSED (75.0% nằm chính xác trong khoảng chuẩn 70–80%)"
    },
    "audit_compliance": {
        "max_consecutive_hf_only": 3,
        "consecutive_hf_chains": ["Scene 08, 09, 10", "Scene 12, 13, 14", "Scene 17, 18, 19"],
        "all_hf_have_positive_justification": True,
        "anti_card_law_enforced": True,
        "anti_mannequin_law_enforced": True,
        "all_characters_have_semantic_actions": True,
        "vertical_occupancy_gate_respected": True,
        "subtitle_safe_area_reserved_px": 200
    }
}

output_payload = {
    "summary": summary,
    "scenes": routing_data
}

with open("scratch/scene_routing.json", "w", encoding="utf-8") as f:
    json.dump(output_payload, f, ensure_ascii=False, indent=2)

# Generate Markdown
with open("scratch/scene_routing.md", "w", encoding="utf-8") as f:
    f.write("# Bảng Phân Loại Routing Toàn Phim (Film-Level Scene Routing Audit)\n\n")
    f.write("## 1. Thông Tin Dự Án\n")
    f.write(f"- **Chủ đề chính**: Du học Australia — Cứ 5 hồ sơ thì 1 bị từ chối Visa?\n")
    f.write(f"- **Thương hiệu**: ESORA (Viết hoa nhất quán)\n")
    f.write(f"- **Tổng thời lượng**: {tl['total_duration']} giây (~1 phút 56 giây)\n")
    f.write(f"- **Khung hình**: Vertical 720×1280 (9:16 Shorts / Reels / TikTok)\n")
    f.write(f"- **Tổng số phân cảnh**: {total_scenes} scenes\n\n")
    f.write("## 2. Thống Kê Phân Bổ Engine Routing & Ngân Sách Nhân Vật\n")
    f.write(f"- **HF_ONLY (Visual-First & Kinetic Open Canvas)**: {hf_count} scenes ({hf_count/total_scenes*100:.1f}%)\n")
    f.write(f"- **HYBRID (Clean Plate + Floating Callouts)**: {hybrid_count} scenes ({hybrid_count/total_scenes*100:.1f}%)\n")
    f.write(f"- **FLOW_ONLY (Zero-Text & Physical Props)**: {flow_count} scenes (0% — Explainer sư phạm/thương hiệu yêu cầu lớp đồ họa đồng hành)\n")
    f.write(f"- **Ngân sách Nhân vật (Film-Level Character Budget)**: {char_yes_count}/{total_scenes} scenes ({char_ratio:.1f}%) có nhân vật (`character: yes`), {char_no_count}/{total_scenes} scenes ({(char_no_count/total_scenes)*100:.1f}%) thuần đồ họa/dữ liệu (`character: no`). **Đạt chuẩn 70–80%**.\n\n")
    f.write("### Kết quả Kiểm định Film-Level Routing Audit:\n")
    f.write(f"- **Tỷ lệ HF_ONLY**: {hf_count/total_scenes*100:.1f}% (Đạt chuẩn cân bằng cho video Explainer giáo dục chuyên sâu).\n")
    f.write(f"- **Chuỗi HF_ONLY liên tiếp tối đa**: 3 scenes (Tuân thủ nghiêm ngặt quy tắc không vượt quá 3 scenes HF_ONLY liên tiếp).\n")
    f.write(f"- **Luật Chống Ma-nơ-canh (Gate 10)**: 100% scenes có nhân vật đều định nghĩa rõ **Semantic Action** cụ thể. Tuyệt đối không có nhân vật đứng im làm cảnh.\n")
    f.write(f"- **100% scenes HF_ONLY có Positive Justification**: Từng scene HF_ONLY đều chứng minh tính vượt trội của cấu trúc đồ họa so với diễn xuất người thật.\n")
    f.write(f"- **100% scenes HYBRID tuân thủ Anti-Card Law**: Tuyệt đối không dùng hộp chữ nhật đè lên video; chỉ dùng floating pin pointer và bare hero metrics.\n")
    f.write(f"- **An toàn phụ đề**: Chừa trống cố định 180–200px đáy màn hình cho phụ đề hiển thị.\n\n")
    f.write("---\n\n")
    f.write("## 3. Bảng Chi Tiết Routing 20 Phân Cảnh\n\n")
    f.write("| Scene | Thời gian | Thời lượng | Mode | Nhân vật | Semantic Action / Hành động Ngữ nghĩa | Visual Center | Đóng góp Flow / HyperFrames |\n")
    f.write("| :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |\n")
    for s in routing_data:
        char_badge = "`yes`" if s["character"] == "yes" else "`no`"
        f.write(f"| **Scene {s['scene_number']:02d}** | {s['start']:05.2f}s – {s['end']:05.2f}s | {s['duration']:4.2f}s | `{s['preferred_mode']}` | {char_badge} | {s['semantic_action']} | {s['visual_center']} | Flow: {s['flow_contribution']}<br>HF: {s['hf_contribution']} |\n")

print("Created scratch/scene_routing.json and scratch/scene_routing.md successfully!")
