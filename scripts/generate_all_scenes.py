"""Generate all scenes for Du Hoc Canada Explainer Video using Google Flow Omni Flash."""
import json
import time
import urllib.request
from pathlib import Path

API_BASE = "http://127.0.0.1:8100"
PROJECT_ID = "e0f85a1a-6bac-443f-a734-d9a450cf4d4d"
OUTPUT_DIR = Path("output/du_hoc_canada")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

STYLE_PREFIX = (
    "Modern 2D vector animation illustration style, ultra clean minimalist white background "
    "with subtle pale geometric lines, modern tech corporate explainer motion graphics aesthetic, "
    "zero background clutter, crisp vector outlines, modern fresh color palette of navy blue, "
    "soft sky blue, cheerful warm orange, and crisp white. Relatable, approachable, friendly, "
    "trustworthy educational atmosphere, vertical 9:16 aspect ratio. "
)

# Scene definitions (Scenes 2 to 17, Scene 1 is user's real footage)
SCENES = [
    {
        "id": "scene_02",
        "title": "Cảnh 2: Lịch 1/9 và thay đổi tài chính",
        "duration_s": 6,
        "media_id": "453d755b-844b-4fb5-b2cb-2f1bcaf5da02",  # Already generated approved V4
        "image_prompt": "Already created V4",
        "video_prompt": (
            "Gentle 2D motion graphics animation, the parents and student smile warmly as they look at the laptop, "
            "the blue chart arrow on the calendar marked 1/9 pulses smoothly upward, clean vector motion, subtle happy head nods, "
            "educational corporate explainer animation"
        ),
    },
    {
        "id": "scene_03",
        "title": "Cảnh 3: Mức tăng 23.400 CAD (~440 triệu)",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "A cheerful Asian teenage student wearing a stylish orange hoodie and backpack standing beside "
            "a large modern financial infographic pillar displaying prominent bold text '$23,400 CAD' "
            "and '~440 Triệu VNĐ' with subtle gold coin icons and a small clean Canadian red maple leaf badge. "
            "Clean white minimalist background, bright confident expression, vertical 9:16."
        ),
        "video_prompt": (
            "Gentle 2D motion animation, the student gestures proudly toward the financial pillar, "
            "the numbers and maple leaf icon have a soft modern glow, subtle coin floating animation, friendly educational motion"
        ),
    },
    {
        "id": "scene_04",
        "title": "Cảnh 4: Chưa gồm học phí và chi phí di chuyển",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "Two distinct modern infographic cards floating on a clean white background: one card with a graduation cap icon for 'Học Phí' (Tuition), "
            "the other card with a modern airplane icon for 'Vé Máy Bay' (Flights), with an elegant plus sign '+ Tuition & Flights'. "
            "A relatable student and parent thoughtfully examining the checklist with curiosity, vertical 9:16."
        ),
        "video_prompt": (
            "Clean 2D vector animation, the two infographic cards float smoothly with subtle bouncing motion, "
            "the student and parent nod in thoughtful agreement, clean motion graphics"
        ),
    },
    {
        "id": "scene_05",
        "title": "Cảnh 5: Đi một mình tăng 553 CAD theo IRCC",
        "duration_s": 8,
        "image_prompt": (
            STYLE_PREFIX +
            "A smart Asian student holding a neat blue study permit passport booklet, next to an official minimalist badge with bold text 'IRCC' "
            "and a prominent rising metric '+553 CAD' in a modern speech bubble. Clean minimalist white background with faint vector lines, vertical 9:16."
        ),
        "video_prompt": (
            "Gentle 2D vector motion, the student smiles and looks at the passport, "
            "the IRCC metric badge gently pulses, crisp modern corporate explainer animation"
        ),
    },
    {
        "id": "scene_06",
        "title": "Cảnh 6: Đi cùng gia đình tăng theo số người",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "The relatable friendly Asian family (father, mother, and teenage student) walking together with modern travel suitcases, "
            "friendly smiling faces, with cute subtle floating family badges '+1', '+2' indicating family members. "
            "Ultra clean minimalist white background, warm and supportive atmosphere, vertical 9:16."
        ),
        "video_prompt": (
            "Smooth 2D walk cycle animation, the loving family walks forward cheerfully wheeling their suitcases, "
            "warm smiles and happy family bonding, clean vector motion"
        ),
    },
    {
        "id": "scene_07",
        "title": "Cảnh 7: Bảng số liệu chi phí theo số người",
        "duration_s": 8,
        "image_prompt": (
            STYLE_PREFIX +
            "A clean modern 3-tiered infographic bar chart comparison on pure white background: "
            "Tier 1: '2 Người ➔ ~550 Triệu', "
            "Tier 2: '4 Người ➔ ~820 Triệu', "
            "Tier 3: '7 Người ➔ ~1,16 Tỷ'. "
            "Vibrant blue and warm orange graphic bars, modern typography, ultra clean, professional finance explainer graphic, vertical 9:16."
        ),
        "video_prompt": (
            "Dynamic 2D motion graphics, the three graphic bars animate and rise sequentially from bottom to top, "
            "the numbers count up smoothly, crisp and clear infographic animation"
        ),
    },
    {
        "id": "scene_08",
        "title": "Cảnh 8: Phương án tài chính nhiều năm học",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "A sleek modern horizontal timeline roadmap on clean white background with 4 connected milestone nodes: "
            "'Năm 1', 'Năm 2', 'Năm 3', 'Năm 4' leading to a graduation cap icon. "
            "The supportive parents reviewing the roadmap with confidence and calm smiles, vertical 9:16."
        ),
        "video_prompt": (
            "Smooth 2D motion graphics, a bright light pulse travels along the roadmap connecting the year milestones, "
            "the parents smile approvingly, reassuring educational motion"
        ),
    },
    {
        "id": "scene_09",
        "title": "Cảnh 9: Quy định riêng tại Quebec và CAQ",
        "duration_s": 8,
        "image_prompt": (
            STYLE_PREFIX +
            "A stylish minimalist stylized map silhouette of Quebec province in royal blue with an official golden stamp badge 'CAQ Quy Trình Riêng', "
            "alongside a bold text card '> 24,600 CAD (~460 Triệu)'. Clean minimalist white background, clear educational infographic, vertical 9:16."
        ),
        "video_prompt": (
            "Clean 2D vector animation, the CAQ stamp gently imprints onto the Quebec map graphic, "
            "the financial metric card slides in smoothly from the side, crisp explainer motion"
        ),
    },
    {
        "id": "scene_10",
        "title": "Cảnh 10: Tài chính không chỉ là đủ tiền nộp hồ sơ",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "The caring Asian father and mother sitting at a clean modern white desk with a laptop, looking thoughtful and responsible, "
            "a glowing bright lightbulb idea icon floating above, symbolizing smart long-term planning. "
            "Zero background clutter, ultra clean minimalist white backdrop, vertical 9:16."
        ),
        "video_prompt": (
            "Gentle 2D animation, the lightbulb icon softly glows, the parents exchange an understanding warm glance and nod, "
            "thoughtful and responsible atmosphere"
        ),
    },
    {
        "id": "scene_11",
        "title": "Cảnh 11: 4 yếu tố cần tính trước",
        "duration_s": 8,
        "image_prompt": (
            STYLE_PREFIX +
            "A beautiful modern circular infographic with 4 clean vector icons orbiting: "
            "1. Graduation cap (Học Phí), 2. Cozy House (Chi Phí Sinh Hoạt), 3. Airplane (Đi Lại), 4. Growth Chart (Dài Hạn). "
            "Clean white background, vibrant harmonious colors, clean layout, vertical 9:16."
        ),
        "video_prompt": (
            "Smooth 2D motion graphics, the four icons gently orbit in a circular motion around the center, "
            "each icon lightly pulsing in turn, hypnotic clean explainer animation"
        ),
    },
    {
        "id": "scene_12",
        "title": "Cảnh 12: Canada siết chặt và kiểm soát chỉ tiêu",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "A stylized modern magnifying glass closely examining a clean visa application dossier with a green checkmark shield of quality, "
            "representing thorough rigorous review and high standards. Clean white background with geometric accents, vertical 9:16."
        ),
        "video_prompt": (
            "Clean 2D vector animation, the magnifying glass smoothly scans across the visa dossier, "
            "the green shield icon gleams with a subtle shine of approval, professional motion"
        ),
    },
    {
        "id": "scene_13",
        "title": "Cảnh 13: Trung tâm Esora đồng hành toàn diện",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "A welcoming, elegant, modern education counseling office with an illuminated clean logo sign 'ESORA' on the wall. "
            "A professional, friendly, and smiling Asian educational consultant wearing a neat blazer warmly greeting the family. "
            "Ultra clean bright interior, trustworthy and professional, vertical 9:16."
        ),
        "video_prompt": (
            "Gentle 2D motion, the friendly Esora consultant warmly welcomes the family with a polite hand gesture and beaming smile, "
            "inviting and trustworthy atmosphere"
        ),
    },
    {
        "id": "scene_14",
        "title": "Cảnh 14: Lộ trình định hướng trường, ngành, học bổng",
        "duration_s": 8,
        "image_prompt": (
            STYLE_PREFIX +
            "The friendly female Esora counselor standing beside a clear modern interactive screen showing a clear 4-step pathway: "
            "'Trường Học ➔ Ngành Học ➔ Học Bổng ➔ Tài Chính'. "
            "The student and parents looking at the pathway with immense relief and excitement, vertical 9:16."
        ),
        "video_prompt": (
            "Clean 2D animation, the counselor points to each step on the interactive pathway as they light up in succession, "
            "the student and parents smile with deep clarity and confidence"
        ),
    },
    {
        "id": "scene_15",
        "title": "Cảnh 15: Hồ sơ phù hợp năng lực tài chính & đậu visa",
        "duration_s": 8,
        "image_prompt": (
            STYLE_PREFIX +
            "A joyful moment where a large green 'VISA APPROVED' stamp firmly marks a study permit document. "
            "The Asian student holding the approved visa grinning with happiness, the parents proudly patting the student's shoulder. "
            "Celebratory, heartwarming, ultra clean white backdrop, vertical 9:16."
        ),
        "video_prompt": (
            "Heartwarming 2D animation, the green stamp presses down with a subtle sparkle of stars, "
            "the student smiles widely and raises the passport in triumph, proud emotional parents"
        ),
    },
    {
        "id": "scene_16",
        "title": "Cảnh 16: Kêu gọi hành động tư vấn 1:1 Esora",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "A prominent modern Call-To-Action card on pure white background: "
            "Bold clean text 'ESORA - TƯ VẤN LỘ TRÌNH 1:1', an elegant phone/hotline button icon, and a modern chat consultation bubble. "
            "Clean royal blue and warm orange accents, extremely clear and engaging, vertical 9:16."
        ),
        "video_prompt": (
            "Engaging 2D motion graphics, the consultation CTA card smoothly pulses, "
            "the phone and chat icon animate with friendly inviting waves, crisp commercial ending motion"
        ),
    },
    {
        "id": "scene_17",
        "title": "Cảnh 17: Chuẩn bị sớm, tự tin bước vào tương lai",
        "duration_s": 6,
        "image_prompt": (
            STYLE_PREFIX +
            "The confident Asian teenage student with backpack and suitcase walking forward toward a beautiful sunny modern Canadian university campus in the distance, "
            "autumn red maple trees, golden sunlight, look of pure optimism and confidence, back-turned slightly smiling over shoulder, vertical 9:16."
        ),
        "video_prompt": (
            "Inspiring 2D vector animation, the student walks toward the campus as warm golden sunlight gently rays across the screen, "
            "a red maple leaf drifts softly in the breeze, uplifting and emotional finale"
        ),
    },
]

print(f"Total AI scenes to generate: {len(SCENES)} scenes (from Scene 2 to Scene 17)")
with open(OUTPUT_DIR / "scenes_manifest.json", "w", encoding="utf-8") as f:
    json.dump(SCENES, f, ensure_ascii=False, indent=2)
print(f"Saved manifest to {OUTPUT_DIR / 'scenes_manifest.json'}")
