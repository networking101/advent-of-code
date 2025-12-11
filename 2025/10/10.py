from copy import deepcopy

with open("input2", "r") as fp:
    lines = [line.strip() for line in fp]


silver = 0
for k, line in enumerate(lines):
    a, b = line.split(']')
    b, c = b.split('{')

    a = a[1:]
    b = b.strip().split()
    b = [[int(x) for x in y[1:-1].split(',')] for y in b]
    c = [int(x) for x in c[:-1].split(',')]

    start_a = '.' * len(a)

    DP = []
    queue = [[0, [], start_a]]
    z = 0
    while queue:
        i, prev_buttons, lights = queue.pop(0)
        
        found = False
        for button in b:
            new_lights = ''
            for j in range(len(lights)):
                if j in button:
                    if lights[j] == '.':
                        new_lights += '#'
                    else:
                        new_lights += '.'
                else:
                    new_lights += lights[j]
        
            if new_lights == a:
                # print(prev_buttons + [button])
                silver += i + 1
                found = True
            else:
                if new_lights not in DP:
                    DP.append(new_lights)
                    queue.append([i + 1, prev_buttons + [button], new_lights])

            # if found:
            #     break
        if found:
            break

print(silver)

def remove_buttons(x, bs):
    new_bs = deepcopy(bs)
    for button in bs:
        if j in button:
            new_bs.remove(button)
    return new_bs

gold = 0
for k, line in enumerate(lines):
    print()
    print(k)
    a, b = line.split(']')
    b, c = b.split('{')

    a = a[1:]
    b = b.strip().split()
    b = [[int(x) for x in y[1:-1].split(',')] for y in b]
    c = [int(x) for x in c[:-1].split(',')]


    # print(a, b, c)
    start_c = [0] * len(c)
    
    DP = []
    queue = [[0, [], start_c, b]]
    z = 0
    while queue:
        i, prev_buttons, counts, bs = queue.pop(0)
        if i > z:
            print(i)
            z = i


        found = False

        new_bs = deepcopy(bs)
        for button in bs:
            new_counts = deepcopy(counts)
            max_jump = 999999999
            for j in (range(len(counts))):
                assert(new_counts[j] <= c[j])
                if (c[j] - new_counts[j]) < max_jump :
                    max_jump = (c[j] - new_counts[j])

            for j in (range(len(counts))):
                if j in button:
                    new_counts[j] += max_jump
                    if new_counts[j] == c[j]:
                        new_bs = remove_buttons(j, bs)

            if new_counts == c:
                print(f"MATCH: {i + max_jump}")
                gold += i + max_jump
                found = True
                break

            break_counts = False
            for nc, cc in zip(new_counts, c):
                if nc > cc:
                    break_counts = True
                    break
            if not break_counts and new_counts not in DP:
                DP.append(new_counts)
                queue.append([i + max_jump, prev_buttons + [button], new_counts, new_bs])

        if found:
            break

print("GOLD")
print(gold)