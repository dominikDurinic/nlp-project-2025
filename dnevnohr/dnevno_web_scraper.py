import requests
from bs4 import BeautifulSoup

from dnevnohr.getArticleText import  get_article_text_dnevno
from helper.normalizeDate import normalize_date

headers = {"User-Agent": "Mozilla/5.0"}

def scrape_portal_dnevno(query: str, num_pages: int = 5):
    articles = []

    for page in range(1, num_pages + 1):
        url = "https://www.dnevno.hr/"
        params = {"s": query, "paged": page}

        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        links = soup.select("article.post > a[href]")

        if not links:
            print(f"Nema više članaka na stranici {page}.")
            break

        for a in links:
            link = a["href"]

            if "/tag/" in link.lower():
                continue

            print("Scraping:", link)

            try:
                full_text, publish_date, title = get_article_text_dnevno(link)
                articles.append({
                    "source": "dnevno.hr",
                    "publish_date": normalize_date(publish_date),
                    "title": title,
                    "article_url": link,
                    "text": full_text
                })

            except Exception as e:
                print(f"Greška pri dohvaćanju {link}: {e}")

    return articles
