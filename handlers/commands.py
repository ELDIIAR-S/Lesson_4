from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command

from database import main_db
from database.queries import get_users

from handlers.buttons import (
    main_buttons,
    main_builder,
    menu_inline,
    product_actions
)


router_commands = Router()


# =========================
# START
# =========================

@router_commands.message(Command("start"))
async def start_command(message: Message, bot):
    await message.answer(
        "Привет. Напиши своё имя",
        reply_markup=menu_inline
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Привет. Твой ID - {message.from_user.id}"
    )


# =========================
# HELP
# =========================

@router_commands.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "/start - старт бота\n"
        "/help - помощник\n"
        "/form - заполнить анкету\n"
        "/users - показать анкеты\n"
        "/products - показать товары"
    )



# USERS
# =========================

@router_commands.message(Command("users"))
async def users_command(message: Message):
    users = get_users()

    if not users:
        await message.answer(
            "📭 В базе пока нет записей."
        )
        return

    text = "📋 Записи из базы:\n\n"

    for user_id, name, age, phone in users:
        text += (
            f"ID: {user_id}\n"
            f"Имя: {name}\n"
            f"Возраст: {age}\n"
            f"Телефон: {phone}\n"
            "────────────\n"
        )

    await message.answer(text)



# HELLO
# =========================

@router_commands.message(F.text == "привет")
async def hello_command(message: Message):
    await message.answer("Hello")



# MEM
# =========================

@router_commands.message(Command("mem"))
async def mem_command(message: Message, bot):
    photo = FSInputFile("media/mem.png")

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo
    )


@router_commands.callback_query(F.data == "mem")
async def mem_callback(call: CallbackQuery, bot):
    photo = FSInputFile("media/mem.png")

    await bot.send_photo(
        chat_id=call.message.chat.id,
        photo=photo
    )



# PRODUCTS
# =========================

@router_commands.message(Command("products"))
async def get_products(message: Message):
    products = await main_db.get_product_db()

    if not products:
        await message.answer(
            "В базе товаров нет!"
        )
        return

    for (
        name,
        price,
        category,
        description,
        product_id,
        photo_id
    ) in products:

        await message.answer_photo(
            photo=photo_id,
            caption=(
                f"Название - {name}\n"
                f"Цена - {price}\n"
                f"Описание - {description}\n"
                f"Категория - {category}\n"
                f"Артикул - {product_id}"
            ),
            reply_markup=product_actions(
                product_id=product_id
            )
        )
