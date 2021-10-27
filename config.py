import os
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Getting envs
API_TOKEN = os.getenv("API_TOKEN")

# Configuring logging and storage
logging.basicConfig(level=logging.DEBUG)

storage = MemoryStorage()


displayed_commands = [
    types.BotCommand(command="/start", description="Start"),
    types.BotCommand(command="/help", description="Список доступынх команд"),
]

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
executor = Executor(dp, skip_updates=True)
