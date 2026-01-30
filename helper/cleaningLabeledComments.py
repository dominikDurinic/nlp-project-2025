import json
import random
from collections import Counter

def sanitize_dataset(input_file, output_file, max_char_length=280):
    data = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line)
            # Čistimo tekst od suvišnih razmaka
            text = " ".join(item['clean_text'].split())
            
            # KRITERIJ 1: Duljina. Predugački komentari zbunjuju model (overfitting na detalje)
            if len(text) <= max_char_length:
                item['clean_text'] = text
                data.append(item)

    # Brojimo koliko imamo nakon filtriranja duljine
    stats = Counter(item['label'] for item in data)
    print(f"Nakon filtriranja duljine: {stats}")
    
    # KRITERIJ 2: Balansiranje na najmanju klasu
    min_count = min(stats.values())
    
    final_data = []
    for label in stats.keys():
        subset = [item for item in data if item['label'] == label]
        final_data.extend(random.sample(subset, min_count))
        
    # KRITERIJ 3: Shuffle
    random.shuffle(final_data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in final_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            
    print(f"\n✅ REZULTAT: Svaka klasa sada ima točno {min_count} KRATKIH i JASNIH primjera.")
    print(f"Ukupno u datasetu: {len(final_data)}")

# Pokreni skriptu
sanitize_dataset('./data/train/jugoslavija_only.jsonl', './data/train/jugoslavija_super_clean.jsonl')