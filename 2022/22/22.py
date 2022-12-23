import numpy as np
from copy import deepcopy

with open("input2", "r") as fp:
    lines = [line.rstrip() for line in fp]

def print_board(pos=None, face=None):
    for j, y in enumerate(cube[pos[0]]):
        for i, x in enumerate(y):
            if pos and face and pos[1] == j and pos[2] == i:
                if face == 0:
                    print('^', end='')
                if face == 1:
                    print('>', end='')
                if face == 2:
                    print('v', end='')
                if face == 3:
                    print('<', end='')
            else:
                print(x, end='')
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

orig_distances = deepcopy(distances)
orig_directions = deepcopy(directions)

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
        if d == 'R':
            facing = (facing + 1) % 4
        else:
            facing = (facing - 1) % 4

print((pos[0]+1) * 1000 + (pos[1]+1) * 4 + (facing-1) % 4)

# # create board and paths
# board = []
# path = ""
# b = True
# maxx = 0
# for l in lines:
#     if not l:
#         b = False
#     elif b:
#         if (len(l)-1) > maxx:
#             maxx = len(l)-1
#         board.append(list(l))
#     else:
#         path = l
# maxy = len(board)-1

# # pad right
# for i, y in enumerate(board):
#     board[i] = y + [' '] * (maxx - len(y) + 1)


# Part 2
# example
distances = orig_distances
directions = orig_directions

c_size = 4
face_front = []
face_bottom = []
face_top = []
face_back = []
face_left = []
face_right = []
# for y in range(c_size):
#     face_front.append([''] * c_size)
#     face_bottom.append([''] * c_size)
#     face_top.append([''] * c_size)
#     face_back.append([''] * c_size)
#     face_left.append([''] * c_size)
#     face_right.append([''] * c_size)

for y in range(c_size):
    face_front.append([''] * c_size)
    face_bottom.append([''] * c_size)
    face_top.append([''] * c_size)
    face_back.append([''] * c_size)
    face_left.append([''] * c_size)
    face_right.append([''] * c_size)
    for x in range(c_size):
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
# c_size = 50
# TODO

def check_up(f, y, x):
    lf = f
    ly = y
    lx = x
    if y < 0:
        if f == 0:
            tf = 1
            ty = c_size - 1
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 1:
            tf = 5
            ty = c_size - 1
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 2:
            tf = 0
            ty = c_size - 1
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 3:
            tf = 1
            ty = lx
            tx = 0
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 4:
            tf = 1
            ty = c_size - (lx + 1)
            tx = c_size - 1
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 5:
            tf = 2
            ty = c_size
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
    return (lf, ly - 1, lx)

def check_down(f, y, x):
    lf = f
    ly = y
    lx = x
    if y > c_size - 1:
        if f == 0:
            tf = 2
            ty = 0
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 1:
            tf = 0
            ty = 0
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 2:
            tf = 5
            ty = 0
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 3:
            tf = 2
            ty = c_size - (lx + 1)
            tx = 0
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 4:
            tf = 2
            ty = c_size - (lx + 1)
            tx = c_size - 1
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 5:
            tf = 1
            ty = 0
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
    return (lf, ly + 1, lx)

def check_right(f, y, x):
    lf = f
    ly = y
    lx = x
    if x > c_size - 1:
        if f == 0:
            tf = 4
            ty = ly
            tx = 0 
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 1:
            tf = 4
            ty = 0
            tx = c_size - (ly + 1)
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 2:
            tf = 4
            ty = c_size - 1
            tx = ly
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 3:
            tf = 0
            ty = ly
            tx = 0
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 4:
            tf = 5
            ty = c_size - (ly + 1)
            tx = c_size - 1
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 5:
            tf = 4
            ty = c_size - (ty + 1)
            tx = c_size - 1
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
    return (lf, ly, lx + 1)

def check_left(f, y, x):
    lf = f
    ly = y
    lx = x
    if x > c_size - 1:
        if f == 0:
            tf = 3
            ty = ly
            tx = c_size - 1
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 1:
            tf = 3
            ty = 0
            tx = ly
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 2:
            tf = 3
            ty = c_size - 1
            tx = c_size - (ly + 1)
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 3:
            tf = 5
            ty = c_size - (ly + 1)
            tx = 0
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 4:
            tf = 0
            ty = c_size - 1
            tx = lx
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
        if f == 5:
            tf = 3
            ty = c_size - (ly + 1)
            tx = 0
            if cube[tf][ty][tx] == '#':
                return (lf, ly, lx)
            return (tf, ty, tx)
    return (lf, ly, lx - 1)

def change_direction(src, dst):
    print(f"Change direction {(src, dst)}")
    if src == 0:
        if dst == 1:
            return 0
        if dst == 4:
            return 1
        if dst == 2:
            return 2
        if dst == 3:
            return 3
    if src == 1:
        if dst == 5:
            return 0
        if dst == 0:
            return 2
        if dst == 3:
            return 2
        if dst == 4:
            return 2
    if src == 2:
        if dst == 0:
            return 0
        if dst == 5:
            return 2
        if dst == 3:
            return 0
        if dst == 4:
            return 0
    if src == 5:
        if dst == 2:
            return 0
        if dst == 1:
            return 2
        if dst == 3:
            return 1
        if dst == 4:
            return 3
    if src == 3:
        if dst == 1:
            return 1
        if dst == 2:
            return 1
        if dst == 0:
            return 1
        if dst == 5:
            return 1
    if src == 4:
        if dst == 1:
            return 3
        if dst == 2:
            return 3
        if dst == 5:
            return 3
        if dst == 0:
            return 3
    raise Exception("Shouldn't get here")

# generate up, right, down, and left coordinates for each position on the cube
coordinates = {}
# f 0 = front
# f 1 = top
# f 2 = bottom
# f 3 = left
# f 4 = right
# f 5 = back
for f in range(len(cube)):
    for y in range(c_size):
        for x in range(c_size):
            coordinates[(f, y, x)] = []
            coordinates[(f, y, x)].append(check_up(f, y, x))
            coordinates[(f, y, x)].append(check_right(f, y, x))
            coordinates[(f, y, x)].append(check_down(f, y, x))
            coordinates[(f, y, x)].append(check_left(f, y, x))

# Move around board
# 0 = up
# 1 = right
# 2 = down
# 3 = left
facing = 1
pos = (0, 0, 0)
itteration = 0
while directions or distances:
    d = distances.pop(0)
    for _ in range(d):
        if facing == 0 and coordinates[pos][0] != pos:
            n_pos = coordinates[pos][0]
            if pos[0] != n_pos[0]:
                facing = change_direction(pos[0], n_pos[0])
        if facing == 1 and coordinates[pos][1] != pos:
            n_pos = coordinates[pos][1]
            if pos[0] != n_pos[0]:
                facing = change_direction(pos[0], n_pos[0])
        if facing == 2 and coordinates[pos][2] != pos:
            n_pos = coordinates[pos][2]
            if pos[0] != n_pos[0]:
                facing = change_direction(pos[0], n_pos[0])
        if facing == 3 and coordinates[pos][3] != pos:
            n_pos = coordinates[pos][3]
            if pos[0] != n_pos[0]:
                facing = change_direction(pos[0], n_pos[0])
                
        pos = n_pos
    
    print_board(pos, facing)
    if itteration == 0:
        exit(0)

    if directions:
        d = directions.pop(0)
        # print(d)
        if d == 'R':
            facing = (facing + 1) % 4
        else:
            facing = (facing - 1) % 4
    
    print_board(pos, facing)
    if itteration == 0:
        exit(0)
    itteration += 1

print(pos)
print((pos[0]+1) * 1000 + (pos[1]+1) * 4 + (facing-1) % 4)