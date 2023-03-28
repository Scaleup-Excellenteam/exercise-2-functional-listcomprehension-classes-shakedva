import time


def timer(f, *args, **kwargs):
    start_time = time.time()
    f(args, **kwargs)
    # time.sleep(2)
    end_time = time.time()
    return end_time - start_time


# print(timer(print, "Hello"))
# print(timer(zip, [1, 2, 3], [4, 5, 6]))
# print(timer("Hi {name}".format, name="Bug"))
