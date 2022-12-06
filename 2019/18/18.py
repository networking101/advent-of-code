from copy import deepcopy

with open("input3", "r") as fp:
    lines = [line.strip() for line in fp]

def print_grid(g):
    for y in g:
        for x in y:
            print(x, end='')
        print()

def find_keys(g):
    keys = {}
    for y in range(len(g)):
        for x in range(len(g[y])):
            if g[y][x] == '@' or 0x61 <= ord(g[y][x]) <= 0x7a:
                keys[g[y][x]] = (y, x)

    return keys

def find_key_dist(g, c):
    # coordinates, distance, doors
    queue = [[c, 1, ""]]
    dist = {}
    while queue:
        c, di, do = queue.pop(0)
        y, x = c
        g[y][x] = '#'
        
        # Check for open spaces
        # up
        if g[y-1][x] == '.' or g[y-1][x] == '@':
            queue.append([[y-1,x], di+1, do])
        # right
        if g[y][x+1] == '.' or g[y][x+1] == '@':
            queue.append([[y, x+1], di+1, do])
        # down
        if g[y+1][x] == '.' or g[y+1][x] == '@':
            queue.append([[y+1, x], di+1, do])
        # left
        if g[y][x-1] == '.' or g[y][x-1] == '@':
            queue.append([[y, x-1], di+1, do])

        # Check for keys
        # up
        if 0x61 <= ord(g[y-1][x]) <= 0x7a:
            dist[g[y-1][x]] = [di, do]
            queue.append([[y-1,x], di+1, do])
        # right
        if 0x61 <= ord(g[y][x+1]) <= 0x7a:
            dist[g[y][x+1]] = [di, do]
            queue.append([[y, x+1], di+1, do])
        # down
        if 0x61 <= ord(g[y+1][x]) <= 0x7a:
            dist[g[y+1][x]] = [di, do]
            queue.append([[y+1, x], di+1, do])
        # left
        if 0x61 <= ord(g[y][x-1]) <= 0x7a:
            dist[g[y][x-1]] = [di, do]
            queue.append([[y, x-1], di+1, do])

        # Check for doors
        # up
        if 0x41 <= ord(g[y-1][x]) <= 0x5a:
            do += g[y-1][x]
            queue.append([[y-1,x], di+1, do])
        # right
        if 0x41 <= ord(g[y][x+1]) <= 0x5a:
            do += g[y][x+1]
            queue.append([[y, x+1], di+1, do])
        # down
        if 0x41 <= ord(g[y+1][x]) <= 0x5a:
            do += g[y+1][x]
            queue.append([[y+1, x], di+1, do])
        # left
        if 0x41 <= ord(g[y][x-1]) <= 0x5a:
            do += g[y][x-1]
            queue.append([[y, x-1], di+1, do])

    return dist


grid = []
for line in lines:
    grid.append([x for x in line])

print_grid(grid)

keys = find_keys(grid)

found_keys = ['@']
searched_keys = []
distances = {}

# find distances between keys
while found_keys:
    start = found_keys.pop(0)
    new_dist = find_key_dist(deepcopy(grid), keys[start])
    distances[start] = new_dist
    searched_keys.append(start)
    for k in new_dist:
        if k not in found_keys and k not in searched_keys:
            found_keys.append(k)

for d in distances:
    print(d, distances[d])
print()

def recursion(curr, fk):
    if (keys[curr], fk) in optimized:
        return optimized[(curr, fk)]
    # if len(optimized) % 10 == 0:
    #     print(fk)
    if len(fk) == num_keys:
        ans = 0
    else:
        min_vals = []
        for k in distances[curr]:
            if k not in fk:
                dist, drs = distances[curr][k]
                drs = list(drs)
                open_path = True
                for x in drs:
                    if x.lower() not in fk:
                        open_path = False
                        break
                if open_path:
                    new_fk = ''.join(sorted(fk + k))
                    cur_d = recursion(k, new_fk) + dist
                    if curr == '@':
                        print(cur_d)
                    min_vals.append(cur_d)
        ans = min(min_vals)
    optimized[(curr, fk)] = ans
    return ans

# find shortest path
start = '@'
path = {}
optimized = {}
num_keys = len(keys)
print(recursion(start, start))