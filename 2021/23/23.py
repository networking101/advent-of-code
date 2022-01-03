from copy import deepcopy
from time import time

starttime = time()

with open("input", "r") as fp:
    lines = [line.rstrip() for line in fp]

initialPositions = {}
finalPositions = {'A':[(2,3), (3,3)], 'B':[(2,5), (3,5)], 'C':[(2,7), (3,7)], 'D':[(2,9), (3,9)]}
restingPositions = [(1,1), (1,2), (1,4), (1,6), (1,8), (1,10), (1,11)]
passingPositions = [(2,3), (2,5), (2,7), (2,9), (3,3), (3,5), (3,7), (3,9)]
cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

finalCost = 999999999

for j in range(len(lines)):
    for i in range(len(lines[j])):
        if lines[j][i] in ["A", "B", "C", "D"]:
            tmp = lines[j][i]
            if lines[j][i] not in initialPositions:
                initialPositions[lines[j][i]] = {}
                initialPositions[lines[j][i]][0] = ((j,i), "start")
            else:
                initialPositions[lines[j][i]][1] = ((j,i), "start")

def checkIfDone(position):
    for bp in position:
        for p in position[bp]:
            if position[bp][p][1] != "done":
                return False
    return True

def getDPString(position):
    ret = ""

    for char in ['A', 'B', 'C', 'D']:
        tmp = []
        for i in position[char]:
            tmp.append(position[char][i][0])
        ret += str(min(tmp)) + str(max(tmp))

    return ret

def checkBlocked(first, second, rp):
    for i in range(min(first, second)+1, max(first, second)):
        if i%2 == 0:
            if (1, i) not in rp:
                return False

    return True


DP = {}
# currRP is resting places that are empty
# currPP is passing points that are empty
def solve(position, currRP, currPP):
    global finalCost
    if checkIfDone(position):
        return 0

    dpString = getDPString(position)
    if dpString in DP:
        return DP[dpString]
    minEnergy = [999999999999]
    for bp in position:
        for p in position[bp]:
            currPos, currState = position[bp][p]
            altPos, altState = position[bp][(p+1)%2]
            if currState == "done":
                continue

            if currState == "moved":
                topPlacement = finalPositions[bp][0]
                bottomPlacement = finalPositions[bp][1]
                # if the bottom placement for this character is open
                if bottomPlacement in currPP:
                    if checkBlocked(currPos[1], bottomPlacement[1], currRP):
                        npp = deepcopy(currPP)
                        npp.remove(bottomPlacement)
                        nrp = deepcopy(currRP)
                        nrp.append(currPos)
                        np = deepcopy(position)
                        np[bp][p] = (bottomPlacement, "done")
                        energyCost = (abs(bottomPlacement[0] - currPos[0]) + abs(bottomPlacement[1] - currPos[1])) * cost[bp]
                        best = solve(np, nrp, npp)
                        # we can return because this is the best decision to make
                        DP[dpString] = best + energyCost
                        return best + energyCost
                else:
                    if altState == "done":
                        # if the top placement for this chracter is open
                        if topPlacement in currPP:
                            if checkBlocked(currPos[1], topPlacement[1], currRP):
                                npp = deepcopy(currPP)
                                npp.remove(topPlacement)
                                nrp = deepcopy(currRP)
                                nrp.append(currPos)
                                np = deepcopy(position)
                                np[bp][p] = (topPlacement, "done")
                                energyCost = (abs(topPlacement[0] - currPos[0]) + abs(topPlacement[1] - currPos[1])) * cost[bp]
                                best = solve(np, nrp, npp)
                                #we can return because this is the best decision to make
                                DP[dpString] = best + energyCost
                                return best + energyCost

            if currState == "start":
                if currPos[0] == 3:
                    # if the bottom row is blocked, we cannot continue with this character
                    if (2, currPos[1]) not in currPP :
                        continue
                for rp in currRP:
                    # if the second leftmost or second rightmost values are blocked, we cannot get to these resting places
                    if rp[1] == 1 and (1,2) not in currRP:
                        continue
                    if rp[1] == 11 and (1,10) not in currRP:
                        continue

                    if checkBlocked(currPos[1], rp[1], currRP):
                        npp = deepcopy(currPP)
                        npp.append(currPos)
                        nrp = deepcopy(currRP)
                        nrp.remove(rp)

                        np = deepcopy(position)
                        np[bp][p] = ((rp[0], rp[1]), "moved")
                        energyCost = (abs(rp[0] - currPos[0]) + abs(rp[1] - currPos[1])) * cost[bp]
                        best = solve(np, nrp, npp)
                        minEnergy.append(best + energyCost)
    DP[dpString] = min(minEnergy)
    return min(minEnergy)

print(solve(initialPositions, deepcopy(restingPositions), []))

endtime = time()
print(endtime - starttime)