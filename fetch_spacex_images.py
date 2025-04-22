import requests
import sys
import argparse
from main import download_photo, determine_file_extension
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-id', nargs='?')
    parser.add_argument ('-path','-p', nargs='?', default="images")
    args = parser.parse_args()
    Path(f'{args.path}').mkdir(parents=True, exist_ok=True)
 
    return parser


def fetch_spacex_last_launch(directory, id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response_link = requests.get(url)
    response_link.raise_for_status()
    list_data = response_link.json()
    if isinstance(list_data, list):
        for data in list_data:
            data_url = data['links']['flickr']['original']
            if len(data_url) > 0:
                numbered_list = enumerate(data_url)
                break
    else:
        data_url = list_data['links']['flickr']['original']
        numbered_list = enumerate(data_url)

    for image in numbered_list:
        file_name = 'spacex_{}{}'.format((image[0]), determine_file_extension(image[1]))
        file_path = Path(directory) / file_name
        url_photo = image[1]
        download_photo(file_path, url_photo)


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    if namespace.id:
        id = namespace.id
    else:
        id = ''
    fetch_spacex_last_launch(directory, id)
    print('Done!')

if __name__ == '__main__':
    main()