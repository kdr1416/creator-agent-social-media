# Trần Minh Nhật — storyboard + pilot

- Full storyboard: `planning/storyboard.md` and editable `planning/storyboard.json`.
- Locked routing: `planning/scene_routing.json` and `.md`.
- Editable composition: `index.html`; local image/font/GSAP/voice assets.
- Final isolated pilot: `renders/tran-minh-nhat-pilot.mp4`.
- `render-src/visual-only.html` is a derivative for rendering picture before FFmpeg mux. The canonical composition retains its one original voice track.
- No TTS, music, time stretching, publishing or other scene renders.

Render from this project folder with Node.js and HyperFrames 0.8.170:

```powershell
npx --yes hyperframes@0.8.170 render --composition render-src/visual-only.html --quality delivery --fps 30 --workers 2 --output renders/visual-only.mp4
ffmpeg -n -i renders/visual-only.mp4 -i assets/scene_04.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -movflags +faststart renders/tran-minh-nhat-pilot.mp4
```

FFmpeg and FFprobe must be on PATH. Choose a new output filename when an export already exists. `npx --yes hyperframes@0.8.170 preview` opens the editable timeline with original audio.

Research notes: `.omc/research/tran-minh-nhat-2026-10-21.md` in repository. Scene10's mentor-experience claim needs verification before public release. The personal admissions result is supplied narrative, not independently verified. Campus photograph is from the official VU page; see `assets/ledger.json`. This private pilot does not establish a redistribution licence for institutional imagery or local Windows font files. Obtain appropriate rights before public distribution.

Existing audio_handoff, production_status, transcripts, raw script and all 17 voice slices are protected by before/after SHA256 records in `qa/`. New workflow handoff is saved as `scratch/render_handoff.json` without replacing an old file.
