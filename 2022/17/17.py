with open("input", "r") as fp:
    lines = [line.strip() for line in fp][0]

b_size = 5000

rocks = [[['@','@','@','@']],\

        [['.','@','.'],\
        ['@','@','@'],\
        ['.','@','.']],\

        [['.','.','@'],\
        ['.','.','@'],\
        ['@','@','@']],\
        
        [['@'],\
        ['@'],\
        ['@'],\
        ['@']],\
        
        [['@','@'],\
        ['@','@']]]
rock_size = [(1, 4), (3, 3), (3, 3), (4, 1), (2, 2)]

def print_board():
    found_piece = False
    for i, b in enumerate(board):
        if ("#" not in b and "@" not in b) and not found_piece:
            continue
        found_piece = True
        print("|", end="")
        for a in b:
            print(a, end="")
        print("|", end="\n")
    print("+-------+")
    print()

def board_clear(pos, r_idx):
    y, x = pos
    rock = rocks[r_idx % len(rocks)]

    for j in range(len(rock)):
        for i in range(len(rock[0])):
            if rock[j][i] == '@':
                board[y+j][x+i] = '.'

def board_add(pos, r_idx):
    y, x = pos
    rock = rocks[r_idx % len(rocks)]

    for j in range(len(rock)):
        for i in range(len(rock[0])):
            if rock[j][i] == '@':
                board[y+j][x+i] = '@'

floor = b_size - 1
top = floor - 3
board = []
for i in range(b_size):
    board.append(['.'] * 7)

def check_overlap(pos, r_idx):
    y, x = pos
    rock = rocks[r_idx % len(rocks)]

    if x < 0:
        return False
    if x + len(rocks[r_idx % len(rocks)][0])-1 > 6:
        return False

    for j in range(len(rock)):
        for i in range(len(rock[0])):
            if board[y+j][x+i] == '#' and rock[j][i] == '@':
                return False
    return True

def find_top(t):
    for j in reversed(range(t, floor+1)):
        if '#' not in board[j] and '@' not in board[j]:
            return j - 3

    tmp = 0
    return

def solidify(pos, r_idx):
    y, x = pos
    rock = rocks[r_idx % len(rocks)]

    for j in range(len(rock)):
        for i in range(len(rock[0])):
            if rock[j][i] == '@':
                board[y+j][x+i] = '#'


r_idx = 0
dir_idx = 0
rock_pos = (-1, -1)
while True:
    # place rock
    if rock_pos == (-1, -1):
        if r_idx == 2023:
            print(b_size - find_top(top-2) - 6)
        move = lines[dir_idx % len(lines)]
        if move == "<":
            rock_pos = (top - len(rocks[r_idx % len(rocks)]) + 1, 1)
        else:
            rock_pos = (top - len(rocks[r_idx % len(rocks)]) + 1, 3)
        dir_idx += 1
        board_add(rock_pos, r_idx)
        # print("Place and lateral")
        # print_board()
    
    # mov rock down
    n_rock_pos = (rock_pos[0]+1, rock_pos[1])
    old_rock_pos = rock_pos
    if check_overlap(n_rock_pos, r_idx):
        rock_pos = n_rock_pos
        board_clear(old_rock_pos, r_idx)
        board_add(rock_pos, r_idx)
    else:
        # We came to rest on another piece
        solidify(rock_pos, r_idx)
        #print_board()
        rock_pos = (-1, -1)
        top = find_top(top-2)
        #print(b_size - top - 4)
        r_idx = r_idx + 1
        continue

    # print("Down")
    # print_board()
        
    # mov rock sideways
    move = lines[dir_idx % len(lines)]
    if move == "<":
        n_rock_pos = (rock_pos[0], rock_pos[1]-1)
    else:
        n_rock_pos = (rock_pos[0], rock_pos[1]+1)
    dir_idx += 1
    old_rock_pos = rock_pos
    if check_overlap(n_rock_pos, r_idx):
        rock_pos = n_rock_pos
        board_clear(old_rock_pos, r_idx)
        board_add(rock_pos, r_idx)

    # print("Lateral")
    # print_board()

    # We hit the floor
    if (len(rocks[r_idx % len(rocks)]) - 1) + rock_pos[0] == floor:
        solidify(rock_pos, r_idx)
        #print_board()
        rock_pos = (-1, -1)
        top = find_top(top-2)
        r_idx = r_idx + 1