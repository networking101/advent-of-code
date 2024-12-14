with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

x_bound = 101
y_bound = 103

robots_p = []
robots_v = []

def print_grid(robots):
    grid = [['.' for xx in range(x_bound)] for yy in range(y_bound)]

    for r in robots:
        px, py = r
        grid[py][px] = "#"

    for j, y in enumerate(grid):
        for i, x in enumerate(y):
            print(x, end='')
        print()

for line in lines:
    left, right = line.split()
    px, py = [int(x) for x in left[2:].split(",")]
    vx, vy = [int(x) for x in right[2:].split(",")]
    robots_p.append((px, py))
    robots_v.append((vx, vy))

quadrants = [(range(0, int(y_bound/2)), range(0, int(x_bound/2))), \
             (range(0, int(y_bound/2)), range(int(x_bound/2) + 1, x_bound)), \
             (range(int(y_bound/2) + 1, y_bound), range(0, int(x_bound/2))), \
             (range(int(y_bound/2) + 1, y_bound), range(int(x_bound/2) + 1, x_bound))]
    
def silver(robots_p):
    # count quadrants
    q_count = [0, 0, 0, 0]

    for x, y in robots_p:
        for i, q in enumerate(quadrants):
            ry, rx = q
            if x in rx and y in ry:
                q_count[i] += 1

    silver = 1
    for c in q_count:
        silver *= c

    print(silver)

def gold(i, robots_p):
    score = 0
    for px, py in robots_p:
        if (px+1, py+1) in robots_p or \
            (px-1, py+1) in robots_p or \
            (px+1, py-1) in robots_p or \
            (px-1, py-1) in robots_p or \
            (px-1, py) in robots_p or \
            (px+1, py) in robots_p or \
            (px, py-1) in robots_p or \
            (px, py+1) in robots_p:
            score += 1
    # adjust tolerance if getting too many false positives or did not find tree
    tolerance = 1.5
    if score > len(lines)/tolerance:
        print(i)
        return True
    
    return False

z = 0
flag_silver = False
flag_gold = False
while True:
    for i, (p, v) in enumerate(zip(robots_p, robots_v)):
        px, py = p
        vx, vy = v
        px = (px + vx) % x_bound
        py = (py + vy) % y_bound
        robots_p[i] = (px, py)
        robots_v[i] = (vx ,vy)
    z += 1
    if z == 100:
        silver(robots_p)
        flag_silver = True

    if gold(z, robots_p):
        flag_gold = True

    if flag_silver and flag_gold:
        break
