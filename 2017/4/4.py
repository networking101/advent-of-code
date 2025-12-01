with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

lines = [line.split() for line in lines]

def check_gold(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    for x in a:
        if x not in b:
            return False
        b.remove(x)
    
    return True

silver = 0
gold = 0
for line in lines:
    found_silver = 0
    found_gold = 0
    while line:
        curr = line.pop()
        if curr in line:
            found_silver = 1
        for rest in line:
            if check_gold(list(curr), list(rest)):
                found_gold = 1
    if not found_silver:
        silver += 1
    if not found_gold:
        gold += 1

print(silver)
print(gold)