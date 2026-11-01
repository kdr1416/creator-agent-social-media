import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("scratch/whisper_raw.json", "r", encoding="utf-8") as f:
    d = json.load(f)

raw_lines = d["raw_lines"]
raw_segs = d["raw_segments"]

print(f"Total lines in raw.txt: {len(raw_lines)}")
print(f"Total segments from Whisper: {len(raw_segs)}")

# Let's inspect each line and matching whisper segment
for i, line in enumerate(raw_lines):
    print(f"L{i+1:02d}: {line}")
