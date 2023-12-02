with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

count1 = 0
count2 = 0

for line in lines:
    check1 = False
    check2 = False
    good = []
    bad = []
    aba = []

    index = 0
    for i, c in enumerate(line):
        if c == '[':
            good.append(line[index:i])
            index = i+1
        if c == ']':
            bad.append(line[index:i])
            index = i+1
    good.append(line[index:len(line)])

    for g in good:
        for i, c in enumerate(g[:-3]):
            if g[i] == g[i+3] and g[i+1] == g[i+2] and g[i] != g[i+1]:
                check1 = True
                break
        for i, c in enumerate(g[:-2]):
            if g[i] == g[i+2] and g[i] != g[i+1]:
                aba.append(g[i:i+3])

    for b in bad:
        for i, c in enumerate(b[:-3]):
            if b[i] == b[i+3] and b[i+1] == b[i+2] and b[i] != b[i+1]:
                check1 = False
                break
        for j in aba:
            reverse = j[1]+j[0]+j[1]
            # print(reverse)
            if reverse in b:
                check2 = True

    if check1:
        count1 += 1
    if check2:
        count2 += 1

print(count1)
print(count2)