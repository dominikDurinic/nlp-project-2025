import requests


def get_all_comments(thread_id):
    headers = {"User-Agent": "Mozilla/5.0"}
    all_comments = []
    skip = 0
    take = 10  # maksimalno koliko API dopušta u jednom potezu

    while True:
        url = f"https://www.index.hr/api/comments?commentThreadId={thread_id}&skip={skip}&take={take}"
        response = requests.get(url, headers=headers)
        data = response.json()
        batch = data.get("comments", [])
        if not batch:
            break
        for item in batch:
            all_comments.append({
                "source":"index.hr",
                "commentThreadId": thread_id,
                "author": item.get("posterFullName", "Anonimno"),
                "text": item.get("content", ""),
                "date": item.get("createdDateUtc", "")
            })
        skip += take  # idi na sljedeću “stranicu”

    return all_comments

