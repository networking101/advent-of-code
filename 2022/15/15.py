import intervaltree

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

my_row_ind = 10
my_row_ind = 2000000
low_bound = 0
up_bound = 20
up_bound = 4000000

# Parse input
coords = {}
for line in lines:
    sensor, beacon = line.split(": ")
    sx, sy = [int(i[2:].replace(",","")) for i in sensor.split()[-2:]]
    bx, by = [int(i[2:].replace(",","")) for i in beacon.split()[-2:]]
    coords[(sy,sx)] = (by,bx)

# loop through coords and get sensors that intersect my_row_ind
b_intercepts = []
minx = 0
maxx = 0
ranges = []
for s, b in coords.items():
    # grab any beacons on my_row
    if b[0] == my_row_ind:
        b_intercepts.append(b[1])

    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])

    # if sensor scans my_row_ind, get range of overlap
    if (s[0] - dist) <= my_row_ind <= (s[0] + dist):
        offset = abs(s[0] - my_row_ind)
        # get min and max x values
        if (s[1] - (dist - offset)) < minx:
            minx = (s[1] - (dist - offset))
        if s[1] + (dist - offset) > maxx:
            maxx = s[1] + (dist - offset)
        ranges.append(range(s[1] - (dist - offset), s[1] + (dist - offset) + 1))

# loop through ranges update my_row with covered points
my_row = ['.'] * (maxx - minx + 1)
for i in ranges:
    for j in i:
        my_row[j - minx] = '#'

# loop through b_intercepts and add them to my_row\
for b in b_intercepts:
    my_row[b - minx] = "B"

tot = 0
for x in my_row:
    if x == '#':
        tot += 1

print(tot)

# Part 2
# loop through coords and get sensors that intersect my_row_ind
ranges = {}
for s, b in coords.items():
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    # check lower areas
    for d in range(dist+1):
        # if sensor scans my_row_ind, get range of overlap
        offset = dist - d
        if s[0] - d < low_bound:
            break
        if (s[0] - d) not in ranges:
            ranges[s[0] - d] = []
        new_range = (max(low_bound, s[1] - offset), min(up_bound, s[1] + offset + 1))
        if new_range[0] != new_range[1]:
            ranges[s[0] - d].append(new_range)

    # check higher areas
    for d in range(dist+1):
        # if sensor scans my_row_ind, get range of overlap
        offset = dist - d
        if s[0] + d > up_bound:
            break
        if (s[0] + d) not in ranges:
            ranges[s[0] + d] = []
        new_range = (max(low_bound, s[1] - offset), min(up_bound, s[1] + offset + 1))
        if new_range[0] != new_range[1]:
            ranges[s[0] + d].append(new_range)

idx = 0
for k, v in ranges.items():
    tree = intervaltree.IntervalTree.from_tuples(v)
    tree.merge_overlaps(strict=False)
    if len(tree) != 1:
        for z in tree:
            tmp = str(z)
            if "0," in tmp:
                tmp = int(tmp.split("0, ")[1][:-1])
                print(tmp*4000000 + k)
                exit(0)