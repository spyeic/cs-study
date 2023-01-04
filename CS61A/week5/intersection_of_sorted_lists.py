
def find_both(list1, list2):
    index1 = 0
    index2 = 0
    both = []
    while not (len(list1) == index1 or len(list2) == index2):
        n1 = list1[index1]
        n2 = list2[index2]
        if n1 < n2:
            index1 += 1
        elif n1 > n2:
            index2 += 1
        else:
            index1 += 1
            index2 += 1
            both.append(n1)

    return both


l1 = [4, 6, 9, 14]
l2 = [5, 4, 7, 6, 1]

