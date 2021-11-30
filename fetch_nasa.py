from general_funcs import get_file_extension
from general_funcs import download_pic

import datetime
import requests
import os


def download_nasa_apod_images(nasa_api, folder, count_of_pictures=30):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": nasa_api,
              "count": count_of_pictures}
    images_data = requests.get(url, params=params)
    images_data.raise_for_status()
    images_data = images_data.json()

    for index, pic_data in enumerate(images_data):
        url = pic_data["url"]

        file_name = f"apod_image_{index}{get_file_extension(url)}"
        file_path = os.path.join(folder, file_name)

        download_pic(file_path, url)


def download_nasa_epic_images(nasa_api, folder):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": nasa_api}
    images_data = requests.get(url, params=params)
    images_data.raise_for_status()
    images_data = images_data.json()

    for index, pic_data in enumerate(images_data):
        data = datetime.datetime.strptime(pic_data["date"], '%Y-%m-%d %H:%M:%S')
        prepared_data = data.strftime('%Y/%m/%d')

        name = pic_data["image"]
        url = f"https://api.nasa.gov/EPIC/archive/natural/{prepared_data}/png/{name}.png?api_key={nasa_api}"
        filename = f"epic_image_{index}.png"
        file_path = os.path.join(folder, filename)
        download_pic(file_path, url)
