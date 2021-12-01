from copy import deepcopy

with open("input", "r") as fp:
    lines = [int(line.strip()) for line in fp]

backup = deepcopy(lines)

res = 0

# Silver
index = lines.pop(0)
for line in lines:
    if line > index:
        res += 1
    index = line

print(res)

# Gold
lines = backup

res = 0
index = sum(lines[:3])
temp = index
for i in range(3, len(lines)):
    temp += lines[i]
    temp -= lines[i-3]
    if temp > index:
        res += 1
    index = temp

print(res)