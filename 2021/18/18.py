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

def followUpLeft(places, left):
    curr = left[:-1]
    # move up tree
    while curr:
        if curr[-1] == '0':
            curr = curr[:-1]
        else:
            curr = curr[:-1] + "0"
            # move down tree
            while curr not in places:
                curr += "1"
            places[curr] += places[left]
            return
    return

def followUpRight(places, right):
    curr = right[:-1]
    # move up tree
    while curr:
        if curr[-1] == '1':
            curr = curr[:-1]
        else:
            curr = curr[:-1] + "1"
            # move down tree
            while curr not in places:
                curr += "0"
            places[curr] += places[right]
            return
    return

def explode(places, position):
    #if position[-2] == '1' and position[:-2]+"01":
    #    return True
    if position[-1] == "0":
        left = position
        right = position[:-1] + "1"
    else:
        right = position
        left = position[:-1] + "0"

    oldPlaces = deepcopy(places)

    # solve left
    immediateLeft = left[:-2] + "0"
    if immediateLeft in oldPlaces:
        places[immediateLeft] += places[left]
        #places[immediateLeft[:-1] + '1'] = 0
    else:
        followUpLeft(places, left)
        #places[immediateLeft] = 0
        if left[-2] == "0":
            places[immediateLeft] = 0

    # solve right
    immediateRight = right[:-2] + "1"
    if immediateRight in oldPlaces:
        places[immediateRight] += places[right]
        #places[immediateRight[:-1] + '0'] = 0
    else:
        followUpRight(places, right)
        if right[-2] == "1":
            places[immediateRight] = 0

    places.pop(left)
    places.pop(right)
    return False

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


places = {}
position = ""
curr = json.loads(lines.pop(0))
fillPlaces(places, position, curr)
for line in lines:
    while True:
        modified = False
        for p in places:
            if len(p) == 5:
                if p[-2] == "1" and p[:-2]+"01" in places:
                    explode(places, p[:-2]+"01")
                else:
                    explode(places, p)
                printHomework(places)
                modified = True
                break
        if modified:
            continue
        modified = False
        for p in places:
            if type(places[p]) == type(0) and places[p] > 9:
                split(places, p)
                printHomework(places)
                modified = True
                break
        if not modified:
            break
    
    # add new line
    nextPlaces = {}
    nextPosition = ""
    next = json.loads(line)
    fillPlaces(nextPlaces, nextPosition, next)
    printHomework(places)
    places = addition(places, nextPlaces)
    printHomework(places)
    
while True:
    modified = False
    for p in places:
        if len(p) == 5:
            if p[-2] == "1" and p[:-2]+"01" in places:
                explode(places, p[:-2]+"01")
            else:
                explode(places, p)
            #printHomework(places)
            modified = True
            break
    if modified:
        continue
    modified = False
    for p in places:
        if type(places[p]) == type(0) and places[p] > 9:
            split(places, p)
            #printHomework(places)
            modified = True
            break
    if not modified:
        break

printHomework(places)