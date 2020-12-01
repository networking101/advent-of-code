with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

instructions = []
for line in lines:
    line = line.split(" ")
    first = [int(x) for x in line[-3].split(",")]
    second = [int(x) for x in line[-1].split(",")]

    if line[0] == "turn":
        if line[1] == "off":
            instructions.append([0, first, second])
        if line[1] == "on":
            instructions.append([1, first, second])
    if line[0] == "toggle":
        instructions.append([2, first, second])


size = 1000
grid = []

for i in range(size):
    grid.append([0] * size)


for inst in instructions:
    x1 = inst[1][0]
    y1 = inst[1][1]
    x2 = inst[2][0]
    y2 = inst[2][1]

    print(x1, x2, y1, y2)

    for j in range(y1, y2+1):
        for i in range(x1, x2+1):
            if inst[0] == 0 and grid[j][i] > 0:
                grid[j][i] -= 1
            if inst[0] == 1:
                grid[j][i] += 1
            if inst[0] == 2:
                grid[j][i] = grid[j][i] + 2

print("DEBUG done switching")

sum = 0

for i in range(size):
    for j in range(size):
        sum += grid[i][j]

print(sum)
