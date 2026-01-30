from helper.cleaning import clean_jsonl

## -------- Cleaning text ---------

# cleaning articles - 24sata
clean_jsonl(
    "data/original/articles/24sata_articles.jsonl",
    "data/clean/articles/clean_24sata_articles.jsonl"
)

# cleaning comments
clean_jsonl(
    "data/original/comments/24sata_comments.jsonl",
    "data/clean/comments/clean_24sata_comments.jsonl"
)

# cleaning articles - dnevnohr
clean_jsonl(
    "data/original/articles/dnevnohr_articles.jsonl",
    "data/clean/articles/clean_dnevnohr_articles.jsonl"
)

# cleaning articles - indexhr
clean_jsonl(
    "data/original/articles/indexhr_articles.jsonl",
    "data/clean/articles/clean_indexhr_articles.jsonl"
)

# cleaning comments
clean_jsonl(
    "data/original/comments/indexhr_comments.jsonl",
    "data/clean/comments/clean_indexhr_comments.jsonl"
)

# cleaning articles - jutarnjihr
clean_jsonl(
    "data/original/articles/jutarnjihr_articles.jsonl",
    "data/clean/articles/clean_jutarnjihr_articles.jsonl"
)

# cleaning articles - narodhr
clean_jsonl(
    "data/original/articles/narodhr_articles.jsonl",
    "data/clean/articles/clean_narodhr_articles.jsonl"
)

# cleaning comments
clean_jsonl(
    "data/original/comments/narodhr_comments.jsonl",
    "data/clean/comments/clean_narodhr_comments.jsonl"
)

# cleaning articles - vecernjihr
clean_jsonl(
    "data/original/articles/vecernjihr_articles.jsonl",
    "data/clean/articles/clean_vecernjihr_articles.jsonl"
)

# cleaning comments
clean_jsonl(
    "data/original/comments/vecernjihr_comments.jsonl",
    "data/clean/comments/clean_vecernjihr_comments.jsonl"
)






# cleaning posts - reddit
clean_jsonl(
    "data/original/posts/reddit_posts_AskCroatia.jsonl",
    "data/clean/posts/clean_reddit_posts_AskCroatia.jsonl"
)



# cleaning posts comments
clean_jsonl(
    "data/original/posts/comments/reddit_comments_AskCroatia.jsonl",
    "data/clean/posts/comments/clean_reddit_comments_AskCroatia.jsonl"
)

# cleaning posts - reddit
clean_jsonl(
    "data/original/posts/reddit_posts_Croatia.jsonl",
    "data/clean/posts/clean_reddit_posts_Croatia.jsonl"
)



# cleaning posts comments
clean_jsonl(
    "data/original/posts/comments/reddit_comments_Croatia.jsonl",
    "data/clean/posts/comments/clean_reddit_comments_Croatia.jsonl"
)


# cleaning posts - reddit
clean_jsonl(
    "data/original/posts/reddit_posts_hreddit.jsonl",
    "data/clean/posts/clean_reddit_posts_hreddit.jsonl"
)



# cleaning posts comments
clean_jsonl(
    "data/original/posts/comments/reddit_comments_hreddit.jsonl",
    "data/clean/posts/comments/clean_reddit_comments_hreddit.jsonl"
)
