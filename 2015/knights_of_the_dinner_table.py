from copy import deepcopy

with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

data = {}
left = []

for line in lines:
    vals = line.split()
    if vals[0] not in data:
        data[vals[0]] = []
    other = vals[-1][:-1]
    happiness = int(vals[3])
    if vals[2] == "lose":
        happiness *= -1
    data[vals[0]].append((other, happiness))
    if vals[0] not in left:
        left.append(vals[0])

orig = left[0]
count = 0

# gold

for i in data:
    data[i].append(("you", 0))
data["you"] = []
for i in left:
    data["you"].append((i, 0))
left.append("you")


def recurse(old, l, tot):
    global count
    global orig
    global data

    if len(l) == 0:
        for j in data[old]:
            if j[0] == orig:
                tot += j[1]
        for j in data[orig]:
            if j[0] == old:
                tot += j[1]
        return tot

    templ = []
    for i in l:
        nex = 0
        newl = deepcopy(l)
        oldl = data[old]
        nexl = data[i]
        newl.remove(i)
        newtot = tot
        for j in oldl:
            if j[0] == i:
                newtot += j[1]
        for j in nexl:
            if j[0] == old:
                newtot += j[1]
        #count += 1
        #if count == 3:
            #exit(0)
        templ.append(recurse(i, newl, newtot))
        
    return max(templ)

for i in data:
    print(i, end="  ")
    print(data[i])

tot = 0
old = left.pop(0)
tot = recurse(old, left, tot)
print("")
print(tot)
