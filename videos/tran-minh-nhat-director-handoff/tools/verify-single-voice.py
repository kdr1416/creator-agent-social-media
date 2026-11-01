"""Verify a picture+voice export and produce review sheets; requires PyAV, NumPy, Pillow."""
import argparse
import hashlib
import json
from pathlib import Path
import wave

import av
import numpy as np
from PIL import Image, ImageDraw, ImageOps


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--video', type=Path, required=True)
    parser.add_argument('--voice', type=Path, required=True)
    parser.add_argument('--source-root', type=Path)
    parser.add_argument('--source-manifest', type=Path)
    parser.add_argument('--proof-times', default='0.7,1.7,2.8,3.8,5.4,8.8,10.2,11.7,13.7')
    args = parser.parse_args()
    root = args.project.resolve()
    qa = root / 'qa'
    qa.mkdir(exist_ok=True)
    before = {}
    changed = []
    if args.source_manifest:
        before = json.loads(args.source_manifest.read_text(encoding='utf-8-sig'))
        base = args.source_root or Path.cwd()
        changed = [p for p, h in before.items() if hashlib.sha256((base / p).read_bytes()).hexdigest() != h]
        if changed:
            raise RuntimeError('Source files changed: ' + ', '.join(changed))
    with wave.open(str(args.voice), 'rb') as audio:
        if audio.getsampwidth() != 2 or audio.getnchannels() != 1:
            raise ValueError('This verifier expects supplied mono PCM16 narration.')
        rate = audio.getframerate()
        original = audio.readframes(audio.getnframes())
        source_duration = audio.getnframes() / rate
    decoded_parts = []
    with av.open(str(args.video)) as media:
        audio_stream = media.streams.audio[0]
        audio_codec = audio_stream.codec_context.name
        audio_duration = float(audio_stream.duration * audio_stream.time_base)
        resampler = av.AudioResampler(format='s16', layout='mono', rate=rate)
        for frame in media.decode(audio=0):
            decoded_parts.extend(f.to_ndarray().reshape(-1) for f in resampler.resample(frame))
        decoded_parts.extend(f.to_ndarray().reshape(-1) for f in resampler.resample(None))
    a = np.frombuffer(original, np.int16).astype(float) / 32768
    b = np.concatenate(decoded_parts).astype(float) / 32768
    n = min(len(a), len(b))
    correlation = float(np.corrcoef(a[:n], b[:n])[0, 1])
    rms = float(np.sqrt(np.mean(b*b)))
    if correlation < .98 or rms < .001:
        raise RuntimeError(f'Audio integrity failed: correlation={correlation:.6f}, rms={rms:.6f}')
    times = [float(t) for t in args.proof_times.split(',')]
    cols = min(3, len(times))
    rows = (len(times) + cols - 1) // cols
    sheet = Image.new('RGB', (cols*360, rows*670), '#493D36')
    draw = ImageDraw.Draw(sheet)
    frames = []
    index = 0
    with av.open(str(args.video)) as media:
        video = media.streams.video[0]
        video_duration = float(video.duration * video.time_base)
        video_info = {'path':str(args.video), 'codec':video.codec_context.name,
                      'width':video.width, 'height':video.height,
                      'fps':str(video.average_rate), 'duration':video_duration, 'frames':video.frames}
        if (video.width,video.height) != (720,1280):
            raise RuntimeError('This style trial expects a 720x1280 canvas.')
        if abs(video_duration-source_duration) > .05:
            raise RuntimeError('Video duration differs from voice by more than 0.05s.')
        for frame in media.decode(video=0):
            if index == len(times):
                break
            if float(frame.time) < times[index]:
                continue
            im = frame.to_image()
            frames.append(im.copy())
            mobile = im.resize((360,640))
            mobile.save(qa / f'mobile-{index}.png')
            sheet.paste(mobile,(index%cols*360,index//cols*670+30))
            draw.text((index%cols*360+12,index//cols*670+8),f'{times[index]:.2f}s',fill='#F8EFDE')
            index += 1
    if index != len(times):
        raise RuntimeError('Some proof times exceed the rendered duration.')
    sheet.save(qa/'final-contact-sheet.jpg',quality=92)
    chosen = [min(i,len(frames)-1) for i in (2,5,8)]
    hero = Image.new('RGB',(1080,640),'#F8EFDE')
    thumbnail = Image.new('L',(360,214),240)
    for i,k in enumerate(chosen):
        hero.paste(frames[k].resize((360,640)),(i*360,0))
        thumbnail.paste(ImageOps.grayscale(frames[k]).resize((120,214)),(i*120,0))
    hero.save(qa/'style-preview.jpg',quality=94)
    thumbnail.save(qa/'grayscale-thumbnail.png')
    report = {'source_files_checked':len(before),'source_files_changed':changed,
              'video':video_info,'audio':{'codec':audio_codec,'duration':audio_duration,
              'source_duration':source_duration,'source_sample_rate':rate,
              'decoded_correlation_with_source':correlation,'original_rms':float(np.sqrt(np.mean(a*a))),
              'decoded_rms':rms,'decoded_peak':float(np.max(np.abs(b))),
              'clipped_samples':int(np.sum(np.abs(b)>=.999))},
              'proof_times':times,'user_approval':'pending'}
    check_path = qa/'final-check.json'
    if check_path.exists():
        check = json.loads(check_path.read_text(encoding='utf-8-sig'))
        report['check'] = {'ok':check['ok'],**{k:{'errors':check[k].get('errorCount'),
                  'warnings':check[k].get('warningCount')} for k in ('lint','runtime','layout','contrast')},
                  'contrast_checked':check['contrast']['checked'],'contrast_passed':check['contrast']['passed']}
    (qa/'review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
