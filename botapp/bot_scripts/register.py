from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from botapp.keyboards.keyboard import kb_profile, kb_register, kb_register_cancel
from botapp.views import get_user, exist_user, register_user
from botapp.validators import email_valid, password_valid, login_valid


class RegisterUser(StatesGroup):
    username = State()
    first_name = State()
    last_name = State()
    email = State()
    password = State()
    age = State()


async def register_profile_command(message: types.Message):
    try:
        await get_user(message.from_user.id)
    except:
        await RegisterUser.username.set()
        await message.reply('Придумайте логин: ', reply_markup=kb_register_cancel)
    else:
        await message.answer('Вы зарегистрированный пользователь', reply_markup=kb_profile)


async def add_username(message: types.Message, state=FSMContext):
    if await exist_user(message.text.lower()):
        await message.answer(f'Пользователь <b>{message.text}</b> уже существует, придумайте другой логин',
                             parse_mode='HTML',
                             reply_markup=kb_register_cancel)
        return
    elif not login_valid(message.text):
        await message.answer('Некорректный логин, придумайте другой', reply_markup=kb_register_cancel)
        return
    async with state.proxy() as data:
        data['username'] = message.text.lower()
    await RegisterUser.next()
    await message.reply('Как вас зовут?', reply_markup=kb_register_cancel)


async def add_first_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await RegisterUser.next()
    await message.answer('Фамилия:', reply_markup=kb_register_cancel)


async def add_last_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await RegisterUser.next()
    await message.answer('Электронная почта:', reply_markup=kb_register_cancel)


async def add_email(message: types.Message, state=FSMContext):
    if not email_valid(message.text):
        await message.answer('Некорректный Email, попробуйте ещё раз!', reply_markup=kb_register_cancel)
        return
    async with state.proxy() as data:
        data['email'] = message.text
    await RegisterUser.next()
    await message.answer('Придумайте пароль:', reply_markup=kb_register_cancel)


async def add_password(message: types.Message, state=FSMContext):
    if not password_valid(message.text):
        await message.answer('Некорректный или ненадёжный пароль, попробуйте ещё раз!',
                             reply_markup=kb_register_cancel)
        return
    async with state.proxy() as data:
        data['password'] = message.text
    await RegisterUser.next()
    await message.reply('Введите возраст', reply_markup=kb_register_cancel)


async def add_age(message: types.Message, state=FSMContext):
    try:
        tg_username = message.from_user.username
    except:
        tg_username = ''
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
        except:
            await message.answer('Некорректные данные, попробуйте ещё раз', reply_markup=kb_register_cancel)
        else:
            await register_user(
                username=data['username'], first_name=data['first_name'], last_name=data['last_name'],
                email=data['email'], password=data['password'], age=data['age'],
                telegram_username=tg_username, telegram_id=message.from_user.id)
            await message.answer(
                f"<u>Вы успешно зарегистрированы!</u>\n"
                f"Логин: {data['username']}\n"
                f"Имя: {data['first_name']}\n"
                f"Фамилия: {data['last_name']}\n"
                f"Email: {data['email']}\n"
                f"Пароль: {data['password']}\n"
                f"Телеграм: {message.from_user.username}\n"
                f"Telegram_ID: {message.from_user.id}\n"
                f"Возраст: {data['age']}\n", reply_markup=kb_profile, parse_mode="HTML")
            await state.finish()


async def register_cancel_handler(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Изменения отменены', reply_markup=kb_register)


async def test_command(message: types.Message):
    await message.answer("тест")


def register_handler(dp):
    dp.register_message_handler(register_profile_command, commands=['register'], state=None)
    # # хендлер отмены должен быть тут, чтобы корректно работать
    dp.register_message_handler(register_cancel_handler, state='*', commands=['cancel_registration'])
    dp.register_message_handler(register_cancel_handler, Text(equals='cancel_registration', ignore_case=True),
                                state='*')
    dp.register_message_handler(add_username, state=RegisterUser.username)
    dp.register_message_handler(add_first_name, state=RegisterUser.first_name)
    dp.register_message_handler(add_last_name, state=RegisterUser.last_name)
    dp.register_message_handler(add_email, state=RegisterUser.email)
    dp.register_message_handler(add_password, state=RegisterUser.password)
    dp.register_message_handler(add_age, state=RegisterUser.age)
    dp.register_message_handler(test_command, state='*', commands=['test'])
