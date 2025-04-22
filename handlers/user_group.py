from aiogram import types, Router, F

group_router = Router()

restricted_words = ['червяк','училка','домашка','дорого','дорогой']

@group_router.message()
async def worlds(message: types.Message):
    worlds_list = message.text.split(' ')
    for word in worlds_list:
        if word in restricted_words:
            await (message.answer('Соблюдайте правила чата!'))
            await message.delete()
            break

