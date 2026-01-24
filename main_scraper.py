'''
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
'''
from reddit.getComments import get_reddit_comments
from helper.saveToJsonL import append_to_jsonl, save_to_jsonl
'''
from reddit.reddit_web_scraper import scrape_portal_reddit
from helper.saveToJsonL import append_to_jsonl, save_to_jsonl
from vecernjihr.getComments import get_vecernji_comments
from vecernjihr.vecernji_web_scraper import scrape_portal_vecernji
'''
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
articles = scrape_portal_narod("jugoslavija", 10)

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



## ------- JUTARNJI.HR -------

articles = scrape_portal_jutarnji("jugoslavija", 10)
articles.extend(scrape_portal_jutarnji("tito", 10))
articles.extend(scrape_portal_jutarnji("jugonostalgija", 10))
articles = exclude_sport(articles)

save_to_jsonl(articles, "data/original/articles/jutarnjihr_articles.jsonl")


## ------- VECERNJI.HR -------

articles = scrape_portal_vecernji("jugoslavija", 10)
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

# subreddits: Croatia, AskCroatia, hreddit    
#posts = scrape_portal_reddit("jugoslavija", max_pages=3, sub="Croatia")

#posts = scrape_portal_reddit("jugoslavija", max_pages=3, sub="AskCroatia")
#posts = scrape_portal_reddit("komunjare", max_pages=3, sub="AskCroatia")
#posts = scrape_portal_reddit("juga", max_pages=3, sub="AskCroatia")

#posts = scrape_portal_reddit("jugoslavija", max_pages=3, sub="hreddit")
#posts = scrape_portal_reddit("život+u+jugoslaviji", max_pages=3, sub="hreddit")

#save_to_jsonl(posts, "data/original/posts/reddit_posts_Croatia.jsonl")
#save_to_jsonl(posts, "data/original/posts/reddit_posts_AskCroatia.jsonl")
#save_to_jsonl(posts, "data/original/posts/reddit_posts_hreddit.jsonl")

#append_to_jsonl("data/original/posts/reddit_posts_Croatia.jsonl", posts)
#append_to_jsonl("data/original/posts/reddit_posts_AskCroatia.jsonl", posts)
#append_to_jsonl("data/original/posts/reddit_posts_hreddit.jsonl", posts)

comments = []
for post in posts:
    url = post.get("article_url")
    post_id = post.get("id")
    if not url:
        continue

    comments.extend(get_reddit_comments(url, post_id))
'''

posts = [{"url":"https://www.reddit.com/r/croatia/comments/1fdr6ej/jugonostalgija_u_hrvatskoj/","id":"1fdr6ej"},
         {"url":"https://www.reddit.com/r/croatia/comments/195v3rf/evo_jedan_podatak_za_pokazati_jugonostalgi%C4%8Darima/","id":"195v3rf"},
         {"url":"https://www.reddit.com/r/croatia/comments/d719zg/u_jugoslaviji_je_bilo_zabranjeno_i%C4%87i_u_crkvu/","id":"d719zg"},
         {"url":"https://www.reddit.com/r/croatia/comments/w1y25v/bratstvo_i_jedinstvo_u_jugoslaviji_utopija_ili/","id":"w1y25v"},
         {"url":"https://www.reddit.com/r/croatia/comments/hljuh8/pitanje_za_starije_kako_je_izgledao_prosje%C4%8Dan_dan/","id":"hljuh8"},
         {"url":"https://www.reddit.com/r/hreddit/comments/1mthjrs/ja_sam_mislio_da_su_u_jugoslaviji_svi_i%C5%A1li_na/","id":"1mthjrs"},]

comments = []
for post in posts:
    url = post.get("url")
    post_id = post.get("id")
    if not url:
        continue

    comments.extend(get_reddit_comments(url, post_id))

#save_to_jsonl(comments, "data/original/posts/comments/reddit_comments_Croatia.jsonl")
#save_to_jsonl(comments, "data/original/posts/comments/reddit_comments_AskCroatia.jsonl")
#save_to_jsonl(comments, "data/original/posts/comments/reddit_comments_hreddit.jsonl")
#append_to_jsonl("data/original/posts/comments/reddit_comments_Croatia.jsonl", comments)
#append_to_jsonl("data/original/posts/comments/reddit_comments_AskCroatia.jsonl", comments)
#append_to_jsonl("data/original/posts/comments/reddit_comments_hreddit.jsonl", comments)
append_to_jsonl("data/original/posts/comments/reddit_comments_Croatia.jsonl", comments)