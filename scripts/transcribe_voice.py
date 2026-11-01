import os
import sys
import json
from pathlib import Path

# Force UTF-8 encoding for standard outputs
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from faster_whisper import WhisperModel

AUDIO_PATH = Path("input_voice/Generated Audio October 08, 2026 - 8_40PM.wav")
OUTPUT_JSON = Path("scratch/voice_timeline.json")
OUTPUT_MD = Path("scratch/voice_timeline.md")

print(f"Loading Whisper model (base)...")
model = WhisperModel("base", device="cpu", compute_type="int8")

import wave
import numpy as np

print(f"Reading {AUDIO_PATH}...")
with wave.open(str(AUDIO_PATH), "rb") as w:
    frames = w.readframes(w.getnframes())
    rate = w.getframerate()
    audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0

target_rate = 16000
if rate != target_rate:
    print(f"Resampling from {rate}Hz to {target_rate}Hz...")
    num_samples = int(len(audio) * target_rate / rate)
    audio_16k = np.interp(
        np.linspace(0, len(audio), num_samples, endpoint=False),
        np.arange(len(audio)),
        audio
    ).astype(np.float32)
else:
    audio_16k = audio

print(f"Transcribing audio ({len(audio_16k)/target_rate:.2f}s)...")
segments, info = model.transcribe(audio_16k, beam_size=5, language="vi")

print(f"Detected language: {info.language} with probability {info.language_probability:.2f}")

raw_segments = []
for seg in segments:
    raw_segments.append({
        "start": round(seg.start, 2),
        "end": round(seg.end, 2),
        "duration": round(seg.end - seg.start, 2),
        "text": seg.text.strip()
    })

# Group segments into scene chunks of roughly 4s - 8s (perfect for Flow clips)
scenes = []
current_scene = None

for s in raw_segments:
    if not current_scene:
        current_scene = {
            "start": s["start"],
            "end": s["end"],
            "text": s["text"]
        }
    else:
        tentative_duration = s["end"] - current_scene["start"]
        # If adding this keeps duration <= 8s, or if current duration is too short (< 4s), merge
        if tentative_duration <= 8.5 or (current_scene["end"] - current_scene["start"]) < 3.5:
            current_scene["end"] = s["end"]
            current_scene["text"] += " " + s["text"]
        else:
            current_scene["duration"] = round(current_scene["end"] - current_scene["start"], 2)
            scenes.append(current_scene)
            current_scene = {
                "start": s["start"],
                "end": s["end"],
                "text": s["text"]
            }

if current_scene:
    current_scene["duration"] = round(current_scene["end"] - current_scene["start"], 2)
    scenes.append(current_scene)

# Assign scene indices
for i, sc in enumerate(scenes, 1):
    sc["scene_number"] = i

OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump({"raw_segments": raw_segments, "scenes": scenes}, f, ensure_ascii=False, indent=2)

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write("# Timeline Phân Cảnh từ Voice Diễn Giả\n\n")
    f.write(f"- **Tổng thời lượng**: {raw_segments[-1]['end'] if raw_segments else 0} giây\n")
    f.write(f"- **Số phân cảnh dự kiến**: {len(scenes)} cảnh\n\n")
    f.write("| Cảnh | Thời gian (Start - End) | Thời lượng | Lời thoại diễn giả |\n")
    f.write("| :---: | :---: | :---: | :--- |\n")
    for sc in scenes:
        f.write(f"| Scene {sc['scene_number']} | {sc['start']:.1f}s - {sc['end']:.1f}s | {sc['duration']}s | {sc['text']} |\n")

print(f"Transcription complete! Created {len(scenes)} scenes.")
print(f"Saved to {OUTPUT_JSON} and {OUTPUT_MD}")
