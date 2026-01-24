import json
import re
import emoji
from tqdm import tqdm

# hrvatske stop riječi (možeš proširiti)
STOPWORDS = {
    "i","u","na","za","da","je","sam","si","su","smo","ste",
    "a","ali","pa","te","to","tu","ti","mi","vi","oni","one","ono","od","do",
    "kao","koji","koja","koje","koju","što","šta","jer","bez","s","sa","ovo",
    "tamo","ovdje","biti","imam","ima","imaju","bilo","bila","bili","bile"
}

def clean_text(text: str) -> str:
    if not text:
        return ""

    # lower
    text = text.lower()

    # ukloni URL-ove
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # ukloni emoji
    text = emoji.replace_emoji(text, replace="")

    # ukloni sve što nije slovo ili razmak
    text = re.sub(r"[^a-zA-ZčćžšđČĆŽŠĐ ]", " ", text)

    # tokenizacija
    tokens = text.split()

    # ukloni stop riječi i prekratke riječi
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]

    return " ".join(tokens)


def clean_jsonl(input_path: str, output_path: str):
    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:

        for line in tqdm(infile, desc=f"Cleaning {input_path}"):
            obj = json.loads(line)

            # novi objekt koji ide u clean datoteku
            new_obj = {}

            # kopiraj sve meta podatke osim title/text
            for key, value in obj.items():
                if key not in ("title", "text"):
                    new_obj[key] = value

            # ako postoji title → očisti ga
            if "title" in obj:
                new_obj["clean_title"] = clean_text(obj.get("title", ""))

            # text postoji i u articles i u comments
            new_obj["clean_text"] = clean_text(obj.get("text", ""))

            outfile.write(json.dumps(new_obj, ensure_ascii=False) + "\n")
