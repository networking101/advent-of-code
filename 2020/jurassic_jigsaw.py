from math import sqrt
from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]


data = {}
name = ""
for line in lines:
    if not line:
        continue

    if "Tile" in line:
        name = line[5:-1]
        data[name] = []
        continue

    data[name].append(line)

orientation = {}

for i in data:
    orientation[i] = ["", "", "", ""]


def print_tile(t):
    for i in t:
        print(i)
    print("")

def rotate_right(tile):
    nt = []

    for i in tile:
        nt.append("")

    for i in range(len(tile)):
        for j in range(len(tile)):
            nt[i] = tile[j][i] + nt[i]

    return nt

def rotate_left(tile):
    nt = []

    for i in tile:
        nt.append("")

    for i in range(len(tile)):
        for j in range(len(tile)):
            nt[len(tile)-1-j] += tile[i][j]

    return nt

def flip(tile):
    nt = []
    for i in tile:
        nt.append("")

    for i in range(len(tile)):
        for j in range(len(tile)):
            nt[i] += tile[i][len(tile)-1-j]

    return nt


def get_top(tile):
    return tile[0]

def get_right(tile):
    x = ""
    for i in tile:
        x += i[-1]
    return x

def get_bottom(tile):
    return tile[-1][::-1]

def get_left(tile):
    x = ""
    for i in tile[::-1]:
        x += i[0]
    return x

# get first tile
for i in data:
    starting = [i]
    found1 = [i]
    break



# get orientation
while starting:
    i = starting.pop(0)
    first = deepcopy(data[i])
    for j in data:
        second = deepcopy(data[j])
        if i == j:
            continue

        found = False
        for k in range(4):
            for l in range(8):
                t = ""
                if l%4 == 0:
                    t = get_top(second)
                if l%4 == 1:
                    t = get_right(second)
                if l%4 == 2:
                    t = get_bottom(second)
                if l%4 == 3:
                    t = get_left(second)

                if get_top(first) == t:
                    if j not in found1:
                        starting.append(j)
                        found1.append(j)
                    orientation[i][k] = j
                    found = True

                if l == 3 or l == 7:
                    if found == True:
                        break
                    data[j] = flip(second)
                    second = data[j]
            first = rotate_left(first)


# get the first corner
first = ""
silver = 1
for i in orientation:
    tc = 0
    for j in orientation[i]:
        if not j:
            tc += 1

    if tc == 2:
        first = i
        silver *= int(i)

print("Silver:  " + str(silver))

# set up actual image
picture = []
wall_size = int(sqrt(len(data)))
for i in range(wall_size):
    picture.append(list())
    for j in range(wall_size):
        picture[i].append("")

# orient the top left corner
for i in range(4):
    if orientation[first][0] or orientation[first][3]:
        data[first] = rotate_right(data[first])
        orientation[first].insert(0, orientation[first].pop())
    else:
        break
picture[0][0] = first
found = [(first, [0,0])]
found2 = [first]


def fix_or(y, x, adj, cur):
    if (y == 0 and orientation[adj][0] != "") or (x == 0 and orientation[adj][3] != "") or (y == wall_size-1 and orientation[adj][2] != "") or (x == wall_size-1 and orientation[adj][1] != ""):
        data[adj] = flip(data[adj])
        t = orientation[adj][1]
        orientation[adj][1] = orientation[adj][3]
        orientation[adj][3] = t
        while orientation[adj][(i+2)%4] != cur:
            data[adj] = rotate_right(data[adj])
            orientation[adj].insert(0, orientation[adj].pop())

# put each tile in the correct position with the correct orientation
while found:
    curr, pos = found.pop(0)
    y, x = pos
    for i in range(4):
        if orientation[curr][i]:
            offset = 0
            adjacent = orientation[curr][i]
            if adjacent in found2:
                continue
            while orientation[adjacent][(i+2)%4] != curr:
                data[adjacent] = rotate_right(data[adjacent])
                orientation[adjacent].insert(0, orientation[adjacent].pop())
                offset += 1
            if i == 0:
                fix_or(y-1, x, adjacent, curr)
                if get_top(data[curr]) == get_bottom(data[adjacent]):
                    data[adjacent] = flip(data[adjacent])
                    t = orientation[adjacent][1]
                    orientation[adjacent][1] = orientation[adjacent][3]
                    orientation[adjacent][3] = t
                picture[y-1][x] = adjacent
                found.append((adjacent, [y-1, x]))
            if i == 1:
                fix_or(y, x+1, adjacent, curr)
                picture[y][x+1] = adjacent
                found.append((adjacent, [y, x+1]))
            if i == 2:
                fix_or(y+1, x, adjacent, curr)
                if get_bottom(data[curr]) == get_top(data[adjacent]):
                    data[adjacent] = flip(data[adjacent])
                    t = orientation[adjacent][1]
                    orientation[adjacent][1] = orientation[adjacent][3]
                    orientation[adjacent][3] = t
                picture[y+1][x] = adjacent
                found.append((adjacent, [y+1, x]))
            if i == 3:
                fix_or(y, x-1, adjacent, curr)
                picture[y][x-1] = adjacent
                found.append((adjacent, [y, x-1]))

            found2.append(adjacent)

for i in data:
    tilesize = len(data[i][0])-2
    break

# set final picture without borders
tracker = 0
final = []
for i in range(len(picture)):
    for j in range(len(picture[i])):
        t = data[picture[i][j]]
        t.pop()
        t.pop(0)
        for k in range(len(t)):
            t[k] = t[k][1:-1]
            if j == 0:
                final.append(t[k])
            else:
                final[tracker+k] += t[k]
    
    tracker += tilesize

for i in final:
    print(i)
input("")

monster = [[1,0],[2,1],[2,4],[1,5],[1,6],[2,7],[2,10],[1,11],[1,12],[2,13],[2,16],[1,17],[0,18],[1,18],[1,19]]

# find monster
cnt = 0
for k in range(8):
    realcase = False
    for i in range(len(final)-2):
        for j in range(len(final[i])-19):
            case = True
            for m, n in monster:
                if final[i+m][j+n] != "#":
                    case = False
            if case == True:
                realcase = True
                
                for m, n in monster:
                    final[i+m] = final[i+m][:j+n] + "O" + final[i+m][j+n+1:]
                
                cnt += 1

    if realcase == True:
        break
    final = rotate_right(final)

    if k == 3:
        final = flip(final)

for i in final:
    for j in i:
        if j == "O":
            print(j, end="")
        else:
            print(" ", end="")
    print("")

count = 0
for i in final:
    for j in i:
        if j == "#":
            count += 1

print("Gold:    " + str(count))