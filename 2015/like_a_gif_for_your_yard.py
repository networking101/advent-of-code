from copy import deepcopy

with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []

for i in range(len(lines)):
    grid.append([])
    for j in range(len(lines[i])):
        grid[i].append(lines[i][j])

def calcNeighbors(g, y, x):
    if x < 0 or y < 0:
        return False
    try:
        if g[y][x] == "#":
            return True
    except:
        pass
    return False


for k in range(100):
    ng = deepcopy(grid)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            ts = 0
            for l in range(-1, 2):
                for m in range(-1, 2):
                    if l == m == 0:
                        continue
                    if calcNeighbors(grid, i + l, j + m):
                        ts += 1
            if (grid[i][j] == "#" and (ts == 2 or ts == 3)) or (grid[i][j] == "." and ts == 3):
                ng[i][j] = "#"
            else:
                ng[i][j] = "."

    ng[0][0] = "#"
    ng[0][len(grid[0])-1] = "#"
    ng[len(grid)-1][len(grid[0])-1] = "#"
    ng[len(grid)-1][0] = "#"

    for z in ng:
        print(z)
    print("")

    grid = ng


cnt = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if grid[i][j] == "#":
            cnt += 1

print(cnt)
