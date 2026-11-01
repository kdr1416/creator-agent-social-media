# 07. API, Event & Integration Analysis

## 1. REST API Endpoint Catalog

Flow Kit exposes 14 API routers under `/api`. Below is the complete catalog of primary production endpoints:

### Project Management (`/api/projects`)
- `POST /api/projects`: Create project with automated character/location bible setup.
- `GET /api/projects`: List all active projects.
- `GET /api/projects/{id}`: Retrieve project details.
- `PATCH /api/projects/{id}`: Update project metadata, story, or paygate tier.
- `DELETE /api/projects/{id}`: Soft delete (sets `status='DELETED'`).
- `GET /api/projects/{id}/characters`: List associated character entities.
- `GET /api/projects/{id}/output-dir`: Get physical disk output path.

### Video Management (`/api/videos`)
- `POST /api/videos`: Create a video under a project.
- `GET /api/videos/{id}`: Retrieve video details with scene list.
- `PATCH /api/videos/{id}`: Update video title, tags, or orientation.
- `DELETE /api/videos/{id}`: Cascade delete video and scenes.
- `POST /api/videos/{id}/concat`: Trigger FFmpeg concatenation with optional TTS audio ducking.
- `POST /api/videos/{id}/publish`: Upload video to YouTube using configured channel rules.

### Scene Management (`/api/scenes`)
- `POST /api/scenes`: Create scene with prompt, character references, and chain type.
- `GET /api/scenes/{id}`: Retrieve scene details.
- `PATCH /api/scenes/{id}`: Mutate scene prompts, narrator text, or trim parameters without deleting downstream media IDs.
- `DELETE /api/scenes/{id}`: Delete scene.
- `POST /api/scenes/reorder`: Reorder scene display sequence for a video.
- `POST /api/scenes/{id}/continuation`: Create a downstream scene chained to this scene's end frame.

### Request Queue & Batch Operations (`/api/requests`)
- `POST /api/requests`: Submit a single generation request (409 Conflict if active request exists).
- `POST /api/requests/batch`: Submit multiple requests atomically; skips duplicates idempotently.
- `GET /api/requests/batch-status`: Poll aggregate status (`total`, `pending`, `processing`, `completed`, `failed`, `done`, `all_succeeded`).
- `GET /api/requests`: List requests with optional filters (`status`, `scene_id`, `video_id`, `project_id`).

### Provider Job Queue (`/api/provider-jobs`)
- `POST /api/provider-jobs`: Enqueue external generation job (`QUEUED`).
- `GET /api/provider-jobs/wait-next`: Long-poll endpoint to claim the next available job.
- `POST /api/provider-jobs/{id}/heartbeat`: Extend active worker lease.
- `POST /api/provider-jobs/{id}/progress`: Update percentage progress (0-100%).
- `POST /api/provider-jobs/{id}/complete`: Mark job `SUCCEEDED` with result URLs and media IDs.
- `POST /api/provider-jobs/{id}/fail`: Mark job `FAILED` with error message.

### Video Quality Review (`/api/reviews`)
- `POST /api/videos/{vid}/review`: Run automated vision quality evaluation (`light` or `deep` mode).
- `GET /api/videos/{vid}/review`: Retrieve latest review results and dimension scores.

### Audio & Music (`/api/tts` & `/api/music`)
- `POST /api/tts/generate`: Synthesize speech from text using OmniVoice.
- `POST /api/music/generate`: Request background track generation via Suno API.
- `POST /api/music/callback`: Webhook receiver for Suno generation completion.

### Extension Bridge Internals (`/api/ext`)
- `POST /api/ext/callback`: Resilient HTTP response callback from Chrome extension (requires `X-Callback-Secret`).
- `GET /api/ext/tabs`: List active Flow tabs detected by the extension.
- `POST /api/ext/netlog`: Netlog receiver for reverse-engineering batchexecute RPC payloads.

---

## 2. WebSocket Protocols

### 2.1 Extension Bridge WebSocket (`ws://127.0.0.1:9222`)
- **Server**: Ran by Python agent (`agent/main.py:run_ws_server`).
- **Client**: Chrome Extension background service worker (`extension/background.js`).
- **Handshake**:
  1. Extension connects to `ws://127.0.0.1:9222`.
  2. Agent sends: `{"type": "callback_secret", "secret": "<32-byte-token>"}`.
  3. Extension saves secret in `chrome.storage.local`.
- **Command Messages (Agent -> Extension)**:
  - `{"id": "<uuid>", "method": "batch_rpc", "params": {"rpcid": "ogiZ0b", "freq": "...", "captchaAction": "IMAGE_GENERATION"}}`
  - `{"id": "<uuid>", "method": "solve_captcha", "params": {"captchaAction": "VIDEO_GENERATION"}}`
  - `{"id": "<uuid>", "method": "reload_extension"}`
  - `{"id": "<uuid>", "method": "list_tabs"}`
- **Response Messages**:
  - Sent back either over WS: `{"id": "<uuid>", "status": 200, "data": "<batchexecute-response>"}`
  - Or via HTTP fallback: `POST /api/ext/callback` with header `X-Callback-Secret`.

### 2.2 Dashboard Real-Time WebSocket (`/ws/dashboard`)
- **Endpoint**: `GET /ws/dashboard` (Upgrade to WebSocket).
- **Security**: Origin check enforces connections only from `localhost`, `127.0.0.1`, or `chrome-extension://`.
- **Initial Snapshot**:
  ```json
  {
    "type": "snapshot",
    "health": { "status": "ok", "extension_connected": true },
    "requests": [ ... active pending and processing requests ... ],
    "worker": { "active": 2, "slots": 3 }
  }
  ```
- **Live Stream Events**: Emits `request_update`, `worker_tick`, and `log_entry` in real time.

---

## 3. External Services & Third-Party Integrations

| Integration | Purpose | Entry Point / File | Data Contract | Credentials / Env | Failure Handling |
|---|---|---|---|---|---|
| **Google Flow** | Image & Video generation (Veo 2/3, Omni Flash) | `agent/services/flow_batch.py`, `extension/background.js` | Google `batchexecute` RPCs with `f.req` envelopes | Active logged-in Google session cookies in browser | Automatic tab revival, reCAPTCHA retry, cooldown backoff on `UNUSUAL_ACTIVITY` |
| **Anthropic Claude** | Vision QA and video review | `agent/services/video_reviewer.py` | JSON frame analysis payload | `ANTHROPIC_API_KEY` | Graceful fallback to local CLI providers (`claude`, `agy`, `codex`) |
| **Suno AI** | Background music generation | `agent/services/suno.py` | REST API (`api.sunoapi.org/api/v1/gateway`) | `SUNO_API_KEY` (env or `channel_rules.json`) | Webhook callback with polling fallback up to 600s |
| **OmniVoice** | Neural voice synthesis | `agent/services/tts.py` | Isolated Python subprocess CLI | Local weights (`k2-fsa/OmniVoice`) | Subprocess timeout (120s), audio tail padding & fade-out |
| **YouTube API** | Video publishing & scheduling | `youtube/upload.py`, `youtube/auth.py` | Resumable chunked upload (`MediaFileUpload`) | OAuth2 `client_secrets.json` & stored user tokens | Exponential backoff for upload errors; skips if token invalid |
| **muse.ai** | Alternative video provider | `agent/services/muse2api_client.py` | OpenAI-compatible HTTP gateway | `MUSE2API_URL`, `MUSE2API_KEY` | Failover across up to 3 accounts with 1800s timeout |
