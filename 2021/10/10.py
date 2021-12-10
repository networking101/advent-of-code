from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

a1 = ['(', ')']
b1 = ['[', ']']
c1 = ['{', '}']
d1 = ['<', '>']

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

opposite = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

pushes = ['(', '[', '{', '<']
pops = [')', ']', '}', '>']

score = 0
score2 = []

for line in lines:
    badline = False
    stack = []
    for i in line:
        good = True
        if i in pushes:
            stack.append(i)
        if i in pops:
            tmp1 = i
            tmp2 = stack.pop()
            if tmp1 in a1 and tmp2 in a1 or tmp1 in b1 and tmp2 in b1 or tmp1 in c1 and tmp2 in c1 or tmp1 in d1 and tmp2 in d1:
                tmp = "good"
            else:
                good = False
                score += points[tmp1]
                badline = True
                break
    if badline:
        continue

    tmpscore = 0
    while stack:
        tmp3 = stack.pop()
        tmpscore *= 5
        tmpscore += points2[opposite[tmp3]]

    score2.append(tmpscore)

newscore2 = sorted(score2)
finalscore2 = newscore2[int(len(score2)/2)]

print(score)

print(finalscore2)