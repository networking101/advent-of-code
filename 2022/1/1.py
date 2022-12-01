with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

x = 0
maxVal = []
for line in lines:
    if not line:
        maxVal.append(x)
        x = 0
    else:
        x += int(line)

maxVal.sort(reverse=True)
a, b, c = (maxVal[0], maxVal[1], maxVal[2])
print(a)
print(a + b + c)