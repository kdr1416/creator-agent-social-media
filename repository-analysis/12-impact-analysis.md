# 12. Impact Analysis & Dependency Matrix

## 1. Upstream & Downstream Dependency Matrix

| Modified Component | Directly Affected Downstream Modules | Potential Risk / Breaking Impact | Verification Check |
|---|---|---|---|
| **`agent/db/schema.py`** | `crud.py`, `models/`, `api/`, `processor.py` | Schema mismatch, `sqlite3.OperationalError: no such column`, migration failure. | Run SQLite WAL check, inspect `flow_agent.db` table info, run `test_db_connection.py`. |
| **`agent/worker/processor.py`** | All generation workflows, dashboard stats, queue dispatch | Pipeline stall, race condition, thread starvation, rate-limit bans from Google. | Verify queue drain, test deferral timers with `test_processor.py`. |
| **`agent/sdk/services/provider_base.py`** | `FlowProvider`, `AssistantProvider`, `Muse2APIProvider`, `OperationService` | `TypeError: abstract method not implemented`, parameter mismatch. | Run `test_operations.py`, `test_assistant_provider.py`. |
| **`agent/services/flow_batch.py`** | `FlowProvider`, `FlowClient`, `extension/background.js` | Malformed Google `f.req` envelopes, `400 Bad Request`, `PUBLIC_ERROR_UNUSUAL_ACTIVITY`. | Run `test_flow_batch_golden.py` against recorded wire traces. |
| **`extension/hijack_bypass.js`** | Extension token generation, all Flow requests | Poisoned reCAPTCHA tokens (`extension_hijack_detected`), instant generation rejections. | Test reCAPTCHA minting via `GET /api/ext/test-captcha`. |
| **`agent/services/post_process.py`** | `videos.py:concat_video()`, video assembly | FFmpeg exit code 1, unplayable MP4 outputs, out-of-sync audio. | Run `test_video_assemble.py`. |
| **`agent/services/video_reviewer.py`** | `api/reviews.py`, auto-regenerate loops | False negative prompt repairs, infinite regeneration loops. | Run `test_review_regenerate.py` with mock review responses. |

---

## 2. Breaking Change Scenarios & Preventative Safeguards

### Scenario 1: Changing Column Types or Adding Constraints in SQLite
- **Issue**: SQLite does not support `ALTER TABLE ... ALTER COLUMN` or modifying existing `CHECK` constraints.
- **Safeguard**: Follow the migration pattern established in `agent/db/schema.py#L255-L297`:
  1. Rename current table to `_table_old`.
  2. Create new table with updated constraints and columns.
  3. Copy data: `INSERT OR IGNORE INTO table SELECT ... FROM _table_old`.
  4. Drop `_table_old`.
  5. Run inside an explicit migration block guarded by table introspection.

### Scenario 2: Google Flow Wire ID Updates
- **Issue**: Google rolls out a new video duration wire format or deprecates an RPC ID.
- **Safeguard**:
  - Model keys are stored in `agent/models.json` outside Python code.
  - Image models use dynamic resolution (`resolve_image_model`) accepting valid wire IDs directly, allowing hot-patching without requiring a Flow Kit release.

### Scenario 3: Modifying Concurrency Limits
- **Issue**: Increasing `FLOW_GENERATION_MAX_CONCURRENT` above 5 or dropping `FLOW_COOLDOWN_S` below 10s causes Google's bot detection to flag the user's IP.
- **Safeguard**: Provider capabilities enforce hard ceiling caps in `APIRateLimiter` to protect user Google accounts.

---

## 3. Regression Verification Checklist

Before deploying modifications to a production Flow Kit instance:
1. [ ] **Database Connection Health**: Verify `init_db()` completes without foreign key violations.
2. [ ] **Extension Handshake**: Confirm extension connects to `ws://127.0.0.1:9222` and receives `callback_secret`.
3. [ ] **reCAPTCHA Token Integrity**: Execute `GET /api/ext/test-captcha` and confirm token does not contain `extension_hijack_detected`.
4. [ ] **Single Scene Image Generation**: Submit a test image generation; verify media ID is formatted as a valid UUID.
5. [ ] **Scene Chaining**: Test continuation scene creation; verify `vertical_end_scene_media_id` is passed correctly to the downstream scene.
6. [ ] **Audio Pipeline**: Verify OmniVoice generates WAV with trailing silence padding and 30fps H.264 video trims to exact audio duration.
