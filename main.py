import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from pyexpat.errors import messages

TOKEN= "7028073659:AAErWTfD_vHqxfOwb823LP7WxcjZg5lL_1A"

bot = Bot(token = TOKEN)
dp = Dispatcher()
from handlers.user_private import user_router
dp.include_router(user_router)

from handlers.user_group import group_router
dp.include_router(group_router)

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())