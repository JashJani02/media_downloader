# image/extractors/youtube.py

import re

def extract_youtube_thumbnail(url):
    match = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", url)
    if not match:
        return []

    vid = match.group(1)

    qualities = [
        "maxresdefault",
        "sddefault",
        "hqdefault",
        "mqdefault",
        "default"
    ]

    return [f"https://img.youtube.com/vi/{vid}/{q}.jpg" for q in qualities]