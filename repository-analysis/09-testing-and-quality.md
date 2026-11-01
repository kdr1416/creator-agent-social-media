# 09. Testing, Verification & Quality Assurance

## 1. Test Architecture Overview

The repository features 27 specialized unit and integration test suites under `tests/unit/`, supported by fixtures in `tests/fixtures/` and global configurations in `tests/conftest.py`.

```text
tests/
├── conftest.py                     # Async fixtures, temporary DB initialization & mocks
├── fixtures/                       # Mock responses for Flow batch and provider jobs
└── unit/                           # 27 unit test suites
    ├── test_assistant_provider.py  # Tests AssistantProvider job queuing & completion
    ├── test_cli_providers.py       # Tests CLI reviewer binary resolution & execution
    ├── test_db_connection.py       # Tests SQLite WAL mode, async connection locks & concurrency
    ├── test_file_url_paths.py      # Tests file:// URL parsing across Windows and POSIX
    ├── test_flow_batch.py          # Tests Google Flow batchexecute envelope generation
    ├── test_flow_batch_golden.py   # Golden tests validating exact wire formats against Google specs
    ├── test_flow_client_batch.py   # Tests WebSocket RPC matching and pending future resolution
    ├── test_flow_global_throttle.py# Tests process-wide rate limiting and cooldown timing
    ├── test_flow_project_session.py# Tests project session pinning and idle rotation
    ├── test_flow_upload_api.py     # Tests image upload wire payloads
    ├── test_models.py              # Tests dynamic model catalog loading and fallback aliases
    ├── test_muse2api_provider.py   # Tests muse.ai gateway provider adapter
    ├── test_muse_review.py         # Tests muse video review handling
    ├── test_omni_flash.py          # Tests Gemini Omni Flash validation (durations, aspect ratios)
    ├── test_operations.py          # Tests OperationService high-level media generation orchestration
    ├── test_parsing.py             # Tests UUID extraction, URL parsing, and error classifiers
    ├── test_processor.py           # Tests WorkerController loop, rate limiting, and prerequisites
    ├── test_provider_aware_projects.py # Tests provider selection inheritance across projects
    ├── test_provider_jobs.py       # Tests provider_job leasing, heartbeats, progress, and terminal states
    ├── test_result_handler.py      # Tests mapping generation responses into database records
    ├── test_review_regenerate.py   # Tests automated prompt repair and scene regeneration loops
    ├── test_setup.py               # Tests installation checks and environment validations
    ├── test_tts_scripts.py         # Tests OmniVoice script templates, tensor reshaping, and tail fade
    ├── test_video_assemble.py      # Tests FFmpeg normalization, trimming, and concatenation
    ├── test_video_model_family.py  # Tests veo vs omni_flash model routing
    ├── test_video_reviewer.py      # Tests 6-dimension weighted scoring and contact sheet assembly
    └── test_youtube.py             # Tests YouTube scheduling logic and metadata rules
```

---

## 2. Key Testing Patterns & Quality Gates

### 2.1 Event Loop & Database Isolation (`conftest.py`)
Because `aiosqlite` connections and `asyncio.Lock` instances are bound to the running event loop, running tests under `pytest-asyncio` requires rebuilding locks per test.
`agent/db/schema.py` uses `_get_db_init_lock()`:
```python
def _get_db_init_lock() -> asyncio.Lock:
    global _db_init_lock, _db_init_loop
    loop = asyncio.get_running_loop()
    if _db_init_lock is None or _db_init_loop is not loop:
        _db_init_lock = asyncio.Lock()
        _db_init_loop = loop
    return _db_init_lock
```
This pattern eliminates the notorious `"database table is locked"` race condition during concurrent test execution.

### 2.2 Wire Protocol Golden Tests (`test_flow_batch_golden.py`)
Google's `batchexecute` wire protocol is verified against recorded golden payloads to ensure that RPC IDs (`ogiZ0b`, `eb1hJf`, `nprQif`), aspect ratios, and model IDs match Google Flow's expected wire formats exactly.

### 2.3 Automated Video Review Quality Gate (`test_review_regenerate.py`)
Automated tests verify that when a scene video scores < 7.5:
1. Critical errors (e.g. character morphing, extra limbs, reversed motion) trigger prompt mutations.
2. The scene's `video_prompt` is patched with targeted stabilization instructions.
3. A `REGENERATE_VIDEO` request is queued.
4. Downstream upscale videos and child continuation scenes are safely cascaded for re-evaluation.

---

## 3. Running the Test Suite

To run tests in an environment with development dependencies installed:
```bash
# Install developer dependencies
pip install -r requirements-dev.txt

# Run all unit tests
pytest tests/unit/

# Run with coverage report
pytest --cov=agent tests/unit/

# Run single test module
pytest tests/unit/test_parsing.py -v
```
