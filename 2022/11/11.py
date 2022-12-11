from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

monkeys = {}
curr_monkey = 0
tot_mod = 1
for line in lines:
    if line[:6] == "Monkey":
        assert int(line.split()[1][:-1]) == curr_monkey
        monkeys[curr_monkey] = {"inspect":0}
    if line[:8] == "Starting":
        i = [int(x) for x in line[16:].replace(" ", "").split(",")]
        monkeys[curr_monkey]["items"] = i
    if line[:9] == "Operation":
        ops = line.split()[-3:]
        monkeys[curr_monkey]["ops"] = ops
    if line[:4] == "Test":
        test = int(line.split()[-1])
        tot_mod *= test
        monkeys[curr_monkey]["div"] = test
    if line[:7] == "If true":
        t_monk = int(line.split()[-1])
        monkeys[curr_monkey]["true"] = t_monk
    if line[:8] == "If false":
        f_monk = int(line.split()[-1])
        monkeys[curr_monkey]["false"] = f_monk
    if not line:
        curr_monkey += 1

monkeys2 = deepcopy(monkeys)

# for m in monkeys:
#     print(m, monkeys[m])

def operation(old, o_list):
    first, op, second = o_list
    if first == "old":
        first = old
    else:
        first = int(first)
    if second == "old":
        second = old
    else:
        second = int(second)
    if op == "+":
        return first + second
    if op == "*":
        return first * second

# Part 1
old = 0
for round in range(20):
    for monk in range(curr_monkey+1):
        while monkeys[monk]["items"]:
            i = monkeys[monk]["items"].pop(0)
            monkeys[monk]["inspect"] += 1
            # calc worry level
            worry = operation(i, monkeys[monk]["ops"])
            worry = int(worry/3)
            t_monk = monkeys[monk]["true"]
            f_monk = monkeys[monk]["false"]
            if worry % monkeys[monk]["div"] == 0:
                monkeys[t_monk]["items"].append(worry)
            else:
                monkeys[f_monk]["items"].append(worry)


inspect = []
for m in monkeys:
    inspect.append(monkeys[m]["inspect"])
inspect.sort()
inspect = inspect[::-1]
print(inspect.pop(0) * inspect.pop(0))

# Part 2
old = 0
for round in range(10000):
    for monk in range(curr_monkey+1):
        while monkeys2[monk]["items"]:
            i = monkeys2[monk]["items"].pop(0)
            monkeys2[monk]["inspect"] += 1
            # calc worry level
            worry = operation(i, monkeys2[monk]["ops"])
            worry = worry % tot_mod
            t_monk = monkeys2[monk]["true"]
            f_monk = monkeys2[monk]["false"]
            if worry % monkeys2[monk]["div"] == 0:
                monkeys2[t_monk]["items"].append(worry)
            else:
                monkeys2[f_monk]["items"].append(worry)


inspect = []
for m in monkeys2:
    inspect.append(monkeys2[m]["inspect"])
inspect.sort()
inspect = inspect[::-1]
print(inspect.pop(0) * inspect.pop(0))