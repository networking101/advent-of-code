with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]


x = 10
y = -1
i = 0
j = 0
d = 1
q = 0
for k in lines:
    if k[0] == "F":
        i += x * int(k[1:])
        j += y * int(k[1:])

    if k[0] == "R":
        t = int(k[1:])
        if int(t/90) % 4 == 2:
            nx = -x
            ny = -y
            q = (q + 2) % 4
        if int(t/90) % 4 == 0:
            continue
        if int(t/90) % 4 == 1:
            ny = x
            nx = y*-1
            q = (q + 1) % 4
        if int(t/90) % 4 == 3:
            ny = x*-1
            nx = y
            q = (q + 3) % 4
        y = ny
        x = nx

    if k[0] == "L":
        t = int(k[1:])
        if int(t/90) % 4 == 2:
            nx = -x
            ny = -y
            q = (q - 2) % 4
        if int(t/90) % 4 == 0:
            continue
        if int(t/90) % 4 == 1:
            ny = x*-1
            nx = y
            q = (q - 1) % 4
        if int(t/90) % 4 == 3:
            ny = x
            nx = y*-1
            q = (q - 3) % 4
        y = ny
        x = nx

    if k[0] == "N":
        y -= int(k[1:])

    if k[0] == "E":
        x += int(k[1:])

    if k[0] == "S":
        y += int(k[1:])

    if k[0] == "W":
        x -= int(k[1:])



print(abs(i) + abs(j))
