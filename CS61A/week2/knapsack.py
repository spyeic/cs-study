def split(n) -> tuple[int, int]:
    return n // 10, n % 10


def knapsack(n, k):
    before, last = split(n)
    if last == k:
        return True
    if before == 0:
        return last == k
    return knapsack(before, k - last) or knapsack(before, k)
