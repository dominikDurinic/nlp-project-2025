from dva_cetiri_sata.getArticleText import get_article_24sata
from dva_cetiri_sata.getLinks import scrape_24sata_scroll


def scrape_portal_24sata(query: str, scroll_times: int = 10):
    article_links = scrape_24sata_scroll(query, scroll_times)

    articles = []

    for url in article_links:
        print("Scraping:", url)

        # Dohvati tekst članka
        try:
            full_text, title, publish_date = get_article_24sata(url)
        except Exception as e:
            print("Greška u članku:", e)
            continue

        articles.append({
            "source": "24sata.hr",
            "url": url,
            "title": title,
            "publish_date": publish_date,
            "text": full_text
        })

    return articles
