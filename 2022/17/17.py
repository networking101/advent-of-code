import time

with open("input2", "r") as fp:
    directions = [line.strip() for line in fp][0]

start_time = time.time()

b_size = 20000

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
        
print(f"Length of directions {len(directions)}")

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
    assert top-2 > 0
    for j in reversed(range(t-2, t+4)):
        if '#' not in board[j]:
            return j - 3

def solidify(pos, r_idx):
    y, x = pos
    rock = rocks[r_idx % len(rocks)]

    for j in range(len(rock)):
        for i in range(len(rock[0])):
            if rock[j][i] == '@':
                board[y+j][x+i] = '#'

def get_template(top):
    template = []
    for j in range(top + 4, top + 4 + 10):
        tmp = []
        for i in range(7):
            tmp.append(board[j][i])
        template.append(tmp)

    # for j in template:
    #     for i in j:
    #         print(i, end='')
    #     print()
    # print()

    return template

def check_template(template, top):
    for j in range(len(template)):
        for i in range(7):
            if template[j][i] != board[top + 4 + j][i]:
                return False
    return True

def copy_template(template):
    for j in range(10):
        for i in range(7):
            board[floor - (10 - j) + 1][i] = template[j][i]

    # print_board()



floor = b_size - 1
top = floor - 3
board = []
for i in range(b_size):
    board.append(['.'] * 7)

r_idx = 0
dir_idx = 0
rock_pos = (-1, -1)
search = False
template = []
print_all = False
print_resting = False
while True:
    # place rock
    if rock_pos == (-1, -1):
        if r_idx == 2023:
            print(f"Solution 1: {floor - find_top(top) - 5}")

        if r_idx == 1000000000000:
            print(f"Solution 2: {floor - find_top(top) - 5 + height_jump}")
            exit(0)

        # Template
        if r_idx == 2023:
        #if r_idx == 21:
            template = get_template(top)
            template_dir_idx = dir_idx
            template_r_idx = r_idx
            template_top = top
            search = True

        # place new piece
        rock_pos = (top - len(rocks[r_idx % len(rocks)]) + 1, 2)
        board_add(rock_pos, r_idx)
        if print_all:
            print_board()

        # move new piece laterally
        old_rock_pos = rock_pos
        move = directions[dir_idx % len(directions)]
        if move == "<":
            try:
                rock_pos = (top - len(rocks[r_idx % len(rocks)]) + 1, 1)
            except:
                print(f"Error:  {r_idx}, {dir_idx}")
                exit(0)
        else:
            try:
                rock_pos = (top - len(rocks[r_idx % len(rocks)]) + 1, 3)
            except:
                print(f"Error:  {r_idx}, {dir_idx}")
                exit(0)
        dir_idx += 1
        board_clear(old_rock_pos, r_idx)
        board_add(rock_pos, r_idx)
        if print_all:
            print_board()
    
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
        if print_all or print_resting:
            print_board()
        rock_pos = (-1, -1)
        top = find_top(top)
        r_idx = r_idx + 1
        if search:
            if check_template(template, top):
                t_height = floor - (template_top+3)
                cur_height = floor - (top+3)
                print(f"Template Height: {t_height}")
                print(template_r_idx, template_dir_idx)
                print(f"Next Height: {cur_height}")
                print(r_idx, dir_idx)
                diff_height = cur_height - t_height
                diff_rocks = r_idx - template_r_idx
                itterations = int((1000000000000 - cur_height) / diff_rocks)
                height_jump = itterations * diff_height
                print(f"Height jump: {height_jump}")
                print(f"Pickup: {(itterations * diff_rocks)}")
                # reset board
                board = []
                for i in range(b_size):
                    board.append(['.'] * 7)
                # copy template to board
                copy_template(template)
                r_idx = r_idx + (diff_rocks * (itterations + 1))
                tmp = 0
        continue

    if print_all:
        print_board()
        
    # mov rock sideways
    move = directions[dir_idx % len(directions)]
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

    if print_all:
        print_board()

    # We hit the floor
    if (len(rocks[r_idx % len(rocks)]) - 1) + rock_pos[0] == floor:
        solidify(rock_pos, r_idx)
        if print_all or print_resting:
            print_board()
        rock_pos = (-1, -1)
        top = find_top(top)
        r_idx = r_idx + 1