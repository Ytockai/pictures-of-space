import requests
import sys
import os
import argparse
from dotenv import load_dotenv
from functions import download_photo, determine_file_extension, get_response
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-date', '-d', nargs='?')
    parser.add_argument ('-path','-p', nargs='?', default="images")
    args = parser.parse_args()
    Path(f'{args.path}').mkdir(parents=True, exist_ok=True)
 
    return parser

def fetch_apod(nasa_token, directory, date=None):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'start_date': date,
        'api_key': nasa_token,
    }
    photos_data = get_response(url, payload)
    if isinstance(photos_data, list):
        for data in photos_data:
            if "image" in data["media_type"]:
                photo_url = data['url']
                file_name = 'apod_{}{}'.format(data['date'],determine_file_extension(photo_url))
                file_path = Path(directory) / file_name
                download_photo(file_path, photo_url)
            else:
                date = data['date']
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
        fetch_apod(nasa_token, directory, namespace.date)
    else:
        fetch_apod(nasa_token, directory)
    print('Done!')

if __name__ == '__main__':
    main()