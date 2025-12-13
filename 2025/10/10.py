from copy import deepcopy

with open("input", "r") as fp:
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

b = []
c = []

def find_new_buttons(done_buttons, curr_state):
    global b
    global c

    # print(b, c)

    new_set_buttons = []

    min_val = 999999999
    min_state = 0
    # print(curr_state, c)
    for i, (cs, es) in enumerate(zip(curr_state, c)):
        if cs != es and es < min_val:
            min_state = i
            min_val = es

    # print(min_state, min_val)

    for btn in b:
        if btn not in done_buttons and min_state in btn:
            new_set_buttons.append(btn)

    return new_set_buttons

fewest_buttons = 999999999
def recursion(i, set_buttons, done_buttons, curr_state):
    global b
    global c
    global fewest_buttons

    # print("i, set_buttons, done_buttons, curr_state")
    # print(i, set_buttons, done_buttons, curr_state)
    # input()

    if i >= fewest_buttons:
        return 999999999

    if curr_state == c:
        print(f"new fewest: {i}")
        fewest_buttons = i
        return i

    if len(set_buttons) == 0:
        set_buttons = find_new_buttons(done_buttons, curr_state)

        # this path exausted all our button options without reaching the goal state
        if len(set_buttons) == 0:
            return 999999999

    # print(set_buttons)
    # exit(0)
    need_to_remove_button = False
    result = 999999999
    for sb in set_buttons:
        if i == 0:
            print(f"new top set: {sb}")
        new_curr_state = deepcopy(curr_state)

        for state in sb:
            new_curr_state[state] += 1

            # if we reached an end condition for a state, need to remove the buttons for future calls
            if new_curr_state[state] == c[state]:
                need_to_remove_button = True

        tmp = 999999999
        # if i == 58:
        #     print("JUJU sb set_buttons need_to_remove_button")
        #     print(f"JUJU {sb} {set_buttons} {need_to_remove_button}")
        if need_to_remove_button:
            tmp = recursion(i + 1, [], done_buttons + set_buttons, new_curr_state)
        else:
            tmp = recursion(i + 1, set_buttons, done_buttons, new_curr_state)

        if tmp < result:
            result = tmp

    # print(f"result: {result}, {i}")
    return result

gold = 0
for k, line in enumerate(lines):
    print(k)
    a, b = line.split(']')
    b, c = b.split('{')

    a = a[1:]
    b = b.strip().split()
    b = [[int(x) for x in y[1:-1].split(',')] for y in b]
    c = [int(x) for x in c[:-1].split(',')]

    # if we sort the buttons in order of largest to smallest, we should increase performance
    # not enough
    # b = sorted(b, key=len, reverse=True)

    # print(a, b, c)
    # exit(0)
    
    curr_state = [0] * len(c)
    
    # reset globals
    fewest_buttons = 999999999
    print(b, c)
    tmp = recursion(0, [], [], curr_state)
    print(tmp)
    print()
    # exit(0)

    gold += tmp


print("GOLD")
print(gold)