with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

tot_silver = 0
tot_gold = 0
for line in lines:
    a, b = line .split(",")
    a = a.split("-")
    b = b.split("-")
    a = set(range(int(a[0]), int(a[1])+1))
    b = set(range(int(b[0]), int(b[1])+1))

    if a.issubset(b) or b.issubset(a):
        tot_silver += 1

    for x in a:
        if x in b:
            tot_gold += 1
            break

print(tot_silver)
print(tot_gold)