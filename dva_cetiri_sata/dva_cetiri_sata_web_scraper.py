import requests
from bs4 import BeautifulSoup
from dva_cetiri_sata.getArticleText import  get_article_24sata

headers = {"User-Agent": "Mozilla/5.0"}

def scrape_portal_24sata(query: str):
    url = "https://www.24sata.hr/trazi"
    params = {"query": query}

    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    articles = []

    # svaki članak je u article_wrap → card
    cards = soup.select("div.article_wrap div.card")

    for card in cards:
        link = card.get("data-article-link")
        if link and not link.startswith("http"):
            link = "https://www.24sata.hr" + link

        try:
            full_text, title, publish_date = get_article_24sata(link)
        except Exception as e:
            print(f"Greška pri dohvaćanju članka {link}: {e}")
            full_text, title, publish_date = None, None, None

        articles.append({
            "source": "24sata.hr",
            "url": link,
            "title": title,
            "publish_date": publish_date,
            "text": full_text
        })

    return articles
