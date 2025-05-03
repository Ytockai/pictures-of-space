import requests
import sys
import os
import argparse
from dotenv import load_dotenv
from main import download_photo, determine_file_extension
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-date', '-d', nargs='?')
    parser.add_argument ('-path','-p', nargs='?', default="images")
    args = parser.parse_args()
    Path(f'{args.path}').mkdir(parents=True, exist_ok=True)
 
    return parser

def download_apod(nasa_token, directory, date=None):
    apod_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'start_date': date,
        'api_key': nasa_token,
    }
    
    response = requests.get(f'{apod_url}', params=payload)
    response.raise_for_status()
    photos_data = response.json()
    if isinstance(photos_data, list):
        for i in photos_data:
            if "image" in i["media_type"]:
                photo_url = i['url']
                file_name = 'apod_{}{}'.format(i['date'],determine_file_extension(photo_url))
                file_path = Path(directory) / file_name
                download_photo(file_path, photo_url)
            else:
                date = i['date']
                print(f'фото нет за {date}')
    else:
        photo_url = photos_data['url']
        file_name = 'apod_{}{}'.format(photos_data['date'],determine_file_extension(photo_url))
        file_path = Path(directory) / file_name
        download_photo(file_path, photo_url)



def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    if namespace.date:
        download_apod(nasa_token, directory, namespace.date)
    else:
        download_apod(nasa_token, directory)
    print('Done!')

if __name__ == '__main__':
    main()