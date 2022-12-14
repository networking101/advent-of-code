import json

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

left = []
right = []
for line in lines:
    if not line:
        continue
    if len(left) == len(right):
        left.append(json.loads(line))
    else:
        right.append(json.loads(line))

def recursion(l, r):
    for i in range(min(len(l), len(r))):
        if isinstance(l[i], int) and isinstance(r[i], int):
            if l[i] < r[i]:
                return 1
            elif l[i] > r[i]:
                return -1
            else:
                continue
        if isinstance(l[i], list) and isinstance(r[i], int):
            res = recursion(l[i], [r[i]])
            if res != 0:
                return res
            continue
        if isinstance(l[i], int) and isinstance(r[i], list):
            res = recursion([l[i]], r[i])
            if res != 0:
                return res
            continue
        if isinstance(l[i], list) and isinstance(r[i], list):
            res = recursion(l[i], r[i])
            if res != 0:
                return res
            continue
    
    if len(l) < len(r):
        return 1
    if len(l) > len(r):
        return -1
    return 0


correct = 0
for i in range(len(right)):
    if recursion(left[i], right[i]) == 1:
        correct += i+1

print(correct)

# Part2

all_lines = []
i = 0
for line in lines:
    if not line:
        continue
    curr = json.loads(line)
    if not all_lines:
        all_lines.append(curr)
        continue
    test = True
    for j in range(len(all_lines)):
        if recursion(curr, all_lines[j]) == 1:
            all_lines.insert(j, curr)
            test = False
            break
    if test :
        all_lines.insert(j+1, curr)

curr = [[2]]
test = True
for j in range(len(all_lines)):
    if recursion(curr, all_lines[j]) == 1:
        all_lines.insert(j, curr)
        test = False
        break
if test :
    all_lines.insert(j+1, curr)

curr = [[6]]
test = True
for j in range(len(all_lines)):
    if recursion(curr, all_lines[j]) == 1:
        all_lines.insert(j, curr)
        test = False
        break
if test :
    all_lines.insert(j+1, curr)

first = 0
for l in range(len(all_lines)):
    if str(all_lines[l]) == str([[2]]):
        first = l+1
    if str(all_lines[l]) == str([[6]]):
        print(first * (l+1))
        break