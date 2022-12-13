from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []
start = ()
end = ()

As = []

for y in range(len(lines)):
    tmp = []
    for x in range(len(lines[0])):
        if lines[y][x] == "S":
            start = (y, x)
            tmp.append("a")
            continue
        if lines[y][x] == "E":
            end = (y, x)
            tmp.append("z")
            continue
        if lines[y][x] == "a" and x == 0:
            As.append((y, x))
        tmp.append(lines[y][x])
    grid.append(tmp)

grid2 = deepcopy(grid)

def print_grid(g):
    for y in g:
        for x in y:
            print(x, end='')
        print()
    print()

# Part 1
found = []
queue = [(start, 0)]
while queue:
    (y, x), d = queue.pop(0)
    found.append((y, x))
    if (y, x) == end:
        print(d)
        min_dist = d
        break
    curr_ord = ord(grid[y][x])
    grid[y][x] = '.'
    # check up
    if y-1 >= 0 and (ord(grid[y-1][x]) - curr_ord) <= 1 and grid[y-1][x] != ".":
        if (y-1, x) not in found:
            queue.append(((y-1, x), d+1))
    # check down
    if y+1 < len(grid) and (ord(grid[y+1][x]) - curr_ord) <= 1 and grid[y+1][x] != ".":
        if (y+1, x) not in found:
            queue.append(((y+1, x), d+1))
    # check left
    if x-1 >= 0 and (ord(grid[y][x-1]) - curr_ord) <= 1 and grid[y][x-1] != ".":
        if (y, x-1) not in found:
            queue.append(((y, x-1), d+1))
    # check right
    if x+1 < len(grid[0]) and (ord(grid[y][x+1]) - curr_ord) <= 1 and grid[y][x+1] != ".":
        if (y, x+1) not in found:
            queue.append(((y, x+1), d+1))

# Part 2
for a in As:
    start = a
    grid = deepcopy(grid2)
    found = []
    queue = [(start, 0)]
    while queue:
        (y, x), d = queue.pop(0)
        found.append((y, x))
        if (y, x) == end:
            if d < min_dist:
                min_dist = d
            break
        curr_ord = ord(grid[y][x])
        grid[y][x] = '.'
        # check up
        if y-1 >= 0 and (ord(grid[y-1][x]) - curr_ord) <= 1 and grid[y-1][x] != ".":
            if (y-1, x) not in found:
                queue.append(((y-1, x), d+1))
        # check down
        if y+1 < len(grid) and (ord(grid[y+1][x]) - curr_ord) <= 1 and grid[y+1][x] != ".":
            if (y+1, x) not in found:
                queue.append(((y+1, x), d+1))
        # check left
        if x-1 >= 0 and (ord(grid[y][x-1]) - curr_ord) <= 1 and grid[y][x-1] != ".":
            if (y, x-1) not in found:
                queue.append(((y, x-1), d+1))
        # check right
        if x+1 < len(grid[0]) and (ord(grid[y][x+1]) - curr_ord) <= 1 and grid[y][x+1] != ".":
            if (y, x+1) not in found:
                queue.append(((y, x+1), d+1))

print(min_dist)