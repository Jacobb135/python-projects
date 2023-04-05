from wonderwords import RandomSentence

s = RandomSentence()
random_word_list = []


def random_words():
    random_word_list.clear()
    for _ in range(6):
        words = s.sentence()
        random_word_list.append(str(words))
        words_to_type = " ".join(random_word_list)
    return words_to_type