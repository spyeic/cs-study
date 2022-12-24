# Example: Fibonacci
# Note: It's not an efficient way
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


def fib1(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

