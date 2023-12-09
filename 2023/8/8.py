import math

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

directions = [x for x in lines[0]]
maps = {}

for line in lines[2:]:
    key, rest = line.split(' = ')
    l, r = rest.split(', ')
    l = l[1:]
    r = r[:-1]
    maps[key] = [l, r]

curr_key = "AAA"
d = 0
while curr_key != "ZZZ":
    curr_dir = directions[d%len(directions)]
    if curr_dir == "R":
        curr_key = maps[curr_key][1]
    else:
        curr_key = maps[curr_key][0]
    d += 1

print(d)

d_tot = 1
for k, v in maps.items():
    if k[-1] == "A":
        curr_key = k
        d = 0
        while curr_key[-1] != "Z":
            curr_dir = directions[d%len(directions)]
            if curr_dir == "R":
                curr_key = maps[curr_key][1]
            else:
                curr_key = maps[curr_key][0]
            d += 1
        
        d_tot = abs(d_tot * d) // math.gcd(d_tot, d)

print(d_tot)