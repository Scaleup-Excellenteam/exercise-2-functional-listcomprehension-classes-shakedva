from collections import defaultdict


def group_by(func, iterable):
    """
    The function groups elements of an iterable into a dictionary.
    :param func: function
    :param iterable:
    :return: a dictionary:
            the keys are the return values from the function
            the values are lists of the elements that got the return value of the key.
    """
    res_dict = defaultdict(list)
    for i in iterable:
        res_dict[func(i)].append(i)
    return res_dict
