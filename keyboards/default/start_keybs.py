from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from loader import dp

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)

start_keyboards.add(KeyboardButton("🍴 Menyu"))
start_keyboards.add(KeyboardButton("📋 Mening buyurtmalarim"))
start_keyboards.add(KeyboardButton("📨 Xabar yuborish"), KeyboardButton("⚙️ Sozlamalar"))


contact = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📞 Telefon raqam yuborish', request_contact=True)]
])



