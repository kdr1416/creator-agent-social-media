#!/usr/bin/env python3
"""Small offline project contract/scene render/assembly CLI. Python stdlib only.

No agent dispatch, backend, dependency installation or automatic production.
Render commands are explicit project-owned argv arrays, executed without a shell.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import wave
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temp.replace(path)


def stamp():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def local(root, relative):
    if not isinstance(relative, str) or not relative:
        raise ValueError("Expected a nonempty project-relative path")
    path = (root / relative).resolve()
    if Path(relative).is_absolute() or not path.is_relative_to(root):
        raise ValueError(f"Path escapes project: {relative}")
    return path


def load(root, template=False):
    config = read(root / "project_manifest.json")
    timeline = read(root / "inputs/scene-manifest.json")
    state = read(root / "production_status.json")
    style = read(root / "creative/style-tokens.json")
    assert config["schema_version"] == timeline["schema_version"] == state["schema_version"] == 2
    assert config["production_agent"] in ("codex", "antigravity")
    assert isinstance(config["pilot_scene_ids"], list)
    assert isinstance(style["subtitles"]["enabled"], bool)
    assert state["approval"]["status"] in ("pending", "changes_requested", "approved")
    assert isinstance(state["scenes"], dict)
    scenes = timeline["scenes"]
    assert isinstance(scenes, list)
    ids = [s["scene_id"] for s in scenes]
    assert len(ids) == len(set(ids))
    assert len({s["output"] for s in scenes}) == len(scenes)
    assert set(config["pilot_scene_ids"]).issubset(ids)
    assert set(state["scenes"]).issubset(ids)
    for scene in scenes:
        assert re.fullmatch(r"[A-Za-z0-9_-]+", scene["scene_id"])
        assert scene["engine"] in ("hyperframes", "remotion")
        assert scene["routing_reason"].strip()
        assert isinstance(scene["raw_text"], str) and isinstance(scene["corrected_text"], str)
        assert type(scene["start_sample"]) is int and type(scene["end_sample"]) is int
        assert scene["end_sample"] > scene["start_sample"] >= 0
        source, output = local(root, scene["source"]), local(root, scene["output"])
        assert source != output and source.is_relative_to(root / "scenes")
        assert output.is_relative_to(root / "scenes")
        argv = scene.get("render_argv") or config["renderers"][scene["engine"]]
        assert isinstance(argv, list) and all(isinstance(x, str) for x in argv)
    local(root, config["audio"]["path"])
    if template:
        assert not scenes and not config["pilot_scene_ids"]
        assert state["approval"]["status"] == "pending"
        return config, timeline, state
    width, height = config["canvas"]["width"], config["canvas"]["height"]
    assert type(width) is int and type(height) is int and width > 0 and height > 0
    assert width % 2 == height % 2 == 0, "yuv420p delivery needs even dimensions"
    assert Fraction(str(config["fps"])) > 0
    assert type(config["audio"]["sample_rate"]) is int and config["audio"]["sample_rate"] > 0
    assert type(config["audio"]["total_samples"]) is int and config["audio"]["total_samples"] > 0
    assert scenes and config["pilot_scene_ids"], "Define scenes and an explicit pilot selection"
    audio = local(root, config["audio"]["path"])
    assert digest(audio) == config["audio"]["sha256"], "Master audio changed"
    with wave.open(str(audio), "rb") as wav:
        assert wav.getcomptype() == "NONE", "Use original PCM WAV"
        assert wav.getframerate() == config["audio"]["sample_rate"]
        assert wav.getnframes() == config["audio"]["total_samples"]
    previous = 0
    for scene in scenes:
        assert scene["start_sample"] == previous, "Scene bounds must be contiguous from t=0"
        previous = scene["end_sample"]
    assert previous == config["audio"]["total_samples"], "Scene bounds must cover the master"
    return config, timeline, state


def frame_plan(config, timeline):
    fps = Fraction(str(config["fps"]))
    rate = config["audio"]["sample_rate"]
    result = []
    # Cumulative rounding matches existing picture_frame_plan.json semantics.
    for scene in timeline["scenes"]:
        start = round(Fraction(scene["start_sample"], rate) * fps)
        end = round(Fraction(scene["end_sample"], rate) * fps)
        assert end > start, "Each scene must occupy at least one picture frame"
        result.append({"scene_id": scene["scene_id"], "start_sample": scene["start_sample"],
                       "end_sample": scene["end_sample"], "global_start_frame": start,
                       "global_end_frame": end, "picture_frames": end - start,
                       "fps": str(fps), "grid_error_ms": float(Fraction(start, 1) / fps -
                                                               Fraction(scene["start_sample"], rate)) * 1000})
    return result


def shared_files(root, config):
    paths = [root / "project_manifest.json", root / "inputs/scene-manifest.json",
             local(root, config["audio"]["path"])]
    for directory in ("creative", "assets", "components"):
        paths.extend(p for p in (root / directory).rglob("*") if p.is_file())
    return paths


def fingerprint(root, files):
    rows = [(p.relative_to(root).as_posix(), digest(p)) for p in sorted(set(files))]
    return hashlib.sha256(json.dumps(rows).encode()).hexdigest()


def hyperframes_diagnostic(path, source_dir):
    """Only engine-owned bookkeeping proven in HyperFrames 0.8.170.

    Do not ignore .hyperframes wholesale: preview HTML, unknown state, authored
    files and symlinks may be render inputs. Shared assets never use this filter.
    """
    relative = path.relative_to(source_dir)
    if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != source_dir and p.is_relative_to(source_dir)):
        return False
    if relative.parts in {
        (".hyperframes", "history-id"),
        (".hyperframes", "hf-ids-stamped.json"),
        (".hyperframes", "video-state.json"),
    }:
        return True
    return (relative.parts[:3] == (".hyperframes", "artifacts", "checks")
            and len(relative.parts) == 4
            and re.fullmatch(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\.json", relative.name) is not None)


def scene_files(root, scene, include_output=False):
    source = local(root, scene["source"])
    output = local(root, scene["output"])
    files = []
    for path in source.parent.rglob("*"):
        if not path.is_file() or (path == output and not include_output):
            continue
        # Explicit entries/approved outputs are always content, even if named
        # like a diagnostic. Studio edits to source HTML remain fingerprinted.
        if (path not in (source, output) and scene["engine"] == "hyperframes"
                and hyperframes_diagnostic(path, source.parent)):
            continue
        files.append(path)
    return files


def scene_fingerprint(root, config, scene):
    files = shared_files(root, config) + scene_files(root, scene)
    return fingerprint(root, files)


def approval_fingerprint(root, config, timeline):
    files = shared_files(root, config)
    for scene in timeline["scenes"]:
        if scene["scene_id"] in config["pilot_scene_ids"]:
            files.extend(scene_files(root, scene, include_output=True))
    return fingerprint(root, files)


def require_approval(root, config, timeline, state):
    approval = state["approval"]
    assert approval["status"] == "approved", "Human pilot approval is required"
    assert approval["reviewer"] and approval["evidence"] and approval["approved_at"]
    assert approval["fingerprint"] == approval_fingerprint(root, config, timeline), "Approval is stale"


def probe(path):
    result = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-show_streams",
                             "-show_format", "-of", "json", str(path)],
                            check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def verify_picture(path, config, frames):
    data = probe(path)
    video = next(s for s in data["streams"] if s["codec_type"] == "video")
    assert video["width"] == config["canvas"]["width"]
    assert video["height"] == config["canvas"]["height"]
    assert Fraction(video["r_frame_rate"]) == Fraction(str(config["fps"]))
    assert int(video["nb_read_frames"]) == frames, "Rendered frame count differs from frame plan"
    return data


def require_render(root, config, scene, state):
    record = state["scenes"].get(scene["scene_id"], {})
    assert record.get("source_fingerprint") == scene_fingerprint(root, config, scene), "Scene source changed"
    assert record.get("render_sha256") == digest(local(root, scene["output"])), "Scene render changed"
    assert record.get("technical_qa") == "passed", "Scene technical QA is missing"


def render_scene(root, config, timeline, state, scene_id, dry_run=False):
    scene = next(s for s in timeline["scenes"] if s["scene_id"] == scene_id)
    if scene_id not in config["pilot_scene_ids"]:
        require_approval(root, config, timeline, state)
    source, output = local(root, scene["source"]), local(root, scene["output"])
    assert source.is_file(), "Scene source is missing"
    row = next(r for r in frame_plan(config, timeline) if r["scene_id"] == scene_id)
    staging = root / "build" / (scene_id + ".rendering.mp4")
    values = dict(root=str(root), source=str(source), output=str(staging),
                  width=config["canvas"]["width"], height=config["canvas"]["height"],
                  fps=config["fps"], frames=row["picture_frames"],
                  duration=float(Fraction(row["picture_frames"], 1) / Fraction(str(config["fps"]))),
                  composition_id=scene.get("composition_id", scene_id))
    command = scene.get("render_argv") or config["renderers"][scene["engine"]]
    assert command, "Configure a local renderer argv; no dependencies are installed automatically"
    argv = [token.format(**values) for token in command]
    print(json.dumps({"cwd": str(source.parent), "argv": argv}))
    if dry_run:
        return
    staging.parent.mkdir(parents=True, exist_ok=True)
    if staging.exists():
        staging.unlink()  # A prior failed staging artifact is never accepted as a fresh render.
    state["scenes"][scene_id] = {"status": "rendering", "visual_qa": "pending"}
    state["final"] = {"status": "pending"}
    write(root / "production_status.json", state)
    try:
        subprocess.run(argv, cwd=source.parent, check=True)
        verify_picture(staging, config, row["picture_frames"])
        output.parent.mkdir(parents=True, exist_ok=True)
        staging.replace(output)
    except Exception:
        state["scenes"][scene_id]["status"] = "failed"
        write(root / "production_status.json", state)
        raise
    state["scenes"][scene_id] = {"status": "rendered", "technical_qa": "passed", "visual_qa": "pending",
                                "source_fingerprint": scene_fingerprint(root, config, scene),
                                "render_sha256": digest(output), "updated_at": stamp()}
    write(root / "production_status.json", state)


def assemble(root, config, timeline, state, dry_run=False):
    require_approval(root, config, timeline, state)
    rows = frame_plan(config, timeline)
    for scene in timeline["scenes"]:
        require_render(root, config, scene, state)
        assert state["scenes"][scene["scene_id"]].get("visual_qa") == "passed", "Record visual QA after inspection"
    build = root / "build"
    if dry_run:
        print("Assembly ready: normalize scene picture, concatenate, mux master audio at t=0")
        return
    build.mkdir(exist_ok=True)
    write(build / "picture_frame_plan.json", rows)
    state["final"] = {"status": "assembling"}
    write(root / "production_status.json", state)
    try:
        for scene, row in zip(timeline["scenes"], rows):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(local(root, scene["output"])),
                            "-map", "0:v:0", "-an", "-frames:v", str(row["picture_frames"]),
                            "-r", str(config["fps"]), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                            str(build / (scene["scene_id"] + ".mp4"))], check=True)
        (build / "concat.txt").write_text("".join(f"file '{s['scene_id']}.mp4'\n" for s in timeline["scenes"]), encoding="utf-8")
        final = build / "final_master.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "1", "-i", str(build / "concat.txt"),
                        "-i", str(local(root, config["audio"]["path"])), "-map", "0:v:0", "-map", "1:a:0",
                        "-c:v", "copy", "-c:a", "aac", "-movflags", "+faststart", str(final)], check=True)
        data = verify_picture(final, config, rows[-1]["global_end_frame"])
        assert any(s["codec_type"] == "audio" for s in data["streams"])
        state["final"] = {"status": "rendered", "path": "build/final_master.mp4", "sha256": digest(final),
                          "technical_qa": "passed", "visual_qa": "pending", "audio_correlation_qa": "pending", "updated_at": stamp()}
    except Exception:
        state["final"] = {"status": "failed"}
        raise
    finally:
        write(root / "production_status.json", state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("command", choices=("validate", "plan", "render-scene", "record-approval", "assemble"))
    parser.add_argument("--template", action="store_true", help="Validate an intentionally unconfigured template only")
    parser.add_argument("--scene")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--reviewer")
    parser.add_argument("--evidence", help="Actual user approval quote/chat reference, never agent-invented")
    args = parser.parse_args()
    root = args.project.resolve()
    if args.template and args.command != "validate":
        parser.error("--template is valid only with validate")
    config, timeline, state = load(root, args.template)
    if args.command == "validate":
        print("VALID template structure (production settings unset)" if args.template else "VALID project/audio/timing contract")
    elif args.command == "plan":
        rows = frame_plan(config, timeline)
        if args.dry_run:
            print(json.dumps(rows))
        else:
            write(root / "build/picture_frame_plan.json", rows)
    elif args.command == "render-scene":
        if not args.scene:
            parser.error("render-scene requires --scene")
        render_scene(root, config, timeline, state, args.scene, args.dry_run)
    elif args.command == "record-approval":
        if not args.reviewer or not args.evidence:
            parser.error("record-approval requires --reviewer and --evidence from explicit human approval")
        for scene in timeline["scenes"]:
            if scene["scene_id"] in config["pilot_scene_ids"]:
                require_render(root, config, scene, state)
                assert state["scenes"][scene["scene_id"]].get("visual_qa") == "passed"
        state["approval"] = {"status": "approved", "reviewer": args.reviewer, "evidence": args.evidence,
                             "approved_at": stamp(), "fingerprint": approval_fingerprint(root, config, timeline)}
        if args.dry_run:
            print(json.dumps(state["approval"]))
        else:
            write(root / "production_status.json", state)
    else:
        assemble(root, config, timeline, state, args.dry_run)


if __name__ == "__main__":
    if not __debug__:
        sys.exit("Run without -O: project contract and approval checks must remain enabled")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    try:
        main()
    except (AssertionError, ValueError, TypeError, KeyError, OSError, wave.Error,
            ZeroDivisionError, StopIteration, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error or 'Invalid project contract'}", file=sys.stderr)
        sys.exit(1)
