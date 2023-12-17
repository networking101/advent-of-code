import heapq

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[int(z) for z in line] for line in lines]

start = (0, 0)
end = (len(grid) - 1, len(grid[0]) - 1)
yrange = range(len(grid))
xrange = range(len(grid[0]))

# part 1
optimal = {}
count1 = []
queue = [(0, start[0], start[1], [0, 1])]
while queue:
    cost, y, x, direction = heapq.heappop(queue)
    if (y, x) == end:
        count1.append(cost)
        continue
    step, d = direction
    if (y, x, step, d) in optimal:
        continue
    optimal[(y, x, step, d)] = cost
    assert step < 4

    # check up
    ny = y - 1
    nx = x
    if ny in yrange and not (step == 3 and d == 0) and d != 2:
        if d == 0:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 0]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])

    # check right
    ny = y
    nx = x + 1
    if nx in xrange and not (step == 3 and d == 1) and d != 3:
        if d == 1:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 1]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])

    # check down
    ny = y + 1
    nx = x
    if ny in yrange and not (step == 3 and d == 2) and d != 0:
        if d == 2:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 2]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])

    # check left
    ny = y
    nx = x - 1
    if nx in xrange and not (step == 3 and d == 3) and d != 1:
        if d == 3:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 3]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])
print(min(count1))

# part 2
optimal = {}
count2 = []
queue = [(0, start[0], start[1], [0, 1])]
while queue:
    cost, y, x, direction = heapq.heappop(queue)
    if (y, x) == end:
        count2.append(cost)
        continue
    step, d = direction
    if (y, x, step, d) in optimal:
        continue
    optimal[(y, x, step, d)] = cost

    # check up
    ny = y - 1
    nx = x
    if ny in yrange and not (step == 10 and d == 0) and not (step < 4 and d != 0) and d != 2:
        if d == 0:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 0]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])

    # check right
    ny = y
    nx = x + 1
    if nx in xrange and not (step == 10 and d == 1) and not (step < 4 and d != 1) and d != 3:
        if d == 1:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 1]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])

    # check down
    ny = y + 1
    nx = x
    if ny in yrange and not (step == 10 and d == 2) and not (step < 4 and d != 2) and d != 0:
        if d == 2:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 2]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])

    # check left
    ny = y
    nx = x - 1
    if nx in xrange and not (step == 10 and d == 3) and not (step < 4 and d != 3) and d != 1:
        if d == 3:
            new_direction = [step+1, d]
        else:
            new_direction = [1, 3]
        heapq.heappush(queue, [cost + grid[ny][nx], ny, nx, new_direction])
print(min(count2))