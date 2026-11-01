# 10. Design Decisions, Architectural Evolution & History

## 1. Environment & Versioning Context
- **Snapshot State**: The local workspace is an un-versioned source snapshot (no `.git` directory present).
- **Forensic Evidence Sources**: Architectural evolution was reconstructed via:
  1. Internal migration logs and code comments in `agent/services/flow_batch.py`, `agent/db/schema.py`, and `extension/background.js`.
  2. Setup files (`setup.py`, `.fk-setup.json`, `setup.sh`).
  3. Deprecated routes and legacy compatibility aliases documented in `ARCHITECTURE.md` and `PLAN.md`.

---

## 2. Major Architectural Evolutions & Pivots

### Evolution 1: The September 2026 Google Flow Migration (REST -> batchexecute)
- **Previous State**: Google Flow operated under `labs.google/fx/tools/flow` using REST endpoints on `aisandbox-pa.googleapis.com` authenticated with a bearer token (`Bearer ya29...`).
- **Trigger**: In September 2026, Google redesigned Flow onto `flow.google.com`, discontinued minting OAuth bearer tokens in the UI, and migrated all RPCs to Google's internal `batchexecute` wire protocol.
- **Architectural Response**:
  - Deprecated all REST proxy code in the extension.
  - Implemented `agent/services/flow_batch.py` to serialize Google `f.req` envelopes.
  - Moved execution directly into the browser tab's `MAIN` world via `chrome.scripting.executeScript`, utilizing Google session cookies and extracting per-page CSRF tokens (`WIZ_global_data.SNlM0e`).

### Evolution 2: The Anti-Hijack reCAPTCHA Arms Race (`hijack_bypass.js`)
- **Trigger**: Google deployed frontend script `boq_labs-ai-sandbox-frontend_20260922.00_p0` containing function `x2a`. Function `x2a` monkeypatched `grecaptcha.enterprise.execute` to inject `action: "extension_hijack_detected"`, causing all backend generations to fail with `PUBLIC_ERROR_UNUSUAL_ACTIVITY`.
- **Architectural Response**:
  - Developed `extension/hijack_bypass.js`, executing at `document_start` before any page scripts run.
  - Applied a 3-level property trap on `window.grecaptcha`, `grecaptcha.enterprise`, and `enterprise.execute`.
  - When the genuine reCAPTCHA script assigns `execute`, the trap preserves the pristine function in `window.__fk_hijack` and immediately self-cleans its property descriptors.
  - This restored automated token minting without triggering Google's anti-bot heuristic.

### Evolution 3: Monolithic Flow Coupling -> Pluggable Provider SPI
- **Previous State**: The backend initially coupled generation directly to Google Flow via the Chrome extension. If the user had no Chrome or no Google account, the entire toolchain was unusable.
- **Trigger**: Need to support alternative models (OpenAI-compatible gateways, muse.ai, and external AI agents).
- **Architectural Response**:
  - Introduced the `MediaProvider` interface and `ProviderRegistry` (`agent/sdk/services/`).
  - Added the `provider_job` persistent SQLite table and `/api/provider-jobs` long-polling API, allowing independent external workers (`assistant_worker.py`) to process tasks without touching the Chrome extension.
  - Added `Muse2APIProvider` for HTTP-based rendering.
  - Updated the request queue with per-provider rate limiting (`FLOW_MAX_CONCURRENT=5, cooldown=10s` vs `ASSISTANT_MAX_CONCURRENT=2, cooldown=0s`).

### Evolution 4: Dual-Transport Resiliency (WebSocket + HTTP Callback)
- **Trigger**: Generating high-resolution videos or upscales often takes 60 to 180 seconds. Chrome service workers or browser tabs occasionally discard or reset WebSocket connections during long waits, causing lost generation receipts.
- **Architectural Response**:
  - Added an HTTP callback route: `POST /api/ext/callback`.
  - On WebSocket connection, the agent issues a single-session bearer token (`_CALLBACK_SECRET`).
  - When an RPC finishes in the browser, the extension posts the result directly to `POST /api/ext/callback` with header `X-Callback-Secret`.
  - This guarantees atomic delivery even if the WebSocket connection drops during rendering.
