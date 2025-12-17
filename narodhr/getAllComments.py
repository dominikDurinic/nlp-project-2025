import requests

from narodhr.getThreadDetails import get_thread_details

DISQUS_API_KEY = "A6n72ZScd1B7CmTHoRG5EDApWW4RJBRhaxY7ZqGpFNaZkSZiSi5X9BzLD9qGx5jC"

def get_comments(thread_id, forum="narodhr"):
    # 1. dohvati pravi internal thread id
    thread_id_final = get_thread_details(thread_id, forum)

    # 2. povuci komentare
    url = "https://disqus.com/api/3.0/threads/listPosts.json"
    params = {"forum": forum, "thread": thread_id_final, "api_key": DISQUS_API_KEY, "limit": 100}
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()

    comments = []
    for post in data.get("response", []):
        comments.append({
            "source" :"narod.hr",
            "id": post["id"],
            "author": post["author"]["name"],
            "message": post["message"],
            "createdAt": post["createdAt"]
        })
    return comments

