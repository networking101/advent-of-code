from copy import deepcopy

with open("input", "r") as fp:
    grid = [[int(l) for l in line.strip()] for line in fp]

flashes = 0
backupGrid = deepcopy(grid)

count = 0
loopCount = 0
while True:
    loopCount += 1
    queue = []
    for y in range(10):
        for x in range(10):
            grid[y][x] += 1
            if grid[y][x] == 10:
                queue.append([y, x])
                flashes += 1

    while queue:
        y, x = queue.pop(0)

        for i in range(-1, 2):
            for j in range(-1, 2):
                ty = y+i
                tx = x+j
                if ty >= 0 and tx >= 0 and ty <= 9 and tx <= 9:
                    grid[ty][tx] += 1
                    if grid[ty][tx] == 10:
                        queue.append([ty, tx])
                        flashes += 1

    check = True
    for y in range(10):
        for x in range(10):
            if grid[y][x] > 9:
                grid[y][x] = 0
            if grid[y][x] != 0:
                check = False
    
    if check:
        break

    if loopCount == 100:
        print(flashes)

print(loopCount)