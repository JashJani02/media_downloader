import requests

def extract_reddit_images(url: str) -> list:
    try:
        if not url.endswith(".json"):
            url = url.rstrip("/") + "/.json"

        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)

        if res.status_code != 200:
            return []

        data = res.json()
        image_urls = []

        def traverse(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():

                    # direct image links
                    if isinstance(v, str) and v.endswith(
                        (".jpg", ".png", ".jpeg", ".webp")
                    ):
                        image_urls.append(v)

                    # reddit preview images
                    if k == "source" and isinstance(v, dict):
                        if "url" in v:
                            image_urls.append(v["url"])

                    traverse(v)

            elif isinstance(obj, list):
                for i in obj:
                    traverse(i)

        traverse(data)

        return list(set(image_urls))

    except Exception:
        return []