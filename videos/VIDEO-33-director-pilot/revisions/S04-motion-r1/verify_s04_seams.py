import os
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot")
S03_P = PROJECT_ROOT / "revisions" / "S03-motion-r1" / "renders" / "pilot.mp4"
S04_P = PROJECT_ROOT / "revisions" / "S04-motion-r1" / "renders" / "pilot.mp4"
S05_P = PROJECT_ROOT / "revisions" / "S05-zoom-motion-r1" / "renders" / "pilot.mp4"
SOURCE_WAV = PROJECT_ROOT / "inputs" / "source_audio.wav"

OUT_DIR = PROJECT_ROOT / "revisions" / "S04-motion-r1" / "seam_checks"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# S03 is 128 frames (target 128)
# S04 is 121 frames (target 121)
# S05 is 172 frames, target is 171 frames (-1 tail frame)

s03_conf = OUT_DIR / "s03_conformed.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(S03_P), "-frames:v", "128", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", str(s03_conf)], check=True)

s04_conf = OUT_DIR / "s04_conformed.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(S04_P), "-frames:v", "121", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", str(s04_conf)], check=True)

s05_conf = OUT_DIR / "s05_conformed.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(S05_P), "-frames:v", "171", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", str(s05_conf)], check=True)

# Concat S03 + S04 + S05 (total 128 + 121 + 171 = 420 frames = 14.000s)
# S03 starts at 9.8667s, ends at 14.1333s
# S04 starts at 14.1333s, ends at 18.1667s
# S05 starts at 18.1667s, ends at 23.8667s

concat_list = OUT_DIR / "concat.txt"
with open(concat_list, "w", encoding="utf-8") as f:
    f.write(f"file '{s03_conf.as_posix()}'\n")
    f.write(f"file '{s04_conf.as_posix()}'\n")
    f.write(f"file '{s05_conf.as_posix()}'\n")

vid_concat = OUT_DIR / "vid_concat.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(vid_concat)], check=True)

# Mux with source audio from t=9.8667s to 23.8667s (duration 14.000s)
clip_with_audio = OUT_DIR / "cluster_S03_S04_S05.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-i", str(vid_concat),
    "-ss", "9.8667", "-t", "14.0000",
    "-i", str(SOURCE_WAV),
    "-c:v", "copy",
    "-c:a", "aac", "-ar", "24000", "-b:a", "192k",
    str(clip_with_audio)
], check=True)

# Seam S03 -> S04: boundary frame 128 (4.2667s in clip) -> extract [3.2667s, 5.2667s]
seam_03 = OUT_DIR / "seam_03_S03_S04_new.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-ss", "3.2667", "-i", str(clip_with_audio),
    "-t", "2.0000",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    str(seam_03)
], check=True)

# Seam S04 -> S05: boundary frame 128+121 = 249 (8.3000s in clip) -> extract [7.3000s, 9.3000s]
seam_04 = OUT_DIR / "seam_04_S04_S05_new.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-ss", "7.3000", "-i", str(clip_with_audio),
    "-t", "2.0000",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    str(seam_04)
], check=True)

print("Cluster S03-S04-S05 and seam clips generated successfully!")
