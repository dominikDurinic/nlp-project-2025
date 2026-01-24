import json
from bert_classifier.predictLabel import predict_label


# obrada cijele JSONL datoteke, dodavanje predikcija i spremanje u novu JSONL datoteku
def label_jsonl(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:

        for line in infile:
            obj = json.loads(line)

            clean_text = obj.get("clean_text", "")
            pred = predict_label(clean_text)

            # ZADRŽI META PODATKE + CLEAN TEXT + PRED LABEL
            new_obj = {
                "source": obj.get("source"),
                "publish_date": obj.get("publish_date"),
                "article_url": obj.get("article_url"),
                "clean_text": clean_text,
                "pred_label": pred
            }

            outfile.write(json.dumps(new_obj, ensure_ascii=False) + "\n")
