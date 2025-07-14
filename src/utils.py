# reddit-persona-generator/src/utils.py

import os

def save_to_file(filepath, text):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

def extract_username(url):
    return url.rstrip("/").split("/")[-1]