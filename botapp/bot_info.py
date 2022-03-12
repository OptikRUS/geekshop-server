import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



"""
регистрируем нужного бота в нашем приложении
"""

storage = MemoryStorage()
bot = Bot(token=os.getenv('API_TOKEN'))
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot, storage=storage)

