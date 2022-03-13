from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from botapp.keyboards.keyboard import kb_profile, kb_edit_profile, kb_cancel, kb_login
from botapp.views import get_user, edit_profile


class AddUserInfo(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()


async def profile_command(message: types.Message):
    try:
        user = await get_user(message.from_user.id)
    except:
        await message.answer('Вы не авторизированы! Войти через телеграм?', reply_markup=kb_login)
    else:
        if user.is_active:
            await message.answer(
                f'<u>Вот ваш профиль GeekShop:</u>'
                f'\nЛогин: {user.username}'
                f'\nИмя: {user.first_name}'
                f'\nФамилия: {user.last_name}'
                f'\nТелеграм: {user.telegram_username}'
                f'\nТелеграм_ID: {user.telegram_id}'
                f'\nEmail: {user.email}'
                f'\nВозраст: {user.age}'
                f'\nБыл в сети GeekShop: {user.last_login}', reply_markup=kb_edit_profile, parse_mode="HTML")
        else:
            await message.answer(f'Ваш профиль неактивен. Обратитесь к администратору: @OptikRUS')


async def edit_profile_command(message: types.Message):
    try:
        await get_user(message.from_user.id)
    except:
        await message.answer('Вы не авторизованы! Войти через телеграм?', reply_markup=kb_login)
    else:
        await AddUserInfo.first_name.set()
        await message.answer('Введи имя: ', reply_markup=kb_cancel)


async def add_first_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await AddUserInfo.next()
    await message.answer('Теперь фамилию:', reply_markup=kb_cancel)


async def add_last_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await AddUserInfo.next()
    await message.answer('Введите возраст:', reply_markup=kb_cancel)


async def add_age(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
        except:
            await message.answer('Некорректные данные', reply_markup=kb_cancel)
        else:
            user = await get_user(message.from_user.id)
            try:
                tg_username = message.from_user.username
            except:
                tg_username = ''
            await edit_profile(user=user, first_name=data['first_name'], last_name=data['last_name'],
                               age=data['age'], telegram_username=tg_username)
            await message.answer(
                f"<u>Профиль успешно изменён!</u>\n"
                f"Имя: {data['first_name']}\n"
                f"Фамилия: {data['last_name']}\n"
                f"Телеграм: @{tg_username}\n"
                f"Telegram_ID: {message.from_user.id}\n"
                f"Возраст: {data['age']}\n", reply_markup=kb_profile, parse_mode="HTML")
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
