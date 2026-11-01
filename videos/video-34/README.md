# Codex-first project template

Copy this directory to a new name under `videos/`; do not produce inside the template.
All media/brand/format values are intentionally unset. No pilot, mascot, font,
resolution, aspect ratio, FPS or easing is selected for you.

The workflow is Audio Input → Antigravity Audio Analysis → Codex Creative Planning
→ Codex Pilot Production → Human Approval → Codex Full Production → Final Rendering
& QA. Antigravity can produce instead when explicitly requested by the user.

## Files and ownership

| File/directory | Purpose |
|---|---|
| `project_manifest.json` | Project identity, agents, canvas/FPS, master reference/hash, pilot IDs, local renderer argv |
| `inputs/source_audio.wav` (supply it) | Immutable original PCM master, not a bundled placeholder |
| `inputs/scene-manifest.json` | Antigravity analysis provenance, contiguous sample bounds, raw and corrected text, independent scene entries |
| `inputs/scene.example.json` | Record guide; copy into `scenes`, supply actual end sample; not production data |
| `creative/storyboard.md` | Creative intent, timed actions, scene QA/revision notes |
| `creative/style-tokens.json` | Project-owned design system, optional subtitles/characters, approved constraints |
| `assets/ledger.json` | Reusable assets with path, source/license, hash and semantic IDs as applicable |
| `components/motion.js` | Optional reusable GSAP operation with explicit per-motion choices; add engine-compatible components here |
| `scenes/<id>/` | Independent editable source and declared render output |
| `REVIEW.html` | Pilot playback from manifest; no approval button or invented approval |
| `production_status.json` | Durable human approval evidence, scene progress/QA/hashes, final state and next actions |
| `build/` | Cumulative frame plan, normalized picture and final assembly |

## Configure, validate, plan

Commands below run from repository root. Replace `<project>` with the copied path.
`tools/codex_project.py` uses only Python stdlib and installed executables, calls no
backend and installs nothing. It is a local file/render helper, not an agent scheduler.

1. Fill project ID, width/height (even for yuv420p), FPS (number or rational string,
   e.g. a project-selected `30000/1001`), audio metadata and SHA256. Use original PCM
   sample rate and sample count, not rounded seconds. Obtain the hash with
   `Get-FileHash -Algorithm SHA256`. Preserve raw transcript/ASR evidence separately.
2. Receive Antigravity analysis. Populate scene records, starting at sample 0 and
   covering the whole master contiguously with half-open bounds. Store immutable
   `raw_text` and separate fact-checked `corrected_text`; do not rerun old hardcoded
   `scratch/calc_contiguous_splits.py` or `scripts/slice_scene_audio.py` on a new project.
   Those utilities target historical inputs; their cumulative timing conventions,
   and existing `picture_frame_plan.json` field names, are retained here.
3. Set `pilot_scene_ids`. Choose HyperFrames or Remotion per scene, record why,
   set `source`, `composition_id`, `output`, and a local renderer command.
4. Plan storyboard/style/assets. No particular art style, card policy, rig or
   motion preset is mandatory. Approved project constraints govern continuation.

```powershell
python tools/codex_project.py videos/_template_codex_first validate --template
python tools/codex_project.py <project> validate
python tools/codex_project.py <project> plan
```

Template validation checks the intentionally empty structure. Production validation
requires actual configuration, PCM/hash and complete timing. It does not certify
art direction or that a renderer's scene reads the configuration correctly.

## Scene production and rendering

`render_argv` is an array of tokens, with no shell expansion. A scene override takes
precedence over `project_manifest.json.renderers[engine]`. It runs in the source's
parent directory. Supported placeholders:
`{root}`, `{source}`, `{output}`, `{width}`, `{height}`, `{fps}`, `{frames}`,
`{duration}` (picture-grid seconds), `{composition_id}`.

Use the already installed CLI executable or Node CLI file; pin the existing version.
For Windows `.cmd` launchers, prefer `node.exe` plus the CLI's absolute JS entry so
no shell is required. Do not use `npx` in a way that downloads dependencies.

HyperFrames argv shape after checking the installed CLI's options:
`["node", "<installed-hyperframes-cli.js>", "render", "--output", "{output}"]`.
Its scene source/config must read the project's canvas, FPS and planned picture
duration; follow installed `hyperframes-core`/CLI guidance. The runner checks actual
output frame count, dimensions and FPS and refuses a mismatch.

Remotion argv shape after checking the installed CLI's options:
`["node", "<installed-remotion-cli.js>", "render", "{source}", "{composition_id}",
"{output}", "--frames=0-<last-frame>"]`.
Compute last-frame as `{frames} - 1` in project configuration (no arithmetic expansion
is performed by the runner), or configure duration via composition props/metadata.
Bind width/height/FPS/duration to project values in that source, not to this example.
The existing `remotion-project/` is preserved; its experimental fixed-format Root
is not a universal project adapter. Use a new project-owned entry with the existing
installed packages. TSX source is supported; `index.html` is not required.

```powershell
python tools/codex_project.py <project> render-scene --scene S01 --dry-run
python tools/codex_project.py <project> render-scene --scene S01
python -m http.server 8766 --directory <project>
```

Open `http://127.0.0.1:8766/REVIEW.html`. For source previews use the selected engine's
preview/check commands. Slice preview audio only with PCM sample bounds, keeping the
master untouched. Picture renders can be silent; final audio comes from the master.

The runner renders only the explicit scene, sets `rendering` then `rendered` or
`failed`, records hashes/technical QA and leaves visual QA pending. Inspect opening,
transformation and final frames plus playback/target-size readability; then record
`visual_qa: "passed"` and inspection evidence in that scene's state. Technical QA
never grants human approval. Render failure leaves the scene resumable.

## Approval and continuation

Only after the human explicitly approves the actual pilot and shared design:

```powershell
python tools/codex_project.py <project> record-approval --reviewer "<human>" --evidence "<actual approval quote/chat reference>"
```

This stores reviewer, UTC timestamp, evidence and a revision fingerprint in
`production_status.json`. It is a record of the user's decision, not an identity or
authorization service. Never run it based on silence or automated checks.

The fingerprint binds project/scene manifests, master, creative files, shared assets,
components and pilot source/render artifacts. Changes there invalidate approval.
Confirm the complete scene roster and audio timing before pilot approval. The full
scene manifest remains fingerprinted: adding/removing scenes or changing timing
requires renewed review and revalidation of existing renders. Per-scene dependency
optimization is a future enhancement; approval is never retained automatically
after a structural video change.

Prepare shared files before approval; additions/changes later require renewed review.
Changes only to non-pilot scene source leave pilot approval intact. New scene-local
visuals/motion are allowed within the approved style. New/edited files in a scene
invalidate its prior render fingerprint, even if status text still says rendered.
Rerender only that scene and inspect it again. Final assembly refuses stale renders.

For HyperFrames scenes only, semantic fingerprints exclude these engine-owned
diagnostics directly under the scene source directory: `.hyperframes/history-id`,
`.hyperframes/hf-ids-stamped.json`, `.hyperframes/video-state.json`, and
`.hyperframes/artifacts/checks/<lowercase-UUID>.json`. These are history identity,
ID-stamping bookkeeping, history/check attribution and diagnostic reports verified
against installed HyperFrames 0.8.170; do not use these reserved files as authored
render inputs. Declared scene entries and approved outputs are always tracked.
Symlinks, unknown files, preview HTML, configuration, JS/HTML/SVG, assets and shared
dependencies remain tracked; there is no directory-wide or extension-wide ignore.
Studio changes to the actual HTML still invalidate the render/approval as before.
If upgrading engines or introducing other metadata, verify its role before extending
this allowlist. Existing approvals that hashed these diagnostics may become stale
once after this fix: rerender/review them; never auto-rewrite their fingerprint.

Resume in a new chat by reading project manifest → scene manifest → storyboard/style
→ production status. Check hashes before relying on recorded completion. Update
`phase` and `next_actions` after each work session; no separate Antigravity handoff
package is needed. Human approval gates non-pilot rendering and final assembly;
agents must also respect that gate before authoring full-production scenes.

## Final assembly and QA

```powershell
python tools/codex_project.py <project> assemble --dry-run
python tools/codex_project.py <project> assemble
```

Requires current pilot approval and fresh renders with technical + recorded visual
QA for every scene. Normalizes picture codecs, concatenates in manifest order and
muxes untouched master input from t=0 (AAC delivery encoding; no audio time stretch).
Uses cumulative sample-to-frame quantization; no forced 30 FPS and no per-scene
rounding drift. It does not normalize loudness, add music or burn subtitles.

Final technical checks cover picture dimensions, FPS, exact frame count and presence
of audio. Final visual playback, decoded-audio correlation/sync, clipping/loudness,
target platform and subtitle QA (if requested) remain explicit measured reviews;
`final.visual_qa` and `final.audio_correlation_qa` stay pending until performed.
Do not label a master complete from encode success alone.
