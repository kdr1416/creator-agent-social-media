import os
import sys
import json
import hashlib
import subprocess
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(r"D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot")
OUTPUT_DIR = PROJECT_ROOT / "build" / "master-approved-r2"
MANIFEST_PATH = OUTPUT_DIR / "ASSEMBLY_MANIFEST_R2.json"
INTERMEDIATE_DIR = OUTPUT_DIR / "intermediate"
SEAMS_DIR = OUTPUT_DIR / "seams"
PROOFS_DIR = OUTPUT_DIR / "proofs"

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def get_video_stream_info(filepath):
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-count_frames",
        "-show_entries", "stream=nb_read_frames,r_frame_rate,width,height,pix_fmt,codec_name,duration",
        "-of", "json",
        str(filepath)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = json.loads(res.stdout)
    return data["streams"][0]

def get_audio_stream_info(filepath):
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=codec_name,sample_rate,channels,channel_layout,duration,duration_ts,bit_rate",
        "-of", "json",
        str(filepath)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = json.loads(res.stdout)
    return data["streams"][0]

def main():
    print("=== STEP 1: Verify Manifest & Inputs ===")
    assert MANIFEST_PATH.exists(), f"Manifest not found: {MANIFEST_PATH}"
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    INTERMEDIATE_DIR.mkdir(parents=True, exist_ok=True)
    SEAMS_DIR.mkdir(parents=True, exist_ok=True)
    PROOFS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Verify voice
    voice_path = Path(manifest["voice"]["absolute_path"])
    assert voice_path.exists(), f"Voice file not found: {voice_path}"
    voice_sha = sha256_file(voice_path)
    assert voice_sha == manifest["voice"]["sha256"], f"Voice SHA mismatch: expected {manifest['voice']['sha256']}, got {voice_sha}"
    print(f"Voice SHA OK: {voice_sha}")

    # 2. Verify old masters
    for old_m in manifest["old_masters"]:
        old_path = Path(old_m["path"])
        if old_path.exists():
            old_sha = sha256_file(old_path)
            print(f"Old master verified: {old_m['label']} -> {old_sha[:16]}...")
        else:
            print(f"Warning: Old master not found: {old_path}")

    # 3. Verify input scenes
    scenes_info = []
    total_target_frames = 0
    for scene in manifest["scenes"]:
        scene_id = scene["scene_id"]
        scene_path = Path(scene["absolute_video_path"])
        assert scene_path.exists(), f"Scene video not found: {scene_path}"
        scene_sha = sha256_file(scene_path)
        assert scene_sha == scene["sha256"], f"Scene {scene_id} SHA mismatch: expected {scene['sha256']}, got {scene_sha}"
        
        vinfo = get_video_stream_info(scene_path)
        actual_frames = int(vinfo["nb_read_frames"])
        target_frames = scene["target_frames"]
        total_target_frames += target_frames
        
        print(f"[{scene_id}] SHA OK | actual_frames={actual_frames} target={target_frames} tail_adj={scene['tail_adjustment_frames']}")
        scenes_info.append({
            "scene": scene,
            "path": scene_path,
            "actual_frames": actual_frames,
            "target_frames": target_frames,
            "tail_adj": scene["tail_adjustment_frames"]
        })

    assert total_target_frames == 2255, f"Total target frames is {total_target_frames}, expected 2255"
    print(f"All 14 scenes verified. Total target frames: {total_target_frames}")

    print("\n=== STEP 2: Conforming Intermediate Scene Clips ===")
    conformed_clips = []
    concat_list_path = INTERMEDIATE_DIR / "concat_list.txt"
    
    with open(concat_list_path, "w", encoding="utf-8") as f_concat:
        for item in scenes_info:
            s_id = item["scene"]["scene_id"]
            in_path = item["path"]
            target = item["target_frames"]
            out_clip = INTERMEDIATE_DIR / f"{s_id}_conformed.mp4"
            
            # Use ffmpeg -frames:v target to take exact first target frames [0, target-1]
            cmd = [
                "ffmpeg", "-y", "-v", "error",
                "-i", str(in_path),
                "-frames:v", str(target),
                "-an",
                "-c:v", "libx264", "-preset", "fast", "-crf", "17",
                "-pix_fmt", "yuv420p", "-r", "30",
                str(out_clip)
            ]
            subprocess.run(cmd, check=True)
            
            # Verify conformed frame count
            vinfo_conf = get_video_stream_info(out_clip)
            conf_frames = int(vinfo_conf["nb_read_frames"])
            assert conf_frames == target, f"Conformed {s_id} frame mismatch: {conf_frames} vs {target}"
            print(f"Conformed {s_id}: exact {conf_frames} frames -> {out_clip.name}")
            
            # Write line for concat demuxer (using relative or forward slash paths)
            f_concat.write(f"file '{out_clip.as_posix()}'\n")
            conformed_clips.append(out_clip)

    print("\n=== STEP 3: Concatenate Picture Grid (VIDEO-33-clean-approved-r2.mp4) ===")
    clean_video_path = OUTPUT_DIR / "VIDEO-33-clean-approved-r2.mp4"
    cmd_concat = [
        "ffmpeg", "-y", "-v", "error",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_path),
        "-c:v", "copy",
        str(clean_video_path)
    ]
    subprocess.run(cmd_concat, check=True)
    
    clean_info = get_video_stream_info(clean_video_path)
    clean_frames = int(clean_info["nb_read_frames"])
    clean_sha = sha256_file(clean_video_path)
    assert clean_frames == 2255, f"Clean video frame count mismatch: expected 2255, got {clean_frames}"
    print(f"Clean video concatenated successfully: {clean_frames} frames, {clean_info['width']}x{clean_info['height']} @ {clean_info['r_frame_rate']}")
    print(f"Clean Video SHA256: {clean_sha}")

    print("\n=== STEP 4: Mux Untouched Voice (VIDEO-33-master-approved-r2.mp4) ===")
    master_video_path = OUTPUT_DIR / "VIDEO-33-master-approved-r2.mp4"
    # Mux clean video with original voice. Untouched voice starting from t=0.000s
    cmd_mux = [
        "ffmpeg", "-y", "-v", "error",
        "-i", str(clean_video_path),
        "-i", str(voice_path),
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "24000",
        "-ac", "1",
        str(master_video_path)
    ]
    subprocess.run(cmd_mux, check=True)
    
    master_vinfo = get_video_stream_info(master_video_path)
    master_ainfo = get_audio_stream_info(master_video_path)
    master_frames = int(master_vinfo["nb_read_frames"])
    master_sha = sha256_file(master_video_path)
    
    assert master_frames == 2255, f"Master video frame count mismatch: expected 2255, got {master_frames}"
    print(f"Master video muxed successfully: {master_frames} frames, audio codec={master_ainfo['codec_name']}, rate={master_ainfo['sample_rate']}")
    print(f"Master Video SHA256: {master_sha}")

    print("\n=== STEP 5: Extract 13 Seam Clips (60 frames around cut with original audio) ===")
    boundaries = [
        ("seam_01_S01_S02", 181, "S01", "S02"),
        ("seam_02_S02_S03", 296, "S02", "S03"),
        ("seam_03_S03_S04", 424, "S03", "S04"),
        ("seam_04_S04_S05", 545, "S04", "S05"),
        ("seam_05_S05_S06", 716, "S05", "S06"),
        ("seam_06_S06_S07", 890, "S06", "S07"),
        ("seam_07_S07_S08", 1030, "S07", "S08"),
        ("seam_08_S08_S09", 1194, "S08", "S09"),
        ("seam_09_S09_S10", 1418, "S09", "S10"),
        ("seam_10_S10_S11", 1602, "S10", "S11"),
        ("seam_11_S11_S12", 1807, "S11", "S12"),
        ("seam_12_S12_S13", 1913, "S12", "S13"),
        ("seam_13_S13_S14", 2049, "S13", "S14"),
    ]

    seams_summary = []
    for name, boundary_frame, sc_before, sc_after in boundaries:
        start_f = max(0, boundary_frame - 30)
        end_f = min(2255, boundary_frame + 30)
        num_frames = end_f - start_f
        start_time = start_f / 30.0
        dur_time = num_frames / 30.0
        
        out_seam = SEAMS_DIR / f"{name}.mp4"
        cmd_seam = [
            "ffmpeg", "-y", "-v", "error",
            "-ss", f"{start_time:.4f}",
            "-i", str(master_video_path),
            "-t", f"{dur_time:.4f}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k",
            str(out_seam)
        ]
        subprocess.run(cmd_seam, check=True)
        print(f"Extracted {name}: frames [{start_f}, {end_f}] ({start_time:.3f}s - {start_time+dur_time:.3f}s)")
        seams_summary.append({
            "name": name,
            "boundary_frame": boundary_frame,
            "sc_before": sc_before,
            "sc_after": sc_after,
            "start_frame": start_f,
            "end_frame": end_f,
            "start_time": start_time,
            "duration": dur_time,
            "file": f"seams/{name}.mp4"
        })

    print("\n=== STEP 6: Extract Visual Proofs (Open/Mid/End & Mobile 360x640 & Grayscale) ===")
    proofs_manifest = []
    for sc in manifest["scenes"]:
        s_id = sc["scene_id"]
        start_frame, end_frame = sc["master_frame_range_half_open"]
        mid_frame = start_frame + (end_frame - start_frame) // 2
        last_frame = end_frame - 1
        
        for f_name, f_idx in [("open", start_frame), ("mid", mid_frame), ("end", last_frame)]:
            out_img = PROOFS_DIR / f"{s_id}_{f_name}_f{f_idx}.png"
            cmd_frame = [
                "ffmpeg", "-y", "-v", "error",
                "-i", str(clean_video_path),
                "-vf", f"select=eq(n\\,{f_idx})",
                "-vframes", "1",
                str(out_img)
            ]
            subprocess.run(cmd_frame, check=True)

            # Grayscale proof
            out_gray = PROOFS_DIR / f"{s_id}_{f_name}_f{f_idx}_gray.png"
            cmd_gray = [
                "ffmpeg", "-y", "-v", "error",
                "-i", str(out_img),
                "-vf", "format=gray",
                str(out_gray)
            ]
            subprocess.run(cmd_gray, check=True)

            proofs_manifest.append({
                "scene_id": s_id,
                "label": f_name,
                "frame": f_idx,
                "color_path": f"proofs/{out_img.name}",
                "gray_path": f"proofs/{out_gray.name}"
            })
    print(f"Extracted {len(proofs_manifest)} frame proofs with grayscale pairs.")

    # Generate 360x640 mobile preview video
    mobile_mp4 = OUTPUT_DIR / "VIDEO-33-mobile-360x640-preview.mp4"
    cmd_mobile = [
        "ffmpeg", "-y", "-v", "error",
        "-i", str(master_video_path),
        "-vf", "scale=360:640",
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-c:a", "aac", "-b:a", "96k",
        str(mobile_mp4)
    ]
    print("Generating mobile 360x640 preview video...")
    subprocess.run(cmd_mobile, check=True)
    print("Mobile preview generated.")

    # Generate film poster thumbnail (using S04 mid frame f484)
    poster_img = OUTPUT_DIR / "VIDEO-33-thumbnail.png"
    cmd_poster = [
        "ffmpeg", "-y", "-v", "error",
        "-i", str(clean_video_path),
        "-vf", "select=eq(n\\,484)",
        "-vframes", "1",
        str(poster_img)
    ]
    subprocess.run(cmd_poster, check=True)
    print("Poster thumbnail generated.")

    # Save assembly summary json
    summary_data = {
        "master_video": {
            "path": str(master_video_path),
            "filename": master_video_path.name,
            "sha256": master_sha,
            "frames": master_frames,
            "fps": 30,
            "duration": master_frames / 30.0
        },
        "clean_video": {
            "path": str(clean_video_path),
            "filename": clean_video_path.name,
            "sha256": clean_sha,
            "frames": clean_frames,
            "fps": 30,
            "duration": clean_frames / 30.0
        },
        "voice": {
            "source_path": str(voice_path),
            "sha256": voice_sha,
            "samples": 1803840,
            "sample_rate": 24000,
            "duration_seconds": 75.16
        },
        "seams": seams_summary,
        "proofs": proofs_manifest
    }
    with open(OUTPUT_DIR / "assembly_summary.json", "w", encoding="utf-8") as f_sum:
        json.dump(summary_data, f_sum, indent=2, ensure_ascii=False)

    print("\n=== Assembly Finished Successfully! ===")

if __name__ == "__main__":
    main()
