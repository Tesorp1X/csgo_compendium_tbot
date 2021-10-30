from aiogram.types import Message, ParseMode, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from run_script import dp

from bot.states import PickEmStates
import bot.keyboards.reply as reply_kb
import bot.keyboards.inline as inline_kb

from dbService.pickEmService import get_all_teams


@dp.message_handler(state=[PickEmStates.waiting_for_best_team,
                           PickEmStates.waiting_for_worst_team])
async def pick_em_best_worst_team_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    state_str = await state.get_state()
    if state_str == "PickEmStates:waiting_for_best_team":
        pick_em_best = message.text
        pick_em_worst = "Не выбрано"

    else:
        pick_em_best = "Не выбрано"
        pick_em_worst = message.text

    pick_em_top7 = "Не выбрано\n"
    message_text = "PGL Major 2021 Legends Stage Pick-Em Challenge.\n" + \
                   "1. Выбери команду, которая закончит 3 - 0\n" + \
                   "2. Выбери команду, которая закончит 0 - 3\n" + \
                   "3. Выбери команды, которые пройдут в следующую стадию\n"

    data = await state.get_data()
    if data.__contains__("pick-ems"):
        pick_ems = data["pick-ems"]
        if state_str == "PickEmStates:waiting_for_best_team":
            pick_ems["best"] = pick_em_best
            if pick_ems.__contains__("worst"):
                pick_em_worst = pick_ems["worst"]
        else:
            pick_ems["worst"] = pick_em_worst
            if pick_ems.__contains__("best"):
                pick_em_best = pick_ems["best"]

        if pick_ems.__contains__("top7"):
            pick_em_top7 = ""
            for team in pick_ems["top7"]:
                pick_em_top7 += team + ', '
    else:
        if state_str == "PickEmStates:waiting_for_best_team":
            new_pick_ems = {"best": pick_em_best}
        else:
            new_pick_ems = {"worst": pick_em_worst}
        data["pick-ems"] = new_pick_ems

    message_text += "\nТвой Pick-Em:\n" + \
                    "Команда 3-0: " + pick_em_best + '\n' + \
                    "Команда 0-3: " + pick_em_worst + '\n' + \
                    "Команды плей-офф: " + pick_em_top7 + '\n'

    await PickEmStates.pick_em_menu.set()
    await state.set_data(data)

    await message.bot.send_message(message.from_user.id, message_text,
                                   reply_markup=inline_kb.get_pick_em_options_inline_kb())


@dp.message_handler(state=[PickEmStates.waiting_for_top7_team])
async def pick_em_top7_teams_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    teams_left = data["teams_left"] - 1
    available_teams = data["available_teams"]
    top7_list = data["pick-ems"]["top7"]
    if teams_left > 0:
        data["teams_left"] = teams_left
        top7_list.append(message.text)
        available_teams.remove(message.text)
        await message.answer(f"Выбери еще {teams_left} команд.",
                             reply_markup=reply_kb.generic_reply_kb(available_teams))
    else:
        top7_list.append(message.text)
        available_teams.remove(message.text)
        message_text = "PGL Major 2021 Legends Stage Pick-Em Challenge.\n" + \
                       "1. Выбери команду, которая закончит 3 - 0\n" + \
                       "2. Выбери команду, которая закончит 0 - 3\n" + \
                       "3. Выбери команды, которые пройдут в следующую стадию\n"

        pick_em_best = 'Не выбрано'
        pick_em_worst = 'Не выбрано'
        pick_em_top7 = ''
        for team in top7_list:
            pick_em_top7 += team + ', '

        pick_ems = data["pick-ems"]
        if pick_ems.__contains__("best"):
            pick_em_best = pick_ems["best"]
        if pick_ems.__contains__("worst"):
            pick_em_worst = pick_ems["worst"]

        message_text += "\nТвой Pick-Em:\n" + \
                        "Команда 3-0: " + pick_em_best + '\n' + \
                        "Команда 0-3: " + pick_em_worst + '\n' + \
                        "Команды плей-офф: " + pick_em_top7 + '\n'

        await PickEmStates.pick_em_menu.set()
        del data["teams_left"]
        del data["available_teams"]

        await message.bot.send_message(message.from_user.id, message_text,
                                       reply_markup=inline_kb.get_pick_em_options_inline_kb())

    await state.set_data(data)
