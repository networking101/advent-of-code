with open("input2", "r") as fp:
    lines = [line.strip() for line in fp][0]

b_size = 10

rocks = [['#','#','#','#'],\

        [['.','#','.'],\
        ['#','#','#'],\
        ['.','#','.']],\

        [['.','.','#'],\
        ['.','.','#'],\
        ['#','#','#']],\
        
        [['#'],\
        ['#'],\
        ['#'],\
        ['#']],\
        
        [['#','#'],\
        ['#','#']]]
rock_size = [(1, 4), (3, 3), (3, 3), (4, 1), (2, 2)]

def print_board():
    for i, b in enumerate(board):
        if "#" not in b:
            continue
        print("|", end="")
        for a in b:
            print(a, end="")
        print("|", end="\n")
    print("+-------+")
    print()

def board_add(pos, r_idx):
    y, x = pos
    rock = rocks[r_idx]

    for j in range(len(rock)):
        for i in range(len(rock[0])):
            if rock[j][i] == '#':
                board[y+j][x+i] == '#'

floor = b_size - 1
top = floor - 3
board = []
for i in range(b_size):
    board.append(['.'] * 7)

print_board()

def check_overlap(pos, r_idx):
    y, x = pos
    rock = rocks[r_idx]

    for j in range(len(rock)):
        for i in range(len(rock[0])):
            if board[y+j][x+i] == '#' and rock[j][i] == '#':
                return False

    return True

r_idx = 0
dir_idx = 0
rock_pos = (-1, -1)
while True:
    # place rock
    if rock_pos == (-1, -1):
        move = lines[dir_idx]
        if move == "<":
            rock_pos = (top - len(rocks[r_idx]), 1)
        else:
            rock_pos = (top - len(rocks[r_idx]), 3)
        dir_idx += 1
    
    # mov rock down
    n_rock_pos = (rock_pos[0]+1, rock_pos[1])
    if check_overlap(n_rock_pos, r_idx):
        rock_pos = n_rock_pos
    else:
        continue

    board_add(rock_pos, r_idx)
    print_board()
        
    # mov rock sideways
    move = lines[dir_idx]
    if move == "<":
        n_rock_pos = (rock_pos[0], rock_pos[1]-1)
    else:
        n_rock_pos = (rock_pos[0], rock_pos[1]+1)
    dir_idx += 1
    if check_overlap(n_rock_pos, r_idx):
        rock_pos = n_rock_pos

    board_add(rock_pos, r_idx)
    print_board()
    break