from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

floor_size = 500

grid = []

for i in range(floor_size):
    grid.append([])
    for j in range(int(floor_size)):
        if i%2 == 0:
            grid[i].append(0)
            grid[i].append(" ")
        if i%2 == 1:
            grid[i].append(" ")
            grid[i].append(0)

for line in lines:
    
    x = int(floor_size/2)
    y = int(floor_size/2)

    i = 0
    while i < len(line):
        t = ""
        if line[i] == "n" or line[i] == "s":
            t = line[i:i+2]
            i += 1
        else:
            t = line[i]

        if t == "e":
            x -= 2
        if t == "w":
            x += 2
        if t == "ne":
            x -= 1
            y -= 1
        if t == "nw":
            x += 1
            y -= 1
        if t == "se":
            x -= 1
            y += 1
        if t == "sw":
            x += 1
            y += 1
        
        i += 1
    assert grid[y][x] != " "

    grid[y][x] = (grid[y][x]+1)%2

cnt = 0
for i in grid:
    for j in i:
        if j == 1:
            cnt += 1


print("Silver:  " + str(cnt))

def count_adjacent(g, y, x):
    cnt = 0

    if x-2 >= 0 and g[y][x-2] == 1:
        cnt += 1
    if x+2 <= floor_size-1 and g[y][x+2] == 1:
        cnt += 1
    if x-1 >=0 and y-1 >= 0 and g[y-1][x-1] == 1:
        cnt += 1
    if x+1 <= floor_size-1 and y+1 <= floor_size-1 and g[y+1][x+1] == 1:
        cnt += 1
    if x-1 >= 0 and y+1 <= floor_size-1 and g[y+1][x-1] == 1:
        cnt += 1
    if x+1 <= floor_size-1 and y-1 >= 0 and g[y-1][x+1] == 1:
        cnt += 1

    return cnt


for k in range(100):
    ng = deepcopy(grid)
    for i in range(floor_size):
        for j in range(floor_size+1):

            if grid[i][j] == " ":
                continue

            t = count_adjacent(grid, i, j)

            if grid[i][j] == 0 and t == 2:
                ng[i][j] = 1
            if grid[i][j] == 1 and t != 1 and t != 2:
                ng[i][j] = 0

    grid = ng

cnt = 0
for i in grid:
    for j in i:
        if j == 1:
            cnt += 1

print("Gold:  " + str(cnt))