from pathlib import Path
import json,subprocess,math
P=Path(__file__).resolve().parents[1];E=P/'build/r1-evidence';E.mkdir(exist_ok=True)
H=json.loads((P/'components/pilot-highlights.json').read_text(encoding='utf-8'));rows=[]
for sid,highlights in H.items():
 for h in highlights:
  images={}
  for stage,t in [('before',h['at']-.1),('during',h['at']+.2),('settled',h['at']+.65)]:
   name=f'{sid}-{h["id"]}-{stage}.png'
   subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(P/f'scenes/{sid}/{sid}-pilot.mp4'),'-frames:v','1','-vf','scale=360:640',str(E/name)],check=True)
   images[stage]={'path':'build/r1-evidence/'+name,'local_time':t}
  rows.append({**h,'scene':sid,'first_eligible_picture_frame_time':math.ceil(h['at']*30)/30,'evidence':images,'verified_in_actual_mp4':'screenshots extracted; visual inspection recorded in revision-r1.md'})
for sid,t in [('S03',1.25),('S08',5.3)]:
 for version,base in [('before',P/'build/revision-r1-before'),('after',P)]:
  subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(base/f'scenes/{sid}/{sid}-pilot.mp4'),'-frames:v','1','-vf','scale=360:640',str(E/f'{sid}-comparison-{version}.png')],check=True)
(E/'timing.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('21 before/during/settled highlight screenshots and 4 comparison frames extracted')
