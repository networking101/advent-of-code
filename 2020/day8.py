from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

for j in range(len(lines) + 1):
    ll = deepcopy(lines)
    if j:
        a, b = ll[j].split()
        if a == "nop":
            ll[j] = "jmp " + b
        elif a == "jmp":
            ll[j] = "nop " + b
        else:
            continue

    i = 0
    acc = 0
    inst = []
    while True:
        try:
            t,u = ll[i].split()
        except:
            print(acc)
            exit(0)
        if t == "nop":
            i += 1
        if t == "acc":
            acc += int(u)
            i += 1
        if t == "jmp":
            i += int(u)
        
        if i in inst:
            if not j:
                print(acc)
            break
        inst.append(i)

