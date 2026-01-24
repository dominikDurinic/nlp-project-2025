import json
import random

with open("./data/train/labeled_comments.jsonl", "r", encoding="utf-8") as f:
    lines = [json.loads(line) for line in f]

random.shuffle(lines)

with open("./data/train/labeled_comments_shuffled.jsonl", "w", encoding="utf-8") as f:
    for item in lines:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
