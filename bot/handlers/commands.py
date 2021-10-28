from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

from run_script import dp
from bot.states import RegistrationStates
from dbService.pickEmService import get_user, add_new_user


@dp.message_handler(commands="start", state="*")
async def welcome_handler(message: Message):
    user = get_user(message.from_user.id)

    if not user:
        await message.answer("Привет. Нужно пройти очень короткую регистрацию. Напиши свой ник.")
        await RegistrationStates.waiting_for_name.set()
        return

    await message.answer("Привет, уже знакомы.")


@dp.message_handler(state=RegistrationStates.waiting_for_name)
async def complete_register(message: Message, state: FSMContext):
    name = message.text
    t_id = message.from_user.id

    add_new_user(t_id, name)

    await message.answer("Добро пожаловать в PGL CSGO Major 2021 Compendium!")
