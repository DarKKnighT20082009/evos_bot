from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

from keyboards.inline.buy_kb import buy_product_new
from loader import dp

from keyboards.default.menu_keyboards import menu_keyboards, lavash_keyboards, hotdog_keyboards, trindwich_keyboards, burger_keyboards,cake_keyboards, fri_keyboards, ice_keyboards
from keyboards.default.start_keybs import start_keyboards


@dp.message_handler()
async  def keyboards_func(message: types.Message, state: FSMContext):
    if message.text == "🍴 Menyu":
        await message.answer("Kategoryani tanlang", reply_markup=menu_keyboards)
    elif message.text == "📋 Mening buyurtmalarim":
        await message.answer("Bu mening zakazlarim bo'limi")
    elif message.text == "📨 Xabar yuborish":
        await  message.answer("Bu ariza qoldirish joyi, admin bilan bog'lanish uchun @mirolimov_a")
    elif message.text == "⚙️ Sozlamalar":
        await  message.answer("Bu sozlamalar joyi")
    elif message.text == "🔙 Mainga qaytish":
        await message.answer("Tanlang:", reply_markup=start_keyboards)

    elif message.text == "🌯Lavash":
        lavash_all = InputFile("photos/lavash/lavash_all.jpg")
        await message.answer_photo(photo=lavash_all, reply_markup=lavash_keyboards)
    elif message.text == "Lavash oddiy":
        lavash_img = InputFile("photos/lavash/lavash_oddiy.png")
        await message.answer_photo(photo=lavash_img, caption="Narxi: 28000 sum", reply_markup=buy_product_new)
    elif message.text == "Lavash pishloqli":
        sirli_l = InputFile("photos/lavash/sirli_l.png")
        await message.answer_photo(photo=sirli_l, caption="Narxi: 31000 sum")
    elif message.text == "Mini lavash":
        mini_l = InputFile("photos/lavash/mini_l.png")
        await message.answer_photo(photo=mini_l, caption="Narxi: 23000 sum")
    elif message.text == "Lavash achchiq":
        achchiq_l = InputFile("photos/lavash/achchiq_l.png")
        await message.answer_photo(photo=achchiq_l, caption="Narxi: 28000 sum")
    elif message.text == "Fitter":
        fitter_l = InputFile("photos/lavash/fitter_l.png")
        await message.answer_photo(photo=fitter_l, caption="Narxi: 24000 sum")
    elif message.text == "🔙 Orqaga qaytish" or message.text == "🍴 Menyu":
        await message.answer("Tanlang:", reply_markup=menu_keyboards)

    elif message.text == "🌭Hot-dog":
        hotdog_all = InputFile("photos/Hot_dog/hotdog_all.jpg")
        await message.answer_photo(photo=hotdog_all, reply_markup=hotdog_keyboards)
    elif message.text == "HotDog":
        HotDog_img = InputFile("photos/Hot_dog/hotdog.png")
        await message.answer_photo(photo=HotDog_img, caption="Narxi: 14000 sum")
    elif message.text == "Dabl HotDog":
        Dabl_hotdog = InputFile("photos/Hot_dog/dabl_hotdog.png")
        await message.answer_photo(photo=Dabl_hotdog, caption="Narxi: 21000 sum")
    elif message.text == "HotDog mini":
        mini_hotdog = InputFile("photos/Hot_dog/mini_hotdog.png")
        await message.answer_photo(photo=mini_hotdog, caption="Narxi: 8000 sum")
    elif message.text == "🔙 Orqaga qaytish" or message.text == "🍴 Menyu":
        await message.answer("Tanlang:", reply_markup=menu_keyboards)

    elif message.text == "🌮Trindwich":
        trinwich_all = InputFile("photos/Trindwich/Trindwich_all.png")
        await message.answer_photo(photo=trinwich_all, reply_markup=trindwich_keyboards)
    elif message.text == "Trindwich go'shtli":
        trindwich_g = InputFile("photos/Trindwich/trindwich_g.png")
        await message.answer_photo(photo=trindwich_g, caption="Narxi: 26000 sum")
    elif message.text == "Trindwich tovuqli":
        trindwich_t = InputFile("photos/Trindwich/trindwich_t.png")
        await message.answer_photo(photo=trindwich_t, caption="Narxi: 24000 sum")
    elif message.text == "🔙 Orqaga qaytish" or message.text == "🍴 Menyu":
        await message.answer("Tanlang:", reply_markup=menu_keyboards)

    elif message.text == "🍔Burger":
        burger_all = InputFile("photos/Burger/burger_all.jpg")
        await message.answer_photo(photo=burger_all, reply_markup=burger_keyboards)
    elif message.text == "Burger":
        gamburger_img = InputFile("photos/Burger/gamburger.png")
        await message.answer_photo(photo=gamburger_img, caption="Narxi: 22000 sum")
    elif message.text == "Dabl Burger":
        dablburger = InputFile("photos/Burger/dablburger.jpg")
        await message.answer_photo(photo=dablburger, caption="Narxi: 33000 sum")
    elif message.text == "Chizburger":
        chizburger = InputFile("photos/Burger/chizburger.png")
        await message.answer_photo(photo=chizburger, caption="Narxi:24 000 sum")
    elif message.text == "Dabl Chizburger":
        dablchizburger = InputFile("photos/Burger/dablchizburger.png")
        await message.answer_photo(photo=dablchizburger, caption="Narxi: 37000 sum")
    elif message.text == "🔙 Orqaga qaytish" or message.text == "🍴 Menyu":
        await message.answer("Tanlang:", reply_markup=menu_keyboards)

    elif message.text == "🍩Sweets":
        cake_all = InputFile("photos/cake/photo_2023-09-29_17-10-19.jpg")
        await message.answer_photo(photo=cake_all, reply_markup=cake_keyboards)
    elif message.text == "Medovik Asalim":
        asalim = InputFile("photos/cake/asalim.png")
        await message.answer_photo(photo=asalim, caption="Narxi: 16000 sum")
    elif message.text == "Chizkeyk":
        chizkeyk = InputFile("photos/cake/chizkeyk.png")
        await message.answer_photo(photo=chizkeyk, caption="Narxi: 16000 sum")
    elif message.text == "Donut karamelli":
        donut_caramel = InputFile("photos/cake/donat_caramel.png")
        await message.answer_photo(photo=donut_caramel, caption="Narxi: 15000 sum")
    elif message.text == "Donut qulupnayli":
        donut_fruit = InputFile("photos/cake/donut_fruit.png")
        await message.answer_photo(photo=donut_fruit, caption="Narxi: 15000 sum")
    elif message.text == "🔙 Orqaga qaytish" or message.text == "🍴 Menyu":
        await message.answer("Tanlang:", reply_markup=menu_keyboards)

    elif message.text == "🥩Steyk":
        steyk = InputFile("photos/steyk/steyk.jpg")
        await message.answer_photo(photo=steyk, caption="Narxi: 60000 sum")

    elif message.text == "🍦Muzqaymoq":
        ice_all = InputFile("photos/Ice_cream/ice_cream_all.jpg")
        await message.answer_photo(photo=ice_all, reply_markup=ice_keyboards, caption="Hozirch sotuvda mavjud emas")
    elif message.text == "Shokolad sousli":
        ice_choko = InputFile("photos/Ice_cream/ice_cream_all.jpg")
        await message.answer_photo(photo=ice_choko, caption="Narxi: 000 sum")
    elif message.text == "Karamel sousli":
        ice_caramel = InputFile("photos/Ice_cream/ice_cream_all.jpg")
        await message.answer_photo(photo=ice_caramel, caption="Narxi: 000 sum")
    elif message.text == "Qulupnay sousli":
        ice_strawberry = InputFile("photos/Ice_cream/ice_cream_all.jpg")
        await message.answer_photo(photo=ice_strawberry, caption="Narxi: 000 sum")
    elif message.text == "Shoko-babl":
        choko_babl = InputFile("photos/Ice_cream/ice_cream_all.jpg")
        await message.answer_photo(photo=choko_babl, caption="Narxi: 000 sum")
    elif message.text == "Kamalak-babl":
        rainbow_babl = InputFile("photos/Ice_cream/ice_cream_all.jpg")
        await message.answer_photo(photo=rainbow_babl, caption="Narxi: 000 sum")
    elif message.text == "🔙 Orqaga qaytish" or message.text == "🍴 Menyu":
        await message.answer("Tanlang:", reply_markup=menu_keyboards)

    elif message.text == "🍟Kartoshka Fri":
        fri = InputFile("photos/Fri/kartoshka_fri.png")
        await message.answer_photo(photo=fri, reply_markup=fri_keyboards)
    elif message.text == "Kartoshka Fri":
        fri = InputFile("photos/Fri/kartoshka_fri.png")
        await message.answer_photo(photo=fri, caption="Narxi: 14000 sum")
    elif message.text == "Qovurilgan kartoshka":
        qovurilgan_kartoshka = InputFile("photos/Fri/qovurilgan_kartoshka.png")
        await message.answer_photo(photo=qovurilgan_kartoshka, caption="Narxi: 15000 sum")
    elif message.text == "Smayliklar":
        smiles = InputFile("photos/Fri/smiles.png")
        await message.answer_photo(photo=smiles, caption="Narxi: 14000 sum")
    elif message.text == "🔙 Orqaga qaytish" or message.text == "🍴 Menyu":
        await message.answer("Tanlang:", reply_markup=menu_keyboards)