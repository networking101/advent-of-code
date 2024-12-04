import re

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]
puzzle_input = "".join(lines)

silver = 0
gold = 0

expression = r'mul\(\d{1,3},\d{1,3}\)'
mults = re.findall(expression, puzzle_input)

for m in mults:
    l, r = m.split(",")
    l = int(l[4:])
    r = int(r[:-1])
    silver += l * r

print(silver)

flag = True
for i, c in enumerate(puzzle_input):
    # print(flag, i)
    if flag:
        if i < len(puzzle_input) - 7 and puzzle_input[i:i+7] == "don't()":
            flag = False
        if i < len(puzzle_input) - 4 and puzzle_input[i:i+4] == "mul(" and len(re.findall(expression, puzzle_input[i:i+12])):
            l, r = re.findall(expression, puzzle_input[i:i+12])[0].split(",")
            l = int(l[4:])
            r = int(r[:-1])
            gold += l * r
    else:
        if i < len(puzzle_input) - 4 and puzzle_input[i:i+4] == "do()":
            flag = True

print(gold)