from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

blank_grid = []
blizzard_dict = {}
blizzard = {}
for j, y in enumerate(lines):
    row = []
    blank_row = []
    for i, x in enumerate(y):
        if x == ">" or x == "<" or x == "^" or x == "v":
            blizzard[(j, i)] = [x]
            blank_row.append('.')
        else:
            blank_row.append(x)
    blank_grid.append(blank_row)
blizzard_dict[0] = blizzard

grid_size = (len(blank_grid) - 2) * (len(blank_grid[0]) - 2)

def print_grid(b=None, pos=None):
    printable_grid = deepcopy(blank_grid)

    if b != None:
        for (y, x), v in b.items():
            if len(v) > 1:
                printable_grid[y][x] = str(len(v))
            else:
                printable_grid[y][x] = v[0]

    for j, y in enumerate(printable_grid):
        for i, x in enumerate(y):
            if pos != None and pos[0] == j and pos[1] == i:
                assert printable_grid[j][i] == '.'
                print('E', end='')
            else:
                print(x, end='')
        print()
    print()

def move_blizzard(b):
    new_blizzard = {}
    for (y, x), vals in b.items():
        for v in vals:
            if v == 'v':
                if y+1 == len(blank_grid)-1:
                    next_pos = (1, x)
                else:
                    next_pos = (y+1, x)
                if next_pos in new_blizzard:
                    new_blizzard[next_pos].append('v')
                else:
                    new_blizzard[next_pos] = ['v']
            if v == '>':
                if x+1 == len(blank_grid[0])-1:
                    next_pos = (y, 1)
                else:
                    next_pos = (y, x+1)
                if next_pos in new_blizzard:
                    new_blizzard[next_pos].append('>')
                else:
                    new_blizzard[next_pos] = ['>']
            if v == '<':
                if x-1 == 0:
                    next_pos = (y, len(blank_grid[0]) - 2)
                else:
                    next_pos = (y, x-1)
                if next_pos in new_blizzard:
                    new_blizzard[next_pos].append('<')
                else:
                    new_blizzard[next_pos] = ['<']
            if v == '^':
                if y-1 == 0:
                    next_pos = (len(blank_grid) - 2, x)
                else:
                    next_pos = (y-1, x)
                if next_pos in new_blizzard:
                    new_blizzard[next_pos].append('^')
                else:
                    new_blizzard[next_pos] = ['^']
    return new_blizzard


# first itteration is forward and back
# second itteration is forward the second time
step = 0
curr_step = step
for z in range(2):
    # Go forward
    start = (0, 1)
    ending = (len(blank_grid)-1, len(blank_grid[0]) - 2)
    # position, time, grid
    queue = [(start, step)]
    DP = []
    while queue:

        pos, step = queue.pop(0)
        y, x = pos

        # if we have been in this position with the blizzard in this configuration, we don't need to check again
        key = str(pos) + str(step % grid_size)
        if key in DP:
            continue
        else:
            DP.append(key)

        # if we are at finishing location, we are done
        if pos == ending:
            print(step)
            break

        step += 1

        # move blizzard
        if step % grid_size not in blizzard_dict:
            # update blizzard positions
            blizzard = move_blizzard(blizzard_dict[(step-1) % grid_size])
            blizzard_dict[step % grid_size] = blizzard
        else:
            blizzard = blizzard_dict[step % grid_size]

        # move position
        # if we are at starting location, only move down or stay
        if pos == start:
            if (y+1, x) not in blizzard:
                queue.append(((y+1, x), step))
            else:
                queue.append((start, step))
            continue

        # check each direction and append if open
        # check up
        if (y-1, x) not in blizzard and blank_grid[y-1][x] != '#':
            queue.append(((y-1, x), step))
        # check right
        if (y, x+1) not in blizzard and blank_grid[y][x+1] != '#':
            queue.append(((y, x+1), step))
        # check down
        if (y+1, x) not in blizzard and blank_grid[y+1][x] != '#':
            queue.append(((y+1, x), step))
        # check left
        if (y, x-1) not in blizzard and blank_grid[y][x-1] != '#':
            queue.append(((y, x-1), step))
        # stay
        if (y, x) not in blizzard:
            queue.append(((y, x), step))

    if z == 1:
        break

    # Go back
    curr_step = 0
    ending = (0, 1)
    start = (len(blank_grid)-1, len(blank_grid[0]) - 2)
    # position, time, grid
    queue = [(start, step)]
    DP = []
    while queue:

        pos, step = queue.pop(0)
        y, x = pos

        # if we have been in this position with the blizzard in this configuration, we don't need to check again
        key = str(pos) + str(step % grid_size)
        if key in DP:
            continue
        else:
            DP.append(key)

        # if we are at finishing location, we are done
        if pos == ending:
            break

        step += 1

        # move blizzard
        if step % grid_size not in blizzard_dict:
            # update blizzard positions
            blizzard = move_blizzard(blizzard_dict[(step-1) % grid_size])
            blizzard_dict[step % grid_size] = blizzard
        else:
            blizzard = blizzard_dict[step % grid_size]

        # move position
        # if we are at starting location, only move down or stay
        if pos == start:
            if (y-1, x) not in blizzard:
                queue.append(((y-1, x), step))
            else:
                queue.append((start, step))
            continue

        # check each direction and append if open
        # check up
        if (y-1, x) not in blizzard and blank_grid[y-1][x] != '#':
            queue.append(((y-1, x), step))
        # check right
        if (y, x+1) not in blizzard and blank_grid[y][x+1] != '#':
            queue.append(((y, x+1), step))
        # check down
        if (y+1, x) not in blizzard and blank_grid[y+1][x] != '#':
            queue.append(((y+1, x), step))
        # check left
        if (y, x-1) not in blizzard and blank_grid[y][x-1] != '#':
            queue.append(((y, x-1), step))
        if (y, x) not in blizzard:
            queue.append(((y, x), step))