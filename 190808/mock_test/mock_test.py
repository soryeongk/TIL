def supoja01(answers):
    corrects = 0
    my_ans = [1,2,3,4,5]
    for a, m in zip(answers, my_ans):
        if a == m:
            corrects += 1
        else:
            continue
    return corrects

def supoja02(answers):
    corrects = 0
    my_ans = [2,1,2,3,2]
    for a, m in zip(answers, my_ans):
        if a == m:
            corrects += 1
        else:
            continue

def supoja03(answers):
    corrects = 0
    my_ans = [3,3,1,1,2]
    for a, m in zip(answers, my_ans):
        if a == m:
            corrects += 1
        else:
            continue

def solution(answers):
    honors = []
