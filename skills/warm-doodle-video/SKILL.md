---
name: warm-doodle-video
description: Research or create playful 2D cartoon and mixed-media collage videos with vivid accents, coloured text strips, simple mascots and punchy motion. Use for this user's reference-led video style, including skill-only refinement, scripts, voice slices and FlowKit handoffs.
---

# Warm Doodle Video — playful cartoon and collage

Support reference-led style research and, when production is requested, turn narration into an original illustrated story with editable HyperFrames source and MP4. The reference establishes a visual taste, not a sequence to copy. This skill is a creative treatment within the current video workflow; it does not replace engine routing or authorize editing existing production files.

**Maturity: research candidate.** The first three-scene pilot was rejected for style mismatch. Its palette, font, student rig and layouts are negative evidence, not an approved preset. Read [the reference audit](references/reference-audit.md) before proposing the next interpretation. Keep this skill's identifier stable while its visual direction is refined.

The approved project engine governs implementation. HyperFrames/GSAP examples below are conditional technical guidance, not a restriction on this style: use existing Remotion guidance for a compatible frame-based implementation. This treatment does not require a character rig or fixed easing.

## Enter with the actual brief

Read the user's current request and existing project instructions. Use the available `hyperframes` entry point, `hyperframes-core` for composition structure, and `fk-edu-motion-explainer` when working in FlowKit. Load animation/CLI guidance when building. If a dependency is unavailable, report the missing capability rather than inventing an equivalent command.

First resolve the operation. **Analysis or skill-only research:** edit only the explicitly requested skill files, or answer without editing when only analysis is requested. Do not create a production storyboard, generate assets, render, update workflow/handoff/status files, install globally, or refresh an old archive merely because those capabilities exist. **Video creation:** use the production guidance below within the authorized scope. A research request does not activate production.

Infer settled choices from the conversation. For an explicitly authorized experiment such as “pick three scenes, design a storyboard and create videos,” complete those renders without reopening an optional style interview. A render request does not authorize publishing, replacing a production film, rewriting the voice, or continuing all scenes.

## Preserve source material

- Treat workflow docs, `render_handoff.json`, `production_status.json`, transcripts, routing and original WAVs as read-only unless the user explicitly requests edits.
- Create a new output directory, refusing to reuse an existing directory by default. Copy required audio/assets; hash source files before and after. Record old/new file paths distinctly.
- When handoff and status disagree, inspect their revision evidence. The handoff describes prior intent; status describes recorded execution. Do not silently reconcile them or claim the handoff represents current completion.
- Use actual WAV sample counts for scene length. Preserve raw ASR and timing; write `corrected_text` separately. Copy supplied voice without TTS replacement or time stretching.
- If random sampling is requested, record the eligible pool, selection method, exclusions and selected IDs. Do not secretly hand-pick scenes. Restricting the pool to an existing engine requires an explicit explanation.
- Fact-check factual names, places and claims against primary sources. User-provided personal success stories remain attributed source material, not independently verified outcomes. Use illustrative documents, never counterfeit evidence.

## The style's grammar

Read [visual and motion guidance](references/visual-language.md) before storyboarding. Use [tokens](assets/style-tokens.json) as adjustable starting values, not a universal brand replacement.

The recognisable combination is light softly tinted grounds, vivid accents, compact cartoon acting, real-media cutouts, coloured text strips and deliberate changes in visual emphasis. Preserve colour relationships, typography treatment, asset mix, composition and motion rhythm together. Fine outlines and cream backgrounds alone do not establish a match. Keep original subjects, mascot design, wording and scene content.

The bundled `doodle-kit.js`, `style.css`, `paper.png` and `scene-sans-bold.ttf` belong to the rejected pilot. They are technical fixtures, not default visual assets. `DoodleSans` is Segoe UI Bold, not a hand-drawn font; its alias proves no stylistic suitability. Design or source assets from the reference audit before production. The old rig may inform articulation mechanics, but its human proportions, muted colours and expression have no style approval.

A compact mascot can operate a prop, guide attention or react to an event. A timed supporting reaction is valid; forcing a full human character to physically cause every diagram is unnecessary. Keep reactions tied to the narrated beat and follow project semantic-action requirements. Repeated idle bounce without a narrative role still fails.

## Design from the spoken meaning

For each scene, identify:

1. What changes in the viewer's understanding?
2. What visible object/action can demonstrate that change?
3. Does the character cause the action, guide attention, or react to its result?
4. What few words are essential on screen?

Choose the visual family from the spoken meaning: everyday cartoon situation, large physical prop, annotated document/screen cutout, or simple mechanism. Preserve supplied documents and their provenance. When none exists, create an explicitly illustrative prop; never fabricate proof. Do not translate every noun into a stock-looking icon or connect every list with an S-curve. A coloured headline strip is an intentional text treatment; it does not authorize a large generic information card.

Keep engine and treatment separate. Preserve locked `HF_ONLY`, `FLOW_ONLY` and `HYBRID` modes; record a scene-specific override before changing them. In `HF_ONLY`, use independent vector layers. For Flow footage, follow its zero-generated-text and reference/batch/review contracts; an illustrated preference alone does not justify converting a physical-performance scene.

Write a new storyboard in the experiment's own directory before making assets. At minimum record narration provenance, actual duration, `raw_text`, `corrected_text`, engine/reason, style candidates/selection, visual verb, opening/transformation/final states, protagonist action, timed beats, signature motion, asset layers, text inventory/budget, physical containers, accent choice, mobile plan, dark-mass strategy and handoff. Use [storyboard fields](references/storyboard-fields.json) as the schema guide.

Compare neighbouring scenes. Change the dominant silhouette, prop system or camera logic when the meaning changes. Reusing palette and character is desirable; reusing the same framed layout for every sentence is not.

Record `reference_alignment` for colour relationships, type treatment, asset mix, composition, mascot language and motion rhythm, with visible evidence for each. Proposed changes remain candidates until compared against the reference. Technical checks prove renderability, not similarity.

Recurring blue feature headings, red problem statements or green results may establish continuity. Reuse semantic treatments deliberately; vary the main visual and action rather than banning recurring motifs.

## Build and deliver

- Stage assets selected for the new design; do not automatically copy the rejected pilot's visual kit. Fonts, textures, scripts and audio must resolve locally. Keep an asset ledger with provenance.
- Search the available HyperFrames registry for named effects before hand-building. Use a matching primitive when suitable; an installed but unwired component does not count as used. A custom prop or character action is appropriate when registry examples solve a different problem.
- Use one paused, seekable GSAP timeline per composition, matching the registered timeline key to the root composition ID. Scene roots use `width:100%;height:100%`; place modular styles/scripts inside their template transport.
- Keep motion deterministic. Use authored coordinates and explicit poses; no independent clock, network request or unseeded randomness while rendering. Layer far arm behind the torso, near arm and grasping hand in front.
- When a rig helper already positions an SVG group with `transform`, animate a separate outer wrapper for scene-level travel. Preserve its authored placement. Verify head/hand pivots with actual poses: a numerically plausible SVG origin can still detach a nested part. Sample at the gesture peak, not only before/after.
- Distribute action over the spoken duration. Reserve a readable resolve; do not complete everything in the first second and hold a poster.
- Plan scene-level changes in emphasis as well as object motion: an opening reframe when useful, stepped phrase reveal, main action, reaction and resolve. Use selective pop/settle, draw-on marks or directional transitions according to meaning. A different easing on a static composition is insufficient. Do not force a camera move or transition on every beat.
- Use the full project canvas with spacing and text hierarchy chosen for the approved treatment. Subtitles are optional; reserve only their actual area when requested. Verify essential text at the target viewing size. No universal font size, footer, character rig or mascot quota applies.
- Run the actual HyperFrames check and inspect opening, signature-in-progress and final frames. Review a mobile preview, thumbnail and grayscale. Watch playback when tooling permits; if only sampled frames were inspected, state that limitation accurately.
- Compare reference and candidate side by side on all six `reference_alignment` axes. Record `match`, `partial` or `mismatch` with evidence, not an invented similarity score. Rework mismatches before claiming the requested style was achieved. User acceptance is a separate result.
- Verify rendered video/audio streams, dimensions, timing and non-silent audio; compare copied WAV hashes. Record measured QA results and unresolved issues. Never infer approval from a successful encode.
- If Windows HyperFrames fails its actual single-voice audio mix, see [the bounded local fallback](references/windows-audio-fallback.md). Do not silently drop narration; this helper is not a replacement for multi-track mixing.
- `scripts/verify-single-voice.py` checks a 720×1280 mono-voice export, audio correlation, timing and optional source manifest, and produces mobile/grayscale/proof sheets. It requires PyAV, NumPy and Pillow. Pass custom proof times for other durations; the default times are for the first three-scene trial.
- Deliver the MP4, editable source, storyboard and evidence. For a reusable package, include this skill with its references and toolkit. State whether it was merely packaged or actually installed/discovered; do not claim global installation from creating a folder.

## Example request

“Dùng `$warm-doodle-video` từ `skills/warm-doodle-video/SKILL.md`. Đọc handoff/status ở chế độ chỉ đọc. Chọn ngẫu nhiên ba cảnh đủ điều kiện, giữ nguyên voice, tự thiết kế storyboard theo nội dung và render trong thư mục mới.”

The rejected first pilot lives in `videos/warm-doodle-style-lab/` in this repository. Preserve it for comparison; do not reuse it as an approved style example or revise it during skill-only research. Apply feedback to this skill narrowly; do not change the existing production workflow automatically.
