with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

rules = []
updates = []

r_flag = True
for line in lines:
    if not line:
        r_flag = False
        continue

    if r_flag:
        rules.append([int(x) for x in line.split("|")])
    else:
        updates.append([int(x) for x in line.split(",")])

def check_rules(this_list):
    for j, y in enumerate(this_list):
        for i, x in enumerate(this_list[j+1:]):
            if [y, x] not in rules:
                return False
    return True

def fix_update(this_list):
    if len(this_list) == 1:
        return this_list
    
    for j, y in enumerate(this_list):
        found = True
        for i, x in enumerate(this_list):
            if j == i:
                continue
            if [y, x] not in rules:
                found = False
                break
        
        if found:
            this_list.pop(j)
            return [y] + fix_update(this_list)

    assert(False)

silver = 0
gold = 0
for update in updates:
    if check_rules(update):
        silver += update[int(len(update) / 2)]
    else:
        new_update = fix_update(update)
        gold += new_update[int(len(new_update) / 2)]

print(silver)
print(gold)