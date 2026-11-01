import os
import sys
import subprocess
import hashlib
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot")
BUILD_DIR = BASE_DIR / "build"
RENDERS_DIR = BUILD_DIR / "renders"
INTER_DIR = RENDERS_DIR / "intermediate"
INTER_DIR.mkdir(parents=True, exist_ok=True)

PLAN = [
    ("S01", 181),
    ("S02", 115),
    ("S03", 128),
    ("S04", 121),
    ("S05", 171),
    ("S06", 174),
    ("S07", 140),
    ("S08", 164),
    ("S09", 224),
    ("S10", 184),
    ("S11", 205),
    ("S12", 106),
    ("S13", 136),
    ("S14", 206),
]

def count_frames(video_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-count_packets",
        "-show_entries", "stream=nb_read_packets",
        "-of", "default=nokey=1:noprint_wrappers=1",
        str(video_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return int(res.stdout.strip())

def get_duration(video_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=nokey=1:noprint_wrappers=1",
        str(video_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

concat_list_file = INTER_DIR / "concat.txt"
with open(concat_list_file, "w", encoding="ascii") as clist:
    for sid, target_frames in PLAN:
        src = BUILD_DIR / "scenes" / sid / "renders" / "pilot.mp4"
        dst = INTER_DIR / f"{sid}.mp4"
        print(f"Processing {sid}: target {target_frames} frames from {src.name}...")
        
        cmd = [
            "ffmpeg", "-y",
            "-i", str(src),
            "-frames:v", str(target_frames),
            "-an",
            "-c:v", "libx264",
            "-crf", "15",
            "-preset", "fast",
            "-pix_fmt", "yuv420p",
            "-r", "30",
            str(dst)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        
        actual_frames = count_frames(dst)
        print(f"  {sid}: encoded {actual_frames} frames (expected {target_frames})")
        assert actual_frames == target_frames, f"Frame mismatch in {sid}: {actual_frames} != {target_frames}"
        clist.write(f"file '{sid}.mp4'\n")

total_expected_frames = sum(f for _, f in PLAN)
print(f"\nTotal expected frames: {total_expected_frames}")

# 1. Concat into clean video
clean_video = RENDERS_DIR / "VIDEO-33-clean.mp4"
print(f"\nConcatenating into clean video: {clean_video}...")
cmd_concat = [
    "ffmpeg", "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", str(concat_list_file),
    "-c", "copy",
    str(clean_video)
]
subprocess.run(cmd_concat, capture_output=True, check=True)

clean_frames = count_frames(clean_video)
clean_dur = get_duration(clean_video)
clean_sha = sha256_file(clean_video)
print(f"Clean Video: {clean_frames} frames, {clean_dur:.4f}s, SHA256: {clean_sha}")
assert clean_frames == total_expected_frames, f"Clean video frame mismatch: {clean_frames} != {total_expected_frames}"

# 2. Mux with original audio into master video
master_video = RENDERS_DIR / "VIDEO-33-master.mp4"
source_audio = BASE_DIR / "inputs" / "source_audio.wav"
print(f"\nMuxing with original audio into master video: {master_video}...")

cmd_mux = [
    "ffmpeg", "-y",
    "-i", str(clean_video),
    "-i", str(source_audio),
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "256k",
    str(master_video)
]
subprocess.run(cmd_mux, capture_output=True, check=True)

master_frames = count_frames(master_video)
master_dur = get_duration(master_video)
master_sha = sha256_file(master_video)
print(f"Master Video: {master_frames} frames, {master_dur:.4f}s, SHA256: {master_sha}")
assert master_frames == total_expected_frames, f"Master video frame mismatch: {master_frames} != {total_expected_frames}"

print("\nSUCCESS! Assembly verified perfectly.")
