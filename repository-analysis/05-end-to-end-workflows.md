# 05. End-to-End Workflow Analysis

## Workflow 1: Project Creation & Character Bible Inception

```mermaid
sequenceDiagram
    autonumber
    actor User as Agent / User
    participant Router as POST /api/projects
    participant CRUD as DB CRUD (crud.py)
    participant Disk as File System (output/)

    User->>Router: POST /api/projects (name, story, material, characters)
    Router->>CRUD: create_project()
    loop For each entity
        Router->>Router: _build_character_profile() (apply COMPOSITION_GUIDELINES)
        Router->>CRUD: create_character()
        Router->>CRUD: link_project_character()
    end
    Router->>Disk: Ensure project output folders (output/{name}/raw, etc.)
    Router-->>User: 200 OK (Project JSON with populated entities)
```

| Step | Module | File | Function | Input | Output | Responsibility |
|---|---|---|---|---|---|---|
| 1 | API | `agent/api/projects.py` | `create()` | `ProjectCreate` payload | Project JSON | Validates input, generates UUIDs, sets paygate tier & material. |
| 2 | Logic | `agent/api/projects.py` | `_build_character_profile()` | Entity metadata & story | Image prompt + description | Applies orientation (portrait for characters, landscape for locations) and style guidelines. |
| 3 | Database | `agent/db/crud.py` | `create_character()` | Entity dictionary | Character record | Persists character/location with generated slug. |
| 4 | Storage | `agent/api/projects.py` | `Path.mkdir()` | Output directory path | Directory tree | Prepares `output/{project_name}/raw`, `review_full`, etc. |

---

## Workflow 2: Asynchronous Request Batch Pipeline & Worker Dispatch

```mermaid
sequenceDiagram
    autonumber
    actor Agent as CLI / Skill
    participant API as POST /api/requests/batch
    participant DB as SQLite DB
    participant Worker as WorkerController (_run_loop)
    participant Limiter as APIRateLimiter
    participant Ops as OperationService
    participant Prov as MediaProvider (Flow / Assistant)
    participant Bus as EventBus

    Agent->>API: POST /api/requests/batch ([RequestCreate, ...])
    API->>DB: Idempotent insert: create_request() for each (status=PENDING)
    API-->>Agent: 200 OK (List of Request records)
    
    loop Every POLL_INTERVAL (5s)
        Worker->>DB: list_actionable_requests()
        DB-->>Worker: Return actionable PENDING requests
        loop For each request
            Worker->>Worker: Check prerequisites (_prerequisites_met)
            alt Prerequisites missing
                Worker->>Worker: Defer request for 30s
            else Prerequisites satisfied
                Worker->>Limiter: acquire() [concurrency slot + cooldown]
                Limiter-->>Worker: Gate opened
                Worker->>DB: update_request(status='PROCESSING')
                Worker->>Bus: emit('request_update', status='PROCESSING')
                Worker->>Ops: _dispatch(req)
                Ops->>Prov: provider.run(job)
                Prov-->>Ops: Generation result (media_id, output_url)
                Worker->>DB: update_request(status='COMPLETED', media_id, output_url)
                Worker->>DB: apply_scene_result() or apply_character_result()
                Worker->>Bus: emit('request_update', status='COMPLETED')
                Worker->>Limiter: release()
            end
        end
    end
```

| Step | Module | File | Function | Input | Output | Responsibility |
|---|---|---|---|---|---|---|
| 1 | API | `agent/api/requests.py` | `create_batch()` | `BatchRequestCreate` | List of `Request` | Ingests requests atomically, auto-sets video orientation, skips active duplicates. |
| 2 | Worker | `agent/worker/processor.py` | `_run_loop()` | - | PENDING requests | Queries queue, orders by priority (character > image > video > upscale). |
| 3 | Worker | `agent/worker/processor.py` | `_prerequisites_met()` | `req`, `orientation` | Boolean | Checks that image exists before video gen, and video exists before upscale. |
| 4 | Worker | `agent/worker/processor.py` | `APIRateLimiter.acquire()` | - | - | Throttles requests per provider (e.g. 5 concurrent, 10s cooldown for Flow). |
| 5 | Orchestrator | `agent/sdk/services/operations.py` | `_run_provider_job()` | `ProviderJob` | Result Dict | Resolves provider via registry, verifies capabilities, calls `provider.run()`. |
| 6 | Database | `agent/sdk/services/result_handler.py` | `apply_scene_result()` | `media_id`, `output_url` | DB update | Writes image/video URLs and media IDs into `scene` table. |
| 7 | Events | `agent/services/event_bus.py` | `emit()` | Event JSON | Broadcast | Pushes real-time progress to connected dashboard clients. |

---

## Workflow 3: Google Flow Chrome Extension BatchRPC & Anti-Detection Bypass

```mermaid
sequenceDiagram
    autonumber
    participant Prov as FlowProvider
    participant Client as FlowClient (WebSocket)
    participant BG as extension/background.js
    participant Page as Flow Tab (MAIN World)
    participant Trap as hijack_bypass.js
    participant Google as Google Flow Backend

    Prov->>Client: batch_rpc(rpcid, freq, captchaAction)
    Client->>BG: WS Send: {method: 'batch_rpc', params: {...}}
    BG->>BG: Find or open active flow.google.com tab
    Note over Trap,Page: hijack_bypass.js trapped pristine grecaptcha at document_start
    BG->>Page: captchaFromTab() -> calls pristine grecaptcha.enterprise.execute()
    Page-->>BG: Return genuine Enterprise reCAPTCHA token
    BG->>BG: Substitute __CAPTCHA__ placeholder with token
    BG->>Page: chrome.scripting.executeScript(runBatchRpc)
    Page->>Page: Read WIZ_global_data (SNlM0e / at, FdrFJe / sid, cfb2h / bl)
    Page->>Google: fetch(/_/AiSandboxAngularFrontend/data/batchexecute, {f.req, at, credentials:'include'})
    Google-->>Page: Chunked response )]}' + ["wrb.fr", rpcid, "..."]
    Page-->>BG: Return response text
    BG->>Client: POST /api/ext/callback {id, status, data} (Resilient HTTP)
    Client-->>Prov: Resolve pending asyncio.Future
```

| Step | Module | File | Function | Input | Output | Responsibility |
|---|---|---|---|---|---|---|
| 1 | Service | `agent/services/flow_client.py` | `batch_rpc()` | RPC ID, freq payload | Pending Future | Creates promise tracked in `_pending[req_id]`, forwards command over WebSocket. |
| 2 | Extension | `extension/background.js` | `handleBatchRpc()` | WS message | Injected execution | Identifies candidate Flow tab; triggers tab revival if discarded by Chrome. |
| 3 | Extension | `extension/hijack_bypass.js` | `savePristine()` | Function reference | `window.__fk_hijack` | Intercepts original reCAPTCHA execute before Google's `x2a` tamper script wraps it. |
| 4 | Extension | `extension/background.js` | `captchaFromTab()` | `captchaAction` | reCAPTCHA Token | Executes in-page token mint using unpoisoned function. |
| 5 | In-Page | `extension/background.js` | `runBatchRpc()` | RPC parameters | HTTP Response text | Extracts `WIZ_global_data.SNlM0e` (`at` token) and performs browser fetch with session cookies. |
| 6 | Bridge | `agent/main.py` | `ext_callback()` | Result payload + Secret | Confirmation | HTTP fallback callback that sets result on `_pending[req_id]` Future. |

---

## Workflow 4: Video Quality Review & Auto-Regeneration Loop

```mermaid
sequenceDiagram
    autonumber
    actor User as User / Review Skill
    participant API as POST /api/videos/{vid}/review
    participant Reviewer as VideoReviewer (video_reviewer.py)
    participant FFmpeg as FFmpeg Binary
    participant Vision as Claude Vision / CLI Agent
    participant CRUD as DB CRUD
    participant ReqAPI as POST /api/requests

    User->>API: POST /api/videos/{vid}/review?mode=light
    API->>Reviewer: review_video(video_id, mode)
    loop For each scene video
        Reviewer->>FFmpeg: Extract frames (4 FPS light, 8 FPS deep)
        FFmpeg-->>Reviewer: Raw PNG/JPG frames
        Reviewer->>Reviewer: Build contact sheet (3x3 grid image)
        Reviewer->>Vision: Submit contact sheet + scene prompt + character refs
        Vision-->>Reviewer: JSON score (6 dimensions, errors, notes)
        Reviewer->>Reviewer: Compute overall weighted score (0.0 - 10.0)
        alt Score < 7.5 (Failed Quality Gate)
            Reviewer->>Reviewer: Generate prompt fix directives (_fix_guide)
            Reviewer->>CRUD: Update scene video_prompt with fix directives
            Reviewer->>ReqAPI: Create REGENERATE_VIDEO request
        end
    end
    Reviewer-->>API: Full VideoReview report
    API-->>User: 200 OK (Scores, verdicts, regenerated scenes)
```

| Step | Module | File | Function | Input | Output | Responsibility |
|---|---|---|---|---|---|---|
| 1 | API | `agent/api/reviews.py` | `review_video_endpoint()` | `video_id`, `mode` | `VideoReview` JSON | Entry point for automated visual quality assessment. |
| 2 | Service | `agent/services/video_reviewer.py` | `_extract_frames()` | Video file path, FPS | Frame image files | Uses FFmpeg to extract sequential video frames into temporary storage. |
| 3 | Service | `agent/services/video_reviewer.py` | `_build_contact_sheet()` | Frame array | Single JPEG image | Assembles 9 frames into a 3x3 contact sheet for token-efficient vision analysis. |
| 4 | Vision | `agent/services/video_reviewer.py` | `_call_vision_cli()` or API | Sheet image + Prompt | Dimension scores | Prompts Claude / CLI reviewer to grade visual quality across 6 weighted dimensions. |
| 5 | QA Gate | `agent/services/video_reviewer.py` | `_compute_overall()` | Dimension scores | Overall score | Computes weighted score. Triggers auto-regen if score < 7.5 (up to 2 cycles). |

---

## Workflow 5: Narration, Music & Final Video Assembly

```mermaid
sequenceDiagram
    autonumber
    actor Agent as CLI / User
    participant ConcatAPI as POST /api/videos/{vid}/concat
    participant TTS as TTS Service (tts.py)
    participant FFmpeg as PostProcess (post_process.py)
    participant Disk as Output Directory

    Agent->>ConcatAPI: POST /api/videos/{vid}/concat (fit_narrator=True)
    loop For each scene
        opt If narrator_text present
            ConcatAPI->>TTS: generate_tts(narrator_text)
            TTS->>TTS: Subprocess OmniVoice + tail padding + fade
            TTS-->>ConcatAPI: Generated WAV audio path & duration
            ConcatAPI->>FFmpeg: trim_video(scene.mp4, 0, audio_duration)
            FFmpeg-->>ConcatAPI: Trimmed scene MP4
        end
        ConcatAPI->>FFmpeg: normalize_clip(scene.mp4, H.264/AAC, 30fps)
        FFmpeg-->>ConcatAPI: Normalized clip
    end
    ConcatAPI->>FFmpeg: merge_videos(clips, final_path)
    opt If BGM requested
        ConcatAPI->>FFmpeg: Mix background music with audio ducking
    end
    ConcatAPI-->>Agent: 200 OK (Final Master Video Path & Duration)
```

| Step | Module | File | Function | Input | Output | Responsibility |
|---|---|---|---|---|---|---|
| 1 | Audio | `agent/services/tts.py` | `generate_tts()` | `narrator_text`, voice ref | WAV audio file | Executes OmniVoice in isolated subprocess; appends 0.4s silence and 0.06s fade-out. |
| 2 | FFmpeg | `agent/services/post_process.py` | `trim_video()` | Video path, start, end | Trimmed MP4 | Trims scene video exactly to narrator speech duration. |
| 3 | FFmpeg | `agent/services/post_process.py` | `normalize_clip()` | Clip path | Standardized MP4 | Transcodes video to uniform `h264/yuv420p` + 48kHz AAC stereo. |
| 4 | FFmpeg | `agent/services/post_process.py` | `merge_videos()` | List of clip paths | Concat text demuxer | Concatenates normalized clips using FFmpeg concat demuxer without re-encoding. |
