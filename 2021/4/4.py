from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

tiles = []

drawn = lines.pop(0).split(',')
lines.pop(0)

tile = []
for l in lines:
    if not l:
        tiles.append(tile)
        tile = []
    else:
        row = []
        for z in l.split(" "):
            row.append(z)
        while " " in row:
            row.remove(" ")
        while "" in row:
            row.remove("")
        tile.append(row)

backupTiles = deepcopy(tiles)

def calculate(t, d):
    sum = 0
    for x in t:
        for y in x:
            if y != 'x':
                sum += int(y)
    return sum * int(d)

# Silver
stop = False
for i in range(len(drawn)):
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            for z in range(len(tiles[0][0])):
                if drawn[i] == tiles[x][y][z]:
                    tiles[x][y][z] = 'x'

    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            if tiles[x][y][0] == 'x' and tiles[x][y][1] == 'x' and tiles[x][y][2] == 'x' and tiles[x][y][3] == 'x' and tiles[x][y][4] == 'x':
                print(calculate(tiles[x], drawn[i]))
                stop = True
            elif tiles[x][0][y] == 'x' and tiles[x][1][y] == 'x' and tiles[x][2][y] == 'x' and tiles[x][3][y] == 'x' and tiles[x][4][y] == 'x':
                print(calculate(tiles[x], drawn[i]))
                stop = True
            if stop:
                break
        if stop:
            break
    if stop:
        break

# Gold
tiles = backupTiles
while len(tiles) != 0:
    popping = []
    stop = False
    for i in range(len(drawn)):
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                for z in range(len(tiles[0][0])):
                    if drawn[i] == tiles[x][y][z]:
                        tiles[x][y][z] = 'x'

        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                if tiles[x][y][0] == 'x' and tiles[x][y][1] == 'x' and tiles[x][y][2] == 'x' and tiles[x][y][3] == 'x' and tiles[x][y][4] == 'x':
                    popping.append(x)
                    stop = True
                elif tiles[x][0][y] == 'x' and tiles[x][1][y] == 'x' and tiles[x][2][y] == 'x' and tiles[x][3][y] == 'x' and tiles[x][4][y] == 'x':
                    popping.append(x)
                    stop = True
                if stop == True and len(tiles) == 1:
                    print(calculate(tiles[0], drawn[i]))
                    exit(0)

        if stop:
            newTiles = []
            for t in range(len(tiles)):
                if t not in popping:
                    newTiles.append(tiles[t])
            tiles = newTiles
            break