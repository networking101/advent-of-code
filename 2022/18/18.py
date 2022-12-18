from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

cubes = []
maxx = 0
maxy = 0
maxz = 0
minx = 20
miny = 20
minz = 20
for line in lines:
    x, y, z = [int(c) for c in line.split(',')]
    if x > maxx:
        maxx = x
    if x < minx:
        minx = x
    if y > maxy:
        maxy = y
    if y < miny:
        miny = y
    if z > maxz:
        maxz = z
    if z < minz:
        minz = z
    cubes.append((x, y, z))

exposed_sides = 0
for c in cubes:
    x, y, z = c
    # check x
    if (x-1, y, z) not in cubes:
        exposed_sides += 1
    if (x+1, y, z) not in cubes:
        exposed_sides += 1
    # check y
    if (x, y-1, z) not in cubes:
        exposed_sides += 1
    if (x, y+1, z) not in cubes:
        exposed_sides += 1
    # check z
    if (x, y, z-1) not in cubes:
        exposed_sides += 1
    if (x, y, z+1) not in cubes:
        exposed_sides += 1

print(exposed_sides)

exposed_sides = 0
found_air = [(x, y, z)]
queue = [(minx-1, miny, minz)]
while queue:
    x, y, z = queue.pop(0)

    # check for cubes in vicinity
    if (x-1, y, z) in cubes:
        exposed_sides += 1
    if (x+1, y, z) in cubes:
        exposed_sides += 1
    if (x, y-1, z) in cubes:
        exposed_sides += 1
    if (x, y+1, z) in cubes:
        exposed_sides += 1
    if (x, y, z-1) in cubes:
        exposed_sides += 1
    if (x, y, z+1) in cubes:
        exposed_sides += 1

    # search left
    if x-1 >= minx-1 and (x-1, y, z) not in cubes and (x-1, y, z) not in found_air:
        queue.append((x-1, y, z))
        found_air.append((x-1, y, z))

    # search right
    if x+1 <= maxx+1 and (x+1, y, z) not in cubes and (x+1, y, z) not in found_air:
        queue.append((x+1, y, z))
        found_air.append((x+1, y, z))

    # search up
    if y-1 >= miny-1 and (x, y-1, z) not in cubes and (x, y-1, z) not in found_air:
        queue.append((x, y-1, z))
        found_air.append((x, y-1, z))

    # search down
    if y+1 <= maxy+1 and (x, y+1, z) not in cubes and (x, y+1, z) not in found_air:
        queue.append((x, y+1, z))
        found_air.append((x, y+1, z))

    # search in
    if z-1 >= minz-1 and (x, y, z-1) not in cubes and (x, y, z-1) not in found_air:
        queue.append((x, y, z-1))
        found_air.append((x, y, z-1))

    # search out
    if z+1 <= maxz+1 and (x, y, z+1) not in cubes and (x, y, z+1) not in found_air:
        queue.append((x, y, z+1))
        found_air.append((x, y, z+1))
    
print(exposed_sides)