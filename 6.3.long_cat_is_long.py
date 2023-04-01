import re

# non-alphanumeric characters regex
PATTERN = r"([^\w\s])"


def count_words(text):
    """
    :param text: str
    :return: a dictionary that maps words from the text to their length
    """
    text = text.lower()
    words = [re.sub(PATTERN, '', word) for word in text.split()]
    count_dict = {word: len(word) for word in words}
    return count_dict
