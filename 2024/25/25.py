with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

locks = []
keys = []

locks2 = []
keys2 = []

# false = lock, true = key
flag = False
curr = []
for i, line in enumerate(lines):
    if not line:
        if not flag:
            locks.append(curr)
        else:
            keys.append(curr)
        curr = []

        if i < len(lines) - 1 and lines[i+1] == '#####':
            flag = False
        if i < len(lines) - 1 and lines[i+1] != '#####':
            flag = True
    else:
        curr.append([x for x in line])
if not flag:
    locks.append(curr)
else:
    keys.append(curr)

for lock in locks:
    tmp = [0,0,0,0,0]
    for row in lock:
        for i, col in enumerate(row):
            if col == '#':
                tmp[i] += 1
    locks2.append(tmp)

for key in keys:
    tmp = [0,0,0,0,0]
    for row in key:
        for i, col in enumerate(row):
            if col == '#':
                tmp[i] += 1
    keys2.append(tmp)

silver = 0
for lock in locks2:
    for key in keys2:
        flag = True
        for i in range(5):
            if lock[i] + key[i] > 7:
                flag = False

        if flag:
            silver += 1
print(silver)