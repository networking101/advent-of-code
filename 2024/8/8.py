with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[x for x in y] for y in lines]

y_max = len(grid) - 1
x_max = len(grid[0]) - 1

antennas = {}
antinodes_silver = []
antinodes_gold = []

for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x != '.':
            if x not in antennas:
                antennas[x] = [(j, i)]
            else:
                antennas[x].append((j, i))

for k, v in antennas.items():
    for j, a in enumerate(v):
        for i, b in enumerate(v):
            if j == i:
                continue
            
            y1, x1 = a
            y2, x2 = b

            if (y1, x1) not in antinodes_gold:
                antinodes_gold.append((y1, x1))
            if (y2, x2) not in antinodes_gold:
                antinodes_gold.append((y2, x2))

            dx = x2 - x1
            dy = y2 - y1

            # check first
            i = 0
            while True:
                y1 = y1 - dy
                x1 = x1 - dx
                if y1 >= 0 and y1 <= y_max and x1 >= 0 and x1 <= x_max:
                    if (y1, x1) not in antinodes_silver and i == 0:
                        antinodes_silver.append((y1, x1))
                    if (y1, x1) not in antinodes_gold:
                        antinodes_gold.append((y1, x1))
                else:
                    break
                i += 1

            # check second
            i = 0
            while True:
                y2 = y2 + dy
                x2 = x2 + dx
                if y2 >= 0 and y2 <= y_max and x2 >= 0 and x2 <= x_max:
                    if (y2, x2) not in antinodes_silver and i == 0:
                        antinodes_silver.append((y2, x2))
                    if (y2, x2) not in antinodes_gold:
                        antinodes_gold.append((y2, x2))
                else:
                    break
                i += 1

print(len(antinodes_silver))
print(len(antinodes_gold))