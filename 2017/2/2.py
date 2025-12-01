with open("input", "r") as fp:
    lines = [line.strip() for line in fp]


grid = [[int(index) for index in line.split()] for line in lines]

silver = 0
for line in grid:
    silver += max(line) - min(line)

print(silver)

gold = 0
for line in grid:
    for y, vy in enumerate(line):
        for x, vx in enumerate(line[y:]):
            if max(vx, vy) % min(vx, vy) == 0 and vy != vx:
                print(vy, vx)
                gold += int(max(vx, vy) / min(vx, vy))

print(gold)

# 564 too high