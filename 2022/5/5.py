from copy import deepcopy

with open("input", "r") as fp:
    lines = [line for line in fp]

stacks = []
instructions = []
flag = False
stack_size = 0
for line in lines:
    if " 1   2 " in line:
        stack_size = int(len(line)/4)
    if not line.strip():
        flag = True
        continue
    if flag:
        instructions.append(line)
    else:
        stacks.append(line)

stack_check = {}
stack_set = {}
for i in range(stack_size):
    stack_check[(i*4)+1] = str(i+1)
    stack_set[str(i+1)] = []

for s in stacks[:-1]:
    for i in range(1, len(s), 4):
        if s[i] != " ":
            stack_set[stack_check[i]].insert(0, s[i])

sc = deepcopy(stack_check)
ss = deepcopy(stack_set)

for i in instructions:
    obs = i.split()
    val = obs[1]
    frm = obs[3]
    to = obs[5]

    for x in range(int(val)):
        tmp = stack_set[frm].pop()
        stack_set[to].append(tmp)

    mov = (-1*int(val))
    tmp = ss[frm][mov:]
    ss[frm] = ss[frm][:mov]
    ss[to] = ss[to] + tmp

for s in stack_set:
    print(stack_set[s][-1], end='')
print()

for s in ss:
    print(ss[s][-1], end='')
print()

# for i in instructions:
#     obs = i.split()
#     val = obs[1]
#     frm = obs[3]
#     to = obs[5]

#     mov = (-1*int(val))
#     tmp = ss[frm][mov:]
#     ss[frm] = ss[frm][:mov]
#     ss[to] = ss[to] + tmp

# for s in ss:
#     print(ss[s][-1], end='')
# print()