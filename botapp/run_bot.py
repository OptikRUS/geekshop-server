import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geekshop.settings")
django.setup()

from aiogram import executor
from bot_info import dp
from bot_scripts import start
from bot_scripts.users import auth, profile, register
from bot_scripts.games.hangman import hangman
from bot_scripts.games import games


async def on_statup(_):
    print('Бот онлайн')


"""регистрируем здесь наши контроллеры"""

start.start_handler(dp)
auth.auth_handlers(dp)
profile.profile_handler(dp)
register.register_handler(dp)
games.games_handler(dp)
hangman.hangman_handler(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_statup)
