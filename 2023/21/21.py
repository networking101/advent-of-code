from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

oggrid = [[z for z in line]for line in lines]
xrange = range(len(oggrid[0]))
yrange = range(len(oggrid))

open_count = 0
start = None
for j, y in enumerate(oggrid):
    for i, x in enumerate(y):
        if x == 'S':
            start = (j, i)
        if x != '#':
            open_count += 1

oggrid[start[0]][start[1]] = '.'

def calculate_steps(new_queue, needed_steps, step=0):
    step_collection = {}
    grid = deepcopy(oggrid)
    while step < needed_steps:
        step_collection[step] = deepcopy(new_queue)
        step += 1
        queue = new_queue
        new_queue = []
        while queue:
            y, x = queue.pop(0)
            grid[y][x] = '#'

            for dir, coord in enumerate([[-1, 0], [0, 1], [1, 0], [0,-1]]):
                yy = y + coord[0]
                xx = x + coord[1]

                if yy in yrange and xx in xrange and grid[yy][xx] != '#':
                    grid[yy][xx] = '#'
                    new_queue.append((yy, xx))

    step_collection[step] = deepcopy(new_queue)

    even_count = 0
    odd_count = 0
    for k, v in step_collection.items():
        if needed_steps%2 == 0:
            if k%2 == 0:
                even_count += len(v)
            else:
                odd_count += len(v)
        else:
            if k%2 == 0:
                odd_count += len(v)
            else:
                even_count += len(v)

    return (even_count, odd_count)

print(calculate_steps([start], 64, 0)[0])

count2 = 0
distance = 26501365
num_skip = (distance + 1 - len(oggrid)) // len(oggrid)

# get complete squares
even, odd = calculate_steps([start], len(oggrid) - 1, 0)

squares_count = [0, 0]
for i in range(1, num_skip + 1):
    if i % 2 == 1:           # add to even
        squares_count[0] += 4 * i
    else:                   # add to odd
        squares_count[1] += 4 * i
squares_count[1] += 1
count2 += squares_count[0] * even + squares_count[1] * odd

# get 4 corners
edge_steps = distance - len(oggrid)//2 - (num_skip * len(oggrid))
edges = [(0, xrange[-1]//2), (yrange[-1]//2, xrange[-1]), (yrange[-1], xrange[-1]//2), (yrange[-1]//2, 0)]
for edge in edges:
    res, _ = calculate_steps([edge], edge_steps, 1)
    count2 += res
if edge_steps > len(oggrid):
    for edge in edges:
        res, _ = calculate_steps([edge], edge_steps - len(oggrid), 1)
        count2 += res

# get cut squares
resout = 0
insize = (distance + 1) % len(oggrid)
insize += len(oggrid) - 2
outsize = insize % len(oggrid)
outer = num_skip + 1
inner = num_skip

corners = [(0, 0), (0, xrange[-1]), (yrange[-1], 0), (yrange[-1], xrange[-1])]
for corner in corners:
    resin, _ = calculate_steps([corner], insize, 0)
    if insize != outsize or insize - len(oggrid) + 2 != 0:
        resout, _ = calculate_steps([corner], outsize, 0)
    count2 += resin * inner
    count2 += resout * outer

print(count2)