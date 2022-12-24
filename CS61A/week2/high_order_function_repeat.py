def repeat(f, a):
    while f(a) != a:
        a = f(a)
    return a


def g(y):
    return (y + 5) // 3


print(repeat(g, 1))
