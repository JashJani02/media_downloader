# image/downloader.py

import requests
import os
import uuid
from .dispatcher import get_extractor
from .utils.image_utils import get_image_resolution


class ImageDownloader:

    def __init__(self, download_dir="downloads"):
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)

    def fetch(self, url):
        extractor = get_extractor(url)
        return extractor(url)

    def download(self, url):
        image_urls = self.fetch(url)

        results = []

        for img_url in image_urls:
            try:
                data = requests.get(img_url, timeout=10).content

                width, height, label = get_image_resolution(data)

                filename = f"{uuid.uuid4()}.jpg"
                path = os.path.join(self.download_dir, filename)

                with open(path, "wb") as f:
                    f.write(data)

                results.append({
                    "url": img_url,
                    "path": path,
                    "resolution": f"{width}x{height}",
                    "quality": label
                })

            except Exception:
                continue

        return results