import json
import time
from collections import Counter

from bert_classifier.predictLabel import predict_label

def label_jsonl_with_metrics(input_path, output_path):
    start_time = time.time()
    total_samples = 0

    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:

        for line in infile:
            obj = json.loads(line)
            clean_text = obj.get("clean_text", "")
            
            # predikcija - poziv naseg modela
            pred = predict_label(clean_text)
            
            total_samples += 1

            new_obj = {**obj, "pred_label": pred} 
            outfile.write(json.dumps(new_obj, ensure_ascii=False) + "\n")

    end_time = time.time()
    total_duration = end_time - start_time
    
    # ispis metrike
    print(f"--- INFERENCE IZVJEŠTAJ ---")
    print(f"Obrađeno primjera: {total_samples}")
    print(f"Ukupno vrijeme: {total_duration:.2f} s")
    print(f"Prosječno po rečenici (Latency): {(total_duration/total_samples)*1000:.2f} ms")
    print(f"Rečenica po sekundi (Throughput): {total_samples/total_duration:.2f} r/s")
    