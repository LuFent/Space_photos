import requests
import os

from urllib.parse import urlparse


def download_pic(dir, url):
    response = requests.get(url)
    response.raise_for_status()

    with open(dir, 'wb') as file:
        file.write(response.content)


def get_file_extension(path):
    return os.path.splitext(urlparse(path).path)[1]