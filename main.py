import requests
from pathlib import Path

Path("images").mkdir(parents=True, exist_ok=True)

def fetch_spacex_last_launch(url):
    response_link = requests.get(url)
    response_link.raise_for_status()
    list_image = response_link.json()["links"]['flickr']["original"]
    numbered_list = enumerate(list_image)
    for image in numbered_list:
        file_name = 'spacex_'+ str(image[0]) + '.jpg'
        file_path = Path("images") / file_name
        with open(file_path, 'wb') as file:
            response = requests.get(image[1])
            response.raise_for_status()
            file.write(response.content)

def main():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    fetch_spacex_last_launch(url)
    print('Done!')

if __name__ == '__main__':
    main()