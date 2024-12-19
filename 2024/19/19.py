with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

patterns = [list(x) for x in lines.pop(0).split(', ')]
lines.pop(0)

designs = [list(x) for x in lines]

DP = {}

def recurse(design):
    if len(design) == 0:
        return 1

    if str(design) in DP:
        return DP[str(design)]

    res = 0
    for p in patterns:
        if p == design[:len(p)]:
            res += recurse(design[len(p):])
    
    DP[str(design)] = res

    return res

silver = 0
gold = 0
for d in designs:
    res = recurse(d)
    if res != 0:
        silver += 1
    gold += res

print(silver)
print(gold)