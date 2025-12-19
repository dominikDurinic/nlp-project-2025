from jutarnjihr.getArticleText import get_article_text_jutarnji
from jutarnjihr.getLinks import scrape_jutarnji_links


def scrape_portal_jutarnji(query: str, pages: int = 5):
    links = scrape_jutarnji_links(query, pages)

    articles = []


    for url in links:
        print("Scraping:", url)

        full_text, publish_date, title = get_article_text_jutarnji(url)

        if full_text is None:
            print("Preskačem članak:", url)
            continue


        articles.append({
            "source": "jutarnji.hr",
            "publishDate": publish_date,
            "title": title,
            "url": url,
            "text": full_text
        })


    return articles
