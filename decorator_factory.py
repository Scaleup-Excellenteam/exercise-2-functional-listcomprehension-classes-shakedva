from functools import wraps


class IncorrectTypeException(Exception):
    """
    Custom exception for comparing types.
    """
    def __init__(self, expected_type, actual_type):
        self.message = f"Expected type {expected_type}, got {actual_type} instead"
        super().__init__(self.message)


def check_type(correct_type):
    """
    A decorator that checks whether the function's element type is the expected one.
    Raising an exception if they don't match.
    :param correct_type: the expected type of the function
    :return: a decorator that can be used in a function
    """
    def check_type_decorator(f):
        """
        :param f: function to be decorated
        :return: a wrapped function that checks the type of its argument
        """
        @wraps(f)
        def wrapper(element):
            """
            :param element: an element to check its type
            :return: result of the original function f with its element
            :raise: when the element is not the expected type.
            """
            if type(element) != correct_type:
                raise IncorrectTypeException(correct_type, type(element))
            return f(element)
        return wrapper
    return check_type_decorator


@check_type(int)
def times2(num):
    """
    Uses decorator that checks that the num received is in type int.
    Print the power of the given number by 2.
    :param num: int to be powered by 2
    """
    print(num ** 2)


@check_type(str)
def hello_name(name):
    """
    Uses decorator that checks that the name received is in type str.
    :param name: a name to print with the preceding of the word hello.
    """
    print(f"Hello, {name}")


def main():
    times2(3)
    hello_name('Shaked')


if __name__ == "__main__":
    main()
