> Historical first-pilot document. Current R1 assets/source/evidence: revision-r1.md and asset ledger. Prior pilot NOT APPROVED.

# VIDEO-34 — First creative pilot / implementation notes

**AWAITING HUMAN REVIEW.** S03 and S08 only. Experimental Warm Mediterranean Editorial Illustration; no visual style/pilot approval, no full production. Working 1080×1920 / 30 FPS is authorized for this pilot, not approved for the whole film.

## Actual deliverables

| Scene | Review MP4 | Master range | Picture / exact voice |
|---|---|---|---|
| S03 | `../scenes/S03/S03-pilot.mp4` | [243986,458528) samples / 10.166083…–19.105333…s | 268 frames, 8.933333s / 214542 PCM samples, 8.939250s |
| S08 | `../scenes/S08/S08-pilot.mp4` | [966480,1101123) samples / 40.270000–45.880125s | 168 frames, 5.600000s / 134643 PCM samples, 5.610125s |

`../REVIEW.html` shows the two independent videos with controls and original global time ranges; playing one pauses the other. It never automatically plays the next scene. No connective narration, music, subtitles, SFX, CTA or logo redraw was added. Both excerpts keep their complete supplied sample intervals. Final MP4 uses AAC mono 24kHz, and the exact PCM WAV excerpt is retained beside each scene.

## Artwork actually created

- `assets/illustration/S03-coast.svg`: original coastal world, stone facade with enclosed colored balconies, striped café awning, tables/cups/chairs, curved limestone promenade, small square, sea/bay, plants, walkers, runner, café residents, friends and family. Named SVG groups are directly editable. The world is Malta-inspired composite geography, not a mapped route.
- `assets/illustration/S08-home.svg`: original home/terrace, reflected warm light, architecture/sea view, desk/chair/laptop, parent and child, separate gaze/head/arm/sleeve/hand/lid elements. A limited pose system supports this shot only.
- Two byte-exact scene WAV excerpts derived from the user master; a shared local GSAP runtime at `assets/vendor/gsap.min.js` and two scene copies of it, with license notice preserved. All seven real files plus the preserved Esora asset are in `assets/ledger.json`. No planned assets were represented as existing files. Regeneration uses the project-local runtime, not the old C1 fixture.

## Reusable implementation

`components/build_pilot_art.py` is the editable drawing source: path/line/ellipse/group helpers, window/gallarija module, plant, standing and seated illustration functions. It emits the two SVGs; it does not fetch stock art or install packages.

`components/pilot-motion.js` implements a finite stride helper and two explicit GSAP scene timelines. S03 uses limited spatial reframing, limb phases, café cup action and gaze/gesture changes. S08 uses explicit arm paths with shoulder/elbow/wrist control, gaze/head poses, fixed laptop hinge, timed hand contact and a small smile change. All state is driven by a paused GSAP timeline; no render-critical real-time callbacks.

`components/build_pilot_sources.py` embeds the canonical SVG and choreography into independent `scenes/S03/index.html` and `scenes/S08/index.html`; each entry resolves its runtime locally. It derives picture duration from **cumulative** rounded master sample boundaries at 30 FPS, and reads WAV excerpts by exact sample bounds. `build/pilot-working-config.json` records the resulting pilot-only sources, frame plan and outputs. The 17-scene input manifest remains byte-identical. Renderer entries for the other 15 scenes are intentionally not authored or configured; this is not a validation of a fully configured 17-scene production project.

## Visual decisions and observed limitations

Warm stone/ivory and desaturated sea green with clay accents, subtle static vector paper pattern, selective contour and contact shadows. No text inside either scene. S03 opens at a slightly closer crop, opens out once, then makes one small final reframe; it avoids five disconnected activity panels. S08 keeps the room and chair fixed, lets the hand clear the laptop, then establishes contact on the family cue. The final contact is held before the excerpt ends.

This is the first visual sample, not a claim of final advertising quality. S03 people are deliberately small; the family beat may need a stronger crop or more distinctive acting at phone size. The stride is stylized, without a full planted-foot/IK solver; silhouette and gait refinement remain a legitimate review item. S08 retains simplified hands/face and a mostly fixed torso; gaze clarity and emotional nuance can be refined after feedback. No visual test substitutes for the user's assessment of beauty, character design or naturalness.

## Measured QA

Evidence: `build/pilot-evidence/`.

| Check | Result and practical limit |
|---|---|
| HyperFrames 0.8.170 check | Both `ok: true`; no runtime errors. S03 layout findings 0. S08 retains one rotation_pivot_drift warning on the head: authored rotation around the neck, reviewed in keyframes. It is reported, not suppressed. |
| Silent picture warning | Both checks warn audio_file_without_element because picture source is intentionally silent. Voice is muxed separately; delivered MP4 audio and playback are independently verified. |
| Actual render | Both rendered at 1080×1920 / 30 FPS, 268/168 frames. DrawElement capture, hardware GPU; final logs record approximately 32.6s / 17.2s render time. No engine upgrade/dependency installation. |
| Source seeking | Screenshot SHA256 matches at 3.8s after forward and backward seeks in each scene. This is a measured sample, not an exhaustive proof at every frame. |
| SVG IDs/assets | Unique IDs, no failed resource requests or source-page console errors in browser QA. |
| S08 contact | At 5.4s, parent wrist and child hand center both (468,924) in SVG world coordinates, measured distance 0. This checks endpoint geometry, not anatomical quality. |
| Browser review | Chrome 150; 360/768/1280px widths, no horizontal overflow/console errors. Both video streams load at 1080×1920; early playback advances. At 1280px, each MP4 plays from start through ended with no media error. |
| Encoded frames | Six PNGs extracted from actual MP4s: S03 at 0/3.8/8.8s, S08 at 0/2.6/5.3s; opening/action/end inspected alongside source keyframes and 360×640 captures. |
| Voice integrity | Each PCM excerpt byte-matches its original sample interval; master SHA256 unchanged. Mono 24kHz retained. |
| AAC alignment | Decoded MP4 audio: 214542/134643 samples, peak waveform lag 0 samples in ±800-sample search. Zero-lag correlations 0.999925/0.999948. AAC is lossy; no sample-exact audiovisual-sync claim. |
| A/V duration | Container/audio 8.939250s and 5.610125s. Picture is 5.917ms / 10.125ms shorter from cumulative frame quantization; both differences < one 30-FPS frame. |
| Vietnamese glyphs | No text in video: N/A. Review page's Vietnamese text visually inspected. No new font downloaded. |
| Approval / safety | Human approval object remains pending. S13, master, scene timings/transcripts, logo, storyboard/style proposals and historical projects are not edited by pilot production. |

During iteration, browser QA caught a relative/absolute SVG path interpolation mismatch in smiles and a nested café-arm pivot error; both were corrected before the final renders. A QA-script timeout came from returning the GSAP timeline object to Puppeteer; QA now returns only compact measurements. These fixes are local to video-34. HyperFrames usage query returned unknown; no allowance claims are made. The installed CLI reports a newer version available; the existing version is preserved under the no-install instruction.

## Reproduce or edit one scene

From repository root, the installed CLI entry used is:
`C:/Users/LENOVO/AppData/Local/npm-cache/_npx/110f701c48e68d66/node_modules/hyperframes/bin/hyperframes.mjs`.

Example S08-only iteration; replace S08 with S03 for the other scene:

```powershell
# Edit the relevant drawing function or canonical SVG, and relevant motion branch.
# Run the first command only if regenerating SVG from the drawing source.
python videos/video-34/components/build_pilot_art.py --scene S08
python videos/video-34/components/build_pilot_sources.py --scene S08
$env:PUPPETEER_EXECUTABLE_PATH='C:/Program Files/Google/Chrome/Application/chrome.exe'
node C:/Users/LENOVO/AppData/Local/npm-cache/_npx/110f701c48e68d66/node_modules/hyperframes/bin/hyperframes.mjs check videos/video-34/scenes/S08 --json
node C:/Users/LENOVO/AppData/Local/npm-cache/_npx/110f701c48e68d66/node_modules/hyperframes/bin/hyperframes.mjs render videos/video-34/scenes/S08 --fps 30 --workers 1 --quality looks --output 'D:/Năm 3/flowkit-main/videos/video-34/scenes/S08/picture.mp4'
ffmpeg -hide_banner -y -i videos/video-34/scenes/S08/picture.mp4 -i videos/video-34/scenes/S08/voice-excerpt.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 128k -ar 24000 -movflags +faststart videos/video-34/scenes/S08/S08-pilot.mp4
python videos/video-34/build/pilot-media-qa.py
node videos/video-34/build/pilot-browser-qa.cjs
```

Do not regenerate an SVG after manually editing it unless its drawing source has also been updated. The assembly helper's `--scene` option leaves the other scene's entry/excerpt untouched. If a shared primitive changes, review its dependents and refresh ledger/state hashes; do not assume their old QA remains current. No commands above authorize creation of the other 15 scenes or record human approval.

S03 Studio preview was launched at `http://localhost:8860/#project/S03`, HTTP 200 verified; it exposes the editable picture/timeline, while REVIEW contains the finished audio-bearing MP4s. Preview stop command: installed CLI `preview videos/video-34/scenes/S03 --stop`.

## Rollback / continuation

Before-change hashes and scoped copies are in `scratch/video34-pilot-implementation-backup-20261101/` at repository root. Five preexisting files were backed up: project manifest, production status, scene manifest, asset ledger and REVIEW.html. The scene manifest was never changed. Restore only actually changed preexisting files after protecting any later user edits; move this pilot's new assets/sources/build evidence to a separate backup if discarding it. No destructive Git/delete operation is needed. Preserve the original Esora logo/master and all older video projects.

Request changes with scene ID + local time + desired visual/action, e.g. “S03 2.5s: make the runner's stride more natural” or “S08 4.7s: hold the gaze before hand contact.” Only the named scene will be revised/rendered unless the requested change intentionally affects shared artwork. Approval remains a separate explicit human decision.
