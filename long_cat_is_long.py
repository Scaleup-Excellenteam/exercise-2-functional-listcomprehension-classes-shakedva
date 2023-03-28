import re

PATTERN = r"([^\w\s])"


def count_words(text):
    text = text.lower()
    words = [re.sub(PATTERN, '', word) for word in text.split()]
    count_dict = {word: len(word) for word in words}
    return count_dict

