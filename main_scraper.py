import pandas as pd
from dnevnohr.dnevno_web_scraper import scrape_portal_dnevno
from helper.createDriver import create_driver
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
'''
## ------- INDEX.HR -------

articles = []
articles = scrape_portal("jugoslavija", max_results=100)

articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/indexhr_articles.jsonl")

comments = []
for article in articles:
    thread_id = article.get("commentThreadId")
    article_url = article.get("article_url")
    if not thread_id:
        continue
    comments.extend(get_all_comments(thread_id, article_url))
    print(f"Prikupljeno komentara za članak {article_url}: {len(comments)}")


save_to_jsonl(comments,"data/original/comments/indexhr_comments.jsonl")


## ------- NAROD.HR -------

articles = []
articles = scrape_portal_narod("jugoslavija", 1)

save_to_jsonl(articles, "data/original/articles/narodhr_articles.jsonl")

comments = []
for article in articles:
    t_i = article.get("t_i")
    article_url = article.get("article_url")
    if not t_i:
        continue
    # get_all_comments sada prima URL umjesto thread_id
    comments.extend(get_comments(t_i,article_url=article_url))

save_to_jsonl(comments, "data/original/comments/narodhr_comments.jsonl")


## ------- DNEVNO.HR -------

articles = []
articles = scrape_portal_dnevno("jugoslavija", 14)

articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/dnevnohr_articles.jsonl")


'''
## ------- 24SATA.HR -------

articles = scrape_portal_24sata("jugoslavija", scroll_times=1)
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/24sata_articles.jsonl")

driver = create_driver()

comments = []
for article in articles:
    url = article.get("article_url")
    if not url:
        continue

    comments.extend(get_comments_24sata(url, driver))
    print(f"Prikupljeno komentara za članak {url}: {len(comments)}")

driver.quit()
save_to_jsonl(comments, "data/original/comments/24sata_comments.jsonl")


'''
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
    url = article.get("article_url")
    if not url:
        continue

    comments.extend(get_vecernji_comments(url))

save_to_jsonl(comments, "data/original/comments/vecernjihr_comments.jsonl")


## ------- REDDIT.COM -------

posts = articles = scrape_portal_reddit("jugoslavija", max_pages=1)

save_to_jsonl(posts, "data/original/posts/reddit_posts.jsonl")

comments = []
for post in posts:
    url = post.get("article_url")
    post_id = post.get("id")
    if not url:
        continue

    comments.extend(get_reddit_comments(url, post_id))

save_to_jsonl(comments, "data/original/posts/comments/reddit_comments.jsonl")

'''