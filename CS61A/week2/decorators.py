import time


def trace1(fn):
    print("The decorator is called")

    def new_fn(n):
        print("This is the new function")
        return fn(n)

    return new_fn


# equals to square = trace1(square)
@trace1
def square(n):
    return n * n


def square_sum_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total


def timer(fn):
    def new_fn(*args):
        start = time.time_ns()
        result = fn(*args)
        print(f"Time cost: {(time.time_ns() - start) / 1000000} ms for function {fn.__name__}")
        return result
    return new_fn


@timer
def cube(n):
    return n * n * n


def err():
    pass


@err
def make_err():
    print("Can't exec this function")
