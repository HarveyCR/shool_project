import time

from aiogram.types import ChatPermissions


async def ban_command(message, bot):
    if message.chat.type == "private":
        await message.reply(text="Команда для бана участников(доступно только админам паблика). Работает так:\n"
                                 "Чтобы забанить игрока ответи на его сообщение камандой /ban его сообщение. Там может быть 2 параметра:\n"
                                 "Продолжительности бана в секундах, не меньше 35 по умолчанию - 35\n"
                                 "Сообщение которое увидет получатель бана - по умолчанию 'Вы были забанены админом!\n'"
                                 "Параметры можно не прописывать и просто написать /ban но если они есть то должны прописываться строго через пробел!")
        with open(f'K:/shool_project/shool_project/ban.png', 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo=photo)
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
                                   ChatPermissions(can_send_messages=False),
                                   until_date=time.time() + duration)
    await bot.send_message(message.chat.id,
                           text=message_text,
                           reply_to_message_id=message.reply_to_message.message_id)
