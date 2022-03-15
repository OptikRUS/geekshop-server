from aiogram import types
from aiogram.dispatcher.filters import Text

from botapp.keyboards.keyboard import kb_profile, kb_register
from botapp.bot_scripts.users.views import get_user, get_user_by_telegram, edit_user_telegram_id


async def login_command(message: types.Message):
    try:
        user = await get_user(message.from_user.id)
    except:
        try:
            user = await get_user_by_telegram(message.from_user.username)
        except:
            await message.answer(f'Вы не зарегистрированы на GeekShop или не указан Telegram!\n'
                                 f'Зарегистрироваться через телеграм?', reply_markup=kb_register)
        else:
            await edit_user_telegram_id(user, message.from_user.id)
            await message.answer(f'<b>{user.first_name}</b>, вы авторизованы через телеграм!',
                                 reply_markup=kb_profile, parse_mode="HTML")
    else:
        await message.answer(f'<b>{user.first_name}</b>, вы авторизированный пользователь!',
                             reply_markup=kb_profile, parse_mode="HTML")


def auth_handlers(dp):
    """
    передаём сюда готовые контроллеры
    """
    dp.register_message_handler(login_command, Text(equals='Войти✅'))
