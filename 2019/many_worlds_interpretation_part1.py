from copy import deepcopy

with open("part1_input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = [[z for z in line] for line in lines]

keys = {}
doors = {}
distances = {}
locked_doors = {}

for j, y in enumerate(grid):
    for i, x in enumerate(y):
        if x.islower() or x == '@':
            keys[x] = (j, i)
            distances[x] = {}
            locked_doors[x] = {}
        if x.isupper():
            doors[x] = (j, i)

# find doors between keys
def find_doors(g, key, curr_pos, drs):
    y, x = curr_pos
    if g[y][x] in keys and g[y][x] != key:
        locked_doors[key][g[y][x]] = drs
        return
    if g[y][x].isalpha() and g[y][x].isupper() and g[y][x] != key:
        drs.append(g[y][x])
    g[y][x] = '#'
    for i, pos in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
        yy = y + pos[0]
        xx = x + pos[1]
        if g[yy][xx] != '#':
            find_doors(g, key, [yy, xx], deepcopy(drs))
    return

# find distances between keys
def find_distances(g, key):
    y, x = keys[key]
    queue = [[y, x, 0]]
    while queue:
        y, x, cnt = queue.pop(0)
        if g[y][x] in keys and g[y][x] != key:
            distances[key][g[y][x]] = cnt
            continue
        g[y][x] = '#'
        for i, pos in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            yy = y + pos[0]
            xx = x + pos[1]
            if g[yy][xx] != '#':
                queue.append([yy, xx, cnt + 1])
    return

for key in keys:
    find_doors(deepcopy(grid), key, keys[key], [])
    find_distances(deepcopy(grid), key)

# find distances through all doors
full_distances = {}
full_doors = {}
for key in keys:
    full_distances[key] = {}
    full_doors[key] = {}
    curr_dist_dict = full_distances[key]
    curr_door_dict = full_doors[key]
    queue = [[key, 0, [], [key]]]
    while queue:
        k, dist, drs, kys = queue.pop(0)
        for dk, dv in distances[k].items():
            if dk in kys:
                continue
            curr_dist_dict[dk] = dv + dist
            curr_door_dict[dk] = locked_doors[k][dk] + drs
            kys.append(dk)
            queue.append([dk, dv + dist, deepcopy(locked_doors[k][dk] + drs), kys])

def check_doors(keys, doors):
    for d in doors:
        if d.lower() not in keys:
            return False
    return True

# find shortest path
DP = {}
def recursive3(curr_key, found_keys):
    if len(found_keys) == len(keys):
        return 0
    sorted_keys = deepcopy(found_keys)
    sorted_keys.sort()
    DP_key = (curr_key, ''.join(sorted_keys))
    if DP_key in DP:
        return DP[DP_key]
    
    this_count = [999999999]
    full_dist = full_distances[curr_key]
    full_door = full_doors[curr_key]

    for nk, nv in full_dist.items():
        # check if we have all the keys for next door nd
        if check_doors(found_keys, full_door[nk]) and nk not in found_keys:
            n_found_keys = deepcopy(found_keys)
            n_found_keys.append(nk)
            this_count.append(recursive3(nk, n_found_keys) + nv)

    # print(this_count)
    DP[DP_key] = min(this_count)
    return min(this_count)

count1 = recursive3('@', ['@'])
print(count1)