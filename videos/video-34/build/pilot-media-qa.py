"""Read-only FFprobe, exact PCM excerpt and AAC alignment checks for two pilots."""
from pathlib import Path
import json,subprocess,wave,hashlib,sys
sys.stdout.reconfigure(encoding='utf-8')
P=Path(__file__).resolve().parents[1];E=P/'build/pilot-evidence'
config=json.loads((P/'build/pilot-working-config.json').read_text(encoding='utf-8'))
manifest=json.loads((P/'project_manifest.json').read_text(encoding='utf-8-sig'))
master=P/manifest['audio']['path']
result={'master_sha256':hashlib.sha256(master.read_bytes()).hexdigest(),'scenes':{},'sync_claim':'Exact PCM sample slicing verified separately; encoded A/V is quantized to 30 FPS, not sample-exact audiovisual synchronization.'}
assert result['master_sha256']==manifest['audio']['sha256']
try:
 import numpy as np
except ImportError:
 np=None
for sid,c in config['scenes'].items():
 f=P/c['review_output']
 command=['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(f)]
 info=json.loads(subprocess.check_output(command));(E/f'{sid}-ffprobe.json').write_text(json.dumps(info,indent=2),encoding='utf-8')
 video=next(s for s in info['streams'] if s['codec_type']=='video');audio=next(s for s in info['streams'] if s['codec_type']=='audio')
 with wave.open(str(master),'rb') as w:
  w.setpos(c['start_sample']);original=w.readframes(c['audio_samples'])
 with wave.open(str(P/f'scenes/{sid}/voice-excerpt.wav'),'rb') as w:
  pcm=w.readframes(w.getnframes());sr=w.getframerate();count=w.getnframes()
 checks={'dimensions':(video['width'],video['height'])==(1080,1920),'fps':video['avg_frame_rate']=='30/1','frame_count':int(video['nb_read_frames'])==c['frames'],'pcm_excerpt_byte_exact':pcm==original,'pcm_24000hz':sr==24000,'pcm_sample_count':count==c['audio_samples'],'aac_24000hz_mono':audio['sample_rate']=='24000' and audio['channels']==1,'av_duration_within_one_frame':abs(float(video['duration'])-float(audio['duration']))<=1/30}
 alignment={'status':'NOT TESTED','reason':'numpy unavailable'}
 if np is not None:
  decoded=subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-map','0:a:0','-f','f32le','-acodec','pcm_f32le','-ar','24000','-ac','1','pipe:1'])
  x=np.frombuffer(original,dtype='<i2').astype(np.float64)/32768;y=np.frombuffer(decoded,dtype='<f4').astype(np.float64)
  n=1<<(len(x)+len(y)-1).bit_length();corr=np.fft.irfft(np.fft.rfft(y,n)*np.conj(np.fft.rfft(x,n)),n)
  lags=np.arange(-800,801);lag=int(lags[np.argmax(corr[lags%n])]);count=min(len(x),len(y));pearson=float(np.corrcoef(x[:count],y[:count])[0,1])
  alignment={'status':'MEASURED','decoded_audio_samples':len(y),'aac_vs_pcm_peak_lag_samples':lag,'peak_lag_ms':lag/24,'search_window_samples':[-800,800],'zero_lag_pearson':pearson,'note':'AAC padding may extend decoded PCM. This measures encoded speech waveform alignment, not perceptual visual timing.'}
  checks['encoded_speech_lag_under_1ms']=abs(lag)<=24
 result['scenes'][sid]={'checks':checks,'picture_duration':float(video['duration']),'audio_track_duration':float(audio['duration']),'container_duration':float(info['format']['duration']),'picture_minus_original_audio_ms':(float(video['duration'])-c['audio_duration'])*1000,'audio_alignment':alignment,'file_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'ffprobe_command':command}
(E/'media-qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
assert all(all(s['checks'].values()) for s in result['scenes'].values())
