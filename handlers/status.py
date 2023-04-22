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
    print(message.text.lower())
    if "true" in message.text.lower() or "false" in message.text.lower():
        status = base_chanels.moderation_cheack_change(message.chat.id, meaning=message.text.lower().split(" ")[1])
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Включение модерации: {status}", parse_mode="HTML")
        return
    result = base_chanels.chanel_base_confim(message.chat.id)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Включение модерации: {bool(result[0][0])}", parse_mode="HTML")
