from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

lines = [line.split('-') for line in lines]
groups = {}
threes = []

for x in lines:
    a, b = x
    for y in lines:
        c, d = y
        if a in y and b in y:
            continue

        if a == c:
            if a in groups:
                groups[a].add(d)
            else:
                groups[a] = set()
                groups[a].add(d)
        if a == d:
            if a in groups:
                groups[a].add(c)
            else:
                groups[a] = set()
                groups[a].add(c)
        if b == c:
            if b in groups:
                groups[b].add(d)
            else:
                groups[b] = set()
                groups[b].add(d)
        if b == d:
            if b in groups:
                groups[b].add(c)
            else:
                groups[b] = set()
                groups[b].add(c)


def recurse(steps, k, path):
    path = deepcopy(path)
    path.append(k)

    if steps == 3:
        if path[0] in groups[k]:
            path.sort()
            if path not in threes:
                threes.append(path)
        return

    for v in groups[k]:
        if v in path:
            continue
        recurse(steps + 1, v, path)


for k, v in groups.items():
    recurse(1, k, [])

silver = 0
for t in threes:
    for x in t:
        if x[0] == 't':
            silver += 1
            break

print(silver)

lans = []
found = []
def recurse_gold(k, path):
    for previous in path:
        if previous not in groups[k]:
            return
    
    path.append(k)
    tmp_path = path
    tmp_path.sort()
    tmp_path = ','.join(tmp_path)
    if tmp_path in lans:
        return
    lans.append(tmp_path)

    for v in groups[k]:
        recurse_gold(v, deepcopy(path))

    return

max_lan = []
max_len = 0
for l in lans:
    if len(l) > max_len:
        max_lan = l
        max_len = len(l)
print(max_lan)