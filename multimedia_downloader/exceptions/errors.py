class MediaDownloaderError(Exception):
    """Base exception"""
    pass


class UnsupportedPlatformError(MediaDownloaderError):
    def __init__(self, url):
        super().__init__(f"Unsupported platform for URL: {url}")


class ExtractionError(MediaDownloaderError):
    def __init__(self, message="Failed to extract media"):
        super().__init__(message)


class DownloadError(MediaDownloaderError):
    def __init__(self, message="Failed to download media"):
        super().__init__(message)