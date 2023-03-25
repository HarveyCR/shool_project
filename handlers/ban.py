import time

from aiogram.types import ChatMember


async def ban_command(message, bot):
    if message.chat.type == "private":
        await message.reply(text="Эта команда работает только в группах")
        return

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
