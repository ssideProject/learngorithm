def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    g1 = merge_sort(a[:mid])
    print(g1)
    g2 = merge_sort(a[mid:])
    print(g2)

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result


def merge_sort2(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort2(g1)
    merge_sort2(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        print(i1, i2, ia)
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
    return a

d = [5, 1,3, 9, 4,10]
print(merge_sort2(d))