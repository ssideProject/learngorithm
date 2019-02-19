def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j= i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def insert_sort_fit(collection):
    for index in range(1, len(collection)):
        while 0 < index and collection[index] < collection[index-1]:
            collection[index], collection[index-1] = collection[index-1], collection[index]
            index -=1
    return collection

list1 =[5,4,6,7,2,4,2,7]
list2 =[5,4,6,7,2,4,2,7]

print(insert_sort(list1))
print(insert_sort_fit(list2))