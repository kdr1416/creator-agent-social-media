# VIDEO-34 — Revision R1 delivery

**AWAITING HUMAN REVIEW — NOT APPROVED.** Prior pilot rejected; this is an experimental creative revision, not full production. Actual videos: scenes/S03/S03-pilot.mp4 and scenes/S08/S08-pilot.mp4. REVIEW.html contains the players, old/new comparisons and 21 extracted highlight screenshots.

## Highlight/effect timing — measured against original ASR

Global times below are cue starts; picture sampling quantizes to the next 30-FPS frame. “Sau” screenshots mean after the entrance settles, not after text disappears. All screenshot evidence was extracted from delivered MP4, at 360×640, then visually inspected for the seven phrases and Vietnamese diacritics.

| Scene | Global voice time | Spoken keyword/idea (raw ASR) | Animated text | Motion/effect | Verified in output |
|---|---|---|---|---|---|
| S03 | 10.50s; local 0.333917s | đi bộ (words 46–47) | Đi bộ | Masked upward reveal + yellow path rule | YES — MP4 frames before/during/settled: build/r1-evidence/S03-walk-*.png |
| S03 | 12.40s; local 2.233917s | chạy bộ (words 54–55) | Chạy bộ | Horizontal word stagger + coast path draw | YES — MP4 frames before/during/settled: build/r1-evidence/S03-run-*.png |
| S03 | 13.68s; local 3.513917s | cà phê (words 60–61) | Cà phê | Masked reveal + cup action | YES — MP4 frames before/during/settled: build/r1-evidence/S03-cafe-*.png |
| S03 | 17.54s; local 7.373917s | gia đình (words 77–78) | Gia đình | Scale settle + connection arc / close reframe | YES — MP4 frames before/during/settled: build/r1-evidence/S03-family-*.png |
| S08 | 41.28s; local 1.010000s | sống chậm, (words 172–173) | Sống chậm | Masked two-word reveal; underline resolves on cân bằng (42.14) | YES — MP4 frames before/during/settled: build/r1-evidence/S08-slow-*.png |
| S08 | 43.30s; local 3.030000s | thời gian (words 180–181) | Thời gian | Word stagger + terrace light / attention handoff | YES — MP4 frames before/during/settled: build/r1-evidence/S08-time-*.png |
| S08 | 45.00s; local 4.730000s | Giá đình, (words 186–187) | Gia đình | Second-level settle + contact arc and smile | YES — MP4 frames before/during/settled: build/r1-evidence/S08-family-*.png |
| S08 | 42.14s; local 1.87s | cân bằng (174–175) | Sống chậm remains visible | Rule grows horizontally; pause in hand action | YES — S08-balance-effect.png |

Cue windows follow original ASR, including raw “Giá đình” mapped to corrected “Gia đình”; timestamps are not rewritten. Exact onset of a reveal may be up to one frame after the cue. Text is not verbatim captions; only selected keywords, no fixed footer.

## What changed

- Color/material system rebuilt around navy, bright azure/cyan, clean white, controlled coral/yellow. Static paper grain removed. These are proposed creative colors, not official Esora colors.
- S03 keeps the coastal topology but adds distinct hair/hat/bag/athletic silhouettes, shutter/cornice details, stronger focal reframing and a closer family finish. Camera bounds were corrected after encoded-frame inspection exposed unpainted edges.
- S08 is redrawn: smaller head relative to body, new seated legs/pelvis, shorter upper/forearm reach and a closer child. Hand endpoint at (418,872); fixed laptop hinge (170,835). The workspace remains physically present after attention shifts.
- Masked text, directional word stagger, restrained scale settle, run path, family/contact arcs and the terrace light cue are implemented. Registry search was inspected; its marker/card lower thirds were unsuitable for this composition, so project-specific GSAP geometry was authored without installing registry items.
- Text morphing and independent multi-plane parallax: **NOT IMPLEMENTED**, not required for these beats. No fake 3D camera or physical IK claim.

## Runtime/evidence

HyperFrames 0.8.170, GSAP and FFmpeg already installed. Both checks ok; no runtime errors. Silent-picture warning is expected because voice is muxed separately. A transient masked-text occlusion is info-level; S08 retains a neck-pivot drift warning, visually inspected. CLI success does not certify aesthetic quality. Check, render and mux logs are build/r1-S03-* and build/r1-S08-*.

Both videos 1080×1920 / 30 FPS (pilot working config), 268/168 frames. Exact WAV excerpts remain 214542/134643 samples at mono 24kHz. Audio/container durations 8.939250/5.610125s; picture durations 8.933333/5.600000s. Re-measurement is in build/pilot-evidence/media-qa.json, including decoded AAC correlation/lag. Do not call encoded A/V sample-exact.

Browser results are build/pilot-evidence/browser-final.json: 360/768/1280px REVIEW layouts, full playback at 1280px, source request/console checks, local font readiness and repeated-seek pixel hashes. Windows Arial Bold was copied from the existing local system; no font/dependency installed. Rights provenance is in the asset ledger; redistribution license not independently established.

Before/during/settled screenshots for all seven highlights are in build/r1-evidence; old/new comparison PNGs there come from the respective actual MP4s. The screenshot evidence tests that selected graphics are present, not that every effect is artistically ideal.

## Remaining visual review

S03 gait remains stylized; a dedicated foot-contact solve is not implemented. Family staging is enlarged but still an ensemble shot. The top dark wash is deliberately strong and its balance against architecture needs human feedback. S08 gaze and facial acting are simplified; hand endpoint coincidence is not proof of convincing anatomy. Illustration taste, typography sophistication, rhythm and emotional quality remain for the user's review. No full-production readiness approval is inferred.

## Source and rollback

Current artwork regeneration: components/revise_pilot_r1.py (do not use the old build_pilot_art.py entry point to overwrite R1). Existing helpers in build_pilot_art.py are reused by R1. Source assembly: components/build_pilot_sources.py --scene S03 or S08; choreography: components/pilot-motion.js; cues: components/pilot-highlights.json. Re-render/mux only the affected scene, refresh ledger hashes and rerun QA.

Previous source/assets/creative docs/MP4s/REVIEW/status are preserved in build/revision-r1-before. To rollback, preserve any later edits first, copy the desired backed-up files to matching paths and keep R1 files separately; never delete master, original logo or historical projects. Inputs were hash-snapshotted in revision-r1-before/protected.json.

Only S03/S08 have source or new media; the 17-scene mapping at the end of storyboard.md is planning for other scenes. Master, ASR timestamps and intervals remain untouched. No music, SFX, new voice, subtitles, CTA, branding changes or human approval.
