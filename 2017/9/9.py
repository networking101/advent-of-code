with open("input", "r") as fp:
    line = [line.strip() for line in fp][0]

group_stack = []
garbage_flag = 0

silver = 0
gold = 0

i = 0
while i < len(line):
    c = line[i]
    if not garbage_flag:
        if c == "{":
            group_stack.append(i)
        if c == "}" and len(group_stack) > 0:
            silver += len(group_stack)
            group_stack.pop()
    if c == "<":
        if not garbage_flag:
            gold -= 1
        garbage_flag = 1
    if c == ">":
        garbage_flag = 0
    if c == "!":
        i += 1
        gold -= 1

    if garbage_flag:
        gold += 1

    i += 1

print(silver)
print(gold)

#6429 too low