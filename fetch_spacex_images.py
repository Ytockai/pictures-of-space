import requests
import sys
import argparse
from main import download_photo, determine_file_extension
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-id', nargs='?', default="")
    parser.add_argument ('-path','-p', nargs='?', default="images")
    args = parser.parse_args()
    Path(f'{args.path}').mkdir(parents=True, exist_ok=True)
 
    return parser


def fetch_spacex_last_launch(directory, launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    data_launch = response.json()
    if isinstance(data_launch, list):
        for data in data_launch:
            data_url = data['links']['flickr']['original']
            if len(data_url) > 0:
                break
    else:
        data_url = data_launch['links']['flickr']['original']

    for index, image_url in enumerate(data_url):
        file_name = 'spacex_{}{}'.format(index, determine_file_extension(image_url))
        file_path = Path(directory) / file_name
        download_photo(file_path, image_url)


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    launch_id = namespace.id
    fetch_spacex_last_launch(directory, launch_id)
    print('Done!')

if __name__ == '__main__':
    main()