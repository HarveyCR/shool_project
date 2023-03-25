from utils import base_chanels

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/ban</b> - <em>забанить участника(только админы)</em>
<b>/status</b> - <em>пропишите команду в чате группы и для получения статуса чата</em>
"""


async def status_command(message, bot):
    print(message.chat.type)
    if message.chat.type == "private":
        await message.reply(text="Пропишите команду в чате группы и для получения статуса чата")
        return

    print(base_chanels.chanel_base_confim(message.chat.id))
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND, parse_mode="HTML")
