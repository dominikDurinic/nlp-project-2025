import json
import random

with open("./data/train/jugoslavija_final_cleaned.jsonl", "r", encoding="utf-8") as f:
    lines = [json.loads(line) for line in f]

random.shuffle(lines)

with open("./data/train/jugoslavija_final_cleaned_shuffled.jsonl", "w", encoding="utf-8") as f:
    for item in lines:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
