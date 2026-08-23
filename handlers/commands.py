from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.queries import get_all_users


router = Router()



@router.message(Command("users"))
async def users_command(message: Message):

    users = get_all_users()


    text = "Пользователи:\n\n"


    for user in users:

        text += (
            f"{user[0]} "
            f"{user[1]} "
            f"{user[2]} "
            f"{user[3]}\n"
        )


    await message.answer(text)