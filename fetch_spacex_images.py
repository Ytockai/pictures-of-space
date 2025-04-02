import requests
import sys
import argparse
from main import download_photo, file_extension
from pathlib import Path

Path("images").mkdir(parents=True, exist_ok=True)

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('id', nargs='?')
 
    return parser


def fetch_spacex_last_launch(url):
    response_link = requests.get(url)
    response_link.raise_for_status()
    list_data = response_link.json()
    if isinstance(list_data, list):
        for i in list_data:
            if len(i['links']['flickr']['original'])>0:
                numbered_list = enumerate(i['links']['flickr']['original'])#что-то странное одинаковый код!!!
                break
    else:
        numbered_list = enumerate(list_data['links']['flickr']['original'])# и тут делает одно и то-же

    for image in numbered_list:
        file_name = 'spacex_'+ str(image[0]) + file_extension(image[1])
        file_path = Path("images") / file_name
        url_photo = image[1]
        download_photo(file_path, url_photo)


def main():
    parser = createParser()
    namespace = parser.parse_args (sys.argv[1:])
    if namespace.id:
        url = f'https://api.spacexdata.com/v5/launches/{namespace.id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches'
    fetch_spacex_last_launch(url)
    print('Done!')

if __name__ == '__main__':
    main()