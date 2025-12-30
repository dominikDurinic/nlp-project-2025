def exclude_sport(articles):
    return [a for a in articles if "/sport/" not in a["article_url"].lower()]