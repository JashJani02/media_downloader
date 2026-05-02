import re
import requests

def extract_unsplash_image(url: str) -> list:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)

        if res.status_code != 200:
            return []

        # Look for og:image meta tag (best quality)
        match = re.search(
            r'<meta property="og:image" content="([^"]+)"',
            res.text
        )

        if match:
            return [match.group(1)]

        return []

    except Exception:
        return []