import requests
import sys
import os
import argparse
from dotenv import load_dotenv
from main import download_photo, determine_file_extension
from pathlib import Path


URL = 'https://api.nasa.gov/'

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-date', '-d', nargs='?')
    parser.add_argument ('-path','-p', nargs='?', default="images")
    args = parser.parse_args()
    Path(f'{args.path}').mkdir(parents=True, exist_ok=True)
 
    return parser

def download_apod(url, nasa_token, directory, date=None):
    url_apod = 'planetary/apod'
    payload = {
        'start_date': date,
        'api_key': nasa_token,
    }
    
    response = requests.get(f'{url}{url_apod}', params=payload)
    response.raise_for_status()
    list_data = response.json()
    if isinstance(list_data, list):
        for i in list_data:
            if "image" in i["media_type"]:
                url_photo = i['url']
                file_name = f'apod_{str(i['date'])}{determine_file_extension(url_photo)}'
                file_path = Path(f"{directory}") / file_name
                download_photo(file_path, url_photo)
            else:
                date = i['date']
                print(f'фото нет за {date}')
    else:
        url_photo = list_data['url']
        file_name = f'apod_{str(list_data['date'])}{determine_file_extension(url_photo)}'
        file_path = Path(f"{directory}") / file_name
        download_photo(file_path, url_photo)



def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    if namespace.date:
        download_apod(URL, nasa_token, directory, namespace.date)
    else:
        download_apod(URL, nasa_token, directory)
    print('Done!')

if __name__ == '__main__':
    main()