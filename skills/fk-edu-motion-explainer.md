# Educational Explainer Motion Pipeline

Plan and build narrated educational/commercial explainers with content-specific visuals, intentional motion and accurate audio timing. Codex is the primary production agent; Antigravity analyzes audio and supports production, or produces when the user explicitly requests it.

## Load by phase

- Before storyboard/assets: [routing and asset contracts](fk-edu-motion-explainer.references/routing-and-assets.md).
- Frame/copy design: [visual and text design](fk-edu-motion-explainer.references/visual-design.md).
- Motion/review: [motion and visual QA](fk-edu-motion-explainer.references/motion-and-qa.md).
- Implementation/render: [production contract](fk-edu-motion-explainer.references/production.md).

## Workflow

1. Read root AGENTS.md and the project's brief, manifest, approved style and persistent production state. Start new work from `videos/_template_codex_first/`; preserve old projects.
2. Preserve master audio, raw transcript and sample timing; put fact-checked corrections in `corrected_text`. Antigravity normally supplies the analysis. Do not synthesize replacement narration or stretch timing without authorization.
3. Choose an engine per scene by capability and compatibility. Pure 2D work needs no Flow health check. Use HyperFrames entry/core guidance for its workflow, or existing Remotion guidance for React/frame-based scenes. Do not install extra engines.
4. Define the scene's meaning, visual transformation, timed beats, text inventory, asset sources and render entry. Character, typography, infographic, abstract and mixed storytelling are all valid. No mascot or rig is required.
5. Propose a design system from the brief/references, then build only the agreed pilot scenes. Cards, open canvas, layers, easing, accents and spacing follow the selected style. `references/ANIMATION-STYLES.md` offers candidates without mandating one.
6. Inspect frames and playback, then obtain explicit human approval and record its evidence/revision in `production_status.json`. A successful encode is not approval.
7. Continue remaining scenes in the same project with reusable source/assets/components and approved constraints. Allow new visuals and scene-specific motion. Reopen approval when approved constraints/pilot artifacts change.
8. Render independent scenes; assemble at configured FPS with master audio at t=0. Verify actual output and update production state and next actions for another chat.

## Quality contract

Communicate the intended meaning clearly. Choose text density and visual detail for the content and approved treatment: kinetic typography can lead with words, and infographics can lead with data. Give characters a meaningful role when present. Check legibility at the actual target viewing size, glyph coverage, composition balance, motion intent, continuity and audio sync.

Subtitles are optional. Reserve space only for requested subtitles or actual delivery-platform requirements; there is no fixed footer, safe padding, accent, mascot quota, layer count, anti-card rule or motion preset.

## Generated-media branch (only when required)

For legacy compatibility, `HF_ONLY`, `FLOW_ONLY` and `HYBRID` remain valid routing labels; record the actual renderer separately. These labels do not bind a visual style to an engine. Use Flow only for a requested generation capability. Check health/provider status only in that branch and follow reference-first, UUID, material, batch/throttle and video-review contracts from root AGENTS.md and the applicable generation skill. Put exact text in the compositor. Plan overlay placement around observed footage action; composition and overlay treatments follow the approved brief.

## Completion report

Report scene engines/reasons, source/assets, proof times, actual duration, checks run, output paths, approval state and remaining work. Never claim visual review or human approval from automated tests alone.
