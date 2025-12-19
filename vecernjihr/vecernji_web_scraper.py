from vecernjihr.getArticles import get_article_vecernji
from vecernjihr.getLinks import scrape_vecernji_links


def scrape_portal_vecernji(query: str, max_pages: int = 5):
    links = scrape_vecernji_links(query, max_pages)

    articles = []

    for url in links:
        print("Scraping article:", url)

        full_text, title, publish_date = get_article_vecernji(url)

        if full_text is None:
            print("Skipping (no text):", url)
            continue

        articles.append({
            "source": "vecernji.hr",
            "publishDate": publish_date,
            "title": title,
            "url": url,
            "text": full_text
        })

    return articles
