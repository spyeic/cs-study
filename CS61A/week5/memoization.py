import time


def memo(f):
    cache = {}

    def from_cache(n):
        if n not in cache:
            cache[n] = f(n)

        return cache[n]

    return from_cache


def timer(f):
    def new_fun(n):
        start = time.time()
        r = f(n)
        print(f"takes {(time.time() - start) * 1000} ns to run function {f.__name__}")
        return r

    return new_fun


def fib_raw(n):
    if n == 0 or n == 1:
        return n
    return fib_raw(n - 1) + fib_raw(n - 2)


@timer
def fib(n):
    return fib_raw(n)


@timer
@memo
def new_fib(n):
    return fib_raw(n)
