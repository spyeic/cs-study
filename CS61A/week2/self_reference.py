def print_all(n):
    print(n)
    return print_all


print_all(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)


def print_sums(n):
    print(n)

    def p(k):
        return print_sums(n + k)
    
    return p


print_sums(1)(3)(5)(7)

