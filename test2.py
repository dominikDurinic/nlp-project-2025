from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
from indexhr.getCommentsThreadID import get_comment_thread_id

headers = {"User-Agent": "Mozilla/5.0"}
commentThreadId = get_comment_thread_id("https://www.index.hr/magazin/clanak/anketa-30-pjesama-o-jugoslaviji-koja-je-najbolja/2619762.aspx")
response = requests.get(f"https://www.index.hr/api/comments?commentThreadId={commentThreadId}", headers=headers)

data = response.json()

comments = []
for item in data.get("comments", []):
    comments.append({
        "author": item.get("posterFullName", "Anonimno"),
        "text": item.get("content", ""),
        "date": item.get("createdDateUtc", "")
    })


df = pd.DataFrame(comments)
df.to_csv("jugoslavija_dataset.csv", index=False)
print(f"Dataset spremljen u jugoslavija_dataset.csv")
