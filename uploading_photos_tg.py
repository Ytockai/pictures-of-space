import sys
import time as t
import argparse
from space_bot import send_photo
from main import shuffle_list


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-time', nargs='?', default=14400)
    parser.add_argument ('-path','-p', nargs='?', default="images")
 
    return parser

def upload_photo(time, directory):
    while True:
        for filesindirs in shuffle_list(directory):
            t.sleep(time)
            send_photo(filesindirs, directory)

def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    directory = namespace.path
    upload_photo(int(namespace.time), directory)

if __name__ == '__main__':
    main()