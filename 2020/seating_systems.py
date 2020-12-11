from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []

#ans = "silver"
ans = "gold"

if ans == "silver":
    neighbors = 4
if ans == "gold":
    neighbors = 5

for i in range(len(lines)):
    grid.append([])
    for j in range(len(lines[i])):
        grid[i].append(lines[i][j])

def check2(g, i, j, y, x):
    if x - j > 0:
        xx = 1
    elif x - j < 0:
        xx = -1
    else:
        xx = 0
    if y - i > 0:
        yy = 1
    elif y - i < 0:
        yy = -1
    else:
        yy = 0

    while True:
        if y < 0 or y > len(g)-1 or x < 0 or x > len(g[i])-1:
            break
        if g[y][x] == '#':
            return 1
        if g[y][x] == 'L':
            return 0
        y += yy
        x += xx

    return 0

def checkN(g, i, j):
    c = 0
    for y in range(i-1, i+2):
        for x in range(j-1, j+2):
            if y < 0 or y > len(g)-1 or x < 0 or x > len(g[i])-1 or (x == j and y == i):
                continue
            if g[y][x] == '#':
                c += 1
            if ans == "gold":
                if g[y][x] == '.':
                    c += check2(g, i, j, y, x)
    return c

cnt = 0
while True:
    ng = deepcopy(grid)
    change = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                continue
            t = checkN(grid, i, j)
            if grid[i][j] == '#' and t >= neighbors:
                ng[i][j] = 'L'
                change = True
            if grid[i][j] == "L" and t == 0:
                ng[i][j] = '#'
                change = True
    
    grid = ng
    if change == False:
        break

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            count += 1

print(count)
