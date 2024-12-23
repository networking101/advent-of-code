
with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[x for x in row] for row in lines]

start = None
ending = None
for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x == 'S':
            start = (j, i)
            grid[j][i] = '.'
        if x == 'E':
            ending = (j, i)
            grid[j][i] = '.'

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
y_max = len(grid) - 1
x_max = len(grid[0]) - 1

curr = start
positions = {}
steps = 0
positions[curr] = steps
while curr != ending:
    y, x = curr
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
        if (ny, nx) not in positions and grid[ny][nx] == '.':
            steps += 1
            curr = (ny, nx)
            positions[curr] = steps
            break

# print(steps)
# print(positions)

silver = 0
for k, v in positions.items():
    y, x = k
    for dy, dx in directions:
        ny = y + 2*dy
        nx = x + 2*dx
        if (ny, nx) in positions:
            if positions[(y, x)] + 2 + (steps - positions[(ny, nx)]) <= steps - 100:
            # if positions[(y, x)] + 2 + (steps - positions[(ny, nx)]) < steps:
                silver += 1

print(silver)

directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

gold = 0
for k, v in positions.items():
    y, x = k
    checked = []
    for dy, dx in directions:
        for i in range(21):
            for j in range(21):
                if i + j > 20:
                    continue
                ny = y + dy * i
                nx = x + dx * j
                if (ny, nx) in positions:
                    if positions[(y, x)] + i + j + (steps - positions[(ny, nx)]) <= steps - 100:
                    # if positions[(y, x)] + i + j + (steps - positions[(ny, nx)]) <= steps - 50:
                        if ((y, x), (ny, nx)) not in checked:
                            checked.append(((y, x), (ny, nx)))
                            gold += 1

print(gold)