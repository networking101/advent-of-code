with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

x = 1
y = 3

steps = [[1,1],[3,1],[5,1],[7,1],[1,2]]

size = len(lines[0])

count = 1


i = 0
j = 0

for k in range(5):
    i = 0
    j = 0
    tc = 0
    y, x = steps[k]
    print(y, x)
    while True:
        if lines[i][j] == "#":
            tc += 1

        if i == len(lines)-1:
            break

        i += x
        j = (j + y) % size

    print(tc)
    count *= tc

print(count)
