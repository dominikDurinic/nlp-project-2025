from helper.cleaning import clean_jsonl

## -------- Cleaning text ---------

# cleaning articles

clean_jsonl(
    "data/original/articles/24sata_articles.jsonl",
    "data/clean/articles/clean_24sata_articles.jsonl"
)

# cleaning comments
clean_jsonl(
    "data/original/comments/24sata_comments.jsonl",
    "data/clean/comments/clean_24sata_comments.jsonl"
)


# cleaning posts
clean_jsonl(
    "data/original/posts/reddit_posts.jsonl",
    "data/clean/posts/clean_reddit_posts.jsonl"
)

# cleaning posts comments
clean_jsonl(
    "data/original/posts/comments/reddit_comments.jsonl",
    "data/clean/posts/comments/clean_reddit_comments.jsonl"
)
