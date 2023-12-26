with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

objects = []
# min_intersection = 7
# max_intersection = 27
min_intersection = 200000000000000
max_intersection = 400000000000000

for line in lines:
    position, velocity = line.split('@')
    x, y, z = [int(a) for a in position.split(',')]
    vx, vy, vz = [int(a) for a in velocity.split(',')]

    objects.append(((x, y, z), (vx, vy, vz)))

def check_past(x, y, p1, v1, p2, v2):
    x1, y1, _ = p1
    vx1, vy1, _ = v1
    x2, y2, _ = p2
    vx2, vy2, _ = v2

    if vx1 == 0:
        new_x1 = x1
    else:
        new_x1 = x1 + (vx1 / abs(vx1))
    if vx2 == 0:
        new_x2 = x2
    else:
        new_x2 = x2 + (vx2 / abs(vx2))
    if vy1 == 0:
        new_y1 = y1
    else:
        new_y1 = y1 + (vy1 / abs(vy1))
    if vy2 == 0:
        new_y2 = 0
    else:
        new_y2 = y2 + (vy2 / abs(vy2))

    if abs(x1 - x) > abs(new_x1 - x) and \
        abs(x2 - x) > abs(new_x2 - x) and \
        abs(y1 - y) > abs(new_y1 - y) and \
        abs(y2 - y) > abs(new_y2 - y):
        return True
    return False

count1 = 0
for j, obj1 in enumerate(objects):
    p1, v1 = obj1
    A1 = v1[1]
    B1 = v1[0] * -1
    C1 = A1*p1[0] + B1*p1[1]

    for i, obj2 in enumerate(objects[j+1:]):
        p2, v2 = obj2
        A2 = v2[1]
        B2 = v2[0] * -1
        C2 = A2*p2[0] + B2*p2[1]

        det = A1 * B2 - A2 * B1
        if det == 0:
            continue
        else:
            x = (B2 * C1 - B1 * C2) / det
            y = (A1 * C2 - A2 * C1) / det
            if min_intersection <= x <= max_intersection and min_intersection <= y <= max_intersection:
                if check_past(x, y, p1, v1, p2, v2):
                    count1 += 1
print(count1)

def find_intersection2(first, second):
    p1, v1 = first
    p2, v2 = second

    x1, y1, z1 = p1
    vx1, vy1, vz1 = v1
    x2, y2, z2 = p2
    vx2, vy2, vz2 = v2

    c1 = x2 - x1
    tc1 = vx2 * -1
    sc1 = vx1
    c2 = y2 - y1
    tc2 = vy2 * -1
    sc2 = vy1
    
    if (sc1*tc2 - sc2*tc1) == 0:
        return None

    s = (c1*tc2 - c2*tc1) / (sc1*tc2 - sc2*tc1)
    t = (c1*sc2 - c2*sc1) / (tc1*sc2 - tc2*sc1)

    xx1 = x1 + vx1*s
    yy1 = y1 + vy1*s
    xx2 = x2 + vx2*t
    yy2 = y2 + vy2*t

    return (xx1, yy1)

def find_intersection3(first, second):
    p1, v1 = first
    p2, v2 = second

    x1, y1, z1 = p1
    vx1, vy1, vz1 = v1
    x2, y2, z2 = p2
    vx2, vy2, vz2 = v2

    c1 = x2 - x1
    tc1 = vx2 * -1
    sc1 = vx1
    c2 = y2 - y1
    tc2 = vy2 * -1
    sc2 = vy1
    
    if (sc1*tc2 - sc2*tc1) == 0:
        return None

    s = (c1*tc2 - c2*tc1) / (sc1*tc2 - sc2*tc1)
    t = (c1*sc2 - c2*sc1) / (tc1*sc2 - tc2*sc1)

    xx1 = x1 + vx1*s
    yy1 = y1 + vy1*s
    zz1 = z1 + vz1*s
    xx2 = x2 + vx2*t
    yy2 = y2 + vy2*t
    zz2 = z2 + vz2*t

    if xx1 == xx2 and yy1 == yy2 and zz1 == zz2:
        return (xx1, yy1, zz1)
    return None

# find where all hail converges on a single point, relative x velocity, relative y velocity
for dy in range(-500, 500):
    for dx in range(-500, 500):
        check = True
        origin = None

        position, velocity = objects[0]
        vx, vy, vz = velocity
        relative_object1 = (position, (vx - dx, vy - dy, vz))
        for index2, object2 in enumerate(objects[1:]):
            position, velocity = object2
            vx, vy, vz = velocity
            relative_object2 = (position, (vx - dx, vy - dy, vz))

            res = find_intersection2(relative_object1, relative_object2)
            if res is None:
                check = False
                break
            elif origin is None:
                origin = res
            elif res != origin:
                check = False
                break
        if check:
            break
    if check:
        break

# find where all hail converges on a single point, relative x velocity, relative y velocity, relative z velocity
for dz in range(-500, 500):
    check = True
    origin = None

    position, velocity = objects[0]
    vx, vy, vz = velocity
    relative_object1 = (position, (vx - dx, vy - dy, vz - dz))
    for index2, object2 in enumerate(objects[1:]):
        position, velocity = object2
        vx, vy, vz = velocity
        relative_object2 = (position, (vx - dx, vy - dy, vz - dz))

        res = find_intersection3(relative_object1, relative_object2)
        if res is None:
            check = False
            break
        elif origin is None:
            origin = res
        elif res != origin:
            check = False
            break
    if check:
        break
print(sum(origin))