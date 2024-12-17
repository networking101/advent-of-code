from heapq import heappop, heappush

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[x for x in y] for y in lines]

for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x == 'E':
            end = (j, i)
        if x == 'S':
            start = (j, i)

DP = {}
paths = []
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = []
silver = 999999999

heappush(queue, (0, start, 1, ""))
while queue:
    cost, curr, d, path = heappop(queue)

    # none of our entries left in the queue will beat our current silver score
    if cost > silver:
        break

    # we already have an optimal path for this position
    if (curr, d) in DP and DP[(curr, d)] < cost:
        continue

    DP[(curr, d)] = cost
    if curr == end:
        silver = cost
        paths.append(path)
    
    y, x = curr
    dy, dx = directions[d]
    if grid[y + dy][x + dx] != '#':
        heappush(queue, (cost + 1, (y + dy, x + dx), d, path + "F"))
    heappush(queue, (cost + 1000, curr, (d + 1) % 4, path + "R"))
    heappush(queue, (cost + 1000, curr, (d - 1) % 4, path + "L"))

print(silver)

positions = set()

for path in paths:
    y, x = start
    d = 1
    positions.add(start)

    for step in path:
        if step == 'L':
            d = (d - 1) % 4
        if step == 'R':
            d = (d + 1) % 4
        if step == 'F':
            dy, dx = directions[d]
            ny = y + dy
            nx = x + dx
            positions.add((ny, nx))
            y = ny
            x = nx
print(len(positions))
