from datasets import Dataset
import json

# ucitavanje rucno označenih podataka iz JSONL datoteke
def load_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            data.append({
                "text": obj["clean_text"],
                "label": obj["label"],  # 0=nostalgija, 1=kritika, 2=neutralno

                # META PODACI (ne koriste se u treningu, ali ih nosimo sa sobom)
                "source": obj.get("source"),
                "publish_date": obj.get("publish_date"),
                "article_url": obj.get("article_url"),
            })
    return Dataset.from_list(data)

