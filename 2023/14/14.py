import numpy as np

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[z for z in line] for line in lines]
saved = []

def count_support(grid):
    c = 0
    for j, row in enumerate(grid[::-1]):
        for i, x in enumerate(row):
            if x == 'O':
                c += j+1
    print(c)

part1 = False
index = 0
check = False
while index < 1000000000:
    np_grid = np.array(grid)
    rot_grid = np.rot90(np_grid)
    grid = rot_grid.tolist()
    for cycle in range(4):
        new_grid = []
        for r, row in enumerate(grid):
            new_secions = []
            sections = ''.join(row).split('#')
            for s in sections:
                if len(s) < 2:
                    new_secions.append(s)
                else:
                    s = list(s)
                    for first in range(len(s)):
                        if s[first] == 'O':
                            continue
                        for second in range(first+1, len(s)):
                            if s[second] == 'O':
                                s[first] = 'O'
                                s[second] = '.'
                                break
                    new_secions.append(''.join(s))
            
            new_grid.append(list('#'.join(new_secions)))

        np_grid = np.array(new_grid)
        grid = np.rot90(np_grid, 3)
        grid = grid.tolist()

        if not part1:
            count_support(grid)
            part1 = True

    np_grid = np.array(grid)
    np_grid = np.rot90(np_grid, 3)
    grid = np_grid.tolist()

    if grid in saved and not check:
        for z, s in enumerate(saved):
            if grid == s:
                index = int(1000000000 / (index - z)) * (index - z) + z - (index - z)
                check = True
                break
    saved.append(grid)
    index += 1

count_support(grid)