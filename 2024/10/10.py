with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[int(x) for x in y] for y in lines]

y_max = len(grid) - 1
x_max = len(grid[0]) - 1

zeros = []

for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x == 0:
            zeros.append((j, i))

position_deltas = [(-1,0), (0,1), (1,0), (0,-1)]

def recurse(curr_pos, nines):
    y, x = curr_pos
    curr_val = grid[y][x]

    if curr_val == 9:
        s = 0
        if (y, x) not in nines:
            nines.append((y, x))
            s = 1
        return (s, 1)
    
    next_val = curr_val + 1

    ret_val = (0, 0)
    for dy, dx in position_deltas:
        ny = y + dy
        nx = x + dx
        if ny >= 0 and ny <= y_max and nx >= 0 and nx <= x_max and grid[ny][nx] == next_val:
            s, g = recurse((ny, nx), nines)
            ret_val = (s + ret_val[0], g + ret_val[1])

    return ret_val

silver = 0
gold = 0
for z in zeros:
    s, g = recurse(z, [])
    silver += s
    gold += g

print(silver)
print(gold)