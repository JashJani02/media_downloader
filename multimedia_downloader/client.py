import requests

from multimedia_downloader.audio_video import AudioVideoDownloader
from multimedia_downloader.image.dispatcher import get_extractor
from multimedia_downloader.utils.file_manager import save_file


class Client:

    def __init__(self, download_dir="downloads"):

        """
        Initializes the client with a target directory for all downloads.

        Args:
            download_dir (str): The local directory where media will be saved. 
                                Defaults to "downloads".
        """

        self.download_dir = download_dir
        self.av = AudioVideoDownloader(download_dir)

    # ---------- IMAGE ----------
    def download_images(self, url: str):
        
        """
        Downloads all images from a given URL.

        Args:
            url (str): The URL to extract images from.

        Returns:
            list: A list of dictionaries containing the image URLs and their local paths.
        """

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
        """
        Downloads audio from a given URL.

        Args:
            url (str): The URL of the audio to download.
            fmt (str): The desired audio format. Defaults to "mp3".

        Returns:
            str: The local path where the audio file is saved.
        """
        return self.av.download_audio(url, fmt)

    # ---------- VIDEO ----------
    def download_video(self, url: str, resolution=None):
        
        """
        Downloads a video from a given URL.

        Args:
            url (str): The URL of the video to download.
            resolution (int | str, optional): The desired video resolution. If None, the highest available resolution is used.

        Returns:
            str: The local path where the video file is saved.
        """

        return self.av.download_video(url, resolution)

    # ---------- INFO ----------
    def get_video_info(self, url: str):

        """
        Retrieves information about a video from a given URL.

        Args:
            url (str): The URL of the video.

        Returns:
            dict: A dictionary containing the video information.
        """

        return self.av.get_info(url)

    def get_video_resolutions(self, url: str):

        """
        Retrieves available resolutions for a video from a given URL.

        Args:
            url (str): The URL of the video.

        Returns:
            list: A list of available resolutions.
        """

        return self.av.get_resolutions(url)