import requests
import random 
import os
from urllib.parse import urlparse
from os.path import splitext

URL = 'https://api.nasa.gov/'

def shuffle_list(directory):
    filesindir = os.listdir(directory)
    random.shuffle(filesindir)
    filesrandom = filesindir
    return filesrandom

def download_photo(file_path, url_photo):
    with open(file_path, 'wb') as file:
            response = requests.get(url_photo)
            response.raise_for_status()
            file.write(response.content)

def determine_file_extension(url):
    filename = urlparse(url)
    extension = splitext(filename.path)
    return extension[1]
