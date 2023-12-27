from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid1 = [[z for z in line] for line in lines]
grid2 = deepcopy(grid1)
xrange = range(len(grid1[0]))
yrange = range(len(grid1))

junctions1 = []
junctions2 = []
distances1 = {}
distances2 = {}

for j, y in enumerate(grid1):
    for i, x in enumerate(y):
        if j == 0 and x == '.':
            start = (j, i)
            junctions1.append(start)
            junctions2.append(start)
        if j == len(grid1)-1 and x == '.':
            end = (j, i)
            junctions1.append(end)
            junctions2.append(end)
        if x == 'v' or x == '^' or x == '<' or x == '>':
            grid2[j][i] = '.'

# part 1
for j, y in enumerate(grid1):
    for i, x in enumerate(y):
        if grid1[j][i] == '.':
            # find intersections
            open_edged = 0
            for z, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
                jj = j + coord[0]
                ii = i + coord[1]
                if jj in yrange and ii in xrange and grid1[jj][ii] != '#':
                    open_edged += 1
            if open_edged > 2:
                junctions1.append((j, i))
junctions2 = deepcopy(junctions1)

# part 1
oggrid = deepcopy(grid1)
# find distances to each junction
for junction in junctions1:
    grid = deepcopy(oggrid)
    y, x = junction
    queue = [((y, x), 0)]
    while queue:
        c, s = queue.pop(0)
        j, i = c
        s += 1
        grid[j][i] = '#'
        for z, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            jj = j + coord[0]
            ii = i + coord[1]
            if jj not in yrange or ii not in xrange or grid[jj][ii] == '#':
                continue
            if (z == 0 and grid[jj][ii] == 'v') or (z == 1 and grid[jj][ii] == '<') or (z == 2 and grid[jj][ii] == '^') or (z == 3 and grid[jj][ii] == '>'):
                continue
            if (jj, ii) in junctions1 and (jj, ii) != (y, x):
                if (y, x) not in distances1:
                    distances1[(y, x)] = [((jj, ii), s)]
                else:
                    distances1[(y, x)].append(((jj, ii), s))
            else:
                queue.append(((jj, ii), s))

# part 2
oggrid = deepcopy(grid2)
# find distances to each junction
for junction in junctions2:
    grid = deepcopy(oggrid)
    y, x = junction
    queue = [((y, x), 0)]
    while queue:
        c, s = queue.pop(0)
        j, i = c
        s += 1
        grid[j][i] = '#'
        for z, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            jj = j + coord[0]
            ii = i + coord[1]
            if jj not in yrange or ii not in xrange or grid[jj][ii] == '#':
                continue
            if (jj, ii) in junctions2 and (jj, ii) != (y, x):
                if (y, x) not in distances2:
                    distances2[(y, x)] = [((jj, ii), s)]
                else:
                    distances2[(y, x)].append(((jj, ii), s))
            else:
                queue.append(((jj, ii), s))

# part 1        
def recursive1(curr, visited):
    visited.append(curr)
    if curr == end:
        return 0
    max_distance = [-999999]
    for next_junction, steps in distances1[curr]:
        if next_junction not in visited:
            max_distance.append(recursive1(next_junction, deepcopy(visited)) + steps)

    return max(max_distance)

print(recursive1(start, []))

# part 2        
def recursive2(curr, visited):
    visited.append(curr)
    if curr == end:
        return 0
    max_distance = [-999999]
    for next_junction, steps in distances2[curr]:
        if next_junction not in visited:
            max_distance.append(recursive2(next_junction, deepcopy(visited)) + steps)

    return max(max_distance)

print(recursive2(start, []))