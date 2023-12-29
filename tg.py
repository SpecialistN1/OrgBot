import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 
from aiogram.types import Message
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Здарова, заебал!")

async def main():
    dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
