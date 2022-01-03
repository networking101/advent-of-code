from copy import deepcopy
from time import time

starttime = time()

with open("inputgold", "r") as fp:
    lines = [line.rstrip() for line in fp]

roomDepth = 5

initialPositions = {}
finalPositions = {'A': 3, 'B': 5, 'C':7, 'D':9}
restingPositions = [1, 2, 4, 6, 8, 10, 11]
passingPositions = [(2,3), (2,5), (2,7), (2,9), (3,3), (3,5), (3,7), (3,9), (4,3), (4,5), (4,7), (4,9), (5,3), (5,5), (5,7), (5,9)]
cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

grid = []
for j in range(len(lines)):
    row = []
    for i in range(len(lines[j])):
        row.append(lines[j][i])
        if lines[j][i] in ["A", "B", "C", "D"]:
            if lines[j][i] not in initialPositions:
                initialPositions[lines[j][i]] = {}
                initialPositions[lines[j][i]][0] = ((j,i), "start")
            else:
                tmpKeys = initialPositions[lines[j][i]].keys()
                k = 0
                while k in tmpKeys:
                    k += 1
                initialPositions[lines[j][i]][k] = ((j,i), "start")
    grid.append(row)

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
        for _ in range(len(tmp)):
            c = min(tmp)
            ret += str(c)
            tmp.remove(c)

    return ret

def checkBlocked(cp, bp, second, rp, pp):
    # check passing positions
    for i in range(2, cp[0]):
        if (i, cp[1]) not in pp:
            return False

    # check resting positions
    for i in range(min(cp[1], second)+1, max(cp[1], second)):
        if i%2 == 0:
            if i not in rp:
                return False

    return True

def checkFinalStart(grid, position, bp, p):
    startPos = position[bp][p][0]
    if finalPositions[bp] != startPos[1]:
        return False
    for i in range(startPos[0]+1, roomDepth+1):
        if grid[i][startPos[1]] != bp:
            return False
    return True

def checkFinalReady(grid, position, bp, p):
    for i in range(roomDepth, 1, -1):
        if grid[i][finalPositions[bp]] == bp:
            continue
        if grid[i][finalPositions[bp]] == '.':
            for j in range(2, i):
                if grid[j][finalPositions[bp]] != '.':
                    return None
            return i
        return None
    
    return None


DP = {}
# currRP is resting places that are empty
# currPP is passing points that are empty
def solve(grid, position, currRP, currPP):
    if checkIfDone(position):
        return 0

    dpString = getDPString(position)
    if dpString in DP:
        return DP[dpString]
    minEnergy = [999999999999]
    for bp in position:
        for p in position[bp]:
            currPos, currState = position[bp][p]
            if currState == "done":
                continue

            if currState == "moved":
                newPos = checkFinalReady(grid, position, bp, p)
                if newPos:
                    newPlacement = (newPos, finalPositions[bp])
                    if checkBlocked(currPos, bp, newPlacement[1], currRP, currPP):
                        npp = deepcopy(currPP)
                        npp.remove(newPlacement)
                        nrp = deepcopy(currRP)
                        nrp.append(currPos[1])
                        np = deepcopy(position)
                        np[bp][p] = (newPlacement, "done")
                        ng = deepcopy(grid)
                        ng[newPos][finalPositions[bp]] = bp
                        ng[currPos[0]][currPos[1]] = '.'
                        energyCost = (abs(newPlacement[0] - currPos[0]) + abs(newPlacement[1] - currPos[1])) * cost[bp]
                        best = solve(ng, np, nrp, npp)
                        # we can return because this is the best decision to make
                        DP[dpString] = best + energyCost
                        return best + energyCost
                continue

            if currState == "start":
                # check if we are starting in the final position. If so, we found the best move and we can return
                if checkFinalStart(grid, position, bp, p):
                    npp = deepcopy(currPP)
                    nrp = deepcopy(currRP)
                    np = deepcopy(position)
                    ng = deepcopy(grid)
                    np[bp][p] = (np[bp][p][0], "done")
                    best = solve(ng, np, nrp, npp)
                    DP[dpString] = best
                    return best

                if currPos[0] != 2:
                    # if the rows above are blocked, we cannot continue with this character
                    tmpres = False
                    for z in range(2, currPos[0]):
                        if (z, currPos[1]) not in currPP:
                            tmpres = True
                            break
                    if tmpres:
                        continue
                for rp in currRP:
                    # if the second leftmost or second rightmost values are blocked, we cannot get to these resting places
                    if rp == 1 and 2 not in currRP:
                        continue
                    if rp == 11 and 10 not in currRP:
                        continue

                    if checkBlocked(currPos, bp, rp, currRP, currPP):
                        npp = deepcopy(currPP)
                        npp.append(currPos)
                        nrp = deepcopy(currRP)
                        nrp.remove(rp)

                        np = deepcopy(position)
                        ng = deepcopy(grid)
                        np[bp][p] = ((1, rp), "moved")
                        ng[1][rp] = bp
                        ng[currPos[0]][currPos[1]] = '.'
                        energyCost = (abs(1 - currPos[0]) + abs(rp - currPos[1])) * cost[bp]
                        best = solve(ng, np, nrp, npp)
                        minEnergy.append(best + energyCost)
    DP[dpString] = min(minEnergy)
    return min(minEnergy)

print(solve(grid, initialPositions, deepcopy(restingPositions), []))

endtime = time()
print(endtime - starttime)