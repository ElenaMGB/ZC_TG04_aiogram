import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import TOKEN
import keyboard_tg04dz as kb


bot = Bot(token=TOKEN)
dp = Dispatcher()

# Константы для текста сообщений
START_MESSAGE = 'Приветики, нажми на кнопку!'
LINKS_MESSAGE = 'Вот медиа-ссылки'
DYNAMIC_MESSAGE = 'Показать больше'
GREETING_MESSAGE = 'Привет, {}!'
FAREWELL_MESSAGE = 'До свидания, {}!'
OPTIONS = [
    "Опция 1",
    "Опция 2"
    # Добавьте сюда новые опции
]


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(START_MESSAGE, reply_markup=kb.main)


@dp.message(F.text == "/links")
async def links(message: Message):
    await message.answer(LINKS_MESSAGE, reply_markup=kb.inline_keyboard_media)


@dp.message(F.text == "/dynamic")
async def dynamic(message: Message):
    await message.answer(DYNAMIC_MESSAGE, reply_markup=await kb.dynamic_keyboard())


@dp.message(F.text == "Привет")
async def greet(message: Message):
    await message.answer(GREETING_MESSAGE.format(message.from_user.first_name), reply_markup=kb.main)


@dp.message(F.text == "Пока")
async def farewell(message: Message):
    await message.answer(FAREWELL_MESSAGE.format(message.from_user.first_name), reply_markup=kb.main)


# Обработчик для callback-запросов
@dp.callback_query(F.data.in_(OPTIONS))
async def process_callback(callback_query: CallbackQuery):
    option = callback_query.data
    await bot.send_message(callback_query.from_user.id, f"Вы выбрали: {option}")



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
