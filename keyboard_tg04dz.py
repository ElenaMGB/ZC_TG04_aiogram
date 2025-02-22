from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from main.py import OPTIONS

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
], resize_keyboard=True)


inline_keyboard_media = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://news.yandex.ru')],
    [InlineKeyboardButton(text='Музыка', url='https://music.yandex.ru')],
    [InlineKeyboardButton(text='Видео', url='https://youtube.com')]
])



async def dynamic_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in OPTIONS:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=key))
    return keyboard.adjust(2).as_markup()

