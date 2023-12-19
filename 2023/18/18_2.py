with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

tot1 = 0
y1 = 0
tot2 = 0
y2 = 0
edge1 = 0
edge2 = 0
for line in lines[::-1]:
    direction, steps, color = line.split()
    steps = int(steps)
    color = color[2:-1]
    if direction == 'U':
        y1 -= steps
    if direction == 'D':
        y1 += steps
    if direction == 'R':
        tot1 += steps * y1
    if direction == 'L':
        tot1 -= steps * y1

    direction = color[-1]
    steps2 = int(color[:-1], 16)
    if direction == '3':
        y2 -= steps2
    if direction == '1':
        y2 += steps2
    if direction == '0':
        tot2 += steps2 * y2
    if direction == '2':
        tot2 -= steps2 * y2

    edge1 += steps
    edge2 += steps2

print(int(abs(tot1) + edge1/2 + 1))
print(int(abs(tot2) + edge2/2 + 1))