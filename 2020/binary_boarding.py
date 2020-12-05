with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

res = []

for line in lines:
    r, c = 0, 0
    for i in range(len(line)):
        if line[i] == "B":
            r += 1 << (6-i)
        if line[i] == "R":
            c += 1 << (9-i)

    res.append(r * 8 + c )    


print("Part 1  " + str(max(res)))
print("\n")

for i in range(len(res)):
    if i not in res:
        print("Part 2  " + str(i))
