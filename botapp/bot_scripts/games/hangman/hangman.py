from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from faker import Faker

from .elements.const import HANGMAN, rules, LOCK_SYMBOL
from botapp.keyboards.keyboard import kb_hangman, kb_cancel_hangman
from .elements.tools import get_show_word, letter_valid


class HangMan(StatesGroup):
    state = State()


async def play_hangman_command(message: types.Message):
    await message.answer('Добро пожаловать в игру "Виселица"! Начнём?', reply_markup=kb_hangman)


async def help_hangman_command(message: types.Message):
    await message.answer(f'<u>Правила игры "Виселица"</u>\n{rules}', reply_markup=kb_hangman, parse_mode="HTML")


async def start_hangman_command(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['word'] = Faker('ru_RU').word().upper()
        data['wrongs'] = []
        data['hangman_state'] = [' ']
        data['used_letters'] = []
    await message.answer(f'{HANGMAN[0]}{LOCK_SYMBOL * len(data["word"])}')
    await HangMan.state.set()

    await message.answer('Введите букву:', reply_markup=kb_cancel_hangman)


async def game_procces_command(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        word = data['word']
        wrongs = data['wrongs']
        hangman_state = data['hangman_state']
        used_letters = data['used_letters']
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
    async with state.proxy() as data:
        try:
            await message.answer(f'Вы вышли из игры!\nЗагаданное слово:\n{data["word"]}', reply_markup=kb_hangman)
        except:
            print('Ошибка кнопки')
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()


def hangman_handler(dp):
    dp.register_message_handler(play_hangman_command, Text(equals='Виселица🪜'), state=None)
    dp.register_message_handler(help_hangman_command, Text(equals='Правила🪜'), state=None)
    dp.register_message_handler(start_hangman_command, Text(equals='Играть🪜'), state=None)
    # # хендлер отмены должен быть тут, чтобы корректно работать
    dp.register_message_handler(hangman_cancel_handler, Text(equals='Выйти из игры ❌', ignore_case=True), state='*')
    dp.register_message_handler(game_procces_command, state=HangMan.state)
