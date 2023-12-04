from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

finding = [2, 5]
finding = [17, 61]

bots = [[] for _ in range(1000)]
instructions = []

for line in lines:
    if line[:5] == "value":
        _, v, _, _, _, b = line.split()
        v, b = [int(z) for z in [v, b]]
        bots[b].append(v)
    
    if line[:3] == "bot":
        instructions.append(line)

count = 1

while instructions:
    new_instructions = deepcopy(instructions)
    for i in instructions:
        _, b, _, _, _, l_recv, l, _, _, _, h_recv, h = i.split()
        b, l, h = [int(z) for z in [b, l, h]]

        if len(bots[b]) != 2:
            continue

        if l_recv == 'bot':
            m = min(bots[b])
            bots[b].remove(m)
            bots[l].append(m)
            if finding[0] in bots[l] and finding[1] in bots[l]:
                print(l)

        if h_recv == 'bot':
            m = max(bots[b])
            bots[b].remove(m)
            bots[h].append(m)
            if finding[0] in bots[h] and finding[1] in bots[h]:
                print(h)

        if l_recv == "output" and l <= 2:
            m = min(bots[b])
            bots[b].remove(m)
            count *= m

        if h_recv == "output" and h <= 2:
            m = max(bots[b])
            bots[b].remove(m)
            count *= m

        new_instructions.remove(i)
    instructions = new_instructions

print(count)