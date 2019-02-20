# 학생 3명있다.(1,2,3) 이들은 시험을 포기해서 규칙적으로 문제를 찍기로했다.
# 답안지는 answers를 통해서 list형식 주어진다.
# 학생 들중에 제일 많이 맞춘 사람을 출력하시오. 점수가 같다면 같은 학생 번호르 표시하라.

def solution(answer):
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    match = {1:0, 2:0, 3:0}
    for idx, student in enumerate(students):
        for i in range(len(answer)):
            if student[i % len(student)] == answer[i]:
                match[idx + 1] += 1
    maxx = max(list(match.values()))
    result = [a[0] for a in match.items() if a[1] == maxx]
    return result

def solution2(answers):
    students = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    check = {'1':{'idx':1, 'correct':0},'2':{'idx':2, 'correct':0},'3':{'idx':3, 'correct':0}}
    for idx, student in enumerate(students):
        for a_idx, answer in enumerate(answers):
            if student[a_idx%len(student)] == answer:
                check[str(idx+1)]['correct'] += 1

    scores = list(check.values())
    max_correct = max(tuple((score['correct'] for score in scores)))

    return [score['idx'] for score in scores if score['correct'] >= max_correct]

def solution3(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, check in enumerate(answers):
        if check == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if check == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if check == pattern3[idx%len(pattern3)]:
            score[2] += 1

    count = 1
    for i in score:
        if i >= max(score):
            result.append(count)
        count += 1

    return result




ans1 = [1, 2, 3, 4, 5]
ans2 = [1, 3, 2, 4, 2]
print(solution3(ans1))
print(solution3(ans2))