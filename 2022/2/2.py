with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

opp = {"A": 1, "B":2, "C":3}
you = {"X": 1, "Y":2, "Z":3}

score = 0

for line in lines:
    a, b = line.split()
    a = opp[a]
    b = you[b]
    if ((b - a) % 3) == 1:
        score += b + 6
    if ((b - a) % 3) == 2:
        score += b
    if ((b - a) % 3) == 0:
        score += b + 3

print(score)

opp = {"A": 0, "B":1, "C":2}
points = {"X": 0, "Y":3, "Z":6}

score = 0

for line in lines:
    a, b = line.split()
    a = opp[a]
    b = points[b]
    if b == 0:
        score += b + ((a + 2) % 3) + 1
    if b == 3:
        score += b + a + 1
    if b == 6:
        score += b + ((a+1) % 3) + 1

print(score)