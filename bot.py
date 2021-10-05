import aiogram
import config
import random

import logging

from aiogram import Bot, Dispatcher, executor, types

# Initialize bot and dispatcher

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hello. Do you like fisting ass?")

@dp.message_handler()
async def echo(message: types.Message):
    # Здесь идет обработка сообщений
    val = random.randint(0, 5)
    photo = open(f"billy.jpg", 'rb')
    await message.answer_photo(photo=photo)
    if val == 0:
        await message.answer("three hundred bucks")
    elif val == 1:
        await message.answer("fuck you")
    elif val == 2:
        await message.answer("oh shit im sorry")
    elif val == 3:
        await message.answer("lets selebrate and suck some dick")
    else:
        await message.answer("Fisting ass")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)