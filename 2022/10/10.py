with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

tot = 0
cycle = 0
check = 20
x = 1
current = ['#'] * 3 + ['.'] * 37
CRT = ""
for line in lines:
    # noop
    if line == "noop":
        cycle += 1
        if current[(cycle-1)%40] == "#":
            CRT += "#"
        else:
            CRT += "."
        if cycle == check:
            tot += x * check
            check += 40
        continue

    # add first cycle
    this_x = int(line.split()[1])
    cycle += 1
    if current[(cycle-1)%40] == "#":
        CRT += "#"
    else:
        CRT += "."
    if cycle == check:
        tot += x * check
        check += 40

    # add second cycle
    cycle += 1
    if current[(cycle-1)%40] == "#":
        CRT += "#"
    else:
        CRT += "."
    if cycle == check:
        tot += x * check
        check += 40

    # update x
    x += this_x
    current = ["."] * (x-1) + ["#"] * 3 + ["."] * (40 - (x-1) - 3)

print(tot)
for x in range(len(CRT)):
    if x % 40 == 0:
        print()
    print(CRT[x], end='')
print()