with open("text.txt", "r") as fp:
    line = fp.readline().strip()

size = 170
grid = []

for i in range(size):
    grid.append([0] * size)

#for i in range(size):
#    for j in range(size):
#        print(str(grid[i][j]), end="")
#    print("")

#print("\n")

x1 = int(size/2)
y1 = x1
x2 = x1
y2 = y1


grid[y1][x1] += 1

for i in range(len(line)):
    if i % 2 == 0:
        if line[i] == "^":
            y1 -= 1
        if line[i] == "v":
            y1 += 1
        if line[i] == ">":
            x1 += 1
        if line[i] == "<":
            x1 -= 1

        grid[y1][x1] += 1
    else :
        if line[i] == "^":
            y2 -= 1
        if line[i] == "v":
            y2 += 1
        if line[i] == ">":
            x2 += 1
        if line[i] == "<":
            x2 -= 1

        grid[y2][x2] += 1

count = 0

for i in range(size):
    for j in range(size):
        print(str(grid[i][j]), end="")
        if grid[i][j] > 0:
            count += 1
    print("")

print(count)

#print(grid)
