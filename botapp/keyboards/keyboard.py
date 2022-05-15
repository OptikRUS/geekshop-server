from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

"""
регистрируем кнопки
request_contact - отправить свой контакт
request_location - поделиться геолокаацией
"""

# buttons
button_menu = KeyboardButton('Меню🧷')
button_main = KeyboardButton('Главное меню📎')
button_login = KeyboardButton('Войти✅')
button_register = KeyboardButton('Регистрация🔑')
button_help = KeyboardButton('Помощь💡')
button_profile = KeyboardButton('Профиль👤')
button_edit_profile = KeyboardButton('Редактировать👤')
# button_get_number = KeyboardButton('Поделиться номером', request_contact=True)
# button_get_locate = KeyboardButton('Отправить где я', request_location=True)
button_cancel = KeyboardButton("Отмена⛔️")
button_cancel_registration = KeyboardButton("Отмена🚫")

# games
button_games = KeyboardButton('Игры🎮')

# hangman buttons
button_hangman = KeyboardButton('Виселица🪜')
button_play_hangman = KeyboardButton('Играть🪜')
button_help_hangman = KeyboardButton('Правила🪜')
button_cancel_hangman = KeyboardButton('Выйти из игры ❌')
"""
изменяем вид кнопок:
resize_keyboard - уменньшить размер кнопок 
row_width - ширина ряда
one_time_keyboard - спрятать клавиатуру после выбора
kb_client - регистрируем набор кнопок
"""

# keyboards
kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_profile = ReplyKeyboardMarkup(resize_keyboard=True)
kb_edit_profile = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_register = ReplyKeyboardMarkup(resize_keyboard=True)
kb_register_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_login = ReplyKeyboardMarkup(resize_keyboard=True)

# games
kb_games = ReplyKeyboardMarkup(resize_keyboard=True)

# hangman keyboards
kb_hangman = ReplyKeyboardMarkup(resize_keyboard=True)

kb_cancel_hangman = ReplyKeyboardMarkup(resize_keyboard=True)

"""
настраиваем расположение конопок:
    add(b1).add(b2) - каждая кнопка с новой строки
    add(b1).insert(b2) - кнопка b2 на одной строке с кнопкой b1
    row(b1, b2, b3) - добавляет кнопки в одну строку 
"""

# main
kb_start.add(button_login).add(button_help).insert(button_menu)
kb_menu.add(button_games).insert(button_main)

# auth
kb_login.add(button_login).insert(button_main)
kb_profile.add(button_profile).insert(button_menu)
kb_register.add(button_register).insert(button_menu)
kb_edit_profile.add(button_edit_profile).insert(button_menu)

kb_cancel.add(button_cancel)
kb_register_cancel.add(button_cancel_registration)

# games
kb_games.add(button_hangman).insert(button_menu)

# hangman
kb_hangman.add(button_play_hangman).insert(button_help_hangman).add(button_games).insert(button_menu)

kb_cancel_hangman.add(button_cancel_hangman)
