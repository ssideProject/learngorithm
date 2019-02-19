import numpy as np

ls1 = np.arange(1, 101)

def sum_sub():
    result = -sum(range(0, 101, 2)) + sum(range(1, 101, 2))
    print(result)

def sum_sub2(list):
    result = 0
    for i in list:
        result= (result - i, result + i)[i%2 == 0]
    return result

sum_sub()

sum_sub2(ls1)