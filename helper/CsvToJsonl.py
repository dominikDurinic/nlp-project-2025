#import json
'''
with open("./data/train/labeled_comments.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        try:
            json.loads(line)
        except Exception as e:
            print(f"Greška u retku {i}: {e}")
            print("Problematični redak:")
            print(line)
            break


# stvaranje csv
import pandas as pd
import csv
import json
import math

# 1) Učitaj JSONL
df = pd.read_json("./data/train/clean_new.jsonl", lines=True)

# 2) Zamijeni sve NaN / <NA> s None
df = df.where(pd.notnull(df), None)

# 3) Pretvori comment_id u string
#df["comment_id"] = df["comment_id"].apply(
 #   lambda x: str(int(x)) if isinstance(x, (int, float)) and not math.isnan(x) else (str(x) if x is not None else "")
#)

# 4) Pretvori label u int (0,1,2)
#df["label"] = df["label"].apply(
 #   lambda x: int(x) if isinstance(x, (int, float)) and not math.isnan(x) else ""
#)   

# 5) Ručno spremi CSV bez automatske konverzije
with open("./data/train/clean_new.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(df.columns)
    for _, row in df.iterrows():
        writer.writerow([
            row["source"],
            row["article_url"],
            #row["comment_id"],
            row["postId"],
            row["publish_date"],
            row["clean_text"],
            #row["label"],
            #row["commentThreadId"] if row["commentThreadId"] is not None else "",
            #row["author"] if row["author"] is not None else ""
        ])





'''

import math

def to_str_id(x):
    # Ako je broj (int ili float) i nije NaN → pretvori u string
    if isinstance(x, (int, float)) and not math.isnan(x):
        return str(int(x))
    # Ako je već string → vrati ga
    if isinstance(x, str):
        return x
    # Inače (None, NaN, <NA>) → vrati None
    return None


import pandas as pd
import json

# 1) Učitaj CSV iz Excela (CP1250 + ; delimiter)
df = pd.read_csv("./data/train/opj_data.csv", encoding="utf-8", delimiter=";")

# 3) Pretvori label u int (0, 1, 2)
df["label"] = df["label"].astype("Int64")

# 4) Zamijeni sve NaN s None (što postaje null u JSON-u)
df = df.where(pd.notnull(df), None)

# 5) Spremi u JSONL
with open("./data/train/labeled_comments_2.jsonl", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        f.write(json.dumps(row.to_dict(), ensure_ascii=False) + "\n")

print("Gotovo! JSONL je generiran.")

