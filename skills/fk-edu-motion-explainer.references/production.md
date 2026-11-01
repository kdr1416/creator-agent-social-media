# Production contract

1. Read the project manifest, scene manifest, storyboard, style tokens and production state. Confirm explicit approval before non-pilot production.
2. Build one independent source module per scene. HyperFrames scenes follow `hyperframes-core` (paused seekable timeline, root ID matching timeline key, deterministic local assets). Remotion scenes follow its frame-based composition contract; use their TSX entry/composition ID, not a required HTML file.
3. Use sample bounds from original PCM for audio slices; do not stretch or regenerate the master. Keep raw alignment separate from corrected transcript.
4. For generated-media scenes only, load the relevant `fk-*` skill and obey reference-first, UUID, material, batch, throttling and review-before-upscale contracts. Exact typography belongs in the compositor. Overlay geometry follows approved style and observed footage.
5. Use `tools/codex_project.py` from repository root for template validation, frame plan, individual rendering and FFmpeg assembly. Read the template README for command contracts. It does not install engines, run a pilot automatically or call a backend.
6. Follow motion-and-qa.md before marking visual QA complete. Record actual media measurements separately from human approval. Invalidate stale scene renders after edits and rerender only the affected scene; rebuild final assembly afterwards.
7. Keep source, assets and state in the same project for Codex continuation. Antigravity may use the same files for support/production if explicitly requested; no new handoff package is required.
