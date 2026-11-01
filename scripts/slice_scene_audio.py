import json
import subprocess
from pathlib import Path

with open("scratch/voice_timeline.json", "r", encoding="utf-8") as f:
    tl = json.load(f)

input_audio = Path("input_voice/du-hoc-australia-cu-5-visa-bi-tu-choi-1/Generated Audio October 11, 2026 - 11_22AM.wav")
output_dir = Path("scratch/audio_slices")
output_dir.mkdir(parents=True, exist_ok=True)

for sc in tl["scenes"]:
    num = sc["scene_number"]
    start = sc["start"]
    duration = sc["duration"]
    out_file = output_dir / f"scene_{num:02d}.wav"
    
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start),
        "-t", str(duration),
        "-i", str(input_audio),
        "-c", "copy",
        str(out_file)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"Sliced Scene {num:02d}: {start:.2f}s -> {start+duration:.2f}s ({duration:.2f}s) to {out_file.name}")

print("All 20 scene audio slices created successfully!")
