d = [5,3,4,2,1,6,8]

def solution(d):
    for i in range(0, len(d)-1):
        for j in range(i+1, len(d)):
            if d[i] > d[j]:
                d[i], d[j] = d[j], d[i]
    return d

print(solution(d))