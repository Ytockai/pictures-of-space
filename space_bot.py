import telegram
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["TELEGRAMM_TOKEN"]

bot = telegram.Bot(token=TOKEN)

chat_id='@myspacephoto'

def send_photo(name_photo):
    try:
        bot.send_photo(chat_id=chat_id, photo=open(f'images/{name_photo}', 'rb'))
    except:
        pass
