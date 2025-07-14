# reddit-persona-generator/src/reddit_scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_user_data(username):
    url = f"https://www.reddit.com/user/{username}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    posts = []
    comments = []

    try:
        for kind in ["posts", "comments"]:
            sub_url = f"https://www.reddit.com/user/{username}/{kind}/"
            res = requests.get(sub_url, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")
            entries = soup.find_all("div", class_="_1oQyIsiPHYt6nx7VOmd1sz")
            for entry in entries:
                text = entry.get_text(separator=" ", strip=True)
                if kind == "posts":
                    posts.append(text)
                else:
                    comments.append(text)
    except Exception as e:
        print(f"Failed to fetch data: {e}")

    return {"username": username, "posts": posts, "comments": comments}