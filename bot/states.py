from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    waiting_for_name = State()
