from aiogram import types
from asgiref.sync import sync_to_async, async_to_sync
import asyncio

from users.models import User


@sync_to_async
def get_user(tg_username):
    return User.objects.get(telegram_username=tg_username)


r = get_user('OptikRUS')
print(r)

results = sync_to_async(User.objects.get, thread_sensitive=True)(telegram_username="OptikRUS")
print(results)


def _get_u(tg_username):
    return User.objects.select_related().get(telegram_username=tg_username)


get_u = sync_to_async(_get_u, thread_sensitive=True)
print(get_u)


# def get_(tg_username):
#     return User.objects.get(tg_username=tg_username).username
#
#
# async def main():
#     result = get_("OptikRUS")



async def login_command(message: types.Message):
    tg_username = message.from_user.username
    test = await get_user(tg_username)
    print(test)
    #
    await message.answer(f'Привет {test} тест')
    # if tg_username_request == tg_username:
    #     user = User.objects.filter(telegram_username=tg_username)
    #     context = {
    #         'first_name': user.get().first_name
    #     }
    #     await message.reply(f'Привет, {context["first_name"]}')
    #     await message.answer(f'Привет, {message.from_user.username}')


def auth_handlers(dp):
    """
    передаём сюда готовые контроллеры
    """
    dp.register_message_handler(login_command, commands=['login'])
    # dp.register_message_handler(about_command, commands=['register'])
