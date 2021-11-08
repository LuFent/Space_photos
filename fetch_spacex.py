from urllib.parse import urlparse
from pathlib import Path

import requests
import os


def download_pic(dir, url):
    response = requests.get(url)
    response.raise_for_status()

    with open(dir, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v4/launches/"
    response = requests.get(url).json()[130]
    image_urls = response["links"]["flickr"]["original"]

    index = 0
    folder = "images"
    Path(folder).mkdir(parents=True, exist_ok=True)

    for url in image_urls:
        index += 1

        filename = f"spacex_image_{index}.jpg"
        file_path = os.path.join(folder, filename)

        download_pic(file_path, url)


def main():
    fetch_spacex_last_launch()


if __name__ == "__main__":
    main()