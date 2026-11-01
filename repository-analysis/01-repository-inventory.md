# 01. Repository Discovery & Inventory

## 1. Physical Directory Tree Overview

```text
flowkit-main/
│
├── agent/                         # Core Python backend application
│   ├── api/                       # FastAPI route controllers (14 routers)
│   │   ├── active_project.py      # Active project state pointer for CLI/agents
│   │   ├── characters.py          # Character/entity bible management
│   │   ├── flow.py                # Direct Flow generation endpoints
│   │   ├── materials.py           # Visual material/style preset management
│   │   ├── models.py              # Available AI model key lookup & configuration
│   │   ├── music.py               # Suno music generation & callbacks
│   │   ├── project_characters.py  # Entity-to-project mappings
│   │   ├── projects.py            # Project CRUD, prompt builder & directory setup
│   │   ├── provider_jobs.py       # Async job queue for external assistant workers
│   │   ├── providers.py           # Provider health, status & concurrency limits
│   │   ├── requests.py            # Core async request submission & batch status
│   │   ├── reviews.py             # Video review submission & auto-regen triggers
│   │   ├── scenes.py              # Scene CRUD, reordering & continuation chaining
│   │   ├── tts.py                 # OmniVoice voice template & TTS synthesis
│   │   └── videos.py              # Video CRUD, trimming, concatenation & publish
│   │
│   ├── db/                        # Asynchronous database layer
│   │   ├── crud.py                # CRUD queries, transactions & batch helpers
│   │   └── schema.py              # SQLite schema DDL, WAL initialization & auto-migrations
│   │
│   ├── models/                    # Pydantic data schemas & domain contracts
│   │   ├── character.py           # Character/Entity definitions
│   │   ├── enums.py               # Status types, entity types, orientations
│   │   ├── material.py            # Style preset definitions
│   │   ├── project.py             # Project DTOs
│   │   ├── request.py             # Generation request DTOs
│   │   ├── review.py              # VideoReview & dimension scoring schemas
│   │   ├── scene.py               # Scene DTOs & status tracking
│   │   ├── tts.py                 # TTS request schemas
│   │   └── video.py               # Video DTOs
│   │
│   ├── sdk/                       # Abstract Architecture & Provider SPI Layer
│   │   ├── persistence/           # Storage abstraction (Repository interface & SQLiteRepository)
│   │   └── services/              # Provider Service Provider Interface (SPI)
│   │       ├── assistant_provider.py # Provider implementation for external AI assistants
│   │       ├── flow_provider.py      # Provider implementation for Google Flow
│   │       ├── muse2api_provider.py  # Provider implementation for muse.ai gateway
│   │       ├── operations.py         # OperationService: High-level media generation orchestration
│   │       ├── provider_base.py      # Abstract MediaProvider base class & ProviderJob
│   │       ├── registry.py           # ProviderRegistry managing provider lifecycle & resolution
│   │       └── result_handler.py     # Parsing provider responses into domain models
│   │
│   ├── services/                  # Auxiliary Domain & Integration Services
│   │   ├── cli_providers.py       # Invocation wrapper for CLI vision agents (claude, agy, codex)
│   │   ├── event_bus.py           # Async pub/sub event bus for dashboard updates
│   │   ├── flow_batch.py          # Reverse-engineered Google Flow batchexecute wire protocol
│   │   ├── flow_client.py         # WebSocket bridge manager connecting FastAPI to Chrome Extension
│   │   ├── flow_project_session.py# Flow project session pinning & rotation
│   │   ├── muse2api_client.py     # HTTP client for muse2api OpenAI-compatible gateway
│   │   ├── omni_flash.py          # Gemini Omni Flash video generation via Google Flow
│   │   ├── post_process.py        # FFmpeg video normalization, trimming, and concatenation
│   │   ├── scene_chain.py         # Continuation scene creation & mediaId inheritance
│   │   ├── suno.py                # Suno API client for AI background music generation
│   │   ├── tts.py                 # Subprocess-isolated OmniVoice TTS synthesis engine
│   │   └── video_reviewer.py      # Multi-dimensional automated video QA engine
│   │
│   ├── utils/                     # Shared Utility Functions
│   │   ├── paths.py               # Path normalization & URL-to-path resolution
│   │   └── slugify.py             # Unicode slug generation for characters & entities
│   │
│   ├── worker/                    # Background Processing & Job Execution
│   │   ├── _parsing.py            # UUID/Media ID validation & JSON response extraction
│   │   ├── assistant_worker.py    # Reference CLI worker for long-poll assistant job execution
│   │   └── processor.py           # Background request queue processor & APIRateLimiter
│   │
│   ├── config.py                  # Global application configuration & env variable defaults
│   ├── main.py                    # FastAPI application setup, WebSocket server & lifespan
│   ├── materials.py               # In-memory style instruction presets
│   ├── models.json                # Dynamic AI model keys (Veo 2, Veo 3, Imagen 3, Nano Banana)
│   └── providers.json             # Dynamic vision review CLI provider configuration
│
├── dashboard/                     # React 18 Frontend Dashboard (Vite + Tailwind + shadcn/ui)
│   ├── public/                    # Static assets (favicons, SVG sprite icons)
│   ├── src/                       # Source code
│   │   ├── api/                   # API client & WebSocket subscription context
│   │   ├── components/            # UI components (gallery, pipeline, scene card, logs, ui primitives)
│   │   ├── i18n/                  # Multi-language translations (English & Vietnamese)
│   │   ├── pages/                 # Route pages (Dashboard, Projects, Gallery, Logs, Settings)
│   │   ├── App.tsx                # App root & navigation router
│   │   └── main.tsx               # React DOM entry point
│   ├── package.json               # Frontend dependencies
│   └── vite.config.ts             # Vite bundler configuration
│
├── extension/                     # Chrome Extension Bridge (Manifest V3)
│   ├── background.js              # Service worker: WS client to Python agent, RPC dispatcher
│   ├── content.js                 # Content script: Token capture trigger & tab messaging
│   ├── hijack_bypass.js           # MAIN-world trap intercepting reCAPTCHA enterprise execute
│   ├── injected.js                # MAIN-world script executing in-page fetches
│   ├── manifest.json              # MV3 configuration & permissions
│   ├── popup.html / popup.js      # Extension browser action status popup
│   ├── rules.json                 # DeclarativeNetRequest rules for headers/referers
│   └── side_panel.html / .js      # Integrated side-panel dashboard
│
├── youtube/                       # YouTube Automated Publishing Integration
│   ├── auth.py                    # OAuth2 token authentication & token storage per channel
│   └── upload.py                  # Video upload, metadata injection & scheduling rules
│
├── tools/                         # Operational & Review Utilities
│   ├── review_board.html          # Lightweight visual review board UI
│   └── review_server.py           # HTTP server (port 8200) serving video review board
│
├── skills/ & .agents/skills/      # Antigravity/Codex AI Agent Reusable Skills
│   ├── fk-create-project.md       # Project creation workflow
│   ├── fk-gen-images.md           # Scene image generation batch workflow
│   ├── fk-gen-videos.md           # Scene video generation batch workflow
│   ├── fk-review-video.md         # Video review & scoring workflow
│   ├── fk-concat.md               # Video concatenation & final render workflow
│   └── ... (40+ specialized production skills)
│
├── tests/                         # Test Suite
│   ├── fixtures/                  # Mock data for batch RPCs and provider jobs
│   ├── unit/                      # 27 comprehensive unit test modules
│   └── conftest.py                # Pytest async fixtures & event loop configuration
│
├── scripts/                       # Operational automation scripts (storyboards, voice, sync)
├── output/                        # Default output directory for generated video/audio artifacts
├── requirements.txt               # Production Python dependencies
├── requirements-dev.txt           # Developer & test dependencies (pytest, etc.)
└── setup.py                       # Project installer & CLI tool configuration
```

---

## 2. Inventory of Primary Modules & Their Core Responsibilities

| Module / Component | Physical Path | Primary Responsibility |
|---|---|---|
| **FastAPI Core & Lifespan** | `agent/main.py` | Initializes SQLite DB, runs WebSocket server (`ws://127.0.0.1:9222`), boots background worker loop, mounts 14 API routers, handles extension callbacks. |
| **Configuration Central** | `agent/config.py` | Defines host/ports, media providers, worker timeouts, model catalogs, rate limits, audio paths, and credentials. |
| **Request Dispatcher & Queue** | `agent/worker/processor.py` | Background loop that pulls `PENDING` generation requests, checks prerequisites, enforces per-provider rate limits (`APIRateLimiter`), delegates to `OperationService`, and records outcomes. |
| **Provider SPI & Registry** | `agent/sdk/services/` | Decouples high-level generation requests from concrete backend execution. Houses `MediaProvider` base class and concrete adapters (`FlowProvider`, `AssistantProvider`, `Muse2APIProvider`). |
| **Flow batchexecute Wire Protocol** | `agent/services/flow_batch.py` | Builds exact Google internal RPC envelopes (`f.req`) for image generation (`ogiZ0b`), video generation (`eb1hJf`, `nprQif`), upscaling (`SPrCad`), and parses chunked `)]}'` responses. |
| **Extension WebSocket Client** | `extension/background.js` | Persistent background worker maintaining WebSocket connection to `agent/main.py`, receiving `batch_rpc` commands, and orchestrating tab execution. |
| **Anti-Tamper reCAPTCHA Trap** | `extension/hijack_bypass.js` | Runs at `document_start` in the MAIN world to intercept pristine `grecaptcha.enterprise.execute` before Google Flow's anti-extension `x2a` tamper script can poison it. |
| **Automated Video QA Engine** | `agent/services/video_reviewer.py` | Extracts video frames, compiles contact sheets, analyzes them via Claude 3.5 Sonnet / Haiku or local CLI tools across 6 weighted criteria, and returns actionable prompt repair directives. |
| **Audio & Post-Production** | `agent/services/post_process.py`, `tts.py`, `suno.py` | Subprocess-isolated OmniVoice speech synthesis with tail padding, Suno music generation, and FFmpeg clip normalization and concat demuxing. |
| **YouTube Publishing Pipeline** | `youtube/upload.py`, `auth.py` | Channel OAuth2 credential caching, video metadata formatting, and scheduled publishing for Shorts and long-form videos. |
| **Realtime Monitoring Dashboard** | `dashboard/` | Full React 18 single-page app displaying live generation pipeline stages, scene thumbnails, review boards, and system logs. |

---

## 3. Entry Points Summary

1. **Backend Server Entry Point**:
   - `python -m agent.main` (or via `setup.py` entrypoint / uvicorn):
   - Starts HTTP server on `http://127.0.0.1:8100` and WebSocket bridge on `ws://127.0.0.1:9222`.
2. **Chrome Extension Entry Point**:
   - `extension/manifest.json`: Background service worker `background.js` initializes on browser boot, connects to `ws://127.0.0.1:9222`.
3. **Web Dashboard Entry Point**:
   - `dashboard/index.html` -> `dashboard/src/main.tsx`: React app running via Vite dev server (`npm run dev`) or served statically.
4. **Standalone Assistant Worker Entry Point**:
   - `python -m agent.worker.assistant_worker`: Consumer process polling `/api/provider-jobs/wait-next` to handle tasks delegated to AI assistants.
5. **Review Board Entry Point**:
   - `python tools/review_server.py [port]`: Standalone review server on port 8200.
