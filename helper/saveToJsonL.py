import json
import os

def save_to_jsonl(data, filename):
    mode = "a" if os.path.isfile(filename) else "w"
    with open(filename, mode, encoding="utf-8") as f:
        for row in data:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
