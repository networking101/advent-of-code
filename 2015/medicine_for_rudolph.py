from copy import deepcopy
import re

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

print("Silver:  " + str(len(endmol)))


revs = {}
outs = []

for i in conv:
    for j in conv[i]:
        revs[j] = i
        if revs[j] != 'e':
            outs.append(j)

doubles = {}
deuces = {}
trips = {}
pairs = {}

tri = re.compile('.*Rn.*Y.*Ar')
pair = re.compile('.*Rn.*Ar')

for i in revs:
    if revs[i] == 'e':
        continue

    if i == revs[i]*2:
        doubles[i] = revs[i]
    elif len(i) <= 4:
        deuces[i] = revs[i]
    elif tri.match(i):
        trips[i] = revs[i]
    elif pair.match(i):
        pairs[i] = revs[i]

cnt = 0
oldmol = ""
while oldmol != mol:
    oldmol = mol
    found = False

    # check for doubles
    for i in doubles:
        while i in mol:
            found = True
            cnt += 1
            mol = mol.replace(i, doubles[i], 1)
    
    # check for deuces
    for i in deuces:
        while i in mol:
            found = True
            cnt += 1
            mol = mol.replace(i, deuces[i], 1)

    if found == True:
        continue

    # check for trips
    for i in trips:
        while i in mol:
            found = True
            cnt += 1
            mol = mol.replace(i, trips[i], 1)

    # check for pairs
    for i in pairs:
        while i in mol:
            found = True
            cnt += 1
            mol = mol.replace(i, pairs[i], 1)
        
    if found == True:
        continue

# molecules are mixed up now, count special molecules

moll = re.findall('[A-Z][^A-Z]*', mol)

a = len(moll)
b = moll.count("Rn")

s = a - b*4 + 1

print("Gold:  " + str(s + cnt))
