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
            key = str(c).zfill(2) + str(d).zfill(2)
            distDict[key] = distance
    scannersDist[s] = distDict

matches = {}
for s1 in range(len(scanners)):
    for s2 in range(s1+1, len(scanners)):
        nmatches = []
        for v1 in scannersDist[s1]:
            for v2 in scannersDist[s2]:
                if scannersDist[s1][v1] == scannersDist[s2][v2]:
                    key2 = str(v1).zfill(2) + str(v2).zfill(2)
                    nmatches.append(key2)
        if len(nmatches) >= 12:
            key1 = str(s1).zfill(2) + str(s2).zfill(2)
            matches[key1] = nmatches

# first scanner is scanner 0.  All positions are fixed to its relative position
for i in range(len(scanners)):
    first = str(i).zfill(2)
    for j in matches:
        if first not in j[:2]:
            if first not in j[2:]:
                continue
            else:
                second = j[:2]
        else:
            second = j[2:]

        scanMatch = matches[j]
        for k in scanMatch:
            if first == j[:2]:
                firstBeacon1 = k[:2]
                firstBeacon2 = k[2:4]
                secondBeacon1 = k[4:6]
                secondBeacon2 = k[6:]
            else:
                secondBeacon1 = k[:2]
                secondBeacon2 = k[2:4]
                firstBeacon1 = k[4:6]
                firstBeacon2 = k[6:]

print("DEBUG")