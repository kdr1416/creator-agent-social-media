---
style: reference-led-cartoon-collage-reconstruction
canvas: 720x1280
duration: 15
fps: 30
audio: none
font: ReferenceSans
---

# Design truth — reconstruct source0–15s

User now explicitly requests reconstruction of the first15s of the supplied video, without audio. Reproduce its subject, wording, sequence, layout and colour relationships as closely as practical; the earlier skill's originality guideline yields to this direct reconstruction request. Build new vector environments/mascots, not a full-frame source-video trim. Reuse only small authentic product UI crops as textures.

Use the actual source frames in reference/ as visual ground truth. Source360×640 maps exactly2× to720×1280. Maintain the original full-height layout, including source bottom props and week line: this deliberate reference-reconstruction overrides adding a new200px subtitle footer. No added caption track.

Fonts: local Arial regular and bold, aliased ReferenceSans. Exact source font unidentified; choose regular/medium visual weight and approximate its form, not the rejected Segoe UI Bold. Main ordinary text32–38px, banner text36–42px, secondary24–28px. Dark ink#30323B, white text on red#C83432, orange#F57931 and vivid blue#079CF0. These bright strips are small typography accents, not cards.

Street: peach wash#FFE9D8/#FFD7BC, lavender buildings and yellow windows, neutral gray road. Street begins with a tight close view and rapidly pulls back. Night: blue#222B53, warm yellow moon/window, clay roof. Room: pale lilac#EBE3ED wall, tan#EAD0B3 floor, pink rug/curtains, blue-to-teal cylinder desk, warm orange mascot. Laptop: large screen above, mascot and animated school below. Study plan: soft cream#FFF4E9, blue heading, real screenshot with tape, actual metric16 weeks, small mascot moves along W1–W8.

Shared assets/youpass-kit.js exposes YP.mascot(id,x,y,scale,color,headband,helmet), YP.scooter(id,x,y,scale,bodyColor,riderColor,helmetColor), YP.school(id,x,y,scale,face), YP.plant(id,x,y,scale), YP.sparkle(...). Read helper source if using its limbs. Static SVG transforms on helper root must be preserved; animate a separate outer wrapper for travel. All actor IDs prefix scene-specific names. Use direct path deformation or local transformOrigin percent for nested limbs; verify no detachment.

Host loads assets/style.css, GSAP and kit. Scenes are template subcompositions with IDs matching scene filenames. Put styles/scripts inside template. No audio/video node; single registered paused timeline per scene; deterministic and finite. Avoid CSS-transform/GSAP conflicts and repeated fromTo immediateRender mutations. Main editor assembles and owns between-scene seams. Palette and scene staging follow the actual frames, not the old sample project.
