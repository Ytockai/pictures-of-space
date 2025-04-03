import telegram
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["TELEGRAMM_TOKEN"]

bot = telegram.Bot(token=TOKEN)

chat_id='@myspacephoto'

bot.send_photo(chat_id=chat_id, photo=open('images/epic_0.png', 'rb'))