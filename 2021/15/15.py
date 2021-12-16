from copy import deepcopy

with open("input", "r") as fp:
    grid = [[int(x) for x in line.strip()] for line in fp]

backup_grid = deepcopy(grid)
maxVal = 999999999

ysize = len(grid) - 1
xsize = len(grid[0])-1

distances = []
for j in range(len(grid)):
    d = []
    for i in range(len(grid[j])):
        d.append(maxVal)
    distances.append(d)

distances[ysize][xsize] = grid[ysize][xsize]

for j in range(ysize, -1, -1):
    for i in range(xsize, -1, -1):
        if i == xsize and j == ysize:
            continue

        if j+1 > ysize:
            down = maxVal
        else:
            down = distances[j+1][i]

        if i+1 > xsize:
            right = maxVal
        else:
            right = distances[j][i+1]

        if j-1 < 0:
            up = maxVal
        else:
            up = distances[j-1][i]

        if i-1 < 0:
            left = maxVal
        else:
            left = distances[j][i-1]

        distances[j][i] = grid[j][i] + min(up, down, left, right)

print(min(distances[0][1], distances[1][0]))

ysize2 = len(grid)*5 - 1
xsize2 = len(grid[0])*5 - 1

# make grid2
grid2 = []
for j in range(ysize2 + 1):
    grid2.append([0] * (xsize2 + 1))

# fill in old grid values to grid2
for j in range(len(backup_grid)):
    for i in range(len(backup_grid[j])):
        grid2[j][i] =  backup_grid[j][i]

# expand grid2 in the y direction
for j in range(ysize + 1, ysize2 + 1):
    for i in range(xsize + 1):
        tmp = grid2[j - (ysize+1)][i] + 1
        if tmp > 9:
            tmp = 1
        grid2[j][i] = tmp

# expand the rest of grid2 in the x direction
for j in range(ysize2 + 1):
    for i in range(xsize + 1, xsize2 + 1):
        tmp = grid2[j][i - (xsize + 1)] + 1
        if tmp > 9:
            tmp = 1
        grid2[j][i] = tmp

distances2 = []
for j in range(len(grid2)):
    d = []
    for i in range(len(grid2[j])):
        d.append(maxVal)
    distances2.append(d)

distances2[ysize2][xsize2] = grid2[ysize2][xsize2]
maxVal = 999999999

for j in range(ysize2, -1, -1):
    for i in range(xsize2, -1, -1):
        if i == xsize2 and j == ysize2:
            continue

        if j+1 > ysize2:
            down = maxVal
        else:
            down = distances2[j+1][i]

        if i+1 > xsize2:
            right = maxVal
        else:
            right = distances2[j][i+1]

        if j-1 < 0:
            up = maxVal
        else:
            up = distances2[j-1][i]

        if i-1 < 0:
            left = maxVal
        else:
            left = distances2[j][i-1]

        distances2[j][i] = grid2[j][i] + min(up, down, left, right)

print(min(distances2[0][1], distances2[1][0]))