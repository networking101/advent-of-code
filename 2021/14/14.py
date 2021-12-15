from collections import Counter
from copy import deepcopy
from time import time

start = time()

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

template = lines.pop(0)
backup_template = deepcopy(template)
lines.pop(0)

rules = {}
for line in lines:
    a, b = line.split(" -> ")
    rules[a] = b

templateDict = {}
for x in rules.values():
    templateDict[x] = 0

def solve(t):
    for _ in range(10):
        #print(_)
        newT = t[0]
        for i in range(1, len(t)):
            newT += rules[t[i-1:i+1]]
            newT += t[i]
        t = newT
    return t

tempList = list(solve(template))
juju = Counter(tempList)
tl = juju.values()

print(max(tl) - min(tl))

# Gold

def solve2(t):
    for _ in range(20):
        newT = t[0]
        for i in range(1, len(t)):
            pair = t[i-1:i+1]
            newT += rules[pair]
            newT += t[i]
        t = newT

    tmpDict = Counter(list(t))
    tmpDict[t[-1]] -= 1
    return (t[:-1], tmpDict)

template = backup_template
counts = {}
finalDict = {}
newTemplate = ""

# complete steps 1-20
for i in range(1, len(template)):
    pair = template[i-1:i+1]
    currTemplate, tmpDict = solve2(pair)
    tDict = deepcopy(templateDict)
    for x in tmpDict:
        tDict[x] += tmpDict[x]
    newTemplate += currTemplate
    for t in tDict:
        finalDict[pair] = tDict
newTemplate += template[-1]

# complete steps 21-40
template = newTemplate
for r in rules:
    if r in finalDict:
        continue
    _, tmpDict = solve2(r)
    tDict = deepcopy(templateDict)
    for x in tmpDict:
        tDict[x] += tmpDict[x]
    finalDict[r] = tDict

finalfinalDict = deepcopy(templateDict)
for j in range(1, len(template)):
    pair = template[j-1:j+1]
    for i in finalDict[pair]:
        finalfinalDict[i] += finalDict[pair][i]

finalfinalDict[template[-1]] += 1

tl = finalfinalDict.values()
print(max(tl) - min(tl))
end = time()
print("Runtime: " + str(end-start))