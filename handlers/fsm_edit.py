from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import main_db
from handlers import buttons

router_edit = Router()

class EditProduct(StatesGroup):
    field = State()
    new_value = State()

"собака, кошка, мышка"
# split(',')

# edit:1001
@router_edit.callback_query(F.data.startswith('edit:'))
async def edit_start(call: CallbackQuery, state: FSMContext):
    product_id = call.data.split(':')[1]
    print(product_id)

    await state.update_data(product_id=product_id)
    await call.message.answer("Что меняем?", reply_markup=buttons.edit_fields)
    await call.answer()
    await state.set_state(EditProduct.field)


@router_edit.callback_query(EditProduct.field, F.data.startswith('field_'))
async def edit_field(call: CallbackQuery, state: FSMContext):
    field = call.data.removeprefix('field_')
    await state.update_data(field=field)

    await call.message.answer('Введите новое значение')
    await call.answer()
    await state.set_state(EditProduct.new_value)


@router_edit.message(EditProduct.new_value, F.text)
async def edit_save(message: Message, state: FSMContext):
    data = await state.get_data()

    if data['field'] == 'price' and not message.text.isdigit():
        await message.answer('Цена должна быть числом. Попробуйте еще раз')
        return
    else:
        await main_db.update_product_db(field=data['field'], value=message.text, product_id=data['product_id'])
        await message.answer("Товар обновлен!")
        await state.clear()