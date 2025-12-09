import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def get_article_text(article_url):
    html = requests.get(article_url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    article = soup.find("section", {"aria-label": "Tekst članka"})

    if not article:
        return ""

    blocks = []
    for tag in article.find_all(["p", "h3"]):
        blocks.append(tag.get_text(strip=True))

    full_text = "\n".join(blocks)
    return full_text