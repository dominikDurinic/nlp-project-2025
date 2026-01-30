import json

KEYWORDS = [
    "jugoslav", "jugoslavija", "jugoslaveni", "jugoslavensko", "jugoslavenski",
    "sfrj", "sfry", "juga", "yu", "yugo",
    "tito", "titov", "komunist", "komunizam",
    "komunjara", "komunjare", "komunjari", "komunjarsk",
    "partizan", "partizani", "udba", "udbaš", "udbaši",
    "jugonostal", "prije u jugi", "prije u jugoslaviji", "u jugi", "u jugoslaviji"
]

def mentions_jugoslavija(text):
    text_lower = text.lower()
    return any(kw in text_lower for kw in KEYWORDS)

def filter_jsonl(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:

        for line in infile:
            obj = json.loads(line)
            text = obj.get("clean_text", "")

            if mentions_jugoslavija(text):
                outfile.write(json.dumps(obj, ensure_ascii=False) + "\n")

# primjer poziva
filter_jsonl(
    "./data/clean/posts/clean_reddit_posts_AskCroatia.jsonl",
    "./data/jugo_only/comments/jugoslavija_only_clean_AskCroatia_posts.jsonl"
)

filter_jsonl(
    "./data/clean/posts/clean_reddit_posts_Croatia.jsonl",
    "./data/jugo_only/comments/jugoslavija_only_clean_Croatia_posts.jsonl"
)
filter_jsonl(
    "./data/clean/posts/clean_reddit_posts_hreddit.jsonl",
    "./data/jugo_only/comments/jugoslavija_only_clean_hreddit_posts.jsonl"
)