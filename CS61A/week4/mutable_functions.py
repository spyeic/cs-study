def make_withdraw(balance):

    def withdraw(m):
        nonlocal balance
        last = balance - m
        if last >= 0:
            balance = last
            return last
        else:
            return "Can't withdraw"

    return withdraw


def make_withdraw2(balance):
    b = [balance]

    def withdraw(m):
        last = b[0] - m
        if last >= 0:
            b[0] = last
            return last
        else:
            return "Can't withdraw"

    return withdraw
