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
        await message.reply(
            text="Пропишите команду в чате группы и для получения статуса чата /status:\n Выводиться поле с данными как автомотическая модерация по заданному списку(по умолчанию False) и напрямую щапрещенные слова\n"
                 "Запрещенная модерауия True или False. Специально заданные список может быть пустым или задан админами\n"
                 "Чтобы поменять Модерауию напишите в группу '/status moderation True' для включения или '/status moderation False' для выключения\n"
                 "Для добавления введите '\status forbiddena словa',  для удаления '\status forbiddenr слово'")
        return
    print(message.text.lower(), "Статус")
    if "moderation" in message.text.lower():
        if "true" in message.text.lower() or "false" in message.text.lower():
            status = base_chanels.moderation_cheack_change(message.chat.id, meaning=message.text.lower().split(" ")[2])
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Включение модерации: {status}", parse_mode="HTML")
            return
    elif "forbidden" in message.text.lower():
        if "forbiddena" in message.text.lower():
            new_words = base_chanels.forbidden_words_add(message.chat.id, message.text.lower())
        elif "forbiddenr" in message.text.lower():
            new_words = base_chanels.forbidden_words_remove(message.chat.id, message.text.lower())
        else:
            pass
    new_words = '\n'.join(new_words)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Включение модерации: {bool(base_chanels.chanel_base_confim(message.chat.id)[0][0])}\n Запрещенные слова:\n {new_words.strip()}", parse_mode="HTML")
