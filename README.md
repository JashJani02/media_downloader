# Multimedia downloader
A universal media downloader for images, videos, and audio from multiple platforms.

## **📂 Project Structure**
<pre>
multimedia-downloader/  
├── multimedia_downloader/      # Core Package  
│   ├── __init__.py             # Package entry point  
│   ├── client.py               # Main High-level API (Client class)  
│   ├── audio_video/            # A/V Logic  
│   │   ├── __init__.py  
│   │   ├── downloader.py       # yt-dlp implementation  
│   │   └── utils.py  
│   ├── image/                  # Image Logic  
│   │   ├── __init__.py  
│   │   ├── downloader.py       # Scraper/Requests implementation  
│   │   ├── dispatcher.py       # Platform routing  
│   │   ├── utils.py  
│   │   └── extractors/         # Scraping Methods/Patterns  
│   │       ├── __init__.py  
│   │       ├── generic.py  
│   │       ├── instagram.py  
│   │       ├── reddit.py  
│   │       ├── twitter.py  
│   │       ├── youtube.py  
│   │       └── unsplash.py  
│   ├── exceptions/             # Custom Error Handling  
│   │   └── errors.py  
│   └── utils/                  # Helper utilities  
│       ├── file_manager.py  
│       └── image_utils.py  
├── tests/                      # Testing suite  
├── pyproject.toml              # Build system & Dependencies  
├── LICENSE                     # MIT License  
└── README.md                   # Documentation
</pre>

## Tech-Stack
1)   **Language:** Python
2)   **Audio/Video Extraction:** `yt-dlp`
3)   **Image Scraping:** `BeautifulSoup4`, `Requests`, `Instaloader`
4)   **Image Processing:** `Pillow`
5)   **Package Management:** `pip`, `uv`
6)   **Build System:** `pyproject.toml`

## **🛠 Installation**

You can set up the Multimedia Downloader using two methods:

### **Method A: Using Package Managers (Recommended)**

Install directly from PyPI using pip or  uv.

**Using pip:**

<pre>pip install multimedia-downloader</pre>

**Using uv:**

<pre>uv pip install multimedia-downloader</pre>

### **Method B: Cloning the Repository (Development)**

If you want to modify the source code or contribute locally:

1) Clone the repository<pre>git clone https://github.com/JashJani02/multimedia-downloader.git</pre>
2) Change directory<pre>cd multimedia-downloader</pre>
3) Create a Virtual Environment<pre>python -m venv .venv</pre>
4) Activate the venv
<ul><li>Windows<pre>.venv\Scripts\activate</pre></li><li>Linux/Mac-OS<pre>source .venv/bin/activate</pre></li></ul>
5) Install the dependencies<pre>pip install -e .</pre>

## **📖 API Reference & Usage**

The easiest way to use the library is via the Client class.

### **Initializing the Client**
<pre>
from media_downloader import Client

# Files will be saved in the specified directory  
client = Client(download_dir="my_downloads")
</pre>
### **1. Audio & Video**

Powered by yt-dlp, supporting YouTube and 1000+ other sites.

| Function | Parameters | Description |
| :---- | :---- | :---- |
| get_video_info(url) | url: str | Returns raw metadata (title, views, etc). |
| get_video_resolutions(url) | url: str | Returns a list of available heights (e.g. 1080, 720). |
| download_video(url, res) | url: str, resolution: int | Downloads the best quality up to the specified resolution. |
| download_audio(url, fmt) | url: str, fmt: str | Downloads and converts audio to mp3, wav, etc. |

### **2. Images**

Specialized scrapers for Instagram, Reddit, Unsplash, and more.

| Function | Parameters | Description |
| :---- | :---- | :---- |
| download_images(url) | url: str | Scrapes the URL and saves all found images to the disk. |

## **💡 Example Usage**
<pre>
from media_downloader import Client

client = Client()

# Download a 1080p video from YouTube  
client.download_video(("https://youtu.be/dQw4w9WgXcQ"), resolution=1080)

# Download high-res images from an Instagram post  
client.download_images("(https://www.instagram.com/p/DTTUGFOiCys/)")
</pre>

## **🔗 References & Credits**

This universal library is the evolution of my specialized downloader projects:

* [Image Downloader](https://github.com/JashJani02/Image-downloader) - Core image scraping logic.  
* [A-V Downloader](https://github.com/JashJani02/A-V-Downloader) - Core video/audio processing logic.

## **⚖ License**

This project is licensed under the **MIT License** \- see the [LICENSE](https:/github.com/JashJani02/multimedia_downloader/blob/main/LICENSE) file for details.
