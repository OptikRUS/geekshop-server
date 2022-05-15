from asgiref.sync import sync_to_async
import re


@sync_to_async
def get_show_word(word, letter, symbol, hide_word=''):
    temp = list(word)
    if len(word) == len(hide_word):
        h_temp = list(hide_word)
        for i in range(len(word)):
            if temp[i] == letter and h_temp[i] == symbol:
                h_temp[i] = letter
        return "".join(h_temp)
    else:
        for i in range(len(word)):
            if temp[i] == letter:
                temp[i] = letter
            else:
                temp[i] = symbol
    return "".join(temp)


@sync_to_async
def letter_valid(letter):
    pattern = r"[а-яА-ЯёЁ]"
    if re.match(pattern, letter) is not None and len(letter) == 1:
        return True
    return False







# for i in word:
#     if i == letter:
#         hide_word += letter
#     else:
#         hide_word += symbol
# return hide_word