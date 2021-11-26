from dotenv import load_dotenv
from os import listdir
from pathlib import Path
from time import sleep
from random import shuffle
import fetch_spacex
import fetch_nasa

import telegram
import os


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
    fetch_nasa.download_nasa_apod_images(nasa_api_token, folder)
    fetch_nasa.download_nasa_epic_images(nasa_api_token, folder)

    files = listdir(folder)
    shuffle(files)
    bot = telegram.Bot(token=tg_token)

    for file in files:
        path = os.path.join(folder, file)
        with open(path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)

        sleep(delay)


if __name__ == "__main__":
    main()