from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

gridSize = 50

grid = []
for x in range(gridSize * -1, gridSize + 1):
    g1 = []
    for y in range(gridSize * -1, gridSize + 1):
        g2 = [0] * (gridSize * 2 + 1)
        g1.append(g2)
    grid.append(g1)

# parse instructions.  Ignore sizes that are too big
instruction = []
for line in lines:
    command, rest = line.split(" ")
    x, y, z = rest.split(',')
    x = [int(t) for t in x[2:].split("..")]
    x = list(range(x[0], x[1]+1))
    y = [int(t) for t in y[2:].split("..")]
    y = list(range(y[0], y[1]+1))
    z = [int(t) for t in z[2:].split("..")]
    z = list(range(z[0], z[1]+1))

    if max(x) > gridSize or min(x) < (gridSize * -1) or max(y) > gridSize or min(y) < (gridSize * -1) or max(z) > gridSize or min(z) < (gridSize * -1):
        continue

    instruction.append((command, x, y, z))

# Silver
# flip grid cubes for each instruction
for i in instruction:
    command = i[0]
    for x in i[1]:
        for y in i[2]:
            for z in i[3]:
                if command == "on":
                    grid[x + gridSize][y + gridSize][z + gridSize] = 1
                else:
                    grid[x + gridSize][y + gridSize][z + gridSize] = 0

# count on lights
count = 0
for x in grid:
    for y in x:
        for z in y:
            if z == 1:
                count += 1

print(count)

# Gold

instructionGold = []
for line in lines:
    command, rest = line.split(" ")
    x, y, z = rest.split(',')
    x = [int(t) for t in x[2:].split("..")]
    y = [int(t) for t in y[2:].split("..")]
    z = [int(t) for t in z[2:].split("..")]

    instructionGold.append((command, range(x[0], x[1]+1), range(y[0], y[1]+1), range(z[0], z[1]+1)))

previousBlocks = []
for i in range(len(instructionGold)):
    acomm, ax, ay, az = instructionGold[i]
    newPB = []
    for bcomm, bx, by, bz in previousBlocks:
        xrange = range(max(ax[0], bx[0]), min(ax[-1], bx[-1])+1)
        yrange = range(max(ay[0], by[0]), min(ay[-1], by[-1])+1)
        zrange = range(max(az[0], bz[0]), min(az[-1], bz[-1])+1)
        if len(xrange) == 0 or len(yrange) == 0 or len(zrange) == 0:
            continue
        if bcomm == "on":
            newPB.append(("off", xrange, yrange, zrange))
        else:
            newPB.append(("on", xrange, yrange, zrange))
    previousBlocks += newPB
    if acomm == "on":
        previousBlocks.append(instructionGold[i])

tot = 0
for pcomm, px, py, pz in previousBlocks:
    tmptot = (px[-1]+1 - px[0]) * (py[-1]+1 - py[0]) * (pz[-1]+1 - pz[0])
    if pcomm == "on":
        tot += tmptot
    else:
        tot -= tmptot

print(tot)