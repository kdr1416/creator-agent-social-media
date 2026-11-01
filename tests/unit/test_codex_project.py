"""Offline contract tests, plus tiny synthetic media in tmp_path (never a pilot)."""
import copy
import importlib.util
import json
import shutil
import subprocess
import sys
import wave
from unittest.mock import patch
from pathlib import Path

import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("codex_project", ROOT / "tools/codex_project.py")
project = importlib.util.module_from_spec(spec)
spec.loader.exec_module(project)


def make_project(tmp_path):
    root = tmp_path / "project with spaces"
    shutil.copytree(ROOT / "videos/_template_codex_first", root)
    audio = root / "inputs/source_audio.wav"
    with wave.open(str(audio), "wb") as stream:
        stream.setparams((1, 2, 8000, 0, "NONE", "not compressed"))
        stream.writeframes(b"\x10\x00" * 8000)
    config = project.read(root / "project_manifest.json")
    config.update(project_id="test", canvas={"width": 160, "height": 90}, fps=24, pilot_scene_ids=["S01"])
    config["audio"].update(sha256=project.digest(audio), sample_rate=8000, total_samples=8000)
    timeline = project.read(root / "inputs/scene-manifest.json")
    example = project.read(root / "inputs/scene.example.json")
    for index, (start, end) in enumerate(((0, 4001), (4001, 8000)), 1):
        scene = copy.deepcopy(example)
        sid = f"S{index:02}"
        scene.update(scene_id=sid, start_sample=start, end_sample=end,
                     source=f"scenes/{sid}/entry.tsx", output=f"scenes/{sid}/render.mp4",
                     engine="remotion", composition_id=sid)
        # FFmpeg fixture exercises argv substitution, staging and real probe checks
        # without running a video engine or producing any user project content.
        scene["render_argv"] = ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
                                "color=c=blue:s={width}x{height}:r={fps}", "-frames:v", "{frames}",
                                "-c:v", "libx264", "-pix_fmt", "yuv420p", "{output}"]
        source = root / scene["source"]
        source.parent.mkdir(parents=True)
        source.write_text("// test fixture, no HTML entry required", encoding="utf-8")
        timeline["scenes"].append(scene)
    project.write(root / "project_manifest.json", config)
    project.write(root / "inputs/scene-manifest.json", timeline)
    return root


class TestCodexProject(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="codex-v2-test-", dir=ROOT / "scratch")
        assert Path(self.temp.name).resolve().is_relative_to((ROOT / "scratch").resolve())
        self.addCleanup(self.temp.cleanup)
        self.root = make_project(Path(self.temp.name))

    def approved_hyperframes_fixture(self):
        config, timeline, state = project.load(self.root)
        for scene in timeline["scenes"]:
            original = self.root / scene["source"]
            entry = original.with_name("index.html")
            original.rename(entry)
            entry.write_text("<svg><circle r='12'/></svg><script src='motion.js'></script>", encoding="utf-8")
            scene.update(engine="hyperframes", source=entry.relative_to(self.root).as_posix())
            (entry.parent / "motion.js").write_text("const travel = 100;", encoding="utf-8")
            (entry.parent / "shape.svg").write_text("<svg/>", encoding="utf-8")
            (self.root / scene["output"]).write_bytes(b"unit invalidation fixture; not playable media")
        project.write(self.root / "inputs/scene-manifest.json", timeline)
        (self.root / "assets/shared.svg").write_text("<svg/>", encoding="utf-8")
        for scene in timeline["scenes"]:
            state["scenes"][scene["scene_id"]] = {
                "technical_qa": "passed", "visual_qa": "passed", "fixture_only": True,
                "source_fingerprint": project.scene_fingerprint(self.root, config, scene),
                "render_sha256": project.digest(self.root / scene["output"]),
            }
        state["approval"] = {"status": "approved", "reviewer": "SYNTHETIC UNIT FIXTURE",
                             "approved_at": project.stamp(), "evidence": "No human approval; unit fixture only",
                             "fingerprint": project.approval_fingerprint(self.root, config, timeline),
                             "fixture_only": True}
        project.write(self.root / "production_status.json", state)
        return config, timeline, state

    def test_known_hyperframes_diagnostics_keep_approval_and_render_valid(self):
        config, timeline, state = self.approved_hyperframes_fixture()
        paths = [".hyperframes/history-id", ".hyperframes/hf-ids-stamped.json",
                 ".hyperframes/video-state.json",
                 ".hyperframes/artifacts/checks/90429744-294a-4c83-8551-1196923d81ec.json"]
        before = state["approval"]["fingerprint"]
        for scene in timeline["scenes"]:
            directory = (self.root / scene["source"]).parent
            for name in paths:
                path = directory / name
                path.parent.mkdir(parents=True, exist_ok=True)
                for content in ("initial diagnostic", "updated diagnostic"):
                    path.write_text(content, encoding="utf-8")
                    project.require_approval(self.root, config, timeline, state)
                    project.require_render(self.root, config, scene, state)
        assert before == project.approval_fingerprint(self.root, config, timeline)

    def test_html_js_svg_edits_still_invalidate_approval_and_render(self):
        config, timeline, state = self.approved_hyperframes_fixture()
        for name in ("index.html", "motion.js", "shape.svg"):
            path = (self.root / timeline["scenes"][0]["source"]).parent / name
            original = path.read_bytes()
            with self.subTest(name=name):
                path.write_bytes(original + b" changed")
                with self.assertRaisesRegex(AssertionError, "Approval is stale"):
                    project.require_approval(self.root, config, timeline, state)
                with self.assertRaisesRegex(AssertionError, "Scene source changed"):
                    project.require_render(self.root, config, timeline["scenes"][0], state)
            path.write_bytes(original)

    def test_shared_assets_still_invalidate_all_dependent_scenes(self):
        config, timeline, state = self.approved_hyperframes_fixture()
        (self.root / "assets/shared.svg").write_text("<svg><path/></svg>", encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "Approval is stale"):
            project.require_approval(self.root, config, timeline, state)
        for scene in timeline["scenes"]:
            with self.assertRaisesRegex(AssertionError, "Scene source changed"):
                project.require_render(self.root, config, scene, state)

    def test_full_roster_timing_and_project_configuration_remain_protected(self):
        config, timeline, state = self.approved_hyperframes_fixture()
        manifest = self.root / "inputs/scene-manifest.json"
        original = manifest.read_bytes()
        changed = copy.deepcopy(timeline)
        changed["scenes"][0]["end_sample"] -= 1
        changed["scenes"][1]["start_sample"] -= 1
        roster = copy.deepcopy(timeline)
        roster["scenes"][1]["end_sample"] = 6000
        added = copy.deepcopy(roster["scenes"][1])
        added.update(scene_id="S03", start_sample=6000, end_sample=8000,
                     source="scenes/S03/index.html", output="scenes/S03/render.mp4")
        roster["scenes"].append(added)
        for candidate in (changed, roster):
            project.write(manifest, candidate)
            c, t, s = project.load(self.root)
            with self.assertRaisesRegex(AssertionError, "Approval is stale"):
                project.require_approval(self.root, c, t, s)
            manifest.write_bytes(original)
        path = self.root / "project_manifest.json"
        config["fps"] = 30
        project.write(path, config)
        with self.assertRaisesRegex(AssertionError, "Approval is stale"):
            project.require_approval(self.root, config, timeline, state)

    def test_unknown_preview_and_nested_files_are_not_ignored(self):
        config, timeline, state = self.approved_hyperframes_fixture()
        directory = (self.root / timeline["scenes"][0]["source"]).parent
        for name in (".hyperframes/custom.json", ".hyperframes/preview/cache.html",
                     ".hyperframes/variables.json", ".hyperframes/artifacts/checks/authored.json",
                     "assets/.hyperframes/history-id", "video-state.json", "debug.log"):
            path = directory / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("authored or unknown content", encoding="utf-8")
            with self.subTest(name=name), self.assertRaisesRegex(AssertionError, "Approval is stale"):
                project.require_approval(self.root, config, timeline, state)
            path.unlink()
        # The same metadata names in shared assets are always semantic inputs.
        path = self.root / "assets/.hyperframes/history-id"
        path.parent.mkdir(parents=True)
        path.write_text("shared dependency", encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "Approval is stale"):
            project.require_approval(self.root, config, timeline, state)

    def test_explicit_entry_and_non_hyperframes_metadata_are_tracked(self):
        config, timeline, state = self.approved_hyperframes_fixture()
        scene = timeline["scenes"][0]
        path = (self.root / scene["source"]).parent / ".hyperframes/video-state.json"
        path.parent.mkdir(parents=True)
        path.write_text("render input", encoding="utf-8")
        # Filter cannot hide the declared source or pilot output.
        explicit = dict(scene, source=path.relative_to(self.root).as_posix())
        assert path in project.scene_files(self.root, explicit)
        explicit = dict(scene, output=path.relative_to(self.root).as_posix())
        assert path in project.scene_files(self.root, explicit, include_output=True)
        scene["engine"] = "remotion"
        assert path in project.scene_files(self.root, scene)


    def test_template_structure_is_valid_but_not_production_ready(self):
        root = ROOT / "videos/_template_codex_first"
        project.load(root, template=True)
        with self.assertRaises((AssertionError, TypeError, ValueError)):
            project.load(root)


    def test_contiguous_samples_cumulative_frames_and_master_integrity(self):
        configured = self.root
        config, timeline, _ = project.load(configured)
        rows = project.frame_plan(config, timeline)
        assert [r["picture_frames"] for r in rows] == [12, 12]
        config["fps"] = "30000/1001"
        rows = project.frame_plan(config, timeline)
        assert rows[0]["global_end_frame"] == rows[1]["global_start_frame"]
        assert rows[-1]["global_end_frame"] == 30
        timeline["scenes"][1]["start_sample"] += 1
        project.write(configured / "inputs/scene-manifest.json", timeline)
        with self.assertRaisesRegex(AssertionError, "contiguous"):
            project.load(configured)
        with self.assertRaisesRegex(ValueError, "escapes"):
            project.local(configured, "../outside.mp4")
        with (configured / config["audio"]["path"]).open("ab") as stream:
            stream.write(b"changed")
        with self.assertRaisesRegex(AssertionError, "Master audio changed"):
            project.load(configured)


    def test_approval_blocks_nonpilot_and_dry_run_has_no_writes(self):
        configured = self.root
        config, timeline, state = project.load(configured)
        before = {p: project.digest(p) for p in configured.rglob("*") if p.is_file()}
        project.render_scene(configured, config, timeline, state, "S01", dry_run=True)
        with self.assertRaisesRegex(AssertionError, "Human pilot approval"):
            project.render_scene(configured, config, timeline, state, "S02", dry_run=True)
        assert before == {p: project.digest(p) for p in configured.rglob("*") if p.is_file()}


    def test_source_edit_invalidates_scene_but_not_shared_approval(self):
        configured = self.root
        config, timeline, state = project.load(configured)
        before = project.approval_fingerprint(configured, config, timeline)
        scene = timeline["scenes"][1]
        original = project.scene_fingerprint(configured, config, scene)
        (configured / scene["source"]).write_text("changed non-pilot")
        assert original != project.scene_fingerprint(configured, config, scene)
        assert before == project.approval_fingerprint(configured, config, timeline)
        (configured / "creative/style-tokens.json").write_text("changed shared style")
        assert before != project.approval_fingerprint(configured, config, timeline)


    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "Installed FFmpeg required")
    def test_synthetic_scene_render_approval_persistence_and_assembly(self):
        configured = self.root
        config, timeline, state = project.load(configured)
        project.render_scene(configured, config, timeline, state, "S01")
        state["scenes"]["S01"]["visual_qa"] = "passed"  # Fixture evidence, never a user decision.
        project.write(configured / "production_status.json", state)
        before_approval = (configured / "production_status.json").read_bytes()
        subprocess.run([sys.executable, str(ROOT / "tools/codex_project.py"), str(configured),
                        "record-approval", "--reviewer", "TEST FIXTURE", "--evidence", "synthetic test only",
                        "--dry-run"], check=True, capture_output=True)
        assert before_approval == (configured / "production_status.json").read_bytes()
        subprocess.run([sys.executable, str(ROOT / "tools/codex_project.py"), str(configured),
                        "record-approval", "--reviewer", "TEST FIXTURE", "--evidence", "synthetic test only"], check=True)
        config, timeline, state = project.load(configured)
        project.require_approval(configured, config, timeline, state)
        project.render_scene(configured, config, timeline, state, "S02")
        state["scenes"]["S02"]["visual_qa"] = "passed"
        project.assemble(configured, config, timeline, state)
        assert state["final"]["status"] == "rendered"
        assert state["final"]["visual_qa"] == state["final"]["audio_correlation_qa"] == "pending"
        data = project.probe(configured / "build/final_master.mp4")
        assert abs(float(data["format"]["duration"]) - 1) < 0.1
        assert config["audio"]["sha256"] == project.digest(configured / config["audio"]["path"])
        (configured / timeline["scenes"][1]["source"]).write_text("revised scene")
        with self.assertRaisesRegex(AssertionError, "Scene source changed"):
            project.assemble(configured, config, timeline, state, dry_run=True)
        style = configured / "creative/style-tokens.json"
        style.write_text(style.read_text() + "\n")
        with self.assertRaisesRegex(AssertionError, "Approval is stale"):
            project.require_approval(configured, config, timeline, state)


    def test_noop_renderer_cannot_claim_an_old_output(self):
        configured = self.root
        config, timeline, state = project.load(configured)
        scene = timeline["scenes"][0]
        scene["render_argv"] = [sys.executable, "-c", "pass"]
        (configured / scene["output"]).write_bytes(b"old artifact")
        with self.assertRaises((subprocess.CalledProcessError, FileNotFoundError)):
            project.render_scene(configured, config, timeline, state, "S01")
        saved = project.read(configured / "production_status.json")
        assert saved["scenes"]["S01"]["status"] == "failed"
        assert (configured / scene["output"]).read_bytes() == b"old artifact"


class TestInstructionGeneration(unittest.TestCase):
    def test_cli_write_scope_sync_parity_and_compatibility_entry(self):
        with tempfile.TemporaryDirectory(prefix="codex-v2-generator-", dir=ROOT / "scratch") as temp:
            sandbox = Path(temp).resolve()
            assert sandbox.is_relative_to((ROOT / "scratch").resolve())
            shutil.copy2(ROOT / "setup.py", sandbox / "setup.py")
            shutil.copytree(ROOT / "skills", sandbox / "skills")
            (sandbox / "scripts").mkdir()
            shutil.copy2(ROOT / "scripts/sync_skills.py", sandbox / "scripts/sync_skills.py")
            baseline = {p.relative_to(sandbox): project.digest(p) for p in sandbox.rglob("*") if p.is_file()}
            subprocess.run([sys.executable, "setup.py", "--tool", "codex"], cwd=sandbox, check=True, capture_output=True)
            after = {p.relative_to(sandbox): project.digest(p) for p in sandbox.rglob("*") if p.is_file()}
            changed = {str(p) for p in after if after[p] != baseline.get(p)}
            assert changed == {"AGENTS.md", ".fk-setup.json"}
            body = (sandbox / "AGENTS.md").read_text(encoding="utf-8")
            assert len([line for line in body.splitlines() if line.startswith("## ")]) == 5
            for old in ("Before ANY workflow", "180–200", "180-200", "70–80%"):
                assert old not in body
            assert "Codex Full Production" in body and "no Google Flow service" in body
            skills = list((sandbox / "skills").glob("fk-*.md"))
            assert body.count("| `/fk-") == len(skills)
            state = project.read(sandbox / ".fk-setup.json")
            state["tools"] = ["claude", "codex", "antigravity"]
            project.write(sandbox / ".fk-setup.json", state)
            sentinel = sandbox / ".agents/skills/custom/SKILL.md"
            sentinel.parent.mkdir(parents=True)
            sentinel.write_text("preserve independent skill")
            subprocess.run([sys.executable, "setup.py", "sync"], cwd=sandbox, check=True, capture_output=True)
            assert (sandbox / "AGENTS.md").read_text(encoding="utf-8") == body
            assert sentinel.read_text() == "preserve independent skill"
            assert len(list((sandbox / ".claude/commands").glob("fk-*.md"))) == len(skills)
            assert len(list((sandbox / ".agents/skills").glob("fk-*/SKILL.md"))) == len(skills)
            for ref in (sandbox / "skills/fk-edu-motion-explainer.references").glob("*.md"):
                assert ref.read_bytes() == (sandbox / ".agents/skills/fk-edu-motion-explainer/references" / ref.name).read_bytes()
            subprocess.run([sys.executable, "scripts/sync_skills.py"], cwd=sandbox, check=True, capture_output=True)
            mirror = (sandbox / ".agents/skills/fk-edu-motion-explainer/SKILL.md").read_text(encoding="utf-8")
            assert "references/visual-design.md" in mirror
            assert "180–200" not in mirror

    def test_2d_helper_never_connects_to_a_backend(self):
        with patch("socket.create_connection", side_effect=AssertionError("Unexpected network access")):
            config, timeline, state = project.load(ROOT / "videos/_template_codex_first", template=True)
            assert state["approval"]["status"] == "pending"
