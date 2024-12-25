with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

flag = False
solved = {}
gates = {}

max_z = 0

for line in lines:

    if not line:
        flag = True
    elif flag:
        left, right = line.split(" -> ")
        gates[right] = left.split()
        if right[0] == 'z' and int(right[1:]) > max_z:
            max_z = int(right[1:])

    else:
        left, right = line.split(": ")
        solved[left] = int(right)

# for k, v in gates.items():
#     print(k, v)
# print()
# for k, v in solved.items():
#     print(k, v)

def recurse(curr):
    if curr in solved:
        return solved[curr]
    
    a, calc, b = gates[curr]

    if a not in solved:
        a = recurse(a)
    else:
        a = solved[a]
    if b not in solved:
        b = recurse(b)
    else:
        b = solved[b]
    
    if calc == 'AND':
        res = a & b
    elif calc == 'OR':
        res = a | b
    elif calc == 'XOR':
        res = a ^ b
    else:
        assert(False)

    solved[curr] = res
    return res

silver = 0
for k, v in gates.items():
    if k[0] == 'z':
        solved[k] = recurse(k)
        silver += solved[k] << int(k[1:])

print(silver)