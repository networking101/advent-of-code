from typing import final


from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.rstrip() for line in fp]

initialPositions = {}
finalPositions = {'A':[(2,3), (3,3)], 'B':[(2,5), (3,5)], 'C':[(2,7), (3,7)], 'D':[(2,9), (3,9)]}
restingPositions = {(1,1): "open", (1,2): "open", (1,4): "open", (1,6): "open", (1,8): "open", (1,10): "open", (1,11): "open"}
passingPositions = {(2,3): "closed", (2,5): "closed", (2,7): "closed", (2,9): "closed", (3,3): "closed", (3,5): "closed", (3,7): "closed", (3,9): "closed"}
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

itterations = 0
def solve(position, restingPositions, passingPositions, energyCost):
    global finalCost
    global itterations
    if energyCost > finalCost:
        return
    if checkIfDone(position):
        if energyCost < finalCost:
            print("New best:   " + str(energyCost))
            finalCost = energyCost
        itterations += 1
        if itterations%50 == 0:
            print(itterations)
        return
    for bp in position:
        tmp1 = position[bp]
        for p in position[bp]:
            tmp2 = position[bp][p]
            if position[bp][p][1] == "done":
                continue

            if position[bp][p][1] == "moved":
                tmp = finalPositions[bp][1]
                if passingPositions[finalPositions[bp][1]] == "open":
                        npassingPositions = deepcopy(passingPositions)
                        npassingPositions[finalPositions[bp][1]] = "closed"
                        nrestingPositions = deepcopy(restingPositions)
                        nrestingPositions[position[bp][p][0]] = "open"
                        nPositions = deepcopy(position)
                        nPositions[bp][p] = (finalPositions[bp][1], "done")
                        nenergyCost = energyCost + (abs(finalPositions[bp][0][0] - position[bp][p][0][0]) + abs(finalPositions[bp][0][1] - position[bp][p][0][1])) * cost[bp]
                        solve(nPositions, nrestingPositions, npassingPositions, nenergyCost)
                        return
                else:
                    if position[bp][(p+1)%2][1] == "done":
                        if passingPositions[finalPositions[bp][0]] == "open":
                            npassingPositions = deepcopy(passingPositions)
                            npassingPositions[finalPositions[bp][0]] = "closed"
                            nrestingPositions = deepcopy(restingPositions)
                            nrestingPositions[position[bp][p][0]] = "open"
                            nPositions = deepcopy(position)
                            nPositions[bp][p] = (finalPositions[bp][0], "done")
                            nenergyCost = energyCost + (abs(finalPositions[bp][0][0] - position[bp][p][0][0]) + abs(finalPositions[bp][0][1] - position[bp][p][0][1])) * cost[bp]
                            solve(nPositions, nrestingPositions, npassingPositions, nenergyCost)
                            return

            if position[bp][p][1] == "start":
                # top row
                if position[bp][p][0][0] == 3:
                    if passingPositions[(2, position[bp][p][0][1])] == "closed":
                        continue
                for rp in restingPositions:
                    tmp3 = restingPositions[rp]
                    if restingPositions[rp] == "open":
                        if rp[1] == 1 and restingPositions[(1,2)] == "closed":
                            continue
                        if rp[1] == 11 and restingPositions[(1,10)] == "closed":
                            continue

                        #if position[bp][p][0][0] == 2:
                        npassingPositions = deepcopy(passingPositions)
                        npassingPositions[position[bp][p][0]] = "open"
                        nrestingPositions = deepcopy(restingPositions)
                        nrestingPositions[rp] = "closed"

                        nPositions = deepcopy(position)
                        nPositions[bp][p] = ((rp[0], rp[1]), "moved")
                        nenergyCost = energyCost + (abs(rp[0] - position[bp][p][0][0]) + abs(rp[1] - position[bp][p][0][1])) * cost[bp]
                        solve(nPositions, nrestingPositions, npassingPositions, nenergyCost)
    return

solve(initialPositions, restingPositions, passingPositions, 0)

print(finalCost)
print(itterations)