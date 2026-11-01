# BÁO CÁO SÀNG LỌC NGHIÊM NGẶT & TINH GỌN CÔNG NGHỆ (FLOW KIT V2)

- **Giai đoạn:** Phase 9 — Strict Repository Shortlisting & Technology Minimization
- **Nguyên tắc chỉ đạo:** "Existing Capability First — New Dependency Only When Necessary"
- **Mục tiêu:** Tìm ra tổ hợp công nghệ nhỏ nhất, loại bỏ phức tạp thừa, nâng cấp thực chất chất lượng visual và animation 2D.

---

## 1. PHÂN LOẠI 5 NHÓM THEO HIỆN TRẠNG & NHU CẦU THỰC TẾ

```
[A. EXISTING CORE] ──────────► GSAP, FFmpeg, HyperFrames (Đang chạy ổn định trong production)
[B. ALREADY IN REPO] ────────► Remotion (Có sẵn tại remotion-project/, kích hoạt theo capability)
[C. NEW INTEGRATION (SKILLS)]► gsap-skills, remotion-skills (0kb runtime, chống AI hallucination)
[D. CONDITIONAL EXPERIMENTS] ─► SVGO, Satori, dotLottie (Thử nghiệm khi có yêu cầu cụ thể)
[E. EXCLUDED FOR NOW] ───────► 10 Repositories bị loại bỏ hoàn toàn (Trùng lặp, dư thừa, nặng nề)
```

---

## 2. BẢNG SÀNG LỌC CUỐI CÙNG CHO TẤT CẢ 18 REPOSITORIES

| # | Repository | Already Available? | Unique Capability | Real Need | Duplication | Bằng chứng thực tế | Final Decision | Lý do kỹ thuật |
|---|---|---|---|---|---|---|---|---|
| 1 | `greensock/GSAP` | **CÓ** (Lõi) | Timeline chính xác tuyệt đối, seek-safe | Cực cao | Không | Đang chạy toàn bộ `VIDEO-33` | **KEEP EXISTING** | Trụ cột điều khiển animation hiện tại. |
| 2 | `FFmpeg/FFmpeg` | **CÓ** (Lõi) | Ghép frame bit-exact, master PCM audio sync | Bắt buộc | Không | Đảm bảo AV-sync 0.9999 correlation | **KEEP EXISTING** | Chuẩn công nghiệp duy nhất cho final assembly. |
| 3 | `remotion-dev/remotion` | **CÓ** (`remotion-project/`) | Spring physics cơ học, component hóa React | Cao | Bổ trợ HF | Đã có `Scene2.tsx` chạy thử nghiệm | **KEEP EXISTING** | Giữ làm engine tùy chọn cho physics/UI, không xóa. |
| 4 | `greensock/gsap-skills` | **CHƯA** | Dạy AI cú pháp GSAP 3 chuẩn, timeline context | Rất cao | Không | Ngăn chặn lỗi nhầm syntax GSAP 2 cũ | **INTEGRATE NOW** | 0kb runtime, chỉ là file markdown hướng dẫn Agent. |
| 5 | `remotion-dev/skills` | **CHƯA** | Dạy AI pattern render-safe, `useCurrentFrame` | Cao | Không | Ngăn chặn lỗi vi phạm React rules trong render | **INTEGRATE NOW** | 0kb runtime, tài liệu chuẩn hóa cho Codex/Antigravity. |
| 6 | `svg/svgo` | **CHƯA** | Dọn dẹp metadata, giữ semantic ID cho SVG | Cao | Không | SVGs từ AI/Figma thường chứa ID rác gây lỗi DOM | **INTEGRATE NOW** | Công cụ build-step chạy qua CLI (`npx svgo`), không làm nặng app. |
| 7 | `vercel/satori` | **CHƯA** | Chuyển JSX Flexbox layout thành vector SVG | Trung bình | Bổ trợ SVG | Tạo layout bảng biểu, card, typography không cần vẽ XML | **CONDITIONAL EXPERIMENT** | Chỉ dùng khi kịch bản có layout text/thống kê phức tạp. |
| 8 | `LottieFiles/dotlottie-web` | **CHƯA** | Runtime WebAssembly chạy file vector Lottie | Cao (Character) | Không | Giải quyết cử động nhân vật phức tạp (đi bộ, biểu cảm) | **CONDITIONAL EXPERIMENT** | Chỉ kích hoạt khi project có nguồn asset Lottie chất lượng. |
| 9 | `juliangarnier/anime` | **CHƯA** | SVG path morphing & line drawing | Thấp | **Trùng GSAP** | GSAP + SVG path đã xử lý được 90% animation | **EXCLUDE FOR NOW** | Không đưa thêm 1 animation runtime thứ hai vào cùng 1 trang. |
| 10 | `motiondivision/motion` | **CHƯA** | WAAPI gestures & spring | Thấp | **Trùng Remotion** | WAAPI không seek được frame-exact trên headless server | **EXCLUDE FOR NOW** | Không phù hợp với programmatic video rendering. |
| 11 | `motion-canvas/motion-canvas` | **CHƯA** | Generator-based procedural canvas video | Thấp | **Trùng HF/Remotion** | Đã có HyperFrames và Remotion | **EXCLUDE FOR NOW** | Thêm engine thứ 3 sẽ gây hỗn loạn kiến trúc. |
| 12 | `mrdoob/three.js` | **CHƯA** | WebGL 3D rendering | Rất thấp | Không | 2D explainer không cần 3D scene graph nặng nề | **EXCLUDE FOR NOW** | Gánh nặng memory, headless render rất chậm. |
| 13 | `pmndrs/react-three-fiber` | **CHƯA** | React wrapper cho Three.js | Rất thấp | Phụ thuộc 3D | Cần Three.js mới chạy được | **EXCLUDE FOR NOW** | Loại bỏ theo Three.js. |
| 14 | `pmndrs/drei` | **CHƯA** | Component helpers cho R3F | Rất thấp | Phụ thuộc 3D | Cần R3F mới chạy được | **EXCLUDE FOR NOW** | Loại bỏ theo Three.js. |
| 15 | `dimforge/rapier` | **CHƯA** | 2D/3D physics simulation WASM | Rất thấp | **Trùng Remotion spring** | GSAP easing & Remotion spring giải quyết đủ độ nảy | **EXCLUDE FOR NOW** | Quá phức tạp và dư thừa cho video giải thích 2D. |
| 16 | `pmndrs/postprocessing` | **CHƯA** | WebGL post-processing shaders | Rất thấp | Phụ thuộc 3D | Cần Three.js canvas mới chạy được | **EXCLUDE FOR NOW** | CSS filters & SVG textures giải quyết đủ glow/grain 2D. |
| 17 | `goldfire/howler.js` | **CHƯA** | Web Audio API playback trong browser | Rất thấp | Không liên quan | Chỉ phát audio trên web, không ảnh hưởng video render | **EXCLUDE FOR NOW** | FFmpeg đã đảm nhiệm toàn bộ audio offline. |
| 18 | `Vanilagy/mediabunny` | **CHƯA** | WebCodecs media parser/muxer | Thấp | **Trùng FFmpeg** | FFmpeg CLI đã mux MP4 cực nhanh và ổn định | **EXCLUDE FOR NOW** | Không thay thế FFmpeg trong pipeline sản xuất. |

---

## 3. TỔ HỢP CÔNG NGHỆ TỐI THIỂU ĐỀ XUẤT (MINIMAL RECOMMENDED STACK)

### Core Production Stack (Siêu Tinh Gọn)
1. **Rendering & Compositing:**
   - **HyperFrames (HTML/SVG):** Engine mặc định cho 2D explainer, mascot, doodle.
   - **Remotion (React/TSX):** Engine tùy chọn khi cần Spring physics, typography phức tạp hoặc UI components.
2. **Animation Engine:**
   - **GSAP 3:** Động cơ timeline, easing, stagger cho toàn bộ chuyển động.
3. **Asset & Assembly Tooling:**
   - **SVGO:** Dọn dẹp và chuẩn hóa ID cho tài nguyên vector SVG trước khi đưa vào animation.
   - **FFmpeg:** Cắt lát sample bounds và ghép video master đồng bộ âm thanh.
4. **Agent Intelligence (0kb Runtime):**
   - **`gsap-skills`** & **`remotion-skills`**: Nạp vào kho chỉ dẫn để AI viết code chính xác ngay từ lần đầu.

---

## 4. KHOẢNG TRỐNG CHẤT LƯỢNG THỰC TẾ & KẾ HOẠCH KIỂM CHỨNG BẰNG 1 PILOT

### Khoảng trống còn lại (Chưa công nghệ nào giải quyết tự động):
- **Chất lượng Mỹ thuật Gốc (Art Direction):** Không có thư viện nào tự vẽ ra được nhân vật đẹp nếu không có họa sĩ hoặc tài nguyên thiết kế chuẩn.
- **Tính tự nhiên của Cử động (Character Rigging):** Cần quy chuẩn tách lớp cơ thể (Body parts hierarchy) hơn là thêm một thư viện code mới.

### Kế hoạch Kiểm chứng bằng 1 Pilot Mẫu (15–30s):
- **Cùng Brief & Audio:** Sử dụng 1 đoạn audio voice-over 15s có sẵn từ `input_voice/`.
- **Thử nghiệm A/B:**
  - *Nhánh A (Baseline cũ):* Code thủ công bằng HyperFrames + SVG thuần.
  - *Nhánh B (Stack tinh gọn mới):* Sử dụng SVGO làm sạch SVG + chỉ dẫn GSAP chuẩn từ `gsap-skills` + quy tắc Full Canvas (bỏ footer 200px).
- **Tiêu chí đánh giá:** So sánh độ mượt easing, độ sắc nét bố cục và tốc độ render trước khi áp dụng đại trà.
