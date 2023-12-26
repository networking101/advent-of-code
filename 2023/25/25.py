from copy import deepcopy
import random
from collections import Counter

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

components = {}
connections = []
nodes = []

for line in lines:
    left, right = line.split(':')
    right = right.split()

    if left in components:
        components[left] += right
    else:
        components[left] = right
    if left not in nodes:
        nodes.append(left)
    
    for r in right:
        if (r, left) not in connections and (left, r) not in connections:
            connections.append((r, left))
        if r in components:
            components[r].append(left)
        else:
            components[r] = [left]
        if r not in nodes:
            nodes.append(r)

pairs = {}    
def find_end(curr, end, found, tf):
    queue = [curr]
    while queue:
        curr = queue.pop(0)
        if curr == end:
            tf += deepcopy(found)
            return
        random.shuffle(components[curr])
        for nxt in components[curr]:
            if nxt not in found:
                found.append(nxt)
                queue.append((nxt))

def get_num_nodes(curr, removed):
    found = [curr]
    queue = [curr]
    while queue:
        curr = queue.pop(0)
        random.shuffle(components[curr])
        for nxt in components[curr]:
            if nxt not in found and nxt not in removed:
                found.append(nxt)
                queue.append((nxt))
    return len(found)

print("Stop running when you think you found the answer")
while True:
    count = 0
    total_found = []
    while count < 300:
        start = random.randint(0, len(nodes) - 1)
        end = random.randint(0, len(nodes) - 1)
        if start == end:
            continue

        start = nodes[start]
        end = nodes[end]
        find_end(start, end, [start], total_found)
        count += 1

    removed = []
    tf = Counter(total_found)
    tf = [(v, k) for k, v in tf.items()]
    tf.sort(reverse=True)
    count = 0
    for v, k in tf:
        removed.append(k)
        count += 1
        if count == 6:
            break

    a = nodes[random.randint(0, len(nodes) - 1)]
    while a in removed:
        a = nodes[random.randint(0, len(nodes) - 1)]
    a_len = get_num_nodes(a, removed)


    b = nodes[random.randint(0, len(nodes) - 1)]
    while a in removed:
        b = nodes[random.randint(0, len(nodes) - 1)]
    b_len = get_num_nodes(b, removed)
    
    if b_len + a_len + 6 == len(nodes):
        print((b_len+3) * (a_len+3))

