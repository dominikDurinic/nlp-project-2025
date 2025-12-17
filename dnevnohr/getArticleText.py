from urllib.parse import parse_qs, unquote, urlparse
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def get_article_text_dnevno(article_url):
    r = requests.get(article_url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    # --- NOVI layout ---
    section = soup.find("section", class_="description")
    if section:
        # Naslov
        title_tag = section.find("h1")
        title = title_tag.get_text(" ", strip=True) if title_tag else None

        #  Datum
        time_tag = section.find("time")
        publish_date = None
        if time_tag:
            if time_tag.has_attr("datetime"):
                publish_date = time_tag["datetime"].split("T")[0]
            else:
                publish_date = time_tag.get_text(" ", strip=True)

        #  Tekst članka
        blocks = []
        for tag in section.find_all(["p", "h2"]):
            text = tag.get_text(" ", strip=True)  # razmak između child tagova
            if text:
                blocks.append(text)
        full_text = "\n".join(blocks)

        return full_text, publish_date, title

    # --- STARI layout fallback ---
    article = soup.find("div", class_="td-post-content")
    title_tag = soup.find("h1", class_="entry-title")
    title = title_tag.get_text(" ", strip=True) if title_tag else None

    time_tag = soup.find("time", class_="entry-date")
    publish_date = None
    if time_tag:
        if time_tag.has_attr("datetime"):
            publish_date = time_tag["datetime"].split("T")[0]
        else:
            publish_date = time_tag.get_text(" ", strip=True)

    blocks = []
    if article:
        for tag in article.find_all(["p", "h3"]):
            text = tag.get_text(" ", strip=True)
            if text:
                blocks.append(text)
    full_text = "\n".join(blocks)

    return full_text, publish_date, title
