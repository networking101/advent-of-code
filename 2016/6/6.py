with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

data = []

for i in lines[0]:
    data.append([])

for line in lines:
    for i, c in enumerate(line):
        data[i].append(c)

solution1 = ''
solution2 = ''

for l in data:
    solution1 += max(set(l), key=l.count)
    solution2 += min(set(l), key=l.count)

print(solution1)
print(solution2)