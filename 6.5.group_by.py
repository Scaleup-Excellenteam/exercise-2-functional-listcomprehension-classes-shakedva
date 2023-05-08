from collections import defaultdict


def group_by(function, elements):
    """
    This function groups elements of an iterable into a dictionary based on the return value of the given function.
    :param function: function
    :param elements: iterable to group
    :return: a dictionary:
            the keys are the return values from the function
            the values are lists of the elements that got the return value of the key.
    """
    res_dict = defaultdict(list)
    [res_dict[function(i)].append(i) for i in elements]
    return dict(res_dict)


def main():
    """
    Calls the function group_by in order to group the elements based on the output of the function sent. 
    """
    print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == "__main__":
    main()

