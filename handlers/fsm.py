from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.queries import add_user, get_users


router = Router()


class Form(StatesGroup):
    name = State()
    age = State()
    city = State()


# начало анкеты
@router.message(F.text == "/form")
async def start_form(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Введите имя:")


# имя
@router.message(Form.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(Form.age)
    await message.answer("Введите возраст:")


# возраст
@router.message(Form.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)

    await state.set_state(Form.city)
    await message.answer("Введите город:")


# город + сохранение в БД
@router.message(Form.city)
async def get_city(message: Message, state: FSMContext):
    data = await state.get_data()

    name = data["name"]
    age = data["age"]
    city = message.text

    add_user(
        name=name,
        age=age,
        city=city
    )

    await message.answer(
        f"Анкета сохранена:\n"
        f"Имя: {name}\n"
        f"Возраст: {age}\n"
        f"Город: {city}"
    )

    await state.clear()


# отмена
@router.message(F.text == "/cancel")
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отменена")


# просмотр всех записей
@router.message(F.text == "/users")
async def show_users(message: Message):

    users = get_users()

    if not users:
        await message.answer("Записей нет")
        return

    text = "Пользователи:\n\n"

    for user in users:
        text += (
            f"Имя: {user[1]}\n"
            f"Возраст: {user[2]}\n"
            f"Город: {user[3]}\n\n"
        )

    await message.answer(text)