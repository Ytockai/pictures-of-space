import telegram
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["TELEGRAMM_TOKEN"]

bot = telegram.Bot(token=TOKEN)

bot.send_message(chat_id='@myspacephoto', text="Привет")