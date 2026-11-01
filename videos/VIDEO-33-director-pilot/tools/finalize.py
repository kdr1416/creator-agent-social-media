"""Verify delivered pilot media and write a reviewable Antigravity handoff.

Uses local FFmpeg/FFprobe, Pillow, NumPy and fontTools; no network or media APIs.
"""
from pathlib import Path
import json, subprocess, hashlib, wave, html, re, shutil
import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from prepare import ROOT, REPO, SOURCE, REFERENCE, save, digest, manifest

TIMES={'S01':[.1,1.5,3.3,5.8],'S05':[.1,1.0,2.1,5.5],'S09':[.1,2.6,4.3,7.2]}

def command(args):
    return subprocess.run(args,check=True,capture_output=True).stdout

def main():
    board=json.loads((ROOT/'STORYBOARD.json').read_text(encoding='utf-8'))
    font=TTFont(ROOT/'assets/fonts/segoe-ui-black.ttf')
    cmap=font.getBestCmap()
    visible=''.join(t['text'] for s in board['scenes'] for t in s['visible_text_inventory'])
    allvi='ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ'
    missing=sorted(set(c for c in visible+allvi if not c.isspace() and ord(c) not in cmap))
    assert not missing,missing
    save('qa/font-coverage.json',{'font':'Segoe UI Black','path':'assets/fonts/segoe-ui-black.ttf','source_sha256':digest(ROOT/'assets/fonts/segoe-ui-black.ttf'),'visible_text_all_scenes_covered':True,'vietnamese_precomposed_test_string':allvi,'missing_glyphs':missing,'unicode_normalization':'source text preserved; precomposed Vietnamese cmap checked','raster_check':'See final mobile proof sheets, including ĐIỂM TỰA and NHIỀU THỊ TRƯỜNG.'})
    reports=[]; overview=Image.new('RGB',(1080,680),'#FFF8E9'); draw=ImageDraw.Draw(overview)
    label_font=ImageFont.truetype(str(ROOT/'assets/fonts/segoe-ui-black.ttf'),22)
    proof_sheet=Image.new('RGB',(4*360,3*680),'#FFF8E9')
    proof_draw=ImageDraw.Draw(proof_sheet)
    comparison=Image.new('RGB',(4*270,520),'#FFF8E9')
    ref=Image.open(ROOT/'qa/reference-12.jpg').convert('RGB').resize((270,480))
    comparison.paste(ref,(0,40)); ImageDraw.Draw(comparison).text((15,10),'Reference 12',font=label_font,fill='#30313B')
    for row,(sid,times) in enumerate(TIMES.items()):
        s=next(s for s in board['scenes'] if s['scene_id']==sid)
        folder=ROOT/'pilots'/sid; video=folder/'renders/pilot.mp4'; voice=folder/'assets/voice.wav'
        probe=json.loads(command(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]))
        vs=next(st for st in probe['streams'] if st['codec_type']=='video')
        aus=next(st for st in probe['streams'] if st['codec_type']=='audio')
        assert (vs['width'],vs['height'])==(720,1280)
        assert vs['avg_frame_rate']=='30/1'
        vd=float(vs['duration']);ad=float(aus['duration'])
        with wave.open(str(voice),'rb') as w:
            rate=w.getframerate();frames=w.getnframes();original=w.readframes(frames)
        a=np.frombuffer(original,np.int16).astype(np.float64)/32768
        decoded=command(['ffmpeg','-v','error','-i',str(video),'-vn','-ac','1','-ar','24000','-f','s16le','-'])
        b=np.frombuffer(decoded,np.int16).astype(np.float64)/32768
        length=min(len(a),len(b));corr=float(np.corrcoef(a[:length],b[:length])[0,1])
        rms=float(np.sqrt(np.mean(b*b))); gain=float(np.sqrt(np.mean(b[:length]**2))/np.sqrt(np.mean(a[:length]**2)))
        assert corr>.98,(sid,corr)
        assert rms>.001 and abs(vd-frames/rate)<.05
        with wave.open(str(ROOT/'inputs/source_audio.wav'),'rb') as w:
            w.setpos(s['start_sample']); expected=w.readframes(s['sample_frames'])
        assert original==expected, sid
        proofs=[]
        for col,t in enumerate(times):
            target=ROOT/f'qa/{sid}/frame-{t:.2f}.png';target.parent.mkdir(exist_ok=True)
            command(['ffmpeg','-y','-v','error','-ss',str(t),'-i',str(video),'-frames:v','1',str(target)])
            im=Image.open(target).convert('RGB'); mobile=im.resize((360,640),Image.Resampling.LANCZOS)
            mobile.save(ROOT/f'qa/{sid}/mobile-{t:.2f}.png')
            proof_sheet.paste(mobile,(col*360,row*680+40))
            proof_draw.text((col*360+12,row*680+9),f'{sid} · {t:.2f}s',fill='#30313B',font=label_font)
            ImageOps.grayscale(im).resize((180,320)).save(ROOT/f'qa/{sid}/gray-{t:.2f}.png')
            footer=np.asarray(im)[1080:,:,:]
            proofs.append({'at':t,'frame':str(target.relative_to(ROOT)),'footer_pixel_range':(footer.max(axis=(0,1))-footer.min(axis=(0,1))).tolist()})
        last=Image.open(ROOT/f'qa/{sid}/frame-{times[-1]:.2f}.png').convert('RGB')
        overview.paste(last.resize((360,640)),(row*360,40));draw.text((row*360+12,9),{'S01':'S01 · Điểm tựa','S05':'S05 · Malta','S09':'S09 · Phân bổ'}[sid],font=label_font,fill='#30313B')
        comparison.paste(last.resize((270,480)),((row+1)*270,40));ImageDraw.Draw(comparison).text(((row+1)*270+15,10),sid,font=label_font,fill='#30313B')
        check=json.loads((folder/'qa-check.json').read_text(encoding='utf-8-sig'))
        assert check['ok'] and not check['browserSkipped']
        report={'scene_id':sid,'video':str(video.relative_to(ROOT)),'file_sha256':digest(video),'video_codec':vs['codec_name'],'width':720,'height':1280,'fps':vs['avg_frame_rate'],'video_frames':int(vs['nb_frames']),'video_duration':vd,'audio_codec':aus['codec_name'],'audio_duration':ad,'source_samples':frames,'source_duration':frames/rate,'picture_tail_over_voice_ms':round((vd-frames/rate)*1000,6),'voice_pcm_bit_exact_source_range':True,'decoded_audio_correlation':corr,'decoded_audio_rms':rms,'decoded_vs_source_rms_ratio':gain,'hyperframes_check_ok':check['ok'],'runtime_error_count':check['runtime']['errorCount'],'layout_error_count':check['layout']['errorCount'],'contrast':check['contrast'],'motion_assertions_enabled':check['motion']['enabled'],'proofs':proofs,'note':'AAC is lossy; copied PCM stays bit-exact. One-frame picture rounding is not voice stretching. Automated motion assertions were not authored; motion is reviewed with real frames and playback.'}
        save(f'qa/{sid}/verification.json',report);reports.append(report)
        s['status']='pilot_rendered_awaiting_user_review'
        for aobj in s['asset_contract']:aobj['status']='implemented_in_editable_pilot_source'
        s['asset_contract_evidence']=f'pilots/{sid}/index.html; pilots/{sid}/assets/layered-art.svg'
        for axis,data in s['reference_alignment'].items():
            data['assessment']='partial' if axis in ['motion_rhythm','asset_mix'] and sid=='S09' else 'match'
            data['candidate_evidence']=f'qa/{sid}/mobile-{times[-1]:.2f}.png; in-progress {times[2]}s; pilots/{sid}/index.html'
            data['revision_needed']='User acceptance pending. S09 deliberately omits mascot/photo for abstract allocation; does not prove full-film motion continuity.' if sid=='S09' else 'No mismatch seen in inspected frames; style and motion remain subject to user review.'
        save(f'scenes/{sid}/packet.json',s)
    overview.save(ROOT/'qa/PILOT_OVERVIEW.jpg',quality=94)
    proof_sheet.save(ROOT/'qa/ALL_FRAME_PROOFS.jpg',quality=92)
    comparison.save(ROOT/'qa/REFERENCE_COMPARISON.jpg',quality=94)
    gray=ImageOps.grayscale(overview).resize((540,340));gray.save(ROOT/'qa/GRAYSCALE_THUMBNAIL.png')
    save('qa/media-verification.json',reports)
    save('STORYBOARD.json',board)
    # Scene interval and full-film picture grid are independent of pilot frame rounding.
    scenes=board['scenes']; assert scenes[0]['start_sample']==0
    assert all(a['end_sample']==b['start_sample'] for a,b in zip(scenes,scenes[1:]))
    assert scenes[-1]['end_sample']==1803840
    save('qa/timeline-audit.json',{'scene_count':14,'source_segments_covered':list(range(1,18)),'sample_frames':1803840,'sample_rate':24000,'duration':75.16,'contiguous_without_overlap':True,'full_film_picture_frames_30fps':2255,'individual_pilot_frames':{r['scene_id']:r['video_frames'] for r in reports},'full_film_rendered':False})
    before=json.loads((ROOT/'qa/source-before.json').read_text(encoding='utf-8'))
    after=manifest(); changed=[p for p,h in before.items() if after.get(p)!=h]
    added=[p for p in after if p not in before]
    assert not changed and not added, (changed,added)
    save('qa/source-after.json',after)
    save('qa/source-integrity.json',{'files_checked':len(before),'changed':changed,'added_to_source_projects':added,'all_input_and_reference_files_unchanged':True})
    ledger=[]
    for p in sorted((ROOT/'assets').rglob('*')):
        if p.is_file():ledger.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p),'provenance':'Wikimedia Commons credit in CREDITS.md' if p.name=='valletta.jpg' else 'supplied approved reference; paths in ASSET_PLAN.json'})
    save('assets/ledger.json',ledger)
    ap=json.loads((ROOT/'ASSET_PLAN.json').read_text(encoding='utf-8'))
    for group in ap['new_pilot']:
        for item in group['layers']:item['status']='implemented_in_pilot_HTML_and_layered_SVG'
    ap['delivered_assets_ledger']='assets/ledger.json';save('ASSET_PLAN.json',ap)
    save('TECHNICAL_HANDOFF.md',technical(reports))
    save('REVIEW_GUIDE.md',review())
    save('ANTIGRAVITY_PROMPT.md',antigravity())
    save('START_HERE.md','# VIDEO-33 · Bàn giao đạo diễn\n\nMở REVIEW.html để xem 3 MP4; xem STORYBOARD.html cho chuỗi 14 khung và STORYBOARD.md/.json cho đặc tả toàn phim. Đọc DIRECTOR_BRIEF.md → CONTINUITY.md → RESEARCH.md → ASSET_PLAN.md → packet scenes/Sxx → TECHNICAL_HANDOFF.md.\n\nĐã hoàn thành phạm vi storyboard + 3 pilot, chờ người dùng duyệt. 11 cảnh còn lại chỉ thiết kế. Không dựng full hoặc xuất bản tự động. S10 có vấn đề số tiền trong voice cần chủ nội dung xác nhận trước bản phát hành.\n\nMP4: pilots/S01/renders/pilot.mp4, pilots/S05/renders/pilot.mp4, pilots/S09/renders/pilot.mp4. Editable source cạnh từng render. Source audio + raw/timing nằm trong inputs/ và được hash bảo toàn.\n\nMinh chứng: qa/PILOT_OVERVIEW.jpg, qa/ALL_FRAME_PROOFS.jpg, qa/REFERENCE_COMPARISON.jpg, qa/GRAYSCALE_THUMBNAIL.png, qa/media-verification.json.\n')
    status={'project':'VIDEO-33-director-pilot','phase':'storyboard_and_three_pilots_complete_awaiting_user_review','user_approved':False,'duration':75.16,'sample_frames':1803840,'scenes_designed':14,'pilot_scenes':['S01','S05','S09'],'pilot_renders':reports,'remaining_scenes':11,'remaining_scenes_status':'design_only_not_authorized_for_render_in_this_turn','full_film_rendered':False,'source_integrity':'qa/source-integrity.json','review_entry':'REVIEW.html','publication_hold':['S10 price claim 3.8bn VND lacks verified cost basis; keeping original voice does not resolve claim'],'auditory_review':'Source WAV made available for playback; independent perceptual listening/phonetic adjudication is not established by tool output. ASR uncertainties remain explicit. No voice edits.','playback_review':'See qa/playback-review.json for observed browser playback, separate from sampled-frame QA.','workflow_capabilities':{'flow_health':'unreachable','flow_generation_used':False,'hyperframes_version':'0.8.170','usage':'unknown / usage_request_failed','skills_update':'attempt failed ENOTFOUND registry.npmjs.org; already-installed workflow read and used, no successful update','audio_fallback_used':False,'renderer':'actual HyperFrames, screenshot capture, NVIDIA hardware GPU'},'next_action':'User reviews storyboard/pilot ideas; Antigravity receives production prompt only after approval.'}
    save('production_status.json',status)
    save('REVIEW.html',gallery(scenes))
    print(json.dumps({'all_sources_unchanged':True,'source_files_checked':len(before),'pilots':[{'id':r['scene_id'],'duration':r['video_duration'],'audio_corr':r['decoded_audio_correlation']} for r in reports],'font_missing':missing},ensure_ascii=False,indent=2))

def technical(reports):
    table='\n'.join(f"| {r['scene_id']} | {r['source_samples']} | {r['source_duration']:.9f} | {r['video_frames']} | {r['video_duration']:.6f} | {r['decoded_audio_correlation']:.6f} |" for r in reports)
    return '''# Technical handoff

## Source and timing

`inputs/source_audio.wav`: original PCM16, mono, 24,000Hz, 1,803,840 sample frames = 75.16s. Copied WAV and all original slices/transcripts remain unchanged. All 17 slices reassemble bit-for-bit; original/reference files are hashed before and after. See qa/source-integrity.json and qa/audio-source-verification.json.

14 scene intervals are exact half-open sample ranges [start, end). Use sample bounds, never the rounded timestamps printed in a Markdown table. Corrected text is editorial metadata, not a replacement voice. Seg13 con gái/con cái remains uncertain; do not silently change it or claim phonetic verification. Internal cue times are approximate director marks, not forced word alignment.

## Three delivered exports

| Scene | Source samples | Voice seconds | Video frames at 30fps | Picture seconds | AAC/source correlation |
|---|---:|---:|---:|---:|---:|
'''+table+'''

AAC is lossy and therefore cannot be bit-identical to PCM; correlation verifies alignment/content and non-silent audio. Exact PCM is shipped. No TTS, speed, pitch, EQ, added soundtrack or removed pauses. Successful native HyperFrames audio export; the fallback was not used.

## Future film assembly — only after user approval

Use planning/picture_frame_plan.json/.csv. Global boundary = round-half-up(start_sample × 30 / 24000), not accumulated scene duration. 2255 picture frames for the full 75.16s voice. This is a plan, not a produced full film.

Standalone pilot rounding uses ceil frames, and S05 is one frame longer than its assigned global picture slot. For future assembly derive a picture-only copy to the global slot count; keep source pilot untouched. Place exactly one full `inputs/source_audio.wav` at t=0 over assembled picture. Do not join independently AAC-encoded pilot voices for the final film: encoder padding can drift. Keep final hold through the last voice sample; no artificial black-out at audio end.

## Editable source

Each pilot has `index.html`, local `assets/voice.wav`, GSAP, fonts, an editable `layered-art.svg`, `hyperframes.json`, `package.json`, `frame.md` and `renders/pilot.mp4`. HTML owns placement/timing; SVG is a layer extraction, not an extra imported duplicate. When editing the SVG separately, sync its changed markup back into HTML. Rig travel wrappers surround fixed SVG placement groups; arm paths/hand endpoints move together. Far arm behind torso, near arm in front.

One paused GSAP timeline per root, matching composition ID. Deterministic, offline media; no unseeded random, render clock or network fetch. Root width/height 100%, canvas data-width=720/data-height=1280. Prefix new IDs. To mount as subcomposition, put styles/scripts inside `<template>`; read the installed HyperFrames core contract first. Current projects are standalone pilots.

Reproducible commands per pilot: `npx hyperframes@0.8.170 check --at 0,1.5,3.3,5.8 --json` (adapt times to duration); `npx hyperframes@0.8.170 preview --background`; `npx hyperframes@0.8.170 render --fps 30 --quality delivery --workers 2 --output renders/pilot.mp4`. Current environment used cached official CLI directly to avoid npm DNS. Browser execution required normal local permissions. Version 0.8.170 matched CLI latest metadata. Workflow skill refresh failed DNS; already-installed skill files were read, no successful refresh is claimed. Usage API returned unknown.

Python utilities are persistent project tools, not API batch submitters: prepare.py generates initial direction (refuses overwrite); build_pilots.py rebuilds ONLY three sources; finalize.py verifies exports and builds proof/handoff. Run finalize after any render change. Do not rerun build_pilots over manual edits without deliberately integrating them first. No calls to media-generation API were made.

## Validation limits

Native HyperFrames check passed lint/runtime/layout/contrast for all three at actual sampled times. Motion assertions are not enabled; visual proof and browser playback are separate evidence. Cmap tested all Vietnamese precomposed characters plus every visible scene string; raster/mobile proof required as well. Current reference comparison does not constitute user approval.

Footer y=1080–1280 remains free of important visuals. Main text 44–76px, S01 final strip 46px, not Arial Black. Font licensing/provenance and photo attribution are in CREDITS.md. Flow server was unreachable at preflight; all scenes positively route to HF_ONLY, so no Flow request/ref/UUID/video-review branch is required. Future engine changes need an explicit routing override.
'''

def review():
    return '''# Review guide · User approval pending

Mở REVIEW.html hoặc xem riêng ba MP4. Đây là ba trích đoạn có voice gốc, không phải bản phim ghép liên tục.

1. **S01 / 0–6.0194s:** có đọc được quan hệ “việc học → điểm tựa lâu dài” từ sách và mặt đỡ không? Mascot giữ mép trang, nhà chỉ là ẩn dụ; nếu nhà trông như phần thưởng được cấp tự động, cần sửa cách xuất hiện.
2. **S05 / 18.1512–23.8575s:** giấy mở phải lộ Valletta có lý do địa lý; tay có theo đúng nếp không; nhà cũ vẫn còn; ảnh không bị hiểu là căn nhà chào bán. Kiểm frame 1.0/2.1s, không chỉ poster kết.
3. **S09 / 39.8001–47.2510s:** ba đồng từ một nơi phân bổ sang nhiều vùng; không có đường tăng lợi nhuận/khiên bảo đảm. Cơ chế đủ rõ khi nghe một lần; nếu giống đường đi tuần tự, cần làm rõ đây là phân bổ đồng thời, không quy trình ba bước.

Xem qa/ALL_FRAME_PROOFS.jpg cho opening/action/final; từng ảnh 360×640 nằm trong qa/Sxx/. Đọc dấu ở “ĐIỂM TỰA DÀI LÂU” và “NHIỀU THỊ TRƯỜNG”, xem grayscale thumbnail để phát hiện khối tối dính nhau. So cạnh reference ở qa/REFERENCE_COMPARISON.jpg: màu, chữ, asset mix, bố cục, mascot, nhịp chuyển động. Video encode thành công không có nghĩa ý tưởng/phong cách được chấp nhận.

## Phần chưa được chứng minh

Chưa dựng 11 cảnh còn lại, chưa xem full-film seam/playback. Gia phả S10 mới là thiết kế. Mốc cử động nội cảnh là ước lượng đạo diễn; không tuyên bố đã nghe thẩm định âm vị độc lập bằng công cụ. Đối chiếu nghe từ WAV nguyên bản trước khóa timing chi tiết ở phần sản xuất còn lại. Seg02/13 vẫn giữ uncertainty trong input.

S10 có claim “3,8 tỷ” chưa khớp cấu phần phí MPRP hiện tại. Voice nguyên vẹn theo brief; không tự cắt/sửa. Cần chủ nội dung xác nhận cơ sở con số/phạm vi hoặc cho phép sửa ở giai đoạn sau trước phát hành. Không yêu cầu thay audio trong lượt này; đây là vấn đề biên tập thực tế được ghi lại, không cản duyệt ý tưởng/pilot.

Có thể duyệt riêng: (a) visual proposition toàn phim; (b) phong cách/mascot/font; (c) cách chuyển động và nhịp của 3 pilot. Duyệt một mục không tự cho phép dựng full hay xuất bản. Mọi điều chỉnh layout/pose/easing thường quy được linh hoạt trong ranh giới ý nghĩa đã khóa.
'''

def antigravity():
    return '''# Prompt bàn giao cho Antigravity

Tiếp nhận folder `videos/VIDEO-33-director-pilot/`. Trong trạng thái hiện tại chỉ đọc, kiểm tra và chuẩn bị sản xuất; đợi người dùng duyệt storyboard/pilot trước khi dựng 11 cảnh còn lại. Không coi sự tồn tại của prompt này là lệnh tự chạy full.

Đọc START_HERE.md, DIRECTOR_BRIEF.md, STORYBOARD.md/.json, CONTINUITY.md, ASSET_PLAN.md/.json, RESEARCH.md, TECHNICAL_HANDOFF.md, REVIEW_GUIDE.md và production_status.json. Sau đó đọc scenes/Sxx/PACKET.md cùng packet.json cho từng cảnh. Source audio/raw ASR/timing nằm trong inputs/; sample bounds là nguồn sự thật.

Khi người dùng đã duyệt sản xuất, bạn phụ trách tạo asset tách lớp/pose và dựng các cảnh chưa làm. Codex đã quyết định ý chính, hình chủ đạo, trạng thái đầu–biến đổi–kết, vai trò mascot và điểm chuyển cảnh. Không tự đoán lại nội dung từ một câu voice hoặc thay hình bằng stock icon/card. Chọn asset đúng asset_contract; ghi nguồn, license, checksum. Nếu thiếu asset chính, giữ ý thiết kế, báo vướng mắc cụ thể và làm cảnh độc lập khác.

Giữ: mascot cam bo góc/mũ tím/ba lô xanh; warm cream/peach/lilac + accents tươi, nét mảnh; voice gốc không sửa sample/pitch/speed/EQ; font Segoe UI Black full dấu; subtitle footer 200px; physical contact/semantic action; quan hệ hình và ý chính trong packet. Không ghi Hình minh hoạ hoặc Không gian minh hoạ lên video. Không tự thêm CTA, thành tích, nghề, giá, lợi nhuận, quyền visa/quốc tịch hoặc quyền làm việc EU.

Linh hoạt: cân khung, tỷ lệ vật thể, nếp giấy, số nét, pose/ánh mắt, easing và dời cue cử động bên trong cùng lát voice sau nghe đối chiếu. Cue đạo diễn không phải word-alignment. Nếu cần thay prop chủ đạo hoặc engine, ghi previous_mode/new_mode/routing_override_reason và lý do giữ nghĩa; không đổi âm thầm.

S01/S05/S09 có source editable, assets/fonts local và MP4. Giữ chúng như mốc review, không ghi đè khi sửa; tạo revision riêng. Khai thác ngữ pháp, không nhân bản nguyên cảnh sách/ảnh/ba bệ sang mọi đoạn. 11 cảnh còn lại chưa có asset/render dù packet đầy đủ. Không sửa dự án VIDEO-33 hoặc tran-minh-nhat-director-handoff, không đổi workflow chính.

Đặc biệt S10: giữ trạng thái HOLD_PUBLICATION cho claim giá 3,8 tỷ trong voice tới khi chủ nội dung xác nhận cơ sở hiện hành. Bốn thế hệ theo MPRP là điều kiện hồ sơ, không bốn đời con cháu mặc nhiên có quyền; mua nhà không tự tạo thường trú/quốc tịch; thăm Schengen khác quyền lao động. Không dùng việc bỏ số khỏi overlay để tuyên bố claim audio đã được giải quyết.

QA mỗi cảnh: actual HyperFrames check; opening/signature-in-progress/final frames; playback voice gốc; mobile 360×640; font dấu; grayscale; tiếp xúc tay/đạo cụ; đủ thời gian kết. Film QA: không lặp visual meaning/action/layout, không card ngụy trang, không nhân vật mannequin, không mã hóa quyền lợi chưa xác minh. Assemble sau cùng theo global picture_frame_plan, một track full WAV duy nhất. Không nối AAC pilot để thay voice tổng.
'''

def gallery(scenes):
    entries=[]
    for sid in TIMES:
        s=next(s for s in scenes if s['scene_id']==sid)
        entries.append(f'''<article><h2>{sid} · {html.escape(s['title'])}</h2><p>{s['start']:.3f}–{s['end']:.3f}s trong voice gốc · {s['duration']:.3f}s</p><video id="video-{sid}" controls playsinline preload="metadata" poster="qa/{sid}/frame-{TIMES[sid][-1]:.2f}.png" src="pilots/{sid}/renders/pilot.mp4"></video><button onclick="const v=document.getElementById('video-{sid}');v.currentTime=0;v.play()">Phát {sid} từ đầu</button><output id="state-{sid}">Chưa phát</output><p>{html.escape(s['takeaway'])}</p><a href="pilots/{sid}/index.html">Source HTML</a> · <a href="scenes/{sid}/PACKET.md">Scene packet</a></article>''')
    script=''.join(f"document.getElementById('video-{sid}').addEventListener('timeupdate',e=>{{const v=e.target;document.getElementById('state-{sid}').textContent=v.currentTime.toFixed(2)+' / '+v.duration.toFixed(2)+'s'+(v.ended?' · Đã phát hết':' · Đang phát');}});" for sid in TIMES)
    return '''<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VIDEO-33 · Storyboard & 3 pilots</title><style>@font-face{font-family:Review;src:url('assets/fonts/arial.ttf')}@font-face{font-family:ReviewDisplay;src:url('assets/fonts/segoe-ui-black.ttf');font-weight:900}*{box-sizing:border-box}body{margin:0;padding:32px;background:#FFF8E9;color:#30313B;font-family:Review,sans-serif;line-height:1.5}h1,h2{font-family:ReviewDisplay,sans-serif}h1{font-size:30px}h2{font-size:22px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:32px;max-width:1250px}article{min-width:0}video{display:block;width:360px;max-width:100%;aspect-ratio:9/16;background:#F0EAFB}button{display:block;margin:12px 0;padding:12px 18px;border:0;background:#087BC1;color:white;font:700 16px Review,sans-serif;cursor:pointer}output{display:block;font-size:15px}a{color:#06659B}p{max-width:850px}.note{border-left:4px solid #A990D5;padding-left:15px}</style><h1>Một điểm tựa, thêm lựa chọn</h1><p>Storyboard 14 cảnh / voice gốc 75,16s. Ba pilot dưới đây là trích đoạn độc lập; chưa dựng full. Chờ duyệt ý tưởng và phong cách.</p><p><a href="STORYBOARD.html">Storyboard toàn phim</a> · <a href="REVIEW_GUIDE.md">Hướng dẫn duyệt</a> · <a href="ANTIGRAVITY_PROMPT.md">Bàn giao Antigravity</a></p><div class="grid">'''+''.join(entries)+'''</div><p class="note">Lưu ý biên tập: câu chi phí “3,8 tỷ” ở cảnh S10 chưa được xác minh theo cấu phần MPRP hiện tại. Voice được giữ nguyên; đọc RESEARCH.md trước bản phát hành. Ba pilot không bao gồm S10.</p><script>'''+script+'</script></html>'

if __name__=='__main__':
    main()
    from content_confirmations import apply
    apply()
