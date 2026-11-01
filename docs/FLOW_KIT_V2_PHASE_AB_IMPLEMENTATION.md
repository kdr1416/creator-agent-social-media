# Flow Kit V2 — Phase A/B implementation record

Date: 2026-11-01 (Asia/Saigon). Scope: instruction migration, minimal project
template and offline validation. No pilot or historical video was produced.

## 1. Repository and safety

Actual filesystem root: `D:\Năm 3\flowkit-main`. The alternative
`D:\Nam 3\flowkit-main` did not exist; no equivalence was assumed.

`git rev-parse --show-toplevel` and `git status --short` both reported that this
directory is not a Git repository. No `.git` exists here. Consequently there is
no Git status, commit diff, or reliable classification of pre-existing uncommitted
user changes. Existing contents were treated as the user's baseline and backed up
before editing. No Git initialization, reset, checkout, clean or other destructive
operation was performed.

Backup and audit evidence:
`scratch/flowkit-v2-phase-ab-backup-20261101/`. It contains original modified-file
copies, `modified-paths.json`, `change-inventory.json`, `phase-ab.diff`,
`preserved-hashes.json` and `preservation-result.json`. The diff is generated from
backup contents, not a Git commit. `.fk-setup.json` was backed up and preserved.

## 2. Context read

All five required documents were present (no MISSING documents):

1. `docs/FLOW_KIT_V2_CODEX_CONTEXT_MANIFEST.md`
2. `docs/architecture/FLOW_KIT_V2_IMPLEMENTATION_READINESS_REPORT.md`
3. `docs/architecture/FLOW_KIT_V2_ARCHITECTURE_AND_SIMPLIFICATION_REPORT.md`
4. `docs/EXTERNAL_REPOSITORIES_EVALUATION.md`
5. `BAO_CAO_TOAN_DIEN_REVERSE_ENGINEERING.md`

The current user scope and Codex-first decisions take precedence over older
proposals to archive Remotion, consolidate skills, add dependencies, enforce
layer/easing quotas, force 30 FPS, or hand full production to Antigravity.

Source/context inspected: root `AGENTS.md`, `setup.py`, `.fk-setup.json`, required
animation-style/explainer/warm-doodle files and all four explainer sidecars,
`skills/README.md`, `skills/voice-to-scene-design/SKILL.md`, existing setup tests,
`scripts/sync_skills.py`, audio slicing/frame-plan utilities, demo/Remotion package
metadata and Remotion composition entry. Inventoried `.agents/skills/`, `skills/`,
`references/`, `videos/`, `hyperframes-demo/` and `remotion-project/`. No equivalent
Codex-first template existed. Nested project instructions were identified in the
demo and historical video directories; those directories were left intact.

Used installed `codebase-memory`: project selection, index status/schema,
generator symbol search, caller/callee trace and coverage check. The index was
fast-mode; AGENTS and scripts had exclusion/coverage limitations, so material
generator and script behavior was verified directly from source.

## 3. Modified files (17)

- `setup.py`
- `AGENTS.md` (generated)
- `scripts/sync_skills.py`
- `references/ANIMATION-STYLES.md`
- `skills/README.md`
- `skills/fk-edu-motion-explainer.md`
- `skills/fk-edu-motion-explainer.references/routing-and-assets.md`
- `skills/fk-edu-motion-explainer.references/visual-design.md`
- `skills/fk-edu-motion-explainer.references/motion-and-qa.md`
- `skills/fk-edu-motion-explainer.references/production.md`
- `skills/warm-doodle-video/SKILL.md`
- `tests/unit/test_setup.py`
- `.agents/skills/fk-edu-motion-explainer/SKILL.md` (generated)
- `.agents/skills/fk-edu-motion-explainer/references/routing-and-assets.md` (copied)
- `.agents/skills/fk-edu-motion-explainer/references/visual-design.md` (copied)
- `.agents/skills/fk-edu-motion-explainer/references/motion-and-qa.md` (copied)
- `.agents/skills/fk-edu-motion-explainer/references/production.md` (copied)

## 4. New delivery files (15)

- `tools/codex_project.py`
- `tests/unit/test_codex_project.py`
- This implementation record
- The 12 files in the template tree below

Backup/audit files under `scratch/flowkit-v2-phase-ab-backup-20261101/` are additional
operational evidence, not production artifacts. Temporary media fixtures were
created only under isolated scratch test directories and cleaned up by the tests.

## 5. Change summary

Replaced global Flow-first instructions and creative mandates with Codex-first
routing. Isolated generated-media technical safeguards to the optional Flow/API
branch. Converted explainer guidance to project-approved creative choices, removed
fixed footer/mascot/card/color/motion mandates, and retained exact audio/timing and
quality review requirements. Style catalog remains optional and engine-neutral.

Added a configurable empty project template and a stdlib-only local helper for
contract checks, cumulative frame planning, explicit single-scene rendering,
human approval recording and FFmpeg assembly. No agent orchestration system or
backend changes were introduced. See `change-inventory.json` and `phase-ab.diff`
for exact backup-based line changes; a Git diff is unavailable.

## 6. AGENTS.md V2

Root path/name is unchanged. It has exactly five level-two blocks:

1. Global Rules
2. Workflow Routing
3. Engine Routing
4. Creative Contracts
5. Skill Discovery

Codex owns planning, pilot, continuation and final rendering/QA. Antigravity normally
owns audio analysis/support and can produce on explicit user request. Project
settings own format, palette, fonts, spacing, optional characters and subtitles.
No mandatory footer, mascot quota, anti-card rule, accent, safe padding, character
rig, easing, anticipation, overshoot or minimum visual layer count is imposed.

## 7. Generator synchronization

`setup.py` remains the instruction single source of truth:
`_CRITICAL_RULES` → global rules; `_PIPELINE_OVERVIEW` → workflow;
`_ENGINE_ROUTING` and `_CREATIVE_CONTRACTS` → technical/creative layers;
`_agents_md_body()` → five-block root plus table discovered from `skills/fk-*.md`;
`generate_codex()` → root AGENTS. No separate competing root instruction file
was added. `generate_antigravity()` retains frontmatter/link rewriting and sidecar
copying. The legacy `scripts/sync_skills.py` entry now delegates to that generator
instead of maintaining a second, incomplete copy implementation.

Write scope was checked from source and in a temporary copy **before** regenerating
the live root:

| Invocation | Writes |
|---|---|
| `python setup.py --tool codex` | Root `AGENTS.md`, `.fk-setup.json` (records Codex as selected target) |
| `python setup.py sync` | Configs for saved tool targets + `.fk-setup.json`; current selection includes Claude/Codex/Antigravity |
| `python scripts/sync_skills.py` | Generated `fk-*` skill bodies and sidecar references in `.agents/skills/` only |

Live regeneration used `generate_codex()` and the explainer-only subset of
`generate_antigravity()`, preserving the saved tool selection and unrelated skill
files. Writing `.agents` required sandbox escalation, which succeeded; nothing
remains blocked by approval review. `setup.py clean` was never run.

## 8. Skills preserved

All 42 existing `fk-*` skills remain discoverable with their original IDs. Only the
educational explainer body/four references and warm-doodle entry were refined;
no skill was deleted, merged or deprecated. `voice-to-scene-design`, HyperFrames
entry/core/animation/creative/CLI/workflows, `remotion-motion-director`, conversion,
generation, review, concat, provider and model capabilities remain available.
No GSAP Skills, Remotion Skills, SVGO, animation engine or dependency was installed.

## 9. Template and continuation

```text
videos/_template_codex_first/
├── README.md
├── project_manifest.json
├── production_status.json
├── REVIEW.html
├── inputs/
│   ├── scene-manifest.json
│   └── scene.example.json
├── creative/
│   ├── storyboard.md
│   └── style-tokens.json
├── assets/ledger.json
├── components/motion.js
├── scenes/README.md
└── build/README.md
```

Master audio is supplied by a real project; no fake WAV, scene code or pilot render
is bundled. Format/FPS/brand settings are unset. Character and subtitle features
are optional. Per-scene engine/argv/source/composition ID support HyperFrames and
Remotion entries; TSX does not require an HTML wrapper. Shared animation utility
requires explicit per-motion timing/easing rather than a global preset.

Approval persists reviewer, timestamp, actual evidence and revision fingerprint.
Shared manifests/audio/creative/assets/components and pilot artifacts are bound to
approval. Shared changes require renewed review. Non-pilot scene-local new visuals
and animation are allowed without changing the pilot. A scene-source edit invalidates
its prior render fingerprint; assembly refuses stale artifacts. The helper cannot
prove a human's identity or enforce decisions against manual JSON edits; agents must
record genuine approval and honor the gate before authoring full production.

The helper does not auto-author or auto-render scenes, schedule agents, transcribe
audio or install a renderer. It runs only the explicit project-owned command for
the requested scene, verifies staged output before replacing that scene's declared
render, and records failures. Visual QA remains a recorded human/agent inspection,
not an automatic inference. The README documents placeholder/renderer contracts,
frame plan compatibility and continuation across chats.

## 10. Validation actually run

| Check | Result/evidence |
|---|---|
| Stdlib regression suite | **PASS: 8 tests**, including generator CLI/sync and synthetic-media integration |
| `--tool codex` in temporary copy | **PASS:** exactly AGENTS + setup state changed |
| `sync` in temporary copy | **PASS:** five V2 blocks, 42 skill rows, matching copied references, independent skill sentinel preserved |
| Legacy skill sync entry | **PASS:** canonical generator/link rewriting and sidecar behavior |
| Template structural validation | **PASS:** intentionally empty template accepted; production validation rejects unset configuration |
| Audio/timing/frame plan | **PASS:** hash integrity, contiguous samples, cumulative frames, rational FPS and gap rejection |
| Human approval gate | **PASS:** non-pilot blocked pending approval; record survives a new process; changed shared style makes approval stale; approval dry-run writes nothing |
| Scene editing/stale output | **PASS:** local non-pilot edit invalidates that render without changing pilot fingerprint; no-op renderer cannot claim old output |
| Real FFmpeg/FFprobe fixture | **PASS:** two temporary synthetic picture clips rendered independently and assembled with PCM master input; dimensions/FPS/frames/audio checked, master hash unchanged |
| 2D backend isolation | **PASS for helper/template path:** no backend client exists; validation tested with socket connections rejected; instructions explicitly isolate preflight |
| Python syntax | **PASS:** py_compile on changed/new Python files |
| JavaScript syntax | **PASS:** Node module syntax checks for reusable component and REVIEW script |
| New instructions stale-rule scan | **PASS:** no fixed footer or mascot-quota strings in updated root/source/explainer/generated mirror |
| Existing project/source preservation | **PASS:** 3,413 baseline files checked, zero changed/missing |

Preservation hash scopes: `agent/`, `extension/`, historical `videos/`,
`hyperframes-demo/`, `remotion-project/`, `repository-analysis/`; excludes
`node_modules`, `__pycache__` and `.hyperframes` caches. This is a content check,
not proof that each old project still renders. Root database files were not part
of that hash snapshot; no database/backend operation was performed.

Reproduce the dependency-free checks from repository root:

```powershell
python -m unittest discover -s tests/unit -p test_codex_project.py -v
python tools/codex_project.py videos/_template_codex_first validate --template
python -m py_compile setup.py scripts/sync_skills.py tools/codex_project.py tests/unit/test_setup.py tests/unit/test_codex_project.py
```

Initial validation failures were corrected: the environment's default temp path
was not writable under the sandbox, so fixtures now use verified workspace scratch
paths; Windows console JSON output was made Unicode-safe. Final runs above passed.

## 11. Not tested / not claimed

- Neither system Python nor repository venv has pytest. The existing pytest suite,
  including updated `tests/unit/test_setup.py`, was **not run**. No dependencies
  were installed. The stdlib suite separately exercises the changed generator.
- No fresh Codex process was launched to prove automatic instruction ingestion.
  Standard root AGENTS location, file presence and exact generator parity were
  verified; this already-running chat retains its original supplied context.
- No HyperFrames/Remotion browser render, old-project rerender, engine upgrade,
  Google Flow health/generation, transcription or real production pilot was run.
  Engine/dependency sources were preserved; renderer argv binding must be verified
  against the selected installed CLI when a real project is configured.
- REVIEW JavaScript syntax was checked; browser playback/layout was not inspected.
- Professional art direction, subtitle placement, final visual playback, actual
  speech/audio correlation, loudness and target-platform quality require real
  production media. Synthetic technical fixtures do not establish those results.

## 12. Rollback

Because Git metadata is absent, restore original file copies from the backup,
not `git reset`. First copy aside any edits made **after** this implementation.
`change-inventory.json.modified` lists only files changed in this phase; each
original is at the same relative path under the backup directory.

From the verified repository root, this restores those existing files only:

```powershell
$repo = (Get-Location).Path
$backup = Join-Path $repo 'scratch/flowkit-v2-phase-ab-backup-20261101'
$inventory = Get-Content -LiteralPath (Join-Path $backup 'change-inventory.json') -Raw | ConvertFrom-Json
foreach ($entry in $inventory.modified) {
    $source = Join-Path $backup $entry.path
    $target = Join-Path $repo $entry.path
    Copy-Item -LiteralPath $source -Destination $target
}
```

The `.agents` restore may require the same filesystem permission as regeneration.
Leave new files/template in place until reviewed, or move them to a separately
verified backup location. Do not recursively remove `videos/`, engine directories
or backup data. Do not run `setup.py clean`. After rollback, generator/root/skill
sources must be restored together to avoid reintroducing a mixed instruction set.

## 13. Use Flow Kit V2

Copy the template to a new project name, supply original PCM audio and Antigravity
analysis, configure project format and scene entries, then let Codex plan the
creative direction and explicitly requested pilot. Review pilot playback; record
actual human approval. Continue remaining scenes in that same project, inspect
and render each independently, then assemble and complete measured final QA.
Use `validate`, `plan`, `render-scene --scene`, `record-approval` and `assemble`
as documented in the template README. Keep production status and next actions
current for resumption. Google Flow remains dormant unless the project needs it.

Phase A/B stops here. No production pilot is authorized or claimed by this report.
