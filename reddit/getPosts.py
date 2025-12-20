from datetime import datetime, timezone
import requests 

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }

def get_reddit_post(url: str):
    try:
        post_id = url.split("/comments/")[1].split("/")[0]
    except:
        return None, None, None, None

    api_url = f"https://www.reddit.com/comments/{post_id}.json"
    r = requests.get(api_url, headers=HEADERS)
    data = r.json()

    post_data = data[0]["data"]["children"][0]["data"]

    # Naslov
    title = post_data.get("title")
    
    # Tekst
    text = post_data.get("selftext") or ""

    # Datum
    ts = post_data.get("created_utc")
    publish_date = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")

    # Id posta
    id = post_data.get("id")

    return id, text, title, publish_date
