def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """

    def func_adder(g):
        "*** YOUR CODE HERE ***"

        def k(x):
            return func(g(x))

        return composer(k)

    return func, func_adder


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2 * b + 3 * a
        n -= 1
    return c


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    """
    "*** YOUR CODE HERE ***"
    """
    def f(nu, s):
        before, last = nu // 10, nu % 10
        if nu <= 0:
            return 0
        elif last > s:
            return f(before, s)
        elif last < s:
            return f(nu, s - 1) + 1
        else:
            return f(before, s - 1)

    return f(n, n % 10)
    """
    before, last = n // 10, n % 10
    if before == 0:
        return 0
    before_s_last = before % 10
    dif = last - before_s_last - 1
    if dif < 0:
        dif = 0
    return missing_digits(before) + dif


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"

    def f(n, t):
        if n == 0:
            return 1
        if n < 2 ** t:
            return 0
        return f(n - 2 ** t, t) + f(n, t + 1)

    return f(total, 0)
