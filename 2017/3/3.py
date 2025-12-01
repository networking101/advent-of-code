with open("input", "r") as fp:
    puzzle_input = [int(line.strip()) for line in fp][0]

grid_size = 1000
start = int(grid_size / 2) - 1

y_coords = [0, -1, 0, 1]
x_coords = [1, 0, -1, 0]


def fill_grid_gold(g, y, x):
    neighbor_sum = 0
    y_neighbors = [0, -1, -1, -1, 0, 1, 1, 1]
    x_neighbors = [1, 1, 0, -1, -1, -1, 0, 1]

    for dy, dx in zip(y_neighbors, x_neighbors):
        neighbor_sum += g[y + dy][x + dx]
    
    return neighbor_sum

y = start
x = start
grid_silver = [[0 for j in range(grid_size)] for i in range(grid_size)]
grid_gold = [[0 for j in range(grid_size)] for i in range(grid_size)]

size = 1
curr_direction = 0
gold_found = 1
for i in range(1, puzzle_input + 1):
    if i == 1:
        grid_gold[y][x] = 1
    else:
        grid_gold[y][x] = fill_grid_gold(grid_gold, y, x)
        if grid_gold[y][x] > puzzle_input and gold_found:
            print(f"Gold: {grid_gold[y][x]}")
            gold_found = 0
    grid_silver[y][x] = i

    new_y = y + y_coords[curr_direction]
    new_x = x + x_coords[curr_direction]

    
    if abs(new_x - start) >= size or abs(new_y - start) >= size:
        curr_direction = (curr_direction + 1) % 4
        # we need to expand the border
        if curr_direction == 1:
            size += 1
        else: # we went outside the boundary but are not ready to expand the border
            new_y = y + y_coords[curr_direction]
            new_x = x + x_coords[curr_direction]

    old_y = y
    old_x = x
    y = new_y
    x = new_x

print(f"Silver: {abs(old_y - start) + abs(old_x - start)}")