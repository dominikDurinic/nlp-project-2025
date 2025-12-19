import pandas as pd
from dnevnohr.dnevno_web_scraper import scrape_portal_dnevno
from indexhr.getAllComments import get_all_comments
from indexhr.index_web_scraper import scrape_portal
from jutarnjihr.jutarnji_web_scraper import scrape_portal_jutarnji
from narodhr.narodhr_web_scraper import scrape_portal_narod
from narodhr.getAllComments import get_comments
from dva_cetiri_sata.dva_cetiri_sata_web_scraper import  scrape_portal_24sata
from dva_cetiri_sata.getComments import  get_comments_24sata
from filter import exclude_sport
from saveToJsonL import save_to_jsonl
from vecernjihr.getComments import get_vecernji_comments
from vecernjihr.vecernji_web_scraper import scrape_portal_vecernji
'''
## index.hr

articles = []
articles = scrape_portal("jugoslavija", max_results=30)

articles = exclude_sport(articles)


save_to_jsonl(articles, "data/articles/indexhr_articles.jsonl")

comments = []
for article in articles:
    thread_id = article.get("commentThreadId")
    if not thread_id:
        continue
    comments.extend(get_all_comments(thread_id))


save_to_jsonl(comments,"data/comments/indexhr_comments.jsonl")


## narod.hr

articles = []
articles = scrape_portal_narod("jugoslavija", 1)

save_to_jsonl(articles, "data/articles/narodhr_articles.jsonl")

comments = []
for article in articles:
    t_i = article.get("t_i")
    if not t_i:
        continue
    # get_all_comments sada prima URL umjesto thread_id
    comments.extend(get_comments(t_i))

save_to_jsonl(comments, "data/comments/narodhr_comments.jsonl")


## dnevno.hr

articles = []
articles = scrape_portal_dnevno("jugoslavija", 2)

articles = exclude_sport(articles)

save_to_jsonl(articles, "data/articles/dnevnohr_articles.jsonl")

'''

## 24sata.hr

articles = scrape_portal_24sata("jugoslavija", 2)
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/articles/24sata_articles.jsonl")

comments = []
for article in articles:
    url = article.get("url")
    if not url:
        continue

    comments.extend(get_comments_24sata(url))

save_to_jsonl(comments, "data/comments/24sata_comments.jsonl")

'''

## jutarnji.hr

articles = scrape_portal_jutarnji("jugoslavija", 2)
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/articles/jutarnjihr_articles.jsonl")


## vecernji.hr

articles = scrape_portal_vecernji("jugoslavija", 1)
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/articles/vecernjihr_articles.jsonl")

comments = []
for article in articles:
    url = article.get("url")
    if not url:
        continue

    comments.extend(get_vecernji_comments(url))

save_to_jsonl(comments, "data/comments/vecernjihr_comments.jsonl")
'''