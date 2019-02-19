priorities = [1,1,9,1,1,1]
location = 0


def solution(priorities, location):
    max = 0
    stack = priorities.copy()

    for i in priorities:
        if max < i:
            max = i

    stack[location] = 'a'

    for i in range(len(priorities)):
        print(stack.index('a'))
        if priorities[0] != max:
            print(priorities[0], stack[0])
            priorities.append(priorities.pop(0))
            stack.append(stack.pop(0))
        return stack.index('a')

print(solution(priorities,location))