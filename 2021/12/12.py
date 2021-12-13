from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

starting = []

for line in lines:
    l, r = line.split('-')
    if l == "start":
        starting.append(r)
    if r == "start":
        starting.append(l)
    

def recurse(char, foundCaves):
    global lines

    count = 0

    for line in lines:
        l, r = line.split('-')
        if (char == l or char == r) and "start" not in line:
            if r == "end" or l == "end":
                count += 1
                continue

            fc = deepcopy(foundCaves)
            if char == l:
                nxt = r
            else:
                nxt = l
            if nxt.islower():
                if nxt in foundCaves:
                    continue
                fc.append(nxt)
            count += recurse(nxt, fc)

    return count

def recurse2(char, foundCaves, smallCave):
    global lines

    count = 0

    for line in lines:
        l, r = line.split('-')
        if (char == l or char == r) and "start" not in line:
            if r == "end" or l == "end":
                count += 1
                continue

            fc = deepcopy(foundCaves)
            if char == l:
                nxt = r
            else:
                nxt = l
            if nxt.islower():
                if nxt in foundCaves:
                    if not smallCave:
                        count += recurse2(nxt, fc, True)
                    continue
                fc.append(nxt)
            count += recurse2(nxt, fc, smallCave)

    return count

# Silver
numPaths = 0
for char in starting:
    foundCaves = []
    if char.islower():
        foundCaves.append(char)
    numPaths += recurse(char, foundCaves)

print(numPaths)

# Gold
numPaths = 0
for char in starting:
    foundCaves = []
    if char.islower():
        foundCaves.append(char)
    numPaths += recurse2(char, foundCaves, False)

print(numPaths)