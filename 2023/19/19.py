from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

workflows = {}
part_ratings = []

swap = False
for line in lines:
    if not line:
        swap = True
        continue

    if not swap:
        name, rules = line[:-1].split('{')
        workflows[name] = []
        rules = rules.split(',')
        for rule in rules:
            if '<' in rule or '>' in rule:
                condition, output = rule.split(":")
                check = '>'
                if '<' in condition:
                    check = '<'
                condition = list(condition.partition(check))
                condition[-1] = int(condition[-1])
                condition.append(output)
                workflows[name].append(condition)
            else:
                workflows[name].append([rule])

    if swap:
        part = {}
        for p in line[1:-1].split(','):
            property, val = p.split("=")
            part[property] = int(val)
        part_ratings.append(part)


accept = []
reject = []

def recursive(name, part):
    for rule in workflows[name]:
        if len(rule) == 1:
            if rule[0] == 'A':
                accept.append(part)
            elif rule[0] == 'R':
                reject.append(part)
            else:
                recursive(rule[0], part)
        else:
            if rule[1] == '<':
                if part[rule[0]] < rule[2]:
                    if rule[3] == 'A':
                        accept.append(part)
                    elif rule[3] == 'R':
                        reject.append(part)
                    else:
                        recursive(rule[3], part)
                    break
            else:
                if part[rule[0]] > rule[2]:
                    if rule[3] == 'A':
                        accept.append(part)
                    elif rule[3] == 'R':
                        reject.append(part)
                    else:
                        recursive(rule[3], part)
                    break
    return

for p in part_ratings:
    recursive('in', p)

count1 = 0
for a in accept:
    for k, v in a.items():
        count1 += v

print(count1)

# part 2
accept = []
reject = []
queue = [['in', {'x':range(1, 4001), 'm':range(1, 4001), 'a':range(1, 4001), 's':range(1, 4001)}]]
while queue:
    curr, vals = queue.pop(0)
    
    rules = workflows[curr]
    for r in rules:
        if len(r) == 1:
            if r[0] == 'A':
                accept.append(vals)
            elif r[0] == 'R':
                reject.append(vals)
            else:
                queue.append([r[0], vals])
        else:
            property, check, amount, destination = r
            if amount in vals[property]:
                if check == '<':
                    nvals = deepcopy(vals)
                    nvals[property] = range(vals[property][0], amount)
                    vals[property] = range(amount, vals[property][-1] + 1)
                    if destination == 'A':
                        accept.append(nvals)
                    elif destination == 'R':
                        reject.append(nvals)
                    else:
                        queue.append([destination, nvals])
                if check == '>':
                    nvals = deepcopy(vals)
                    nvals[property] = range(amount+1, vals[property][-1] + 1)
                    vals[property] = range(vals[property][0], amount+1)
                    if destination == 'A':
                        accept.append(nvals)
                    elif destination == 'R':
                        reject.append(nvals)
                    else:
                        queue.append([destination, nvals])
            else:
                if check == '<':
                    if vals[property][-1] < amount:
                        nvals = deepcopy(vals)
                        if destination == 'A':
                            accept.append(nvals)
                        elif destination == 'R':
                            reject.append(nvals)
                        else:
                            queue.append([destination, nvals])
                        break
                    if vals[property][0] >= amount:
                        continue
                if check == '>':
                    if vals[property][0] > amount:
                        nvals = deepcopy(vals)
                        if destination == 'A':
                            accept.append(nvals)
                        elif destination == 'R':
                            reject.append(nvals)
                        else:
                            queue.append([destination, nvals])
                        break
                    if vals[property][-1] <= amount:
                        continue

count2 = 0           
for z in accept:
    tmp_count = 1
    for k, v in z.items():
        tmp_count *= len(v)
    count2 += tmp_count

print(count2)