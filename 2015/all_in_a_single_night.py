from copy import deepcopy

with open("text.txt", "r") as fp:
    lines = [line.split() for line in fp]

distances = []

for line in lines:
    distances.append((line[0], line[2], line[4]))

neighbors = {}

def findmindist(dist, start, sl):
    global neighbors

    minlist = []

    for i in sl:
        newdist = dist
        newlist = deepcopy(sl)
        newlist.remove(i)
        for j in neighbors[start]:
            if j[0] == i:
                newdist += j[1]
        minlist.append(findmindist(newdist, i, newlist))
    if len(minlist) > 0:
        mindist = max(minlist)
        return mindist
    return dist

for d in distances:
    temp1 = d[0]
    temp2 = d[1]
    if temp1 not in neighbors:
        neighbors[temp1] = []
    if temp2 not in neighbors[temp1]:
        neighbors[temp1].append([temp2, int(d[2])])

    if temp2 not in neighbors:
        neighbors[temp2] = []
    if temp1 not in neighbors[temp2]:
        neighbors[temp2].append([temp1, int(d[2])])

minlist = []
for a in neighbors:
    foundset = [a]
    startinglist = []
    for i in neighbors:
        if i != a:
            startinglist.append(i)
    minlist.append(findmindist(0, a, startinglist))
print(max(minlist))

