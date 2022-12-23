with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []
size_y = len(lines)
size_x = len(lines[0])
for line in lines:
    grid.append(list(line))

directions = [0, 2, 3, 1]

def expand_grid():
    global size_y
    global size_x

    # check if we have an elf on the border
    border = False
    for j, y in enumerate(grid):
        if grid[j][0] == '#' or grid[j][len(grid[0]) - 1] == '#':
            border = True
    if '#' in grid[0] or '#' in grid[len(grid)-1]:
        border = True

    if not border:
        return

    size_x += 2
    size_y += 2
    for g in grid:
        g.insert(0, '.')
        g.append('.')
    grid.insert(0, ['.'] * (size_x))
    grid.append(['.'] * (size_x))

def check_change(og, ng):
    for oy, ny in zip(og, ng):
        for ox, nx in zip(oy, ny):
            if ox != nx:
                return True
    return False

step = 1
while True:
    # Step 1, propose new positions

    expand_grid()
    # create new grid
    new_grid = []
    for i in range(size_y):
        new_grid.append(['.'] * size_x)

    proposed = {}
    for j, y in enumerate(grid):
        for i, x in enumerate(y):
            if x == '#':
                # if no elves adjacent, dont move
                if grid[j-1][i-1] != '#' and grid[j-1][i] != '#' and grid[j-1][i+1] != '#' and grid[j][i+1] != '#' and grid[j+1][i+1] != '#' and grid[j+1][i] != '#' and grid[j+1][i-1] != '#' and grid[j][i-1] != '#':
                    new_grid[j][i] = '#'
                    continue
                prop = False
                for z in directions:
                    # check north
                    if z == 0:
                        if grid[j-1][i-1] != '#' and grid[j-1][i] != '#' and grid[j-1][i+1] != '#':
                            if (j-1, i) in proposed:
                                proposed[(j-1, i)].append((j, i))
                            else:
                                proposed[(j-1, i)] = [(j, i)]
                            prop = True
                            break
                    # check south
                    if z == 2:
                        if grid[j+1][i-1] != '#' and grid[j+1][i] != '#' and grid[j+1][i+1] != '#':
                            if (j+1, i) in proposed:
                                proposed[(j+1, i)].append((j, i))
                            else:
                                proposed[(j+1, i)] = [(j, i)]
                            prop = True
                            break
                    # check west
                    if z == 3:
                        if grid[j-1][i-1] != '#' and grid[j][i-1] != '#' and grid[j+1][i-1] != '#':
                            if (j, i-1) in proposed:
                                proposed[(j, i-1)].append((j, i))
                            else:
                                proposed[(j, i-1)] = [(j, i)]
                            prop = True
                            break
                    # check east
                    if z == 1:
                        if grid[j-1][i+1] != '#' and grid[j][i+1] != '#' and grid[j+1][i+1] != '#':
                            if (j, i+1) in proposed:
                                proposed[(j, i+1)].append((j, i))
                            else:
                                proposed[(j, i+1)] = [(j, i)]
                            prop = True
                            break

                # if there are no proposed positions available, elf does not move
                if not prop:
                    new_grid[j][i] = '#'

    # rotate through direction order
    directions.append(directions.pop(0))

    # Step 2, Move to new positions
    for k, v in proposed.items():
        if len(v) == 1:
            new_grid[k[0]][k[1]] = '#'
        else:
            for j, i in v:
                new_grid[j][i] = '#'

    # if the grid did not change, we are done
    if not check_change(grid, new_grid):
        print(step)
        break

    grid = new_grid

    if step == 10:
        minx = size_x
        miny = size_y
        maxx = 0
        maxy = 0
        for j, y in enumerate(grid):
            for i, x in enumerate(grid):
                if grid[j][i] == '#':
                    if j < miny:
                        miny = j
                    if j > maxy:
                        maxy = j
                    if i < minx:
                        minx = i
                    if i > maxx:
                        maxx = i
        tot = 0
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                if grid[y][x] == '.':
                    tot += 1
        print(tot)

    step += 1