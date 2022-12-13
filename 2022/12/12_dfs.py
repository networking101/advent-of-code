from copy import deepcopy
import sys
import time

start_time = time.time()
sys.setrecursionlimit(2000)

with open("input4", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []
start = ()
end = ()

for y in range(len(lines)):
    tmp = []
    for x in range(len(lines[0])):
        if lines[y][x] == "S":
            start = (y, x)
            tmp.append("a")
            continue
        if lines[y][x] == "E":
            end = (y, x)
            tmp.append("z")
            continue
        tmp.append(lines[y][x])
    grid.append(tmp)

distances = {}
def recursion(p, v, d):
    y, x = p
    if (y, x) == end:
        print("FOUND END: " + str(d))
        print(time.time() - start_time)
        return 0
    if str(p) in distances:
        return distances[str(p)]
    v.append((y, x))
    dists = [999999999]
    # check up
    if y-1 >= 0 and (ord(grid[y-1][x]) - ord(grid[y][x])) <= 1 and (y-1, x) not in v:
        dists.append(recursion((y-1, x), deepcopy(v), d+1))
    # check left
    if x-1 >= 0 and (ord(grid[y][x-1]) - ord(grid[y][x])) <= 1 and (y, x-1) not in v:
        dists.append(recursion((y, x-1), deepcopy(v), d+1))
    # check down
    if y+1 < len(grid) and (ord(grid[y+1][x]) - ord(grid[y][x])) <= 1 and (y+1, x) not in v:
        dists.append(recursion((y+1, x), deepcopy(v), d+1))
    # check right
    if x+1 < len(grid[0]) and (ord(grid[y][x+1]) - ord(grid[y][x])) <= 1 and (y, x+1) not in v:
        dists.append(recursion((y, x+1), deepcopy(v), d+1))

    curr_min = min(dists) + 1
    distances[str(p)] = curr_min
    return curr_min

print(recursion(start, [], 0))
print(time.time() - start_time)

# 595 too high
# 613 too high
# 497 wrong someone elses
# 463 wrong
# 481 wrong someone elses