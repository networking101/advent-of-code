import numpy as np
from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

terrains = []

t = []
for line in lines:
    if not line:
        terrains.append(t)
        t = []
    else:
        t.append([z for z in line])
terrains.append(t)

def check(t, curr):
    a = curr
    b = curr + 1

    while a >= 0 and b < len(t):
        if t[a] != t[b]:
            assert a != curr
            return -1
        a -= 1
        b += 1

    return curr + 1

def cycle(t, pos, saved=-1):
    for j, row in enumerate(t[:-1]):
        if t[j] == t[j+1]:
            c =  check(t, j)
            if c != -1 and not (c == saved and pos == 0):
                return (c * 100, 0)

    np_t = np.array(t)
    np_t = np.rot90(np_t, 3)
    rot_t = np_t.tolist()
    
    for i, col in enumerate(rot_t[:-1]):
        if rot_t[i] == rot_t[i+1]:
            c =  check(rot_t, i)
            if c != -1 and not (c == saved and pos == 1):
                return (c, 1)
            
    assert pos != -1 and saved != -1
    return (-1, -1)

count1 = 0
count2 = 0
for terrain in terrains:
    res, pos = cycle(terrain, -1)
    saved = res
    if pos == 0:
        saved = int(saved / 100)
    assert saved != -1
    count1 += res

    caught = False
    for jj, y in enumerate(terrain):
        for ii, x in enumerate(y):
            new_terrain = deepcopy(terrain)
            if x == '.':
                new_terrain[jj][ii] = '#'
            else:
                new_terrain[jj][ii] = '.'

            res, _ = cycle(new_terrain, pos, saved)
            if res != -1:
                caught = True
                count2 += res
                break
        if caught:
            break

print(count1)
print(count2)