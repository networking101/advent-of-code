from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

p1 = []
p2 = []
x = p1
for line in lines[1:]:
    if line:
        if "Player" in line:
            x = p2
            continue
        x.append(int(line))


def recurse(n1, n2, state, ans):
    while n1 and n2:

        if ans == 'g':
            if n1 + [0] + n2 in state:
                #print("Same State")
                return (1, n1)
            state.append(n1 + [0] + n2)


        a = n1.pop(0)
        b = n2.pop(0)
        if ans == 'g' and a <= len(n1) and b <= len(n2):
            x, _ = recurse(deepcopy(n1)[:a], deepcopy(n2)[:b], [], ans)
            if x == 1:
                n1.append(a)
                n1.append(b)
            else:
                n2.append(b)
                n2.append(a)
            continue
        if a > b:
            n1.append(a)
            n1.append(b)
        else:
            n2.append(b)
            n2.append(a)
    
    if n1:
        return (1, n1)
    else:
        return (2, n2)

_, final = recurse(deepcopy(p1), deepcopy(p2), [], 's')

tot = 0
ind = 1
for i in final[::-1]:
    tot += i*ind
    ind += 1

print("Silver:  " + str(tot))

_, final = recurse(p1, p2, [], 'g')

tot = 0
ind = 1
for i in final[::-1]:
    tot += i*ind
    ind += 1

print("Gold:  " + str(tot))