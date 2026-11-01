import wave
import numpy as np
import sys

sys.stdout.reconfigure(encoding="utf-8")

audio_path = "videos/VIDEO-33/inputs/source_audio.wav"
with wave.open(audio_path, "rb") as w:
    sr = w.getframerate()
    frames = w.getnframes()
    pcm = w.readframes(frames)

data = np.frombuffer(pcm, dtype=np.int16)

window_size = int(sr * 0.05) # 50ms
hop_size = int(sr * 0.025)   # 25ms

rms_list = []
times = []
for i in range(0, len(data) - window_size, hop_size):
    chunk = data[i:i+window_size]
    rms = np.sqrt(np.mean(chunk.astype(float)**2))
    rms_list.append(rms)
    times.append(i / sr)

rms_arr = np.array(rms_list)
times_arr = np.array(times)

# Print valleys where RMS < 500 (silence/pause)
silence_mask = rms_arr < 500

# Group contiguous silence intervals
silences = []
in_silence = False
start_t = 0.0
for t, s in zip(times_arr, silence_mask):
    if s and not in_silence:
        in_silence = True
        start_t = t
    elif not s and in_silence:
        in_silence = False
        if (t - start_t) >= 0.15: # at least 150ms
            silences.append((start_t, t, t - start_t))
if in_silence and (times_arr[-1] - start_t) >= 0.15:
    silences.append((start_t, times_arr[-1], times_arr[-1] - start_t))

print(f"Detected {len(silences)} significant silence intervals (duration >= 150ms):")
for idx, (st, en, dur) in enumerate(silences, 1):
    # Find minimum RMS point inside silence
    s_idx = int(st * sr)
    e_idx = int(en * sr)
    sub = np.abs(data[s_idx:e_idx])
    min_pt = s_idx + np.argmin(sub)
    print(f"Silence {idx:2d}: {st:6.3f}s -> {en:6.3f}s (dur: {dur:5.3f}s) | mid: {(st+en)/2:6.3f}s | min_sample: {min_pt} ({(min_pt/sr):.3f}s)")
