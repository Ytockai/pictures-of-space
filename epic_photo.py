import argparse
import requests
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from main import download_photo
from pathlib import Path


URL = 'https://api.nasa.gov/'

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-path','-p', nargs='?', default="images")
    args = parser.parse_args()
    Path(f'{args.path}').mkdir(parents=True, exist_ok=True)
 
    return parser

def download_epic_photo(nasa_token, directory):
    url_epic = 'EPIC/api/natural/'
    payload = {
        'images': '',
        'api_key': nasa_token,
    }

    response = requests.get(f'{URL}{url_epic}', params=payload)
    response.raise_for_status()
    list_data_photo = response.json()
    numbered_list = enumerate(list_data_photo)
    for data_photo in numbered_list:
        date = datetime.strptime(data_photo[1]['date'], '%Y-%m-%d %H:%M:%S')
        date_photo = date.strftime('%Y/%m/%d')
        name_photo = data_photo[1]['image']
        photo_url = f'{URL}EPIC/archive/natural/{date_photo}/png/{name_photo}.png'
        photo_payload = {
            'api_key': nasa_token,
        }
        photo_response = requests.get(photo_url, params=photo_payload)
        response.raise_for_status()
        file_name = 'epic_{}.png'.format(data_photo[0])
        file_path = Path(directory) / file_name
        download_photo(file_path, photo_response.url)

def main():
    load_dotenv()
    parser = create_parser()
    directory = parser.parse_args().path
    nasa_token = os.environ["NASA_TOKEN"]
    download_epic_photo(nasa_token, directory)

if __name__ == '__main__':
    main()