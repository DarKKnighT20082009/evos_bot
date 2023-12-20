from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile
from keyboards.default.menu_keyboards import menu_keyboards
from keyboards.inline.buy_kb import buy_product_new
from loader import dp


@dp.message_handler(Text(equals="🍴 Menu"))
async def menu(message: types.Message):
    await message.answer("Menu bo'limi", reply_markup=menu_keyboards)


@dp.message_handler(text="🌯 Lavash")
async def lavash_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🌯 Lavash")
    lavash_rasm = "https://cp.ectn.uz/files//0622/lavash_s_govyadinoy_evos.png"
    info = ("Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
            ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=lavash_rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🌭 Hot dog")
async def hotdog_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🌭 Hot dog")
    rasm = "https://cp.ectn.uz/files//0622/hot_dog_Baguette_evos.png"
    info = ("Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
            ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🌮Trindwich")
async def lavash_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🌮Trindwich")
    trindwich_rasm = InputFile("photos/Trindwich/trindwich_g.png")
    info = ("Narxi: 26000 sum")
    await message.answer_photo(photo=trindwich_rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🍔Burger")
async def lavash_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🍔Burger")
    burger_rasm = InputFile("photos/Burger/gamburger.png")
    info = ("Narxi: 26000 sum")
    await message.answer_photo(photo=burger_rasm, caption=info, reply_markup=buy_product_new)


@dp.callback_query_handler(text="buy_product_new")
async def buy_product_new_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_name = data.get("product_name")
    text = f"Sotib olindi, {product_name}"
    await call.message.answer(text=text)