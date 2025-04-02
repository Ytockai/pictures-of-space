import requests
from pathlib import Path
from urllib.parse import urlparse
from os.path import splitext

Path("images").mkdir(parents=True, exist_ok=True)

URL = 'https://api.nasa.gov/'

def download_photo(file_path, url_photo):
    with open(file_path, 'wb') as file:
            response = requests.get(url_photo)
            response.raise_for_status()
            file.write(response.content)

def file_extension(url):
    filename = urlparse(url)
    extension = splitext(filename.path)
    return extension[1]

def main():
    pass

if __name__ == '__main__':
    main()