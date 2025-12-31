import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def get_article_text_jutarnji(article_url):
    try:
        r = requests.get(article_url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        # Detekcija premium / free
        container = soup.select_one(".itemFullText")
        if not container:
            return None, None, None  # nema sadržaja

        classes = container.get("class", [])
        if "itemFullText--premium" in classes:
            return None, None, None  # premium → skip
        elif "itemFullText--freecontent" not in classes:
            return None, None, None  # nepoznat tip → skip

        # Naslov
        title_tag = soup.find("h1")
        title = title_tag.get_text(" ", strip=True) if title_tag else None

        '''
        # Datum
        publish_date = None
        time_tag = soup.find("time")
        if time_tag:
            if time_tag.has_attr("datetime"):
                publish_date = time_tag["datetime"].split("T")[0]
            else:
                publish_date = time_tag.get_text(strip=True)

        '''
         # Datum
        publish_date = None
        if publish_date is None: 
            date_span = soup.find("span", class_="item__author__date") 
            if date_span: 
                publish_date = date_span.get_text(strip=True)

                
        # Tekst članka
        blocks = []
        for tag in container.find_all(["p", "h2", "h3"]):
            text = tag.get_text(" ", strip=True)
            if text:
                blocks.append(text)

        full_text = "\n".join(blocks)

        return full_text, publish_date, title

    except Exception as e:
        print("Greška u parsiranju članka:", e)
        return None, None, None
