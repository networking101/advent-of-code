with open("input", "r") as fp:
    lines = [line.replace('\n', '') for line in fp]

grid = []
op = []

for i, line in enumerate(lines):
    if i == (len(lines) - 1):
        for c in line.split():
            op.append(c)
    elif i == 0:
        for c in line.split():
            grid.append([int(c)])
    else:
        for j, c in enumerate(line.split()):
            grid[j].append(int(c))

silver = 0
for i, g in enumerate(grid):
    if op[i] == '+':
        silver += sum(g)
    else:
        tmp = 1
        for c in g:
            tmp *= c
        silver += tmp

print(silver)

grid2 = {}
gold = 0
for i, line in enumerate(lines):
    if i == 0:
        for j, c in enumerate(line):
            grid2[j] = [c]
    elif i == (len(lines) - 1):
        continue
    else:
        for j, c in enumerate(line):
            grid2[j].append(c)

gold_grid = []
tmp = []
for k, v in grid2.items():
    if set(v) == {' '}:
        gold_grid.append(tmp)
        tmp = []
    else:
        num = int(''.join(v).strip())
        tmp.append(num)
gold_grid.append(tmp)

gold = 0
for i, g in enumerate(gold_grid):
    if op[i] == '+':
        gold += sum(g)
    else:
        tmp = 1
        for c in g:
            tmp *= c
        gold += tmp

print(gold)