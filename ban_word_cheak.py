def ban_word_cheak(sentence):
    sentence_words = sentence.lower().split(" ")
    with open('ban_words.txt') as f:
        ban_words = [word.strip("\n") for word in f.readlines()]
    for word in sentence_words:
        new_word = ''
        for letter in word:
            if letter.isalpha() is True:
                new_word += letter
        if new_word in ban_words:
            return True


if __name__ == '__main__':
    ban_word_cheak("Это самый   крвссный р_о_м_б")