from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_router = Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await (message.answer("Привет, это бот по FunTime валюте!"))

@user_router.message(F.text.lower() == ('каталог'))
@user_router.message(Command('catalog'))
async def catalog(message: types.message):
    await (message.answer('Это каталог'))

@user_router.message(F.text.lower() == ('корзина'))
@user_router.message(Command('busket'))
async def busket(message: types.message):
    await (message.answer('Это корзина'))

@user_router.message(F.text.lower() == ('оплата'))
@user_router.message(Command('donat'))
async def donat(message: types.message):
    await (message.answer('Плати'))

# @user_router.message(F.text.lower().contains('стои')|F.text.lower().contains('цен'))
# async def echo(message: types.Message):
#     await(message.answer("Только команды!"))
    # user_text=message.text
    # await (message.answer(user_text))

