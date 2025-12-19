import requests
from bs4 import BeautifulSoup

from vecernjihr.getLinks import get_vecernji_comment_pages

headers = {"User-Agent": "Mozilla/5.0"}

def scrape_vecernji_comments_page(article_url, page=1):
    comments_url = article_url.rstrip("/") + "/komentari"
    if page > 1:
        comments_url += f"?page={page}"

    r = requests.get(comments_url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    comments = []

    # svaki komentar je u .comment-box
    for box in soup.select(".comment-box"):
        comment_id = box.get("id")  # npr. head_post_15278239

        # vrijeme
        time_tag = box.select_one(".comment-card__time")
        created_date = time_tag.get_text(strip=True) if time_tag else None

        # tekst
        text_tag = box.select_one(".comment-card__text p")
        text = text_tag.get_text(" ", strip=True) if text_tag else None

        comments.append({
            "source":"vecernji.hr",
            "article_url": article_url,
            "comment_id": comment_id,
            "created_date": created_date,
            "text": text,
        })

    return comments


def get_vecernji_comments(article_url):
    total_pages = get_vecernji_comment_pages(article_url)
    print(f"Found {total_pages} comment pages")

    all_comments = []

    for page in range(1, total_pages + 1):
        print(f"Scraping comments page {page}/{total_pages}")
        page_comments = scrape_vecernji_comments_page(article_url, page)
        all_comments.extend(page_comments)

    return all_comments
