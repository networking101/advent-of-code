import numpy as np

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

regions = []
presents = {}

tmp = []
index = 0
for line in lines:
    if "x" in line:
        l, r = line.split(": ")

        regions.append((([int(x) for x in l.split("x")], [int(x) for x in r.split()])))
    
    else:
        if ":" in line:
            index = int(line.split(":")[0])
            tmp = []

        elif not line:
            presents[index] = tmp

        else:
            tmp.append(line)

silver = 0
for grid_size, requirements in regions:
    area = grid_size[0] * grid_size[1]

    num_pieces = sum(requirements)

    if num_pieces * 9 <= area:
        silver += 1
        
print(silver)