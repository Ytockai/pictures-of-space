import requests
import sys
import argparse
from functions import download_photo, determine_file_extension, get_response
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-id', nargs='?', default="")
    parser.add_argument ('-path','-p', nargs='?', default="images")
    args = parser.parse_args()
    Path(f'{args.path}').mkdir(parents=True, exist_ok=True)
 
    return parser


def fetch_spacex_last_launch(directory, data_launch):
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
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    data_launch = get_response(url)
    fetch_spacex_last_launch(directory, data_launch)
    print('Done!')

if __name__ == '__main__':
    main()