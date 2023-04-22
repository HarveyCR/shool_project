async def start_command(message, bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожповать в бот модератор. Добавьте меня в группу, и я буду модерировать чат!\nДля подробного ознакомления нажмите команду /help")
