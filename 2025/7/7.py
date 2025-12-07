with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

y_dirs = [0, -1, -1, -1, 0, 1, 1, 1]
x_dirs = [1, 1, 0, -1, -1, -1, 0, 1]

grid = [list(line) for line in lines]

y_pos = 0
x_pos = 0

for i, x in enumerate(grid[0]):
    if x == 'S':
        x_pos = i

silver = 0
for j, y in enumerate(grid[0:]):
    if j == 0:
        continue
    for i, x in enumerate(y):
        if x == '.':
            if grid[j-1][i] == '|' or grid[j-1][i] == 'S':
                grid[j][i] = '|'
        if x == '^':
            if grid[j-1][i] == '|' or grid[j-1][i] == 'S':
                silver += 1
                grid[j][i - 1] = '|'
                grid[j][i + 1] = '|'

print(silver)

gold_counts = {}
for i in range(len(grid[0])):
    gold_counts[i] = 0

for j, y in enumerate(grid[0:]):
    if j == 0:
        gold_counts[x_pos] = 1
    for i, x in enumerate(y):
        if x == '.':
            continue
        if x == '^':
            if i - 1 >= 0:
                gold_counts[i-1] += gold_counts[i]
            if i + 1 < len(grid[0]):
                gold_counts[i+1] += gold_counts[i]
            gold_counts[i] = 0

gold = 0
for k, v in gold_counts.items():
    gold += v

print(gold)