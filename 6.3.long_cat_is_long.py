import re

# non-alphanumeric characters regex
PATTERN = r"([^\w\s])"


def count_words(text):
    """
    Receives text as string and returns a map of words from the text to their length
    :param text: str
    :return: a dictionary that maps words from the text to their length
    """
    text = text.lower()
    # split the text into words and remove non-alphanumeric characters.
    words = [re.sub(PATTERN, '', word) for word in text.split()]
    count_dict = {word: len(word) for word in words}
    return count_dict


def main():
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))


if __name__ == "__main__":
    main()
