from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [int(line.strip()) for line in fp]

ol = deepcopy(lines)
size = 25
val = 0

while True:
    curr = lines[:25]
    n = lines[size]
    cond = False
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if curr[i] + curr[j] == n:
                cond = True
                break
        if cond:
            break
    if not cond:
        print("Silver:  " + str(n))
        val = n
        break
    lines.pop(0)

vali = ol.index(val)

for i in range(vali, 0, -1):
    for j in range(i-1, 0, -1):
        if sum(ol[j:i]) == val:
            mn = min(ol[j:i])
            mx = max(ol[j:i])
            print("Gold:  " + str(mn + mx))
            exit(0)
        if sum(ol[j:i]) > val:
            break
