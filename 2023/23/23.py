from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[z for z in line] for line in lines]
xrange = range(len(grid[0]))
yrange = range(len(grid))

for i, x in enumerate(grid[0]):
    if x == '.':
        start = (0, i)
for i, x in enumerate(grid[-1]):
    if x == '.':
        end = (len(grid) - 1, i)

def print_grid(curr, g):
    for j, y in enumerate(g):
        for i, x in enumerate(y):
            if (j, i) == curr:
                print('*', end='')
            else:
                print(x, end='')
        print()
    print()

DP = {}
def skip_to_fork(g, c, d):
    step = 1
    y, x = c

    if c in DP:
        coord, saved_step, last_dir = DP[c]
        y, x = coord
        if g[y][x] == '#' or g[y][x] == '*' or saved_step is None:
            return (coord, None)
        if last_dir == 2:
            g[y-1][x] = '*'
        if last_dir == 3:
            g[y][x+1] = '*'
        if last_dir == 0:
            g[y+1][x] = '*'
        if last_dir == 1:
            g[y][x-1] = '*'
        return (coord, saved_step)
    
    while True:
        g[y][x] = '*'
        directions = []
        last_wall = 0
        for i, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            yy = y + coord[0]
            xx = x + coord[1]
            if yy in yrange and xx in xrange and g[yy][xx] != '#' and g[yy][xx] != '*':
                directions.append((yy, xx))
                ld = i
            if yy in yrange and xx in xrange and g[yy][xx] == '#':
                last_wall += 1
        if (y, x) == end:
            return ((y, x), step)
        elif len(directions) > 1:
            DP[c] = ((y, x), step, last_dir)
            print(len(DP))
            return ((y, x), step)
        elif len(directions) == 0:
            if last_wall == 3:
                DP[c] = ((y, x), None, last_dir)
            return ((y, x), None)
        else:
            step += 1
            y, x = directions[0]
            last_dir = ld

def recursive(g, curr, part2, dir):
    y, x = curr
    g[y][x] = '*'

    curr, s = skip_to_fork(g, curr, dir)

    if s is None:
        return -999999
    y, x = curr
    g[y][x] = '*'

    # print_grid(curr, g)

    if curr == end:
        return s
    
    steps = [-999999]
    for i, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
        yy = y + coord[0]
        xx = x + coord[1]
        if yy in yrange and xx in xrange and g[yy][xx] != '#' and g[yy][xx] != '*':
            if part2:
                steps.append(recursive(deepcopy(g), (yy, xx), part2, i))
            else:
                if not (coord[0] == -1 and g[yy][xx] == 'v') and  \
                not (coord[0] == 1 and g[yy][xx] == '^') and \
                not (coord[1] == -1 and g[yy][xx] == '>') and \
                not (coord[1] == 1 and g[yy][xx] == '<'):
                    steps.append(recursive(deepcopy(g), (yy, xx), part2, i))

    return max(steps) + s

print(recursive(deepcopy(grid), start, 0, 2) - 1)
DP = {}
print(recursive(deepcopy(grid), start, 1, 2) - 1)
