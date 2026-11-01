"""Render updated sample clip:
- REMOVED lower subtitles (user will do subtitles themselves).
- FIXED text alignment: dynamically measure text dimensions with textbbox for pixel-perfect centering.
- Expand popup card width (640px) so text never overflows.
- Highlight bar is perfectly centered and hugs the highlighted text.
- Removed unsupported emoji in top badge.
"""
import math
import wave
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import av

INPUT_IMG_PATH = Path("scratch/test_scene_2_orange_white.jpg")
INPUT_AUDIO_PATH = Path("input_voice/Generated Audio October 08, 2026 - 8_40PM.wav")
OUTPUT_VIDEO_PATH = Path("output/du_hoc_canada/demo_scene_2_orange_white.mp4")
OUTPUT_VIDEO_PATH.parent.mkdir(parents=True, exist_ok=True)

START_SEC = 4.36
END_SEC = 10.28
DURATION = END_SEC - START_SEC  # ~5.92s
FPS = 30
TOTAL_FRAMES = int(DURATION * FPS)
WIDTH = 720
HEIGHT = 1280

# Load fonts
FONT_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
font_top = ImageFont.truetype(FONT_BOLD, 28)
font_card_sub = ImageFont.truetype(FONT_BOLD, 28)
font_card_main = ImageFont.truetype(FONT_BOLD, 42)
font_popup1_title = ImageFont.truetype(FONT_BOLD, 32)
font_popup1_desc = ImageFont.truetype(FONT_BOLD, 26)

# Brand Colors (Orange - White Theme)
BRAND_ORANGE = (255, 107, 43)
BRAND_WHITE = (255, 255, 255)
CHARCOAL = (30, 41, 59)
LIGHT_ORANGE_BG = (255, 243, 235)
YELLOW_ORANGE_HL = (255, 205, 87)
GRAY_TEXT = (100, 116, 139)

base_img = Image.open(INPUT_IMG_PATH).convert("RGBA")
orig_w, orig_h = base_img.size

# Extract audio slice
print(f"Extracting audio slice {START_SEC:.2f}s - {END_SEC:.2f}s...")
with wave.open(str(INPUT_AUDIO_PATH), "rb") as w:
    audio_rate = w.getframerate()
    audio_channels = w.getnchannels()
    sampwidth = w.getsampwidth()
    w.setpos(int(START_SEC * audio_rate))
    num_audio_frames = int(DURATION * audio_rate)
    raw_audio_bytes = w.readframes(num_audio_frames)

audio_samples = np.frombuffer(raw_audio_bytes, dtype=np.int16)

def ease_out_back(x):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

print(f"Rendering {TOTAL_FRAMES} frames ({DURATION:.2f}s) at {FPS} FPS...")
container = av.open(str(OUTPUT_VIDEO_PATH), mode="w")

# Video stream
v_stream = container.add_stream("h264", rate=FPS)
v_stream.width = WIDTH
v_stream.height = HEIGHT
v_stream.pix_fmt = "yuv420p"
v_stream.options = {"crf": "18", "preset": "fast"}

# Audio stream (AAC)
a_stream = container.add_stream("aac", rate=audio_rate)
a_stream.layout = "mono"
a_stream.format = "fltp"

for frame_idx in range(TOTAL_FRAMES):
    t = frame_idx / FPS

    # 1. Background subtle camera zoom (1.0 -> 1.05x)
    zoom = 1.0 + 0.05 * (t / DURATION)
    crop_w = int(orig_w / zoom)
    crop_h = int(orig_h / zoom)
    left = (orig_w - crop_w) // 2
    top = int((orig_h - crop_h) * 0.4)
    cropped = base_img.crop((left, top, left + crop_w, top + crop_h))
    frame_canvas = cropped.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS).convert("RGBA")

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 2. TOP BANNER (DU HỌC CANADA) - Perfectly centered Orange Pill
    pill_text = "DU HỌC CANADA"
    tb_box = draw.textbbox((0, 0), pill_text, font=font_top)
    tb_w = tb_box[2] - tb_box[0]
    pill_w = tb_w + 64
    pill_h = 50
    pill_x0 = (WIDTH - pill_w) // 2
    pill_y0 = 60
    pill_x1 = pill_x0 + pill_w
    pill_y1 = pill_y0 + pill_h

    # Shadow & Pill
    draw.rounded_rectangle([pill_x0, pill_y0 + 4, pill_x1, pill_y1 + 4], radius=25, fill=(0, 0, 0, 30))
    draw.rounded_rectangle([pill_x0, pill_y0, pill_x1, pill_y1], radius=25, fill=(BRAND_ORANGE[0], BRAND_ORANGE[1], BRAND_ORANGE[2], 245))
    draw.text((pill_x0 + 32, pill_y0 + 10), pill_text, font=font_top, fill=BRAND_WHITE)

    # 3. POPUP 1: "THAY ĐỔI QUAN TRỌNG" (t=1.8s to 3.8s)
    if 1.8 <= t < 3.8:
        progress = (t - 1.8) / 0.35
        scale = max(0.01, ease_out_back(progress)) if progress < 1.0 else 1.0

        card_w = int(580 * scale)
        card_h = int(120 * scale)
        card_cx = WIDTH // 2
        card_cy = 220
        cx0 = card_cx - card_w // 2
        cy0 = card_cy - card_h // 2
        cx1 = cx0 + card_w
        cy1 = cy0 + card_h

        draw.rounded_rectangle([cx0, cy0 + 6, cx1, cy1 + 6], radius=24, fill=(0, 0, 0, 35))
        draw.rounded_rectangle([cx0, cy0, cx1, cy1], radius=24, fill=(255, 255, 255, 250), outline=BRAND_ORANGE, width=3)

        if scale > 0.85:
            p1_title = "THAY ĐỔI TÀI CHÍNH QUAN TRỌNG"
            p1_desc = "Cập nhật chính sách mới từ IRCC"
            
            b1 = draw.textbbox((0, 0), p1_title, font=font_popup1_title)
            b2 = draw.textbbox((0, 0), p1_desc, font=font_popup1_desc)
            
            w1 = b1[2] - b1[0]
            w2 = b2[2] - b2[0]
            
            draw.text((card_cx - w1 // 2, cy0 + 22), p1_title, font=font_popup1_title, fill=BRAND_ORANGE)
            draw.text((card_cx - w2 // 2, cy0 + 68), p1_desc, font=font_popup1_desc, fill=CHARCOAL)

    # 4. POPUP 2: "CHÍNH THỨC ÁP DỤNG" & "TỪ NGÀY 01 THÁNG 09" (t=3.8s to end)
    if t >= 3.8:
        p2_time = t - 3.8
        p2_intro = min(1.0, p2_time / 0.3)
        scale2 = ease_out_back(p2_intro) if p2_intro < 1.0 else 1.0

        box_w = int(640 * scale2)
        box_h = int(150 * scale2)
        box_cx = WIDTH // 2
        box_cy = 220
        bx0 = box_cx - box_w // 2
        by0 = box_cy - box_h // 2
        bx1 = bx0 + box_w
        by1 = by0 + box_h

        draw.rounded_rectangle([bx0, by0 + 8, bx1, by1 + 8], radius=28, fill=(0, 0, 0, 40))
        draw.rounded_rectangle([bx0, by0, bx1, by1], radius=28, fill=(255, 255, 255, 250), outline=BRAND_ORANGE, width=4)

        if scale2 > 0.85:
            txt_sub = "CHÍNH THỨC ÁP DỤNG"
            txt_main = "TỪ NGÀY 01 THÁNG 09"

            sub_b = draw.textbbox((0, 0), txt_sub, font=font_card_sub)
            main_b = draw.textbbox((0, 0), txt_main, font=font_card_main)

            sub_w = sub_b[2] - sub_b[0]
            main_w = main_b[2] - main_b[0]

            sub_x = box_cx - sub_w // 2
            sub_y = by0 + 24
            main_x = box_cx - main_w // 2
            main_y = by0 + 72

            draw.text((sub_x, sub_y), txt_sub, font=font_card_sub, fill=GRAY_TEXT)

            hl_start_t = 4.2
            if t >= hl_start_t:
                hl_prog = min(1.0, (t - hl_start_t) / 0.35)
                hl_pad_x = 12
                total_hl_w = main_w + hl_pad_x * 2
                curr_hl_w = int(total_hl_w * hl_prog)
                hl_x0 = main_x - hl_pad_x
                hl_y0 = main_y + 12
                hl_y1 = hl_y0 + 38
                # Warm orange-yellow highlighter
                draw.rounded_rectangle([hl_x0, hl_y0, hl_x0 + curr_hl_w, hl_y1], radius=8, fill=(YELLOW_ORANGE_HL[0], YELLOW_ORANGE_HL[1], YELLOW_ORANGE_HL[2], 220))

            draw.text((main_x, main_y), txt_main, font=font_card_main, fill=CHARCOAL)

    # Composite frame
    final_frame = Image.alpha_composite(frame_canvas, overlay).convert("RGB")
    v_frame = av.VideoFrame.from_ndarray(np.array(final_frame), format="rgb24")
    for packet in v_stream.encode(v_frame):
        container.mux(packet)

# Flush video stream
for packet in v_stream.encode(None):
    container.mux(packet)

# Encode audio stream
audio_float = (audio_samples.astype(np.float32) / 32768.0)
frame_size = 1024
for i in range(0, len(audio_float), frame_size):
    chunk = audio_float[i:i + frame_size]
    if len(chunk) < frame_size:
        chunk = np.pad(chunk, (0, frame_size - len(chunk)))
    a_frame = av.AudioFrame.from_ndarray(chunk.reshape(1, -1), format="fltp", layout="mono")
    a_frame.sample_rate = audio_rate
    for packet in a_stream.encode(a_frame):
        container.mux(packet)

for packet in a_stream.encode(None):
    container.mux(packet)

container.close()
print(f"Done! Re-rendered video: {OUTPUT_VIDEO_PATH} ({OUTPUT_VIDEO_PATH.stat().st_size} bytes)")
