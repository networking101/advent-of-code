with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

nodes = {}
leaves = []
roots = {}

for line in lines:
    if ('->') in line:
        l, r = line.split(' -> ')
        program, weight = l.split()
        subs = r.split(', ')

        nodes[program] = int(weight[1:-1])
        roots[program] = subs

    else:
        program, weight = line.split()
        nodes[program] = int(weight[1:-1])
        leaves.append(program)

# silver
for k, v in roots.items():
    not_root = 0
    for k2, v2 in roots.items():
        if v == v2:
            continue
        if k in v2:
            not_root = 1
    if not not_root:
        print(k)
        break

gold = 0
def recurse(node):
    if node in leaves:
        return (nodes[node], 0)
    
    sub_values = []
    for sub_node in roots[node]:
        if sub_node in leaves:
            sub_values.append(nodes[sub_node])
        else:
            a, b = recurse(sub_node)
            # we already have an answer if bail condition
            if b == -1:
                return (a, b)
            sub_values.append(a + b)

    # make sure we have at least one value
    assert(len(sub_values))
    # check if different value was found
    if len(set(sub_values)) > 1:
        # figure out which value is consistant
        if sub_values.count(min(sub_values)) != 1:
            same = min(sub_values)
        else:
            same = max(sub_values)
        # its easier to run everything again and check for the off value
        found = 0
        for sub_node in roots[node]:
            tmp = 0
            if sub_node in leaves:
                tmp = nodes[sub_node]
                if tmp != same:
                    # we need a bail condition when we find the answer
                    return (same, -1)
            else:
                a, b = recurse(sub_node)
                if a + b != same:
                    # we need a bail condition when we find the answer
                    return (same - b, -1)
    
    return (nodes[node], sum(sub_values))

gold,_ = recurse(k)
print(gold)