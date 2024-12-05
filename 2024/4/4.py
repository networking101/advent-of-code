with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

y_size = len(lines)
x_size = len(lines[0])

grid = [[x for x in y] for y in lines]

coords = [[-4,1], [-4,4], [1,4], [4,4], [4,1], [4,-4], [1,-4], [-4,-4]]
XMAS = "XMAS"

def check_x_mas(y, x):
    if y-1 < 0 or x-1 < 0 or y+1 >= y_size or x+1 >= x_size:
        return False
    
    corners = [grid[y-1][x-1], grid[y-1][x+1], grid[y+1][x-1], grid[y+1][x+1]]

    if corners.count('M') == 2 and corners.count('S') == 2 and grid[y-1][x-1] != grid[y+1][x+1]:
        return True
    
    return False

def check_xmas(y_start, x_start, y_end, x_end):
    if y_end < -1 or x_end < -1 or y_end > y_size or x_end > x_size:
        return False
    
    if y_end < y_start:
        y_range = list(range(y_start, y_end, -1))
    else:
        y_range = list(range(y_start, y_end))
    if x_end < x_start:
        x_range = list(range(x_start, x_end, -1))
    else:
        x_range = list(range(x_start, x_end))

    for i in range(4):
        if len(y_range) == 1:
            y = y_range[0]
        else:
            y = y_range[i]
        if len(x_range) == 1:
            x = x_range[0]
        else:
            x = x_range[i]

        if grid[y][x] != XMAS[i]:
            return False

    return True

silver = 0
gold = 0

for j, row in enumerate(grid):
    for i, c in enumerate(row):
        if c == "X":
            for ny, nx in coords:
                if check_xmas(j, i, j+ny, i+nx):
                    silver += 1
        if c == "A":
            if check_x_mas(j, i):
                gold += 1

print(silver)
print(gold)