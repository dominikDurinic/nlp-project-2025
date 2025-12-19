from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_24sata_scroll(query: str, scroll_times: int = 10):
    # Chrome headless
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    search_url = f"https://www.24sata.hr/trazi?query={query}"
    driver.get(search_url)

    # Scroll X puta
    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # čekaj da se feed učita

    # Uzmi HTML nakon scrollanja
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    links = []
    cards = soup.select("div.article_wrap div.card")

    for card in cards:
        link = card.get("data-article-link")
        if link and not link.startswith("http"):
            link = "https://www.24sata.hr" + link
        links.append(link)

    # ukloni duplikate
    links = list(dict.fromkeys(links))

    return links
