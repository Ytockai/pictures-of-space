import requests
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from main import download_photo
from pathlib import Path

Path("images").mkdir(parents=True, exist_ok=True)

URL = 'https://api.nasa.gov/'

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

def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    epic_photo(nasa_token)

if __name__ == '__main__':
    main()