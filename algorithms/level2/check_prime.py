from sympy import isprime
import math
from itertools import permutations

def solution(numbers):
    answer = 0
    print(numbers)
    print(len(numbers))
    temp = [e for e in numbers]
    print(temp)
    tmp = []
    tmp2 = []
    for i in range(1, len(numbers)+1):
        per = permutations(temp, i)
        tmp += list(set(per))
        print(tmp)
    for i in tmp:
        tmp2.append(int("".join(i)))
    tmp2 = list(set(tmp2))
    print(tmp2)
    tmp2.sort()

    for i in tmp2:
        cnt = 0
        if i == 2:
            answer += 1
        else:
            for j in range(2, int(math.sqrt(i)+1)):
                if i % j == 0:
                    cnt += 1
            if cnt == 0 and i > 2:
                answer += 1
    return answer

print(solution('113'))