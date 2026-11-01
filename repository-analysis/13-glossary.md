# 13. System Glossary & Domain Terminology

## 1. Domain Concepts & Internal Terminology

| Term | Definition / Role in Flow Kit |
|---|---|
| **Google Flow** | Google's web application (`flow.google.com`) for creative AI media generation, hosting models like Veo 2/3, Imagen 3, Nano Banana Pro, and Gemini Omni Flash. |
| **batchexecute** | Google's proprietary internal wire protocol for executing batched RPC calls using URL-encoded POST forms with `f.req` envelopes and `)]}'` chunked responses. |
| **WIZ_global_data** | In-page JavaScript global object on Google properties carrying session metadata, notably `SNlM0e` (`at` CSRF token), `FdrFJe` (session ID), and `cfb2h` (build label). |
| **`hijack_bypass.js`** | Injected MAIN-world script that neutralizes Google Flow's anti-extension monkeypatch `x2a` to prevent `extension_hijack_detected` reCAPTCHA poisoning. |
| **MediaProvider** | Abstract base class in `agent/sdk/services/provider_base.py` providing a common interface for generation backends (`flow`, `assistant`, `muse2api`). |
| **ProviderJob** | Backend-agnostic data structure encapsulating a generation task (image, edit, I2V, R2V, upscale). |
| **`provider_job` Table** | Persistent SQLite queue table implementing a leasing protocol (`lease_expires_at`) for external workers and AI assistants. |
| **Scene Chaining** | Technique ensuring visual and motion continuity across video cuts by passing the parent scene's video media ID as the start frame of the continuation scene. |
| **Contact Sheet** | 3x3 stitched grid of extracted video frames sent to vision models (Claude 3.5 Sonnet / Haiku) for cost-effective video QA analysis. |
| **Video Reviewer** | Automated engine scoring video clips across 6 weighted dimensions (character consistency, prompt adherence, motion quality, visual fidelity, temporal coherence, composition). |
| **Material** | Visual style preset (e.g. `3d_pixar`, `realistic`, `anime`) defining style instructions, lighting, and negative prompts injected into character and scene prompts. |
| **Character Bible** | Structured reference entity collection (characters, locations, visual assets, creatures, factions) holding reference image prompts and Google Flow media IDs. |
| **OmniVoice** | Neural TTS model (`k2-fsa/OmniVoice`) executed in a dedicated subprocess to synthesize narrator audio with trailing silence padding. |
| **Suno AI** | Third-party generative music service (`api.sunoapi.org`) used to compose contextual background soundscapes. |
| **WAL Mode** | SQLite Write-Ahead Logging mode (`PRAGMA journal_mode=WAL`), allowing non-blocking concurrent reads while writes are committed. |

---

## 2. Key RPC Identifiers (Google Flow Wire Protocol)

| RPC ID | Meaning / Functionality | Module Reference |
|---|---|---|
| `ogiZ0b` | `RPC_GEN_IMAGE`: Image generation | `agent/services/flow_batch.py` |
| `eb1hJf` | `RPC_GEN_VIDEO`: Image-to-video (I2V) generation | `agent/services/flow_batch.py` |
| `YhhmEf` | `RPC_GEN_VIDEO_TEXT`: Text-to-video (T2V) generation | `agent/services/flow_batch.py` |
| `nprQif` | `RPC_GEN_VIDEO_FIRST_LAST`: Video chaining from start and end frames | `agent/services/flow_batch.py` |
| `MZZa6b` | `RPC_GEN_VIDEO_REFERENCES`: Video generation with reference entities | `agent/services/flow_batch.py` |
| `jwpduf` | `RPC_OPERATION`: Polling operation completion status | `agent/services/flow_batch.py` |
| `Zzl0ze` | `RPC_PROJECT_MEDIA`: Listing project media items | `agent/services/flow_batch.py` |
| `as29s` | `RPC_MEDIA`: Fetching signed media download URLs | `agent/services/flow_batch.py` |
| `maseQ` | `RPC_UPLOAD_IMAGE`: Direct image upload | `agent/services/flow_batch.py` |
| `SPrCad` | `RPC_UPSCALE_IMAGE`: Image upscaling | `agent/services/flow_batch.py` |
| `jHPbke` | `RPC_CREATE_PROJECT`: Pinned project creation | `agent/services/flow_batch.py` |
