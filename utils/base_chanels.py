import sqlite3

# import random

alphabet = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',


def chanel_base_confim(chanel_id):
    conn = sqlite3.connect('utils/chanels_and_user.db')
    cursor = conn.cursor()
    results = cursor.execute(f"""SELECT name_id FROM Telegram_channels WHERE name_id = {chanel_id}""").fetchall()
    # print(chanel_id, results)
    # print(bool(results))
    if bool(results) is False:
        cursor.execute(
            f"""INSERT INTO Telegram_channels (name_id, cheack) VALUES('{chanel_id}', True)""")
    result = cursor.execute(f"""SELECT cheack FROM Telegram_channels WHERE name_id = {chanel_id}""").fetchall()
    conn.commit()
    conn.close()
    return moderation_cheack(chanel_id)


def moderation_cheack(chanel_id):
    conn = sqlite3.connect('utils/chanels_and_user.db')
    cursor = conn.cursor()
    result = cursor.execute(f"""SELECT cheack FROM Telegram_channels WHERE name_id = {chanel_id}""").fetchall()
    conn.close()
    return result


def moderation_cheack_change(chanel_id, meaning):
    # print(chanel_id, meaning, "я тут был")
    conn = sqlite3.connect('utils/chanels_and_user.db')
    cursor = conn.cursor()
    if meaning == "true":
        meaning = True
    elif meaning == "false":
        meaning = False
    else:
        return "некоректный статус"
    cursor.execute(f"""UPDATE Telegram_channels SET cheack = {meaning} WHERE name_id = {chanel_id}""")
    conn.commit()
    conn.close()
    # print(meaning, "Что не работает")
    return meaning


def forbidden_words_add(chanel_id, words):
    # print("биба и боба")
    conn = sqlite3.connect('utils/chanels_and_user.db')
    cursor = conn.cursor()
    result = cursor.execute(f"""SELECT forbidden_words FROM Telegram_channels WHERE name_id = {chanel_id}""").fetchall()[0]
    print(result, words.split(' ')[2:])
    if len(result) == 0:
        result = words.split(' ')[2:]
    else:
        result = ' '.join(result).split(" ") + words.split(' ')[2:]
    cursor.execute(
        f"""UPDATE Telegram_channels SET forbidden_words = '{' '.join(result)}' WHERE name_id = {chanel_id}""")
    # cursor.execute(
    #     f"""UPDATE Telegram_channels SET forbidden_words = 'кт я' WHERE name_id = -1001835833661""")
    conn.commit()
    conn.close()
    return result


def forbidden_words_remove(chanel_id, word):
    conn = sqlite3.connect('utils/chanels_and_user.db')
    cursor = conn.cursor()
    result = cursor.execute(f"""SELECT forbidden_words FROM Telegram_channels WHERE name_id = {chanel_id}""").fetchall()
    result = (' '.join(' '.join(result[0]).split(" "))).replace(word.split(' ')[2], "")
    # print(result, 'Ремув')
    cursor.execute(
        f"""UPDATE Telegram_channels SET forbidden_words = '{result}' WHERE name_id = {chanel_id}""")
    # cursor.execute(
    #     f"""UPDATE Telegram_channels SET forbidden_words = 'кт я' WHERE name_id = -1001835833661""")
    conn.commit()
    conn.close()
    return [result]


if __name__ == '__main__':
    chanel_base_confim(-156123165414456)
    # user_status_cheak(-15321564, 154965832498)
    # print('aaa'.replace('a', ""))
