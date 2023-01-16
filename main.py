from TOKEN_API import TOKEN_API
from aiogram import Bot, Dispatcher, executor, types
from ban_word_cheak import ban_word_cheak

# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка фото</em>
"""

WARNING_MESSAGE = """
<b>Пожалуйста, соблюдайте правила ссобщества!</b>
"""


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Добро пожповать в бот модератор. Заданатьте нам 100 российских тенге и мы может что-то сделаем!")


@dp.message_handler()
async def send_answer(message: types.Message):
    if message.from_user.id == 777000:
        await message.reply(text=WARNING_MESSAGE, parse_mode='HTML')
    else:
        if ban_word_cheak(message.text.lower()) is True:
            await message.reply(text="Вы использовали запрещенное слово! Если такое продолжиться, вы будите забаненны!")
            await message.delete()
    # print(message.from_user.id)


async def on_startup(_):
    print("Bot secsesefuly start!")


async def start():
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    start()
