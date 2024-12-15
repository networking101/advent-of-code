with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

y_max = len(lines)
x_max = len(lines[0])

grid_silver = []
grid_gold = []
instructions = []

# parse input
flag_store = False
for line in lines:
    if not line:
        flag_store = True
        continue
    
    if flag_store:
        instructions += [x for x in line]
    else:
        grid_silver.append([x for x in line])
        row = []
        for x in line:
            if x == '#':
                row += ['#', '#']
            if x == 'O':
                row += ['[', ']']
            if x == '.':
                row += ['.', '.']
            if x == '@':
                row += ['@', '.']
        grid_gold.append(row)

# find current position silver
curr_silver = None
for j, y in enumerate(grid_silver):
    for i, x in enumerate(y):
        if x == '@':
            curr_silver = (j, i)
            grid_silver[j][i] = '.'

# find current position gold
curr_gold = None
for j, y in enumerate(grid_gold):
    for i, x in enumerate(y):
        if x == '@':
            curr_gold = (j, i)
            grid_gold[j][i] = '.'

def print_grid(grid, curr):
    for j, y in enumerate(grid):
        for i, x in enumerate(y):
            if curr == (j, i):
                print("@", end='')
            else:
                print(x, end='')
        print()
    print()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def find_edge(grid, curr, dir):
    y, x = curr
    dy, dx = directions[dir]
    ny = y + dy
    nx = x + dx

    if grid[y][x] == '#':
        return False

    if grid[ny][nx] == '.':
        tmp = grid[ny][nx]
        grid[ny][nx] = grid[y][x]
        grid[y][x] = tmp
        return True

    res = find_edge(grid, (ny, nx), dir)
    if res:
        tmp = grid[ny][nx]
        grid[ny][nx] = grid[y][x]
        grid[y][x] = tmp
        return True
    
    return False

def check_move(curr, dir):
    y, x = curr
    dy, dx = directions[dir]
    ny = y + dy
    nx = x + dx

    if grid_gold[ny][nx] == '.':
        return True
    if grid_gold[ny][nx] == '#':
        return False

    if grid_gold[ny][nx] == '[':
        ny2 = ny
        nx2 = nx + 1
    if grid_gold[ny][nx] == ']':
        ny2 = ny
        nx2 = nx - 1

    if check_move((ny, nx), dir) and check_move((ny2, nx2), dir):
        return True
    return False

def move(curr, dir):
    if grid_gold[curr[0]][curr[1]] == '.':
        return
    
    assert(grid_gold[curr[0]][curr[1]] == '[' or grid_gold[curr[0]][curr[1]] == ']')
    
    y, x = curr
    dy, dx = directions[dir]
    ny = y + dy
    nx = x + dx
    if grid_gold[y][x] == '[':
        y2 = y
        x2 = x + 1
    if grid_gold[y][x] == ']':
        y2 = y
        x2 = x - 1

    ny2 = y2 + dy
    nx2 = x2 + dx

    move((ny, nx), dir)
    move((ny2, nx2), dir)

    tmp = grid_gold[y][x]
    grid_gold[y][x] = grid_gold[ny][nx]
    grid_gold[ny][nx] = tmp

    tmp = grid_gold[y2][x2]
    grid_gold[y2][x2] = grid_gold[ny2][nx2]
    grid_gold[ny2][nx2] = tmp


def find_edge_gold(curr, dir):
    if check_move(curr, dir):
        y, x = curr
        dy, dx = directions[dir]
        ny = y + dy
        nx = x + dx
        move((ny, nx), dir)
        return True

    return False

for i in instructions:
    if i == '^':
        if find_edge(grid_silver, curr_silver, 0):
            curr_silver = (curr_silver[0] + directions[0][0], curr_silver[1] + directions[0][1])
        if find_edge_gold(curr_gold, 0):
            curr_gold = (curr_gold[0] + directions[0][0], curr_gold[1] + directions[0][1])
    if i == '>':
        if find_edge(grid_silver, curr_silver, 1):
            curr_silver = (curr_silver[0] + directions[1][0], curr_silver[1] + directions[1][1])
        if find_edge(grid_gold, curr_gold, 1):
            curr_gold = (curr_gold[0] + directions[1][0], curr_gold[1] + directions[1][1])
    if i == 'v':
        if find_edge(grid_silver, curr_silver, 2):
            curr_silver = (curr_silver[0] + directions[2][0], curr_silver[1] + directions[2][1])
        if find_edge_gold(curr_gold, 2):
            curr_gold = (curr_gold[0] + directions[2][0], curr_gold[1] + directions[2][1])
    if i == '<':
        if find_edge(grid_silver, curr_silver, 3):
            curr_silver = (curr_silver[0] + directions[3][0], curr_silver[1] + directions[3][1])
        if find_edge(grid_gold, curr_gold, 3):
            curr_gold = (curr_gold[0] + directions[3][0], curr_gold[1] + directions[3][1])

silver = 0
for j, y in enumerate(grid_silver):
    for i, x in enumerate(y):
        if grid_silver[j][i] == 'O':
            silver += 100 * j + i

print(silver)

gold = 0
for j, y in enumerate(grid_gold):
    for i, x in enumerate(y):
        if grid_gold[j][i] == '[':
            gold += 100 * j + i

print(gold)