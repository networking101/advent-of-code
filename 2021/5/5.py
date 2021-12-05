from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []
for i in range(1000):
    grid.append([0] * 1000)

backup_grid = deepcopy(grid)

# Silver
for line in lines:
    l, r = line.split(" -> ")
    l = [int(z) for z in l.split(",")]
    r = [int(z) for z in r.split(",")]

    if l[0] == r[0] or l[1] == r[1]:
        temp = list(range(min(l[0], r[0]), max(l[0],r[0])+1))
        for x in range(min(l[0], r[0]), max(l[0],r[0])+1):
            for y in range(min(l[1], r[1]), max(l[1],r[1])+1):
                grid[y][x] += 1

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] >= 2:
            total += 1

print(total)

grid = backup_grid

# Gold
for line in lines:
    l, r = line.split(" -> ")
    l = [int(z) for z in l.split(",")]
    r = [int(z) for z in r.split(",")]

    if l[0] == r[0] or l[1] == r[1]:
        for x in range(min(l[0], r[0]), max(l[0],r[0])+1):
            for y in range(min(l[1], r[1]), max(l[1],r[1])+1):
                grid[y][x] += 1

    if abs(l[0] - r[0]) == abs(l[1] - r[1]):
        if (l[0] < r[0] and l[1] < r[1]) or (l[0] > r[0] and l[1] > r[1]):
            tmp = min(l[1], r[1])
            for x in range(min(l[0], r[0]), max(l[0],r[0])+1):
                grid[tmp][x] += 1
                tmp += 1
        else:
            tmp = max(l[1], r[1])
            for x in range(min(l[0], r[0]), max(l[0],r[0])+1):
                grid[tmp][x] += 1
                tmp -= 1
            

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] >= 2:
            total += 1

print(total)