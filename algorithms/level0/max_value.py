import numpy as np
list1 = np.arange(1, 10,1)

def max_value(list):
    max = 0
    for i in range(len(list)):
        if max <= list[i]:
            max = list[i]
    return max

print(max_value(list1))
print(max(list1))