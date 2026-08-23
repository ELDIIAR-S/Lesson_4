import asyncio

from aiogram import Dispatcher

from config import bot
from database.main_db import create_table
from handlers import commands, echo, fsm


dp = Dispatcher()


async def main():
    create_table()

    dp.include_router(commands.router)
    dp.include_router(fsm.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
