from dbService.helper import create_tables
from bot.handlers import commands, messages, callbacks

from aiogram import Dispatcher
from config import dp, displayed_commands, bot, executor


async def on_startup(dispatcher: Dispatcher):
    """
        Creates tables if they don't exist and sets displayed commands.
    """
    create_tables()

    await bot.set_my_commands(commands=displayed_commands)


if __name__ == '__main__':
    executor.on_startup(on_startup)
    executor.start_polling(dp)
