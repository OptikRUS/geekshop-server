from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

"""
регистрируем кнопки
request_contact - отправить свой контакт
request_location - поделиться геолокаацией
"""
button_menu = KeyboardButton('/menu')
button_main = KeyboardButton('/main')
button_login = KeyboardButton('/login')
button_register = KeyboardButton('/register')
button_help = KeyboardButton('/help')
button_profile = KeyboardButton('/profile')
button_edit_profile = KeyboardButton('/edit_profile')

# button_get_number = KeyboardButton('Поделиться номером', request_contact=True)
# button_get_locate = KeyboardButton('Отправить где я', request_location=True)
button_cancel = KeyboardButton("/cancel")
button_cancel_registration = KeyboardButton("/cancel_registration")
button_test = KeyboardButton("/test")

inline_button_menu = InlineKeyboardButton(text="Меню", callback_data="start")

"""
изменяем вид кнопок:
resize_keyboard - уменньшить размер кнопок 
row_width - ширина ряда
one_time_keyboard - спрятать клавиатуру после выбора
kb_client - регистрируем набор кнопок
"""

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_profile = ReplyKeyboardMarkup(resize_keyboard=True)
kb_edit_profile = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_register = ReplyKeyboardMarkup(resize_keyboard=True)
kb_register_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)

inline_kb_menu = InlineKeyboardMarkup()

"""
настраиваем расположение конопок:
    add(b1).add(b2) - каждая кнопка с новой строки
    add(b1).insert(b2) - кнопка b2 на одной строке с ккнопкой b1
    row(b1, b2, b3) - добавляет кнопки в одну строку 
"""

kb_start.add(button_login).add(button_help).insert(button_menu)
kb_profile.add(button_profile).insert(button_menu)
kb_register.add(button_register).insert(button_menu)
kb_edit_profile.add(button_edit_profile).insert(button_menu)
kb_menu.add(button_help).insert(button_menu).add(button_main)

kb_cancel.add(button_cancel)
kb_register_cancel.add(button_cancel_registration)

inline_kb_menu.add(inline_button_menu)