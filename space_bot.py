import sys
import telegram
import os
import argparse
from dotenv import load_dotenv
from main import random_list

load_dotenv()

TOKEN = os.environ["TELEGRAMM_TOKEN"]

bot = telegram.Bot(token=TOKEN)

chat_id='@myspacephoto'

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('name_image', nargs='?')
 
    return parser

def send_photo(name_photo):
    try:
        bot.send_photo(chat_id=chat_id, photo=open(f'images/{name_photo}', 'rb'))
    except:
        pass


def main():
    directory = 'images'
    parser = createParser()
    namespace = parser.parse_args (sys.argv[1:])
    if namespace.name_image:
        name_photo = namespace.name_image
        send_photo(name_photo)
    else:
        name_photo = random_list(directory)[0]
        send_photo(name_photo)

if __name__ == '__main__':
    main()