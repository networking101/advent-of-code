from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

gridx = 500
gridy = 200

grid = []
for i in range(gridy):
    grid.append(['.'] * gridx*2)

miny = 0
maxy = 0
minx = gridx
maxx = gridx

def print_grid():
    global miny, maxy, minx, maxx
    for j in range(miny, maxy+1):
        for i in range(minx, maxx+1):
            print(grid[j][i],end='')
        print("")
    print()

for line in lines:
    instructions = line.split(' -> ')
    for i, v in enumerate(instructions):
        # if this is the first point, only update min and max values
        if i == 0:
            x, y = [int(z) for z in instructions[i].split(',')]
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y
        # otherwise, update min and max values and append path to grid
        else:
            ox, oy = [int(z) for z in instructions[i-1].split(',')]
            x, y = [int(z) for z in instructions[i].split(',')]
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y
            for a in range(min(x, ox), max(x, ox)+1):
                for b in range(min(y, oy), max(y, oy)+1):
                    grid[b][a] = '#'

grid_orig = deepcopy(grid)

# Part 1
units = 0
while True:
    x = 500
    y = 0

    while y < maxy:
        # if next space is empty, move down
        if grid[y+1][x] == '.':
            y += 1
            continue

        # if next space blocked
        if grid[y+1][x] != '.':
            # first try diagonal left.  if open check that next
            if grid[y+1][x-1] == '.':
                y += 1
                x -= 1
            # if diagonal left block, check diagonal right.  if open check that next
            elif grid[y+1][x+1] == '.':
                y += 1
                x += 1
            # if both diagonals are blocked, place sand
            else:
                grid[y][x] = 'o'
                units += 1
                break
    if y == maxy:
        #print_grid()
        print(units)
        break

# Part 2
grid = grid_orig
maxy += 2
maxx = 500 + maxy
minx = 500 - maxy
grid[maxy] = ['#'] * gridx*2
units = 0
while True:
    x = 500
    y = 0

    while y < maxy:
        # if next space is empty, move down
        if grid[y+1][x] == '.':
            y += 1
            continue

        # if next space blocked
        if grid[y+1][x] != '.':
            # first try diagonal left.  if open check that next
            if grid[y+1][x-1] == '.':
                y += 1
                x -= 1
            # if diagonal left block, check diagonal right.  if open check that next
            elif grid[y+1][x+1] == '.':
                y += 1
                x += 1
            # if both diagonals are blocked, place sand
            else:
                grid[y][x] = 'o'
                units += 1
                break
    if y == 0:
        #print_grid()
        print(units)
        break