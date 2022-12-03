with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

total = 0

for line in lines:
    a = line[:int(len(line)/2)]
    b = line[int(len(line)/2):]
    
    for x in a:
        if x in b:
            tmp = ord(x)
            if 65 <= tmp <= 90:
                total += tmp - 38
                break
            if 97 <= tmp <= 122:
                total += tmp - 96
                break

print(total)

total = 0

group = []
tmp2 = []
for i in range(len(lines)):
    tmp2.append(lines[i])
    if i % 3 == 2:
        group.append(tmp2)
        tmp2 = []

for x, y, z in group:
    for i in x:
        if i in y and i in z:
            tmp = ord(i)
            if 65 <= tmp <= 90:
                total += tmp - 38
                break
            if 97 <= tmp <= 122:
                total += tmp - 96
                break

print(total)