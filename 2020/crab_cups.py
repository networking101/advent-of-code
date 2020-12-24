from copy import deepcopy
#pi = "389125467"
pi = "871369452"

#ans = "silver"
ans = "gold"

origpi = deepcopy(pi)
pilen = len(pi)

pi = [int(x) for x in pi]

lowest = int(min(pi))
highest = int(max(pi))

numrounds = 100

if ans == "gold":
    numrounds = 10000000
    while highest < 1000000:
        highest += 1
        pi.append(highest)


data = []
data.append([0, 0])
for i in range(len(pi)):
    data.append((0, 0, []))

def porder(s):
    initial = s
    out = str(s)
    s = data[s][1]
    while s != initial:
        out += str(s)
        s = data[s][1]
    return out

data[pi[0]] = [pi[highest-1], pi[1]]
for i in range(1, highest-1):
    data[pi[i]] = [pi[i-1], pi[i+1]]
data[pi[highest-1]] = [pi[highest-2], pi[0]]


curr = pi[0]
for i in range(numrounds):
    precurr, nextcurr = data[curr]

    currcut = []
    tnext = nextcurr
    for j in range(3):
        currcut.append(tnext)
        tnext = data[tnext][1]
    
    dest = curr - 1
    if dest < lowest:
        dest = highest
    while dest in currcut:
        dest = dest - 1
        if dest < lowest:
            dest = highest

    predest, nextdest = data[dest]

    # cut out currcut
    data[curr][1] = data[currcut[2]][1]
    data[dest][0] = data[currcut[0]][0]

    # insert currcut
    data[dest][1] = currcut[0]
    data[nextdest][0] = currcut[2]
    data[currcut[0]][0] = dest
    data[currcut[2]][1] = nextdest

    curr = data[curr][1]

if ans == "silver":
    print(porder(1)[1:])

if ans == "gold":
    first = data[1][1]
    second = data[first][1]
    print(first*second)
        
