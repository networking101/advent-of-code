with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

res = []

for line in lines:
    t = 0
    for i in range(len(line)):
        if line[i] == "B" or line[i] == "R":
            t += 1 << (9-i)
    res.append(t)    

print("Part 1  " + str(max(res)))
print("\n")

for i in range(len(res)):
    if i not in res:
        print("Part 2  " + str(i))
