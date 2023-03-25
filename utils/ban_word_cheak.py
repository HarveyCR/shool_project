def ban_word_cheak(sentence):
    print(sentence)
    sentence_words = sentence.lower().split(" ")
    with open('ban_words.txt') as f:
        ban_words = [word.strip("\n").lower() for word in f.readlines()]
    for word in sentence_words:
        new_word = ''
        for letter in word:
            if letter.isalpha() is True:
                new_word += letter
        print(ban_words, new_word)
        if new_word in ban_words:
            return True
    return False


if __name__ == '__main__':
    print(ban_word_cheak("ОГО ромб!"))
