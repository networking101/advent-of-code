from copy import deepcopy
from heapq import *

with open("input", "r") as fp:
    grid = [[int(x) for x in line.strip()] for line in fp]

backup_grid = deepcopy(grid)
maxVal = 999999999

ysize = len(grid)
xsize = len(grid[0])

distances = []
for j in range(len(grid)):
    d = []
    for i in range(len(grid[j])):
        d.append(maxVal)
    distances.append(d)

h = []
heappush(h, (0, 0, 0))

def checkDistance(d, y, x):
    global grid
    global distances
    global h
    global ysize
    global xsize
    if y >= ysize or y < 0  or x >= xsize or x < 0:
        return

    newdist = d + grid[y][x]
    if newdist < distances[y][x]:
        distances[y][x] = newdist
        heappush(h, (newdist, y, x))

while h:
    dist, y, x = heappop(h)

    checkDistance(dist, y+1, x)
    checkDistance(dist, y-1, x)
    checkDistance(dist, y, x+1)
    checkDistance(dist, y, x-1)


print(distances[ysize-1][xsize-1])


# Gold
ysize2 = len(grid)*5
xsize2 = len(grid[0])*5

# make grid2
grid2 = []
for j in range(ysize2):
    grid2.append([0] * (xsize2))

# fill in old grid values to grid2
for j in range(len(backup_grid)):
    for i in range(len(backup_grid[j])):
        grid2[j][i] =  backup_grid[j][i]

# expand grid2 in the y direction
for j in range(ysize, ysize2):
    for i in range(xsize):
        tmp = grid2[j - (ysize)][i] + 1
        if tmp > 9:
            tmp = 1
        grid2[j][i] = tmp

# expand the rest of grid2 in the x direction
for j in range(ysize2):
    for i in range(xsize, xsize2):
        tmp = grid2[j][i - (xsize)] + 1
        if tmp > 9:
            tmp = 1
        grid2[j][i] = tmp

distances2 = []
for j in range(len(grid2)):
    d = []
    for i in range(len(grid2[j])):
        d.append(maxVal)
    distances2.append(d)

h2 = []
heappush(h2, (0, 0, 0))

def checkDistance2(d, y, x):
    global grid2
    global distances2
    global h2
    global ysize2
    global xsize2
    if y >= ysize2 or y < 0  or x >= xsize2 or x < 0:
        return

    newdist = d + grid2[y][x]
    if newdist < distances2[y][x]:
        distances2[y][x] = newdist
        heappush(h2, (newdist, y, x))

while h2:
    dist, y, x = heappop(h2)

    checkDistance2(dist, y+1, x)
    checkDistance2(dist, y-1, x)
    checkDistance2(dist, y, x+1)
    checkDistance2(dist, y, x-1)


print(distances2[ysize2-1][xsize2-1])