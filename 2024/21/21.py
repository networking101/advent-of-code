from copy import deepcopy
from heapq import heappop, heappush

with open("input3", "r") as fp:
    lines = [line.strip() for line in fp]

codes = [x for x in ''.join(lines)]

num_pad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
num_locations = {"7": (0, 0), "8": (0, 1), "9": (0, 2), \
                 "4": (1, 0), "5": (1, 1), "6": (1, 2), \
                 "1": (2, 0), "2": (2, 1), "3": (2, 2), \
                 "0": (3, 1), "A": (3, 2)}
dir_pad = [[None, "^", "A"], ["<", "v", ">"]]
dir_locations = {"^": (0, 1), "A": (0, 2), \
                 "<": (1, 0), "v": (1, 1), ">": (1, 2)}

dir_to_directions = ["^", ">", "v", "<"]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# get distances on number pad
num_dists = {}
for j, y in enumerate(num_pad):
    for i, x in enumerate(y):
        if x == None:
            continue

        # use BFS to find all paths between each numbers
        start = (j, i)
        queue = []
        heappush(queue, (0, j, i, ""))
        while queue:
            step, yy, xx, path_s = heappop(queue)

            curr = (yy, xx)
            # if curr != start:
            if (start, curr) not in num_dists:
                num_dists[(start, curr)] = [path_s]
            elif len(num_dists[(start, curr)][0]) == len(path_s):
                num_dists[(start, curr)].append(path_s)
            
            if step > 5:
                break

            for d, (dy, dx) in enumerate(directions):
                ny = yy + dy
                nx = xx + dx
                if ny < 0 or ny >= len(num_pad) or nx < 0 or nx >= len(num_pad[0]) or num_pad[ny][nx] == None:
                    continue
                queue.append((step + 1, ny, nx, path_s + dir_to_directions[d]))

for k, v in num_dists.items():
    s, e = k
    print((num_pad[s[0]][s[1]], num_pad[e[0]][e[1]]), v)
# exit(0)

# get distances on direction pad
dir_dists = {}
for j, y in enumerate(dir_pad):
    for i, x in enumerate(y):
        if x == None:
            continue

        # use BFS to find all paths between each directions
        start = (j, i)
        queue = []
        heappush(queue, (0, j, i, ""))
        while queue:
            step, yy, xx, path_s = heappop(queue)

            curr = (yy, xx)
            # if curr != start:
            if (start, curr) not in dir_dists:
                dir_dists[(start, curr)] = [path_s]
            elif len(dir_dists[(start, curr)][0]) == len(path_s):
                dir_dists[(start, curr)].append(path_s)
            
            if step > 5:
                break

            for d, (dy, dx) in enumerate(directions):
                ny = yy + dy
                nx = xx + dx
                if ny < 0 or ny >= len(dir_pad) or nx < 0 or nx >= len(dir_pad[0]) or dir_pad[ny][nx] == None:
                    continue
                queue.append((step + 1, ny, nx, path_s + dir_to_directions[d]))

# for k, v in dir_dists.items():
#     s, e = k
#     print((dir_pad[s[0]][s[1]], dir_pad[e[0]][e[1]]), v)
# exit(0)

def recurse_nums(codes, path):
    if len(codes) == 1:
        return [path]
    
    curr_pad = codes.pop(0)
    next_pad = codes[0]
        
    min_paths = []
    len_min_path = 999999999
    for p in num_dists[(num_locations[curr_pad], num_locations[next_pad])]:
        new_path = deepcopy(path)
        min_path = recurse_nums(deepcopy(codes), new_path + p + "A")
        tmp = 0
        for mp in min_path:
            if len(mp) < len_min_path:
                min_paths = [mp]
                len_min_path = len(mp)
            elif len(mp) == len_min_path:
                min_paths.append(mp)

    return min_paths

DP = {}
def recurse_dirs(codes, path):
    if len(codes) == 1:
        return [path]
    
    curr_pad = codes.pop(0)
    next_pad = codes[0]
        
    min_paths = []
    len_min_path = 999999999
    for p in dir_dists[(dir_locations[curr_pad], dir_locations[next_pad])]:
        new_path = deepcopy(path)
        min_path = recurse_dirs(deepcopy(codes), new_path + p + "A")
        tmp = 0
        for mp in min_path:
            if len(mp) < len_min_path:
                min_paths = [mp]
                len_min_path = len(mp)
            elif len(mp) == len_min_path:
                min_paths.append(mp)

    DP[(curr_pad, next_pad, path)] = min_paths
    return min_paths

# numeric keypad
min_paths = recurse_nums(['A'] + codes, "")

print("numeric keypad")

# first directional keypad
new_min_paths = []
for codes in min_paths:
    # print(codes)
    new_min_paths += recurse_dirs(['A'] + list(codes), "")

print("first directional keypad")

min_paths = new_min_paths
len_min_path = 999999999
for mp in min_paths:
    if len(mp) < len_min_path:
        min_paths = [mp]
        len_min_path = len(mp)
    elif len(mp) == len_min_path:
        min_paths.append(mp)

# second directional keypad
new_min_paths = []
for codes in min_paths:
    # print(codes)
    new_min_paths += recurse_dirs(['A'] + list(codes), "")

print("second directional keypad")

min_paths = new_min_paths
len_min_path = 999999999
for mp in min_paths:
    if len(mp) < len_min_path:
        min_paths = [mp]
        len_min_path = len(mp)
    elif len(mp) == len_min_path:
        min_paths.append(mp)

# third directional keypad
new_min_paths = []
for codes in min_paths:
    # print(codes)
    new_min_paths += recurse_dirs(['A'] + list(codes), "")

min_paths = new_min_paths
len_min_path = 999999999
for mp in min_paths:
    if len(mp) < len_min_path:
        min_paths = [mp]
        len_min_path = len(mp)
    elif len(mp) == len_min_path:
        min_paths.append(mp)

print(min_paths)