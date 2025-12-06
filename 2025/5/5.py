with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

fresh_ids = []
ingredients = []
switch = 0
for line in lines:
    if not line:
        switch += 1
        continue
    
    if switch == 0:
        l, r = line.split('-')
        fresh_ids.append(range(int(l), int(r) + 1))

    if switch == 1:
        ingredients.append(int(line))

silver = 0
for i in ingredients:
    for fi in fresh_ids:
        if i in fi:
            silver += 1
            break

print(silver)

fresh_sets = []
for fi in fresh_ids:
    if len(fresh_sets) == 0:
        fresh_sets.append(fi)
        continue

    f = fi[0]
    l = fi[-1]
    new_fresh_sets = []
    for fs in fresh_sets:
        if f in fs:
            f = fs[0]
            if l in fs:
                l = fs[-1]
        elif l in fs:
            l = fs[-1]
            if f in fs:
                f = fs[0]
        else:
            if fs[0] < f or fs[-1] > l:
                new_fresh_sets.append(fs)

    new_fresh_sets.append(range(f, l+1))
    fresh_sets = new_fresh_sets
    

gold = 0
for fs in fresh_sets:
    gold += len(fs)
print(gold)