from aiogram import types


def generic_reply_kb(items: list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)

    keyboard.add(*items)

    return keyboard



