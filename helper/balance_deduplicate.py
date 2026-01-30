import json
from collections import Counter

def clean_and_balance_dataset(input_file, output_file):
    unique_texts = set()
    cleaned_data = []
    
    print(f"--- Započinjem čišćenje datoteke: {input_file} ---")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                item = json.loads(line)
                text = item['clean_text'].strip()
                
                # Provjera duplikata na temelju teksta
                if text not in unique_texts:
                    unique_texts.add(text)
                    cleaned_data.append(item)
            except Exception as e:
                continue

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in cleaned_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    '''
    # Brojanje stanja nakon čišćenja
    stats = Counter(item['label'] for item in cleaned_data)
    
    print(f"Uklonjeno duplikata: {total_before - len(cleaned_data) if 'total_before' in locals() else 'nepoznato'}")

    print("\n--- TRENUTNO STANJE (Nakon čišćenja) ---")
    names = {0: "Nostalgija", 1: "Kritika", 2: "Neutralno"}
    for label, count in sorted(stats.items()):
        print(f"Label {label} ({names.get(label, 'Nepoznato')}): {count} primjera")

    # Spremanje očišćenog fajla
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in cleaned_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            
    print(f"\n✅ Očišćeni dataset spremljen u: {output_file}")
'''
# Pokreni skriptu
clean_and_balance_dataset('./data/clean/posts/clean_reddit_posts_hreddit.jsonl', './data/clean/posts/clean_reddit_posts_hreddit_deduplicated.jsonl')