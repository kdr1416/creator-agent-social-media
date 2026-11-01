# 11. Customization & Extension Strategy

## 1. Customization Classification Map

| Zone | Risk Level | Modules / Components | Reason & Coupling |
|---|---|---|---|
| **Safe Zones** | Low | `agent/materials.py`, `agent/models.json`, `agent/providers.json`, `skills/` | Purely declarative configuration or user-facing skills. Zero impact on core logic. |
| **Extension Zones** | Low / Medium | `agent/sdk/services/provider_base.py`, `agent/sdk/services/registry.py` | Official Service Provider Interface (SPI). Adding providers requires subclassing without editing existing adapters. |
| **Moderate Zones** | Medium | `agent/services/video_reviewer.py`, `agent/services/tts.py`, `agent/api/` | Adding review dimensions, audio post-processing, or auxiliary REST endpoints. |
| **High-Risk Zones** | High | `agent/worker/processor.py`, `agent/db/schema.py`, `agent/db/crud.py` | Concurrency controls, database transaction integrity, state machines, and request dispatch loop. |
| **Critical Zones** | Extremely High | `agent/services/flow_batch.py`, `extension/hijack_bypass.js`, `extension/background.js` | Reverse-engineered Google internal wire protocols and anti-bot defense bypasses. Modifying without exact packet traces causes account bans or generation failures. |

---

## 2. Step-by-Step Recipes for Common Customizations

### Recipe A: Adding a New Media Generation Provider (e.g. ComfyUI / Sora / Runway)
**Goal**: Integrate a new backend without modifying the Google Flow bridge or SQLite schema.

1. **Step 1: Create Provider Adapter**
   - File: `agent/sdk/services/custom_provider.py`
   - Implement `MediaProvider`:
   ```python
   from agent.sdk.services.provider_base import MediaProvider, ProviderCapabilities, ProviderJob

   class CustomComfyProvider(MediaProvider):
       name = "comfyui"
       display_name = "Local ComfyUI Worker"

       @property
       def capabilities(self) -> ProviderCapabilities:
           return ProviderCapabilities(
               generate_image=True,
               edit_image=False,
               i2v=True,
               r2v=False,
               upscale=False,
               max_concurrent=1,
               cooldown_s=2.0,
           )

       def is_available(self) -> bool:
           # Check if ComfyUI HTTP server is reachable
           return True

       def check(self, job: ProviderJob) -> str | None:
           # Return error string if job unsupported
           return None

       async def run(self, job: ProviderJob) -> dict:
           # Execute ComfyUI generation, save file to output/
           return {"output_url": "file:///path/to/media.mp4", "media_id": "<uuid>"}
   ```

2. **Step 2: Register in `ProviderRegistry`**
   - File: `agent/sdk/services/registry.py`
   - In `__init__`:
   ```python
   from agent.sdk.services.custom_provider import CustomComfyProvider
   providers["comfyui"] = CustomComfyProvider()
   ```

3. **Step 3: Enable in Configuration**
   - File: `agent/config.py`
   - Set `DEFAULT_PROVIDER = "comfyui"` or pass `"provider": "comfyui"` in `RequestCreate`.

---

### Recipe B: Adding a New Visual Material / Style Preset
**Goal**: Add a custom artistic style (e.g. `cyberpunk_neon`, `claymation`).

1. **Via REST API (Persistent in DB)**:
   - Call `POST /api/materials`:
   ```json
   {
     "id": "cyberpunk_neon",
     "name": "Cyberpunk Neon",
     "style_instruction": "Cyberpunk aesthetic, neon rim lighting, holographic reflections, volumetric smoke, high contrast, cinematic octane render.",
     "negative_prompt": "cartoon, low resolution, daylight, washed out",
     "scene_prefix": "In a neon-drenched futuristic megacity",
     "lighting": "High contrast cyan and magenta neon rim lighting"
   }
   ```
2. **Via Code Registry (Built-in)**:
   - File: `agent/materials.py`
   - Add entry to `BUILTIN_MATERIALS` dictionary.
   - Automatically loaded into DB during `lifespan` in `agent/main.py`.

---

### Recipe C: Updating AI Video or Image Model Keys
**Goal**: Point Flow Kit to a newly released Google model (e.g. Veo 3.5 or Nano Banana Ultra) without code changes.

1. **Edit `agent/models.json`**:
   - Add new model key:
   ```json
   "video_models": {
     "VEO_3_5": "veo_3_5_wire_id_from_google"
   },
   "image_models": {
     "NANO_BANANA_ULTRA": "GEM_PIX_3"
   }
   ```
2. **Hot Reload**:
   - `models.json` is loaded directly into `agent/config.py`. Restarting the agent makes the model immediately accessible across all requests.

---

### Recipe D: Adding an External TTS Engine (e.g. ElevenLabs)
**Goal**: Swap or complement OmniVoice with ElevenLabs speech synthesis.

1. **Step 1: Create Engine Adapter**
   - File: `agent/services/elevenlabs_tts.py`
   ```python
   import httpx

   async def generate_elevenlabs_tts(text: str, voice_id: str, output_path: str, api_key: str):
       url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
       headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
       async with httpx.AsyncClient() as client:
           resp = await client.post(url, json={"text": text}, headers=headers)
           with open(output_path, "wb") as f:
               f.write(resp.content)
   ```
2. **Step 2: Mount in `agent/api/tts.py`**:
   - Add query parameter `engine: str = "omnivoice"` and route to `generate_elevenlabs_tts` when selected.
3. **Step 3: Update `agent/services/post_process.py`**:
   - Existing trimming and normalization functions remain completely unchanged.

---

## 3. Recommended Customization Architecture
1. **Never alter `agent/worker/processor.py` for backend-specific logic**. All generation backends must conform to `MediaProvider`.
2. **Never hardcode credentials or secrets**. All API keys must be loaded via `agent/config.py` using `os.environ.get(...)`.
3. **Preserve Subprocess Isolation**: Long-running CPU/GPU-bound tasks (TTS, video transcoding) must run in isolated subprocesses to avoid blocking FastAPI's async event loop.
