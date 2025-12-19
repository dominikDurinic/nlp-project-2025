import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def scrape_vecernji_links(query: str, max_pages: int = 5):
    links = []

    for page in range(1, max_pages + 1):
        url = f"https://www.vecernji.hr/pretraga?query={query}&order=-publish_from&page={page}"
        print("Scraping search page:", url)

        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print("Page error:", r.status_code)
            break

        soup = BeautifulSoup(r.text, "html.parser")

        # svaki rezultat ima <a class="card__link">
        for a in soup.select("a.card__link"):
            href = a.get("href")
            if not href:
                continue

            # relativni → apsolutni
            if href.startswith("/"):
                href = "https://www.vecernji.hr" + href

            links.append(href)

        # ako nema rezultata → prekini
        if not soup.select("a.card__link"):
            break

    # ukloni duplikate
    links = list(dict.fromkeys(links))
    return links


def get_vecernji_comment_pages(article_url):
    url = article_url.rstrip("/") + "/komentari"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    pages = 1
    for a in soup.select("a"):
        href = a.get("href", "")
        if "page=" in href:
            try:
                num = int(href.split("page=")[1])
                pages = max(pages, num)
            except:
                pass

    return pages
