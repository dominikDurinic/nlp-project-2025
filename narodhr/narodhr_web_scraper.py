import requests
from bs4 import BeautifulSoup
from narodhr.getArticleDetails import get_article_details
from urllib.parse import urljoin

base_url = "https://narod.hr"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "hr-HR,hr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://narod.hr/search/jugoslavija",
    "Connection": "keep-alive",
}

def scrape_portal_narod(query, max_pages=5):
    articles = []
    page = 1

    while page <= max_pages:
        url = f"{base_url}/search/{query}/page/{page}"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        for art in soup.find_all("div", class_="td_module_flex"):
            h3_tag = art.find("h3", class_="entry-title")
            link_tag = h3_tag.find("a") if h3_tag else None

            
            if not link_tag or not link_tag.get("href"):
                continue

            link = urljoin(base_url, link_tag["href"])
            print("Scraping:", link)
            title = link_tag.get_text(strip=True) if link_tag else None
            print(link)
            

            # full text from detail page
            full_text, publish_date, t_i = get_article_details(link)

            articles.append({
                "source": "narod.hr",
                "publishDate": publish_date,
                "title": title,
                "url": link,
                "t_i": t_i,
                "text": full_text,
                "commentThreadId": None  # Narod.hr doesn't expose this
            })

        page += 1

    return articles
