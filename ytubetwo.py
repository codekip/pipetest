import asyncio
import yt_dlp
from tqdm import tqdm


async def download_video(url):
    ydl_opts = {
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
        "no_warnings": True,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(info["title"])


async def multi():
    urls = [
        "https://youtu.be/P1ojpsyGCVQ",
        "https://youtu.be/pildU9lK6vM",
        "https://youtu.be/KTkW636B8xg",
        "https://youtu.be/u3_DxGEHWgE",
        "https://youtu.be/hwBySTM4Ngs",
        "https://youtu.be/mJS8ViUehOI",
        "https://youtu.be/Gj7p-wROi7g",
        "https://youtu.be/0Mv_EGHC_QA",
    ]

    tasks = []
    z = tqdm(urls)
    for url in z:
        tasks.append(download_video(url))
        z.set_description(f"Downloading {url}")

    await asyncio.gather(*tasks)


asyncio.run(multi())
