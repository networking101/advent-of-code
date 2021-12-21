from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

iea = lines.pop(0)
lines.pop(0)

space = '.'

def expand(grid):
    global space
    newGrid = []
    ysize = len(grid)
    xsize = len(grid[0])
    newGrid.append([space] * (xsize + 2))
    for j in range(ysize):
        tmp = [space]
        tmp += grid[j]
        tmp += [space]
        newGrid.append(tmp)
    newGrid.append([space] * (xsize + 2))
    return newGrid

def printGrid(grid):
    for a in grid:
        for b in a:
            print(b, end="")
        print("")
    print("")

grid = []
for line in lines:
    grid.append(list(line))

round = 0
grid = expand(grid)
while round < 50:
    grid = expand(grid)
    grid = expand(grid)
    
    newGrid = deepcopy(grid)

    for j in range(1, len(grid)-1):
        for i in range(1, len(grid[j])-1):
            binNumber = ""
            for y in range(j-1, j+2):
                for x in range(i-1, i+2):
                    if grid[y][x] == ".":
                        binNumber += "0"
                    else:
                        binNumber += "1"

            binNumber = int(binNumber, 2)
            newGrid[j][i] = iea[binNumber]

    grid = newGrid
    if grid[1][1] == '#':
        space = '#'
    else:
        space = '.'
    grid[0] = [space] * len(grid[0])
    grid[len(grid)-1] = [space] * len(grid[0])
    for z in grid:
        z[0] = space
        z[len(grid[0])-1] = space

    round += 1

    if round == 2:
        count = 0
        for j in grid:
            for i in j:
                if i == '#':
                    count += 1
        print(count)

count = 0
for j in grid:
    for i in j:
        if i == '#':
            count += 1

print(count)