from aiogram import types
from aiogram.dispatcher.filters import Text
from botapp.bot_info import dp, bot
from botapp.keyboards.keyboard import kb_start, kb_menu


async def start_command(message: types.Message):
    await message.answer("Привет! Это бот магазина GeekShop.", reply_markup=kb_start)  # добавляем набор кнопок


async def menu_command(message: types.Message):
    await message.answer("Привет! Это меню бота.", reply_markup=kb_menu)


async def help_command(message: types.Message):
    await message.answer("Этот бот используется исключительно в целях обучения. По всем вопросам @OptikRUS",
                         reply_markup=kb_menu)


def start_handler(dp):
    """
    передаём сюда готовые контроллеры
    """
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(start_command, Text(equals='Главное меню📎'))
    dp.register_message_handler(menu_command, Text(equals='Меню🧷'))
    dp.register_message_handler(help_command, Text(equals='Помощь💡'))
