from aiogram import Bot, Dispatcher
from config import BOT_API_TOKEN

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)
