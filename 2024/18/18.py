from copy import deepcopy

file_name = "input"

with open(file_name, "r") as fp:
    lines = [line.strip() for line in fp]

lines = [[int(x) for x in y.split(",")]for y in lines]

if file_name == "input":
    y_max = 70
    x_max = 70
    num_bytes = 1024
else:
    y_max = 6
    x_max = 6
    num_bytes = 12

grid = [['.' for x in range(x_max + 1)] for y in range(y_max + 1)]

for x, y in lines[:num_bytes]:
    grid[y][x] = '#'

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(grid):
    # (steps, y, x, path)
    queue = [(0, 0, 0, [])]
    grid[0][0] = 'O'
    while queue:
        steps, y, x, path = queue.pop(0)
        
        path.append((y, x))

        if y == y_max and x == x_max:
            return (steps, path)

        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if ny >= 0 and ny <= y_max and nx >= 0 and nx <= x_max:
                if grid[ny][nx] == '.':
                    grid[ny][nx] = 'O'
                    queue.append((steps + 1, ny, nx, deepcopy(path)))

    return None

steps, shortest_path = bfs(deepcopy(grid))
print(steps)

for x, y in lines[num_bytes:]:
    grid[y][x] = '#'
    # if (y, x) in shortest_pa
    if bfs(deepcopy(grid)) is None:
        print(str(x) + "," + str(y))
        break