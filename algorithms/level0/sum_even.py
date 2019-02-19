import numpy as np

ls1 = np.arange(1, 101)

def max_even(list):
    return (len(list)+1)*len(list)//4

def max_even2(list):
    sum = 0
    for i in list:
        if i%2 != 0:
           sum = i
    return sum




print(max_even(ls1))
print(max_even(ls1))