import json
from pathlib import Path

root = Path(r"D:\Năm 3\flowkit-main\videos\VIDEO-33-director-pilot\build\master-approved-r2")
manifest_p = root / "ASSEMBLY_MANIFEST_R2.json"
summary_p = root / "assembly_summary.json"

with open(manifest_p, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(summary_p, "r", encoding="utf-8") as f:
    summary = json.load(f)

scenes = manifest["scenes"]
seams = summary["seams"]
proofs = summary["proofs"]

# Group proofs by scene
proofs_by_scene = {}
for p in proofs:
    sid = p["scene_id"]
    if sid not in proofs_by_scene:
        proofs_by_scene[sid] = {}
    proofs_by_scene[sid][p["label"]] = p

html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VIDEO-33 Master Approved R2 Review Board</title>
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-gold: #facc15;
      --success: #22c55e;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.5;
      padding: 24px;
    }
    header {
      border-bottom: 1px solid var(--border);
      padding-bottom: 20px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 16px;
    }
    h1 { font-size: 24px; font-weight: 700; color: #fff; display: flex; align-items: center; gap: 10px; }
    .badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .badge-success { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }
    .badge-info { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid #0284c7; }
    .badge-warn { background: rgba(250, 204, 21, 0.2); color: #facc15; border: 1px solid #ca8a04; }
    
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-bottom: 24px;
    }
    .stat-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 16px;
    }
    .stat-label { font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 600; }
    .stat-value { font-size: 18px; font-weight: 700; color: var(--accent); margin-top: 4px; font-family: var(--font-mono); }

    .main-grid {
      display: grid;
      grid-template-columns: 420px 1fr;
      gap: 24px;
      margin-bottom: 32px;
    }
    @media (max-width: 960px) {
      .main-grid { grid-template-columns: 1fr; }
    }

    .player-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .video-wrapper {
      position: relative;
      width: 100%;
      max-width: 360px;
      aspect-ratio: 9/16;
      background: #000;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }
    video {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
    }
    .video-switch-buttons {
      display: flex;
      gap: 8px;
      margin-top: 16px;
      width: 100%;
      max-width: 360px;
    }
    .btn {
      flex: 1;
      background: #334155;
      color: #fff;
      border: 1px solid var(--border);
      padding: 8px 12px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s;
    }
    .btn:hover { background: #475569; }
    .btn.active {
      background: var(--accent);
      color: #0f172a;
      border-color: var(--accent);
    }

    .timeline-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
    }
    .section-title {
      font-size: 16px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .scene-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      max-height: 600px;
      overflow-y: auto;
      padding-right: 6px;
    }
    .scene-item {
      display: grid;
      grid-template-columns: 60px 100px 1fr 80px;
      gap: 12px;
      align-items: center;
      padding: 10px 14px;
      background: #0f172a;
      border: 1px solid var(--border);
      border-radius: 8px;
      font-size: 13px;
      cursor: pointer;
      transition: border-color 0.2s, background 0.2s;
    }
    .scene-item:hover { border-color: var(--accent); background: #131d35; }
    .scene-item.active { border-color: var(--accent-gold); background: rgba(250, 204, 21, 0.08); }
    .scene-id { font-weight: 700; font-family: var(--font-mono); color: var(--accent); }
    .scene-tag-new {
      background: #facc15;
      color: #000;
      font-size: 10px;
      font-weight: 800;
      padding: 1px 4px;
      border-radius: 4px;
      margin-left: 4px;
    }
    .scene-time { font-family: var(--font-mono); color: var(--text-muted); font-size: 12px; }
    .scene-desc { color: #e2e8f0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .scene-frames { font-family: var(--font-mono); text-align: right; color: var(--text-muted); font-size: 12px; }

    .seams-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }
    .seam-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .seam-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      font-weight: 600;
    }
    .seam-video-wrapper {
      width: 100%;
      aspect-ratio: 9/16;
      background: #000;
      border-radius: 6px;
      overflow: hidden;
    }

    .proofs-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      font-size: 13px;
    }
    .proofs-table th, .proofs-table td {
      border: 1px solid var(--border);
      padding: 10px 12px;
      text-align: left;
    }
    .proofs-table th { background: #131d35; color: var(--text-muted); font-weight: 600; }
    .proof-img {
      width: 80px;
      aspect-ratio: 9/16;
      object-fit: cover;
      border-radius: 4px;
      border: 1px solid var(--border);
      cursor: pointer;
      transition: transform 0.2s;
    }
    .proof-img:hover { transform: scale(1.8); z-index: 100; position: relative; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
    .toggle-gray-btn {
      font-size: 11px;
      padding: 4px 10px;
      background: #334155;
      color: #fff;
      border-radius: 4px;
      cursor: pointer;
      border: 1px solid var(--border);
    }
    .toggle-gray-btn:hover { background: #475569; }
  </style>
</head>
<body>

  <header>
    <div>
      <h1>
        VIDEO-33 Master Approved R2 Review Board
        <span class="badge badge-success">14 / 14 PILOTS APPROVED</span>
      </h1>
      <p style="color: var(--text-muted); font-size: 14px; margin-top: 4px;">
        Đa dạng hóa tài sản du học Châu Âu & Thẻ Xanh Malta • Trạng thái: <code>assembled_pending_user_full_master_review</code>
      </p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-info">FPS: 30.00</span>
      <span class="badge badge-info">2,255 FRAMES</span>
      <span class="badge badge-info">75.167s</span>
    </div>
  </header>

  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-label">Độ Dài Master</div>
      <div class="stat-value">75.167s (2,255f)</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Tỷ Lệ Duyệt Pilot</div>
      <div class="stat-value" style="color: #4ade80;">14 / 14 (100%)</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Cảnh Sửa Đổi R2</div>
      <div class="stat-value" style="color: #facc15;">S02, S03, S04</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Đồng Bộ Audio Gốc</div>
      <div class="stat-value">Δ=0ms | r=0.999958</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Mối Nối Chuyển Cảnh</div>
      <div class="stat-value">13 / 13 PASS</div>
    </div>
  </div>

  <div class="main-grid">
    <!-- Left Column: Video Player -->
    <div class="player-card">
      <div class="video-wrapper">
        <video id="mainVideo" controls autoplay playsinline src="VIDEO-33-master-approved-r2.mp4"></video>
      </div>
      <div class="video-switch-buttons">
        <button class="btn active" id="btnMaster" onclick="switchVideo('master')">Master R2 (Voice)</button>
        <button class="btn" id="btnClean" onclick="switchVideo('clean')">Clean R2 (Hình)</button>
        <button class="btn" id="btnMobile" onclick="switchVideo('mobile')">Mobile 360p</button>
      </div>
      <div style="margin-top: 14px; font-family: var(--font-mono); font-size: 13px; color: var(--text-muted); text-align: center;">
        Khung hình: <span id="frameCounter" style="color: var(--accent); font-weight: 700;">0</span> / 2255
        &nbsp;|&nbsp; Thời gian: <span id="timeCounter" style="color: var(--accent); font-weight: 700;">0.00s</span>
      </div>
    </div>

    <!-- Right Column: Interactive Timeline List -->
    <div class="timeline-card">
      <div class="section-title">
        <span>Danh Sách 14 Cảnh Thành Phẩm</span>
        <span style="font-size: 12px; color: var(--text-muted); font-weight: normal;">Nhấp vào cảnh để nhảy trực tiếp</span>
      </div>
      <div class="scene-list" id="sceneList">
"""

for s in scenes:
    sid = s["scene_id"]
    target_f = s["target_frames"]
    start_f, end_f = s["master_frame_range_half_open"]
    start_t, end_t = s["master_time_range_seconds"]
    desc = s["description"]
    is_new = sid in ["S02", "S03", "S04"]
    new_tag = '<span class="scene-tag-new">MỚI DUYỆT</span>' if is_new else ''
    
    html += f"""
        <div class="scene-item" id="item-{sid}" onclick="seekTo({start_t}, '{sid}')">
          <div class="scene-id">{sid} {new_tag}</div>
          <div class="scene-time">{start_t:.2f}s - {end_t:.2f}s</div>
          <div class="scene-desc" title="{desc}">{desc}</div>
          <div class="scene-frames">{target_f}f [{start_f}..{end_f-1}]</div>
        </div>
"""

html += """
      </div>
    </div>
  </div>

  <!-- 13 Seam Transitions Audit Section -->
  <div style="margin-top: 32px;">
    <div class="section-title">
      <span>Kiểm Định 13 Mối Nối Chuyển Cảnh (13 Seams QA Audit - 60 frames quanh điểm cắt)</span>
      <span class="badge badge-success">TẤT CẢ 13 SEAMS ĐẠT CHUẨN</span>
    </div>
    <div class="seams-grid">
"""

for sm in seams:
    sname = sm["name"]
    bf = sm["boundary_frame"]
    sc_b = sm["sc_before"]
    sc_after = sm["sc_after"]
    dur = sm["duration"]
    st = sm["start_time"]
    f_path = sm["file"]
    
    html += f"""
      <div class="seam-card">
        <div class="seam-card-header">
          <span style="color: var(--accent);">{sc_b} &rarr; {sc_after}</span>
          <span style="font-family: var(--font-mono); color: var(--text-muted);">Cut @ f{bf} ({st:.2f}s)</span>
        </div>
        <div class="seam-video-wrapper">
          <video controls preload="metadata" src="{f_path}"></video>
        </div>
      </div>
"""

html += """
    </div>
  </div>

  <!-- Visual Proofs & Grayscale Table -->
  <div style="margin-top: 40px;">
    <div class="section-title">
      <span>Bộ Chứng Chỉ Thị Giác 14 Cảnh (Visual Proofs: Open / Mid / End + Grayscale)</span>
      <button class="toggle-gray-btn" onclick="toggleGrayscaleAll()">Bật/Tắt Grayscale Toàn Bộ</button>
    </div>
    <table class="proofs-table">
      <thead>
        <tr>
          <th>Cảnh</th>
          <th>Mô Tả & Trực Quan</th>
          <th>Khung Mở (Open)</th>
          <th>Khung Giữa (Mid)</th>
          <th>Khung Cuối (End)</th>
        </tr>
      </thead>
      <tbody>
"""

for s in scenes:
    sid = s["scene_id"]
    desc = s["description"]
    v_core = s["visual_core"]
    is_new = sid in ["S02", "S03", "S04"]
    new_tag = '<span class="scene-tag-new">MỚI DUYỆT</span>' if is_new else ''
    
    p_open = proofs_by_scene[sid]["open"]
    p_mid = proofs_by_scene[sid]["mid"]
    p_end = proofs_by_scene[sid]["end"]
    
    html += f"""
        <tr>
          <td><strong style="color: var(--accent); font-family: var(--font-mono);">{sid}</strong> {new_tag}</td>
          <td>
            <div style="font-weight: 600; color: #fff;">{desc}</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">{v_core}</div>
          </td>
          <td>
            <img class="proof-img" src="{p_open['color_path']}" data-color="{p_open['color_path']}" data-gray="{p_open['gray_path']}" alt="{sid} Open f{p_open['frame']}" title="f{p_open['frame']}">
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted);">f{p_open['frame']}</div>
          </td>
          <td>
            <img class="proof-img" src="{p_mid['color_path']}" data-color="{p_mid['color_path']}" data-gray="{p_mid['gray_path']}" alt="{sid} Mid f{p_mid['frame']}" title="f{p_mid['frame']}">
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted);">f{p_mid['frame']}</div>
          </td>
          <td>
            <img class="proof-img" src="{p_end['color_path']}" data-color="{p_end['color_path']}" data-gray="{p_end['gray_path']}" alt="{sid} End f{p_end['frame']}" title="f{p_end['frame']}">
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted);">f{p_end['frame']}</div>
          </td>
        </tr>
"""

html += """
      </tbody>
    </table>
  </div>

  <footer style="margin-top: 48px; border-top: 1px solid var(--border); padding-top: 16px; font-size: 12px; color: var(--text-muted); display: flex; justify-content: space-between;">
    <div>Dự án: <strong>VIDEO-33</strong> • Phiên bản Master: <code>master-approved-r2</code></div>
    <div>Mã băm Master MP4: <code>c079c05e36ccf96dfb84e741248e5534eeacc82c4f56a5662352b6e158e94c7b</code></div>
  </footer>

  <script>
    const video = document.getElementById('mainVideo');
    const frameCounter = document.getElementById('frameCounter');
    const timeCounter = document.getElementById('timeCounter');
    let isGray = false;

    video.addEventListener('timeupdate', () => {
      const curT = video.currentTime;
      const curF = Math.floor(curT * 30);
      timeCounter.textContent = curT.toFixed(2) + 's';
      frameCounter.textContent = curF;
    });

    function switchVideo(type) {
      document.querySelectorAll('.btn').forEach(b => b.classList.remove('active'));
      const curTime = video.currentTime;
      const isPaused = video.paused;
      
      if (type === 'master') {
        video.src = 'VIDEO-33-master-approved-r2.mp4';
        document.getElementById('btnMaster').classList.add('active');
      } else if (type === 'clean') {
        video.src = 'VIDEO-33-clean-approved-r2.mp4';
        document.getElementById('btnClean').classList.add('active');
      } else if (type === 'mobile') {
        video.src = 'VIDEO-33-mobile-360x640-preview.mp4';
        document.getElementById('btnMobile').classList.add('active');
      }
      
      video.currentTime = curTime;
      if (!isPaused) video.play();
    }

    function seekTo(timeSeconds, sceneId) {
      video.currentTime = timeSeconds;
      video.play();
      document.querySelectorAll('.scene-item').forEach(el => el.classList.remove('active'));
      const activeItem = document.getElementById('item-' + sceneId);
      if (activeItem) activeItem.classList.add('active');
    }

    function toggleGrayscaleAll() {
      isGray = !isGray;
      document.querySelectorAll('.proof-img').forEach(img => {
        img.src = isGray ? img.getAttribute('data-gray') : img.getAttribute('data-color');
      });
    }
  </script>
</body>
</html>
"""

with open(root / "REVIEW.html", "w", encoding="utf-8") as f:
    f.write(html)

print("REVIEW.html generated successfully!")
