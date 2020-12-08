from copy import deepcopy

with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

mol = lines[-1]

lines.pop()
lines.pop()

conv = {}
for line in lines:
    a, b = [x.strip() for x in line.split("=>")]
    if a not in conv:
        conv[a] = [b]
    else:
        conv[a].append(b)

endmol = set()
data = {}

"""
for j in conv:
    data[j] = []
    ti = 0
    while True:
        ti = mol.find(j, ti)
        if ti == -1:
            break

        for i in conv[j]:
            ts = ""
            if ti > 0:
                ts += mol[:ti]
            ts += i
            if ti < len(mol)-len(j):
                ts += mol[ti+len(j):]
            endmol.add(ts)
            data[j].append(ts)
        ti += len(j)
"""

revs = {}
outs = []

for i in conv:
    for j in conv[i]:
        revs[j] = i
        outs.append(j)

cnt = 0

def recurse(mol):
    global cnt
    global data
    i = 1
    while i < len(mol):
        found = False
        if mol[:i] in outs:
            cnt += 1
            return (revs[mol[:i]], len(mol[:i]))
        for j in outs:
            if mol[:i] in j:
                found = True
                i += 1
                break
        if found == False:
            subs, l = recurse(mol[i-1:])
            mol = mol[:i-1] + subs + mol[i+l-1:]
            i = 1

recurse(mol)

print(cnt)

print(len(endmol))
