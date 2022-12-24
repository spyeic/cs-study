# Recursive function: a function calls itself
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)


def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


def split(n):
    return n % 10, n // 10


def luhn_algorithm(n):
    if n < 10:
        return n
    last, before_last = split(n)
    return luhn_double(before_last) + last


def luhn_double(n):
    last, before_last = split(n)
    double = sum_digits(2 * last)
    if n < 10:
        return double
    return luhn_algorithm(before_last) + double
