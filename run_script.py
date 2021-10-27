import os
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Dispatcher

from dbService.helper import create_tables

# Getting envs
API_TOKEN = os.getenv("API_TOKEN")

# Configuring logging and storage
logging.basicConfig(level=logging.DEBUG)

storage = MemoryStorage()


displayed_commands = [
    types.BotCommand(command="/help", description="Список доступынх команд"),

]

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
executor = Executor(dp, skip_updates=True)


async def on_startup(dispatcher: Dispatcher):
    """
        Creates tables if they don't exist and sets displayed commands.
    """
    create_tables()

    await bot.set_my_commands(commands=displayed_commands)


if __name__ == '__main__':
    executor.on_startup(on_startup)
    executor.start_polling(dp)
