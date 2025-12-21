import pandas as pd
from dnevnohr.dnevno_web_scraper import scrape_portal_dnevno
from helper.cleaning import clean_jsonl
from indexhr.getAllComments import get_all_comments
from indexhr.index_web_scraper import scrape_portal
from jutarnjihr.jutarnji_web_scraper import scrape_portal_jutarnji
from narodhr.narodhr_web_scraper import scrape_portal_narod
from narodhr.getAllComments import get_comments
from dva_cetiri_sata.dva_cetiri_sata_web_scraper import  scrape_portal_24sata
from dva_cetiri_sata.getComments import  get_comments_24sata
from helper.filter import exclude_sport
from reddit.getComments import get_reddit_comments
from reddit.reddit_web_scraper import scrape_portal_reddit
from helper.saveToJsonL import save_to_jsonl
from vecernjihr.getComments import get_vecernji_comments
from vecernjihr.vecernji_web_scraper import scrape_portal_vecernji

## ------- INDEX.HR -------

articles = []
articles = scrape_portal("jugoslavija", max_results=30)

articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/indexhr_articles.jsonl")

comments = []
for article in articles:
    thread_id = article.get("commentThreadId")
    if not thread_id:
        continue
    comments.extend(get_all_comments(thread_id))


save_to_jsonl(comments,"data/original/comments/indexhr_comments.jsonl")


## ------- NAROD.HR -------

articles = []
articles = scrape_portal_narod("jugoslavija", 1)

save_to_jsonl(articles, "data/original/articles/narodhr_articles.jsonl")

comments = []
for article in articles:
    t_i = article.get("t_i")
    if not t_i:
        continue
    # get_all_comments sada prima URL umjesto thread_id
    comments.extend(get_comments(t_i))

save_to_jsonl(comments, "data/original/comments/narodhr_comments.jsonl")


## ------- DNEVNO.HR -------

articles = []
articles = scrape_portal_dnevno("jugoslavija", 2)

articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/dnevnohr_articles.jsonl")



## ------- 24SATA.HR -------

articles = scrape_portal_24sata("jugoslavija", 2)
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/24sata_articles.jsonl")

comments = []
for article in articles:
    url = article.get("url")
    if not url:
        continue

    comments.extend(get_comments_24sata(url))

save_to_jsonl(comments, "data/original/comments/24sata_comments.jsonl")



## ------- JUTARNJI.HR -------

articles = scrape_portal_jutarnji("jugoslavija", 2)
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/jutarnjihr_articles.jsonl")


## ------- VECERNJI.HR -------

articles = scrape_portal_vecernji("jugoslavija", 1)
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/vecernjihr_articles.jsonl")

comments = []
for article in articles:
    url = article.get("url")
    if not url:
        continue

    comments.extend(get_vecernji_comments(url))

save_to_jsonl(comments, "data/original/comments/vecernjihr_comments.jsonl")


## ------- REDDIT.COM -------

posts = articles = scrape_portal_reddit("jugoslavija", max_pages=1)

save_to_jsonl(posts, "data/original/posts/reddit_posts.jsonl")

comments = []
for post in posts:
    url = post.get("url")
    post_id = post.get("id")
    if not url:
        continue

    comments.extend(get_reddit_comments(url, post_id))

save_to_jsonl(comments, "data/original/posts/comments/reddit_comments.jsonl")


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