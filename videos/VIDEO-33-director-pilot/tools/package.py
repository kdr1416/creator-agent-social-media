"""Package final reproducible handoff; excludes caches and obsolete test frames."""
from pathlib import Path
import json, zipfile, hashlib
from PIL import Image,ImageDraw,ImageFont
from prepare import ROOT, save, digest

def main():
    overview=Image.new('RGB',(1080,680),'#FFF8E9');draw=ImageDraw.Draw(overview)
    font=ImageFont.truetype(str(ROOT/'assets/fonts/segoe-ui-black.ttf'),22)
    for i,(sid,t,label) in enumerate([('S01','5.80','Điểm tựa'),('S05','5.50','Malta'),('S09','7.20','Phân bổ')]):
        overview.paste(Image.open(ROOT/f'qa/{sid}/frame-{t}.png').resize((360,640)),(i*360,40))
        draw.text((i*360+12,9),sid+' · '+label,font=font,fill='#30313B')
    overview.save(ROOT/'qa/PILOT_OVERVIEW.jpg',quality=94)
    save('qa/playback-review.json',{'method':'IAB native browser playback through authored REVIEW.html buttons; timeupdate output observed to reach end. Actual MP4s, not source seeking. Sampled render frames separately inspected at 360x640 and grayscale.','url':'http://127.0.0.1:8766/REVIEW.html','results':[{'scene_id':'S01','observed_output':'6.03 / 6.03s · Đã phát hết','file_sha256':digest(ROOT/'pilots/S01/renders/pilot.mp4')},{'scene_id':'S05','observed_output':'5.73 / 5.73s · Đã phát hết','file_sha256':digest(ROOT/'pilots/S05/renders/pilot.mp4')},{'scene_id':'S09','observed_output':'7.47 / 7.47s · Đã phát hết','file_sha256':digest(ROOT/'pilots/S09/renders/pilot.mp4')}],'perceptual_listening':'Not established independently by browser state/audio emission. Phonetic uncertainties remain documented; no claim of auditory adjudication.','continuous_full_film_playback':False,'note':'Preview at its exact end may hide the composition; the encoded MP4 final frames were inspected and contain the final pose. No full film was created.'})
    required=['DIRECTOR_BRIEF.md','STORYBOARD.md','STORYBOARD.json','STORYBOARD.html','ASSET_PLAN.md','ASSET_PLAN.json','CONTINUITY.md','TECHNICAL_HANDOFF.md','REVIEW_GUIDE.md','production_status.json','ANTIGRAVITY_PROMPT.md','REVIEW.html']
    assert all((ROOT/p).exists() for p in required)
    assert len(list((ROOT/'scenes').glob('*/packet.json')))==14
    status=json.loads((ROOT/'production_status.json').read_text(encoding='utf-8'))
    status['playback_review']='Three encoded MP4s observed to complete in native browser; qa/playback-review.json. No independent perceptual listening/phonetic verification claimed.'
    status['storyboard_visual_sheet']='STORYBOARD.html: S01 original pilot frame, current approved S05 album v5 and S09 v2 stills, plus 11 rough staging sketches. Current motion candidates are identified in latest_motion_revisions and review_entry.'
    save('production_status.json',status)
    technical=ROOT/'TECHNICAL_HANDOFF.md'
    text=technical.read_text(encoding='utf-8')
    if '## Local review server' not in text:
        text+='\n## Local review server\n\nREVIEW.html and STORYBOARD.html also work as local files for offline review. Current local viewer: http://127.0.0.1:8766/REVIEW.html . If it stops, serve this folder with `python -m http.server 8766 --bind 127.0.0.1`; stop with Ctrl+C. No files are published externally. Studio source preview S01: http://localhost:3002/#project/S01 . Browser MP4s were observed to reach their ends (qa/playback-review.json); this is separate from independent perceptual listening.\n'
        technical.write_text(text,encoding='utf-8')
    # Frozen manifest for the portable package; logs/server files continue outside it.
    excluded={'.hyperframes','__pycache__','qa-frames'}
    files=[p for p in ROOT.rglob('*') if p.is_file() and not excluded.intersection(p.relative_to(ROOT).parts) and p.suffix not in ('.zip','.log','.tmp') and p.name!='package_manifest.json']
    save('package_manifest.json',{'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(files)],'excluded':'HyperFrames caches, Python caches, obsolete initial snapshots, running server logs, archive itself. Final proofs are qa/Sxx and qa/ALL_FRAME_PROOFS.jpg.','status':'review_package_not_full_production'})
    archive=ROOT/'VIDEO-33-director-pilot.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files+[ROOT/'package_manifest.json']:
            z.write(p,'VIDEO-33-director-pilot/'+str(p.relative_to(ROOT)))
    print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'files':len(files)+1,'required_files':True,'packets':14,'pilots':3,'full_film':False},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
