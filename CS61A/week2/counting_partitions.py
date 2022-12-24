from lib.ucb import trace


# Expect result:
# n is the original value, the function is trying to split
# n into many pieces such the sum of these piece is n.
# a is the max value of one piece.
@trace
def count_partitions(n, a):
    r = n - a
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif a == 0:
        return 0
    else:
        return count_partitions(r, a) + count_partitions(n, a - 1)


print(count_partitions(6, 4))
