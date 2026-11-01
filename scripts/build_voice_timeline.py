import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("scratch/whisper_raw.json", "r", encoding="utf-8") as f:
    d = json.load(f)

raw_segs = d["raw_segments"]
total_dur = d["total_duration"]

# Defining the 20 structured scenes with exact audio boundaries
scenes_def = [
    {
        "scene_number": 1,
        "start": 0.00,
        "end": 3.80,
        "raw_text": "Dù học Australia nằm hồ sơ thì một bị tự chối vô giá.",
        "corrected_text": "DU HỌC AUSTRALIA: 5 HỒ SƠ THÌ 1 BỊ TỪ CHỐI VISA?",
        "topic": "Hook: 5 hồ sơ thì 1 bị từ chối visa"
    },
    {
        "scene_number": 2,
        "start": 3.80,
        "end": 9.20,
        "raw_text": "Nếu gia đình đang chuẩn bị cho con dù học Australia, có 1 con số rất đáng chú ý.",
        "corrected_text": "Nếu gia đình đang chuẩn bị cho con du học Australia, có một con số rất đáng chú ý:",
        "topic": "Cảnh báo mở đầu cho phụ huynh"
    },
    {
        "scene_number": 3,
        "start": 9.20,
        "end": 12.60,
        "raw_text": "Hơn 21% hồ sơ vô giá dù học bị tự chối.",
        "corrected_text": "Hơn 21% hồ sơ visa du học bị từ chối.",
        "topic": "Thống kê gây sốc: Hơn 21% bị từ chối"
    },
    {
        "scene_number": 4,
        "start": 12.60,
        "end": 18.10,
        "raw_text": "Đây là mức cao nhất trong 10 năm qua, trong quý cảnh Australia đang sích dạc chính sách nhập cư.",
        "corrected_text": "Đây là mức cao nhất trong 10 năm qua, trong bối cảnh Australia đang siết chặt chính sách nhập cư.",
        "topic": "Đỉnh điểm 10 năm & chính sách siết chặt"
    },
    {
        "scene_number": 5,
        "start": 18.10,
        "end": 23.60,
        "raw_text": "Đặc biệt với nhóm dù học nghệ VET, tí lệ hồ sơ được chắp thuận chỉ khoảng 1 nửa.",
        "corrected_text": "Đặc biệt với nhóm du học nghề VET, tỷ lệ hồ sơ được chấp thuận chỉ khoảng một nửa.",
        "topic": "Nhóm VET: Tỷ lệ đỗ chỉ 50%"
    },
    {
        "scene_number": 6,
        "start": 23.60,
        "end": 31.60,
        "raw_text": "Một trong những yếu tốt quan trọng hiện nay là 3 kiểm tra chê new in student, đình, GS, tức đánh giá mục đất học tập thực sự của ứng viên.",
        "corrected_text": "Một trong những yếu tố quan trọng hiện nay là bài kiểm tra Genuine Student – GS, tức đánh giá mục đích học tập thực sự của ứng viên.",
        "topic": "Bài kiểm tra Genuine Student (GS)"
    },
    {
        "scene_number": 7,
        "start": 31.60,
        "end": 35.00,
        "raw_text": "Hồ sơ không chỉ cần chứng minh bạn đủ điều kiện nhập học.",
        "corrected_text": "Hồ sơ không chỉ cần chứng minh bạn đủ điều kiện nhập học.",
        "topic": "Không chỉ đủ điều kiện nhập học"
    },
    {
        "scene_number": 8,
        "start": 35.00,
        "end": 43.80,
        "raw_text": "Cơ quan sách duệt, con xem xét hoàn cảnh tại quê nhà, truyến vòng học tập tại Australia, giá trị của khoá học đối với tương lai và lịch sử gì chú.",
        "corrected_text": "Cơ quan xét duyệt còn xem xét hoàn cảnh tại quê nhà, triển vọng học tập tại Australia, giá trị của khóa học đối với tương lai và lịch sử di trú.",
        "topic": "4 Tiêu chí xét duyệt toàn diện của Bộ Di Trú"
    },
    {
        "scene_number": 9,
        "start": 43.80,
        "end": 47.10,
        "raw_text": "Vì vậy, câu hỏi không chỉ là, bạn hộng ngăn gì,",
        "corrected_text": "Vì vậy, câu hỏi không chỉ là: “Bạn học ngành gì?”",
        "topic": "Câu hỏi bề nổi: Bạn học ngành gì?"
    },
    {
        "scene_number": 10,
        "start": 47.10,
        "end": 53.90,
        "raw_text": "mà còn là, vì sao bạn chọn ngăn này, chọn Australia và kế hoạt của bạn sau khi học sông là gì.",
        "corrected_text": "Mà còn là: “Vì sao bạn chọn ngành này, chọn Australia và kế hoạch của bạn sau khi học xong là gì?”",
        "topic": "Bộ 3 câu hỏi cốt lõi chứng minh động cơ"
    },
    {
        "scene_number": 11,
        "start": 53.90,
        "end": 62.90,
        "raw_text": "Bài báo cũng dẫn trường hợp một nữ sinh in Indonesia từng chuẩn bị bàn giải trình dài 27 tranh, nhưng hồ sơ vi gia vẫn bị tự chối chỉ sau một ngày.",
        "corrected_text": "Bài báo cũng dẫn trường hợp một nữ sinh Indonesia từng chuẩn bị bản giải trình dài 27 trang, nhưng hồ sơ visa vẫn bị từ chối chỉ sau một ngày.",
        "topic": "Case study: Bản giải trình 27 trang bị từ chối sau 1 ngày"
    },
    {
        "scene_number": 12,
        "start": 62.90,
        "end": 67.90,
        "raw_text": "Một trong những vấn đề được đặc ra là, tại sao bạn không học ngăn này ở quê nhà.",
        "corrected_text": "Một trong những vấn đề được đặt ra là: “Tại sao bạn không học ngành này ở quê nhà?”",
        "topic": "Nghi vấn cốt tử: Tại sao không học ở quê nhà?"
    },
    {
        "scene_number": 13,
        "start": 67.90,
        "end": 72.40,
        "raw_text": "Điều này cho thấy, một bộ hồ sơ dài chưa chắc đồng nghĩa với một hồ sơ thuyết phục.",
        "corrected_text": "Điều này cho thấy một bộ hồ sơ dài chưa chắc đồng nghĩa với một hồ sơ thuyết phục.",
        "topic": "Hồ sơ dài != Hồ sơ thuyết phục"
    },
    {
        "scene_number": 14,
        "start": 72.40,
        "end": 77.00,
        "raw_text": "Quang trọng hơn là tính lô rích và sửa nhất quán trong toàn bộ câu chuyện dù học.",
        "corrected_text": "Quan trọng hơn là tính logic và sự nhất quán trong toàn bộ câu chuyện du học.",
        "topic": "Tính logic & sự nhất quán trong câu chuyện"
    },
    {
        "scene_number": 15,
        "start": 77.00,
        "end": 82.80,
        "raw_text": "Vì vậy, khi Australia ngay can kiểm soát dạc hồ sơ dù học, vì chuẩn bị từ đầu can quang trọng.",
        "corrected_text": "Vì vậy, khi Australia ngày càng kiểm soát chặt hồ sơ du học, việc chuẩn bị từ đầu càng quan trọng.",
        "topic": "Chuẩn bị chiến lược ngay từ đầu"
    },
    {
        "scene_number": 16,
        "start": 82.80,
        "end": 87.30,
        "raw_text": "Tại Esora, học viên không chỉ được hỗ trợ trọng trường hay chuẩn bị giới tờ.",
        "corrected_text": "Tại Esora, học viên không chỉ được hỗ trợ chọn trường hay chuẩn bị giấy tờ.",
        "topic": "Esora: Đồng hành vượt trên hồ sơ giấy tờ"
    },
    {
        "scene_number": 17,
        "start": 87.30,
        "end": 94.70,
        "raw_text": "Lỗ trình còn cần làm rõ, học gì, tại sao trọng anh này, tại sao trọng Australia và kế hoạt sau tốt nghiệp là gì.",
        "corrected_text": "Lộ trình còn cần làm rõ: Học gì? Tại sao chọn ngành này? Tại sao chọn Australia? Và kế hoạch sau tốt nghiệp là gì?",
        "topic": "Lộ trình 4 câu hỏi định vị của Esora"
    },
    {
        "scene_number": 18,
        "start": 94.70,
        "end": 99.80,
        "raw_text": "Để toàn bộ hồ sơ thể hiện được một mục tiêu hợp tập gió dàng và nhất quán.",
        "corrected_text": "Để toàn bộ hồ sơ thể hiện được một mục tiêu học tập rõ ràng và nhất quán.",
        "topic": "Mục tiêu học tập rõ ràng và nhất quán"
    },
    {
        "scene_number": 19,
        "start": 99.80,
        "end": 108.00,
        "raw_text": "Dù học Australia không chỉ là được chương nhân. Quân trọng là phải xây dựng được một hồ sơ đủ thuyết phục để đi tiếp đến bước vi gia.",
        "corrected_text": "Du học Australia không chỉ là được trường nhận. Quan trọng là phải xây dựng được một hồ sơ đủ thuyết phục để đi tiếp đến bước visa.",
        "topic": "Thư mời nhập học chỉ là bước đầu -> Cán đích Visa"
    },
    {
        "scene_number": 20,
        "start": 108.00,
        "end": 116.04,
        "raw_text": "Nếu gia đình đang chuẩn bị hồ sơ dù học Australia, Hãy liên hệ Esora để được tư vấn lộ trình một mục tiêu hợp với từng học sinh.",
        "corrected_text": "Nếu gia đình đang chuẩn bị hồ sơ du học Australia, hãy liên hệ Esora để được tư vấn lộ trình 1:1 phù hợp với từng học sinh.",
        "topic": "CTA: Tư vấn lộ trình 1:1 cùng chuyên gia Esora"
    }
]

for s in scenes_def:
    s["duration"] = round(s["end"] - s["start"], 2)

output_json = {
    "audio_file": "input_voice/du-hoc-australia-cu-5-visa-bi-tu-choi-1/Generated Audio October 11, 2026 - 11_22AM.wav",
    "total_duration": total_dur,
    "total_scenes": len(scenes_def),
    "scenes": scenes_def,
    "raw_segments": raw_segs
}

Path("scratch").mkdir(exist_ok=True)
with open("scratch/voice_timeline.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, ensure_ascii=False, indent=2)

with open("scratch/voice_timeline.md", "w", encoding="utf-8") as f:
    f.write("# Voice Timeline — Du học Australia: 5 hồ sơ thì 1 bị từ chối Visa?\n\n")
    f.write(f"- **File Audio:** `Generated Audio October 11, 2026 - 11_22AM.wav`\n")
    f.write(f"- **Tổng thời lượng:** {total_dur}s (~1m 56s)\n")
    f.write(f"- **Số phân cảnh:** {len(scenes_def)} scenes\n")
    f.write(f"- **Định dạng:** Vertical 720×1280 (9:16 Shorts / Reels / TikTok)\n\n")
    f.write("| Scene | Khoảng thời gian | Thời lượng | Chủ đề | Lời dẫn (Corrected Text) |\n")
    f.write("| :---: | :---: | :---: | :--- | :--- |\n")
    for s in scenes_def:
        f.write(f"| Scene {s['scene_number']:02d} | {s['start']:05.2f}s – {s['end']:05.2f}s | {s['duration']:4.2f}s | {s['topic']} | {s['corrected_text']} |\n")

print(f"Generated voice timeline for {len(scenes_def)} scenes successfully!")
