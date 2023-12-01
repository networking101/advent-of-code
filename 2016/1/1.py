with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

dist = [0,0]
cur_d = 0
visited = []
v = False

vals = [x.strip() for x in lines[0].split(',')]

for i in vals:
    if i[0] == 'R':
        cur_d = (cur_d + 1) % 4
    else:
        cur_d = (cur_d - 1) % 4

    d = int(i[1:])

    for j in range(d):
        if cur_d == 0:
            dist[0] += 1
        if cur_d == 1:
            dist[1] += 1
        if cur_d == 2:
            dist[0] -= 1
        if cur_d == 3:
            dist[1] -= 1

        if str(dist) in visited:
            if not v:
                print(dist)
                print(abs(dist[0]) + abs(dist[1]))
                v = True
        else:
            visited.append(str(dist))

print(dist)
print(abs(dist[0]) + abs(dist[1]))