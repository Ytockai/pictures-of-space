import requests
import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from os.path import splitext
from dotenv import load_dotenv

Path("images").mkdir(parents=True, exist_ok=True)

URL = 'https://api.nasa.gov/'

def download_photo(file_path, url_photo):
    with open(file_path, 'wb') as file:
            response = requests.get(url_photo)
            response.raise_for_status()
            file.write(response.content)


def apod(url, nasa_token):
    url_apod = 'planetary/apod'
    payload = {
        'api_key': nasa_token,
    }
    
    response = requests.get(f'{url}{url_apod}', params=payload)
    response.raise_for_status()
    list = response.url
    print(list)


def epic_photo(nasa_token):
    url_epic = 'EPIC/api/natural/'
    payload = {
        'images': '',
        'api_key': nasa_token,
    }

    response = requests.get(f'{URL}{url_epic}', params=payload)
    response.raise_for_status()
    url_key = response.json()
    numbered_url_key = enumerate(url_key)
    for i in numbered_url_key:
        date = datetime.strptime(i[1]['date'], '%Y-%m-%d %H:%M:%S')
        year = date.year
        month = str(date.month).zfill(2)
        day = str(date.day).zfill(2)
        name_photo = i[1]['image']
        url_photo = f'{URL}EPIC/archive/natural/{year}/{month}/{day}/png/{name_photo}.png?api_key={payload["api_key"]}'
        file_name = 'epic_'+ str(i[0]) + '.png'
        file_path = Path("images") / file_name
        download_photo(file_path, url_photo)


def file_extension(url):
    filename = urlparse(url)
    extension = splitext(filename.path)
    return extension[1]

def fetch_spacex_last_launch(url):
    response_link = requests.get(url)
    response_link.raise_for_status()
    list_image = response_link.json()
    numbered_list = enumerate(list_image)
    for image in numbered_list:
        file_name = 'spacex_'+ str(image[0]) + file_extension(image[1]['url'])
        url_photo = image[1]['url']
        file_path = Path("images") / file_name
        with open(file_path, 'wb') as file:
            response = requests.get(url_photo)
            response.raise_for_status()
            file.write(response.content)

def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    apod(URL, nasa_token)
    print('Done!')

if __name__ == '__main__':
    main()