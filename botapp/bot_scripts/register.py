from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from asgiref.sync import sync_to_async

from botapp.keyboards.keyboard import kb_profile, kb_register_profile, kb_register_cancel
from botapp.bot_scripts.auth import get_user

from users.models import User


class RegisterUser(StatesGroup):
    username = State()
    first_name = State()
    last_name = State()
    email = State()
    password = State()
    age = State()


@sync_to_async
def exist_user(username):
    return User.objects.filter(username=username).exists()


@sync_to_async
def register_user(username, first_name, last_name, email, password, age, telegram_username, telegram_id):
    return User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        age=age,
        telegram_username=telegram_username,
        telegram_id=telegram_id
    )


async def register_command(message: types.Message):
    tg_username = message.from_user.username
    try:
        await get_user('@' + tg_username)
    except:
        await message.answer('Начнём регистрацию', reply_markup=kb_register_profile)
    else:
        await message.answer('Вы уже зарегистрированный пользователь!', reply_markup=kb_profile)


async def register_profile_command(message: types.Message):
    await RegisterUser.username.set()
    await message.reply('Введите логин: ', reply_markup=kb_register_cancel)


async def add_username(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await RegisterUser.next()
    await message.reply('Теперь имя', reply_markup=kb_register_cancel)


async def add_first_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await RegisterUser.next()
    await message.reply('Фамилия:', reply_markup=kb_register_cancel)


async def add_last_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await RegisterUser.next()
    await message.reply('Введите почту', reply_markup=kb_register_cancel)


async def add_email(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await RegisterUser.next()
    await message.reply('Введите пароль', reply_markup=kb_register_cancel)


async def add_password(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
    await RegisterUser.next()
    await message.reply('Введите возраст', reply_markup=kb_register_cancel)


async def add_age(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
        except:
            await message.answer('Некорректные данные', reply_markup=kb_register_cancel)
        else:
            await register_user(data['username'], data['first_name'], data['last_name'], data['email'],
                                data['password'], data['age'], '@' + message.from_user.username, message.from_user.id)
            await message.answer(
                f"Вы успешно зарегистрированы!\n"
                f"Логин: {data['username']}\n"
                f"Имя: {data['first_name']}\n"
                f"Фамилия: {data['last_name']}\n"
                f"Email: {data['email']}\n"
                f"Пароль: {data['password']}\n"
                f"Телеграм: @{message.from_user.username}\n"
                f"telegram_id: {message.from_user.id}\n"
                f"Возраст: {data['age']}\n", reply_markup=kb_profile
            )
            await state.finish()


async def register_cancel_handler(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Изменения отменены', reply_markup=kb_register_profile)


async def test_command(message: types.Message):
    await message.answer("тест")


def register_handler(dp):
    dp.register_message_handler(register_command, commands=['register'])
    dp.register_message_handler(register_profile_command, commands=['register_profile'], state=None)
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
