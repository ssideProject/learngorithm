class Solve:
    def __init__(self):
        self.pic =[[]]
        self.navigation =[[]]

    def solution(self, m=0, n=0, picture=[]):
        self.navigation = [[0 for i in range(n)] for j in range(m)]
        self.pic = picture
        # 함수에서 만든 변수를 다른 함수에서 받아서 사용가능한가?
        result = []
        numberOfArea = 0
        maxSize = 0

        for i in range(m):
            for j in range(n):
                if(picture[i][j] !=0 and self.navigation[i][j]== 0):
                    ++numberOfArea
                    sum = self.quest(i, j)
                    if( sum > maxSize):
                        maxSize = sum

        result.append(numberOfArea)
        result.append(maxSize)
        return result

    def quest(self, i, j):
        sum = 1
        self.navigation[i][j] = 1
        if i >= 0 and self.navigation[i+1][j] == 0 and self.pic[i][j] == self.pic[i+1][j]:
            # 행(세로축, i, m)이 아래로 탐색
            sum += self.quest(i+1, j)
        if j <= len(self.navigation[i]) and self.navigation[i][j-1] ==0 and self.pic[i][j] == self.pic[i][j-1]:
            # 열(가로축, j, n)이 왼쪽으로 탐색
            sum += self.quest(i, j-1)
        if j >= 0 and self.navigation[i][j+1] ==0 and self.pic[i][j] == self.pic[i][j+1]:
            # 열(가로축, j, n)이 오른쪽으로 탐색
            sum += self.quest(i, j+1)
        if i <= len(self.navigation) and self.navigation[i-1][j] and self.pic[i][j] == self.pic[i-1][j]:
            # 행(세로축, i, m)이 위로 탐색
            sum += self.quest(i-1, j)
        return sum


a = 6
b = 4
array = [[1, 1, 1, 0],
        [1, 2, 2, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 3],
        [0, 0, 0, 3]]

Solve.solution(a, b, array)