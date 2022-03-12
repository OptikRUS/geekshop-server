from aiogram import types
from asgiref.sync import sync_to_async

from users.models import User


@sync_to_async
def get_user(tg_username):
    return User.objects.get(telegram_username=tg_username)


async def login_command(message: types.Message):
    tg_username = message.from_user.username
    user = await get_user('@' + tg_username)
    await message.answer(f'Привет {user.first_name, user.telegram_username}, вы зарегистрированный пользователь!')


def auth_handlers(dp):
    """
    передаём сюда готовые контроллеры
    """
    dp.register_message_handler(login_command, commands=['login'])
    # dp.register_message_handler(about_command, commands=['register'])

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
