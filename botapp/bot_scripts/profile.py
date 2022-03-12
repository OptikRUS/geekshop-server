from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from asgiref.sync import sync_to_async

from botapp.keyboards.keyboard import kb_profile, kb_edit_profile, kb_cancel, kb_register
from botapp.bot_scripts.auth import get_user


class AddUserInfo(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    photo = State()


@sync_to_async
def edit_profile(user, first_name, last_name, age):
    user.first_name = first_name
    user.last_name = last_name
    user.age = age
    return user.save()


async def profile_command(message: types.Message):
    try:
        user = await get_user('@' + message.from_user.username)
    except:
        await message.answer('Вы не зарегистрированы', reply_markup=kb_register)
    else:
        if user.is_active:
            await message.answer(
                f'Вот ваш профиль GeekShop:'
                f'\nЛогин: {user.username}'
                f'\nИмя: {user.first_name}'
                f'\nФамилия: {user.last_name}'
                f'\nТелеграм: {user.telegram_username}'
                f'\nEmail: {user.email}'
                f'\nФото профиля: {user.image}'
                f'\nВозраст: {user.age}'
                f'\nБыл в сети GeekShop: {user.last_login}', reply_markup=kb_edit_profile
            )
        else:
            await message.answer(f'Ваш профиль неактивен. Обратитесь к администратору: @OptikRUS')


async def edit_profile_command(message: types.Message):
    await AddUserInfo.first_name.set()
    await message.reply('Введи имя: ', reply_markup=kb_cancel)


async def add_first_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await AddUserInfo.next()
    await message.reply('Теперь фамилию', reply_markup=kb_cancel)


async def add_last_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await AddUserInfo.next()
    await message.reply('Введите возраст', reply_markup=kb_cancel)


async def add_age(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
        except:
            await message.answer('Некорректные данные', reply_markup=kb_cancel)
        else:
            user = await get_user('@' + message.from_user.username)
            await edit_profile(user, data['first_name'], data['last_name'], data['age'])
            await message.answer(
                f"Профиль успешно изменён!\n"
                f"Имя: {data['first_name']}\n"
                f"Фамилия: {data['last_name']}\n"
                f"Возраст: {data['age']}\n", reply_markup=kb_profile
            )
            await state.finish()


async def cancel_handler(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Изменения отменены', reply_markup=kb_profile)


def profile_handler(dp):
    """
    передаём сюда готовые контроллеры
    """
    dp.register_message_handler(profile_command, commands=['profile'])
    dp.register_message_handler(edit_profile_command, commands=['edit_profile'], state=None)
    # хендлер отмены должен быть тут, чтобы корректно работать
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(add_first_name, state=AddUserInfo.first_name)
    dp.register_message_handler(add_last_name, state=AddUserInfo.last_name)
    dp.register_message_handler(add_age, state=AddUserInfo.age)
