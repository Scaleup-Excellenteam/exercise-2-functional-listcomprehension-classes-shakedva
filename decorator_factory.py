from functools import wraps


class IncorrectTypeException(Exception):
    """
    Custom exception for comparing types.
    """
    def __init__(self, expected_type, actual_type):
        self.message = f"Expected type {expected_type}, got {actual_type} instead"
        super().__init__(self.message)


def check_type(correct_type):
    def check_type_decorator(f):
        @wraps(f)
        def wrapper(num):
            if type(num) != correct_type:
                raise IncorrectTypeException(correct_type, type(num))
            return f(num)
        return wrapper
    return check_type_decorator


"""
Example usage:
@check_type(int)
def times2(num):
    print(num ** 2)
"""
