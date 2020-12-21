from math import sqrt

with open("input2.txt", "r") as fp:
    lines = [line.strip() for line in fp]

tt = ["123", "456", "789"]

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

for i in data:
    starting = [i]
    break

# get orientation
for i in data:
    first = data[i]
    for j in data:
        second = data[j]
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
                    if i == "2473":
                        print(i)
                        for z in first:
                            print(z)
                        print("\n")
                        for z in second:
                            print(z)
                        print("\n")
                    orientation[i][k] = j
                    if i == "2473":
                        print(j, k, l)
                        print(orientation[j])
                        input("\n")
                    found = True

                if l == 3 or l == 7:
                    if found == True:
                        break
                    data[j] = flip(second)
                    second = data[j]

            data[i] = rotate_left(first)
            first = data[i]

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

first = "1951"

print(silver)

picture = []
wall_size = int(sqrt(len(data)))
for i in range(wall_size):
    picture.append(list())
    for j in range(wall_size):
        picture[i].append("")

# orient the first orientation
for i in range(4):
    if orientation[first][0] or orientation[first][3]:
        data[first] = rotate_right(data[first])
        orientation[first].append(orientation[first].pop(0))
    else:
        break
picture[0][0] = first
found = [(first, [0,0])]
found2 = [first]

"""
for i in orientation:
    print(i, end="  ")
    print(orientation[i])
"""

def fix_or(y, x, adj, cur):
    
    print("Adj: " + adj)
    print(orientation[adj])
    print("")

    if (y == 0 and orientation[adj][0] != "") or (x == 0 and orientation[adj][3] != "") or (y == wall_size-1 and orientation[adj][2] != "") or (x == wall_size-1 and orientation[adj][1] != ""):
        print("FLIP")
        data[adj] = flip(data[adj])
        t = orientation[adj][1]
        orientation[adj][1] = orientation[adj][3]
        orientation[adj][3] = t        
        while orientation[adj][(i+2)%4] != cur:
            print("ROT RIGHT")
            data[adj] = rotate_right(data[adj])
            orientation[adj].append(orientation[adj].pop(0))

        print("Adj: " + adj)
        print(orientation[adj])
        print("")

# put each tile in the correct position with the correct orientation
while found:
    curr, pos = found.pop(0)
    y, x = pos
    print("CURR: " + curr)
    for i in data[curr]:
        print(i)
    print("")
    for i in range(4):
        if orientation[curr][i]:
            offset = 0
            adjacent = orientation[curr][i]
            if adjacent in found2:
                continue
            if adjacent == "2473":
                print("FOUND!!!!")
                for z in data[adjacent]:
                    print(z)
                print(orientation[adjacent])
                print("\n")
            while orientation[adjacent][(i+2)%4] != curr:
                data[adjacent] = rotate_right(data[adjacent])
                orientation[adjacent].append(orientation[adjacent].pop(0))
                offset += 1
            if i == 0:
                fix_or(y-1, x, adjacent, curr)
                picture[y-1][x] = adjacent
                found.append((adjacent, [y-1, x]))
            if i == 1:
                fix_or(y, x+1, adjacent, curr)
                picture[y][x+1] = adjacent
                found.append((adjacent, [y, x+1]))
            if i == 2:
                fix_or(y+1, x, adjacent, curr)
                picture[y+1][x] = adjacent
                found.append((adjacent, [y+1, x]))
            if i == 3:
                fix_or(y, x-1, adjacent, curr)
                picture[y][x-1] = adjacent
                found.append((adjacent, [y, x-1]))

            found2.append(adjacent)

    for i in picture:
        print(i)
    input("")

exit(0)

for i in data:
    tilesize = len(data[i][0])-2
    break

tracker = 0
final = []
for i in range(len(picture)):
    for j in range(len(picture[i])):
        t = data[picture[i][j]]
        t.pop(0)
        t.pop()
        for k in range(len(t)):
            t[k] = t[k][1:-1]
            if j == 0:
                final.append(t[k])
            else:
                final[tracker+k] += t[k]
    
    tracker += tilesize

for i in final:
    print(i)

