from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

values = []

for line in lines:
    test, operators = [x.strip() for x in line.split(':')]
    test = int(test)
    operators = [int(x) for x in operators.split()]

    values.append((test, operators))

def recurse(test, operators, val):

    if len(operators) == 0:
        if val == test:
            return True
        return False

    curr = operators.pop(0)

    # add
    if recurse(test, deepcopy(operators), val + curr):
        return True

    # multiply
    return recurse(test, deepcopy(operators), val * curr)

def recurse_gold(test, operators, val):

    if len(operators) == 0:
        if val == test:
            return True
        return False

    curr = operators.pop(0)

    # add
    if recurse_gold(test, deepcopy(operators), val + curr):
        return True

    # multiply
    if recurse_gold(test, deepcopy(operators), val * curr):
        return True

    # concatenation
    return recurse_gold(test, deepcopy(operators), int(str(val) + str(curr)))

silver = 0
gold = 0
for v in values:
    test, operators = v
    curr = operators.pop(0)
    if recurse(test, deepcopy(operators), curr):
        silver += test
    if recurse_gold(test, deepcopy(operators), curr):
        gold += test

print(silver)
print(gold)