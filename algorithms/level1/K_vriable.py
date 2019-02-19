array1 = [1, 5, 2, 6, 3, 7, 4]
commands2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(len(commands2))

def solution(array, commands):
    result = []
    temp = []
    for i in commands:
        print(i)
        temp = array[i[0]-1:i[1]].sort()
        print(temp)
        result.append(temp[i[2]-1])
    return result

def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(solution(array1, commands2))