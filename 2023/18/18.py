with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

pos1 = (0, 0)
pos2 = (0, 0)
vectors1 = [pos1]
vectors2 = [pos2]
edge1 = 0
edge2 = 0
for line in lines:
    direction, steps, color = line.split()
    steps = int(steps)
    color = color[2:-1]

    y, x = pos1
    if direction == 'U':
        vectors1.append((y-steps, x))
        pos1 = (y-steps, x)
    if direction == 'D':
        vectors1.append((y+steps, x))
        pos1 = (y+steps, x)
    if direction == 'R':
        vectors1.append((y, x+steps))
        pos1 = (y, x+steps)
    if direction == 'L':
        vectors1.append((y, x-steps))
        pos1 = (y, x-steps)
    edge1 += steps

    direction = color[-1]
    steps = int(color[:-1], 16)
    y, x = pos2
    if direction == '3':
        vectors2.append((y-steps, x))
        pos2 = (y-steps, x)
    if direction == '1':
        vectors2.append((y+steps, x))
        pos2 = (y+steps, x)
    if direction == '0':
        vectors2.append((y, x+steps))
        pos2 = (y, x+steps)
    if direction == '2':
        vectors2.append((y, x-steps))
        pos2 = (y, x-steps)
    edge2 += steps

sum1 = 0
sum2 = 0
for i, v in enumerate(vectors1[:-1]):
    vy, vx = v
    nvy, nvx = vectors1[i+1]
    
    sum1 += vy * nvx
    sum2 += vx * nvy

print(abs(sum1 - sum2)/2 + edge1/2 + 1)

sum1 = 0
sum2 = 0
for i, v in enumerate(vectors2[:-1]):
    vy, vx = v
    nvy, nvx = vectors2[i+1]
    
    sum1 += vy * nvx
    sum2 += vx * nvy

print(abs(sum1 - sum2)/2 + edge2/2 + 1)