from aiogram import types

from asgiref.sync import sync_to_async

from botapp.keyboards.keyboard import kb_profile, kb_register

from users.models import User


@sync_to_async
def get_user(tg_username):
    return User.objects.get(telegram_username=tg_username)


async def login_command(message: types.Message):
    tg_username = message.from_user.username
    try:
        user = await get_user('@' + tg_username)
    except:
        await message.answer(f'Вы незарегистрированный пользователь', reply_markup=kb_register)
    else:
        await message.answer(f'Привет {user.first_name}, вы зарегистрированный пользователь!', reply_markup=kb_profile)


def auth_handlers(dp):
    """
    передаём сюда готовые контроллеры
    """
    dp.register_message_handler(login_command, commands=['login'])

# def get_user(tg_username):
#     @sync_to_async
#     def get():
#         return User.objects.get(telegram_username=tg_username)
#
#     async def get_loop():
#         return await get()
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_loop())
#     return loop.run_until_complete(get_loop())
#
#
# r = get_user('@OptikRUS')
# print(r.username, r.first_name, r.last_name)
