import math
import sys

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []
lp = []

for line in lines:
    grid.append([int(x) for x in line])

def check(y, x):
    global grid
    tot = 4

    if y-1 < 0:
        tot -= 1
    elif grid[y][x] < grid[y-1][x]:
        tot -= 1
    if y+1 > len(grid) - 1:
        tot -= 1
    elif grid[y][x] < grid[y+1][x]:
        tot -= 1
    if x-1 < 0:
        tot -= 1
    elif grid[y][x] < grid[y][x-1]:
        tot -= 1
    if x+1 > len(grid[0]) - 1:
        tot -= 1
    elif grid[y][x] < grid[y][x+1]:
        tot -= 1
    
    if tot == 0:
        return True
    return False

def checkBasin(y, x):
    global grid

    tmpCnt = 0

    tx = x
    ty = y-1
    if not (ty < 0 or ty > len(grid) -1 or tx < 0 or tx >len(grid[0]) -1):
        if grid[ty][tx] < 9 and grid[ty][tx] > grid[y][x]:
            tmpCnt += checkBasin(ty, tx)
            grid[ty][tx] = 9

    tx = x
    ty = y+1
    if not (ty < 0 or ty > len(grid) -1 or tx < 0 or tx >len(grid[0]) -1):
        if grid[ty][tx] < 9 and grid[ty][tx] > grid[y][x]:
            tmpCnt += checkBasin(ty, tx)
            grid[ty][tx] = 9

    tx = x-1
    ty = y
    if not (ty < 0 or ty > len(grid) -1 or tx < 0 or tx >len(grid[0]) -1):
        if grid[ty][tx] < 9 and grid[ty][tx] > grid[y][x]:
            tmpCnt += checkBasin(ty, tx)
            grid[ty][tx] = 9

    tx = x+1
    ty = y
    if not (ty < 0 or ty > len(grid) -1 or tx < 0 or tx >len(grid[0]) -1):
        if grid[ty][tx] < 9 and grid[ty][tx] > grid[y][x]:
            tmpCnt += checkBasin(ty, tx)
            grid[ty][tx] = 9

    tmpCnt += 1

    return tmpCnt


# Silver
total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if check(y, x):
            lp.append([y, x])
            total += grid[y][x] + 1

print(total)


# Gold

total = []
for i in lp:
    y, x = i
    tmp = checkBasin(y, x)
    if len(total) < 3:
        total.append(tmp)
    else:
        for i in range(len(total)):
            if tmp > total[i]:
                total.insert(i, tmp)
                tmp = total.pop(i+1)

print(math.prod(total))