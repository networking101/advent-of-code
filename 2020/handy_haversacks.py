with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

data = {}

ans = "silver"
#ans = "gold"

for line in lines:
    line = line.replace("bags", "bag")
    left, right = [x.strip().replace(".", "") for x in line.split("contain")]
    right = right.split(", ")

    data[left] = []
    for i in right:
        t = i.split(" ", 1)
        data[left].append(t)


if ans == "silver":
    found = ["shiny gold bag"]
    index = 0
    while index < len(found):
        for i in data:
            for j in data[i]:
                if j[1] in found and i not in found:
                    found.append(i)
                    break
        index += 1

    found.pop(0)

    print("Silver:  " + str(len(found)))


if ans == "gold":
    found = [["1", "shiny gold bag"]]
    tot = -1
    while found:
        t = found.pop(0)
        try:
            y = int(t[0])
            tot += y
        except:
            pass
        for i in data[t[1]]:
            try:
                x = int(i[0])
            except:
                continue
            found.append([x*y, i[1]])

    print("Gold:  " + str(tot))

