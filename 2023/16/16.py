with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[z for z in line] for line in lines]

yrange = range(len(grid))
xrange = range(len(grid[0]))

count2 = []
for j in range(-1, max(yrange) + 2):
    for i in range(-1, max(xrange) + 2):
        if (j in yrange and i in xrange) or (j not in yrange and i not in xrange):
            continue
        
        if j == -1:
            queue = [[j, i, 2]]
        elif j == max(yrange) + 1:
            queue = [[j, i, 0]]
        elif i == -1:
            queue = [[j, i, 1]]
        elif i == max(xrange) + 1:
            queue = [[j, i, 3]]
        else:
            assert False

        traveled = []
        while queue:
            y, x, d = queue.pop(0)

            if [y, x, d] in traveled:
                continue
            if x in xrange and y in yrange:
                traveled.append([y, x, d])

            # move up
            if d == 0 and x in xrange and y-1 in yrange:
                y -= 1
                if grid[y][x] == '-':
                    queue.append([y, x, 1])
                    queue.append([y, x, 3])
                if grid[y][x] == '\\':
                    queue.append([y, x, 3])
                if grid[y][x] == '/':
                    queue.append([y, x, 1])
                if grid[y][x] == '.' or grid[y][x] == '|':
                    queue.append([y, x, 0])
            # move right
            if d == 1 and x+1 in xrange and y in yrange:
                x += 1
                if grid[y][x] == '|':
                    queue.append([y, x, 0])
                    queue.append([y, x, 2])
                if grid[y][x] == '\\':
                    queue.append([y, x, 2])
                if grid[y][x] == '/':
                    queue.append([y, x, 0])
                if grid[y][x] == '.' or grid[y][x] == '-':
                    queue.append([y, x, 1])
            # move down
            if d == 2 and x in xrange and y+1 in yrange:
                y += 1
                if grid[y][x] == '-':
                    queue.append([y, x, 1])
                    queue.append([y, x, 3])
                if grid[y][x] == '\\':
                    queue.append([y, x, 1])
                if grid[y][x] == '/':
                    queue.append([y, x, 3])
                if grid[y][x] == '.' or grid[y][x] == '|':
                    queue.append([y, x, 2])
            # move left
            if d == 3 and x-1 in xrange and y in yrange:
                x -= 1
                if grid[y][x] == '|':
                    queue.append([y, x, 0])
                    queue.append([y, x, 2])
                if grid[y][x] == '\\':
                    queue.append([y, x, 0])
                if grid[y][x] == '/':
                    queue.append([y, x, 2])
                if grid[y][x] == '.' or grid[y][x] == '-':
                    queue.append([y, x, 3])

        found = []
        tmp_count = 0
        for t in traveled:
            y, x, _ = t
            if [y, x] not in found:
                tmp_count += 1
                found.append([y, x])
        count2.append(tmp_count)
        if j == 0 and i == -1:
            print(tmp_count)

print(max(count2))