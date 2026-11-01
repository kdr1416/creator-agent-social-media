import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("scratch/whisper_raw.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print(f"Total Duration: {d['total_duration']}s\n")
for s in d['raw_segments']:
    print(f"{s['id']:02d} [{s['start']:6.2f} - {s['end']:6.2f}] ({s['duration']:4.2f}s): {s['text']}")
