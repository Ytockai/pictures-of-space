import requests
from pathlib import Path

Path("images").mkdir(parents=True, exist_ok=True)

def list_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_image(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)

def main():
    url = input('введите адресс картинки:')
    numbered_list = enumerate(list_image(url)["links"]['flickr']["original"])
    for image in numbered_list:
        file_name = 'spacex_'+ str(image[0]) + '.jpg'
        file_path = Path("images") / file_name
        download_image(image[1], file_path)
    print('Done!')

if __name__ == '__main__':
    main()