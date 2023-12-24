from copy import deepcopy

with open("input2", "r") as fp:
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

def skip_to_fork(g, c):
    step = 1
    y, x = c
    while True:
        g[y][x] = '#'
        directions = []
        for i, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            yy = y + coord[0]
            xx = x + coord[1]
            if yy in yrange and xx in xrange and g[yy][xx] != '#':
                directions.append((yy, xx))
        if len(directions) == 0:
            if (y, x) == end:
                return ((y, x), step)
            return ((y, x), None)
        elif len(directions) > 1:
            return ((y, x), step)
        else:
            step += 1
            y, x = directions[0]

DP = {}
def recursive(g, curr, part2, dir):
    y, x = curr
    g[y][x] = '#'

    curr, s = skip_to_fork(g, curr)

    if s is None:
        return -999999
    y, x = curr

    if curr == end:
        return s
    if (curr, dir) in DP:
        return DP[(curr, dir)] + s
    
    steps = []
    for i, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
        yy = y + coord[0]
        xx = x + coord[1]
        if yy in yrange and xx in xrange and g[yy][xx] != '#':
            if part2:
                steps.append(recursive(deepcopy(g), (yy, xx), part2, dir))
            else:
                if not (coord[0] == -1 and g[yy][xx] == 'v') and  \
                not (coord[0] == 1 and g[yy][xx] == '^') and \
                not (coord[1] == -1 and g[yy][xx] == '>') and \
                not (coord[1] == 1 and g[yy][xx] == '<'):
                    steps.append(recursive(deepcopy(g), (yy, xx), part2, dir))

    if max(steps) > 0:
        DP[(curr, dir)] = max(steps)
        # print(DP)
    return max(steps) + s

print(recursive(deepcopy(grid), start, 0, 2) - 1)
DP = {}
print(recursive(deepcopy(grid), start, 1, 2) - 1)
