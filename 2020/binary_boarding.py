with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]


res = []

for line in lines:
    s = 0
    e = 127
    l = 0
    r = 7
    for i in line:
        if i == "F":
            e = int((s+e)/2)
        if i == "B":
            s = int((s+e)/2)
        if i == "R":
            l = int((l+r)/2)
        if i == "L":
            r = int((l+r)/2)

    res.append(e * 8 + r )    


print("Part 1  " + str(max(res)))
print("\n")

for i in range(len(res)):
    if i not in res:
        print("Part 2  " + str(i))
