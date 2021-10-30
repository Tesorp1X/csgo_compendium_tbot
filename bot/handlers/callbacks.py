from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData

import bot.keyboards.inline as inline_kb
import bot.keyboards.reply as reply_kb
from config import dp
from dbService.pickEmService import get_all_teams, save_pick_em, get_users_pick_em

from bot.states import PickEmStates

"""
                **MENU OPTIONS**
    1. pick-em // user selected pick-em section 
    2. top5 // user selected top-5 players prediction section
    3. events // user selected events predictions section
    4. main // go to main menu (also need command doing the same,
               but sending a new message with the menu buttons instead.    
"""
menu_options_cb = CallbackData("menu", "option")


@dp.callback_query_handler(menu_options_cb.filter(option=["main"]),
                           state="*")
async def goto_main_menu_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Changing message text to pick-em section (description and stuff)
    and different keyboard (pick 3-0/0-3 teams and teams that will qualify for the next stage).

    """
    await call.message.edit_text("CSGO Compendium: PGL Major Stockholm 2021 Legends Stage\nГлавное меню.")
    await call.message.edit_reply_markup(inline_kb.get_main_menu_inline_kb())
    await call.answer()


# TODO: MAKE callback_query_handler FOR QUERIES THAT NO LONGER VALID
# TODO: MAKE STATES GROUP FOR MENU

"""
                            **PICK-EM SECTION**
"""

"""
                **PICK-EM MENU OPTIONS**
    1. best // user wants to pick the best team in this stage (3-0 team)
    2. top7 // user wants to pick top-7 teams
    3. worst // user wants to pick the worst team (0-3 team)   
    4. submit // user wants to submit their pick-em
"""
pick_em_options_cb = CallbackData("pick-em", "option")


@dp.callback_query_handler(menu_options_cb.filter(option=["pick-em"]),
                           state="*")
async def goto_pick_em_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Changing message text to pick-em section (description and stuff)
    and different inline keyboard (pick 3-0/0-3 teams and teams that will qualify for the next stage).

    """
    users_pick_em_or_none = get_users_pick_em(call.from_user.id)

    message_text = "PGL Major 2021 Legends Stage Pick-Em Challenge.\n" + \
                   "1. Выбери команду, которая закончит 3 - 0\n" + \
                   "2. Выбери команду, которая закончит 0 - 3\n" + \
                   "3. Выбери команды, которые пройдут в следующую стадию\n"

    pick_em_best = "Не выбрано\n"
    pick_em_worst = "Не выбрано\n"
    pick_em_top7 = "Не выбрано\n"

    data = await state.get_data()
    if users_pick_em_or_none is not None:
        data["pick-ems"] = users_pick_em_or_none.copy()
    is_submit = True
    if data.__contains__("pick-ems"):
        pick_ems = data["pick-ems"]
        if pick_ems.__contains__("best"):
            pick_em_best = pick_ems["best"] + '\n'
        else:
            is_submit = False
        if pick_ems.__contains__("worst"):
            pick_em_worst = pick_ems["worst"] + '\n'
        else:
            is_submit = False
        if pick_ems.__contains__("top7"):
            pick_em_top7 = ""
            for team in pick_ems["top7"]:
                pick_em_top7 += team + ', '
            pick_em_top7 += '\n'
        else:
            is_submit = False
    else:
        is_submit = False

    message_text += "\nТвой Pick-Em:\n" + \
                    "Команда 3-0: " + pick_em_best + \
                    "Команда 0-3: " + pick_em_worst + \
                    "Команды плей-офф: " + pick_em_top7

    await call.message.edit_text(message_text)

    await call.message.edit_reply_markup(inline_kb.get_pick_em_options_inline_kb(submit=is_submit))
    await PickEmStates.pick_em_menu.set()
    await call.answer()


@dp.callback_query_handler(pick_em_options_cb.filter(option=["best", "top7", "worst"]), state=PickEmStates.pick_em_menu)
async def select_best_team(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    message_text = ""
    pick_em_best = "Не выбрано"
    pick_em_worst = "Не выбрано"
    pick_em_top7 = "Не выбрано"

    teams = get_all_teams()

    data = await state.get_data()
    if data.__contains__("pick-ems"):
        pick_ems = data["pick-ems"]
        if pick_ems.__contains__("best"):
            pick_em_best = pick_ems["best"]
            teams.remove(pick_ems["best"])
        if pick_ems.__contains__("worst"):
            pick_em_worst = pick_ems["worst"]
            teams.remove(pick_ems["worst"])
        if pick_ems.__contains__("top7"):
            pick_em_top7 = ""
            for team in pick_ems["top7"]:
                pick_em_top7 += team + ', '
                teams.remove(team)

    if callback_data["option"] == "best":
        message_text = "Выбери команду, которая пройдёт в плей-офф со счётом 3 - 0\n"
        await PickEmStates.waiting_for_best_team.set()
    elif callback_data["option"] == "worst":
        message_text = "Выбери команду, которая вылетит с турнира со счётом 0 - 3\n"
        await PickEmStates.waiting_for_worst_team.set()
    else:
        message_text = "Выбери 7 команд, которые пройдут в плей-офф\n"
        await PickEmStates.waiting_for_top7_team.set()
        data["teams_left"] = 7
        data["pick-ems"]["top7"] = []

    data["available_teams"] = teams
    await state.set_data(data)

    message_text += "\nТвой Pick-Em:\n" + \
                    "Команда 3-0: " + pick_em_best + '\n' + \
                    "Команда 0-3: " + pick_em_worst + '\n' + \
                    "Команды плей-офф: " + pick_em_top7 + '\n'

    await call.message.delete()
    await call.bot.send_message(call.from_user.id, message_text, reply_markup=reply_kb.generic_reply_kb(teams))
    await call.answer()


@dp.callback_query_handler(pick_em_options_cb.filter(option=["submit"]),
                           state=PickEmStates.pick_em_menu)
async def submit_pick_em_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    alert_message = "Твой Pick-Em сохранён!"
    message_text = "Твой Pick-Em:\n"

    if not data.__contains__("pick-ems"):
        await call.answer("Ты не сделал ни одного предсказания.", show_alert=True)
        return

    pick_ems = data["pick-ems"]
    if not pick_ems.__contains__("best"):
        await call.answer("Ты не выбрал команду 3-0!", show_alert=True)
        return

    message_text += "Команда 3-0: " + pick_ems["best"] + '\n'

    if not pick_ems.__contains__("worst"):
        await call.answer("Ты не выбрал команду 0-3!", show_alert=True)
        return

    message_text += "Команда 0-3: " + pick_ems["worst"] + '\n'

    if not pick_ems.__contains__("top7"):
        await call.answer("Ты не выбрал команды, которые пройдут в плей-офф!", show_alert=True)
        return
    else:
        if len(pick_ems["top7"]) < 7:
            await call.answer("Ты выбрал не все команды, которые пройдут в плей-офф!", show_alert=True)
            return
    message_text += "Команды плей-офф: "
    for team in pick_ems["top7"]:
        message_text += team + ', '
    save_pick_em(user_t_id=call.from_user.id, best=pick_ems["best"],
                 worst=pick_ems["worst"], top7=pick_ems["top7"])

    await call.message.edit_text(message_text)
    await call.message.edit_reply_markup(inline_kb.get_pick_em_options_inline_kb(submit=True))
    await call.answer(alert_message)

"""
                            **TOP-5 PLAYERS SECTION**
"""

"""
                **TOP-5 MENU OPTIONS**
    1. SLOT1 // user wants to pick 1st slot
    2. SLOT2 // user wants to pick 2nd slot
    3. SLOT3 // user wants to pick 3d slot   
    4. SLOT4 // user wants to pick 4th slot   
    5. SLOT5 // user wants to pick 5th slot
"""
top5_options_cb = CallbackData("top5", "option")


@dp.callback_query_handler(menu_options_cb.filter(option=["top5"]),
                           state="*")
async def goto_top5_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):

    await call.answer("Не работает еще :(", show_alert=True)


"""
                            **EVENTS PREDICTIONS SECTION**
"""

"""
                **EVENTS MENU OPTIONS**
    1. SLOT1 // user wants to pick 1st slot
    2. SLOT2 // user wants to pick 2nd slot
    3. SLOT3 // user wants to pick 3d slot   
    4. SLOT4 // user wants to pick 4th slot   
    5. SLOT5 // user wants to pick 5th slot
"""
events_options_cb = CallbackData("events", "option")


@dp.callback_query_handler(menu_options_cb.filter(option=["events"]),
                           state="*")
async def goto_top5_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):

    await call.answer("Не работает еще :(", show_alert=True)
