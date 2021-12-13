with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

size = 2000

grid = []
for i in range(size):
    grid.append(['.'] * size)

folds = []
for i in range(len(lines)):
    if not lines[i]:
        folds = lines[i+1:]
        break
    x, y = [int(z) for z in lines[i].split(',')]
    grid[y][x] = "#"

def foldy(g, v):
    for j in range(v+1, len(g)):
        for i in range(len(g[0])):
            if g[j][i] == "#":
                g[(v-j) + v][i] = "#"

def foldx(g, v):
    for j in range(len(g)):
        for i in range(v, len(g[0])):
            if g[j][i] == "#":
                g[j][(v-i) + v] = "#"

silver = False
for i in folds:
    _, _, f = i.split(" ")
    orientation, vector = f.split("=")
    vector = int(vector)
    if orientation == "y":
        foldy(grid, vector)
        grid = grid[:vector]
    else:
        foldx(grid, vector)
        for z in range(len(grid)):
            grid[z] = grid[z][:vector]
    
    silverCount = 0
    if not silver:
        for a in grid:
            for b in a:
                if b == "#":
                    silverCount += 1
        print(silverCount)
        silver = True

for i in grid:
    for j in i:
        if j == ".":
            print(" ", end="")
        else:
            print(j, end="")
    print("")