import sys
import os
import telegram
import time as t
import argparse
from dotenv import load_dotenv
from space_bot import send_photo
from functions import shuffle_list


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-time', nargs='?', default=14400, type=int)
    parser.add_argument ('-path','-p', nargs='?', default="images")
 
    return parser

def upload_photos(time, directory, bot, tg_chat_id):
    while True:
        for file in shuffle_list(directory):
            try:
                send_photo(file, directory, bot, tg_chat_id)
                t.sleep(time)
            except telegram.error.NetworkError:
                print('что-то с соединением, попробуем снова через 15 секунд')
                t.sleep(15)
def main():
    load_dotenv()
    token = os.environ["TELEGRAMM_TOKEN"]
    bot = telegram.Bot(token=token)
    tg_chat_id = os.environ["TELEGRAMM_CHAT_ID"]
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    upload_photos(namespace.time, directory, bot, tg_chat_id)

if __name__ == '__main__':
    main()