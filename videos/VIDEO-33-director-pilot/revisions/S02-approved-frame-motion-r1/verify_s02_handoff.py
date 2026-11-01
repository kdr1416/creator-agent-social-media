import os
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot")
S01_CONF = PROJECT_ROOT / "build" / "master-approved-r1" / "intermediate" / "S01_conformed.mp4"
S02_CONF = PROJECT_ROOT / "build" / "master-approved-r1" / "intermediate" / "S02_conformed_new.mp4"
S03_CONF = PROJECT_ROOT / "build" / "master-approved-r1" / "intermediate" / "S03_conformed.mp4"
SOURCE_WAV = PROJECT_ROOT / "inputs" / "source_audio.wav"

OUT_DIR = PROJECT_ROOT / "revisions" / "S02-approved-frame-motion-r1" / "seam_checks"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. Concat S01 + S02 + S03 (total 181 + 115 + 128 = 424 frames = 14.1333s)
concat_list = OUT_DIR / "concat_list.txt"
with open(concat_list, "w", encoding="utf-8") as f:
    f.write(f"file '{S01_CONF.as_posix()}'\n")
    f.write(f"file '{S02_CONF.as_posix()}'\n")
    f.write(f"file '{S03_CONF.as_posix()}'\n")

cluster_video = OUT_DIR / "cluster_video.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(cluster_video)], check=True)

# Mux with original audio (0 - 14.133s)
cluster_with_audio = OUT_DIR / "cluster_S01_S02_S03.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-i", str(cluster_video),
    "-ss", "0", "-t", "14.1333",
    "-i", str(SOURCE_WAV),
    "-c:v", "copy",
    "-c:a", "aac", "-ar", "24000", "-b:a", "192k",
    str(cluster_with_audio)
], check=True)

# Extract Seam 01 (S01 -> S02, boundary 6.033s): range [5.033s, 7.033s]
seam_01 = OUT_DIR / "seam_01_S01_S02.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-ss", "5.0333", "-i", str(cluster_with_audio),
    "-t", "2.0000",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    str(seam_01)
], check=True)

# Extract Seam 02 (S02 -> S03, boundary 9.867s): range [8.867s, 10.867s]
seam_02 = OUT_DIR / "seam_02_S02_S03.mp4"
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-ss", "8.8667", "-i", str(cluster_with_audio),
    "-t", "2.0000",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    str(seam_02)
], check=True)

print("Cluster MP4 and Seam clips generated successfully!")
