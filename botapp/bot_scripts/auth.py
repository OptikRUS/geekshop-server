from aiogram import types

from botapp.keyboards.keyboard import kb_profile, kb_register
from botapp.views import get_user


async def login_command(message: types.Message):
    try:
        user = await get_user(message.from_user.id)
    except:
        await message.answer(f'Вы незарегистрированный пользователь!', reply_markup=kb_register)
    else:
        await message.answer(f'Привет <b>{user.first_name}</b>, вы зарегистрированный пользователь!',
                             reply_markup=kb_profile, parse_mode="HTML")


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
