from dotenv import load_dotenv
from os import listdir
from pathlib import Path
from time import sleep
from random import shuffle
from general_funcs import download_pic
import fetch_spacex
import fetch_nasa

import telegram
import os
import subprocess


def main():
    folder = "images"
    Path(folder).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_TOKEN")
    tg_token = os.getenv("TG_API_TOKEN")
    delay = int(os.getenv("PUBLISHING_DELAY", default=86400))
    chat_id = os.getenv("CHAT_ID", default="@space_imgs")

    amount_of_spacex_photos = 5
    print("Идет скачивание изображений")
    fetch_spacex.fetch_spacex_last_launch(amount_of_spacex_photos, folder)
    fetch_nasa.download_nasa_APOD_images(nasa_api_token, folder)
    fetch_nasa.download_nasa_EPIC_images(nasa_api_token, folder)

    files = listdir(folder)
    shuffle(files)
    bot = telegram.Bot(token=tg_token)

    sent_photos = []
    file_num = 0

    while True:
        try:
            filename = files[file_num]

            path = os.path.join(folder, filename)
            with open(path, 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)

            sent_photos.append(filename)
            file_num += 1
            sleep(delay)

        except IndexError:
            new_files = list(set(listdir(folder)).difference(set(files), set(sent_photos)))
            
            if new_files:
                files = new_files
                file_num = 0
            else:
                print("У бота закончились фотографии")
                break


if __name__ == "__main__":
    main()