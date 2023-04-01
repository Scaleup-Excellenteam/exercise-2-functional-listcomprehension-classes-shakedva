import time


def timer(f, *args, **kwargs):
    """
    :param f: function.
    :param args: args to pass to the function.
    :param kwargs: kwargs to pass to the function.
    :return: The amount of time passed between starting the function received and ending it.
    """
    start_time = time.time()
    f(args, **kwargs)
    end_time = time.time()
    return end_time - start_time

