import os
import sys
import json
import wave
import numpy as np
from pathlib import Path

# Force UTF-8 encoding for standard outputs
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from faster_whisper import WhisperModel

AUDIO_PATH = Path(r"input_voice/du-hoc-australia-cu-5-visa-bi-tu-choi-1/Generated Audio October 11, 2026 - 11_22AM.wav")
RAW_TEXT_PATH = Path(r"input_voice/du-hoc-australia-cu-5-visa-bi-tu-choi-1/raw.txt")
OUTPUT_JSON = Path("scratch/voice_timeline.json")
OUTPUT_MD = Path("scratch/voice_timeline.md")

print(f"Loading Whisper model (base)...")
model = WhisperModel("base", device="cpu", compute_type="int8")

print(f"Reading {AUDIO_PATH}...")
with wave.open(str(AUDIO_PATH), "rb") as w:
    frames = w.readframes(w.getnframes())
    rate = w.getframerate()
    audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0

target_rate = 16000
if rate != target_rate:
    print(f"Resampling from {rate}Hz to {target_rate}Hz...")
    num_samples = int(len(audio) * target_rate / rate)
    audio_16k = np.interp(
        np.linspace(0, len(audio), num_samples, endpoint=False),
        np.arange(len(audio)),
        audio
    ).astype(np.float32)
else:
    audio_16k = audio

total_duration = len(audio_16k) / target_rate
print(f"Transcribing audio ({total_duration:.2f}s) with word timestamps...")
segments, info = model.transcribe(
    audio_16k,
    beam_size=5,
    language="vi",
    word_timestamps=True,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=500)
)

print(f"Detected language: {info.language} with probability {info.language_probability:.2f}")

raw_segments = []
for seg in segments:
    words_data = []
    if seg.words:
        for w in seg.words:
            words_data.append({
                "word": w.word.strip(),
                "start": round(w.start, 2),
                "end": round(w.end, 2),
                "probability": round(w.probability, 2)
            })
    raw_segments.append({
        "id": seg.id,
        "start": round(seg.start, 2),
        "end": round(seg.end, 2),
        "duration": round(seg.end - seg.start, 2),
        "text": seg.text.strip(),
        "words": words_data
    })

print(f"Found {len(raw_segments)} raw Whisper segments.")

# Read raw text lines
with open(RAW_TEXT_PATH, "r", encoding="utf-8") as f:
    raw_lines = [line.strip() for line in f if line.strip()]

# Save raw whisper transcription
OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open("scratch/whisper_raw.json", "w", encoding="utf-8") as f:
    json.dump({
        "total_duration": round(total_duration, 2),
        "raw_lines": raw_lines,
        "raw_segments": raw_segments
    }, f, ensure_ascii=False, indent=2)

print("Saved raw transcription to scratch/whisper_raw.json")
