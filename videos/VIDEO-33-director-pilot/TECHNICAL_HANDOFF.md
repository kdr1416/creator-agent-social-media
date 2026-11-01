> **S05 R1 đã duyệt:** đặt ghim Malta → cắt sang ảnh nhà thật. Dùng [hướng dẫn Antigravity](handoff/S05_STORYBOARD_RESTART_R1/ANTIGRAVITY_PROMPT.md) để dựng pilot riêng. Chưa duyệt frame/motion S05 mới; không dựng full phim. Thông báo này thay trạng thái chờ duyệt S05 ở lịch sử bên dưới.

> **Cập nhật S05:** Album v5 không được duyệt. Mọi mô tả/hình S05 bên dưới là lịch sử và được thay bằng [storyboard viết lại R1](handoff/S05_STORYBOARD_RESTART_R1/S05_STORYBOARD.md), đang chờ duyệt. Hai pilot đã duyệt là S01 bản đầu + S09 motion r1. Chưa dựng frame/pilot mới hoặc full phim.

# Technical handoff

## Source and timing

`inputs/source_audio.wav`: original PCM16, mono, 24,000Hz, 1,803,840 sample frames = 75.16s. Copied WAV and all original slices/transcripts remain unchanged. All 17 slices reassemble bit-for-bit; original/reference files are hashed before and after. See qa/source-integrity.json and qa/audio-source-verification.json.

14 scene intervals are exact half-open sample ranges [start, end). Use sample bounds, never the rounded timestamps printed in a Markdown table. Corrected text is editorial metadata, not a replacement voice. Seg13 con gái/con cái remains uncertain; do not silently change it or claim phonetic verification. Internal cue times are approximate director marks, not forced word alignment.

## Three delivered exports

| Scene | Source samples | Voice seconds | Video frames at 30fps | Picture seconds | AAC/source correlation |
|---|---:|---:|---:|---:|---:|
| S01 | 144466 | 6.019416667 | 181 | 6.033333 | 0.999912 |
| S05 | 136952 | 5.706333333 | 172 | 5.733333 | 0.998781 |
| S09 | 178822 | 7.450916667 | 224 | 7.466667 | 0.999908 |

AAC is lossy and therefore cannot be bit-identical to PCM; correlation verifies alignment/content and non-silent audio. Exact PCM is shipped. No TTS, speed, pitch, EQ, added soundtrack or removed pauses. Successful native HyperFrames audio export; the fallback was not used.

## Future film assembly — only after user approval

Use planning/picture_frame_plan.json/.csv. Global boundary = round-half-up(start_sample × 30 / 24000), not accumulated scene duration. 2255 picture frames for the full 75.16s voice. This is a plan, not a produced full film.

Standalone pilot rounding uses ceil frames, and S05 is one frame longer than its assigned global picture slot. For future assembly derive a picture-only copy to the global slot count; keep source pilot untouched. Place exactly one full `inputs/source_audio.wav` at t=0 over assembled picture. Do not join independently AAC-encoded pilot voices for the final film: encoder padding can drift. Keep final hold through the last voice sample; no artificial black-out at audio end.

## Editable source

Each pilot has `index.html`, local `assets/voice.wav`, GSAP, fonts, an editable `layered-art.svg`, `hyperframes.json`, `package.json`, `frame.md` and `renders/pilot.mp4`. HTML owns placement/timing; SVG is a layer extraction, not an extra imported duplicate. When editing the SVG separately, sync its changed markup back into HTML. Rig travel wrappers surround fixed SVG placement groups; arm paths/hand endpoints move together. Far arm behind torso, near arm in front.

One paused GSAP timeline per root, matching composition ID. Deterministic, offline media; no unseeded random, render clock or network fetch. Root width/height 100%, canvas data-width=720/data-height=1280. Prefix new IDs. To mount as subcomposition, put styles/scripts inside `<template>`; read the installed HyperFrames core contract first. Current projects are standalone pilots.

Reproducible commands per pilot: `npx hyperframes@0.8.170 check --at 0,1.5,3.3,5.8 --json` (adapt times to duration); `npx hyperframes@0.8.170 preview --background`; `npx hyperframes@0.8.170 render --fps 30 --quality delivery --workers 2 --output renders/pilot.mp4`. Current environment used cached official CLI directly to avoid npm DNS. Browser execution required normal local permissions. Version 0.8.170 matched CLI latest metadata. Workflow skill refresh failed DNS; already-installed skill files were read, no successful refresh is claimed. Usage API returned unknown.

Python utilities are persistent project tools, not API batch submitters: prepare.py generates initial direction (refuses overwrite); build_pilots.py rebuilds ONLY three sources; finalize.py verifies exports and builds proof/handoff. Run finalize after any render change. Do not rerun build_pilots over manual edits without deliberately integrating them first. No calls to media-generation API were made.

## Validation limits

Native HyperFrames check passed lint/runtime/layout/contrast for all three at actual sampled times. Motion assertions are not enabled; visual proof and browser playback are separate evidence. Cmap tested all Vietnamese precomposed characters plus every visible scene string; raster/mobile proof required as well. Current reference comparison does not constitute user approval.

Footer y=1080–1280 remains free of important visuals. Main text 44–76px, S01 final strip 46px, not Arial Black. Font licensing/provenance and photo attribution are in CREDITS.md. Flow server was unreachable at preflight; all scenes positively route to HF_ONLY, so no Flow request/ref/UUID/video-review branch is required. Future engine changes need an explicit routing override.

## Local review server

REVIEW.html and STORYBOARD.html also work as local files for offline review. Current local viewer: http://127.0.0.1:8766/REVIEW.html . If it stops, serve this folder with `python -m http.server 8766 --bind 127.0.0.1`; stop with Ctrl+C. No files are published externally. Studio source preview S01: http://localhost:3002/#project/S01 . Browser MP4s were observed to reach their ends (qa/playback-review.json); this is separate from independent perceptual listening.


## Hai pilot chuyển động mới · r1

Đã dựng S05 theo frame v3 và S09 theo frame v2 đã duyệt. Xem `revisions/pilots-approved-frames-r1/REVIEW.html`; MP4/source/asset local nằm trong các thư mục S05 và S09 cạnh trang đó. Voice PCM đúng lát gốc. Bản chuyển động r1 đang chờ người dùng duyệt; không tự coi việc yêu cầu render là duyệt motion, không dựng full. Pilot cũ giữ nguyên để đối chiếu.

Mốc cue mới: S05 bắt đầu mở ban công khoảng 4.32s local theo cụm bất động sản trong ASR; S09 mở phân bổ khoảng 2.43s local theo cụm nhiều thị trường. Đây là bằng chứng timing ASR, không thẩm âm độc lập. Xem DIRECTION.json và verification.json ở revision.


## S05 motion r2 — sửa tính hợp lý, chờ duyệt

S05 motion r1 bị người dùng phản hồi ảo/phi logic. Bản r2 tại `revisions/S05-motion-r2/renders/pilot.mp4` bỏ mọi co giãn mặt nhà/ban công. Giữ ngôi nhà và ban công nguyên hình, không scale/skew/morph/fade. Mascot mở một bìa giấy có bản lề ở góc phải; bước ngang theo mép bìa đang quay, buông tay trước khi bước về vị trí kết. Bìa che được mở đi để lộ kiến trúc có sẵn, không biến giấy thành nhà. Voice nguyên lát nguồn. Frame kiến trúc v3 là tham chiếu đã duyệt; pose kết được chỉnh sau nhả tay để đúng hành động, chưa tự coi motion r2 là đã duyệt. S09 r1 giữ nguyên. Trang xem mới: `revisions/S05-motion-r2/REVIEW.html`.


## S05 hiện tại · album v5 / pilot r1

Người dùng đã duyệt frame album v5 và yêu cầu dựng pilot. MP4 hiện tại: `revisions/S05-album-pilot-v5-r1/renders/pilot.mp4`; source cạnh đó. Mascot ngồi sau bàn, hai tay giữ đúng mép trang album ảnh nhà thật. Cuốn sổ đang mở được hạ phẳng dần để giới thiệu ảnh; ảnh luôn in trên giấy, không trở thành khối nhà. Kết bám frame v5 đã duyệt. Bản chuyển động đang chờ duyệt; voice giữ nguyên, S09 r1 giữ nguyên. Các hướng nhà giấy/phố trước đây là lịch sử, không dùng để thi công tiếp. CREDITS.md/.json trong revision lưu nguồn ảnh và license.
