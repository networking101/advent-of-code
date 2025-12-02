import re

with open("input", "r") as fp:
    lines = [line.strip() for line in fp][0]

lines = lines.split(",")

silver = 0
gold = 0

for line in lines:
    s, e = [int(x) for x in line.split("-")]
    for i in range(s, e + 1):
        curr = str(i)
        mid = int(len(curr) / 2)
        if curr[:mid] == curr[mid:]:
            silver += i

        for j in range(len(curr)-1, 0, -1):
            pattern = "^(" + curr[:j] + ")+$"
            if re.match(pattern, curr):
                gold += i
                break

print(silver)
print(gold)