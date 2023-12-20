from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboards.add(KeyboardButton('🌯Lavash'), KeyboardButton('🌭Hot-dog'))
menu_keyboards.add(KeyboardButton('🌮Trindwich'), KeyboardButton('🍔Burger'))
menu_keyboards.add(KeyboardButton('🥩Steyk'), KeyboardButton("🍟Kartoshka Fri"))
menu_keyboards.add(KeyboardButton('🍦Muzqaymoq'), KeyboardButton('🍩Sweets'))
menu_keyboards.add(KeyboardButton("🔙 Mainga qaytish"))

lavash_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)#🌯 Lavash
lavash_keyboards.add(KeyboardButton("Lavash oddiy"), KeyboardButton("Lavash pishloqli"))
lavash_keyboards.add(KeyboardButton("Mini lavash"), KeyboardButton("Lavash achchiq"))
lavash_keyboards.add(KeyboardButton("Fitter"))
lavash_keyboards.add(KeyboardButton("🔙 Orqaga qaytish"))

hotdog_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)#🌭 HotDog
hotdog_keyboards.add(KeyboardButton("HotDog"), KeyboardButton("Dabl HotDog"))
hotdog_keyboards.add(KeyboardButton("HotDog mini"))
hotdog_keyboards.add(KeyboardButton("🔙 Orqaga qaytish"))

trindwich_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)#🌮 Trindwich`
trindwich_keyboards.add(KeyboardButton("Trindwich go'shtli"), KeyboardButton("Trindwich tovuqli"))
trindwich_keyboards.add(KeyboardButton("🔙 Orqaga qaytish"))

burger_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)# 🍔 Burger
burger_keyboards.add(KeyboardButton("Burger"), KeyboardButton("Dabl Burger"))
burger_keyboards.add(KeyboardButton("Chizburger"), KeyboardButton("Dabl Chizburger"))
burger_keyboards.add(KeyboardButton("🔙 Orqaga qaytish"))

ice_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)# 🍦 Muzqaymoq
ice_keyboards.add(KeyboardButton(""), KeyboardButton(""))
ice_keyboards.add(KeyboardButton(""), KeyboardButton(""))
ice_keyboards.add(KeyboardButton("🔙 Orqaga qaytish"))

fri_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)# 🍟Kartoshka Fri
fri_keyboards.add(KeyboardButton("Kartoshka Fri"), KeyboardButton("Qovurilgan kartoshka"))
fri_keyboards.add(KeyboardButton("Smayliklar"))
fri_keyboards.add(KeyboardButton("🔙 Orqaga qaytish"))

cake_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)# 🍩sweets
cake_keyboards.add(KeyboardButton("Medovik Asalim"), KeyboardButton("Chizkeyk"))
cake_keyboards.add(KeyboardButton("Donut qulupnayli"), KeyboardButton("Donut karamelli"))
cake_keyboards.add(KeyboardButton("🔙 Orqaga qaytish"))