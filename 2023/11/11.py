import numpy as np

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[z for z in line] for line in lines]

exp_x = []
exp_y = []

grid = np.array(grid)

for j, row in enumerate(grid):
    if '#' not in row:
        exp_y.append(j)

grid = np.rot90(grid, 3)

for i, col in enumerate(grid):
    if '#' not in col:
        exp_x.append(i)

grid = np.rot90(grid, )

pos = []

for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x == '#':
            pos.append([j, i])

count1 = 0
count2 = 0

for j, a in enumerate(pos):
    for i, b in enumerate(pos[j+1:]):
        c1 = abs(a[0] - b[0]) + abs(a[1] - b[1])
        c2 = c1
        y_range = range(min(a[0],b[0]), max(a[0],b[0]))
        x_range = range(min(a[1],b[1]), max(a[1],b[1]))
        c1 += sum(min(a[0],b[0]) < z < max(a[0],b[0]) for z in exp_y)
        c1 += sum(min(a[1],b[1]) < z < max(a[1],b[1]) for z in exp_x)
        c2 += sum(min(a[0],b[0]) < z < max(a[0],b[0]) for z in exp_y) * (1000000 - 1)
        c2 += sum(min(a[1],b[1]) < z < max(a[1],b[1]) for z in exp_x) * (1000000 - 1)
        count1 += c1
        count2 += c2

print(count1)
print(count2)