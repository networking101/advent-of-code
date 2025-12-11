with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

lines = [[int(x) for x in line.split(',')] for line in lines]

silver = 0
for j, y in enumerate(lines):
    for i, x in enumerate(lines):
        if i <= j:
            continue

        tmp = (abs(y[0] - x[0]) + 1) * (abs(y[1] - x[1]) + 1)
        if tmp > silver:
            silver = tmp

print(silver)


invalid_blocks = []

for j, y in enumerate(lines):

    ax, ay = y
    dx, dy = lines[(j + 1) % len(lines)]
    bx, by = lines[(j + 2) % len(lines)]

    # check if left turn
    if ay == dy:
        if dx > ax and by < dy:
            invalid_blocks.append((min(ax, bx), min(ay, by), max(ax, bx) - 1, max(ay, by) - 1))
        if dx < ax and by > dy:
            invalid_blocks.append((min(ax, bx) + 1, min(ay, by) + 1, max(ax, bx), max(ay, by)))
    else:
        if dy < ay and bx < dx:
            invalid_blocks.append((min(ax, bx), min(ay, by) + 1, max(ax, bx) - 1, max(ay, by)))
        if dy > ay and bx > dx:
            invalid_blocks.append((min(ax, bx) + 1, min(ay, by), max(ax, bx), max(ay, by) - 1))


def is_overlap(recta, rectb):
    x1_a, y1_a, x2_a, y2_a = recta
    x1_b, y1_b, x2_b, y2_b = rectb

    if x2_a <= x1_b or x2_b <= x1_a:
        return False
    if y2_a <= y1_b or y2_b <= y1_a:
        return False
    
    return True

gold = 0
i = 0
while i < len(lines) - 1:
    a = lines[i]

    j = i + 2
    while j < len(lines):
        b = lines[j]

        ax, ay = a
        bx, by = b

        area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)

        if area <= gold:
            j += 1
            continue

        check = False
        for ib in invalid_blocks:
            
            # check if overlap
            if is_overlap((min(ax, bx), min(ay, by), max(ax, bx), max(ay, by)), ib):
                check = True
                break
        
        if not check:
            gold = area

        j += 1
    i += 1

print(gold)