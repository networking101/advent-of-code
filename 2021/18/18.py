import json
from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

result = ""

def recursePrint(places, curr):
    global result
    result += '['
    # left
    tcurr = curr + "0"
    if tcurr in places:
        result += str(places[tcurr])
    else:
        recursePrint(places, tcurr)

    result += ','

    tcurr = curr + "1"
    if tcurr in places:
        result += str(places[tcurr])
    else:
        recursePrint(places, tcurr)
    
    result += ']'

    return

def printHomework(places):
    global result
    recursePrint(places, "")
    print(result)
    result = ""

def fillPlaces(places, position, curr):
    for a in range(len(curr)):
        p = deepcopy(position)
        p += str(a)
        if type(curr[a]) == type([]):
            fillPlaces(places, p, curr[a])
        else:
            places[p] = curr[a]

    return

def findLeftmost(places):
    curr = '0'
    while curr not in places:
        curr += '0'
    return curr

def findLeft(places, left):
    curr = left[:-1]
    if curr == '0':
        # move over and down tree
        l = left[:-1] + '0'
        while l not in places:
            l += '1'
        return l
    # move up tree
    l = left[:-1]
    while l:
        if l[-1] == '0':
            l = l[:-1]
        else:
            l = l[:-1] + '0'
            # move down tree
            while l not in places:
                l += '1'
            return l
    return None

def findRight(places, right):
    curr = right[-1]
    if curr == '0':
        # move over and down tree
        r = right[:-1] + '1'
        while r not in places:
            r += '0'
        return r
    # move up tree
    r = right[:-1]
    while r:
        if r[-1] == '1':
            r = r[:-1]
        else:
            r = r[:-1] + '1'
            # move down tree
            while r not in places:
                r += '0'
            return r
    return None

def explode(places, position):
    left = position
    right = position[:-1] + "1"

    # nextLeft is the position of the next value to the left
    nextLeft = findLeft(places, left)
    # nextRight is the position of the next value to the left
    nextRight = findRight(places, right)

    # solve left
    # immediateLeft is the position of explodings pair value at the same level in the tree
    immediateLeft = left[:-2] + "0"
    # if we have a regular number pair add left value to it
    if immediateLeft in places:
        places[immediateLeft] += places[left]
    # Otherwise, set it to 0
    else:
        places[immediateLeft] = 0
        # if there is a value to the left, change it
        if nextLeft:
            places[nextLeft] += places[left]

    # solve right
    # immediateRight is the position of explodings pair value at the same level in the tree
    immediateRight = right[:-2] + "1"
    # if we have a regular number pair add right value to it
    if immediateRight in places:
        places[immediateRight] += places[right]
    # Otherwise, set it to 0
    else:
        if not nextRight:
            places[immediateRight] = 0
        elif len(nextRight) != 5:
            places[immediateRight] = 0
        else:
            if nextRight[:3] != right[:3]:
                places[immediateRight] = 0
        # if there is a value to the right, change it
        if nextRight:
            places[nextRight] += places[right]

    places.pop(left)
    places.pop(right)

    return nextRight

def split(places, position):
    places[position + "0"] = places[position]//2
    places[position + "1"] = places[position] - places[position + "0"]
    places.pop(position)
    return

def addition(places, nextPlaces):
    newPlaces = {}
    for p in places:
        newPlaces['0' + p] = places[p]

    for n in nextPlaces:
        newPlaces['1' + n] = nextPlaces[n]

    return newPlaces

def sortKeys(places, newPlaces, curr):
    # left
    newCurr = curr + "0"
    if len(newCurr) < 5:
        sortKeys(places, newPlaces, newCurr)

    # add to new list
    if curr in places:
        newPlaces[curr] = places[curr]

    # right
    newCurr = curr + "1"
    if len(newCurr) < 5:
        sortKeys(places, newPlaces, newCurr)

def cleanLine(places):
    modified = True
    while modified:
        p = findLeftmost(places)
        modified = False
        # while p is not the most rightmost element
        while True:
            if len(p) == 5:
                tmp = places[p]
                p = explode(places, p)
                modified = True
                if not p:
                    break
            else:
                p = findRight(places, p)
                if not p:
                    break
        p = findLeftmost(places)
        while True:
            if type(places[p]) == type(0) and places[p] > 9:
                tmp = places[p]
                split(places, p)
                modified = True
                break
            p = findRight(places, p)
            if not p:
                break

places = {}
curr = json.loads(lines.pop(0))
fillPlaces(places, "", curr)
cleanLine(places)

for line in lines:
    # add new line
    nPlaces = {}
    next = json.loads(line)
    fillPlaces(nPlaces, "", next)
    places = addition(places, nPlaces)

    # clean up math problem
    cleanLine(places)

def magnitude(places):
    depth = 4
    while depth >= 1:
        nplaces = deepcopy(places)
        for p in places:
            if len(p) == depth and p in nplaces:
                if p[-1] == '0':
                    other = p[:-1] + '1'
                    nplaces[p[:-1]] = places[p]*3 + places[other]*2
                else:
                    other = p[:-1] + '0'
                    nplaces[p[:-1]] = places[other]*3 + places[p]*2
                nplaces.pop(p)
                nplaces.pop(other)
        places = nplaces
        depth -= 1

    return places['']

print(magnitude(places))

sums = []
# Gold
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
            
        places = {}
        curr = json.loads(lines[i])
        fillPlaces(places, "", curr)
        cleanLine(places)

        # add new line
        nPlaces = {}
        next = json.loads(lines[j])
        fillPlaces(nPlaces, "", next)
        places = addition(places, nPlaces)

        # clean up math problem
        cleanLine(places)

        sums.append(magnitude(places))

print(max(sums))