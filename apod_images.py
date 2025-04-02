import requests
import sys
import os
import argparse
from dotenv import load_dotenv
from main import download_photo, file_extension
from pathlib import Path

Path("images").mkdir(parents=True, exist_ok=True)

URL = 'https://api.nasa.gov/'

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('date', nargs='?')
 
    return parser

def apod(url, nasa_token, date=None):
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
                file_name = ' apod_'+ str(i['date']) + file_extension(url_photo)
                file_path = Path("images") / file_name
                download_photo(file_path, url_photo)
            else:
                date = i['date']
                print(f'фото нет за {date}')
    else:
        url_photo = list_data['url']
        file_name = 'apod_'+ str(list_data['date']) + file_extension(url_photo)
        file_path = Path("images") / file_name
        download_photo(file_path, url_photo)



def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    parser = createParser()
    namespace = parser.parse_args (sys.argv[1:])
    if namespace.date:
        apod(URL, nasa_token, namespace.date)
    else:
        apod(URL, nasa_token)
    print('Done!')

if __name__ == '__main__':
    main()