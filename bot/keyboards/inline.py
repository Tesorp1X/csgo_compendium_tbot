from aiogram import types

from bot.handlers.callbacks import menu_options_cb, pick_em_options_cb, top5_options_cb, events_options_cb


def get_main_menu_inline_kb():
    pick_em_callback = menu_options_cb.new("pick-em")
    top5_callback = menu_options_cb.new("top5")
    events_callback = menu_options_cb.new("events")

    buttons = [
        types.InlineKeyboardButton(text="Pick-Em Challenge", callback_data=pick_em_callback),
        types.InlineKeyboardButton(text="Выбрать Топ5 игроков", callback_data=top5_callback),
        types.InlineKeyboardButton(text="События", callback_data=events_callback),
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard


def get_pick_em_options_inline_kb(submit: bool = False):
    if submit:
        go_back_callback = menu_options_cb.new("main")
        buttons = [types.InlineKeyboardButton(text="<< Главное меню", callback_data=go_back_callback)]
    else:
        best_team_callback = pick_em_options_cb.new("best")
        worst_team_callback = pick_em_options_cb.new("worst")
        top7_team_callback = pick_em_options_cb.new("top7")
        submit_pick_em_callback = pick_em_options_cb.new("submit")
        go_back_callback = menu_options_cb.new("main")

        buttons = [
            types.InlineKeyboardButton(text="Выбрать команду 3-0", callback_data=best_team_callback),
            types.InlineKeyboardButton(text="Выбрать команду 0-3", callback_data=worst_team_callback),
            types.InlineKeyboardButton(text="Выбрать команды в топ-7", callback_data=top7_team_callback),
            types.InlineKeyboardButton(text="Подтвердить Pick-Em", callback_data=submit_pick_em_callback),  # TODO: add emoji
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
