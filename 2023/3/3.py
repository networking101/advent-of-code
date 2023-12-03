with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

ysize = len(lines)
xsize = len(lines[0])

collection = []

grid = []
for line in lines:
    tmp = []
    for l in line:
        tmp.append(l)
    grid.append(tmp)

def getNum(y, x):
    xmin = x
    xmax = x
    number = []
    number.append(grid[y][x])
    if x-1 >= 0 and grid[y][x-1].isnumeric():
        number.insert(0, grid[y][x-1])
        xmin = x-1

        if x-2 >= 0 and grid[y][x-2].isnumeric():
            number.insert(0, grid[y][x-2])
            xmin = x-2

    if x+1 <=xsize and grid[y][x+1].isnumeric():
        number.append(grid[y][x+1])
        xmax = x+1

        if x+2 <=xsize and grid[y][x+2].isnumeric():
            number.append(grid[y][x+2])
            xmax = x+2

    num_int = int(''.join(number))

    if (xmin, xmax, y) not in (collection):
        # print(num_int)
        collection.append((xmin, xmax, y))

        return (int(num_int))
    return 0

def getNumStar(collection2, y, x):
    xmin = x
    xmax = x
    number = []
    number.append(grid[y][x])
    if x-1 >= 0 and grid[y][x-1].isnumeric():
        number.insert(0, grid[y][x-1])
        xmin = x-1

        if x-2 >= 0 and grid[y][x-2].isnumeric():
            number.insert(0, grid[y][x-2])
            xmin = x-2

    if x+1 <=xsize and grid[y][x+1].isnumeric():
        number.append(grid[y][x+1])
        xmax = x+1

        if x+2 <=xsize and grid[y][x+2].isnumeric():
            number.append(grid[y][x+2])
            xmax = x+2

    num_int = int(''.join(number))
    if (xmin, xmax, y) not in (collection2):
        # print(num_int)
        # print(xmin, xmax)
        collection2.append((xmin, xmax, y))

        return(int(num_int))
    
    return -1


tot = 0
tot2 = 0

for j, row in enumerate(grid):
    for i, c in enumerate(row):
        tot_list = []
        if c != '.' and not c.isnumeric():
            if grid[j-1][i-1].isnumeric():
                tot += getNum(j-1, i-1)
            if grid[j-1][i].isnumeric():
                tot += getNum(j-1, i)
            if grid[j-1][i+1].isnumeric():
                tot += getNum(j-1, i+1)
            if grid[j][i-1].isnumeric():
                tot += getNum(j, i-1)
            if grid[j][i+1].isnumeric():
                tot += getNum(j, i+1)
            if grid[j+1][i-1].isnumeric():
                tot += getNum(j+1, i-1)
            if grid[j+1][i].isnumeric():
                tot += getNum(j+1, i)
            if grid[j+1][i+1].isnumeric():
                tot += getNum(j+1, i+1)

        tot_list = []
        if c == '*':
            c2 = []
            if grid[j-1][i-1].isnumeric():
                t = getNumStar(c2, j-1, i-1)
                if t > 0:
                    tot_list.append(t)
            if grid[j-1][i].isnumeric():
                t = getNumStar(c2, j-1, i)
                if t > 0:
                    tot_list.append(t)
            if grid[j-1][i+1].isnumeric():
                t = getNumStar(c2, j-1, i+1)
                if t > 0:
                    tot_list.append(t)
            if grid[j][i-1].isnumeric():
                t = getNumStar(c2, j, i-1)
                if t > 0:
                    tot_list.append(t)
            if grid[j][i+1].isnumeric():
                t = getNumStar(c2, j, i+1)
                if t > 0:
                    tot_list.append(t)
            if grid[j+1][i-1].isnumeric():
                t = getNumStar(c2, j+1, i-1)
                if t > 0:
                    tot_list.append(t)
            if grid[j+1][i].isnumeric():
                t = getNumStar(c2, j+1, i)
                if t > 0:
                    tot_list.append(t)
            if grid[j+1][i+1].isnumeric():
                t = getNumStar(c2, j+1, i+1)
                if t > 0:
                    tot_list.append(t)
        
            if len(tot_list) == 2:
                tmp = 1
                # print(tot_list)
                for i in tot_list:
                    tmp *= i
                tot2 += tmp
            

print(tot)
print(tot2)