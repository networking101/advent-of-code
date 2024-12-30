with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

secrets = [int(x) for x in lines]

sequences = []
possible_combinations = set()

def process(s):
    s = ((s * 64) ^ s) % 16777216
    s = (int(s / 32) ^ s) % 16777216
    s = ((s * 2048) ^ s) % 16777216
    return s

silver = 0
for i, s in enumerate(secrets):
    start = s
    changes = {}
    last_4_changes = []

    for j in range(2000):
        last = s % 10
        s = process(s)

        last_4_changes.append((s % 10) - last)
        if len(last_4_changes) == 4:
            if str(last_4_changes) not in changes:
                changes[str(last_4_changes)] = s % 10
            possible_combinations.add(str(last_4_changes))
            last_4_changes.pop(0)

    sequences.append(changes)
    silver += s

print(silver)

gold = 0
for pc in possible_combinations:
    best = 0
    for changes in sequences:
        if pc in changes:
            tmp = changes[pc]
            best += changes[pc]
    if best > gold:
        gold = best

print(gold)