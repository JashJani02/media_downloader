import requests

from media_downloader.audio_video import AudioVideoDownloader
from media_downloader.image.dispatcher import get_extractor
from media_downloader.utils.file_manager import save_file


class Client:

    def __init__(self, download_dir="downloads"):
        self.download_dir = download_dir
        self.av = AudioVideoDownloader(download_dir)

    # ---------- IMAGE ----------
    def download_images(self, url: str):
        extractor = get_extractor(url)
        image_urls = extractor(url)

        results = []

        for img_url in image_urls:
            try:
                res = requests.get(img_url, timeout=10)

                if res.status_code != 200:
                    continue

                path = save_file(res.content, self.download_dir)

                results.append({
                    "url": img_url,
                    "path": path
                })

            except Exception:
                continue

        return results

    # ---------- AUDIO ----------
    def download_audio(self, url: str, fmt="mp3"):
        return self.av.download_audio(url, fmt)

    # ---------- VIDEO ----------
    def download_video(self, url: str, resolution=None):
        return self.av.download_video(url, resolution)

    # ---------- INFO ----------
    def get_video_info(self, url: str):
        return self.av.get_info(url)

    def get_video_resolutions(self, url: str):
        return self.av.get_resolutions(url)