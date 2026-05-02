# image/dispatcher.py

from .extractors.generic import extract_images
from .extractors.instagram import extract_instagram_image
from .extractors.youtube import extract_youtube_thumbnail
from .extractors.reddit import extract_reddit_images
from .extractors.twitter import extract_twitter_images
from .extractors.unsplash import extract_unsplash_image


def get_extractor(url):

    if "instagram.com" in url:
        return extract_instagram_image

    elif "reddit.com" in url:
        return extract_reddit_images

    elif "x.com" in url or "twitter.com" in url:
        return extract_twitter_images

    elif "youtube.com" in url or "youtu.be" in url:
        return extract_youtube_thumbnail
    
    elif "unsplash.com" in url:
        return extract_unsplash_image

    return extract_images