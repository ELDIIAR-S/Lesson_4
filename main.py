import logging
import asyncio

from config import bot, dp, Admin
from handlers import commands, echo, fsm, fsm_edit
from database import main_db
from aiogram.types import BotCommand


async def set_commands():
    commands_list = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='mem', description='мем'),
        BotCommand(command='products', description='Получить товары из БД'),
        BotCommand(command='add_product', description='Записать товар'),
    ]

    await bot.set_my_commands(commands_list)


async def on_startup():
    main_db.create_table()
    await set_commands()



dp.include_router(commands.router_commands)
dp.include_router(fsm.router_fsm)
dp.include_router(fsm_edit.router_edit)

dp.startup.register(on_startup)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
