from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from faker import Faker

from botapp.bot_scripts.games.hangman.elements.const import HANGMAN, rules, LOCK_SYMBOL
from botapp.keyboards.keyboard import kb_hangman, kb_cancel_hangman
from botapp.bot_scripts.games.hangman.elements.tools import get_show_word, letter_valid


hangman_state = [' ']
used_letters = []
wrongs = []


class HangMan(StatesGroup):
    state = State()


async def play_hangman_command(message: types.Message):
    await message.answer('Добро пожаловать в игру "Виселица"! Начнём?', reply_markup=kb_hangman)


async def help_hangman_command(message: types.Message):
    await message.answer(f'<u>Правила игры "Виселица"</u>\n{rules}', reply_markup=kb_hangman, parse_mode="HTML")


async def start_hangman_command(message: types.Message, state=FSMContext):
    used_letters.clear()
    wrongs.clear()
    hangman_state.clear()
    hangman_state.append(' ')
    async with state.proxy() as data:
        data['word'] = Faker('ru_RU').word().upper()
    await message.answer(f'{HANGMAN[0]}{LOCK_SYMBOL * len(data["word"])}')
    await HangMan.state.set()

    await message.answer('Введите букву:', reply_markup=kb_cancel_hangman)


async def game_procces_command(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        word = data['word']
    if await letter_valid(message.text):
        letter = message.text.upper()
        if letter in used_letters:
            await message.answer(f'Вы уже использовали букву <b>{letter}</b>!\n'
                                 f'{HANGMAN[len(wrongs)]} {hangman_state[-1]}\nИспользованные буквы:\n{used_letters}',
                                 reply_markup=kb_cancel_hangman, parse_mode="HTML")
        else:
            used_letters.append(letter)
            hide_word_state = await get_show_word(word, letter, LOCK_SYMBOL, hangman_state[-1])
            hangman_state.append(hide_word_state)
            if not word.count(letter):
                wrongs.append(letter)
            await message.answer(f'{HANGMAN[len(wrongs)]} {hangman_state[-1]}\nИспользованные буквы:\n{used_letters}',
                                 reply_markup=kb_cancel_hangman)
            if len(wrongs) == 5:
                await message.answer(f'Вы проиграли!\nЗагаданное слово:\n{word}', reply_markup=kb_hangman)
                await state.finish()
            if word == hangman_state[-1]:
                await message.answer('Вы выиграли!')
                await message.answer(f'{HANGMAN[6]}',
                                     reply_markup=kb_hangman)
                await state.finish()
    else:
        await message.answer('Некорректный ввод, Попробуйте ещё раз!', reply_markup=kb_cancel_hangman)


async def hangman_cancel_handler(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Вы вышли из игры!', reply_markup=kb_hangman)


def hangman_handler(dp):
    dp.register_message_handler(play_hangman_command, commands=['hangman'], state=None)
    dp.register_message_handler(help_hangman_command, commands=['help_hangman'], state=None)
    dp.register_message_handler(start_hangman_command, commands=['play_hangman'], state=None)
    # # хендлер отмены должен быть тут, чтобы корректно работать
    dp.register_message_handler(hangman_cancel_handler, state='*', commands='cancel_hangman')
    dp.register_message_handler(hangman_cancel_handler, Text(equals='cancel_hangman', ignore_case=True), state='*')
    dp.register_message_handler(game_procces_command, state=HangMan.state)
