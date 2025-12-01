from copy import deepcopy

with open("input", "r") as fp:
    lines = [int(line.strip()) for line in fp]

lines_gold = deepcopy(lines)

position = 0
silver = 0
while position < len(lines):
    old_pos = position
    position += lines[position]
    lines[old_pos] += 1

    silver += 1

print(silver)

position = 0
gold = 0
while position < len(lines_gold):
    old_pos = position
    position += lines_gold[position]
    if lines_gold[old_pos] < 3:
        lines_gold[old_pos] += 1
    else:
        lines_gold[old_pos] -= 1

    gold += 1

print(gold)