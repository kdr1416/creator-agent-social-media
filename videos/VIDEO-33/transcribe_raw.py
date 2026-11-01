import json
import os
import sys
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8")

audio_path = "videos/VIDEO-33/inputs/source_audio.wav"
print(f"Loading faster-whisper model (small) on CPU...")
model = WhisperModel("small", device="cpu", compute_type="int8")

print(f"Transcribing {audio_path}...")
segments, info = model.transcribe(
    audio_path,
    language="vi",
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=400),
    word_timestamps=True
)

raw_segments = []
full_raw_text = []

for seg in segments:
    words = []
    if seg.words:
        for w in seg.words:
            words.append({
                "word": w.word,
                "start": round(w.start, 3),
                "end": round(w.end, 3),
                "probability": round(w.probability, 3)
            })
    seg_dict = {
        "id": seg.id,
        "start": round(seg.start, 3),
        "end": round(seg.end, 3),
        "text": seg.text.strip(),
        "words": words
    }
    raw_segments.append(seg_dict)
    full_raw_text.append(seg.text.strip())
    print(f"[{seg.start:6.2f}s -> {seg.end:6.2f}s] {seg.text.strip()}")

output_json = "videos/VIDEO-33/whisper_raw.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump({
        "duration": info.duration,
        "language": info.language,
        "language_probability": info.language_probability,
        "segments": raw_segments
    }, f, ensure_ascii=False, indent=2)

print(f"\nTranscribed {len(raw_segments)} segments. Audio duration: {info.duration:.2f}s")
print(f"Saved raw transcription to {output_json}")
