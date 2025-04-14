import sys
import telegram
import os
import argparse
from dotenv import load_dotenv
from main import random_list

TOKEN = os.environ["TELEGRAMM_TOKEN"]
BOT = telegram.Bot(token=TOKEN)
CHAT_ID = os.environ["CHAT_ID"]


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-name_image', nargs='?')
    parser.add_argument ('-path','-p', nargs='?', default="images")
 
    return parser

def send_photo(name_photo):
    with open(os.path.join('images',name_photo), 'rb') as photo:
        BOT.send_photo(chat_id=CHAT_ID, photo=photo)
    

def main():
    load_dotenv()
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    if namespace.name_image:
        name_photo = namespace.name_image
    else:
        name_photo = random_list(directory)[0]
    try: 
        send_photo(name_photo)
    except telegram.error.BadRequest:
        print(f'фото {name_photo} слишком большое')

if __name__ == '__main__':
    main()