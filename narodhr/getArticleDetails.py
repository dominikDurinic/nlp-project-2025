import json
import re
from urllib.parse import parse_qs, urlparse
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def sanitize_for_json(text: str) -> str:
    if not text:
        return text

    # 1. makni opasne unicode separatore
    text = text.replace("\u2028", " ").replace("\u2029", " ")

    # 2. zamijeni ASCII navodnike
    text = text.replace('"', '“')

    # 3. escapeaj backslash
    text = text.replace("\\", "\\\\")

    return text


def get_article_details(article_url):
    response = requests.get(article_url, headers=headers)
    if response.status_code != 200:
        return "", None

    soup = BeautifulSoup(response.text, "html.parser")

    # Glavni tekst članka
    article = soup.find("div", class_="td-post-content")
    blocks = []
    if article:
        for tag in article.find_all(["p", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                blocks.append(text)
    full_text = sanitize_for_json("\n".join(blocks))


    # Datum objave
    time_tag = soup.find("time", class_="entry-date")
    publish_date_iso = time_tag.get("datetime") if time_tag else None
    if publish_date_iso:
        publish_date_iso = publish_date_iso.split("T")[0]

    # t_i 
    script_tag = soup.find("script", text=re.compile("var embedVars"))
    if not script_tag:
        return None, None

    m = re.search(r"var embedVars\s*=\s*(\{.*?\});", script_tag.string, re.S)
    if not m:
        return None, None

    embedVars = json.loads(m.group(1))
    t_i_raw = embedVars.get("disqusIdentifier")


    return full_text, publish_date_iso, t_i_raw
