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


def fetch_spacex_last_launch(directory, id_launch):
    url = f'https://api.spacexdata.com/v5/launches/{id_launch}'
    response_url = requests.get(url)
    response_url.raise_for_status()
    data_launch = response_url.json()
    if isinstance(data_launch, list):
        for data in data_launch:
            data_url = data['links']['flickr']['original']
            if len(data_url) > 0:
                numbered_list = enumerate(data_url)
                break
    else:
        data_url = data['links']['flickr']['original']
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
        id_launch = namespace.id
    else:
        id_launch = ''
    fetch_spacex_last_launch(directory, id_launch)
    print('Done!')

if __name__ == '__main__':
    main()