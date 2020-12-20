from copy import deepcopy

with open("input2.txt", "r") as fp:
    lines = [line.strip() for line in fp]

rules = []
messages = []

x = rules
for line in lines:
    if not line:
        x = messages
        continue
    x.append(line)

max_message = 0
for i in messages:
    if len(i) > max_message:
        max_message = len(i)

nr = {}
found = []

# break rules out into dictionary
while len(nr) != len(rules):
    for rule in rules:
        left, right = [x.strip() for x in rule.split(":")]
        if "\"" in right:
            nr[left] = right.replace("\"", "")
            found.append(left)
        elif '|' in right:
            right = [x.strip() for x in right.split("|")]
            nr[left] = right
        else:
            nr[left] = [right]

# sort dictionary for easier rule calc
sorted_nr = {}
while len(sorted_nr) != len(nr):
    for i in nr:
        if i in found:
            sorted_nr[i] = nr[i]
        else:
            case = True
            for j in nr[i]:
                for k in j.split():
                    if k not in found:
                        case = False
                        break
                if case == False:
                    break
            if case == True:
                found.append(i)

def recurse(x):
    if not x:
        return [""]
    y = x.pop(0)
    t = []
    for i in sorted_nr[y]:
        nt = recurse(deepcopy(x))
        for j in range(len(nt)):
            nt[j] = i + nt[j]

        t += nt
    return t

# generate all possible rule combos
for i in sorted_nr:
    if sorted_nr[i] == 'a' or sorted_nr[i] == 'b':
        continue
    if i == '0':
        break
    t = []
    for j in sorted_nr[i]:
        t += (recurse(j.split()))
    sorted_nr[i] = t

def second_check(message):
    ind = 0
    check_size = len(sorted_nr['42'][0])
    x = '42'
    count = 0
    while ind < len(message):
        if message[ind: ind+check_size] in sorted_nr[x]:
            ind += check_size
            if x == '42':
                count += 1
            else:
                count -= 1
        else:
            if x == '31' or ind == 0:
                return False

            if message[ind: ind+check_size] in sorted_nr['31']:
                x = '31'
                ind += check_size
                count -= 1
                continue

            return False
    if count == 0:
        return True
    return False

def first_check(message):
    flen = len(sorted_nr['42'][0])
    ending = flen
    first = message[:ending]
    if first not in sorted_nr['42']:
        return False
    while ending < len(message):
        if second_check(message[ending:]):
            return True
        first = message[ending: ending+flen]

        if first not in sorted_nr['42']:
            if second_check(message[ending:]):
                return True
            return False

        ending += flen
    return False

#ans = "silver"
ans = "gold"

# gold
if ans == "gold":
    cnt = 0
    for i in messages:
        if first_check(i):
            cnt += 1


# check messages against rules
if ans == "silver":
    cnt = 0
    for i in messages:
        if i in sorted_nr['0']:
            cnt += 1

print(cnt)