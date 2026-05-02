# image/utils/image_utils.py

from PIL import Image
from io import BytesIO

def get_image_resolution(img_bytes):
    try:
        img = Image.open(BytesIO(img_bytes))
        width, height = img.size
        longest = max(width, height)

        if longest >= 3840:
            label = "4K"
        elif longest >= 1920:
            label = "1080p"
        elif longest >= 1280:
            label = "720p"
        else:
            label = f"{width}x{height}"

        return width, height, label

    except Exception:
        return None, None, "Unknown"