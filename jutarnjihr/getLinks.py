from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_jutarnji_links(query: str, max_pages: int = 5):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    search_url = f"https://www.jutarnji.hr/pretraga?q={query}"
    driver.get(search_url)

    links = []

    for page in range(1, max_pages + 1):

        # čekaj da se rezultati pojave
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".gsc-webResult"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # izvuci linkove
        for a in soup.select("a.gs-title"):
            href = a.get("href")
            if href and "jutarnji.hr" in href:
                links.append(href)

        # pronađi sve brojeve stranica
        page_buttons = driver.find_elements(By.CSS_SELECTOR, ".gsc-cursor-page")

        # ako nema više stranica → prekini
        if page >= len(page_buttons):
            break

        # klikni sljedeći broj stranice
        try:
            page_buttons[page].click()  # page=1 → klikne "2"
        except Exception as e:
            print("Ne mogu kliknuti broj stranice:", e)
            break

        time.sleep(2)

    driver.quit()

    # ukloni duplikate
    links = list(dict.fromkeys(links))

    return links
