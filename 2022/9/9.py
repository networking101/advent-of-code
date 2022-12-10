from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

size = 500
start = (int(size/2), int(size/2))
head = start
tail = start
grid = []
for y in range(size):
    tmp = ['.'] * size
    grid.append(tmp)
    
grid[start[0]][start[1]] = '#'
grid2 = deepcopy(grid)

def update_tail(h, t):
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
        return t
    if abs(h[0] - t[0]) == 2 and abs(h[1] - t[1]) == 0:
        return (int((h[0]+t[0])/2), t[1])
    if abs(h[0] - t[0]) == 0 and abs(h[1] - t[1]) == 2:
        return (t[0], int((h[1]+t[1])/2))
    if abs(h[0] - t[0]) == 2 and abs(h[1] - t[1]) == 1:
        return (int((h[0]+t[0])/2), h[1])
    if abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) == 2:
        return (h[0], int((h[1]+t[1])/2))
    if abs(h[0] - t[0]) == 2 and abs(h[1] - t[1]) == 2:
        return (int((h[0]+t[0])/2), int((h[1]+t[1])/2))
    assert 1==0

def print_grid(g, h, t):
    for y in range(len(g)):
        for x in range(len(g[y])):
            if h[0] == y and h[1] == x:
                print("H",end='')
            elif t[0] == y and t[1] == x:
                print("T", end='')
            else:
                print(g[y][x], end='')
        print()
    print()

def print_grid2(g, r):
    for y in range(len(g)):
        for x in range(len(g[y])):
            found = False
            for z in r:
                if r[z][0] == y and r[z][1] == x:
                    print(str(z), end='')
                    found = True
                    break
            if not found:
                print(g[y][x], end='')
        print()
    print()

for line in lines:
    dir, steps = line.split()
    for i in range(int(steps)):
        if dir == "U":
            head = (head[0]-1, head[1])
        if dir == "D":
            head = (head[0]+1, head[1])
        if dir == "L":
            head = (head[0], head[1]-1)
        if dir == "R":
            head = (head[0], head[1]+1)
        
        tail = update_tail(head, tail)
        grid[tail[0]][tail[1]] = "#"

tot = 0
for y in grid:
    for x in y:
        if x == "#":
            tot += 1

print(tot)

# Part 2
head = start
rope = {0: head, 1: head, 2: head, 3: head, 4: head, 5: head, 6: head, 7: head, 8: head, 9: head}

for line in lines:
    dir, steps = line.split()
    for i in range(int(steps)):
        if dir == "U":
            head = (head[0]-1, head[1])
        if dir == "D":
            head = (head[0]+1, head[1])
        if dir == "L":
            head = (head[0], head[1]-1)
        if dir == "R":
            head = (head[0], head[1]+1)
        
        rope[0] = head
        for j in range(9):
            rope[j+1] = update_tail(rope[j], rope[j+1])
        
        grid2[rope[9][0]][rope[9][1]] = "#"

tot = 0
for y in grid2:
    for x in y:
        if x == "#":
            tot += 1

print(tot)