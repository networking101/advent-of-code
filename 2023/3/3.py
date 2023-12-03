with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

y_max = len(lines)
x_max = len(lines[0])

grid = []
numbers = []

for line in lines:
    tmp = []
    for col in line:
        tmp.append(col)
    grid.append(tmp)

for y, row in enumerate(grid):
    part_num = ''
    xmin = -1
    for x, c in enumerate(row):
        if c.isnumeric():
            if part_num == '':
                xmin = x
            part_num += c
            if x == x_max - 1 or not grid[y][x+1].isnumeric():
                numbers.append((int(part_num), xmin, x, y))
                part_num = ''
                xmin = -1

gears = {}

def checkSymbol(y, x, part_num):
    if x < 0 or y < 0 or x >= x_max or y >= y_max:
        return False
    
    if grid[y][x].isnumeric() or grid[y][x] == '.':
        return False
    
    if grid[y][x] == '*':
        if (y, x) not in gears:
            gears[(y, x)] = [part_num]
        else:
            gears[(y, x)].append(part_num)

    return True

count1 = 0
count2 = 0
symbol = False
for n in numbers:
    part_num, xminval, xmaxval, y = n
    for x in range(xminval, xmaxval+1):
        if checkSymbol(y-1, x, part_num) or checkSymbol(y+1, x, part_num):
            symbol = True

        if x == xminval:
            if checkSymbol(y-1, x-1, part_num) or checkSymbol(y, x-1, part_num) or checkSymbol(y+1, x-1, part_num):
                symbol = True
        
        if x == xmaxval:
            if checkSymbol(y-1, x+1, part_num) or checkSymbol(y, x+1, part_num) or checkSymbol(y+1, x+1, part_num):
                symbol = True
        
    if symbol:
        count1 += part_num

    symbol = False

print(count1)

for k, g in gears.items():
    if len(g) == 2:
        count2 += g[0] * g[1]

print(count2)