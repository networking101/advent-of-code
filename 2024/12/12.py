with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[x for x in y] for y in lines]

y_max = len(grid) - 1
x_max = len(grid[0]) - 1

found = []
coords = [(-1, 0), (0, 1), (1, 0), (0, -1)]
side_coords = [(0, 1), (1, 0)]

def bfs(start):
    area = 1
    perimeter = 0
    perimeter_list = []
    queue = [start]
    found.append((start[0], start[1]))
    while queue:
        y, x = queue.pop(0)

        for dy, dx in coords:
            ny = y + dy
            nx = x + dx

            if ny < 0 or ny > y_max or nx < 0  or nx > x_max:
                perimeter += 1
                if ny != y and (0, ny, nx) not in perimeter_list:
                    perimeter_list.append((0, y, x, ny, nx))
                if nx != x and (1, ny, nx) not in perimeter_list:
                    perimeter_list.append((1, y, x, ny, nx))
            elif grid[ny][nx] != grid[start[0]][start[1]]:
                perimeter += 1
                if ny != y and (0, ny, nx) not in perimeter_list:
                    perimeter_list.append((0, y, x, ny, nx))
                if nx != x and (1, ny, nx) not in perimeter_list:
                    perimeter_list.append((1, y, x, ny, nx))
            elif (ny, nx) not in found:
                area += 1
                found.append((ny, nx))
                queue.append((ny, nx))

    # check sides
    sides = perimeter
    while perimeter_list:
        d, oy, ox, y, x = perimeter_list.pop(0)
        ny = y + side_coords[d][0]
        nx = x + side_coords[d][1]
        ony = oy + side_coords[d][0]
        onx = ox + side_coords[d][1]
        if (d, ony, onx, ny, nx) in perimeter_list:
            sides -= 1
        ny = y - side_coords[d][0]
        nx = x - side_coords[d][1]
        ony = oy - side_coords[d][0]
        onx = ox - side_coords[d][1]
        if (d, ony, onx, ny, nx) in perimeter_list:
            sides -= 1

    return (area * perimeter, area * sides)

silver = 0
gold = 0
for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if (j, i) not in found:
            s, g = bfs((j, i))
            silver += s
            gold += g

print(silver)
print(gold)