def apply_twice(fn, a):
    return fn(fn(a))


def add_five(x):
    return x + 5


# Apply the function twice
r: int = apply_twice(add_five, 1)
print(r)


def compose_fn(f, g):
    def h(x):
        return f(g(x))

    return h


def square(x):
    return x * x


def add_one(x):
    return x + 1


# compose two functions, return the composed function
r = compose_fn(square, add_one)(3)
print(r)


def compose_all(*functions):
    def h(x):
        for f in reversed(functions):
            x = f(x)
        return x

    return h
