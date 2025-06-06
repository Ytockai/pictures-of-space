import sys
import telegram
import os
import argparse
from dotenv import load_dotenv
from functions import shuffle_list


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-name_image', nargs='?')
    parser.add_argument ('-path','-p', nargs='?', default="images")
 
    return parser

def send_photo(name_photo, directory, bot, tg_chat_id):
    with open(os.path.join(directory ,name_photo), 'rb') as photo:
        bot.send_photo(chat_id=tg_chat_id, photo=photo)
    

def main():
    load_dotenv()
    token = os.environ["TELEGRAMM_TOKEN"]
    bot = telegram.Bot(token=token)
    tg_chat_id = os.environ["TELEGRAMM_CHAT_ID"]
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    if namespace.name_image:
        photo_name = namespace.name_image
    else:
        photo_name = shuffle_list(directory)[0]
    try: 
        send_photo(photo_name, directory, bot, tg_chat_id)
    except telegram.error.BadRequest:
        print(f'фото {photo_name} слишком большое')

if __name__ == '__main__':
    main()