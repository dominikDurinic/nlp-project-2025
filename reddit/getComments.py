from datetime import datetime, timezone
import requests
import time
from helper.normalizeDate import normalize_date

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }

def get_reddit_comments(url: str, post_id: str):

    api_url = f"https://www.reddit.com/comments/{post_id}.json"
    r = requests.get(api_url, headers=HEADERS)

    time.sleep(2)
    
    # --- 1) Provjera statusa --- 
    if r.status_code == 429: 
        print("Reddit rate limit (429) – skipping") 
        time.sleep(5)
        return get_reddit_comments(url, post_id)
    if r.status_code == 403: 
        print("Reddit blocked the request (403)") 
        return [] 
    if r.status_code == 404: 
        print("Post not found (404)") 
        return [] 
    
    # --- 2) Pokušaj parsirati JSON --- 
    try: 
        data = r.json() 
    except ValueError: 
        print("Reddit returned non‑JSON response") 
        print("Status:", r.status_code) 
        print("Body:", r.text[:200]) 
        return [] 
    
    # --- 3) Ako JSON nije u očekivanom formatu --- 
    if not isinstance(data, list) or len(data) < 2: 
        print("Unexpected Reddit JSON structure") 
        return []

    comments_raw = data[1]["data"]["children"]

    comments = []
    for c in comments_raw:
        if c["kind"] != "t1":
            continue

        d = c["data"]

        ts = d.get("created_utc")
        date = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
        
        comments.append({
            "source": "reddit.com",
            "postId": post_id,
            "text": d.get("body"),
            "score": d.get("score"),
            "publish_date": normalize_date(date),
            "article_url": url,
        })

    return comments
