import time

from aiogram.types import ChatPermissions

from TOKEN_API import TOKEN_API
from aiogram import Bot, Dispatcher, executor, types
from utils import ban_word_cheak
# from utils import base_chanels

from handlers import start, status, ban, help
from utils import base_chanels

# from database_conection import chanel_base_confim

# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/ban</b> - <em>забанить участника(только админы)</em>
<b>/status</b> - <em>пропишите команду в чате группы и для получения статуса чата</em>
"""

WARNING_MESSAGE = """
<b>Пожалуйста, соблюдайте правила ссобщества!</b>
"""


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await start.start_command(message, bot)


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await help.help_command(message, bot)


@dp.message_handler(commands=["status"])
async def status_command(message: types.Message):
    await status.status_command(message, bot)


@dp.message_handler(commands=["ban"])
async def ban_command(message: types.Message):
    await ban.ban_command(message, bot)


@dp.message_handler()
async def send_answer(message: types.Message):
    base_chanels.chanel_base_confim(message.chat.id)
    # base_chanels.user_status_cheak(message.from_user.id, message.chat.id)

    chat_admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    admins_userId = [admins.user.id for admins in chat_admins]

    print(message.from_user.id in admins_userId)
    if message.from_user.id == 777000:
        await message.reply(text=WARNING_MESSAGE, parse_mode='HTML')

    else:
        if ban_word_cheak.ban_word_cheak(message.text.lower()) is True and message.from_user.id not in admins_userId:
            await bot.restrict_chat_member(message.chat.id, message.from_user.id,
                                           ChatPermissions(can_send_messages=False),
                                           until_date=time.time() + 35, )
            await bot.send_message(message.chat.id,
                                   text="Вам запрещено отправлять сюда сообщения в течение 35 секунды.",
                                   reply_to_message_id=message.message_id)
            # await message.reply(text="Вы использовали запрещенное слово! Если такое продолжиться, вы будите забаненны!")
            # await message.delete()
    # print(message.from_user.id)


async def on_startup(_):
    print("Bot secsesefuly start!")


def start_bot():
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    start_bot()
