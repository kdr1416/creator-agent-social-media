import os
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot")
S02_P = PROJECT_ROOT / "revisions" / "S02-approved-frame-motion-r1" / "renders" / "pilot.mp4"
S03_P = PROJECT_ROOT / "revisions" / "S03-motion-r1" / "renders" / "pilot.mp4"
SOURCE_WAV = PROJECT_ROOT / "inputs" / "source_audio.wav"

OUT_DIR = PROJECT_ROOT / "revisions" / "S03-motion-r1" / "seam_checks"
OUT_DIR.mkdir(parents=True, exist_ok=True)

s02_115 = OUT_DIR / "s02_conformed.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(S02_P), "-frames:v", "115", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", str(s02_115)], check=True)

s03_128 = OUT_DIR / "s03_conformed.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(S03_P), "-frames:v", "128", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", str(s03_128)], check=True)

concat_list = OUT_DIR / "concat.txt"
with open(concat_list, "w", encoding="utf-8") as f:
    f.write(f"file '{s02_115.as_posix()}'\n")
    f.write(f"file '{s03_128.as_posix()}'\n")

vid_concat = OUT_DIR / "vid_concat.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(vid_concat)], check=True)

# Mux with source audio from t=6.0333s to 14.1333s (duration 8.100s)
clip_with_audio = OUT_DIR / "cluster_S02_S03.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-i", str(vid_concat),
    "-ss", "6.0333", "-t", "8.1000",
    "-i", str(SOURCE_WAV),
    "-c:v", "copy",
    "-c:a", "aac", "-ar", "24000", "-b:a", "192k",
    str(clip_with_audio)
], check=True)

# Seam S02 -> S03: around boundary frame 115 (3.833s in this clip) -> extract [2.833s, 4.833s]
seam_02 = OUT_DIR / "seam_02_S02_S03_new.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-ss", "2.8333", "-i", str(clip_with_audio),
    "-t", "2.0000",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    str(seam_02)
], check=True)

print("S02->S03 seam and cluster generated successfully!")
