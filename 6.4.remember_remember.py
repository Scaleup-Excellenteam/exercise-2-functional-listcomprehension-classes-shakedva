import cv2
import numpy as np


def find_hidden_messages(path):
    """
    Receives a path to an image and returns the hidden message in it.
    The characters for the message are written using the indices of the black pixels.
    The message is written in the order of the columns, the character's value is the index of the row.
    :param path: to an image file
    :return: a hidden message within the file
    """
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # black pixel
    result = np.where(img == 1)
    list_of_coordinates = list(zip(result[0], result[1]))
    # sort by column
    list_of_coordinates.sort(key=lambda x: x[1])
    hidden_msg = [chr(i) for i, j in list_of_coordinates]
    return "".join(hidden_msg)


def main():
    """
     Receives a path to an image with a hidden message and calls the function to extract the hidden message and print it
    """
    image_path = input("Enter the path to the file: ")
    print(find_hidden_messages(image_path))


if __name__ == "__main__":
    main()
