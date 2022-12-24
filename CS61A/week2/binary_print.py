# 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101...
# k digits
def all_nums(k):
    if k == 0:
        return

    def func(n, a):
        print(a)
        if n == k:
            return
        func(n + 1, a * 10)
        func(n + 1, a * 10 + 1)
    print(0)
    func(1, 1)


def all_nums1(k):
    def func(n, prefix):
        if n == 0:
            print(prefix)
            return
        func(n - 1, prefix * 10)
        func(n - 1, prefix * 10 + 1)
    func(k, 0)


all_nums1(4)
