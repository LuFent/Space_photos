from dotenv import load_dotenv
from pathlib import Path
from os import listdir
from time import sleep
from random import shuffle

import telegram
import os


def main():
    load_dotenv()
    tg_token = os.getenv("TG_API_TOKEN")

    if os.getenv("PUBLISHING_DELAY"):
        delay = int(os.getenv("PUBLISHING_DELAY"))
    else:
        delay = 86400

    folder = "images"
    files = listdir(folder)
    shuffle(files)

    chat_id = "@space_imgs"
    bot = telegram.Bot(token=tg_token)

    file_num = 0

    while True:
        filename = files[file_num]

        path = os.path.join(folder, filename)
        with open(path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)

        file_num += 1
        sleep(delay)


if __name__ == "__main__":
    main()