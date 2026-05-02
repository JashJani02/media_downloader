import os
import yt_dlp as ytd

from .utils import extract_info, get_resolutions


class AudioVideoDownloader:

    def __init__(self, download_dir="downloads"):
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)

    # ---------- INFO ----------
    def get_info(self, url: str):
        return extract_info(url)

    def get_resolutions(self, url: str):
        info = extract_info(url)
        return get_resolutions(info)

    # ---------- AUDIO ----------
    def download_audio(self, url: str, fmt="mp3"):
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{self.download_dir}/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": fmt,
                    "preferredquality": "192",
                }
            ],
            "quiet": True,
        }

        with ytd.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return {"status": "success", "type": "audio"}

    # ---------- VIDEO ----------
    def download_video(self, url: str, resolution=None):
        format_string = (
    f"bestvideo[ext=mp4][height<={resolution}]+bestaudio[ext=m4a]/best[ext=mp4]"
    if resolution
    else "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
)

        ydl_opts = {
            "format": format_string,
            "outtmpl": f"{self.download_dir}/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
            "quiet": False,
            "verbose": True,
        }

        with ytd.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return {"status": "success", "type": "video"}