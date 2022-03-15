from aiogram import types
from botapp.keyboards.keyboard import kb_games
from aiogram.dispatcher.filters import Text


async def games_command(message: types.Message):
    await message.answer("Во что будем играть?", reply_markup=kb_games)


def games_handler(dp):
    dp.register_message_handler(games_command, Text(equals='Игры🎮'))
