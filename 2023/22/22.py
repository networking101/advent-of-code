from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

bricks = []
resting_bricks = []
levels = {}
supports = {}
x_size = 0
y_size = 0
z_size = 0

for line in lines:
    b = line.split('~')
    b = [[int(zz) for zz in z.split(',')] for z in b]
    bricks.append(b)
    if max(b[0][0], b[1][0]) > x_size:
        x_size = max(b[0][0], b[1][0])
    if max(b[0][1], b[1][1]) > y_size:
        y_size = max(b[0][1], b[1][1])
    if max(b[0][2], b[1][2]) > z_size:
        z_size = max(b[0][2], b[1][2])

for z in range(1, z_size + 1):
    levels[z] = [[0]*(x_size+1) for _ in range(y_size+1)]

# sort by z axis
for j, y in enumerate(bricks):
    lowest = y
    for i, x in enumerate(bricks):
        if i <= j:
            continue
        curr = x
        if curr[0][2] < lowest[0][2]:
            bricks[j] = curr
            bricks[i] = lowest
            lowest = curr

def check_above(ab, at, y, x, ma):
    for z in range(ab, at+1):
        if levels[z][y][x] == 1:
            return (True, z)
    return (False, -1)


altitude_top = 1
altitude_bottom = 1
for bn, brick in enumerate(bricks):
    xrange = range(brick[0][0], brick[1][0]+1)
    yrange = range(brick[0][1], brick[1][1]+1)
    zrange = range(brick[0][2], brick[1][2]+1)

    for z in zrange:
        # check area coverage of layer of block
        tmp = 0
        curr_level = [[0]*(x_size+1) for _ in range(y_size+1)]
        for y in yrange:
            for x in xrange:
                curr_level[y][x] = 1
    
        # check if block needs to drop
        move_amount = 0
        if z != altitude_bottom:
            # check if need to lower
            check = False
            while z != altitude_bottom:
                for j, y in enumerate(curr_level):
                    for i, x in enumerate(y):
                        if x == 1 and levels[z-1][j][i] == 1:
                            check = True
                            break
                    if check:
                        break
                if not check:
                    z -= 1
                    move_amount += 1
                else:
                    break

        # put block on tower
        if z not in supports:
            supports[z] = {}
        for j, y in enumerate(curr_level):
            for i, x in enumerate(y):
                if x == 1:
                    levels[z][j][i] = x
                    supports[z][(j, i)] = bn
        if z > altitude_top:
            altitude_top = z

    # update brick position
    new_pos = deepcopy(brick)
    new_pos[0][2] -= move_amount
    new_pos[1][2] -= move_amount
    resting_bricks.append(new_pos)

    # check if altitude_bottom needs to move up
    if z != altitude_bottom:
        min_alt = altitude_top
        check_list = [[0]*(x_size+1) for _ in range(y_size+1)]
        for j, y in enumerate(levels[altitude_bottom]):
            for i, x in enumerate(y):
                res, ma = check_above(altitude_bottom, altitude_top, j, i, min_alt)
                if res:
                    check_list[j][i] = 1
                    if ma < min_alt:
                        min_alt = ma
        check = True
        for a in check_list:
            for b in a:
                if b == 0:
                    check = False
                    break
            if not check:
                break
        if check:
            altitude_bottom = min_alt + 1

saved = []

def chain_reaction(curr_brick):
    cr_list = [curr_brick]

    for bn, brick in enumerate(resting_bricks):
        if bn <= curr_brick:
            continue
        z = brick[0][2]
        if z == 1:
            continue
        xrange = range(brick[0][0], brick[1][0]+1)
        yrange = range(brick[0][1], brick[1][1]+1)
        spts = []
        for j in yrange:
            for i in xrange:
                if (j, i) in supports[z-1]:
                    spts.append(supports[z-1][(j, i)])
        check_supported = False
        for s in spts:
            if s not in cr_list:
                check_supported = True
        if not check_supported:
            cr_list.append(bn)
    
    return len(cr_list) - 1

supporting_bricks = []
chain_reaction_list = []
count2 = 0
for bn, resting_brick in enumerate(resting_bricks):
    if resting_brick[0][2] == 1:
        continue

    z = resting_brick[0][2]
    xrange = range(resting_brick[0][0], resting_brick[1][0]+1)
    yrange = range(resting_brick[0][1], resting_brick[1][1]+1)
    sprt = []
    for j in yrange:
        for i in xrange:
            if (j, i) in supports[z-1]:
                sprt.append(supports[z-1][(j, i)])
    if len(list(dict.fromkeys(sprt))) == 1:
        supporting_bricks.append(sprt[0])

        # recurse to find all bricks that will move
        if sprt[0] not in chain_reaction_list:
            tmp = chain_reaction(sprt[0])
            count2 += tmp
            chain_reaction_list.append(sprt[0])

print(len(bricks) - len(list(dict.fromkeys(supporting_bricks))))
print(count2)