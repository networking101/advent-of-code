import numpy as np

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

height = 6
width = 50

def print_grid():
    for y in grid:
        for x in y:
            print(x, end='')
        print()
    print()

grid = np.full((height, width), '.')

for line in lines:
    if line[:4] == "rect":
        x, y = [int(z) for z in line[5:].split('x')]
        
        for j in range(y):
            for i in range(x):
                grid[j][i] = "#"
                
    if line[:13] == "rotate column":
        x, x_len = [int(z) for z in line[16:].split()[::2]]
        
        grid = np.transpose(grid)
        grid[x] = np.roll(grid[x], x_len)
        grid = np.transpose(grid)

    if line[:10] == "rotate row":
        y, y_len = [int(z) for z in line[13:].split()[::2]]
        grid[y] = np.roll(grid[y], y_len)

count = 0
for y in grid:
    for x in y:
        if x == '#':
            count += 1

print(count)
print_grid()