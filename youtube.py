from pytube import YouTube
from tqdm import tqdm


def download_video(url):
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    yt.streams.first().download()


def multi():
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

    z = tqdm(urls)
    for url in tqdm(z):
        download_video(url)
        z.set_description(f"Downloading {url}")

multi()
