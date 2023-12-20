import math

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

flip_flops = {}
conjunctions = {}
broadcaster = []

ff_states = {}
c_states = {}

for line in lines:
    if line[0] == '&':
        l = line[1:].split()
        name = l[0]
        output = [z.replace(',', '').strip() for z in l[2:]]
        conjunctions[name] = output
        c_states[name] = {}

for line in lines:
    if line[0] == '%':
        l = line[1:].split()
        name = l[0]
        output = [z.replace(',', '').strip() for z in l[2:]]
        flip_flops[name] = output
        ff_states[name] = 0

        # put flip-flop in the necessary c_states
        for k, v in c_states.items():
            if k in output:
                c_states[k][name] = 0
    elif line[:11] == 'broadcaster':
        l = line.split()
        name = l[0]
        output = [z.replace(',', '').strip() for z in l[2:]]
        broadcaster = output

# return true if any flip-flops are off
def check_flip_flops():
    for k, v in ff_states.items():
        if v == 1:
            return True
    return False

# return true if any conjunctions are off
def check_conjunctions():
    for k, v in c_states.items():
        for kk, vv in v.items():
            if vv == 1:
                return True
    return False

high = 0
low = 0

zg_stored = {}

start = True
button_count = 0
while button_count < 1000 or len(zg_stored) < 4:
# while True:
    start = False

    if button_count == 1000:
        print(high * low)

    # press button
    queue = []
    for n in broadcaster:
        queue.append([n, 0, 'broadcaster'])
    button_count += 1
    low += 1

    while queue:
        name, signal, previous = queue.pop(0)

        if signal:
            high += 1
        else:
            low += 1

        if name == 'zg':
            if signal and previous not in zg_stored:
                zg_stored[previous] = button_count
        
        if name in flip_flops and not signal:
            if ff_states[name]:
                ff_states[name] = 0
            else:
                ff_states[name] = 1
            for f in flip_flops[name]:
                queue.append([f, ff_states[name], name])
            

        if name in conjunctions:
            c_states[name][previous] = signal
            hol = False
            for k, v in c_states[name].items():
                if v == 0:
                    hol = True
                    break
            for f in conjunctions[name]:
                if not hol:
                    queue.append([f, 0, name])
                else:
                    queue.append([f, 1, name])

lcm = 1
for k, v in zg_stored.items():
    lcm = abs(lcm * v) // math.gcd(lcm, v) 
print(lcm)