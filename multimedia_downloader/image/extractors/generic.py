# image/extractors/generic.py

import requests
from bs4 import BeautifulSoup

def extract_images(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        urls = set()

        for img in soup.find_all("img"):
            # normal src
            src = img.get("src")

            # lazy loading
            data_src = img.get("data-src")

            # responsive images
            srcset = img.get("srcset")

            if src and src.startswith("http"):
                urls.add(src)

            if data_src and data_src.startswith("http"):
                urls.add(data_src)

            if srcset:
                for part in srcset.split(","):
                    link = part.strip().split(" ")[0]
                    if link.startswith("http"):
                        urls.add(link)

        return list(urls)

    except Exception:
        return []