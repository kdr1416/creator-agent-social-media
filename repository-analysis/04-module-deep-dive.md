# 04. Module Deep Dive

## 1. Module Analysis Matrix

```text
agent/
├── api/             -> Inbound HTTP route controllers
├── db/              -> SQLite schema & CRUD transactions
├── models/          -> Pydantic schema validation & domain models
├── sdk/             -> Core SPI, OperationService & ProviderRegistry
├── services/        -> Domain services (FlowClient, FlowBatch, Reviewer, TTS, Suno, PostProcess)
├── worker/          -> Background request processor, rate limiters & parsing
└── utils/           -> Path resolution & slugification
```

---

## 2. Deep Dive: API Module (`agent/api/`)

### 2.1 `requests.py`
- **Purpose**: Ingestion and batch status tracking of media generation requests.
- **Key Functions**:
  - `create(body: RequestCreate)`: Creates a single generation request; checks if an active request (`PENDING` or `PROCESSING`) for the same scene + type already exists (returns 409 Conflict if so). Auto-syncs video orientation.
  - `create_batch(body: BatchRequestCreate)`: Ingests an atomic array of requests. Deduplicates idempotently: skips duplicate active requests without throwing errors, returning existing request records.
  - `get_batch_status(video_id, req_type, project_id)`: Aggregates counts of pending, processing, completed, and failed requests to return overall status flags (`done`, `all_succeeded`).
- **Dependencies**: `agent/db/crud.py`, `agent/models/request.py`.
- **Extension Points**: Inject custom request preprocessing filters or webhook triggers on completion.

### 2.2 `projects.py` & `project_characters.py`
- **Purpose**: Project lifecycle management, character profile generation, and reference entity bindings.
- **Key Functions**:
  - `create(body: ProjectCreate)`: Creates project, creates associated character/entity records (characters, locations, generic troops, visual assets), initializes folder structure in `output/{project_name}/`, and triggers prompt composition.
  - `_build_character_profile(...)`: Generates strict reference image prompts based on entity type (`COMPOSITION_GUIDELINES`) and material style instructions.
- **Dependencies**: `agent/materials.py`, `agent/utils/slugify.py`.

### 2.3 `scenes.py`
- **Purpose**: Scene CRUD, ordering, prompt mutation, and continuation scene creation.
- **Key Functions**:
  - `create(body: SceneCreate)`: Registers a new scene.
  - `create_continuation(scene_id: str, body: ContinuationCreate)`: Creates a downstream continuation scene that inherits the parent's end-frame media ID.
  - `reorder(video_id: str, scene_ids: list[str])`: Updates `display_order` sequence.

### 2.4 `provider_jobs.py`
- **Purpose**: Persistent task queue enabling decoupled AI assistants and external workers to claim and execute generation jobs.
- **Endpoints**:
  - `POST /api/provider-jobs`: Worker or provider creates a `QUEUED` job.
  - `GET /api/provider-jobs/wait-next`: Long-polling endpoint for workers to claim a job with lease TTL.
  - `POST /api/provider-jobs/{id}/heartbeat`: Extends lease TTL while rendering.
  - `POST /api/provider-jobs/{id}/complete` & `/fail`: Terminal state transition.

---

## 3. Deep Dive: Database Module (`agent/db/`)

### 3.1 `schema.py`
- **Purpose**: Defines SQLite DDL, enables WAL mode, and executes automatic programmatic migrations on startup.
- **Key Functions**:
  - `init_db()`: Connects to SQLite, sets `PRAGMA journal_mode=WAL`, `PRAGMA foreign_keys=ON`, executes table creation scripts, and verifies schema version.
  - `_get_db_init_lock()`: Rebuilds `asyncio.Lock` bound to the active running event loop, preventing cross-test lock contamination in pytest.
  - `get_db()`: Thread-safe lazy connection acquisition with passive WAL checkpointing (`PRAGMA wal_checkpoint(PASSIVE)`).
- **Embedded Migrations**: Handles automated column additions (`provider` on request, `slug` on character, `target_duration_s` on video, `start_url` on provider_job) and table recreation for updated CHECK constraints.

### 3.2 `crud.py`
- **Purpose**: Low-level database transaction handling.
- **Key Queries**:
  - `list_actionable_requests(exclude_ids, limit)`: Selects `PENDING` requests, prioritizing characters (0) over images (1), videos (2), and upscales (3). Respects `next_retry_at` timestamps.

---

## 4. Deep Dive: SDK & Provider Module (`agent/sdk/services/`)

### 4.1 `provider_base.py`
- **Purpose**: Base contracts and data structures.
- **Key Classes**:
  - `ProviderJob`: Generic, provider-agnostic representation of a media generation task.
  - `ProviderCapabilities`: Declares supported operations (`generate_image`, `edit_image`, `i2v`, `r2v`, `upscale`), `max_concurrent`, and `cooldown_s`.
  - `MediaProvider` (ABC): Abstract base class requiring `capabilities`, `is_available()`, `check(job)`, and `run(job)`.

### 4.2 `registry.py` (`ProviderRegistry`)
- **Purpose**: Central catalog of available providers.
- **Built-in Providers**:
  - `FlowProvider`: Proxies to Google Flow via Chrome extension. Available only when extension is connected.
  - `AssistantProvider`: Dispatches tasks to `provider_job` table. Always available without browser dependency.
  - `Muse2APIProvider`: Communicates with `muse2api` HTTP gateway. Available when `MUSE2API_URL` is set.
- **Key Methods**:
  - `resolve(name)`: Resolves provider by name, falling back to `DEFAULT_PROVIDER`.
  - `status()`: Serializes status of all registered backends for `GET /api/providers/status`.

### 4.3 `operations.py` (`OperationService`)
- **Purpose**: Orchestrates domain generation logic before passing to providers.
- **Key Methods**:
  - `generate_scene_image()`: Validates that all character reference images exist; if any reference character lacks a `media_id`, rejects generation with `Waiting for reference images: {names}`.
  - `generate_scene_video()`: Builds I2V, R2V, or First+Last frame video jobs depending on chain type and reference entities.
  - `upscale_scene_video()`: Prepares video upscale job from existing video media ID.

---

## 5. Deep Dive: Worker & Processing Module (`agent/worker/`)

### 5.1 `processor.py` (`WorkerController`)
- **Purpose**: Background loop driving execution.
- **Key Mechanisms**:
  - `APIRateLimiter`: Enforces concurrency limit (`asyncio.Semaphore`) and minimum cooldown delay (`_last_call` timestamp gate).
  - `_cleanup_stale_processing()`: Resets orphan `PROCESSING` requests to `PENDING` upon server boot.
  - `_prerequisites_met(req, orientation)`: Ensures upstream dependencies are satisfied (e.g. video generation deferred until scene image has completed; upscale deferred until video has completed).
  - `_run_loop()`: Continuously queries actionable requests, matches them against provider availability and concurrency capacity, and spawns concurrent tasks (`asyncio.create_task(_run_one(req))`).

---

## 6. Deep Dive: Services Module (`agent/services/`)

### 6.1 `flow_batch.py`
- **Purpose**: Reverse-engineered wire protocol for Google Flow batchexecute.
- **Key RPC Constants**:
  - `ogiZ0b`: Image Generation (`RPC_GEN_IMAGE`)
  - `eb1hJf`: Video Generation I2V (`RPC_GEN_VIDEO`)
  - `nprQif`: Video First+Last Frame Chaining (`RPC_GEN_VIDEO_FIRST_LAST`)
  - `MZZa6b`: Video References / Ingredients (`RPC_GEN_VIDEO_REFERENCES`)
  - `jwpduf`: Operation Status Polling (`RPC_OPERATION`)
  - `SPrCad`: Image Upscale (`RPC_UPSCALE_IMAGE`)
- **Wire Serialization**: Constructs Google `f.req` envelopes and embeds the `__CAPTCHA__` placeholder.

### 6.2 `video_reviewer.py`
- **Purpose**: Multi-frame automated vision QA.
- **Key Logic**:
  - Extracts frames at specified FPS (Light mode: 4 FPS; Deep mode: 8 FPS) via FFmpeg.
  - Stitches frames into contact sheets (3x3 grid) to feed vision models efficiently.
  - Analyzes frames via Claude Vision API or local CLI subprocess (`claude`, `agy`, `codex`).
  - Evaluates 6 weighted dimensions:
    - Character Consistency (25%)
    - Prompt Adherence (20%)
    - Motion Quality (20%)
    - Visual Fidelity (15%)
    - Temporal Coherence (10%)
    - Composition (10%)
  - If score < 7.5, generates an automated prompt mutation fix guide (e.g. adding camera stabilization prompts or adjusting character anchors).

---

## 7. Deep Dive: Chrome Extension (`extension/`)

### 7.1 `hijack_bypass.js`
- **Security & Anti-Tamper Engine**:
  - Injected into the `MAIN` world at `document_start`.
  - Flow's front-end script (`x2a`) deliberately wraps `grecaptcha.enterprise.execute` to inject `action: "extension_hijack_detected"`.
  - `hijack_bypass.js` applies a 3-level property trap on `window.grecaptcha`, `grecaptcha.enterprise`, and `enterprise.execute`.
  - When the genuine reCAPTCHA script assigns `execute`, the trap saves the pristine function into `window.__fk_hijack` and immediately self-cleans its descriptors.
  - This allows `injected.js` to mint valid, unpoisoned tokens.

### 7.2 `background.js`
- **Bridge Core**:
  - Maintains persistent WebSocket connection to `ws://127.0.0.1:9222`.
  - Listens for `batch_rpc` messages.
  - Finds or automatically opens a `flow.google.com` tab.
  - Executes `runBatchRpc` inside the tab's `MAIN` world via `chrome.scripting.executeScript`.
  - Extracts per-page WIZ tokens (`SNlM0e`), solves reCAPTCHA, and dispatches in-page `fetch()`.
