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
'''
## index.hr

articles = []
articles = scrape_portal("jugoslavija", max_results=30)

articles = exclude_sport(articles)


save_to_jsonl(articles, "indexhr_articles.jsonl")

comments = []
for article in articles:
    thread_id = article.get("commentThreadId")
    if not thread_id:
        continue
    comments.extend(get_all_comments(thread_id))


save_to_jsonl(comments,"indexhr_comments.jsonl")


## narod.hr

articles = []
articles = scrape_portal_narod("jugoslavija", 1)

save_to_jsonl(articles, "narodhr_articles.jsonl")

comments = []
for article in articles:
    t_i = article.get("t_i")
    if not t_i:
        continue
    # get_all_comments sada prima URL umjesto thread_id
    comments.extend(get_comments(t_i))

save_to_jsonl(comments, "narodhr_comments.jsonl")


## dnevno.hr

articles = []
articles = scrape_portal_dnevno("jugoslavija", 2)

articles = exclude_sport(articles)

save_to_jsonl(articles, "dnevnohr_articles.jsonl")


## jutarnji.hr

articles = []
articles = scrape_portal_jutarnji("jugoslavija", 2)

articles = exclude_sport(articles)

save_to_jsonl(articles, "jutarnjihr_articles.jsonl")
'''

## 24sata.hr

articles = scrape_portal_24sata("jugoslavija")
articles = exclude_sport(articles)

save_to_jsonl(articles, "24sata_articles.jsonl")

comments = []
for article in articles:
    url = article.get("url")
    if not url:
        continue

    comments.extend(get_comments_24sata(url))

save_to_jsonl(comments, "24sata_comments.jsonl")
