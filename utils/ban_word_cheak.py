import sqlite3


def ban_word_cheak(sentence, chat_id):
    print(sentence)
    sentence_words = sentence.lower().split(" ")
    with open('utils/ban_words.txt') as f:
        ban_words = [word.strip("\n").lower() for word in f.readlines()]
    conn = sqlite3.connect('utils/chanels_and_user.db')
    cursor = conn.cursor()
    result = cursor.execute(f"""SELECT forbidden_words FROM Telegram_channels WHERE name_id = {chat_id}""").fetchall()[0]
    conn.close()
    if bool(result) is False:
        ban_words = ban_words + (" ".join(result)).strip().split(" ")
    # print(ban_words)
    for word in sentence_words:
        new_word = ''
        for letter in word:
            if letter.isalpha() is True:
                new_word += letter
        # print(ban_words, new_word)
        if new_word in ban_words:
            return True
    return False


if __name__ == '__main__':
    print(ban_word_cheak("ОГО ромб!"))
