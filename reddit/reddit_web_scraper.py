import time
from helper.normalizeDate import normalize_date
from reddit.getLinks import  scrape_reddit_links_subreddit
from reddit.getPosts import get_reddit_post


def scrape_portal_reddit(query: str, max_pages: int = 5):
    
    subreddits = [
        "Croatia",
        "AskCroatia",
        "hreddit"
    ]

    all_links = []

    for sub in subreddits:
        links = scrape_reddit_links_subreddit(sub, query=query, max_pages=max_pages)
        all_links.extend(links)

    print("Ukupno linkova:", len(all_links))

    posts = []

    for url in all_links:
        print("Scraping Reddit post:", url)

        id, full_text, title, publish_date = get_reddit_post(url)

        if full_text is None:
            print("Skipping (no text):", url)
            continue

        posts.append({
            "source": "reddit.com",
            "publish_date": normalize_date(publish_date),
            "id": id,
            "title": title,
            "article_url": url,
            "text": full_text
        })

        time.sleep(0.5)

    return posts
