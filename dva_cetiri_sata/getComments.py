import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def get_comments_24sata(article_url: str):
    comments_url = article_url.rstrip("/") + "/komentari"

    r = requests.get(comments_url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    comments = []

    for c in soup.select("div.thread_comment"):
        comment_id = c.get("id", "").replace("comment-", "")
        created_date = c.get("data-created-date")

        # text
        content_tag = c.select_one(".thread_comment__content")
        text = content_tag.get_text(" ", strip=True) if content_tag else None

        comments.append({
            "source":"24sata.hr",
            "article_url": article_url,
            "comment_id": comment_id,
            "created_date": created_date,
            "text": text,
        })

    return comments
