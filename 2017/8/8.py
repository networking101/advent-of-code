with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

registers = {}
instructions = []

for line in lines:
    instruction = []
    l, r = line.split(" if ")
    r = r.split()

    # save register
    registers[r[0]] = 0

    l = l.split()

    instructions.append([[l[0], l[1], int(l[2])],[r[0], r[1], int(r[2])]])

def check_eval(x):
    a, b, c = x
    ret_val = False
    if b == ">":
        ret_val = True if registers[a] > c else False
    elif b == "<":
        ret_val = True if registers[a] < c else False
    elif b == "==":
        ret_val = True if registers[a] == c else False
    elif b == ">=":
        ret_val = True if registers[a] >= c else False
    elif b == "<=":
        ret_val = True if registers[a] <= c else False
    elif b == "!=":
        ret_val = True if registers[a] != c else False
    else:
        assert(False)

    return ret_val

def modify_register(x):
    a, b, c = x
    if b == "inc":
        registers[a] += c
    else:
        registers[a] += c

gold = 0
for l, r in instructions:
    # check eval
    if check_eval(r):
        a, b, c = l
        if b == "inc":
            registers[a] += c
        else:
            registers[a] -= c
        if registers[a] > gold:
            gold = registers[a]

silver = 0
for k, v in registers.items():
    if v > silver:
        silver = v

print(silver)
print(gold)