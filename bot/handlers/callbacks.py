from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData

import bot.keyboards as inline_kb

from config import dp

"""
question_detail_cb = CallbackData("problem", "problem_id", "user_id", "action")

@dp.callback_query_handler(question_detail_cb.filter(action=["response"]),
                           state=QuestionDetailStates.response_or_discussion)
async def send_response_form(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    problem_id = callback_data["problem_id"]

    problem = get_problem_by_id(problem_id)

    if problem.is_closed:
        await call.answer("Вопрос был закрыт автором и доступен только для чтения", show_alert=True)
        return

    await call.message.answer("Напиши свой ответ в следующем сообщении (для выхода используй /exit)",
                              reply_markup=kb.get_exit_km())
    await QuestionDetailStates.waiting_for_response.set()
    await state.update_data(problem_id=problem_id)
    await call.answer()


"""

"""
                **MENU OPTIONS**
    1. pick-em // user selected pick-em section 
    2. top5 // user selected top-5 players prediction section
    3. events // user selected events predictions section
    4. main // go to main menu (also need command doing the same,
               but sending a new message with the menu buttons instead.    
"""
menu_options_cb = CallbackData("menu", "option")

@dp.callback_query_handler(menu_options_cb.filter(action=["main"]),
                           state="*")
async def goto_main_menu_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Changing message text to pick-em section (description and stuff)
    and different keyboard (pick 3-0/0-3 teams and teams that will qualify for the next stage).

    """
    action_id = callback_data["action_id"]

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
"""
pick_em_options_cb = CallbackData("pick-em", "option")


@dp.callback_query_handler(menu_options_cb.filter(option=["pick-em"]),
                           state="*")
async def goto_pick_em_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Changing message text to pick-em section (description and stuff)
    and different inline keyboard (pick 3-0/0-3 teams and teams that will qualify for the next stage).

    """
    action_id = callback_data["option"]

    await call.answer()


@dp.callback_query_handler(pick_em_options_cb.filter(option=["best"]))
async def select_best_team(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    pass


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


@dp.callback_query_handler(menu_options_cb.filter(action=["top5"]),
                           state="*")
async def goto_top5_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Changing message text to top-5 players of the tournament prediction section (description and stuff)
    and different keyboard (pick 3-0/0-3 teams and teams that will qualify for the next stage).

    """
    action_id = callback_data["action_id"]

    await call.answer()

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


@dp.callback_query_handler(menu_options_cb.filter(action=["events"]),
                           state="*")
async def goto_top5_section(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Changing message text to pick-em section (description and stuff)
    and different keyboard (pick 3-0/0-3 teams and teams that will qualify for the next stage).

    """
    action_id = callback_data["action_id"]

    await call.answer()

