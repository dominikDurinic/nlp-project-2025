import requests
import time

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }

'''
def scrape_reddit_links(query: str, max_pages: int = 5, limit: int = 25):
    all_links = []
    after = None

    for page in range(max_pages):
        url = f"https://www.reddit.com/search.json?q={query}&limit={limit}"
        if after:
            url += f"&after={after}"

        print(f"Fetching page {page+1}: {url}")

        r = requests.get(url, headers=HEADERS)
        data = r.json()

        children = data.get("data", {}).get("children", [])
        if not children:
            break

        for item in children:
            post = item["data"]
            all_links.append("https://www.reddit.com" + post["permalink"])

        after = data.get("data", {}).get("after")
        if not after:
            break

        time.sleep(0.5)  # rate-limit protection

    return all_links
'''

def scrape_reddit_links_subreddit(subreddit: str, query: str, max_pages: int = 3, limit: int = 5):
    all_links = []
    after = None

    for page in range(max_pages):
        url = f"https://www.reddit.com/r/{subreddit}/search.json?q={query}&restrict_sr=1&limit={limit}"
        if after:
            url += f"&after={after}"

        print(f"[{subreddit}] Fetching page {page+1}: {url}")

        r = requests.get(url, headers=HEADERS)

        if "application/json" not in r.headers.get("Content-Type", ""):
            print("Blocked or non-JSON response")
            print(r.text[:300])
            time.sleep(2)
            continue

        data = r.json()
        children = data.get("data", {}).get("children", [])
        if not children:
            break

        for item in children:
            post = item["data"]
            all_links.append("https://www.reddit.com" + post["permalink"])

        after = data.get("data", {}).get("after")
        if not after:
            break

        time.sleep(0.5)

    return all_links
