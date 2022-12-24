def sum_digits_rec(n):
    if n < 10:
        return n
    return sum_digits_rec(n // 10) + (n % 10)


def sum_digits_iter(n):
    total = 0
    while n > 0:
        total += (n % 10)
        n = n // 10
    return total


def cascade(n):
    if n < 10:
        return
    else:
        print(n // 10)
        cascade(n // 10)


def inverse_cascade(n):
    if n < 10:
        print(n)
        return
    else:
        inverse_cascade(n // 10)
        print(n)
        return


def combine(n):
    inverse_cascade(n)
    cascade(n)
