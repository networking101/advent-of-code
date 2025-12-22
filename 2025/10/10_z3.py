import z3

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



gold = 0
for k, line in enumerate(lines):
    a, b = line.split(']')
    b, c = b.split('{')

    a = a[1:]
    b = b.strip().split()
    b = [[int(x) for x in y[1:-1].split(',')] for y in b]
    c = [int(x) for x in c[:-1].split(',')]

    smt = z3.Optimize()

    # create collection of buttons
    z3_buttons = []
    for i, buttons in enumerate(b):
        z3_buttons.append(z3.Int(f"B{i}"))

    # create constraints: num button pushes == voltage
    z3_equations = []
    for i, x in enumerate(c):
        terms = []
        for j, button in enumerate(b):
            if i in button:
                terms.append(z3_buttons[j])
        
        z3_equations.append((sum(terms) == c[i]))

    # create smt optimizer
    optimizer = z3.Optimize()

    # minimize optimizer to total number of button presses
    optimizer.minimize(sum(z3_buttons))

    # add constraint
    for e in z3_equations:
        optimizer.add(e)

    # create constraint: num button pushes >= 0
    for bb in z3_buttons:
        optimizer.add(bb >= 0)

    assert optimizer.check() == z3.sat

    model = optimizer.model()
    for declaration in model.decls():
        gold += model[declaration].as_long()

print(gold)