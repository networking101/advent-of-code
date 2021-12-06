from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

lines = lines[0].split(",")

backupLines = deepcopy(lines)

# Silver

for i in range(80):
    temp = []
    zeros = 0
    for x in range(len(lines)):
        if lines[x] == "0":
            temp.append("6")
            zeros += 1
        else:
            temp.append(str(int(lines[x]) - 1))
    for i in range(zeros):
        temp.append("8")
    lines = temp

print(len(lines))

lines = backupLines

# Gold
hashTable = [-1] * 260

def getFish(days):
    global hashTable
    if hashTable[days] != -1:
        return hashTable[days]
    d = days - 8
    curr = 1
    while d > 0:
        curr += getFish(d-1)
        d -= 7

    hashTable[days] = curr
    return curr


data = []
count = len(lines)

days = 256

for i in lines:
    d = days - int(i)
    while d > 0:
        count += getFish(d-1)
        d -= 7


print(count)