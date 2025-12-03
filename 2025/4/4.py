with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [list(line) for line in lines]

y_max = len(grid)
x_max = len(grid[0])

y_dirs = [0, -1, -1, -1, 0, 1, 1, 1]
x_dirs = [1, 1, 0, -1, -1, -1, 0, 1]

silver = 0
for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x != '@':
            continue

        neighbors = 0
        for dj, di in zip(y_dirs, x_dirs):
            nj = j + dj
            ni = i + di
            if nj < 0 or nj >= y_max or ni < 0 or ni >= x_max:
                continue

            if grid[nj][ni] == '@':
                neighbors += 1

        if neighbors < 4:
            silver += 1

print(silver)

gold = 0
old = -1
new = y_max * x_max
while old != new:
    old = new
    new = 0
    for j, y in enumerate(grid):
        for i, x in enumerate(y):
            if x != '@':
                continue

            neighbors = 0
            for dj, di in zip(y_dirs, x_dirs):
                nj = j + dj
                ni = i + di
                if nj < 0 or nj >= y_max or ni < 0 or ni >= x_max:
                    continue

                if grid[nj][ni] == '@':
                    neighbors += 1

            if neighbors < 4:
                new += 1
                grid[j][i] = '.'
                gold += 1

print(gold)