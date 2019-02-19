def solution(arrangement):
    temp = [e for e in arrangement]
    count =0
    stack =[]
    for i in range(0, len(temp)):
        if temp[i]=='(':
            stack.append('(')
        else:
            stack.pop()
            print(stack.__len__())
            if temp[i-1] =='(':
                count += len(stack)
            else:
                count +=1
        print("count %d" %count)
    return count





print(solution("(()(())())"))