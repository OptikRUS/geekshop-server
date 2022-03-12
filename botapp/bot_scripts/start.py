from aiogram import types
from botapp.bot_info import dp, bot
from botapp.keyboards.keyboard import kb_start


# @dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer("Привет! Это простейший бот на aiogram.", reply_markup=kb_start)  # добавляем набор кнопок


def start_handler(dp):
    """
    передаём сюда готовые контроллеры
    """
    dp.register_message_handler(start_command, commands=['start'])
