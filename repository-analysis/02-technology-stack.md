# 02. Technology Stack & Dependencies

## 1. Core Languages & Runtimes

| Component | Language / Runtime | Version | Notes |
|---|---|---|---|
| **Backend & Workers** | Python | 3.10 - 3.12 (Active: 3.12.10) | Asyncio-native throughout (FastAPI, aiosqlite, aiohttp) |
| **Chrome Extension** | JavaScript (ES2022) | Chrome Manifest V3 | Service worker, DeclarativeNetRequest, MAIN-world scripts |
| **Web Dashboard** | TypeScript / React | TypeScript 5.5, React 18.3 | Bundled via Vite 5.4 |
| **CLI Skills & Prompts** | Markdown / JSON | - | Integrated into Codex / Antigravity Agent OS |

---

## 2. Backend Dependencies (`requirements.txt` & `requirements-dev.txt`)

### Production Runtime Dependencies
- **`fastapi>=0.104.0`**: Core REST and WebSocket framework.
- **`uvicorn>=0.24.0`**: High-performance ASGI web server.
- **`aiosqlite>=0.19.0`**: Non-blocking asynchronous SQLite wrapper with connection locking.
- **`websockets>=12.0`**: Standalone WebSocket server (`agent/main.py:ws_handler`) for extension communication.
- **`pydantic>=2.5.0`**: Data validation, schema definitions, and serialization.
- **`aiohttp>=3.9.0`**: Asynchronous HTTP client for internal and worker communications.
- **`httpx>=0.25.0`**: Async HTTP client for Suno API and external REST interactions.
- **`anthropic>=0.40.0`**: Official Anthropic SDK for Claude Vision automated video review.
- **`google-api-python-client>=2.100.0` & `google-auth-oauthlib>=1.0.0`**: YouTube Data API v3 integration and OAuth2 channel authentication.
- **`python-multipart>=0.0.9`**: Form data and file upload support for FastAPI.

### Developer & Test Dependencies
- **`pytest>=7.4.0`**: Testing framework.
- **`pytest-asyncio>=0.21.0`**: Async test execution fixture support.
- **`pytest-cov>=4.1.0`**: Test coverage reporting.
- **`black>=23.10.0` & `ruff>=0.1.0`**: Code formatting and linting.
- **`mypy>=1.6.0`**: Static type checking.

---

## 3. Frontend Dashboard Dependencies (`dashboard/package.json`)

- **Framework**: React 18.3.1 (`react`, `react-dom`)
- **Build Tool**: Vite 5.4.2
- **Styling**: Tailwind CSS 3.4.1, `tailwind-merge`, `clsx`, `tailwindcss-animate`
- **UI Component System**: Radix UI Primitives (`@radix-ui/react-accordion`, `dialog`, `dropdown-menu`, `progress`, `scroll-area`, `tabs`, `tooltip`, etc.) structured via shadcn/ui.
- **Icons**: Lucide React (`lucide-react`)
- **Video Playback**: Native HTML5 `<video>` custom-wrapped in `VideoPlayer.tsx`.

---

## 4. External Infrastructure & Third-Party Integrations

1. **Google Flow (`flow.google.com`)**:
   - Proprietary generation backend for Veo 2, Veo 3, Imagen 3, Nano Banana Pro (`GEM_PIX_2`), and Gemini Omni Flash.
   - Accessed via in-page `batchexecute` RPCs with session cookies and Enterprise reCAPTCHA tokens.
2. **OmniVoice TTS (`k2-fsa/OmniVoice`)**:
   - Neural speech synthesis running in an isolated Python subprocess via PyTorch/TorchAudio.
3. **Suno API (`api.sunoapi.org`)**:
   - Background music generation with callback and polling fallbacks.
4. **YouTube Data API v3**:
   - Direct OAuth2 resumable upload and video metadata publishing.
5. **Anthropic Claude 3.5 / Haiku / Local CLI Agents**:
   - Automated video frame inspection and QA scoring.
6. **FFmpeg / FFprobe**:
   - Native system binary utilized via `subprocess` for frame extraction, codec normalization (H.264/AAC), video trimming, and concatenation.
