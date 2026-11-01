"""Assemble two self-contained HyperFrames scene entries from editable SVG + GSAP.
Uses the existing installed runtime; does not modify audio or scene manifest.
"""
from pathlib import Path
from fractions import Fraction
import json,shutil,wave,sys,hashlib,argparse
sys.stdout.reconfigure(encoding='utf-8')
P=Path(__file__).resolve().parents[1]
M=json.loads((P/'inputs/scene-manifest.json').read_text(encoding='utf-8-sig'))
project=json.loads((P/'project_manifest.json').read_text(encoding='utf-8-sig'))
gsap=P/'assets/vendor/gsap.min.js'
assert gsap.exists(),gsap
parser=argparse.ArgumentParser()
parser.add_argument('--scene', choices=['S03','S08'])
args=parser.parse_args()
config={'status':'PILOT WORKING CONFIGURATION — NOT FULL FILM APPROVAL','width':1080,'height':1920,'fps':30,'scene_manifest_unchanged':True,'scenes':{}}
if (P/'build/pilot-working-config.json').exists():
    config=json.loads((P/'build/pilot-working-config.json').read_text(encoding='utf-8'))
for sid,name in [('S03','coast'),('S08','home')]:
    if args.scene and args.scene != sid:
        continue
    s=next(x for x in M['scenes'] if x['scene_id']==sid)
    a,b=s['start_sample'],s['end_sample']
    first=round(Fraction(a*30,24000));last=round(Fraction(b*30,24000));frames=last-first
    duration=frames/30
    dst=P/'scenes'/sid;dst.mkdir(parents=True,exist_ok=True)
    (dst/'assets').mkdir(exist_ok=True)
    shutil.copy2(gsap,dst/'assets/gsap.min.js')
    shutil.copy2(P/'assets/fonts/pilot-bold.ttf',dst/'assets/pilot-bold.ttf')
    art=(P/f'assets/illustration/{sid}-{name}.svg').read_text(encoding='utf-8')
    motion=(P/'components/pilot-motion.js').read_text(encoding='utf-8')
    highlights=json.loads((P/'components/pilot-highlights.json').read_text(encoding='utf-8'))[sid]
    overlay='<div class="top-shade"></div>'
    for h in highlights:
        top='17.5%' if sid=='S08' and h['id']=='family' else '9%'
        words=''.join('<span>'+word+'</span> ' for word in h['text'].split())
        overlay+=f'<div class="highlight clip" data-start="{h["at"]}" data-duration="{(h["out"]+.18 if h["out"] else duration)-h["at"]}" id="hl-{h["id"]}" style="top:{top}" data-at="{h["at"]}" data-out="{h["out"]}" data-kind="{h["kind"]}"><div class="word-mask" data-layout-allow-overflow>{words}</div><i></i></div>'
    if sid=='S08':overlay+='<div id="terrace-light"></div>'
    html=f''' <!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=1080,height=1920"><title>{sid} · VIDEO-34 creative pilot</title><link rel="icon" href="data:,"><script src="assets/gsap.min.js"></script><style>html,body{{margin:0;width:100%;height:100%;overflow:hidden;background:#092740}}#root{{position:relative;width:100%;height:100%;overflow:hidden}}@font-face{{font-family:PilotBold;src:url('assets/pilot-bold.ttf');font-weight:700}}#root{{container-type:size}}.top-shade{{position:absolute;inset:0 0 auto;height:38%;background:linear-gradient(#092740 0%,#092740ec 58%,#09274000);pointer-events:none}}.highlight{{position:absolute;left:8%;right:5%;font-family:PilotBold;font-weight:700;font-size:8cqw;line-height:1.16;color:#fff;letter-spacing:-.035em}}.word-mask{{overflow:hidden;padding:8px 0}}.highlight span{{display:inline-block;opacity:0}}.highlight i{{display:block;width:22%;height:5px;background:#ffce40;transform-origin:left}}#hl-family{{color:#41e2e3}}#terrace-light{{position:absolute;right:0;top:38%;width:47%;height:47%;background:linear-gradient(135deg,#ffe598,transparent);opacity:0;pointer-events:none}}svg{{display:block;width:100%;height:100%}}</style></head><body><main id="root" data-composition-id="{sid}" data-width="1080" data-height="1920" data-fps="30" data-duration="{duration:.12f}">{art}{overlay}</main><script>{motion}\nwindow.__timelines=window.__timelines||{{}};window.__timelines['{sid}']=createPilotTimeline('{sid}');</script></body></html>'''
    (dst/'index.html').write_text(html,encoding='utf-8')
    with wave.open(str(P/project['audio']['path']),'rb') as source:
        source.setpos(a);pcm=source.readframes(b-a);params=source.getparams()
    with wave.open(str(dst/'voice-excerpt.wav'),'wb') as out:
        out.setparams(params);out.writeframes(pcm)
    config['scenes'][sid]={'source':f'scenes/{sid}/index.html','start_sample':a,'end_sample':b,'master_start':a/24000,'master_end':b/24000,'audio_samples':b-a,'audio_duration':(b-a)/24000,'cumulative_start_frame':first,'cumulative_end_frame':last,'frames':frames,'picture_duration':duration,'picture_minus_audio_seconds':duration-(b-a)/24000,'audio_sha256':hashlib.sha256(pcm).hexdigest(),'canonical_art':f'assets/illustration/{sid}-{name}.svg','picture_output':f'scenes/{sid}/picture.mp4','review_output':f'scenes/{sid}/{sid}-pilot.mp4'}
    print(sid,frames,'frames; exact audio samples:',b-a)
(P/'build/pilot-working-config.json').write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
