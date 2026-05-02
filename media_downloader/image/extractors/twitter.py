import requests
import re

def extract_twitter_images(url: str) -> list:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)

        if res.status_code != 200:
            return []

        matches = re.findall(
            r"https://pbs\.twimg\.com/media/[A-Za-z0-9_-]+\.[a-zA-Z]+",
            res.text
        )

        return list(set(matches))

    except Exception:
        return []