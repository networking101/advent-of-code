from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

bsize = 21
startpoint = 6
xylen = len(lines)
zwlen = 1

grid = []
for i in range(bsize):
    t1 = []
    for j in range(bsize):
        t2 = []
        for k in range(bsize):
            t3 = []
            for l in range(bsize):
                t3.append('.')
            t2.append(t3)
        t1.append(t2)
    grid.append(t1)

for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[startpoint][startpoint][i+startpoint][j+startpoint] = lines[i][j]

def cn(g, a, z, y, x):
    cnt = 0
    for h in range(a-1, a+2):
        for i in range(z-1, z+2):
            for j in range(y-1, y+2):
                for k in range(x-1, x+2):
                    if i == z and j == y and k == x and h == a:
                        continue
                    
                    if g[h][i][j][k] == "#":
                        cnt += 1

    return cnt



for h in range(6):
    ng = deepcopy(grid)
    for h in range(startpoint-1, startpoint+zwlen+1):
        for i in range(startpoint-1, startpoint+zwlen+1):
            for j in range(startpoint-1, startpoint+xylen+1):
                for k in range(startpoint-1, startpoint+xylen+1):
                    t = cn(grid, h, i, j, k)
                    if grid[h][i][j][k] == '#' and (t > 3 or t < 2):
                        ng[h][i][j][k] = '.'
                    if grid[h][i][j][k] == '.' and t == 3:
                        ng[h][i][j][k] = '#'

    zwlen += 2
    xylen += 2
    startpoint -= 1

    grid = ng

count = 0
for h in grid:
    for i in h:
        for j in i:
            for k in j:
                if k == '#':
                    count += 1

print(count)
