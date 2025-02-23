import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests

from config import TOKEN, THE_DOG_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Function to get all dog breeds
def get_dog_breeds():
    url = "https://api.thedogapi.com/v1/breeds"
    headers = {"x-api-key": THE_DOG_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

# Function to get a dog image by breed
def get_dog_image_by_breed(breed_id):
    url = f"https://api.thedogapi.com/v1/images/search?breed_ids={breed_id}"
    headers = {"x-api-key": THE_DOG_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['url']

# Function to get information about a dog breed
def get_breed_info(breed_name):
    breeds = get_dog_breeds()
    for breed in breeds:
        if breed['name'].lower() == breed_name.lower():
            return breed
    return None

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Напиши на английском название породы собаки, и я пришлю тебе её фото и описание.")

@dp.message()
async def send_dog_info(message: Message):
    breed_name = message.text
    breed_info = get_breed_info(breed_name)
    if breed_info:
        # Print the breed_info to inspect its structure
        print(breed_info)

        # Safely access the fields with a default value if the key is missing
        dog_image_url = get_dog_image_by_breed(breed_info['id'])
        info = (
            f"Порода - {breed_info.get('name', 'Неизвестно')}\n"
            f"Описание - {breed_info.get('temperament', 'Нет описания')}\n"
            f"Продолжительность жизни - {breed_info.get('life_span', 'Неизвестно')}."
        )
        await message.answer_photo(photo=dog_image_url, caption=info)
    else:
        await message.answer("Порода не найдена. Попробуйте еще раз.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
