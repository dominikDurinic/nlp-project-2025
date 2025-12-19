import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": "Mozilla/5.0"}


def extract_publish_date(soup):
    # pronađi sve meta__group elemente unutar članka
    groups = soup.select(".single-article__row .meta__group")

    for g in groups:
        text = g.get_text(" ", strip=True)
        # regex traži DD.MM.YYYY.
        m = re.search(r"\b\d{1,2}\.\d{1,2}\.\d{4}\.", text)
        if m:
            return m.group(0)

    return None



def get_article_vecernji(article_url):
    try:
        r = requests.get(article_url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        # Naslov
        title_tag = soup.select_one(".single-article__title")
        title = title_tag.get_text(" ", strip=True) if title_tag else None

        
        # Datum
        publish_date = extract_publish_date(soup)

        if publish_date is None:
            date_group = soup.select(".meta__group")
            if len(date_group) >= 2:
                publish_date = date_group[1].get_text(" ", strip=True)


        # Tekst članka
        text_blocks = []

        # glavni tekst
        for p in soup.select(".text.text--large p"):
            txt = p.get_text(" ", strip=True)
            if txt:
                text_blocks.append(txt)

        # dodatni tekst (nakon reklama)
        for p in soup.select(".single-article__content p"):
            txt = p.get_text(" ", strip=True)
            if txt:
                text_blocks.append(txt)

        # fallback: p tagovi nakon članka
        for p in soup.find_all("p"):
            txt = p.get_text(" ", strip=True)
            if txt and txt not in text_blocks:
                if "teads" in txt.lower():
                    continue
                text_blocks.append(txt)

        full_text = "\n".join(text_blocks)

        return full_text, title, publish_date

    except Exception as e:
        print("Greška u parsiranju članka:", e)
        return None, None, None
