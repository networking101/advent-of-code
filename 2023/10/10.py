from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[x for x in line] for line in lines]
grid2 = deepcopy(grid)

ysize = len(lines) - 1
xsize = len(lines[0]) - 1

def print_grid():
    for y in grid:
        for x in y:
            print(x, end='')
        print()
    print()

start = []
for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x == 'S':
            start = [j, i]

def get_direction(y, x, c):
    res_list = []
    # check up
    if y-1 >= 0 and grid[y-1][x] != 'L' and grid[y-1][x] != 'J' and grid[y-1][x] != '-' and grid[y-1][x] != '.':
        res_list.append([y-1, x, c+1])
    # check right
    if x+1 <= xsize and grid[y][x+1] != 'L' and grid[y][x+1] != 'F' and grid[y][x+1] != '|' and grid[y][x+1] != '.':
        res_list.append([y, x+1, c+1])
    # check down
    if y+1 <= ysize and grid[y+1][x] != 'F' and grid[y+1][x] != '7' and grid[y+1][x] != '-' and grid[y+1][x] != '.':
        res_list.append([y+1, x, c+1])
    # check left
    if x-1 >= 0 and grid[y][x-1] != '7' and grid[y][x-1] != 'J' and grid[y][x-1] != '|' and grid[y][x-1] != '.' :
        res_list.append([y, x-1, c+1])

    return res_list

y, x = start
grid[y][x] = '.'
queue = get_direction(y, x, 0)

while queue:
    grid[y][x] = '.'
    y, x, c = queue.pop(0)
    queue += get_direction(y, x, c)
print(c)


grid = deepcopy(grid2)
grid.insert(0, ['.']*(xsize+1))
grid.append(['.']*(xsize+1))
for y in grid:
    y.insert(0, '.')
    y.append('.')

start = []
for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x == 'S':
            start = [j, i]

right_list = []
left_list = []
tube = [start]

def check_neighbors(dir, y, x):
    if dir == 0:
        if grid[y][x] == '|':
            right_list.append([y, x+1])
            left_list.append([y, x-1])
        if grid[y][x] == 'F':
            left_list.append([y-1, x])
            left_list.append([y, x-1])
        if grid[y][x] == '7':
            right_list.append([y, x+1])
            right_list.append([y-1, x])
    if dir == 1:
        if grid[y][x] == '-':
            right_list.append([y+1, x])
            left_list.append([y-1, x])
        if grid[y][x] == '7':
            left_list.append([y, x+1])
            left_list.append([y-1, x])
        if grid[y][x] == 'J':
            right_list.append([y, x+1])
            right_list.append([y+1, x])
    if dir == 2:
        if grid[y][x] == '|':
            right_list.append([y, x-1])
            left_list.append([y, x+1])
        if grid[y][x] == 'J':
            left_list.append([y, x+1])
            left_list.append([y+1, x])
        if grid[y][x] == 'L':
            right_list.append([y+1, x])
            right_list.append([y, x-1])
    if dir == 3:
        if grid[y][x] == '-':
            right_list.append([y-1, x])
            left_list.append([y+1, x])
        if grid[y][x] == 'L':
            left_list.append([y+1, x])
            left_list.append([y, x-1])
        if grid[y][x] == 'F':
            right_list.append([y, x+1])
            right_list.append([y-1, x])
    return

def next_pipe(dir, y, x):

    if dir == 0:
        assert grid[y-1][x] == '|' or grid[y-1][x] == 'F' or grid[y-1][x] == '7' or grid[y-1][x] == 'S'
        if grid[y-1][x] == 'S':
            return([y-1, x], 0)
        if grid[y-1][x] == '|':
            return([y-1, x], 0)
        if grid[y-1][x] == 'F':
            return([y-1, x], 1)
        if grid[y-1][x] == '7':
            return([y-1, x], 3)
    if dir == 1:
        assert grid[y][x+1] == '-' or grid[y][x+1] == 'J' or grid[y][x+1] == '7' or grid[y][x+1] == 'S'
        if grid[y][x+1] == 'S':
            return([y, x+1], 1)
        if grid[y][x+1] == '-':
            return([y, x+1], 1)
        if grid[y][x+1] == 'J':
            return([y, x+1], 0)
        if grid[y][x+1] == '7':
            return([y, x+1], 2)
    if dir == 2:
        assert grid[y+1][x] == '|' or grid[y+1][x] == 'L' or grid[y+1][x] == 'J' or grid[y+1][x] == 'S'
        if grid[y+1][x] == 'S':
            return([y+1, x], 2)
        if grid[y+1][x] == '|':
            return([y+1, x], 2)
        if grid[y+1][x] == 'L':
            return([y+1, x], 1)
        if grid[y+1][x] == 'J':
            return([y+1, x], 3)
    if dir == 3:
        assert grid[y][x-1] == '-' or grid[y][x-1] == 'L' or grid[y][x-1] == 'F' or grid[y][x-1] == 'S'
        if grid[y][x-1] == 'S':
            return([y, x-1], 3)
        if grid[y][x-1] == '-':
            return([y, x-1], 3)
        if grid[y][x-1] == 'L':
            return([y, x-1], 0)
        if grid[y][x-1] == 'F':
            return([y, x-1], 2)

pos = []
dir = -1
y, x = start
up = grid[y-1][x]
if up == '|' or up == 'F' or up == '7':
    pos = [y-1, x]
    if up == '|':
        dir = 0
    if up == 'F':
        dir = 1
    if up == '7':
        dir = 3
    check_neighbors(0, y-1, x)
rt = grid[y][x+1]
if not pos and (rt == '-' or rt == 'J' or rt == '7'):
    pos = [y, x+1]
    if rt == '-':
        dir = 1
    if rt == 'J':
        dir = 0
    if rt == '7':
        dir = 2
    check_neighbors(1, y, x+1)
dn = grid[y+1][x]
if not pos and (dn == '|' or dn == 'J' or dn == 'L'):
    pos = [y+1, x]
    if dn == '|':
        dir = 2
    if dn == 'J':
        dir = 3
    if dn == 'L':
        dir = 1
    check_neighbors(2, y+1, x)
lt = grid[y][x-1]
if not pos and (lt == '-' or lt == 'F' or lt == 'L'):
    pos = [y, x-1]
    if lt == '-':
        dir = 3
    if lt == 'F':
        dir = 2
    if lt == 'L':
        dir = 0
    check_neighbors(3, y, x-1)

while pos != start:
    y, x = pos
    tube.append(pos)
    pos, new_dir = next_pipe(dir, y, x)
    check_neighbors(dir, pos[0], pos[1])
    dir = new_dir

def bfs(y, x):
    grid[y][x] = '#'
    count = 1

    queue = [[y, x]]
    while queue:
        y, x = queue.pop(0)
        if y < 0 or y > ysize+2 or x < 0 or x > xsize+2:
            continue
        # check up
        if grid[y-1][x] != '#' and [y-1, x] not in tube:
            grid[y-1][x] = '#'
            count += 1
            queue.append([y-1, x])
        # check right
        if grid[y][x+1] != '#' and [y, x+1] not in tube:
            grid[y][x+1] = '#'
            count += 1
            queue.append([y, x+1])
        # check down
        if grid[y+1][x] != '#' and [y+1, x] not in tube:
            grid[y+1][x] = '#'
            count += 1
            queue.append([y+1, x])
        # check left
        if grid[y][x-1] != '#' and [y, x-1] not in tube:
            grid[y][x-1] = '#'
            count += 1
            queue.append([y, x-1])

    return count

right = []
r_count = 0
left = []
l_count = 0
for r in right_list:
    if r not in tube and r not in right:
        right.append(r)
        y, x = r
        if grid[y][x] != '#':
            r_count += bfs(y, x)
for l in left_list:
    if l not in tube and l not in left:
        left.append(l)
        y, x = l
        if grid[y][x] != '#':
            l_count += bfs(y, x)

print(f"Right {r_count}")
print(f"Left  {l_count}")