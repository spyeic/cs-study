import lib.utils as utils


def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)


def exp_fast(b, n):
    if n == 0:
        return 1
    if b % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return exp_fast(b, n - 1)


def square(n):
    return n * n
