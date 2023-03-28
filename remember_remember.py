import cv2
import numpy as np


def find_hidden_messages(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # save indices where the pixel is black
    result = np.where(img == 1)
    list_of_coordinates = list(zip(result[0], result[1]))
    # sort by column
    list_of_coordinates.sort(key=lambda x: x[1])
    hidden_msg = [chr(i) for i, j in list_of_coordinates]
    return "".join(hidden_msg)


find_hidden_messages('code.png')

# naive solution
# def find_hidden_messages(path):
#     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#     hidden_msg = []
#     for j in range(len(img[0])):
#         for i in range(len(img)):
#             if img[i][j] == 1:  # pixel is black
#                 hidden_msg.append(i)
#                 break
#
#     hidden_msg = [chr(char) for char in hidden_msg]
#     return "".join(hidden_msg)
