import time

from aiogram.types import ChatMember

from TOKEN_API import TOKEN_API
from aiogram import Bot, Dispatcher, executor, types
from utils import ban_word_cheak
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
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожповать в бот модератор. Добавьте меня в группу, настройти и я буду модерировать чат!")


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["status"])
async def status_command(message: types.Message):
    print(base_chanels.chanel_base_confim(message.chat.id))
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["ban"])
async def ban_command(message: types.Message):
    chat_admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    admins_userId = [admins.user.id for admins in chat_admins]
    if message.from_user.id not in admins_userId:
        await message.reply(text="Этой командой могут пользоваться только админы!")
        return
    if message.reply_to_message.from_user.id in admins_userId:
        await bot.send_message(message.chat.id,
                               text="Вы пытаетесь забанить админа!",
                               reply_to_message_id=message.reply_to_message.message_id)
        return
    # await message.reply
    duration = 35
    message_text = "Вы были забанены админом!"
    message_box = message.text.split(" ")
    if len(message_box) == 2:
        duration = int(message_box[1])
    elif len(message_box) > 2:
        message_text = " ".join(message_box[2:])

    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                   ChatMember(can_send_messages=False),
                                   until_date=time.time() + duration)
    await bot.send_message(message.chat.id,
                           text=message_text,
                           reply_to_message_id=message.reply_to_message.message_id)


@dp.message_handler()
async def send_answer(message: types.Message):
    base_chanels.chanel_base_confim(message.chat.id)
    base_chanels.user_status_cheak(message.from_user.id, message.chat.id)

    chat_admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    admins_userId = [admins.user.id for admins in chat_admins]

    print(message.from_user.id in admins_userId)
    if message.from_user.id == 777000:
        await message.reply(text=WARNING_MESSAGE, parse_mode='HTML')

    else:
        if ban_word_cheak.ban_word_cheak(message.text.lower()) is True and message.from_user.id not in admins_userId:
            await bot.restrict_chat_member(message.chat.id, message.from_user.id, ChatMember(can_send_messages=False),
                                           until_date=time.time() + 35, )
            await bot.send_message(message.chat.id,
                                   text="Вам запрещено отправлять сюда сообщения в течение 35 секунды.",
                                   reply_to_message_id=message.message_id)
            # await message.reply(text="Вы использовали запрещенное слово! Если такое продолжиться, вы будите забаненны!")
            # await message.delete()
    # print(message.from_user.id)


async def on_startup(_):
    print("Bot secsesefuly start!")


def start():
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    start()
