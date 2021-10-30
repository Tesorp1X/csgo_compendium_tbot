from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    waiting_for_name = State()


class PickEmStates(StatesGroup):
    pick_em_menu = State()
    waiting_for_best_team = State()
    waiting_for_worst_team = State()
    waiting_for_top7_team = State()
