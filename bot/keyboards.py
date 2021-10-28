from aiogram import types

from bot.handlers.callbacks import menu_options_cb, pick_em_options_cb, top5_options_cb, events_options_cb


def get_generic_inline_kb(keyboard_data: dict, row_widths: int = 1):
    """
    Pass a keyboard_data parameter - a dict of [button_text, callback data] pairs.
    """

    buttons = []
    for button_text in keyboard_data:
        buttons.append(types.InlineKeyboardButton(text=button_text,
                                                  callback_data=keyboard_data[button_text]))

    keyboard = types.InlineKeyboardMarkup(row_width=row_widths)
    keyboard.add(*buttons)

    return keyboard


def generic_reply_kb(items: list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    keyboard.add(*items)

    return keyboard


"""
def get_response_detail_inline_kb(response_obj: Response, user_id: int, is_author: bool = False):
    response_id = response_obj.id

    report_callback = response_detail_cb.new(response_id=response_id, user_id=user_id, action="report")

    buttons = [
        types.InlineKeyboardButton(text=emoji.emojize("Пожаловаться :warning:", use_aliases=True),
                                   callback_data=report_callback)
    ]

    if is_author:
        solve_callback = response_detail_cb.new(response_id=response_id, user_id=user_id, action="solve")
        buttons.append(
            types.InlineKeyboardButton(text=emoji.emojize("Помогло :white_check_mark:", use_aliases=True),
                                       callback_data=solve_callback))

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard
"""


def get_pick_em_options_inline_kb():
    best_team_callback = pick_em_options_cb.new("best")
    worst_team_callback = pick_em_options_cb.new("worst")
    top7_team_callback = pick_em_options_cb.new("top7")
    go_back_callback = menu_options_cb.new("main")

    buttons = [
        types.InlineKeyboardButton(text="Выбрать команду 3-0", callback_data=best_team_callback),
        types.InlineKeyboardButton(text="Выбрать команду 0-3", callback_data=worst_team_callback),
        types.InlineKeyboardButton(text="Выбрать команды в топ-7", callback_data=top7_team_callback),
        types.InlineKeyboardButton(text="<< Главное меню", callback_data=go_back_callback),
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard


def get_top5_options_inline_kb():
    slot1_callback = top5_options_cb.new("SLOT1")
    slot2_callback = top5_options_cb.new("SLOT2")
    slot3_callback = top5_options_cb.new("SLOT3")
    slot4_callback = top5_options_cb.new("SLOT4")
    slot5_callback = top5_options_cb.new("SLOT5")
    go_back_callback = menu_options_cb.new("main")

    buttons = [
        types.InlineKeyboardButton(text="Выбрать игрока", callback_data=slot1_callback),
        types.InlineKeyboardButton(text="Выбрать игрока", callback_data=slot2_callback),
        types.InlineKeyboardButton(text="Выбрать игрока", callback_data=slot3_callback),
        types.InlineKeyboardButton(text="Выбрать игрока", callback_data=slot4_callback),
        types.InlineKeyboardButton(text="Выбрать игрока", callback_data=slot5_callback),
        types.InlineKeyboardButton(text="<< Главное меню", callback_data=go_back_callback),
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard
