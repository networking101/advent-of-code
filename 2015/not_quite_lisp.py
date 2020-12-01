x = 0

with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

print(lines[0])

for i in range(len(lines[0])):
    if lines[0][i] == ')':
        x -= 1
    if lines[0][i] == '(':
        x += 1

    if x == -1:
        print(i + 1)

