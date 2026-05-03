import yt_dlp as ytd


def extract_info(url: str):
    with ytd.YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(url, download=False)

    if "entries" in info:
        info = info["entries"][0]

    return info


def get_resolutions(info: dict):
    resolutions = set()

    for f in info.get("formats", []):
        if f.get("vcodec") != "none" and f.get("height"):
            resolutions.add(f["height"])

    return sorted(resolutions)


def get_best_audio_format():
    return "bestaudio/best"