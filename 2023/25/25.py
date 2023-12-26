from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

components = {}
connections = []

for line in lines:
    left, right = line.split(':')
    right = right.split()

    if left in components:
        components[left] += right
    else:
        components[left] = right
    
    for r in right:
        if (r, left) not in connections and (left, r) not in connections:
            connections.append((r, left))
        if r in components:
            components[r].append(left)
        else:
            components[r] = [left]

# for k, v in components.items():
#     print(k, v)
# print()

# for c in connections:
#     print(c)

def recursive():
    return

def separate_components(stuff, com):
    for s in stuff:
        left, right = s

        if len(com[left]) == 1:
            com.remove(left)
        else:
            com[left].remove(right)
        if len(com[right]) == 1:
            com.remove(right)
        else:
            com[right].remove(left)

for i, a in enumerate(connections):
    for j, b in enumerate(connections):
        l, r = b
        if l in a or r in a or j <= i:
            continue
        for k, c in enumerate(connections):
            l, r = c
            if l in a or l in b or r in a or r in b or k <= i or k <= j:
                continue
            assert a != b != c
            this_com = deepcopy(components)
            # separate_components([a, b, c], this_com)
