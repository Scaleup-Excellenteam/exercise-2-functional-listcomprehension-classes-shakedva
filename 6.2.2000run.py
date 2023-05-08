import timeit
import contextlib
import io


def timer(function, *args, **kwargs):
    """
    Receives a function, its arguments and key arguments and measure the speed of this function.
    :param function: a function.
    :param args: args to pass to the function.
    :param kwargs: kwargs to pass to the function.
    :return: The amount of time passed between starting the function received and ending it.
    """
    with contextlib.redirect_stdout(io.StringIO()):
        execution_time = timeit.timeit(lambda: function(args, **kwargs), number=1000)
    return execution_time


def main():
    """
    Calls timer function with a function and its arguments, and prints the time it took to execute it.
    """
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))


if __name__ == "__main__":
    main()
