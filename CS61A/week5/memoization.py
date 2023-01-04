import time


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def memo(f):
    cache = {}

    def from_cache(n):
        if n not in cache:
            cache[n] = f(n)

        return cache[n]

    return from_cache


def count(fn):
    """
    Without memoization:
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.count
    21891

    With memoization:
    >>> fib = memo(fib)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.count
    39
    :param fn:
    :return:
    """
    def counted(n):
        counted.count += 1
        return fn(n)
    counted.count = 0
    return counted



