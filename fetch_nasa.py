from urllib.parse import urlparse
from dotenv import load_dotenv
from pathlib import Path

import datetime
import requests
import argparse
import os
import sys


def get_file_extension(path):
    return os.path.splitext(urlparse(path).path)[1]


def download_pic(dir, url):
    response = requests.get(url)
    response.raise_for_status()

    with open(dir, 'wb') as file:
        file.write(response.content)


def download_nasa_APOD_images(NASA_API):
    count_of_pictures = 30
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API,
              "count": count_of_pictures}
    images_data = requests.get(url, params=params).json()
    index = 0
    folder = "images"

    for pic_data in images_data:
        index += 1

        url = pic_data["url"]

        file_name = f"apod_image_{index}{get_file_extension(url)}"
        file_path = os.path.join(folder, file_name)

        download_pic(file_path, url)


def download_nasa_EPIC_images(NASA_API):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": NASA_API}
    images_data = requests.get(url, params=params).json()
    index = 0
    folder = "images"

    for pic_data in images_data:
        index += 1

        data = datetime.datetime.strptime(pic_data["date"], '%Y-%m-%d %H:%M:%S')
        prepared_data = f"{data.year}/{str(data.month).zfill(2)}/{str(data.day).zfill(2)}"
        name = pic_data["image"]

        url = f"https://api.nasa.gov/EPIC/archive/natural/{prepared_data}/png/{name}.png?api_key={NASA_API}"
        filename = f"epic_image_{index}.png"
        file_path = os.path.join(folder, filename)
        download_pic(file_path, url)


def main():
    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_TOKEN")

    folder = "images"
    Path(folder).mkdir(parents=True, exist_ok=True)

    download_nasa_EPIC_images(nasa_api_token)
    download_nasa_APOD_images(nasa_api_token)


if __name__ == "__main__":
    main()