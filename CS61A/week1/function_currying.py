
# Function currying is to convert a function that takes multiple arguments
# into a function that takes a single argument and returns another function
# that takes the next argument and so on.

def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def add(x, y):
    return x + y


fn = curry(add)
add_three = fn(3)
print(add_three(2))
