import json
from tqdm import tqdm

def load_ids(txt_path):
    """Učitaj ID-eve iz txt datoteke, svaki u svom redu."""
    with open(txt_path, "r", encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

def filter_jsonl_by_ids(jsonl_path, ids_set, output_path):
    """Filtriraj JSONL prema comment_id i spremi rezultat."""
    with open(jsonl_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:

        for line in tqdm(infile, desc="Filtering JSONL"):
            obj = json.loads(line)

            # comment_id može biti broj ili string → pretvori u string
            cid = str(obj.get("author")).strip()

            # prolazi kroz sve ID-eve iz txt
            for tid in ids_set:
                tid = tid.strip()


                # ako je TXT ID duži → odreži ga na duljinu JSONL ID-a
                #if len(tid) > len(cid):
                #    tid = tid[:len(cid)]

                # ako se poklapaju → spremi
                if cid == tid:
                    outfile.write(json.dumps(obj, ensure_ascii=False) + "\n")
                    break

# -----------------------------
# KORIŠTENJE
# -----------------------------

ids = load_ids("./data/train/ids.txt")  # txt s ID-evima
filter_jsonl_by_ids(
    jsonl_path="./data/clean/comments/clean_narodhr_comments.jsonl",
    ids_set=ids,
    output_path="./data/train/filtrirani_komentari.jsonl"
)
