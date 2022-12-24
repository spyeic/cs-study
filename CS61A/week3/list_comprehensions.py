list1 = [[1, 2], [2, 2], [3, 4], [7, 9]]

for x, y in list1:
    print(x, y)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
new = [letters[i] for i in [1, 3, 4, 5]]
print(new)
new = [i for i in letters if i == 'a' or i == 'g']
print(new)


def divisors(n):
    return [k for k in range(1, n) if n % k == 0]


# start:end:step start <= ... < end
li = letters[:5:]
print(li)

lis = [1, 2, 3, 4, 5]
lis[1:3] = [7, 7, 7, 7, 7]
print(lis)
