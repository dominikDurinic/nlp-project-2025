import requests
from bs4 import BeautifulSoup
from indexhr.getArticleText import get_article_text 
from indexhr.getCommentsThreadID import get_comment_thread_id
from urllib.parse import urljoin

#Scraping s portala indexhr

base_url = "https://www.index.hr"

headers = {"User-Agent": "Mozilla/5.0"}

def scrape_portal(query, max_results):
    articles = []
    offset = 0
    take = 15

    while offset < max_results:
        url = f"https://www.index.hr/search/load-more-search-news?query={query}&orderby=latest&offset={offset}&take={take}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")


        for div in soup.find_all("div", class_="grid-item"):
            link_tag = div.find("a")
            date_tag = div.find("div", class_="publish-date")
            if not link_tag or not link_tag.get("href"):
                continue

            link = urljoin(base_url, link_tag["href"])
            title = link_tag.get_text(strip=True)

            # full text from detail page
            full_text = get_article_text(link)
            #date from listing page
            date = date_tag.get_text(strip=True) if date_tag else None

            # extract commentThreadId from script
            thread_id = get_comment_thread_id(link)


            articles.append({
                "source": "indexhr",
                "publishDate": date,
                "title": title,
                "url": link,
                "text": full_text,
                "commentThreadId": thread_id
            })

        offset+=15

    return articles




