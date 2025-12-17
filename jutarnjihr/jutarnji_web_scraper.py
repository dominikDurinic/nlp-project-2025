import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse, unquote
from jutarnjihr.getArticleText import get_article_text_jutarnji

headers = {"User-Agent": "Mozilla/5.0"}

def extract_real_link(ddg_link: str) -> str:
    if ddg_link.startswith("//duckduckgo.com/l/"):
        ddg_link = "https:" + ddg_link
        parsed = urlparse(ddg_link)
        qs = parse_qs(parsed.query)
        if "uddg" in qs:
            return unquote(qs["uddg"][0])
    return ddg_link

def scrape_portal_jutarnji(query: str, pages: int = 5):
    articles = []
    url = "https://duckduckgo.com/html/"
    results_per_page = 10  # po defaultu DDG HTML
    for page in range(pages):
        params = {"q": f"site:jutarnji.hr {query}", "s": page * results_per_page}
        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        
        for a in soup.select("a.result__a"):
            raw_link = a.get("href")
            link = extract_real_link(raw_link)
            if link and "jutarnji.hr" in link:
                try:
                    data = get_article_text_jutarnji(link)
                    if not data:
                        continue
                    full_text, publish_date, title = data
                    articles.append({
                        "source": "jutarnji.hr",
                        "publishDate": publish_date,
                        "title": title,
                        "url": link,
                        "text": full_text
                    })
                except Exception as e:
                    print(f"Error scraping {link}: {e}")
    return articles

