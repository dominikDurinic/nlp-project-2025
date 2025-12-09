import requests
import re

# pronalazak thread ID za komentare na article sa INDEX.hr
def get_comment_thread_id(article_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(article_url, headers=headers).text
    
    # Regex za traženje commentThreadId u skripti
    match = re.search(r'commentThreadId=(\d+)', html)
    if match:
        return match.group(1)
    else:
        return None

# Primjer
#url = "https://www.index.hr/magazin/clanak/anketa-30-pjesama-o-jugoslaviji-koja-je-najbolja/2619762.aspx"
#thread_id = get_comment_thread_id(url)
#print("Thread ID:", thread_id)
