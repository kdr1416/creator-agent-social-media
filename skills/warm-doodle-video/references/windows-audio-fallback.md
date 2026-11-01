# Single supplied voice fallback

Use only if the actual HyperFrames render fails its audio mix. Do not disable audio correctness checks or deliver a silent file as complete.

The three-scene experiment on Windows with HyperFrames0.8.170 encountered FFmpeg failing to infer an intermediate audio output format. Its source index and audio remain untouched. Rendering a derivative visual-only entry and muxing the supplied voice separately avoids that intermediate mix.

`scripts/render-single-voice.ps1` reproduces this fallback for a NEW isolated project with exactly one supplied narration track. Pass the project directory, narration WAV and an installed FFmpeg executable. It refuses to replace an existing final output, keeps `index.html` intact and preserves voice timing/gain. Its final audio is AAC-encoded, as for a normal MP4 export.

Example from the repository root:

```powershell
& 'skills/warm-doodle-video/scripts/render-single-voice.ps1' `
  -ProjectPath 'videos/my-new-doodle-project' `
  -NarrationPath 'videos/my-new-doodle-project/assets/narration.wav' `
  -FfmpegPath 'ffmpeg'
```

No stretched voice, replacement TTS or re-recorded narration. For BGM/SFX/multiple audio tracks, use the actual audio compositor and its mix contracts instead; this helper intentionally rejects them. Verify dimensions, non-silent audio, frame duration and original hashes after muxing.
