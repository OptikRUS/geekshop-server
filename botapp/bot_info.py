import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv('../.env')

"""
регистрируем нужного бота в нашем приложении
"""

storage = MemoryStorage()
bot = Bot(token=os.getenv('API_TOKEN'))
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot, storage=storage)

