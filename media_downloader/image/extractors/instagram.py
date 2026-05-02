# image/extractors/instagram.py

from urllib.parse import urlparse

try:
    import instaloader
except ImportError:
    instaloader = None


def extract_instagram_image(url):
    if instaloader is None:
        raise ImportError(
            "Install with: pip install media-downloader[image]"
        )

    try:
        L = instaloader.Instaloader()
        L.context.log = lambda *a, **kw: None

        parsed = urlparse(url)
        parts = [p for p in parsed.path.split("/") if p]

        if not parts:
            return []

        if parts[0] in ["p", "reel"]:
            post = instaloader.Post.from_shortcode(L.context, parts[1])

            if post.typename == "GraphSidecar":
                return [n.display_url for n in post.get_sidecar_nodes()]
            return [post.url]

        elif len(parts) == 1:
            profile = instaloader.Profile.from_username(L.context, parts[0])
            return [profile.profile_pic_url]

        return []

    except Exception:
        return []