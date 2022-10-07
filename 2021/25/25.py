from copy import deepcopy

with open("input.bak", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(c)
    grid.append(row)

x = 0
while True:
    """for j in grid:
        for i in j:
            print(i, end="")
        print("")
    print("")"""

    x += 1
    ogrid = deepcopy(grid)

    ng = deepcopy(grid)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == '>':
                if i+1 >= len(grid[j]):
                    nextx = 0
                else:
                    nextx = i + 1
                if grid[j][nextx] == '.':
                    ng[j][nextx] = '>'
                    ng[j][i] = '.'
    
    grid = ng
    ng = deepcopy(grid)

    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == "v":
                if j+1 >= len(grid):
                    nexty = 0
                else:
                    nexty = j + 1
                if grid[nexty][i] == '.':
                    ng[nexty][i] = 'v'
                    ng[j][i] = '.'

    if ng == ogrid:
        print(x)
        break

    grid = ng