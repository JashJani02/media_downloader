from multimedia_downloader import Client


def test_url(url):
    print(f"\nTesting: {url}")

    client = Client()

    try:
        # ---------- YouTube → test AV ----------
        if "youtube.com" in url or "youtu.be" in url:
            print("Detected: YouTube")

            print("Fetching resolutions...")
            resolutions = client.get_video_resolutions(url)
            print("Available:", resolutions)

            print("Downloading video (1080p)...")
            client.download_video(url, resolution=1080)

            print("Downloading audio (wav)...")
            client.download_audio(url, fmt="wav")

        # ---------- Others → image ----------
        else:
            print("Detected: Image-based platform")

            results = client.download_images(url)

            print(f"Downloaded {len(results)} images:")
            for r in results:
                print(" ->", r["path"])

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    test_urls = [
        "https://www.instagram.com/p/DTTUGFOiCys/",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://www.instagram.com/reels/DXxvl65tomi/",
        "https://www.reddit.com/r/formula1/comments/1t0vbk2/f1_the_teams_are_bringing_a_haul_of_upgrades_to/",
        "https://unsplash.com/photos/silhouette-of-person-standing-on-rock-surrounded-by-body-of-water-odxB5oIG_iA"
    ]

    for url in test_urls:
        test_url(url)