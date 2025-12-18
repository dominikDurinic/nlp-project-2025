import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": "Mozilla/5.0"}

def get_article_24sata(article_url):
    r = requests.get(article_url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    # Naslov
    title_tag = soup.find("h1", class_="article__title")
    title = title_tag.get_text(" ", strip=True) if title_tag else None

    # Datum
    time_tag = soup.find("time", class_="article__time")
    publish_date = None
    if time_tag:
        if time_tag.has_attr("datetime"):
            # uzmi samo YYYY-MM-DD dio
            publish_date = time_tag["datetime"].split(" ")[0]
        else:
            publish_date = time_tag.get_text(" ", strip=True)

    # Tekst članka
    blocks = []
    for p in soup.select("div.article__content p"):
        text = p.get_text(" ", strip=True)
        if text:
            # normaliziraj whitespace
            text = re.sub(r"\s+", " ", text)
            blocks.append(text)
    full_text = "\n".join(blocks)

    return full_text, title, publish_date
