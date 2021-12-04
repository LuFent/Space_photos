from general_funcs import download_pic

import requests
import os


def fetch_spacex_last_launch(amount_of_photos, folder):
    if amount_of_photos > 25:
        amount_of_photos = 25

    url = "https://api.spacexdata.com/v4/launches/"
    response = requests.get(url)
    response.raise_for_status()
    flights = response.json()

    for flight in flights:
        if len(flight["links"]["flickr"]["original"]) >= amount_of_photos:
            image_urls = flight["links"]["flickr"]["original"]
            break

    for index, url in enumerate(image_urls):
        filename = f"spacex_image_{index}.jpg"
        file_path = os.path.join(folder, filename)
        download_pic(file_path, url)
