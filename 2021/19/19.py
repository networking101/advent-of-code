from math import *

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

scanners = {}
scannersDist = {}

while True:
    scannerNum = int(lines.pop(0).split(" ")[2])
    tmp = {}
    line = lines.pop(0)
    index = 0
    while line and lines:
        tmp[index] = [int(x) for x in line.split(',')]
        line = lines.pop(0)
        index += 1
    if not lines:
        break
    scanners[scannerNum] = tmp
tmp[index] = [int(x) for x in line.split(',')]
scanners[scannerNum] = tmp

for s in scanners:
    distDict = {}
    for c in range(len(scanners[s])):
        for d in range(c+1, len(scanners[s])):
            if c == d:
                continue
            distance = sqrt((abs(scanners[s][c][0]) - abs(scanners[s][d][0]))**2 + (abs(scanners[s][c][1]) - abs(scanners[s][d][1]))**2 + (abs(scanners[s][c][2]) - abs(scanners[s][d][2]))**2)
            distDict[(c, d)] = distance
    scannersDist[s] = distDict

matches = {}
for s1 in range(len(scanners)):
    for s2 in range(s1+1, len(scanners)):
        nmatches = []
        for v1 in scannersDist[s1]:
            for v2 in scannersDist[s2]:
                if scannersDist[s1][v1] == scannersDist[s2][v2]:
                    nmatches.append((v1, v2))
        if len(nmatches) >= 12:
            matches[(s1, s2)] = nmatches

# first scanner is scanner 0.  All positions are fixed to its relative position
for i in range(len(scanners)):
    first = i
    for j in matches:
        if first != j[0]:
            if first != j[1]:
                continue
            else:
                second = j[0]
        else:
            second = j[1]

        scanMatch = matches[j]
        for k in scanMatch:
            if first == j[0]:
                firstBeacon1 = k[0][0]
                firstBeacon2 = k[0][1]
                secondBeacon1 = k[1][0]
                secondBeacon2 = k[1][1]
            else:
                secondBeacon1 = k[0][0]
                secondBeacon2 = k[0][1]
                firstBeacon1 = k[1][0]
                firstBeacon2 = k[1][1]

print("DEBUG")