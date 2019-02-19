ls1 = ['A', 'B', 'C', 'D', 'E']

class Game():
    def __init__(self):
        self.num = 0
        self.man = []

    def solution(self, num, man):
        for i in range(1, num+1):
            print(man[0], self.check(i))
            man.append(man.pop(0))

    def check(self, num):
        if str(num)[-1] == '3' or str(num)[-1] == '6' or str(num)[-1] == '9':
            return "clap"
        else:
            return num

GG = Game()
gg1 = Game()

print(GG.solution(100, ls1))