from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[x for x in y] for y in lines]

y_max = len(grid) - 1
x_max = len(grid[0]) - 1

for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x == '^':
            coord = (j, i)
            direction = 0

start = coord
gold = 0

visited = []
visited2 = []
orientation = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def next_pos(grid, direction, coord):
    sy, sx = orientation[direction]
    ny = coord[0] + sy
    nx = coord[1] + sx

    if ny < 0 or ny > y_max or nx < 0 or nx > x_max:
        return None
    
    # if we are blocked, stay in same position and rotate right 90 degrees
    if grid[ny][nx] == '#':
        direction = (direction + 1) % 4
        ny = coord[0]
        nx = coord[1]
        
    return (direction, (ny, nx))

while True:
    if coord not in visited:
        visited.append(coord)
    if (direction, coord) not in visited2:
        visited2.append((direction, coord))

    res = next_pos(grid, direction, coord)

    if res is None:
        break

    new_direction, new_coord = res
    ny, nx = new_coord

    # check for loop
    if new_coord != coord and grid[ny][nx] != '#' and new_coord not in visited and new_coord != start:
        loop_grid = deepcopy(grid)
        loop_grid[ny][nx] = '#'
        new_visited2 = deepcopy(visited2)
        loop_direction = direction
        loop_coord = coord
        new_visited2.append((loop_direction, loop_coord))
        while True:
            res = next_pos(loop_grid, loop_direction, loop_coord)

            if res is None:
                break

            new_loop_direction, new_loop_coord = res
            n_loop_y, n_loop_x = new_loop_coord

            if (new_loop_direction, new_loop_coord) in new_visited2:
                gold += 1
                break

            new_visited2.append((new_loop_direction, new_loop_coord))

            loop_direction = new_loop_direction
            loop_coord = new_loop_coord

    direction = new_direction
    coord = new_coord

print(len(visited))
print(gold)