from math import *
from collections import Counter

with open("input2", "r") as fp:
    lines = [line.strip() for line in fp]

scanners = {}
num_beacons = 0     # 127
curr = -1
for line in lines:
    if not line:
        continue

    elif 'scanner' in line:
        _, _, num, _ = line.split()
        num = int(num)
        scanners[num] = []
        curr = num
    
    else:
        a, b, c = [int(z) for z in line.split(',')]
        scanners[curr].append((a, b, c))
        num_beacons += 1

all_beacon_pairs = []

for k, v in scanners.items():
    beacon_pairs = []
    for j, y in enumerate(v):
        for i, x in enumerate(v[j+1:]):
            a, b, c = y
            aa, bb, cc = x
            beacon_pairs.append(abs(a - aa) ** 2 + abs(b - bb) ** 2 + abs(c - cc) ** 2)

    all_beacon_pairs.append(beacon_pairs)

count_found = []
count_not_found = 0
for k, v in scanners.items():
    beacon_pairs = []
    for j, y in enumerate(v):
        found = False
        for i, x in enumerate(v[j+1:]):
            a, b, c = y
            aa, bb, cc = x
            test = abs(a - aa) ** 2 + abs(b - bb) ** 2 + abs(c - cc) ** 2

            num_found = 0
            for ii, scan_group in enumerate(all_beacon_pairs):
                if k == ii:
                    continue
                for jj in scan_group:
                    if test == jj:
                        found = True
                        num_found += 1

            if found:
                count_found.append(num_found)
                break
        if not found:
            count_not_found += 1

print(count_found)
print(len(count_found))
tmp = Counter(count_found)
for k, v in tmp.items():
    print(k, v)
print(count_not_found)