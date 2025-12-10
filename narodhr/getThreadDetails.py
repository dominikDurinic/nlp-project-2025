import requests

DISQUS_API_KEY = "A6n72ZScd1B7CmTHoRG5EDApWW4RJBRhaxY7ZqGpFNaZkSZiSi5X9BzLD9qGx5jC"

def get_thread_details(ident, forum="narodhr"):
    url = "https://disqus.com/api/3.0/threads/details.json"
    params = {"forum": forum, "thread:ident": ident, "api_key": DISQUS_API_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()["response"]["id"]
