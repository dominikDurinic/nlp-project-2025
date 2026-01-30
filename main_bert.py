from bert_classifier.bertProduction import label_jsonl_with_metrics

# labeling clanaka

label_jsonl_with_metrics(
    "data/result/articles/all_articles_to_predict.jsonl",
    "data/result/articles/results_labeled_articles.jsonl"
)


# labeling komentara
label_jsonl_with_metrics(
    "data/result/comments/all_comments_to_predict.jsonl",
    "data/result/comments/results_labeled_comments.jsonl"
)

