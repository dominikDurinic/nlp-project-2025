from datetime import datetime, timezone
import requests

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }

def get_reddit_comments(url: str, post_id: str):

    api_url = f"https://www.reddit.com/comments/{post_id}.json"
    r = requests.get(api_url, headers=HEADERS)
    data = r.json()

    comments_raw = data[1]["data"]["children"]

    comments = []
    for c in comments_raw:
        if c["kind"] != "t1":
            continue

        d = c["data"]

        ts = d.get("created_utc")
        date = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
        
        comments.append({
            "postId": post_id,
            "text": d.get("body"),
            "score": d.get("score"),
            "date": date
        })

    return comments
