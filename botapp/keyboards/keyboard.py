from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

"""
регистрируем кнопки
request_contact - отправить свой контакт
request_location - поделиться геолокаацией
"""

button_login = KeyboardButton('/login')
button_help = KeyboardButton('/help')
# button_id = KeyboardButton('/id')
# button_date = KeyboardButton('/date')
button_get_number = KeyboardButton('Поделиться номером', request_contact=True)
button_get_locate = KeyboardButton('Отправить где я', request_location=True)
# button_cancel = KeyboardButton("/cancel")

"""
изменяем вид кнопок:
resize_keyboard - уменньшить размер кнопок 
row_width - ширина ряда
one_time_keyboard - спрятать клавиатуру после выбора
kb_client - регистрируем набор кнопок
"""

# kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start = ReplyKeyboardMarkup(resize_keyboard=True)


"""
настраиваем расположение конопок:
    add(b1).add(b2) - каждая кнопка с новой строки
    add(b1).insert(b2) - кнопка b2 на одной строке с ккнопкой b1
    row(b1, b2, b3) - добавляет кнопки в одну строку 
"""

# kb_client.add(button_help).add(button_date).add(button_id).row(button_get_number, button_get_locate)
# kb_cancel.add(button_cancel)

kb_start.add(button_login).insert(button_help)