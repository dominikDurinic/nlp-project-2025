from indexhr.getAllComments import get_all_comments
from indexhr.index_web_scraper import scrape_portal
from saveToCSV import save_to_csv
from indexhr.filter import exclude_sport

## indexhr

articles = []
articles = scrape_portal("jugoslavija", max_results=30)

articles = exclude_sport(articles)

save_to_csv(articles, "indexhr_articles.csv")

articles = []
articles = scrape_portal("yugoslavia", max_results=30)

articles = exclude_sport(articles)

save_to_csv(articles, "indexhr_articles.csv")

comments = []
for article in articles:
    thread_id = article.get("commentThreadId")
    if not thread_id:
        continue
    comments.extend(get_all_comments(thread_id))

save_to_csv(comments, "indexhr_comments.csv")