
def fact(n):
    """ Factorial function
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    """
    assert isinstance(n, int)
    assert n >= 0
    if n == 0:
        return 1
    return fact(n - 1) * n


def half_fact(n):
    return fact(n / 2)
