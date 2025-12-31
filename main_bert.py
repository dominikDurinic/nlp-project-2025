from bert_classifier.labelJSONL import label_jsonl

# LABELING POSTOVA
label_jsonl(
    "data/clean/articles/clean_vecernjihr_articles.jsonl",
    "data/result/labeled_vecernjihr_articles.jsonl"
)


# LABELING KOMENTARA
label_jsonl(
    "data/clean/comments/clean_vecernjihr_comments.jsonl",
    "data/result/labeled_vecernjihr_comments.jsonl"
)