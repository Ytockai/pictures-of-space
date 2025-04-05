import random 
import os
import sys
import time as t
import argparse
from space_bot import send_photo


directory = 'images'

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', nargs='?', default=14400)
 
    return parser

def uploading_photo(time):
    filesindir = os.listdir(directory)
    while True:
        random.shuffle(filesindir)
        filesrandom = filesindir
        for filesindirs in filesrandom:
            t.sleep(time)
            send_photo(filesindirs)

def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    uploading_photo(int(namespace.time))

if __name__ == '__main__':
    main()