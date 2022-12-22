import numpy as np

with open("input", "r") as fp:
    lines = [line.rstrip() for line in fp]

def print_board(pos=None, face=None):
    for j, b in enumerate(board):
        for i, c in enumerate(b):
            if pos and pos[0] == j and pos[1] == i:
                if face == 0:
                    print('^', end='')
                if face == 1:
                    print('>', end='')
                if face == 2:
                    print('v', end='')
                if face == 3:
                    print('<', end='')
            else:
                print(c, end='')
        print()
    print()

# create board and paths
board = []
path = ""
b = True
maxx = 0
for l in lines:
    if not l:
        b = False
    elif b:
        if (len(l)-1) > maxx:
            maxx = len(l)-1
        board.append(list(l))
    else:
        path = l
maxy = len(board)-1

# pad right
for i, y in enumerate(board):
    board[i] = y + [' '] * (maxx - len(y) + 1)

# split path
distances = []
directions = []
for i, d in enumerate(path):
    if d == 'L' or d == 'R':
        directions.append(d)
path = path.replace('R', 'L')
distances = [int(x) for x in path.split('L')]

# generate up, right, down, and left coordinates for each position on the board
coordinates = {}
pos = None
for y, b in enumerate(board):
    for x, c in enumerate(b):

        # if we aren't in a valid board position, continue
        if board[y][x] != '.':
            continue

        # get start position
        if not pos:
            pos = (y, x)
        coordinates[(y, x)] = []

        # up
        if y - 1 < 0 or board[y-1][x] == ' ':
            j = maxy
            while j > y:
                if board[j][x] == '#':
                    coordinates[(y, x)].append((y, x))
                    break
                if board[j][x] == '.':
                    coordinates[(y, x)].append((j, x))
                    break
                if board[j][x] == ' ':
                    j -= 1
        elif board[y-1][x] == '#':
            coordinates[(y, x)].append((y, x))
        else:
            coordinates[(y, x)].append((y-1, x))

        # right
        if x+1 > maxx or board[y][x+1] == ' ':
            i = 0
            while i < x:
                if board[y][i] == '#':
                    coordinates[(y, x)].append((y, x))
                    break
                if board[y][i] == '.':
                    coordinates[(y, x)].append((y, i))
                    break
                if board[y][i] == ' ':
                    i += 1
        elif board[y][x+1] == '#':
            coordinates[(y, x)].append((y, x))
        else:
            coordinates[(y, x)].append((y, x+1))

        # down
        if y+1 > maxy or board[y+1][x] == ' ':
            j = 0
            while j < y:
                if board[j][x] == '#':
                    coordinates[(y, x)].append((y, x))
                    break
                if board[j][x] == '.':
                    coordinates[(y, x)].append((j, x))
                    break
                if board[j][x] == ' ':
                    j += 1
        elif board[y+1][x] == '#':
            coordinates[(y, x)].append((y, x))
        else:
            coordinates[(y, x)].append((y+1, x))

        # left
        if x-1 < 0 or board[y][x-1] == ' ':
            i = maxx
            while i > x:
                if board[y][i] == '#':
                    coordinates[(y, x)].append((y, x))
                    break
                if board[y][i] == '.':
                    coordinates[(y, x)].append((y, i))
                    break
                if board[y][i] == ' ':
                    i -= 1
        elif board[y][x-1] == '#':
            coordinates[(y, x)].append((y, x))
        else:
            coordinates[(y, x)].append((y, x-1))


# Move around board
# 0 = up
# 1 = right
# 2 = down
# 3 = left
facing = 1
while directions or distances:
    d = distances.pop(0)
    for _ in range(d):
        if facing == 0 and coordinates[pos][0] != pos:
            pos = coordinates[pos][0]
        if facing == 1 and coordinates[pos][1] != pos:
            pos = coordinates[pos][1]
        if facing == 2 and coordinates[pos][2] != pos:
            pos = coordinates[pos][2]
        if facing == 3 and coordinates[pos][3] != pos:
            pos = coordinates[pos][3]

    if directions:
        d = directions.pop(0)
        # print(d)
        if d == 'R':
            facing = (facing + 1) % 4
        else:
            facing = (facing - 1) % 4

print((pos[0]+1) * 1000 + (pos[1]+1) * 4 + (facing-1) % 4)

# create board and paths
board = []
path = ""
b = True
maxx = 0
for l in lines:
    if not l:
        b = False
    elif b:
        if (len(l)-1) > maxx:
            maxx = len(l)-1
        board.append(list(l))
    else:
        path = l
maxy = len(board)-1

# pad right
for i, y in enumerate(board):
    board[i] = y + [' '] * (maxx - len(y) + 1)


# Part 2
# example
face_front = ["" * 3] * 3
face_bottom = ["" * 3] * 3
face_top = ["" * 3] * 3
face_left = ["" * 3] * 3
face_right = ["" * 3] * 3
face_back = ["" * 3] * 3
for y in range(3):
    for x in range(3):
        face_front[y][x] = board[y][x+8]
        face_bottom[y][x] = board[y+4][x+8]
        face_top[y][x] = board[y+4][x]
        face_back[y][x] = board[y+8][x+8]
        face_left[y][x] = board[y+4][x+4]
        face_right[y][x] = board[y+8][x+12]
face_top = np.rot90(face_top, 2)
face_back = np.rot90(face_back, 2)
face_left = np.rot90(face_left, 1)
face_right = np.rot90(face_right, 2)
cube = [face_front, face_top, face_bottom, face_left, face_right, face_back]

# puzzle input
# TODO

# generate up, right, down, and left coordinates for each position on the cube
coordinates = {}
pos = None
# f 0 = front
# f 1 = top
# f 2 = bottom
# f 3 = left
# f 4 = right
# f 5 = back
for f in range(len(cube)):
    for y in range(len(cube[0])):
        for x in range(len(cube[0][0])):
            # check up
            tf = f
            ty = y
            tx = x
            while True:
                if y - 1 < 0:
                    if f == 0:
                        tf = 1
                        ty = len(face_front) - 1






"""
        # up
        if y - 1 < 0 or board[y-1][x] == ' ':
            j = maxy
            while j > y:
                if board[j][x] == '#':
                    coordinates[(y, x)].append((y, x))
                    break
                if board[j][x] == '.':
                    coordinates[(y, x)].append((j, x))
                    break
                if board[j][x] == ' ':
                    j -= 1
        elif board[y-1][x] == '#':
            coordinates[(y, x)].append((y, x))
        else:
            coordinates[(y, x)].append((y-1, x))
"""