from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

from helper.normalizeDate import normalize_date


def scroll_until_done(driver):
    last_count = 0
    stagnant_rounds = 0

    while True:
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(1.2)

        comments_now = len(driver.find_elements(By.CSS_SELECTOR, "div.thread_comment"))

        if comments_now == last_count:
            stagnant_rounds += 1
        else:
            stagnant_rounds = 0

        if stagnant_rounds >= 5:
            break

        last_count = comments_now

def get_comments_24sata(article_url: str, driver):
    comments_url = article_url.rstrip("/") + "/komentari"

    driver.get(comments_url)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.thread_comment"))
        )
    except:
        return []

    scroll_until_done(driver)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    comments = []

    for c in soup.select("div.thread_comment"):
        comment_id = c.get("id", "").replace("comment-", "")
        created_date = c.get("data-created-date")

        content_tag = c.select_one(".thread_comment__content")
        text = content_tag.get_text(" ", strip=True) if content_tag else None

        if not text:
            continue

        comments.append({
            "source": "24sata.hr",
            "article_url": article_url,
            "comment_id": comment_id,
            "publish_date": normalize_date(created_date),
            "text": text,
        })

    return comments
