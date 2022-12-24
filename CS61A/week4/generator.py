def evens(start, end):
    start = start + start % 2
    while start <= end:
        yield start
        start += 2


def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x


def a_then_b1(a, b):
    yield from a
    yield from b
