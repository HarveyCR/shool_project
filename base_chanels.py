import sqlite3
import random

alphabet = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',


def chanel_base_confim(chanel_id):
    conn = sqlite3.connect('chanels_and_user.db')
    cursor = conn.cursor()
    results = cursor.execute(f"""SELECT Telegram_ID FROM chanels_groups WHERE Telegram_ID = {chanel_id}""").fetchall()
    print(chanel_id, results)
    print(results is False)

    name_id = alphabet[random.randint(0, 25)]
    for i in range(15):
        name_id += alphabet[random.randint(0, 35)]
    # print(name_id)

    if len(results) < 1:
        cursor.execute(
            f"""INSERT INTO chanels_groups('name_id', 'Telegram_ID', 'warning', 'duration') VALUES('{name_id}', {chanel_id}, 'Пожалуйста, соблюдайте правила ссобщества!', 0)""")
        cursor = conn.cursor()

        cursor.execute(f"""CREATE TABLE {name_id}
(Id INT,
 violations INT(20))""")
        conn.commit()
        conn.close()
        return
    conn.close()


def user_status_cheak(user_id, chanel_id):
    conn = sqlite3.connect('chanels_and_user.db')
    cursor = conn.cursor()

    table = cursor.execute(f"""SELECT name_id FROM chanels_groups WHERE Telegram_ID = {chanel_id}""").fetchall()[0][0]
    name = cursor.execute(f"""SELECT id FROM {table} WHERE id = {user_id}""").fetchall()
    print(chanel_id, table, name)
    print(table is False)
    if len(name) < 1:
        cursor.execute(
            f"""INSERT INTO {table}('Id', 'violations') VALUES({user_id}, 0)""")
        cursor = conn.cursor()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    user_status_cheak(-15321564, 154965832498)
