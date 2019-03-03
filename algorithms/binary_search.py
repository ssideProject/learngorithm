ls = [1, 4, 7, 8, 9, 10, 13, 15, 20]

def binary_search(list, num):
    end = len(list)-1
    start = 0
    while start <= end:
        mid = (start+end)//2
        if list[mid] == num:
            return mid
        elif list[mid] > num:
            start = mid+1
        else:
            end = mid-1
    return -1

print(binary_search(ls, 4))