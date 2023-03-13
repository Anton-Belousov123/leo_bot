from aiogram import Dispatcher, Bot

from misc.secrets import secret_info

TOKEN = secret_info.TELEGRAM_API_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
from handlers import dp