with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

machines_silver = []
machines_gold = []

curr_machine_silver = {}
curr_machine_gold = {}
for line in lines:
    if not line:
        machines_silver.append(curr_machine_silver)
        machines_gold.append(curr_machine_gold)
        curr_machine_silver = {}
        curr_machine_gold = {}
        continue

    left, right = line.split(": ")

    if left[:6] == "Button":
        button = left.split()[1]
        x, y = right.split(", ")
        x = int(x.split("+")[1])
        y = int(y.split("+")[1])
        curr_machine_silver[button] = (x, y)
        curr_machine_gold[button] = (x, y)

    if left == "Prize":
        x, y = right.split(", ")
        x = int(x.split("=")[1])
        y = int(y.split("=")[1])
        curr_machine_silver["Prize"] = (x, y)
        curr_machine_gold["Prize"] = (x + 10000000000000, y + 10000000000000)
machines_silver.append(curr_machine_silver)
machines_gold.append(curr_machine_gold)

silver = 0
for m in machines_silver:
    ax, ay = m["A"]
    bx, by = m["B"]
    px, py = m["Prize"]

    # Solve for b
    d = py/ay - px/ax
    e = by/ay - bx/ax

    b = round(d/e, 3)
    a1 = round((px - (b * bx)) / ax, 3)
    a2 = round((py - (b * by)) / ay, 3)

    # check if b1 == b2 (intersection exists)
    # check if we are dealing with whole numbers (no half button presses)
    # check that we are below 100 button presses
    if a2 == a1 and b%1 == 0 and a1%1 == 0 and a1 <= 100 and b <= 100:
        silver += int(a1*3 + b)

print(silver)

gold = 0
for m in machines_gold:
    ax, ay = m["A"]
    bx, by = m["B"]
    px, py = m["Prize"]

    # Solve for b
    d = py/ay - px/ax
    e = by/ay - bx/ax

    b = round(d/e, 3)
    a1 = round((px - (b * bx)) / ax, 3)
    a2 = round((py - (b * by)) / ay, 3)

    # check if b1 == b2 (intersection exists)
    # check if we are dealing with whole numbers (no half button presses)
    # check that we are below 100 button presses
    if a2 == a1 and b%1 == 0 and a1%1 == 0:
        gold += int(a1*3 + b)

print(gold)